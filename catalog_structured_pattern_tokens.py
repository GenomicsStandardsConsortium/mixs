#!/usr/bin/env python3
"""
Script to catalog all tokens used in structured_pattern.syntax fields
from both slots and class slot_usage in a LinkML YAML schema.
"""

import yaml
import re
import sys
from collections import defaultdict, Counter
from pathlib import Path

def extract_tokens_from_syntax(syntax_string):
    """Extract all tokens wrapped in curly brackets from a syntax string."""
    if not syntax_string:
        return []
    
    # Find all {token} patterns, but exclude regex quantifiers like {1,2}
    tokens = re.findall(r'\{([^}]+)\}', syntax_string)
    
    # Filter out regex quantifiers (numbers, commas, ranges)
    filtered_tokens = []
    for token in tokens:
        # Skip if it's just numbers/commas (regex quantifiers)
        if re.match(r'^[\d,]+$', token):
            continue
        filtered_tokens.append(token)
    
    return filtered_tokens

def analyze_schema(yaml_file_path):
    """Analyze a LinkML YAML schema for structured_pattern tokens."""
    
    with open(yaml_file_path, 'r') as f:
        schema = yaml.safe_load(f)
    
    all_tokens = []
    token_locations = defaultdict(list)
    
    # Check slots for structured_pattern
    if 'slots' in schema:
        for slot_name, slot_def in schema['slots'].items():
            if isinstance(slot_def, dict) and 'structured_pattern' in slot_def:
                syntax = slot_def['structured_pattern'].get('syntax', '')
                tokens = extract_tokens_from_syntax(syntax)
                
                for token in tokens:
                    all_tokens.append(token)
                    token_locations[token].append(f"slots.{slot_name}.structured_pattern.syntax")
    
    # Check classes for slot_usage structured_pattern
    if 'classes' in schema:
        for class_name, class_def in schema['classes'].items():
            if isinstance(class_def, dict) and 'slot_usage' in class_def:
                for slot_name, slot_usage in class_def['slot_usage'].items():
                    if isinstance(slot_usage, dict) and 'structured_pattern' in slot_usage:
                        syntax = slot_usage['structured_pattern'].get('syntax', '')
                        tokens = extract_tokens_from_syntax(syntax)
                        
                        for token in tokens:
                            all_tokens.append(token)
                            token_locations[token].append(f"classes.{class_name}.slot_usage.{slot_name}.structured_pattern.syntax")
    
    # Get defined settings
    defined_settings = set()
    if 'settings' in schema:
        defined_settings = set(schema['settings'].keys())
    
    # Count token usage
    token_counts = Counter(all_tokens)
    unique_tokens = set(all_tokens)
    
    return {
        'token_counts': dict(token_counts),
        'token_locations': dict(token_locations),
        'defined_settings': list(defined_settings),
        'unique_tokens': list(unique_tokens)
    }

def main():
    if len(sys.argv) != 2:
        print("Usage: python catalog_structured_pattern_tokens.py <path_to_mixs.yaml>")
        sys.exit(1)
    
    yaml_file = sys.argv[1]
    
    if not Path(yaml_file).exists():
        print(f"Error: File {yaml_file} does not exist")
        sys.exit(1)
    
    print(f"Analyzing structured_pattern tokens in: {yaml_file}")
    print("=" * 80)
    
    results = analyze_schema(yaml_file)
    
    # Summary statistics
    print(f"\nSUMMARY:")
    print(f"Total tokens found: {len(results['token_counts'])}")
    print(f"Unique tokens: {len(results['unique_tokens'])}")
    print(f"Defined settings: {len(results['defined_settings'])}")
    
    # Missing settings
    missing_tokens = set(results['unique_tokens']) - set(results['defined_settings'])
    if missing_tokens:
        print(f"\nMISSING SETTINGS ({len(missing_tokens)}):")
        for token in sorted(missing_tokens):
            print(f"  - {token}")
    
    # Unused settings
    unused_settings = set(results['defined_settings']) - set(results['unique_tokens'])
    if unused_settings:
        print(f"\nUNUSED SETTINGS ({len(unused_settings)}):")
        for setting in sorted(unused_settings):
            print(f"  - {setting}")
    
    # Detailed token locations
    print(f"\nALL TOKEN USAGE:")
    for token in sorted(results['unique_tokens']):
        status = "✅" if token in results['defined_settings'] else "❌"
        print(f"\n{status} {token} ({results['token_counts'][token]} uses):")
        for location in results['token_locations'][token]:
            print(f"    {location}")
    
    # Save complete results to YAML
    output_file = Path.cwd() / "structured_pattern_analysis.yaml"
    
    # Create structure for used but undefined settings (empty if none)
    used_but_undefined_settings = {}
    for token in sorted(missing_tokens):
        used_but_undefined_settings[token] = None
    
    # Add derived analysis to results
    results['missing_settings'] = sorted(missing_tokens)
    results['unused_settings'] = sorted(unused_settings)
    results['used_but_undefined_settings'] = used_but_undefined_settings
    results['analysis_summary'] = {
        'total_token_instances': len([token for tokens in results['token_locations'].values() for token in tokens]),
        'unique_token_count': len(results['unique_tokens']),
        'defined_settings_count': len(results['defined_settings']),
        'missing_settings_count': len(missing_tokens),
        'unused_settings_count': len(unused_settings)
    }
    
    with open(output_file, 'w') as f:
        yaml.dump(results, f, default_flow_style=False, sort_keys=True)
    
    print(f"\nComplete analysis saved to: {output_file}")

if __name__ == "__main__":
    main()