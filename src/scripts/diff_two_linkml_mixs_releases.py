import ast
import os
import pprint
import re
import logging
import tempfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Tuple, Dict, Optional, Any, Set

import click
import requests
import yaml
from dotenv import load_dotenv
from linkml_runtime.utils.schemaview import SchemaView

# Default repository settings
DEFAULT_OWNER = 'GenomicsStandardsConsortium'
DEFAULT_REPO = 'mixs'

# Approved directories for finding schema files
APPROVED_DIRS = ['model/schema', 'src/mixs/schema', 'src/schema']

# Global configuration
SHOW_YAML_FILES = False  # Set to True to log discovered YAML files
VERBOSE_AUTH = False     # Set to True to log auth message every time
SHOW_ALL_CLASS_NAMES = True  # Set to True to log all class names in diffs
SHOW_ALL_ENUM_NAMES = True  # Set to True to log all enum names in diffs
SHOW_ALL_SLOT_NAMES = True  # Set to True to log all slot names in diffs
API_CALL_COUNT = 0       # Track number of API calls made
AUTH_MESSAGE_PRINTED = False  # Track if auth message was already shown

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

# Load name mappings
CLASS_NAME_MAPPINGS = {}  # Will be loaded from TSV file
ENUM_NAME_MAPPINGS = {}   # Will be loaded from TSV file
SLOT_NAME_MAPPINGS = {}   # Will be loaded from TSV file
SUBSET_NAME_MAPPINGS = {}  # Will be loaded from TSV file
INTER_TYPE_REFACTORING = []  # Will be loaded from TSV file


# ============================================================================
# Systematic LinkML Comparison Framework
# ============================================================================

@dataclass
class ValueComparison:
    """Represents a comparison between two values."""
    old_value: Any
    new_value: Any
    value_type: str  # 'scalar', 'list', 'dict', 'instance'
    differences: List[str]
    
    def has_differences(self) -> bool:
        return len(self.differences) > 0


@dataclass
class KeyComparison:
    """Represents comparison of keys between two dictionaries."""
    only_in_old: Set[str]
    only_in_new: Set[str]
    shared: Set[str]
    expected_mappings: Set[str] = None
    inter_type_refactoring: Set[str] = None


@dataclass
class CollectionComparison:
    """Represents comparison of a collection (dict) with keys and values."""
    key_comparison: KeyComparison
    value_comparisons: Dict[str, ValueComparison]
    
    def has_differences(self) -> bool:
        return (len(self.key_comparison.only_in_old) > 0 or 
                len(self.key_comparison.only_in_new) > 0 or
                any(vc.has_differences() for vc in self.value_comparisons.values()))


@dataclass 
class SchemaComparison:
    """Top-level schema comparison result."""
    old_info: Dict[str, Any]
    new_info: Dict[str, Any] 
    scalar_comparisons: Dict[str, ValueComparison]
    collection_comparisons: Dict[str, CollectionComparison]


