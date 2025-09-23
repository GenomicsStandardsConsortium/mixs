#!/usr/bin/env python3
"""
Validate mapping TSV files against actual schema elements.

Checks that all old_name and new_name values in mapping files
actually exist in the corresponding schemas.
"""

from linkml_runtime.utils.schemaview import SchemaView
from pathlib import Path
import sys

# Schema URLs
OLD_SCHEMA_URL = 'https://raw.githubusercontent.com/GenomicsStandardsConsortium/mixs/74744eea9b149b0587b58f48e3dd8d1f879820d2/model/schema/mixs.yaml'
NEW_SCHEMA_URL = 'https://raw.githubusercontent.com/GenomicsStandardsConsortium/mixs/994c7450cc4b974e0ed36d42b1b0cf956f38064c/src/mixs/schema/mixs.yaml'

def load_tsv_mappings(file_path: Path):
    """Load mappings from TSV file."""
    mappings = []
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i == 0:  # Skip header
                    continue
                parts = line.strip().split('\t')
                if len(parts) >= 2:
                    old_name, new_name = parts[0], parts[1]
                    if old_name and new_name:  # Skip empty values
                        mappings.append((old_name, new_name))
                elif len(parts) == 1 and parts[0]:
                    # Handle incomplete mappings (old_name only)
                    mappings.append((parts[0], None))
        return mappings
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return []

def check_mapping_duplicates(mappings, element_type):
    """Check for one-to-many and many-to-one mappings."""
    # Filter out incomplete mappings for duplicate checking
    complete_mappings = [(old, new) for old, new in mappings if new is not None]
    
    # Check one-to-many (one old maps to multiple new)
    old_to_new = {}
    for old_name, new_name in complete_mappings:
        if old_name in old_to_new:
            old_to_new[old_name].append(new_name)
        else:
            old_to_new[old_name] = [new_name]
    
    one_to_many_errors = 0
    for old_name, new_names in old_to_new.items():
        if len(new_names) > 1:
            print(f"❌ ONE-TO-MANY: '{old_name}' maps to multiple {element_type}s: {', '.join(new_names)}")
            one_to_many_errors += 1
    
    # Check many-to-one (multiple old map to same new)
    new_to_old = {}
    for old_name, new_name in complete_mappings:
        if new_name in new_to_old:
            new_to_old[new_name].append(old_name)
        else:
            new_to_old[new_name] = [old_name]
    
    many_to_one_errors = 0
    for new_name, old_names in new_to_old.items():
        if len(old_names) > 1:
            print(f"❌ MANY-TO-ONE: Multiple {element_type}s map to '{new_name}': {', '.join(old_names)}")
            many_to_one_errors += 1
    
    return one_to_many_errors + many_to_one_errors

def validate_class_mappings(old_schema: SchemaView, new_schema: SchemaView):
    """Validate class name mappings."""
    print("=== Validating class_name_mappings.tsv ===")
    
    mapping_file = Path("class_name_mappings.tsv")
    if not mapping_file.exists():
        print(f"File not found: {mapping_file}")
        return
    
    mappings = load_tsv_mappings(mapping_file)
    print(f"Loaded {len(mappings)} mappings")
    
    # Get all class names
    old_classes = set(old_schema.all_classes(imports=True).keys())
    new_classes = set(new_schema.all_classes(imports=True).keys())
    
    print(f"Old schema has {len(old_classes)} classes")
    print(f"New schema has {len(new_classes)} classes")
    
    errors = 0
    
    # Check for missing elements
    for old_name, new_name in mappings:
        if old_name not in old_classes:
            print(f"❌ OLD NOT FOUND: '{old_name}' not in old schema classes")
            errors += 1
        
        if new_name and new_name not in new_classes:
            print(f"❌ NEW NOT FOUND: '{new_name}' not in new schema classes")
            errors += 1
    
    # Check for duplicate mappings
    duplicate_errors = check_mapping_duplicates(mappings, "class")
    errors += duplicate_errors
    
    if errors == 0:
        print("✅ All class mappings are valid!")
    print()

