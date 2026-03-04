#!/usr/bin/env python3
"""Normalize heterogeneous list formatting in MIxS TSV files.

Demonstrates the problem: MIxS data submitters use inconsistent list syntax
in TSV files. Some wrap multivalued fields in [square brackets], some use
bare pipes, some add whitespace around delimiters. The linkml CSV/TSV loader
(via json_flattener) requires [bracket|delimited] syntax to recognize lists.

This script uses SchemaView to identify multivalued slots, then normalizes
all list values to canonical [pipe|delimited] format so linkml-convert can
parse them correctly.

Usage:
    python normalize_tsv_lists.py \\
        --schema src/mixs/schema/mixs.yaml \\
        --target-class MimsSoil \\
        --input messy.tsv \\
        --output normalized.tsv

See also:
    - linkml/linkml#2581  Configurable inlined multivalued strings syntax
    - linkml/linkml#3147  Validator CSV/TSV loader lacks schema-aware parsing
    - GSC/mixs#1060       Cardinality and syntax of env triad slots
"""

import argparse
import csv
import sys
from pathlib import Path

from linkml_runtime.utils.schemaview import SchemaView


def get_multivalued_slots(schema_path: str, target_class: str) -> set[str]:
    """Return set of slot names that are multivalued for the given class."""
    sv = SchemaView(schema_path)
    mv_slots = set()
    for slot_name in sv.class_slots(target_class):
        slot = sv.induced_slot(slot_name, target_class)
        if slot and slot.multivalued:
            mv_slots.add(slot_name)
    return mv_slots


def normalize_list_value(value: str) -> str:
    """Normalize a multivalued field value to canonical [pipe|delimited] format.

    Handles these real-world variants:
        [a|b|c]       -> [a|b|c]       (already canonical)
        a|b|c         -> [a|b|c]       (bare pipes)
        a | b | c     -> [a|b|c]       (spaced pipes)
        [a | b | c]   -> [a|b|c]       (brackets + spaced pipes)
        a             -> a             (single value, no change)
        (empty)       -> (empty)       (missing data, no change)
    """
    if not value or not value.strip():
        return value

    stripped = value.strip()

    # Remove outer brackets if present
    inner = stripped
    if len(inner) >= 2 and inner[0] == '[' and inner[-1] == ']':
        inner = inner[1:-1]

    # Split on pipe, strip whitespace from each element
    parts = [p.strip() for p in inner.split('|')]

    # Filter out empty parts from edge cases like trailing pipes
    parts = [p for p in parts if p]

    if len(parts) == 0:
        return value
    elif len(parts) == 1:
        # Single value — no brackets needed
        return parts[0]
    else:
        # Multiple values — canonical bracket format
        return '[' + '|'.join(parts) + ']'


def normalize_tsv(
    input_path: Path,
    output_path: Path,
    multivalued_slots: set[str],
) -> dict:
    """Read a TSV, normalize multivalued fields, write result.

    Returns a stats dict with counts of changes made.
    """
    stats = {
        'rows_processed': 0,
        'cells_already_canonical': 0,
        'cells_normalized': 0,
        'cells_single_or_empty': 0,
    }

    with open(input_path, newline='') as inf:
        reader = csv.DictReader(inf, delimiter='\t')
        fieldnames = reader.fieldnames

        with open(output_path, 'w', newline='') as outf:
            writer = csv.DictWriter(outf, fieldnames=fieldnames, delimiter='\t')
            writer.writeheader()

            for row in reader:
                stats['rows_processed'] += 1
                normalized_row = {}
                for col, val in row.items():
                    if col in multivalued_slots and val:
                        new_val = normalize_list_value(val)
                        if new_val != val:
                            stats['cells_normalized'] += 1
                        elif '|' in val:
                            stats['cells_already_canonical'] += 1
                        else:
                            stats['cells_single_or_empty'] += 1
                        normalized_row[col] = new_val
                    else:
                        normalized_row[col] = val
                writer.writerow(normalized_row)

    return stats


def main():
    parser = argparse.ArgumentParser(
        description='Normalize heterogeneous list formatting in MIxS TSV files.'
    )
    parser.add_argument(
        '--schema', required=True,
        help='Path to LinkML schema YAML'
    )
    parser.add_argument(
        '--target-class', required=True,
        help='Name of the class whose slots to inspect (e.g., MimsSoil)'
    )
    parser.add_argument(
        '--input', required=True,
        help='Input TSV file with potentially messy list formatting'
    )
    parser.add_argument(
        '--output', required=True,
        help='Output TSV file with normalized list formatting'
    )
    args = parser.parse_args()

    mv_slots = get_multivalued_slots(args.schema, args.target_class)
    print(f'Found {len(mv_slots)} multivalued slots in {args.target_class}:', file=sys.stderr)
    for s in sorted(mv_slots):
        print(f'  {s}', file=sys.stderr)

    stats = normalize_tsv(
        Path(args.input),
        Path(args.output),
        mv_slots,
    )

    print(f'\nNormalization complete:', file=sys.stderr)
    print(f'  Rows processed:        {stats["rows_processed"]}', file=sys.stderr)
    print(f'  Cells normalized:      {stats["cells_normalized"]}', file=sys.stderr)
    print(f'  Cells already correct: {stats["cells_already_canonical"]}', file=sys.stderr)
    print(f'  Cells single/empty:    {stats["cells_single_or_empty"]}', file=sys.stderr)


if __name__ == '__main__':
    main()