class LinkMLComparator:
    """Systematic comparison framework for LinkML schemas following cascading pattern."""
    
    def __init__(self, old_schema: SchemaView, new_schema: SchemaView, 
                 old_info: Dict[str, Any], new_info: Dict[str, Any]):
        self.old_schema = old_schema
        self.new_schema = new_schema
        self.old_info = old_info
        self.new_info = new_info
        
        # Initialize with pattern materialization and class induction
        self._initialize_schemas()
        
        # Load mappings for name change handling
        self.class_mappings = CLASS_NAME_MAPPINGS
        self.enum_mappings = ENUM_NAME_MAPPINGS 
        self.slot_mappings = SLOT_NAME_MAPPINGS
        self.subset_mappings = SUBSET_NAME_MAPPINGS
        self.inter_type_refactoring = INTER_TYPE_REFACTORING
    
    def _initialize_schemas(self):
        """Initialize schemas by materializing patterns and inducing all classes."""
        for i, schema in enumerate([self.old_schema, self.new_schema]):
            schema_label = "OLD" if i == 0 else "NEW"
            try:
                logger.info(f"Materializing patterns for {schema_label} schema...")
                schema.materialize_patterns()
                logger.info(f"Inducing all classes for {schema_label} schema...")
                # Force induction of all classes to use .attributes instead of .slots
                class_names = list(schema.all_classes())
                logger.info(f"Processing {len(class_names)} classes for {schema_label} schema...")
                for j, class_name in enumerate(class_names):
                    if j % 50 == 0:  # Log progress every 50 classes
                        logger.info(f"Induced {j}/{len(class_names)} classes for {schema_label} schema...")
                    schema.induced_class(class_name)
                logger.info(f"Completed {schema_label} schema initialization")
            except Exception as e:
                logger.warning(f"Schema initialization issue for {schema_label} schema ({e})")
    
    def _get_value_type(self, value: Any) -> str:
        """Classify value type for systematic comparison."""
        if value is None or isinstance(value, (str, int, float, bool)):
            return 'scalar'
        elif isinstance(value, (list, tuple)):
            return 'list'
        elif isinstance(value, dict):
            return 'dict'
        else:
            return 'instance'  # LinkML object instance
    
    def _clean_value_for_storage(self, value: Any) -> Any:
        """Clean LinkML types for clean storage in comparison objects."""
        if value is None:
            return None
        
        # Handle basic types
        if isinstance(value, (str, int, float, bool)):
            return value
        
        # Handle collections
        if isinstance(value, (list, tuple)):
            return [self._clean_value_for_storage(v) for v in value]
        
        if isinstance(value, dict):
            return {str(k): self._clean_value_for_storage(v) for k, v in value.items()}
        
        # Handle LinkML object instances with _as_dict method first (most informative)
        if hasattr(value, '_as_dict'):
            try:
                dict_value = value._as_dict
                # For Definition objects, extract just the key information
                if hasattr(value, '__class__') and value.__class__.__name__.endswith('Definition'):
                    # Extract only meaningful fields for Definition objects
                    cleaned_dict = {}
                    important_fields = ['name', 'description', 'title', 'meaning', 'pattern', 'range', 'required', 'multivalued']
                    for field in important_fields:
                        if field in dict_value and dict_value[field] is not None:
                            cleaned_dict[field] = self._clean_value_for_storage(dict_value[field])
                    return cleaned_dict if cleaned_dict else str(value)
                else:
                    # Recursively clean the dictionary for other objects
                    return {str(k): self._clean_value_for_storage(v) for k, v in dict_value.items()}
            except Exception:
                # Fall back to string representation if _as_dict fails
                return str(value)
        
        # Be very aggressive about LinkML object detection and conversion
        if hasattr(value, '__class__'):
            class_name = value.__class__.__name__
            module_name = getattr(value.__class__, '__module__', '')
            
            # Convert ANY object that looks like it could be from LinkML
            if ('linkml' in module_name.lower() or 
                'yamlutils' in module_name.lower() or
                class_name.endswith('Definition') or
                class_name.endswith('Name') or
                'extended_str' in class_name.lower() or
                class_name in {'PermissibleValue', 'Annotation', 'Extension', 'extended_str', 'TypeDefinitionName'} or
                hasattr(value, '_s') or  # YAML mark objects have this attribute
                hasattr(value, '_len')):  # extended_str objects have this
                
                # Just convert to string - all these types support str() conversion
                return str(value)
        
        # Default to string representation for unknown types
        return str(value)
    
    def _compare_scalars(self, old_value: Any, new_value: Any) -> ValueComparison:
        """Compare scalar values."""
        # Clean values immediately before any comparison
        clean_old = self._clean_value_for_storage(old_value)
        clean_new = self._clean_value_for_storage(new_value)
        
        differences = []
        if clean_old != clean_new:
            differences.append(f"{clean_old} vs {clean_new}")
        
        return ValueComparison(
            old_value=clean_old,
            new_value=clean_new, 
            value_type='scalar',
            differences=differences
        )
    
    def _compare_lists(self, old_value: List, new_value: List) -> ValueComparison:
        """Compare list values as sets showing unique elements."""
        differences = []
        
        try:
            old_set = set(old_value) if old_value else set()
            new_set = set(new_value) if new_value else set()
            only_in_old = old_set - new_set
            only_in_new = new_set - old_set
            
            if only_in_old:
                differences.append(f"Only in old: {sorted(only_in_old)}")
            if only_in_new:
                differences.append(f"Only in new: {sorted(only_in_new)}")
                
        except TypeError:
            # Non-hashable items, fall back to length comparison
            if len(old_value) != len(new_value):
                differences.append(f"Length differs: {len(old_value)} vs {len(new_value)}")
        
        # Clean values for storage
        clean_old = self._clean_value_for_storage(old_value)
        clean_new = self._clean_value_for_storage(new_value)
        
        return ValueComparison(
            old_value=clean_old,
            new_value=clean_new,
            value_type='list', 
            differences=differences
        )
    
    def _compare_keys(self, old_keys: Set[str], new_keys: Set[str], 
                     mappings: Dict[str, str] = None) -> KeyComparison:
        """Compare keys between two dictionaries with mapping support."""
        if mappings:
            unique_old, unique_new, expected_mappings = filter_expected_name_changes(
                old_keys, new_keys, mappings
            )
        else:
            unique_old = old_keys - new_keys
            unique_new = new_keys - old_keys  
            expected_mappings = set()
        
        shared = old_keys & new_keys
        
        return KeyComparison(
            only_in_old=unique_old,
            only_in_new=unique_new,
            shared=shared,
            expected_mappings=expected_mappings
        )
    
    def _compare_dict_values(self, old_dict: Dict, new_dict: Dict,
                           mappings: Dict[str, str] = None, 
                           element_type: str = None) -> CollectionComparison:
        """Compare dictionary values following key-first pattern with cascading support."""
        old_keys = set(old_dict.keys()) if old_dict else set()
        new_keys = set(new_dict.keys()) if new_dict else set()
        
        # First compare keys
        key_comparison = self._compare_keys(old_keys, new_keys, mappings)
        
        # Then compare values for shared keys with cascading
        value_comparisons = {}
        
        for key in key_comparison.shared:
            old_val = old_dict.get(key)
            new_val = new_dict.get(key)
            value_comparisons[key] = self._compare_values_with_cascading(
                old_val, new_val, element_type, key
            )
        
        # Also compare mapped values if mappings exist
        if mappings:
            for old_key, new_key in mappings.items():
                if old_key in old_dict and new_key in new_dict:
                    mapped_key = f"{old_key} -> {new_key}"
                    value_comparisons[mapped_key] = self._compare_values_with_cascading(
                        old_dict[old_key], new_dict[new_key], element_type, mapped_key
                    )
        
        return CollectionComparison(
            key_comparison=key_comparison,
            value_comparisons=value_comparisons
        )
    
    def _compare_instances(self, old_instance: Any, new_instance: Any) -> ValueComparison:
        """Compare LinkML object instances using metamodel-guided recursive comparison."""
        differences = []
        
        # Clean instances immediately for storage
        clean_old = self._clean_value_for_storage(old_instance)
        clean_new = self._clean_value_for_storage(new_instance)
        
        if old_instance is None and new_instance is None:
            return ValueComparison(clean_old, clean_new, 'instance', [])
        
        if old_instance is None or new_instance is None:
            differences.append("One instance is None")
            return ValueComparison(clean_old, clean_new, 'instance', differences)
        
        # Try to get the LinkML class type for metamodel-guided comparison
        instance_type = None
        if hasattr(old_instance, '__class__'):
            class_name = old_instance.__class__.__name__
            if class_name.endswith('Definition') or class_name in ['PermissibleValue', 'Annotation']:
                instance_type = class_name
        
        if instance_type:
            # Use metamodel-guided comparison
            field_types = get_element_field_types(instance_type)
            if field_types:
                return self._compare_linkml_instances_with_metamodel(
                    old_instance, new_instance, instance_type, field_types
                )
        
        # Fallback to basic attribute comparison
        return self._compare_instances_fallback(old_instance, new_instance)
    
    def _compare_linkml_instances_with_metamodel(self, old_instance: Any, new_instance: Any, 
                                               instance_type: str, field_types: Dict[str, str]) -> ValueComparison:
        """Compare LinkML instances using metamodel field type information."""
        differences = []
        
        # Compare each field according to its metamodel type
        for field_name, field_type in field_types.items():
            old_val = getattr(old_instance, field_name, None)
            new_val = getattr(new_instance, field_name, None)
            
            # Skip if both are None/empty
            if not is_populated(old_val) and not is_populated(new_val):
                continue
                
            # Skip certain fields that are expected to differ or are not meaningful for comparison
            if field_name in {'name', 'from_schema', '__dict__', '__weakref__'}:
                continue
            
            # Compare based on field type from metamodel
            if field_type == 'scalar':
                if old_val != new_val:
                    differences.append(f"{field_name}: {old_val} vs {new_val}")
                    
            elif field_type == 'list':
                list_comparison = self._compare_lists(old_val or [], new_val or [])
                if list_comparison.has_differences():
                    differences.append(f"{field_name}: {', '.join(list_comparison.differences)}")
                    
            elif field_type == 'dict':
                # For dict fields, we need to recursively compare the nested structure
                dict_comparison = self._compare_dict_values(old_val or {}, new_val or {})
                if dict_comparison.has_differences():
                    # Summarize the dict differences
                    key_comp = dict_comparison.key_comparison
                    summary_parts = []
                    if key_comp.only_in_old:
                        summary_parts.append(f"{len(key_comp.only_in_old)} removed")
                    if key_comp.only_in_new:
                        summary_parts.append(f"{len(key_comp.only_in_new)} added")
                    value_diffs = sum(1 for v in dict_comparison.value_comparisons.values() if v.has_differences())
                    if value_diffs > 0:
                        summary_parts.append(f"{value_diffs} modified")
                    
                    if summary_parts:
                        differences.append(f"{field_name}: {', '.join(summary_parts)}")
        
        # Clean instances for storage
        clean_old = self._clean_value_for_storage(old_instance)
        clean_new = self._clean_value_for_storage(new_instance)
        return ValueComparison(clean_old, clean_new, 'instance', differences)
    
    def _compare_instances_fallback(self, old_instance: Any, new_instance: Any) -> ValueComparison:
        """Fallback comparison for non-LinkML instances or when metamodel is unavailable."""
        differences = []
        
        # Get attributes dynamically, excluding private/internal ones
        old_attrs = set(dir(old_instance)) if old_instance else set()
        new_attrs = set(dir(new_instance)) if new_instance else set()
        
        # Filter attributes - handle None instances safely
        excluded = {attr for attr in (old_attrs | new_attrs)
                   if attr.startswith('_')
                   or (old_instance and callable(getattr(old_instance, attr, None)))
                   or (new_instance and callable(getattr(new_instance, attr, None)))}
        
        all_attrs = (old_attrs | new_attrs) - excluded
        
        for attr in sorted(all_attrs):
            old_val = getattr(old_instance, attr, None)
            new_val = getattr(new_instance, attr, None)
            
            # Only report scalar differences for now (avoid infinite recursion) 
            if old_val != new_val and not isinstance(old_val, (dict, list)) and not isinstance(new_val, (dict, list)):
                differences.append(f"{attr}: {old_val} vs {new_val}")
        
        # Clean instances for storage
        clean_old = self._clean_value_for_storage(old_instance)
        clean_new = self._clean_value_for_storage(new_instance)
        return ValueComparison(clean_old, clean_new, 'instance', differences)
    
    def _compare_values(self, old_value: Any, new_value: Any) -> ValueComparison:
        """Main value comparison dispatcher following systematic pattern."""
        old_type = self._get_value_type(old_value)
        new_type = self._get_value_type(new_value)
        
        # Handle type mismatches
        if old_type != new_type:
            return ValueComparison(
                old_value=self._clean_value_for_storage(old_value),
                new_value=self._clean_value_for_storage(new_value),
                value_type='mixed',
                differences=[f"Type mismatch: {old_type} vs {new_type}"]
            )
        
        # Dispatch to appropriate comparison method
        if old_type == 'scalar':
            return self._compare_scalars(old_value, new_value)
        elif old_type == 'list':
            return self._compare_lists(old_value, new_value)
        elif old_type == 'dict':
            # For dict comparison, we need to wrap the CollectionComparison in a ValueComparison
            dict_comparison = self._compare_dict_values(old_value, new_value)
            return ValueComparison(
                old_value=self._clean_value_for_storage(old_value),
                new_value=self._clean_value_for_storage(new_value),
                value_type='dict',
                differences=["Dict comparison completed"] if dict_comparison.has_differences() else []
            )
        elif old_type == 'instance':
            return self._compare_instances(old_value, new_value)
        else:
            return ValueComparison(
                old_value=self._clean_value_for_storage(old_value), 
                new_value=self._clean_value_for_storage(new_value), 
                value_type=old_type, 
                differences=["Unknown type"]
            )

    def _compare_values_with_cascading(self, old_value: Any, new_value: Any, 
                                     element_type: str = None, element_key: str = None) -> ValueComparison:
        """Enhanced value comparison with cascading support for specific LinkML element types."""
        # First do standard comparison
        base_comparison = self._compare_values(old_value, new_value)
        
        # If both values are LinkML instances, apply cascading comparisons
        if (base_comparison.value_type == 'instance' and 
            old_value is not None and new_value is not None):
            
            # Apply cascading based on element type
            if element_type == 'enums':
                # Cascade to compare permissible_values
                cascaded = self._cascade_enum_comparison(element_key, old_value, new_value)
                if cascaded:
                    # Merge cascading differences into base comparison
                    base_comparison.differences.extend([f"Cascaded: {diff}" for diff in cascaded])
            
            elif element_type == 'classes':
                # Cascade to compare attributes using induced classes
                cascaded = self._cascade_class_comparison(element_key, old_value, new_value)
                if cascaded:
                    # Merge cascading differences into base comparison
                    base_comparison.differences.extend([f"Cascaded: {diff}" for diff in cascaded])
        
        return base_comparison
    
    def _cascade_enum_comparison(self, enum_name: str, old_enum: Any, new_enum: Any) -> List[str]:
        """Cascade down to compare enum permissible_values following the same pattern."""
        differences = []
        
        # Check if enums have permissible_values to compare
        old_pv = getattr(old_enum, 'permissible_values', None) or {}
        new_pv = getattr(new_enum, 'permissible_values', None) or {}
        
        if old_pv or new_pv:
            pv_comparison = self._compare_dict_values(old_pv, new_pv, element_type='permissible_values')
            if pv_comparison.has_differences():
                # Extract key difference summary
                key_comp = pv_comparison.key_comparison
                if key_comp.only_in_old:
                    differences.append(f"permissible_values only in old: {len(key_comp.only_in_old)} values")
                if key_comp.only_in_new:
                    differences.append(f"permissible_values only in new: {len(key_comp.only_in_new)} values")
                
                # Value differences
                value_diffs = sum(1 for v in pv_comparison.value_comparisons.values() if v.has_differences())
                if value_diffs > 0:
                    differences.append(f"permissible_values definition changes: {value_diffs} values")
        
        return differences
    
    def _cascade_class_comparison(self, class_name: str, old_class: Any, new_class: Any) -> List[str]:
        """Cascade down to compare class attributes following the same pattern using induced classes with enhanced SchemaView methods."""
        differences = []
        
        # Always use induced classes to get .attributes instead of .slots
        try:
            old_induced = self.old_schema.induced_class(class_name) if class_name in self.old_schema.all_classes() else old_class
            new_induced = self.new_schema.induced_class(class_name) if class_name in self.new_schema.all_classes() else new_class
            
            # Use SchemaView's class_slots method for more comprehensive slot analysis
            old_class_slots = {}
            new_class_slots = {}
            
            # Get slots using SchemaView methods if available
            try:
                if class_name in self.old_schema.all_classes():
                    old_slot_names = self.old_schema.class_slots(class_name)
                    old_class_slots = {slot_name: self.old_schema.induced_slot(slot_name, class_name) 
                                     for slot_name in old_slot_names}
            except Exception:
                # Fall back to direct attributes if class_slots fails
                old_class_slots = getattr(old_induced, 'attributes', {}) or {}
            
            try:
                if class_name in self.new_schema.all_classes():
                    new_slot_names = self.new_schema.class_slots(class_name)
                    new_class_slots = {slot_name: self.new_schema.induced_slot(slot_name, class_name)
                                     for slot_name in new_slot_names}
            except Exception:
                # Fall back to direct attributes if class_slots fails
                new_class_slots = getattr(new_induced, 'attributes', {}) or {}
            
            # Compare class slots/attributes
            if old_class_slots or new_class_slots:
                attrs_comparison = self._compare_dict_values(old_class_slots, new_class_slots, 
                                                           self.slot_mappings, 'class_slots')
                if attrs_comparison.has_differences():
                    # Extract key difference summary
                    key_comp = attrs_comparison.key_comparison
                    if key_comp.only_in_old:
                        differences.append(f"slots only in old: {len(key_comp.only_in_old)} slots")
                    if key_comp.only_in_new:
                        differences.append(f"slots only in new: {len(key_comp.only_in_new)} slots")
                    if key_comp.expected_mappings:
                        differences.append(f"expected slot mappings: {len(key_comp.expected_mappings)} mappings")
                    
                    # Value differences
                    value_diffs = sum(1 for v in attrs_comparison.value_comparisons.values() if v.has_differences())
                    if value_diffs > 0:
                        differences.append(f"slot definition changes: {value_diffs} slots")
            
            # Also compare inheritance hierarchies if available
            try:
                old_ancestors = set(self.old_schema.class_ancestors(class_name)) if class_name in self.old_schema.all_classes() else set()
                new_ancestors = set(self.new_schema.class_ancestors(class_name)) if class_name in self.new_schema.all_classes() else set()
                
                if old_ancestors != new_ancestors:
                    ancestor_only_old = old_ancestors - new_ancestors
                    ancestor_only_new = new_ancestors - old_ancestors
                    if ancestor_only_old:
                        differences.append(f"ancestors only in old: {len(ancestor_only_old)} ancestors")
                    if ancestor_only_new:
                        differences.append(f"ancestors only in new: {len(ancestor_only_new)} ancestors")
                        
            except Exception:
                # Ancestor comparison is optional, don't fail if not available
                pass
            
        except Exception as e:
            differences.append(f"Error cascading class comparison for {class_name}: {e}")
        
        return differences
    
    def compare_schemas(self) -> SchemaComparison:
        """Main schema comparison following cascading pattern."""
        # Get populated top-level keys
        old_keys = populated_top_level_keys(self.old_schema)
        new_keys = populated_top_level_keys(self.new_schema)
        
        scalar_comparisons = {}
        collection_comparisons = {}
        
        # Helper to get value for a key 
        def get_key_value(schema_view: SchemaView, key: str):
            # First try raw schema
            schema_dict = schema_view.schema._as_dict
            if key in schema_dict and is_populated(schema_dict[key]):
                # Clean the value immediately when retrieving from schema
                return self._clean_value_for_storage(schema_dict[key])
            
            # Use metamodel-discovered collections  
            schema_collections = get_metamodel_schema_collections()
            if key in schema_collections:
                try:
                    method_name = schema_collections[key]
                    method = getattr(schema_view, method_name)
                    value = method(imports=True)
                    # Clean the value immediately when retrieving from schema
                    return self._clean_value_for_storage(value)
                except (AttributeError, TypeError):
                    return None
            return None
        
        # Compare all keys present in either schema
        all_keys = old_keys | new_keys
        
        for key in sorted(all_keys):
            old_value = get_key_value(self.old_schema, key) if key in old_keys else None
            new_value = get_key_value(self.new_schema, key) if key in new_keys else None
            
            # Skip if both are empty/None
            if not is_populated(old_value) and not is_populated(new_value):
                continue
            
            value_type = self._get_value_type(old_value) if old_value is not None else self._get_value_type(new_value)
            
            if value_type == 'dict':
                # Use specialized comparison for schema collections 
                mappings = None
                if key == 'classes':
                    mappings = self.class_mappings
                elif key == 'enums':
                    mappings = self.enum_mappings
                elif key == 'slots':
                    mappings = self.slot_mappings
                elif key == 'subsets':
                    mappings = self.subset_mappings
                
                collection_comparisons[key] = self._compare_dict_values(
                    old_value or {}, new_value or {}, mappings, key
                )
            else:
                # Scalar or list comparison
                scalar_comparisons[key] = self._compare_values(old_value, new_value)
        
        return SchemaComparison(
            old_info=self.old_info,
            new_info=self.new_info,
            scalar_comparisons=scalar_comparisons,
            collection_comparisons=collection_comparisons
        )