def validate_enum_mappings(old_schema: SchemaView, new_schema: SchemaView):
    """Validate enum name mappings."""
    print("=== Validating enum_name_mappings.tsv ===")
    
    mapping_file = Path("enum_name_mappings.tsv")
    if not mapping_file.exists():
        print(f"File not found: {mapping_file}")
        return
    
    mappings = load_tsv_mappings(mapping_file)
    print(f"Loaded {len(mappings)} mappings")
    
    # Get all enum names
    old_enums = set(old_schema.all_enums(imports=True).keys())
    new_enums = set(new_schema.all_enums(imports=True).keys())
    
    print(f"Old schema has {len(old_enums)} enums")
    print(f"New schema has {len(new_enums)} enums")
    
    errors = 0
    
    # Check for missing elements
    for old_name, new_name in mappings:
        if old_name not in old_enums:
            print(f"❌ OLD NOT FOUND: '{old_name}' not in old schema enums")
            errors += 1
        
        if new_name and new_name not in new_enums:
            print(f"❌ NEW NOT FOUND: '{new_name}' not in new schema enums")
            errors += 1
    
    # Check for duplicate mappings
    duplicate_errors = check_mapping_duplicates(mappings, "enum")
    errors += duplicate_errors
    
    if errors == 0:
        print("✅ All enum mappings are valid!")
    print()

def validate_slot_mappings(old_schema: SchemaView, new_schema: SchemaView):
    """Validate slot name mappings."""
    print("=== Validating slot_name_mappings.tsv ===")
    
    mapping_file = Path("slot_name_mappings.tsv")
    if not mapping_file.exists():
        print(f"File not found: {mapping_file}")
        return
    
    mappings = load_tsv_mappings(mapping_file)
    print(f"Loaded {len(mappings)} mappings")
    
    # Get all slot names
    old_slots = set(old_schema.all_slots(imports=True).keys())
    new_slots = set(new_schema.all_slots(imports=True).keys())
    
    print(f"Old schema has {len(old_slots)} slots")
    print(f"New schema has {len(new_slots)} slots")
    
    errors = 0
    incomplete_mappings = []
    
    # Check for missing elements
    for old_name, new_name in mappings:
        if old_name not in old_slots:
            print(f"❌ OLD NOT FOUND: '{old_name}' not in old schema slots")
            errors += 1
        
        if new_name:
            if new_name not in new_slots:
                print(f"❌ NEW NOT FOUND: '{new_name}' not in new schema slots")
                errors += 1
        else:
            incomplete_mappings.append(old_name)
    
    # Check for duplicate mappings
    duplicate_errors = check_mapping_duplicates(mappings, "slot")
    errors += duplicate_errors
    
    if incomplete_mappings:
        print(f"📝 Found {len(incomplete_mappings)} incomplete mappings (old_name only):")
        for old_name in incomplete_mappings:
            print(f"  📝 '{old_name}' (missing new_name)")
    
    if errors == 0:
        print("✅ All slot mappings are valid!")
    print()

def validate_subset_mappings(old_schema: SchemaView, new_schema: SchemaView):
    """Validate subset name mappings."""
    print("=== Validating subset_name_mappings.tsv ===")
    
    mapping_file = Path("subset_name_mappings.tsv")
    if not mapping_file.exists():
        print(f"File not found: {mapping_file}")
        return
    
    mappings = load_tsv_mappings(mapping_file)
    print(f"Loaded {len(mappings)} mappings")
    
    # Get all subset names
    old_subsets = set(old_schema.all_subsets(imports=True).keys())
    new_subsets = set(new_schema.all_subsets(imports=True).keys())
    
    print(f"Old schema has {len(old_subsets)} subsets")
    print(f"New schema has {len(new_subsets)} subsets")
    
    errors = 0
    
    # Check for missing elements
    for old_name, new_name in mappings:
        if old_name not in old_subsets:
            print(f"❌ OLD NOT FOUND: '{old_name}' not in old schema subsets")
            errors += 1
        
        if new_name and new_name not in new_subsets:
            print(f"❌ NEW NOT FOUND: '{new_name}' not in new schema subsets")
            errors += 1
    
    # Check for duplicate mappings
    duplicate_errors = check_mapping_duplicates(mappings, "subset")
    errors += duplicate_errors
    
    if errors == 0:
        print("✅ All subset mappings are valid!")
    print()

