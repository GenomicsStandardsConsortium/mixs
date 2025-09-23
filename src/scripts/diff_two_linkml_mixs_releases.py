import requests
from datetime import datetime
import pprint
import os
from pathlib import Path
from dotenv import load_dotenv
import yaml
from linkml_runtime.utils.schemaview import SchemaView
from typing import List, Tuple, Dict, Optional, Any, Set, Union
from dataclasses import dataclass
from abc import ABC, abstractmethod
import re

APPROVED_DIRS = ['src', 'model']
DEFAULT_OLD_COMMIT = '74744ee'  # mixs6.0.0 - comparing from this version
DEFAULT_NEW_COMMIT = '994c745'  # main branch as of 2025-07-14 - comparing to this version

# Global configuration
SHOW_YAML_FILES = False  # Set to True to print discovered YAML files
VERBOSE_AUTH = False     # Set to True to print auth message every time
SHOW_ALL_CLASS_NAMES = True  # Set to True to print all class names in diffs
SHOW_ALL_ENUM_NAMES = True  # Set to True to print all enum names in diffs
SHOW_ALL_SLOT_NAMES = True  # Set to True to print all slot names in diffs
API_CALL_COUNT = 0       # Track number of API calls made
AUTH_MESSAGE_PRINTED = False  # Track if auth message was already shown

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
        for schema in [self.old_schema, self.new_schema]:
            try:
                schema.materialize_patterns()
                # Force induction of all classes to use .attributes instead of .slots
                for class_name in schema.all_classes():
                    schema.induced_class(class_name)
            except Exception as e:
                print(f"Warning: Schema initialization issue ({e})")
    
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
    
    def _compare_scalars(self, old_value: Any, new_value: Any) -> ValueComparison:
        """Compare scalar values."""
        differences = []
        if old_value != new_value:
            differences.append(f"{old_value} vs {new_value}")
        
        return ValueComparison(
            old_value=old_value,
            new_value=new_value, 
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
        
        return ValueComparison(
            old_value=old_value,
            new_value=new_value,
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
        """Compare LinkML object instances using attribute-based comparison."""
        differences = []
        
        if old_instance is None and new_instance is None:
            return ValueComparison(old_instance, new_instance, 'instance', [])
        
        if old_instance is None or new_instance is None:
            differences.append("One instance is None")
            return ValueComparison(old_instance, new_instance, 'instance', differences)
        
        # Get attributes dynamically, excluding private/internal ones
        old_attrs = set(dir(old_instance)) if old_instance else set()
        new_attrs = set(dir(new_instance)) if new_instance else set()
        
        # Filter attributes  
        excluded = {attr for attr in (old_attrs | new_attrs) 
                   if attr.startswith('_') or callable(getattr(old_instance, attr, None)) 
                   or callable(getattr(new_instance, attr, None))}
        
        all_attrs = (old_attrs | new_attrs) - excluded
        
        for attr in sorted(all_attrs):
            old_val = getattr(old_instance, attr, None)
            new_val = getattr(new_instance, attr, None)
            
            # Only report scalar differences for now (avoid recursion) 
            if old_val != new_val and not isinstance(old_val, (dict, list)) and not isinstance(new_val, (dict, list)):
                differences.append(f"{attr}: {old_val} vs {new_val}")
        
        return ValueComparison(old_instance, new_instance, 'instance', differences)
    
    def _compare_values(self, old_value: Any, new_value: Any) -> ValueComparison:
        """Main value comparison dispatcher following systematic pattern."""
        old_type = self._get_value_type(old_value)
        new_type = self._get_value_type(new_value)
        
        # Handle type mismatches
        if old_type != new_type:
            return ValueComparison(
                old_value=old_value,
                new_value=new_value,
                value_type='mixed',
                differences=[f"Type mismatch: {old_type} vs {new_type}"]
            )
        
        # Dispatch to appropriate comparison method
        if old_type == 'scalar':
            return self._compare_scalars(old_value, new_value)
        elif old_type == 'list':
            return self._compare_lists(old_value, new_value)
        elif old_type == 'dict':
            return self._compare_dict_values(old_value, new_value)
        elif old_type == 'instance':
            return self._compare_instances(old_value, new_value)
        else:
            return ValueComparison(old_value, new_value, old_type, ["Unknown type"])

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
        """Cascade down to compare class attributes following the same pattern using induced classes."""
        differences = []
        
        # Always use induced classes to get .attributes instead of .slots
        try:
            old_induced = self.old_schema.induced_class(class_name) if class_name in self.old_schema.all_classes() else old_class
            new_induced = self.new_schema.induced_class(class_name) if class_name in self.new_schema.all_classes() else new_class
            
            old_attrs = getattr(old_induced, 'attributes', {}) or {}
            new_attrs = getattr(new_induced, 'attributes', {}) or {}
            
            if old_attrs or new_attrs:
                attrs_comparison = self._compare_dict_values(old_attrs, new_attrs, element_type='attributes')
                if attrs_comparison.has_differences():
                    # Extract key difference summary
                    key_comp = attrs_comparison.key_comparison
                    if key_comp.only_in_old:
                        differences.append(f"attributes only in old: {len(key_comp.only_in_old)} attrs")
                    if key_comp.only_in_new:
                        differences.append(f"attributes only in new: {len(key_comp.only_in_new)} attrs")
                    
                    # Value differences
                    value_diffs = sum(1 for v in attrs_comparison.value_comparisons.values() if v.has_differences())
                    if value_diffs > 0:
                        differences.append(f"attribute definition changes: {value_diffs} attrs")
            
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
                return schema_dict[key]
            
            # Use metamodel-discovered collections  
            schema_collections = get_metamodel_schema_collections()
            if key in schema_collections:
                try:
                    method_name = schema_collections[key]
                    method = getattr(schema_view, method_name)
                    return method(imports=True)
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
        if hasattr(value, '_as_dict'):  # For LinkML object instances
            value = value._as_dict

        if isinstance(value, str):  # This also handles extended_str
            return str(value)
        if isinstance(value, (list, tuple)):
            return [clean_value(v) for v in value]
        if isinstance(value, dict):
            return {str(k): clean_value(v) for k, v in value.items()}
        return value

    def value_comparison_to_dict(value_comp: ValueComparison) -> dict:
        """Convert a ValueComparison to a dictionary with just the old and new values."""
        return {
            old_tag: clean_value(value_comp.old_value),
            new_tag: clean_value(value_comp.new_value)
        }

    def key_comparison_to_dict(key_comp: KeyComparison) -> dict:
        """Convert a KeyComparison to a dictionary."""
        return {
            'only_in_old': sorted(list(key_comp.only_in_old)),
            'only_in_new': sorted(list(key_comp.only_in_new)),
            'shared': sorted(list(key_comp.shared)),
            'expected_mappings': sorted(list(key_comp.expected_mappings)) if key_comp.expected_mappings else []
        }

    def collection_comparison_to_dict(coll_comp: CollectionComparison) -> dict:
        """Convert a CollectionComparison to a dictionary."""
        # For collections, we still want to see the key comparison info
        return {
            'key_comparison': key_comparison_to_dict(coll_comp.key_comparison),
            'definition_changes': {
                k: value_comparison_to_dict(v)
                for k, v in coll_comp.value_comparisons.items()
                if v.has_differences()
            }
        }

    # Build the complete comparison dictionary
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
            k: value_comparison_to_dict(v)
            for k, v in comparison.scalar_comparisons.items()
            if v.has_differences()
        },
        'collection_differences': {
            k: collection_comparison_to_dict(v)
            for k, v in comparison.collection_comparisons.items()
            if v.has_differences()
        },
        'summary': {
            'total_scalar_differences': sum(1 for v in comparison.scalar_comparisons.values() if v.has_differences()),
            'total_collection_differences': sum(1 for v in comparison.collection_comparisons.values() if v.has_differences()),
            'total_schema_elements_compared': sum(
                len(comp.key_comparison.shared) + 
                len(comp.key_comparison.only_in_old) + 
                len(comp.key_comparison.only_in_new) 
                for comp in comparison.collection_comparisons.values()
            ),
            'collections_analyzed': list(comparison.collection_comparisons.keys()),
            'scalar_keys_analyzed': list(comparison.scalar_comparisons.keys())
        }
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


def load_class_name_mappings() -> Dict[str, str]:
    """Load class name mappings from TSV file."""
    mappings = {}
    mapping_file = Path(__file__).parent.parent.parent / 'class_name_mappings.tsv'
    
    if not mapping_file.exists():
        print(f"Warning: Class name mapping file not found: {mapping_file}")
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
        print(f"Loaded {len(mappings)} class name mappings")
    except Exception as e:
        print(f"Warning: Could not load class name mappings: {e}")
    
    return mappings


def load_enum_name_mappings() -> Dict[str, str]:
    """Load enum name mappings from TSV file."""
    mappings = {}
    mapping_file = Path(__file__).parent.parent.parent / 'enum_name_mappings.tsv'
    
    if not mapping_file.exists():
        print(f"Warning: Enum name mapping file not found: {mapping_file}")
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
        print(f"Loaded {len(mappings)} enum name mappings")
    except Exception as e:
        print(f"Warning: Could not load enum name mappings: {e}")
    
    return mappings


def load_slot_name_mappings() -> Dict[str, str]:
    """Load slot name mappings from TSV file."""
    mappings = {}
    mapping_file = Path(__file__).parent.parent.parent / 'slot_name_mappings.tsv'
    
    if not mapping_file.exists():
        print(f"Warning: Slot name mapping file not found: {mapping_file}")
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
        print(f"Loaded {len(mappings)} slot name mappings")
    except Exception as e:
        print(f"Warning: Could not load slot name mappings: {e}")
    
    return mappings


def load_subset_name_mappings() -> Dict[str, str]:
    """Load subset name mappings from TSV file."""
    mappings = {}
    mapping_file = Path(__file__).parent.parent.parent / 'subset_name_mappings.tsv'
    
    if not mapping_file.exists():
        print(f"Warning: Subset name mapping file not found: {mapping_file}")
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
        print(f"Loaded {len(mappings)} subset name mappings")
    except Exception as e:
        print(f"Warning: Could not load subset name mappings: {e}")
    
    return mappings


def load_inter_type_refactoring() -> List[Tuple[str, str, str, str]]:
    """Load inter-type refactoring mappings from TSV file."""
    mappings = []
    mapping_file = Path(__file__).parent.parent.parent / 'inter_type_refactoring.tsv'
    
    if not mapping_file.exists():
        print(f"Warning: Inter-type refactoring file not found: {mapping_file}")
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
        print(f"Loaded {len(mappings)} inter-type refactoring mappings")
    except Exception as e:
        print(f"Warning: Could not load inter-type refactoring mappings: {e}")
    
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


def get_metamodel_schema_collections() -> Dict[str, str]:
    """Get schema collections from LinkML metamodel dynamically.
    
    Returns:
        Dict mapping slot names to their corresponding all_* method names.
    """
    # Load the metamodel to discover schema_definition slots dynamically
    try:
        meta_view = SchemaView('/Users/MAM/Documents/gitrepos/compare-mixs/main/mixs/meta.yaml')
        
        # Induce the schema_definition class to get its full attribute structure
        schema_def_class = meta_view.get_class('schema_definition', strict=True)
        induced_class = meta_view.induced_class(schema_def_class.name)
        
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
        for slot_name in induced_class.attributes:
            if slot_name in collection_methods:
                schema_collections[slot_name] = collection_methods[slot_name]
                
        return schema_collections
        
    except Exception as e:
        # Fallback to hardcoded collections if metamodel loading fails
        print(f"Warning: Could not load metamodel ({e}), using fallback collections")
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
        print(f"Warning: Could not induce classes ({e})")
    
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
    
    # Further filter out callable methods
    all_attrs = {
        attr for attr in all_attrs 
        if not (callable(getattr(old_element, attr, None)) or callable(getattr(new_element, attr, None)))
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
    import re
    
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
            pass
        
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
    
    env_file = Path(__file__).parent.parent.parent / 'local' / '.env'
    if env_file.exists():
        load_dotenv(env_file)

    headers = {}
    if token := os.getenv('GITHUB_TOKEN'):
        if validate_github_token(token):
            headers['Authorization'] = f'token {token}'
            if VERBOSE_AUTH or not AUTH_MESSAGE_PRINTED:
                print("Using authenticated GitHub API")
                AUTH_MESSAGE_PRINTED = True
        else:
            if VERBOSE_AUTH or not AUTH_MESSAGE_PRINTED:
                print("WARNING: Invalid GitHub token format detected, using unauthenticated API")
                print("Using unauthenticated GitHub API (rate limited)")
                AUTH_MESSAGE_PRINTED = True
    else:
        if VERBOSE_AUTH or not AUTH_MESSAGE_PRINTED:
            print("Using unauthenticated GitHub API (rate limited)")
            AUTH_MESSAGE_PRINTED = True
    return headers


def fetch_tree(commit_sha: str) -> List[str]:
    """Fetch recursive tree from GitHub API and return YAML files.
    
    Args:
        commit_sha: Git commit SHA to fetch tree for.
        
    Returns:
        List of paths to YAML files in the repository at the given commit.
    """
    global API_CALL_COUNT
    headers = get_github_headers()
    url = f"https://api.github.com/repos/GenomicsStandardsConsortium/mixs/git/trees/{commit_sha}?recursive=1"
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


def get_releases() -> List[Tuple[str, datetime]]:
    """Get releases from GitHub API with pagination support.
    
    Returns:
        List of tuples containing (tag_name, published_date) for each release.
    """
    global API_CALL_COUNT
    headers = get_github_headers()
    url = "https://api.github.com/repos/GenomicsStandardsConsortium/mixs/releases"

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


def get_yaml_files_from_release(tag: str) -> Tuple[List[str], str]:
    """Get list of YAML files and commit SHA from a specific release tag.
    
    Args:
        tag: Release tag name to fetch files for.
        
    Returns:
        Tuple of (yaml_files, commit_sha) where yaml_files is a list of YAML file paths
        and commit_sha is the full commit hash for the tag.
    """
    global API_CALL_COUNT
    headers = get_github_headers()
    # Get commit SHA for the tag
    url = f"https://api.github.com/repos/GenomicsStandardsConsortium/mixs/git/refs/tags/{tag}"
    response = requests.get(url, headers=headers, timeout=10)
    API_CALL_COUNT += 1
    response.raise_for_status()
    commit_sha = response.json()['object']['sha']

    yaml_files = fetch_tree(commit_sha)
    return yaml_files, commit_sha


def get_main_branch_info() -> Tuple[List[str], str, datetime]:
    """Get YAML files and commit info from main branch.
    
    Returns:
        Tuple of (yaml_files, commit_sha, commit_date) where yaml_files is a list
        of YAML file paths, commit_sha is the full commit hash, and commit_date
        is the datetime of the commit.
    """
    global API_CALL_COUNT
    headers = get_github_headers()
    # Get main branch commit
    url = "https://api.github.com/repos/GenomicsStandardsConsortium/mixs/branches/main"
    response = requests.get(url, headers=headers, timeout=10)
    API_CALL_COUNT += 1
    response.raise_for_status()
    branch_info = response.json()

    commit_sha = branch_info['commit']['sha']
    commit_date = datetime.fromisoformat(branch_info['commit']['commit']['author']['date'].replace('Z', '+00:00'))

    yaml_files = fetch_tree(commit_sha)
    return yaml_files, commit_sha, commit_date


def get_raw_schema_url(commit_hash: str, mixs_yaml_path: Optional[str]) -> Optional[str]:
    """Get raw GitHub URL for a mixs.yaml file at a specific commit.
    
    Args:
        commit_hash: Git commit hash.
        mixs_yaml_path: Path to mixs.yaml file within the repository.
        
    Returns:
        Raw GitHub URL to the schema file, or None if no path provided.
    """
    if not mixs_yaml_path:
        return None
    return f"https://raw.githubusercontent.com/GenomicsStandardsConsortium/mixs/{commit_hash}/{mixs_yaml_path}"


def build_full_release_info() -> Dict[str, Dict[str, Any]]:
    """Build comprehensive release info dictionary for all releases and main branch.
    
    Returns:
        Dict mapping short commit hashes to release metadata with commit_sha included.
    """
    releases = get_releases()
    release_info = {}

    # Build release info dict
    for tag, date in releases:
        yaml_files, commit_sha = get_yaml_files_from_release(tag)
        short_hash = commit_sha[:7]
        mixs_yaml_path = find_mixs_yaml_path(yaml_files)

        release_info[short_hash] = {
            'tag': tag,
            'date': date.strftime('%Y-%m-%d'),
            'mixs_yaml_path': mixs_yaml_path,
            'commit_sha': commit_sha
        }

    # Add main branch info
    yaml_files, commit_sha, commit_date = get_main_branch_info()
    short_hash = commit_sha[:7]
    mixs_yaml_path = find_mixs_yaml_path(yaml_files)

    release_info[short_hash] = {
        'tag': 'main',
        'date': commit_date.strftime('%Y-%m-%d'),
        'mixs_yaml_path': mixs_yaml_path,
        'commit_sha': commit_sha
    }

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
            print(f"Warning: Schema {schema_tag} missing required 'id' field")
            return False
            
        if not hasattr(schema, 'name') or not schema.name:
            print(f"Warning: Schema {schema_tag} missing required 'name' field")
            return False
            
        # Check if we can access core collections
        try:
            schema_view.all_classes()
            schema_view.all_slots()
        except Exception as e:
            print(f"Warning: Schema {schema_tag} failed basic collection access: {e}")
            return False
            
        return True
        
    except Exception as e:
        print(f"Warning: Schema validation failed for {schema_tag}: {e}")
        return False


def load_schema_views(old_commit: str = DEFAULT_OLD_COMMIT,
                      new_commit: str = DEFAULT_NEW_COMMIT) -> Tuple[
    SchemaView, SchemaView, Dict[str, Any], Dict[str, Any]]:
    """Load SchemaView objects for old and new commits with validation.
    
    Args:
        old_commit: Short commit hash for the old schema version.
        new_commit: Short commit hash for the new schema version.
        
    Returns:
        Tuple of (old_schema, new_schema, old_info, new_info) where:
        - old_schema, new_schema: SchemaView objects for the schemas
        - old_info, new_info: Dict with release metadata (tag, date, etc.)
        
    Raises:
        ValueError: If specified commits are not found or have no mixs.yaml file.
    """
    release_info = build_full_release_info()

    # Get schema info for specified commits
    old_info = release_info.get(old_commit)
    new_info = release_info.get(new_commit)

    if not old_info:
        raise ValueError(f"Old commit {old_commit} not found in releases")
    if not new_info:
        raise ValueError(f"New commit {new_commit} not found in releases")

    # Get raw URLs
    old_url = get_raw_schema_url(old_info['commit_sha'], old_info['mixs_yaml_path'])
    new_url = get_raw_schema_url(new_info['commit_sha'], new_info['mixs_yaml_path'])

    if not old_url:
        raise ValueError(f"No mixs.yaml found for old commit {old_commit} ({old_info['tag']})")
    if not new_url:
        raise ValueError(f"No mixs.yaml found for new commit {new_commit} ({new_info['tag']})")

    print(f"Loading old schema: {old_info['tag']} ({old_commit})")
    print(f"  URL: {old_url}")
    old_schema = SchemaView(old_url)

    print(f"Loading new schema: {new_info['tag']} ({new_commit})")
    print(f"  URL: {new_url}")
    new_schema = SchemaView(new_url)
    
    # Validate schemas
    print(f"Validating schemas as LinkML SchemaDefinitions...")
    old_valid = validate_schema_definition(old_schema, old_info['tag'])
    new_valid = validate_schema_definition(new_schema, new_info['tag'])
    
    if not old_valid or not new_valid:
        print("Warning: Schema validation issues detected, but proceeding with comparison")

    return old_schema, new_schema, old_info, new_info


def print_releases() -> None:
    """Print all releases with tag and date."""
    releases = get_releases()
    for tag, date in releases:
        print(f"{tag}: {date.strftime('%Y-%m-%d')}")


def build_release_info_dict() -> Dict[str, Dict[str, Any]]:
    """Build release info dictionary with all releases and main branch info (with optional display output).
    
    Returns:
        Dict mapping short commit hashes to release metadata.
    """
    release_info = build_full_release_info()

    if SHOW_YAML_FILES:
        # Print output for each release (excluding main for now)
        releases = get_releases()
        for tag, date in releases:
            yaml_files, commit_sha = get_yaml_files_from_release(tag)
            short_hash = commit_sha[:7]

            print(f"\n{tag}: {date.strftime('%Y-%m-%d')} ({short_hash})")
            for yaml_file in yaml_files:
                print(f"  {yaml_file}")

        # Add main branch info display
        yaml_files, commit_sha, commit_date = get_main_branch_info()
        short_hash = commit_sha[:7]

        print(f"\nmain: {commit_date.strftime('%Y-%m-%d')} ({short_hash})")
        for yaml_file in yaml_files:
            print(f"  {yaml_file}")

    # Return the simplified dict (without commit_sha for backward compatibility)
    return {k: {key: val for key, val in v.items() if key != 'commit_sha'}
            for k, v in release_info.items()}


if __name__ == "__main__":
    # Load name mappings
    CLASS_NAME_MAPPINGS = load_class_name_mappings()
    ENUM_NAME_MAPPINGS = load_enum_name_mappings()
    SLOT_NAME_MAPPINGS = load_slot_name_mappings()
    SUBSET_NAME_MAPPINGS = load_subset_name_mappings()
    INTER_TYPE_REFACTORING = load_inter_type_refactoring()

    # Build and display release info
    release_info = build_release_info_dict()

    # Print the dictionary
    separator = "=" * 50
    print(f"\n{separator}")
    print("Release Info Dictionary:")
    print(separator)
    pprint.pprint(release_info)

    # Save as YAML file
    output_file = Path(__file__).parent.parent.parent / "local" / "mixs_releases.yaml"
    with open(output_file, 'w') as f:
        yaml.dump(release_info, f, default_flow_style=False, sort_keys=False)
    print(f"\nSaved release info to: {output_file}")

    # Load and compare schemas
    print("\n" + "=" * 50)
    print("Loading schemas for comparison...")
    print("=" * 50)

    try:
        old_schema, new_schema, old_info, new_info = load_schema_views(
            DEFAULT_OLD_COMMIT, DEFAULT_NEW_COMMIT
        )

        print("\nOld schema info:")
        pprint.pprint(old_info)

        print("\nNew schema info:")
        pprint.pprint(new_info)

        # Initialize the comparator and run the comparison
        print("\n" + "=" * 80)
        print("RUNNING NEW SYSTEMATIC LINKML COMPARISON FRAMEWORK")
        print("=" * 80)
        comparator = LinkMLComparator(old_schema, new_schema, old_info, new_info)
        comparison_results = comparator.compare_schemas()

        # Convert results to a dictionary
        comparison_dict = schema_comparison_to_dict(comparison_results)

        # Save the results to a YAML file
        output_file = Path(__file__).parent.parent.parent / "local" / "schema_comparison_results.yaml"
        with open(output_file, 'w') as f:
            yaml.dump(comparison_dict, f, default_flow_style=False, sort_keys=False)
        
        summary = comparison_dict.get('summary', {})
        print("\n" + "=" * 50)
        print("SAVING COMPARISON RESULTS TO YAML")
        print("=" * 50)
        print(f"Saved systematic comparison results to: {output_file}")
        print(f"  • Scalar differences: {summary.get('total_scalar_differences', 0)}")
        print(f"  • Collection differences: {summary.get('total_collection_differences', 0)}")
        print(f"  • Total schema elements compared: {summary.get('total_schema_elements_compared', 0)}")


        # Optionally, print a summary report to the console
        print_schema_comparison_report(comparison_results)

    except ValueError as e:
        print(f"\nERROR: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

    print("\n" + "=" * 50)
    print(f"API Usage Summary: {API_CALL_COUNT} GitHub API calls made")
    print("=" * 50)