def schema_comparison_to_dict(comparison: SchemaComparison) -> dict:
    """Convert a SchemaComparison to a structured dictionary for YAML output."""

    old_tag = comparison.old_info.get('tag', 'old')
    new_tag = comparison.new_info.get('tag', 'new')

    def clean_value(value: Any) -> Any:
        """Recursively convert linkml-runtime specific types to basic python types."""
        if value is None:
            return None
        
        # Handle basic types first
        if isinstance(value, (str, int, float, bool)):
            return value
        
        # Handle collections
        if isinstance(value, (list, tuple)):
            return [clean_value(v) for v in value]
        
        if isinstance(value, dict):
            return {str(k): clean_value(v) for k, v in value.items()}
        
        # Handle LinkML specific types - be more aggressive about string conversion
        if hasattr(value, '__class__'):
            class_name = value.__class__.__name__
            module_name = getattr(value.__class__, '__module__', '')
            
            # Convert all LinkML types to strings - they can all be cast to plain strings
            if ('linkml' in module_name or 
                'yamlutils' in module_name or
                class_name.endswith('Definition') or
                class_name.endswith('Name') or
                class_name in {'PermissibleValue', 'Annotation', 'Extension', 'extended_str', 'TypeDefinitionName'}):
                
                # Just cast to string - all these types support str() conversion
                return str(value)
        
        # Handle LinkML object instances with _as_dict method
        if hasattr(value, '_as_dict'):
            try:
                dict_value = value._as_dict
                # Recursively clean the dictionary
                return {str(k): clean_value(v) for k, v in dict_value.items()}
            except Exception:
                # Fall back to string representation if _as_dict fails
                return str(value)
        
        # Default to string representation for unknown types
        return str(value)

    def clean_key(key: Any) -> str:
        """Convert keys to clean strings, handling LinkML types."""
        if hasattr(key, '__class__') and 'linkml' in str(key.__class__):
            return str(key)
        return str(key)

    def value_comparison_to_dict(value_comp: ValueComparison) -> dict:
        """Convert a ValueComparison to a dictionary, only showing fields that actually differ."""
        # For list comparisons, show set differences instead of full lists
        if value_comp.value_type == 'list' and value_comp.differences:
            result = {}
            for diff in value_comp.differences:
                if diff.startswith("Only in old: "):
                    # Use ast.literal_eval for safe parsing instead of eval
                    result['only_in_old'] = ast.literal_eval(diff.replace("Only in old: ", ""))
                elif diff.startswith("Only in new: "):
                    result['only_in_new'] = ast.literal_eval(diff.replace("Only in new: ", ""))
            # Clean the extracted values
            if 'only_in_old' in result:
                result['only_in_old'] = clean_value(result['only_in_old'])
            if 'only_in_new' in result:
                result['only_in_new'] = clean_value(result['only_in_new'])
            return result
        else:
            # For scalar and other types, only show values if they actually differ
            clean_old = clean_value(value_comp.old_value)
            clean_new = clean_value(value_comp.new_value)
            
            # If both values are the same, don't include them in the output
            if clean_old == clean_new:
                return {}
            
            # Only show differing values
            result = {}
            if clean_old is not None:
                result[old_tag] = clean_old
            if clean_new is not None:
                result[new_tag] = clean_new
            return result

    def key_comparison_to_dict(key_comp: KeyComparison) -> dict:
        """Convert a KeyComparison to a dictionary."""
        result = {}
        
        if key_comp.only_in_old:
            result['only_in_old'] = sorted([clean_key(k) for k in key_comp.only_in_old])
        if key_comp.only_in_new:
            result['only_in_new'] = sorted([clean_key(k) for k in key_comp.only_in_new])
        if key_comp.shared:
            result['shared'] = sorted([clean_key(k) for k in key_comp.shared])
        if key_comp.expected_mappings:
            result['expected_mappings'] = sorted(list(key_comp.expected_mappings))
            
        return result

    def collection_comparison_to_dict(coll_comp: CollectionComparison) -> dict:
        """Convert a CollectionComparison to a dictionary."""
        # For collections, we still want to see the key comparison info
        result = {
            'key_comparison': key_comparison_to_dict(coll_comp.key_comparison)
        }
        
        # Add definition changes with cleaned keys, but only include non-empty comparisons
        definition_changes = {}
        for k, v in coll_comp.value_comparisons.items():
            if v.has_differences():
                clean_k = clean_key(k)
                value_dict = value_comparison_to_dict(v)
                # Only include if the value dictionary is not empty
                if value_dict:
                    definition_changes[clean_k] = value_dict
        
        if definition_changes:
            result['definition_changes'] = definition_changes
            
        return result

    # Build the complete comparison dictionary with cleaned keys
    collection_differences = {}
    for k, v in comparison.collection_comparisons.items():
        if v.has_differences():
            clean_k = clean_key(k)
            collection_differences[clean_k] = collection_comparison_to_dict(v)

    result = {
        'comparison_metadata': {
            'old_schema': {
                'tag': comparison.old_info['tag'],
                'date': comparison.old_info['date'],
                'commit_sha': comparison.old_info.get('commit_sha', 'unknown')
            },
            'new_schema': {
                'tag': comparison.new_info['tag'],
                'date': comparison.new_info['date'],
                'commit_sha': comparison.new_info.get('commit_sha', 'unknown')
            },
            'comparison_timestamp': datetime.now().isoformat()
        },
        'scalar_differences': {
            clean_key(k): value_comparison_to_dict(v)
            for k, v in comparison.scalar_comparisons.items()
            if v.has_differences()
        },
        'collection_differences': collection_differences
    }

    return result


def print_schema_comparison_report(comparison: SchemaComparison) -> None:
    """Print a structured report of the schema comparison results."""
    print("\n" + "=" * 80)
    print("SYSTEMATIC LINKML SCHEMA COMPARISON REPORT")
    print("=" * 80)
    
    print(f"\nComparing:")
    print(f"  OLD: {comparison.old_info['tag']} ({comparison.old_info['date']})")  
    print(f"  NEW: {comparison.new_info['tag']} ({comparison.new_info['date']})")
    
    # Report scalar differences
    if comparison.scalar_comparisons:
        print(f"\n🔢 SCALAR VALUE DIFFERENCES ({len(comparison.scalar_comparisons)} keys)")
        print("-" * 50)
        
        for key, value_comp in sorted(comparison.scalar_comparisons.items()):
            if value_comp.has_differences():
                print(f"  {key}:")
                if value_comp.value_type == 'mixed':
                    print(f"    Type mismatch: {type(value_comp.old_value).__name__} vs {type(value_comp.new_value).__name__}")
                elif value_comp.value_type == 'list':
                    for diff in value_comp.differences:
                        print(f"    {diff}")
                else:
                    print(f"    OLD: {value_comp.old_value}")
                    print(f"    NEW: {value_comp.new_value}")
    
    # Report collection differences
    if comparison.collection_comparisons:
        print(f"\n📚 COLLECTION DIFFERENCES ({len(comparison.collection_comparisons)} collections)")
        print("-" * 50)
        
        for key, collection_comp in sorted(comparison.collection_comparisons.items()):
            if collection_comp.has_differences():
                print(f"\n  📁 {key.upper()}:")
                
                # Key differences
                key_comp = collection_comp.key_comparison
                if key_comp.only_in_old or key_comp.only_in_new:
                    print(f"    Key differences:")
                    
                    if key_comp.only_in_old:
                        print(f"      ➖ Only in OLD ({len(key_comp.only_in_old)}): {sorted(list(key_comp.only_in_old))[:5]}{'...' if len(key_comp.only_in_old) > 5 else ''}")
                    
                    if key_comp.only_in_new:
                        print(f"      ➕ Only in NEW ({len(key_comp.only_in_new)}): {sorted(list(key_comp.only_in_new))[:5]}{'...' if len(key_comp.only_in_new) > 5 else ''}")
                
                if key_comp.expected_mappings:
                    print(f"    Expected mappings ({len(key_comp.expected_mappings)}): {sorted(list(key_comp.expected_mappings))[:3]}{'...' if len(key_comp.expected_mappings) > 3 else ''}")
                
                # Value differences for shared/mapped keys
                value_diffs = [(k, v) for k, v in collection_comp.value_comparisons.items() if v.has_differences()]
                if value_diffs:
                    print(f"    Element definition changes ({len(value_diffs)} elements):")
                    for elem_key, value_comp in value_diffs[:5]:  # Show first 5
                        if value_comp.value_type == 'instance' and value_comp.differences:
                            print(f"      🔧 {elem_key}: {', '.join(value_comp.differences[:2])}{'...' if len(value_comp.differences) > 2 else ''}")
                    
                    if len(value_diffs) > 5:
                        print(f"      ... and {len(value_diffs) - 5} more elements with differences")
            
            else:
                print(f"  ✅ {key}: No differences detected")
    
    # Summary
    total_diffs = sum(1 for v in comparison.scalar_comparisons.values() if v.has_differences())
    total_collection_diffs = sum(1 for v in comparison.collection_comparisons.values() if v.has_differences())
    
    print(f"\n📊 SUMMARY:")
    print(f"  • Scalar differences: {total_diffs}/{len(comparison.scalar_comparisons)} keys")
    print(f"  • Collection differences: {total_collection_diffs}/{len(comparison.collection_comparisons)} collections")
    print(f"  • Total schema elements compared: {sum(len(comp.key_comparison.shared) + len(comp.key_comparison.only_in_old) + len(comp.key_comparison.only_in_new) for comp in comparison.collection_comparisons.values())}")