def validate_inter_type_refactoring(old_schema: SchemaView, new_schema: SchemaView):
    """Validate inter-type refactoring mappings."""
    print("=== Validating inter_type_refactoring.tsv ===")
    
    mapping_file = Path("inter_type_refactoring.tsv")
    if not mapping_file.exists():
        print(f"File not found: {mapping_file}")
        return
    
    mappings = []
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
    except Exception as e:
        print(f"Error loading {mapping_file}: {e}")
        return
    
    print(f"Loaded {len(mappings)} inter-type refactoring mappings")
    
    # Get all element names by type
    old_slots = set(old_schema.all_slots(imports=True).keys())
    new_slots = set(new_schema.all_slots(imports=True).keys())
    old_subsets = set(old_schema.all_subsets(imports=True).keys())
    new_subsets = set(new_schema.all_subsets(imports=True).keys())
    old_classes = set(old_schema.all_classes(imports=True).keys())
    new_classes = set(new_schema.all_classes(imports=True).keys())
    old_enums = set(old_schema.all_enums(imports=True).keys())
    new_enums = set(new_schema.all_enums(imports=True).keys())
    
    type_to_old_elements = {
        'slot': old_slots,
        'subset': old_subsets,
        'class': old_classes,
        'enum': old_enums
    }
    
    type_to_new_elements = {
        'slot': new_slots,
        'subset': new_subsets,
        'class': new_classes,
        'enum': new_enums
    }
    
    errors = 0
    
    # Check for missing elements
    for old_type, old_name, new_type, new_name in mappings:
        # Check old element exists
        if old_type not in type_to_old_elements:
            print(f"❌ INVALID OLD TYPE: '{old_type}' not a valid element type")
            errors += 1
        elif old_name not in type_to_old_elements[old_type]:
            print(f"❌ OLD NOT FOUND: '{old_name}' not in old schema {old_type}s")
            errors += 1
        
        # Check new element exists
        if new_type not in type_to_new_elements:
            print(f"❌ INVALID NEW TYPE: '{new_type}' not a valid element type")
            errors += 1
        elif new_name not in type_to_new_elements[new_type]:
            print(f"❌ NEW NOT FOUND: '{new_name}' not in new schema {new_type}s")
            errors += 1
    
    if errors == 0:
        print("✅ All inter-type refactoring mappings are valid!")
    print()

def main():
    """Main validation function."""
    print("Loading schemas...")
    
    try:
        old_schema = SchemaView(OLD_SCHEMA_URL)
        print("✅ Loaded old schema (mixs6.0.0)")
    except Exception as e:
        print(f"❌ Error loading old schema: {e}")
        sys.exit(1)
    
    try:
        new_schema = SchemaView(NEW_SCHEMA_URL)
        print("✅ Loaded new schema (main)")
    except Exception as e:
        print(f"❌ Error loading new schema: {e}")
        sys.exit(1)
    
    print()
    
    # Validate each mapping file
    validate_class_mappings(old_schema, new_schema)
    validate_enum_mappings(old_schema, new_schema)
    validate_slot_mappings(old_schema, new_schema)
    validate_subset_mappings(old_schema, new_schema)
    validate_inter_type_refactoring(old_schema, new_schema)
    
    print("Validation complete!")

if __name__ == "__main__":
    main()