def cascade_enum_comparisons(comparator: LinkMLComparator, enum_name: str, old_enum: Any, new_enum: Any) -> Dict[str, CollectionComparison]:
    """Cascade down to compare enum permissible_values following the same pattern."""
    cascaded_comparisons = {}
    
    # Check if enums have permissible_values to compare
    old_pv = getattr(old_enum, 'permissible_values', None) or {}
    new_pv = getattr(new_enum, 'permissible_values', None) or {}
    
    if old_pv or new_pv:
        cascaded_comparisons['permissible_values'] = comparator._compare_dict_values(old_pv, new_pv)
    
    return cascaded_comparisons


def cascade_class_comparisons(comparator: LinkMLComparator, class_name: str, old_class: Any, new_class: Any) -> Dict[str, CollectionComparison]:
    """Cascade down to compare class attributes following the same pattern."""
    cascaded_comparisons = {}
    
    # Always use induced classes to get .attributes instead of .slots
    try:
        old_induced = comparator.old_schema.induced_class(class_name) if class_name in comparator.old_schema.all_classes() else old_class
        new_induced = comparator.new_schema.induced_class(class_name) if class_name in comparator.new_schema.all_classes() else new_class
        
        old_attrs = getattr(old_induced, 'attributes', {}) or {}
        new_attrs = getattr(new_induced, 'attributes', {}) or {}
        
        if old_attrs or new_attrs:
            cascaded_comparisons['attributes'] = comparator._compare_dict_values(old_attrs, new_attrs)
        
    except Exception as e:
        print(f"Warning: Could not cascade class comparison for {class_name}: {e}")
    
    return cascaded_comparisons


def load_class_name_mappings(mappings_dir: Path) -> Dict[str, str]:
    """Load class name mappings from TSV file."""
    mappings = {}
    mapping_file = mappings_dir / 'class_name_mappings.tsv'
    
    if not mapping_file.exists():
        logger.warning(f"Class name mapping file not found: {mapping_file}")
        return mappings
    
    try:
        with open(mapping_file, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i == 0:  # Skip header
                    continue
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    old_name, new_name = parts
                    mappings[old_name] = new_name
        logger.info(f"Loaded {len(mappings)} class name mappings")
    except Exception as e:
        logger.error(f"Could not load class name mappings: {e}")
    
    return mappings


def load_enum_name_mappings(mappings_dir: Path) -> Dict[str, str]:
    """Load enum name mappings from TSV file."""
    mappings = {}
    mapping_file = mappings_dir / 'enum_name_mappings.tsv'
    
    if not mapping_file.exists():
        logger.warning(f"Enum name mapping file not found: {mapping_file}")
        return mappings
    
    try:
        with open(mapping_file, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i == 0:  # Skip header
                    continue
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    old_name, new_name = parts
                    mappings[old_name] = new_name
        logger.info(f"Loaded {len(mappings)} enum name mappings")
    except Exception as e:
        logger.error(f"Could not load enum name mappings: {e}")
    
    return mappings


def load_slot_name_mappings(mappings_dir: Path) -> Dict[str, str]:
    """Load slot name mappings from TSV file."""
    mappings = {}
    mapping_file = mappings_dir / 'slot_name_mappings.tsv'
    
    if not mapping_file.exists():
        logger.warning(f"Slot name mapping file not found: {mapping_file}")
        return mappings
    
    try:
        with open(mapping_file, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i == 0:  # Skip header
                    continue
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    old_name, new_name = parts
                    mappings[old_name] = new_name
        logger.info(f"Loaded {len(mappings)} slot name mappings")
    except Exception as e:
        logger.error(f"Could not load slot name mappings: {e}")
    
    return mappings


def load_subset_name_mappings(mappings_dir: Path) -> Dict[str, str]:
    """Load subset name mappings from TSV file."""
    mappings = {}
    mapping_file = mappings_dir / 'subset_name_mappings.tsv'
    
    if not mapping_file.exists():
        logger.warning(f"Subset name mapping file not found: {mapping_file}")
        return mappings
    
    try:
        with open(mapping_file, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i == 0:  # Skip header
                    continue
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    old_name, new_name = parts
                    mappings[old_name] = new_name
        logger.info(f"Loaded {len(mappings)} subset name mappings")
    except Exception as e:
        logger.error(f"Could not load subset name mappings: {e}")
    
    return mappings


def parse_schema_spec(spec: str) -> Tuple[str, str, str, str]:
    """Parse schema specification in format owner/repo@commit:path.
    
    Args:
        spec: Schema specification string.
        
    Returns:
        Tuple of (owner, repo, commit, path).
        
    Raises:
        ValueError: If specification format is invalid.
    """
    try:
        # Split on '@' to separate owner/repo from commit:path
        if '@' not in spec:
            raise ValueError("Missing '@' separator")
        
        owner_repo, commit_path = spec.split('@', 1)
        
        # Split owner_repo on '/'
        if '/' not in owner_repo:
            raise ValueError("Missing '/' separator in owner/repo")
        
        owner, repo = owner_repo.split('/', 1)
        
        # Split commit_path on ':'
        if ':' not in commit_path:
            raise ValueError("Missing ':' separator in commit:path")
        
        commit, path = commit_path.split(':', 1)
        
        return owner, repo, commit, path
        
    except Exception as e:
        raise ValueError(f"Invalid schema specification '{spec}': {e}")


def load_inter_type_refactoring(mappings_dir: Path) -> List[Tuple[str, str, str, str]]:
    """Load inter-type refactoring mappings from TSV file."""
    mappings = []
    mapping_file = mappings_dir / 'inter_type_refactoring.tsv'
    
    if not mapping_file.exists():
        logger.warning(f"Inter-type refactoring file not found: {mapping_file}")
        return mappings
    
    try:
        with open(mapping_file, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i == 0:  # Skip header
                    continue
                parts = line.strip().split('\t')
                if len(parts) >= 4:
                    old_type, old_name, new_type, new_name = parts[0], parts[1], parts[2], parts[3]
                    if old_type and old_name and new_type and new_name:
                        mappings.append((old_type, old_name, new_type, new_name))
        logger.info(f"Loaded {len(mappings)} inter-type refactoring mappings")
    except Exception as e:
        logger.error(f"Could not load inter-type refactoring mappings: {e}")
    
    return mappings


def filter_expected_name_changes(old_keys: Set[str], new_keys: Set[str], mappings: Dict[str, str]) -> Tuple[Set[str], Set[str], Set[str]]:
    """Filter out expected name changes based on mappings.
    
    Returns:
        Tuple of (unique_old, unique_new, expected_mappings)
    """
    unique_old = set()
    unique_new = set()
    expected_mappings = set()
    
    # Track which new keys have been accounted for
    accounted_new_keys = set()
    
    for old_key in old_keys:
        if old_key in mappings:
            expected_new_key = mappings[old_key]
            if expected_new_key in new_keys:
                # This is an expected mapping
                expected_mappings.add(f"{old_key} -> {expected_new_key}")
                accounted_new_keys.add(expected_new_key)
            else:
                # Expected mapping but new key not found
                unique_old.add(old_key)
        else:
            # No mapping for this old key - check if it exists unchanged in new keys
            if old_key in new_keys:
                # Key exists unchanged in both schemas
                accounted_new_keys.add(old_key)
            else:
                # Key only exists in old schema
                unique_old.add(old_key)
    
    # Any new keys not accounted for are unique
    unique_new = new_keys - accounted_new_keys
    
    return unique_old, unique_new, expected_mappings


def filter_inter_type_refactoring(element_type: str, only_in_old: Set[str], only_in_new: Set[str], 
                                 inter_type_mappings: List[Tuple[str, str, str, str]]) -> Tuple[Set[str], Set[str], Set[str]]:
    """Filter out expected inter-type refactoring from unique element lists.
    
    Args:
        element_type: Type of element being checked ('slot', 'subset', 'class', 'enum')
        only_in_old: Set of elements only found in old schema
        only_in_new: Set of elements only found in new schema
        inter_type_mappings: List of (old_type, old_name, new_type, new_name) tuples
        
    Returns:
        Tuple of (filtered_old, filtered_new, refactoring_found)
    """
    filtered_old = only_in_old.copy()
    filtered_new = only_in_new.copy()
    refactoring_found = set()
    
    for old_type, old_name, new_type, new_name in inter_type_mappings:
        # If this element type appears as old_type in refactoring, remove from only_in_old
        if old_type == element_type and old_name in only_in_old:
            filtered_old.discard(old_name)
            refactoring_found.add(f"{old_type}:{old_name} -> {new_type}:{new_name}")
        
        # If this element type appears as new_type in refactoring, remove from only_in_new  
        if new_type == element_type and new_name in only_in_new:
            filtered_new.discard(new_name)
            refactoring_found.add(f"{old_type}:{old_name} -> {new_type}:{new_name}")
    
    return filtered_old, filtered_new, refactoring_found


def is_populated(value: Any) -> bool:
    """Check if a value is populated using recursive analysis.
    
    This function performs robust checking of scalars, lists, dicts, and LinkML objects
    to determine if they contain meaningful content.
    
    Args:
        value: Value to check for populated status.
        
    Returns:
        True if value is populated, False if it's None, empty, or effectively empty.
    """
    if value is None:
        return False
    if isinstance(value, str) and value.strip() == "":
        return False
    if isinstance(value, (list, tuple)):
        return any(is_populated(v) for v in value)
    if isinstance(value, dict):
        return any(is_populated(v) for v in value.values())
    return True  # number, bool, LinkML objects, etc.


# Global metamodel schema view - loaded once and reused
_METAMODEL_SCHEMA_VIEW = None

def get_linkml_metamodel() -> SchemaView:
    """Get LinkML metamodel SchemaView with imports merged.
    
    Returns:
        SchemaView of the LinkML metamodel with all imports resolved.
    """
    global _METAMODEL_SCHEMA_VIEW
    
    if _METAMODEL_SCHEMA_VIEW is None:
        temp_path = None
        try:
            logger.info("Loading LinkML metamodel from GitHub...")
            metamodel_url = "https://raw.githubusercontent.com/linkml/linkml-model/refs/heads/main/linkml_model/model/schema/meta.yaml"

            # Download and cache the metamodel
            with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
                response = requests.get(metamodel_url, timeout=30)
                response.raise_for_status()
                f.write(response.text)
                temp_path = f.name

            # Create SchemaView with imports merged
            _METAMODEL_SCHEMA_VIEW = SchemaView(temp_path)
            logger.info("Successfully loaded LinkML metamodel")

        except Exception as e:
            logger.error(f"Failed to load LinkML metamodel: {e}")
            raise RuntimeError(f"Cannot proceed without metamodel: {e}")
        finally:
            # Clean up temp file even if exception occurred
            if temp_path and os.path.exists(temp_path):
                os.unlink(temp_path)
    
    return _METAMODEL_SCHEMA_VIEW


def get_element_field_types(element_class_name: str) -> Dict[str, str]:
    """Get field types for a LinkML element using the metamodel.
    
    Args:
        element_class_name: Name of the LinkML class (e.g., 'ClassDefinition', 'SlotDefinition')
        
    Returns:
        Dict mapping field names to their types ('scalar', 'list', 'dict')
    """
    metamodel = get_linkml_metamodel()
    
    try:
        # Get the induced class definition
        element_class = metamodel.induced_class(element_class_name)
        field_types = {}
        
        for field_name, slot_def in element_class.attributes.items():
            # Determine if this is a scalar, list, or dict field
            if slot_def.multivalued:
                if slot_def.inlined_as_list:
                    field_types[field_name] = 'list'
                else:
                    field_types[field_name] = 'dict'  # multivalued but not inlined_as_list = dict
            else:
                field_types[field_name] = 'scalar'
                
        return field_types
        
    except Exception as e:
        logger.warning(f"Could not get field types for {element_class_name}: {e}")
        return {}


def get_metamodel_schema_collections() -> Dict[str, str]:
    """Get schema collections from LinkML metamodel dynamically.
    
    Returns:
        Dict mapping slot names to their corresponding all_* method names.
    """
    try:
        metamodel = get_linkml_metamodel()
        
        # Induce the schema_definition class to get its full attribute structure
        schema_def_class = metamodel.induced_class('SchemaDefinition')
        
        # Map known collection slots to their SchemaView methods
        collection_methods = {
            'classes': 'all_classes',
            'slots': 'all_slots', 
            'slot_definitions': 'all_slots',  # alias for slots
            'enums': 'all_enums',
            'types': 'all_types', 
            'subsets': 'all_subsets',
        }
        
        # Filter to only include slots that are actually defined in schema_definition
        schema_collections = {}
        for slot_name in schema_def_class.attributes:
            if slot_name in collection_methods:
                schema_collections[slot_name] = collection_methods[slot_name]
                
        return schema_collections
        
    except Exception as e:
        # Fallback to hardcoded collections if metamodel loading fails
        logger.warning(f"Could not load metamodel ({e}), using fallback collections")
        return {
            'classes': 'all_classes',
            'slots': 'all_slots',
            'enums': 'all_enums',
            'types': 'all_types',
            'subsets': 'all_subsets',
        }


def populated_top_level_keys(schema_view: SchemaView) -> Set[str]:
    """Extract top-level keys from a SchemaView that have populated values.
    
    Uses the LinkML metamodel to dynamically discover what collections should exist
    in a SchemaDefinition, then checks both raw schema attributes and resolved
    collections via all_* methods.
    
    Args:
        schema_view: SchemaView instance to analyze.
        
    Returns:
        Set of top-level keys whose values are populated.
    """
    keys = set()
    
    # Ensure schema classes are induced before analysis
    try:
        schema_view.materialize_patterns()
        # Force induction of all classes to replace slots with attributes
        for class_name in schema_view.all_classes():
            schema_view.induced_class(class_name)
    except Exception as e:
        logger.warning(f"Could not induce classes ({e})")
    
    # Check raw schema attributes first
    schema_dict = schema_view.schema._as_dict
    for k, v in schema_dict.items():
        if is_populated(v):
            keys.add(k)
    
    # Dynamically discover collections from metamodel
    schema_collections = get_metamodel_schema_collections()
    
    for key_name, method_name in schema_collections.items():
        try:
            method = getattr(schema_view, method_name)
            result = method(imports=True)
            if is_populated(result):
                keys.add(key_name)
        except (AttributeError, TypeError) as e:
            # Skip if method doesn't exist or fails
            print(f"Warning: Could not access {method_name} ({e})")
    
    return keys


def get_element_introspection_info(schema_view: SchemaView, element_name: str, element_type: str) -> Dict[str, Any]:
    """Get comprehensive introspection information for a schema element using SchemaView methods.
    
    Args:
        schema_view: SchemaView instance to query
        element_name: Name of the element to introspect
        element_type: Type of element ('class', 'slot', 'enum', 'type', 'subset')
        
    Returns:
        Dict with introspection information including mappings, relationships, usage
    """
    info = {
        'element_name': element_name,
        'element_type': element_type,
        'mappings': [],
        'usage': [],
        'relationships': {},
        'metadata': {}
    }
    
    try:
        if element_type == 'class':
            # Get class-specific introspection
            info['relationships']['ancestors'] = list(schema_view.class_ancestors(element_name))
            info['relationships']['descendants'] = list(schema_view.class_descendants(element_name))
            info['relationships']['slots'] = list(schema_view.class_slots(element_name))
            
            # Get identifier slot if available
            try:
                id_slot = schema_view.get_identifier_slot(element_name)
                info['metadata']['identifier_slot'] = id_slot.name if id_slot else None
            except Exception:
                info['metadata']['identifier_slot'] = None
                
        elif element_type == 'slot':
            # Get slot-specific introspection  
            info['relationships']['ancestors'] = list(schema_view.slot_ancestors(element_name))
            
            # Get classes that use this slot
            try:
                usage_index = schema_view.usage_index()
                info['usage'] = usage_index.get(element_name, [])
            except Exception:
                info['usage'] = []
                
        elif element_type == 'enum':
            # Get enum-specific information
            try:
                enum_def = schema_view.get_enum(element_name)
                if enum_def and hasattr(enum_def, 'permissible_values'):
                    info['metadata']['permissible_value_count'] = len(enum_def.permissible_values or {})
                else:
                    info['metadata']['permissible_value_count'] = 0
            except Exception:
                info['metadata']['permissible_value_count'] = 0
        
        # Get mappings for any element type
        try:
            mappings = schema_view.get_mappings(element_name)
            info['mappings'] = list(mappings) if mappings else []
        except Exception:
            info['mappings'] = []
            
        # Get URI information
        try:
            uri = schema_view.get_uri(element_name)
            info['metadata']['uri'] = uri if uri else None
        except Exception:
            info['metadata']['uri'] = None
            
    except Exception as e:
        logger.warning(f"Error getting introspection info for {element_type} {element_name}: {e}")
    
    return info


def serialize_linkml_object_with_schemaview(obj: Any, schema_view: SchemaView = None) -> Any:
    """Enhanced serialization of LinkML objects using SchemaView introspection when available.
    
    Args:
        obj: LinkML object to serialize
        schema_view: Optional SchemaView for enhanced introspection
        
    Returns:
        Serialized representation suitable for YAML output
    """
    if obj is None:
        return None
    
    # Handle basic types
    if isinstance(obj, (str, int, float, bool)):
        return obj
    
    # Handle collections
    if isinstance(obj, (list, tuple)):
        return [serialize_linkml_object_with_schemaview(item, schema_view) for item in obj]
    
    if isinstance(obj, dict):
        return {str(k): serialize_linkml_object_with_schemaview(v, schema_view) for k, v in obj.items()}
    
    # Handle LinkML objects with _as_dict method
    if hasattr(obj, '_as_dict'):
        try:
            dict_rep = obj._as_dict
            
            # If we have a schema_view, enhance with introspection
            if schema_view and hasattr(obj, 'name') and obj.name:
                obj_name = obj.name
                class_name = obj.__class__.__name__
                
                # Determine element type from class name
                element_type = None
                if class_name.endswith('Definition'):
                    element_type = class_name.replace('Definition', '').lower()
                elif class_name in ['PermissibleValue', 'Annotation']:
                    element_type = class_name.lower()
                
                # Add introspection info if we can determine the type
                if element_type and element_type in ['class', 'slot', 'enum', 'type', 'subset']:
                    try:
                        introspection = get_element_introspection_info(schema_view, obj_name, element_type)
                        if introspection.get('relationships') or introspection.get('mappings'):
                            dict_rep['_introspection'] = introspection
                    except Exception:
                        # Don't fail serialization if introspection fails
                        pass
            
            # Recursively serialize the dictionary
            return {str(k): serialize_linkml_object_with_schemaview(v, schema_view) for k, v in dict_rep.items()}
            
        except Exception:
            # Fall back to string representation if _as_dict fails
            return str(obj)
    
    # Handle LinkML specific types by class name patterns
    if hasattr(obj, '__class__'):
        class_name = obj.__class__.__name__
        module_name = getattr(obj.__class__, '__module__', '')
        
        # Check for LinkML types by module or class name patterns
        if ('linkml' in module_name or 
            class_name.endswith('Definition') or
            class_name in {'PermissibleValue', 'Annotation', 'Extension'} or
            'extended_str' in class_name.lower()):
            
            # Try to get meaningful representation
            if hasattr(obj, 'value'):  # For some LinkML wrapper types
                return serialize_linkml_object_with_schemaview(obj.value, schema_view)
            elif hasattr(obj, 'name'):  # For named elements
                return str(obj.name)
            else:
                return str(obj)
    
    # Default to string representation for unknown types
    return str(obj)


def find_element_differences(old_element, new_element, element_type: str) -> List[str]:
    """Find differences between two LinkML elements (enum, class, slot) and return as list of strings."""
    differences = []
    
    # Dynamically discover all attributes from both objects
    old_attrs = set(dir(old_element)) if old_element else set()
    new_attrs = set(dir(new_element)) if new_element else set()
    
    # Element-specific attributes to exclude (complex objects we'll handle separately)
    element_specific_exclusions = {
        'enum': {'permissible_values', 'values'},
        'class': {'slots', 'slot_usage', 'attributes'},
        'slot': {'structured_pattern', 'annotations'}
    }
    
    # Filter out private/internal attributes, methods, and known complex attributes
    excluded_attrs = {
        # Private/internal
        attr for attr in (old_attrs | new_attrs) if attr.startswith('_')
    } | {
        # Obvious differences we don't need to report
        'name', 'from_schema'  # These are expected to differ in mappings
    } | element_specific_exclusions.get(element_type, set())
    
    all_attrs = (old_attrs | new_attrs) - excluded_attrs
    
    # Further filter out callable methods - handle None elements safely
    all_attrs = {
        attr for attr in all_attrs
        if not ((old_element and callable(getattr(old_element, attr, None)))
                or (new_element and callable(getattr(new_element, attr, None))))
    }
    
    for attr in sorted(all_attrs):
        old_val = getattr(old_element, attr, None)
        new_val = getattr(new_element, attr, None)
        
        # Only report scalar/simple values that differ and at least one is non-empty
        if old_val != new_val and (old_val or new_val):
            # Skip complex objects like dicts, lists for now (we'll handle those separately)
            if not isinstance(old_val, (dict, list)) and not isinstance(new_val, (dict, list)):
                old_display = repr(old_val) if old_val else "None"
                new_display = repr(new_val) if new_val else "None"
                differences.append(f"{attr}: {old_display} vs {new_display}")
    
    return differences


def find_enum_differences(old_enum, new_enum) -> List[str]:
    """Find differences between two enum definitions and return as list of strings."""
    return find_element_differences(old_enum, new_enum, 'enum')


def find_class_differences(old_class, new_class) -> List[str]:
    """Find differences between two class definitions and return as list of strings."""
    return find_element_differences(old_class, new_class, 'class')


def find_slot_differences(old_slot, new_slot) -> List[str]:
    """Find differences between two slot definitions and return as list of strings."""
    return find_element_differences(old_slot, new_slot, 'slot')


def compare_enum_metadata(enum_name: str, old_enum, new_enum, old_info: Dict[str, Any], new_info: Dict[str, Any]) -> None:
    """Compare scalar metadata between two enum definitions."""
    print(f"        {enum_name}: comparing metadata")
    
    differences = find_enum_differences(old_enum, new_enum)
    if differences:
        for diff in differences:
            print(f"          {diff}")
    else:
        print(f"          No scalar metadata differences found")


def analyze_slot_settings_usage(schema_view: SchemaView) -> Dict[str, any]:
    """Analyze which slots use which settings in structured_pattern.syntax.
    
    Returns:
        Dict with keys:
        - 'settings_usage': Dict mapping setting names to lists of slot names that use them
        - 'pattern_usage': Dict mapping full patterns to lists of slot names that use them  
        - 'undefined_settings': Set of setting names used but not defined
        - 'unused_settings': Set of setting names defined but not used
    """
    # Note: 're' is already imported at module level

    settings_usage = {}  # setting_name -> [slot_names]
    pattern_usage = {}   # full_pattern -> [slot_names]
    all_referenced_settings = set()
    
    try:
        # Get all defined settings
        defined_settings = set()
        try:
            all_settings = schema_view.schema.settings
            if all_settings:
                defined_settings = set(all_settings.keys())
        except (AttributeError, TypeError):
            # 'settings' attribute may not exist or may be of unexpected type
            # This is expected for some schemas - proceed with empty defined_settings
            logger.debug("No 'settings' attribute found in schema")
        
        # Parse all slots for structured patterns
        all_slots = schema_view.all_slots(imports=True)
        for slot_name, slot_def in all_slots.items():
            if hasattr(slot_def, 'structured_pattern') and slot_def.structured_pattern:
                if hasattr(slot_def.structured_pattern, 'syntax') and slot_def.structured_pattern.syntax:
                    syntax_value = slot_def.structured_pattern.syntax
                    
                    # Track full pattern usage
                    if syntax_value not in pattern_usage:
                        pattern_usage[syntax_value] = []
                    pattern_usage[syntax_value].append(slot_name)
                    
                    # Extract setting names from {setting_name} patterns
                    setting_references = re.findall(r'\{([^}]+)\}', syntax_value)
                    for setting_name in setting_references:
                        all_referenced_settings.add(setting_name)
                        if setting_name not in settings_usage:
                            settings_usage[setting_name] = []
                        if slot_name not in settings_usage[setting_name]:  # Avoid duplicates
                            settings_usage[setting_name].append(slot_name)
        
        # Convert lists to sets to remove duplicates, then back to sorted lists
        for setting_name in settings_usage:
            settings_usage[setting_name] = sorted(list(set(settings_usage[setting_name])))
        
        for pattern in pattern_usage:
            pattern_usage[pattern] = sorted(list(set(pattern_usage[pattern])))
        
        # Find undefined and unused settings
        undefined_settings = all_referenced_settings - defined_settings
        unused_settings = defined_settings - all_referenced_settings
        
    except Exception as e:
        print(f"Error analyzing slot settings usage: {e}")
        return {
            'settings_usage': {},
            'pattern_usage': {},
            'undefined_settings': set(),
            'unused_settings': set()
        }
    
    return {
        'settings_usage': settings_usage,
        'pattern_usage': pattern_usage,
        'undefined_settings': undefined_settings,
        'unused_settings': unused_settings
    }


def diff_top_keys(schema1_view: SchemaView, schema2_view: SchemaView) -> Tuple[Set[str], Set[str]]:
    """Compare top-level keys between two schemas.
    
    Args:
        schema1_view: First SchemaView to compare.
        schema2_view: Second SchemaView to compare.
        
    Returns:
        Tuple of (only_in_1, only_in_2) where each is a set of keys that are
        populated in one schema but missing or empty in the other.
    """
    s1_keys = populated_top_level_keys(schema1_view)
    s2_keys = populated_top_level_keys(schema2_view)
    only_in_1 = s1_keys - s2_keys
    only_in_2 = s2_keys - s1_keys
    return only_in_1, only_in_2



def validate_github_token(token: str) -> bool:
    """Validate GitHub token format.
    
    Args:
        token: GitHub token to validate.
        
    Returns:
        True if token format is valid, False otherwise.
    """
    # GitHub personal access tokens patterns
    patterns = [
        r'^ghp_[a-zA-Z0-9]{36}$',  # Personal access token
        r'^gho_[a-zA-Z0-9]{36}$',  # OAuth token
        r'^ghu_[a-zA-Z0-9]{36}$',  # User token
        r'^ghs_[a-zA-Z0-9]{36}$',  # Server token
        r'^github_pat_[a-zA-Z0-9_]{82}$',  # Fine-grained personal access token
    ]

    return any(re.match(pattern, token) for pattern in patterns)


def get_github_headers() -> Dict[str, str]:
    """Get GitHub API headers with authentication if available.

    Returns:
        Dict containing Authorization header if token is available, empty dict otherwise.
    """
    global AUTH_MESSAGE_PRINTED

    # First check environment variable (for CI/CD like GitHub Actions)
    token = os.getenv('GITHUB_TOKEN')

    # Fall back to .env file for local development
    if not token:
        env_file = Path(__file__).parent.parent.parent / 'local' / '.env'
        if env_file.exists():
            load_dotenv(env_file)
            token = os.getenv('GITHUB_TOKEN')

    headers = {}
    if token:
        if validate_github_token(token):
            headers['Authorization'] = f'token {token}'
            if VERBOSE_AUTH or not AUTH_MESSAGE_PRINTED:
                logger.info("Using authenticated GitHub API")
                AUTH_MESSAGE_PRINTED = True
        else:
            if VERBOSE_AUTH or not AUTH_MESSAGE_PRINTED:
                logger.warning("Invalid GitHub token format detected, using unauthenticated API")
                logger.warning("Using unauthenticated GitHub API (rate limited)")
                AUTH_MESSAGE_PRINTED = True
    else:
        if VERBOSE_AUTH or not AUTH_MESSAGE_PRINTED:
            logger.warning("Using unauthenticated GitHub API (rate limited)")
            AUTH_MESSAGE_PRINTED = True
    return headers


def fetch_tree(owner: str, repo: str, commit_sha: str) -> List[str]:
    """Fetch recursive tree from GitHub API and return YAML files.
    
    Args:
        owner: GitHub repository owner.
        repo: GitHub repository name.
        commit_sha: Git commit SHA to fetch tree for.
        
    Returns:
        List of paths to YAML files in the repository at the given commit.
    """
    global API_CALL_COUNT
    headers = get_github_headers()
    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{commit_sha}?recursive=1"
    response = requests.get(url, headers=headers, timeout=10)
    API_CALL_COUNT += 1
    response.raise_for_status()
    tree = response.json()

    yaml_files = [item['path'] for item in tree['tree']
                  if item['path'].endswith(('.yaml', '.yml'))]
    return yaml_files


def find_mixs_yaml_path(yaml_files: List[str], approved_dirs: Optional[List[str]] = None) -> Optional[str]:
    """Find mixs.yaml file in approved directories.
    
    Args:
        yaml_files: List of YAML file paths to search through.
        approved_dirs: List of approved directory names to search in. 
                      Defaults to APPROVED_DIRS constant.
                      
    Returns:
        Path to mixs.yaml file if found in approved directories, None otherwise.
    """
    if approved_dirs is None:
        approved_dirs = APPROVED_DIRS

    for yaml_file in yaml_files:
        if yaml_file.endswith('mixs.yaml'):
            for approved_dir in approved_dirs:
                if yaml_file.startswith(f'{approved_dir}/'):
                    return yaml_file
    return None


def get_releases(owner: str = DEFAULT_OWNER, repo: str = DEFAULT_REPO) -> List[Tuple[str, datetime]]:
    """Get releases from GitHub API with pagination support.
    
    Args:
        owner: GitHub repository owner (defaults to DEFAULT_OWNER).
        repo: GitHub repository name (defaults to DEFAULT_REPO).
    
    Returns:
        List of tuples containing (tag_name, published_date) for each release.
    """
    global API_CALL_COUNT
    headers = get_github_headers()
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"

    release_info = []
    page = 1

    while True:
        paginated_url = f"{url}?page={page}&per_page=100"
        response = requests.get(paginated_url, headers=headers, timeout=10)
        API_CALL_COUNT += 1
        response.raise_for_status()
        releases = response.json()

        # If no releases returned, we've reached the end
        if not releases:
            break

        for release in releases:
            tag = release['tag_name']
            date = datetime.fromisoformat(release['published_at'].replace('Z', '+00:00'))
            release_info.append((tag, date))

        page += 1

    return release_info


def get_yaml_files_from_release(owner: str, repo: str, tag: str) -> Tuple[List[str], str]:
    """Get list of YAML files and commit SHA from a specific release tag.
    
    Args:
        owner: GitHub repository owner.
        repo: GitHub repository name.
        tag: Release tag name to fetch files for.
        
    Returns:
        Tuple of (yaml_files, commit_sha) where yaml_files is a list of YAML file paths
        and commit_sha is the full commit hash for the tag.
    """
    global API_CALL_COUNT
    headers = get_github_headers()
    # Get commit SHA for the tag
    url = f"https://api.github.com/repos/{owner}/{repo}/git/refs/tags/{tag}"
    response = requests.get(url, headers=headers, timeout=10)
    API_CALL_COUNT += 1
    response.raise_for_status()
    commit_sha = response.json()['object']['sha']

    yaml_files = fetch_tree(owner, repo, commit_sha)
    return yaml_files, commit_sha


def get_main_branch_info(owner: str, repo: str) -> Tuple[List[str], str, datetime]:
    """Get YAML files and commit info from main branch.
    
    Args:
        owner: GitHub repository owner.
        repo: GitHub repository name.
    
    Returns:
        Tuple of (yaml_files, commit_sha, commit_date) where yaml_files is a list
        of YAML file paths, commit_sha is the full commit hash, and commit_date
        is the datetime of the commit.
    """
    global API_CALL_COUNT
    headers = get_github_headers()
    # Get main branch commit
    url = f"https://api.github.com/repos/{owner}/{repo}/branches/main"
    response = requests.get(url, headers=headers, timeout=10)
    API_CALL_COUNT += 1
    response.raise_for_status()
    branch_info = response.json()

    commit_sha = branch_info['commit']['sha']
    commit_date = datetime.fromisoformat(branch_info['commit']['commit']['author']['date'].replace('Z', '+00:00'))

    yaml_files = fetch_tree(owner, repo, commit_sha)
    return yaml_files, commit_sha, commit_date


def get_raw_schema_url(owner: str, repo: str, commit_hash: str, schema_path: Optional[str]) -> Optional[str]:
    """Get raw GitHub URL for a schema file at a specific commit.
    
    Args:
        owner: GitHub repository owner.
        repo: GitHub repository name.
        commit_hash: Git commit hash.
        schema_path: Path to schema file within the repository.
        
    Returns:
        Raw GitHub URL to the schema file, or None if no path provided.
    """
    if not schema_path:
        return None
    return f"https://raw.githubusercontent.com/{owner}/{repo}/{commit_hash}/{schema_path}"


def get_cached_schema_path(commit_hash: str, tag: str) -> Path:
    """Get the local path where a schema should be cached.
    
    Args:
        commit_hash: Git commit hash.
        tag: Release tag name.
        
    Returns:
        Path object for the cached schema file.
    """
    assets_dir = Path(__file__).parent.parent.parent / 'assets' / 'releases_for_diffing'
    filename = f"{tag}_{commit_hash[:7]}_mixs.yaml"
    return assets_dir / filename


def download_schema_file(url: str, local_path: Path) -> bool:
    """Download a schema file from GitHub and save it locally.
    
    Args:
        url: Raw GitHub URL to download from.
        local_path: Local path to save the file.
        
    Returns:
        True if download was successful, False otherwise.
    """
    global API_CALL_COUNT
    try:
        headers = get_github_headers()
        response = requests.get(url, headers=headers, timeout=30)
        API_CALL_COUNT += 1
        response.raise_for_status()

        # Validate that response is valid YAML before writing
        try:
            yaml.safe_load(response.text)
        except yaml.YAMLError as e:
            logger.error(f"Downloaded content is not valid YAML: {e}")
            return False

        # Ensure parent directory exists
        local_path.parent.mkdir(parents=True, exist_ok=True)

        with open(local_path, 'w', encoding='utf-8') as f:
            f.write(response.text)

        logger.info(f"Downloaded schema to: {local_path}")
        return True

    except Exception as e:
        logger.error(f"Error downloading schema from {url}: {e}")
        return False


def download_schema_directory(owner: str, repo: str, commit_hash: str, tag: str) -> Path:
    """Download entire schema directory structure from GitHub for modular schemas.
    
    Args:
        owner: GitHub repository owner.
        repo: GitHub repository name.
        commit_hash: Git commit hash.
        tag: Release tag name.
        
    Returns:
        Path to the local directory containing all schema files.
    """
    # Create cache directory for this specific commit
    cache_dir = Path(__file__).parent.parent.parent / 'assets' / 'releases_for_diffing' / f"{tag}_{commit_hash[:7]}"
    cache_dir.mkdir(parents=True, exist_ok=True)
    
    # Get all YAML files from the repository
    yaml_files = fetch_tree(owner, repo, commit_hash)
    
    # Download all YAML files that might be schema-related
    schema_files = [f for f in yaml_files if f.endswith(('.yaml', '.yml')) and 
                   any(f.startswith(approved_dir) for approved_dir in APPROVED_DIRS)]
    
    for file_path in schema_files:
        remote_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{commit_hash}/{file_path}"
        local_file_path = cache_dir / file_path
        
        # Create subdirectories as needed
        local_file_path.parent.mkdir(parents=True, exist_ok=True)
        
        if download_schema_file(remote_url, local_file_path):
            print(f"  Downloaded: {file_path}")
    
    return cache_dir


def get_schema_path(owner: str, repo: str, commit_hash: str, tag: str, schema_path: Optional[str], use_cache: bool = True) -> Optional[str]:
    """Get path to schema file, downloading and caching if necessary.
    
    Args:
        owner: GitHub repository owner.
        repo: GitHub repository name.
        commit_hash: Git commit hash.
        tag: Release tag name.
        schema_path: Path to schema file within the repository.
        use_cache: Whether to use cached version if available.
        
    Returns:
        Path to schema file (local if cached, URL if not), or None if unavailable.
    """
    if not schema_path:
        return None
    
    # If caching is enabled, download entire schema directory structure
    if use_cache:
        # Check if we already have the full directory cached
        cache_dir = Path(__file__).parent.parent.parent / 'assets' / 'releases_for_diffing' / f"{tag}_{commit_hash[:7]}"
        cached_schema_file = cache_dir / schema_path
        
        if cached_schema_file.exists():
            logger.info(f"Using cached schema: {cached_schema_file}")
            return str(cached_schema_file)
        
        # Download entire schema directory structure
        print(f"Caching schema directory for {tag} ({commit_hash[:7]})...")
        try:
            download_schema_directory(owner, repo, commit_hash, tag)
            if cached_schema_file.exists():
                logger.info(f"Using cached schema: {cached_schema_file}")
                return str(cached_schema_file)
            else:
                print(f"Warning: Schema file {schema_path} not found after caching directory")
        except Exception as e:
            print(f"Failed to cache schema directory: {e}")
    
    # Fall back to remote URL
    remote_url = get_raw_schema_url(owner, repo, commit_hash, schema_path)
    if not remote_url:
        return None
    
    print(f"Using remote schema URL: {remote_url}")
    return remote_url


def build_full_release_info(repositories: List[Tuple[str, str]]) -> Dict[str, Dict[str, Any]]:
    """Build comprehensive release info dictionary for all releases and main branch from multiple repositories.
    
    Args:
        repositories: List of (owner, repo) tuples to fetch releases for.
    
    Returns:
        Dict mapping short commit hashes to release metadata with commit_sha included.
    """
    release_info = {}

    for owner, repo in repositories:
        logger.info(f"Fetching releases for {owner}/{repo}...")
        releases = get_releases(owner, repo)

        # Build release info dict for this repository
        for tag, date in releases:
            yaml_files, commit_sha = get_yaml_files_from_release(owner, repo, tag)
            short_hash = commit_sha[:7]
            schema_yaml_path = find_mixs_yaml_path(yaml_files)

            # Use repo-prefixed key if multiple repos, otherwise just short hash
            key = f"{owner}/{repo}#{short_hash}" if len(repositories) > 1 else short_hash

            release_entry = {
                'owner': owner,
                'repo': repo,
                'tag': tag,
                'date': date.strftime('%Y-%m-%d'),
                'schema_yaml_path': schema_yaml_path,
                'commit_sha': commit_sha
            }

            # Index by short hash
            release_info[key] = release_entry

            # Also index by tag name for convenience (allows using tag names like 'mixs6.0.0')
            tag_key = f"{owner}/{repo}#{tag}" if len(repositories) > 1 else tag
            release_info[tag_key] = release_entry

        # Add main branch info for this repository
        logger.info(f"Fetching main branch info for {owner}/{repo}...")
        yaml_files, commit_sha, commit_date = get_main_branch_info(owner, repo)
        short_hash = commit_sha[:7]
        schema_yaml_path = find_mixs_yaml_path(yaml_files)

        # Use repo-prefixed key if multiple repos, otherwise just short hash
        key = f"{owner}/{repo}#{short_hash}" if len(repositories) > 1 else short_hash

        main_entry = {
            'owner': owner,
            'repo': repo,
            'tag': 'main',
            'date': commit_date.strftime('%Y-%m-%d'),
            'schema_yaml_path': schema_yaml_path,
            'commit_sha': commit_sha
        }

        # Index by short hash
        release_info[key] = main_entry

        # Also index by 'main' for convenience (allows using 'main' as identifier)
        main_key = f"{owner}/{repo}#main" if len(repositories) > 1 else 'main'
        release_info[main_key] = main_entry

    return release_info


def validate_schema_definition(schema_view: SchemaView, schema_tag: str) -> bool:
    """Validate that a schema is a proper LinkML SchemaDefinition.
    
    Args:
        schema_view: SchemaView to validate.
        schema_tag: Human readable identifier for error messages.
        
    Returns:
        True if valid, False otherwise.
    """
    try:
        # Check if schema has required SchemaDefinition properties
        schema = schema_view.schema
        if not hasattr(schema, 'id') or not schema.id:
            logger.warning(f"Schema {schema_tag} missing required 'id' field")
            return False
            
        if not hasattr(schema, 'name') or not schema.name:
            logger.warning(f"Schema {schema_tag} missing required 'name' field")
            return False
            
        # Check if we can access core collections
        try:
            schema_view.all_classes()
            schema_view.all_slots()
        except Exception as e:
            logger.warning(f"Schema {schema_tag} failed basic collection access: {e}")
            return False
            
        return True
        
    except Exception as e:
        logger.warning(f"Schema validation failed for {schema_tag}: {e}")
        return False


def load_schema_views(old_commit: str = '74744ee',
                      new_commit: str = '994c745',
                      use_cache: bool = True) -> Tuple[
    SchemaView, SchemaView, Dict[str, Any], Dict[str, Any]]:
    """Load SchemaView objects for old and new commits with validation.
    
    Args:
        old_commit: Short commit hash for the old schema version.
        new_commit: Short commit hash for the new schema version.
        use_cache: Whether to cache schemas locally in assets/releases_for_diffing.
        
    Returns:
        Tuple of (old_schema, new_schema, old_info, new_info) where:
        - old_schema, new_schema: SchemaView objects for the schemas
        - old_info, new_info: Dict with release metadata (tag, date, etc.)
        
    Raises:
        ValueError: If specified commits are not found or have no mixs.yaml file.
    """
    release_info = build_full_release_info([(DEFAULT_OWNER, DEFAULT_REPO)])

    # Get schema info for specified commits
    old_info = release_info.get(old_commit)
    new_info = release_info.get(new_commit)

    if not old_info:
        raise ValueError(f"Old commit {old_commit} not found in releases")
    if not new_info:
        raise ValueError(f"New commit {new_commit} not found in releases")

    # Get schema paths (local if cached, remote URLs otherwise)
    old_path = get_schema_path(old_info['owner'], old_info['repo'], old_info['commit_sha'], old_info['tag'], old_info['schema_yaml_path'], use_cache)
    new_path = get_schema_path(new_info['owner'], new_info['repo'], new_info['commit_sha'], new_info['tag'], new_info['schema_yaml_path'], use_cache)

    if not old_path:
        raise ValueError(f"No mixs.yaml found for old commit {old_commit} ({old_info['tag']})")
    if not new_path:
        raise ValueError(f"No mixs.yaml found for new commit {new_commit} ({new_info['tag']})")

    print(f"Loading old schema: {old_info['tag']} ({old_commit})")
    print(f"  Path: {old_path}")
    old_schema = SchemaView(old_path)

    print(f"Loading new schema: {new_info['tag']} ({new_commit})")
    print(f"  Path: {new_path}")
    new_schema = SchemaView(new_path)
    
    # Validate schemas
    print(f"Validating schemas as LinkML SchemaDefinitions...")
    old_valid = validate_schema_definition(old_schema, old_info['tag'])
    new_valid = validate_schema_definition(new_schema, new_info['tag'])
    
    if not old_valid or not new_valid:
        print("Warning: Schema validation issues detected, but proceeding with comparison")

    return old_schema, new_schema, old_info, new_info


def print_releases() -> None:
    """Print all releases with tag and date."""
    releases = get_releases(DEFAULT_OWNER, DEFAULT_REPO)
    for tag, date in releases:
        print(f"{tag}: {date.strftime('%Y-%m-%d')}")


def build_release_info_dict(repositories: List[Tuple[str, str]] = None) -> Dict[str, Dict[str, Any]]:
    """Build release info dictionary with all releases and main branch info (with optional display output).
    
    Args:
        repositories: List of (owner, repo) tuples to fetch releases for. 
                     Defaults to [(DEFAULT_OWNER, DEFAULT_REPO)].
    
    Returns:
        Dict mapping short commit hashes to release metadata.
    """
    if repositories is None:
        repositories = [(DEFAULT_OWNER, DEFAULT_REPO)]
    
    release_info = build_full_release_info(repositories)

    if SHOW_YAML_FILES:
        # Print output for each repository's releases
        for owner, repo in repositories:
            logger.info(f"\nYAML files for {owner}/{repo}:")
            releases = get_releases(owner, repo)
            for tag, date in releases:
                yaml_files, commit_sha = get_yaml_files_from_release(owner, repo, tag)
                short_hash = commit_sha[:7]

                print(f"\n{tag}: {date.strftime('%Y-%m-%d')} ({short_hash})")
                for yaml_file in yaml_files:
                    print(f"  {yaml_file}")

            # Add main branch info display
            yaml_files, commit_sha, commit_date = get_main_branch_info(owner, repo)
            short_hash = commit_sha[:7]

            print(f"\nmain: {commit_date.strftime('%Y-%m-%d')} ({short_hash})")
            for yaml_file in yaml_files:
                print(f"  {yaml_file}")

    # Return the simplified dict (without commit_sha for backward compatibility)
    return {k: {key: val for key, val in v.items() if key != 'commit_sha'}
            for k, v in release_info.items()}


@click.command()
@click.option('--old', default=None,
              help='Old schema in format owner/repo@commit:path (e.g., GenomicsStandardsConsortium/mixs@mixs6.0.0:src/mixs/schema/mixs.yaml). Required unless --list-releases.')
@click.option('--new', default=None,
              help='New schema in format owner/repo@commit:path (e.g., GenomicsStandardsConsortium/mixs@main:src/mixs/schema/mixs.yaml). Required unless --list-releases.')
@click.option('--no-cache', is_flag=True, default=False,
              help='Skip caching schemas locally (use remote URLs directly)')
@click.option('--output-dir', type=click.Path(path_type=Path), 
              default=Path(__file__).parent.parent.parent / "assets" / "diff_results",
              help='Directory to save output files (default: assets/diff_results)')
@click.option('--mappings-dir', type=click.Path(path_type=Path),
              default=Path(__file__).parent.parent.parent / "assets" / "between_diff_mappings",
              help='Directory containing mapping TSV files (default: assets/between_diff_mappings)')
@click.option('--log-level', type=click.Choice(['DEBUG', 'INFO', 'WARNING', 'ERROR']),
              default='INFO', help='Set logging level (default: INFO)')
@click.option('--list-releases', is_flag=True, default=False,
              help='List available releases and exit')
def main(old: str, new: str, no_cache: bool, output_dir: Path, mappings_dir: Path, log_level: str, list_releases: bool):
    """Compare two LinkML schema releases and generate diff report.
    
    This script fetches schemas from GitHub repositories, optionally caches them locally
    in assets/releases_for_diffing, and performs a systematic comparison.
    
    Examples:
        # Compare default versions (6.0.0 vs main) from default repo
        python diff_two_linkml_mixs_releases.py
        
        # Compare specific versions using URL-like format
        python diff_two_linkml_mixs_releases.py --old GenomicsStandardsConsortium/mixs@74744ee:model/schema/mixs.yaml --new GenomicsStandardsConsortium/mixs@994c745:src/mixs/schema/mixs.yaml
        
        # Compare schemas from different repositories
        python diff_two_linkml_mixs_releases.py --old owner1/repo1@commit1:path1.yaml --new owner2/repo2@commit2:path2.yaml
        
        # Skip caching (use remote URLs)
        python diff_two_linkml_mixs_releases.py --no-cache
        
        # List available releases
        python diff_two_linkml_mixs_releases.py --list-releases
    """
    global CLASS_NAME_MAPPINGS, ENUM_NAME_MAPPINGS, SLOT_NAME_MAPPINGS, SUBSET_NAME_MAPPINGS, INTER_TYPE_REFACTORING
    
    # Set logging level
    logging.getLogger().setLevel(getattr(logging, log_level))
    logger.info(f"Logging level set to {log_level}")
    
    # Load name mappings
    CLASS_NAME_MAPPINGS = load_class_name_mappings(mappings_dir)
    ENUM_NAME_MAPPINGS = load_enum_name_mappings(mappings_dir)
    SLOT_NAME_MAPPINGS = load_slot_name_mappings(mappings_dir)
    SUBSET_NAME_MAPPINGS = load_subset_name_mappings(mappings_dir)
    INTER_TYPE_REFACTORING = load_inter_type_refactoring(mappings_dir)

    if list_releases:
        logger.info("Available releases:")
        print_releases()
        return

    # Validate required arguments when not listing releases
    if not old or not new:
        raise click.UsageError("--old and --new are required unless --list-releases is used")

    # Build and display release info
    logger.info("Building release information dictionary...")
    release_info = build_release_info_dict()

    # Print the dictionary
    separator = "=" * 50
    print(f"\n{separator}")
    print("Release Info Dictionary:")
    print(separator)
    pprint.pprint(release_info)

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Save as YAML file
    releases_output_file = output_dir / "releases.yaml"
    logger.info(f"Saving release info to: {releases_output_file}")
    with open(releases_output_file, 'w') as f:
        yaml.dump(release_info, f, default_flow_style=False, sort_keys=False)
    logger.info(f"Saved release info to: {releases_output_file}")

    # Load and compare schemas
    logger.info("\n" + "=" * 50)
    logger.info("Loading schemas for comparison...")
    logger.info("=" * 50)

    try:
        # Parse schema specifications
        old_owner, old_repo, old_commit, old_schema_path = parse_schema_spec(old)
        new_owner, new_repo, new_commit, new_schema_path = parse_schema_spec(new)
        
        logger.info(f"Comparing schemas:")
        logger.info(f"  OLD: {old_owner}/{old_repo}@{old_commit}:{old_schema_path}")
        logger.info(f"  NEW: {new_owner}/{new_repo}@{new_commit}:{new_schema_path}")
        
        # For now, only support same repository comparisons 
        if old_owner != new_owner or old_repo != new_repo:
            logger.warning("Cross-repository comparisons not yet fully supported.")
            logger.warning("Using existing load_schema_views for same-repo comparison.")
        
        use_cache = not no_cache
        logger.info("Loading schema views (this may take a moment)...")
        old_schema, new_schema, old_info, new_info = load_schema_views(
            old_commit, new_commit, use_cache
        )

        logger.info("\nOld schema info:")
        pprint.pprint(old_info)

        logger.info("\nNew schema info:")
        pprint.pprint(new_info)

        # Initialize the comparator and run the comparison
        logger.info("\n" + "=" * 80)
        logger.info("RUNNING NEW SYSTEMATIC LINKML COMPARISON FRAMEWORK")
        logger.info("=" * 80)
        logger.info("Initializing LinkML comparator...")
        comparator = LinkMLComparator(old_schema, new_schema, old_info, new_info)
        logger.info("Running schema comparison (this may take several minutes)...")
        comparison_results = comparator.compare_schemas()

        # Convert results to a dictionary
        logger.info("Converting comparison results to dictionary format...")
        comparison_dict = schema_comparison_to_dict(comparison_results)

        # Save the results to a YAML file
        comparison_output_file = output_dir / "schema_comparison_results.yaml"
        logger.info(f"Saving comparison results to: {comparison_output_file}")
        with open(comparison_output_file, 'w') as f:
            # Use the safe dumper to avoid LinkML-specific serialization
            yaml.dump(comparison_dict, f, default_flow_style=False, sort_keys=False, Dumper=yaml.SafeDumper)
        
        summary = comparison_dict.get('summary', {})
        print("\n" + "=" * 50)
        print("SAVING COMPARISON RESULTS TO YAML")
        print("=" * 50)
        print(f"Saved systematic comparison results to: {comparison_output_file}")
        print(f"  • Scalar differences: {summary.get('total_scalar_differences', 0)}")
        print(f"  • Collection differences: {summary.get('total_collection_differences', 0)}")
        print(f"  • Total schema elements compared: {summary.get('total_schema_elements_compared', 0)}")

        # Optionally, print a summary report to the console
        print_schema_comparison_report(comparison_results)

    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise click.ClickException(str(e))
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        raise click.ClickException(f"Unexpected error: {e}")

    logger.info("\n" + "=" * 50)
    logger.info(f"API Usage Summary: {API_CALL_COUNT} GitHub API calls made")
    logger.info("=" * 50)


if __name__ == "__main__":
    main()