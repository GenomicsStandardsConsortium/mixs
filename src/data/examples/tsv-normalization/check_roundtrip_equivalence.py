#!/usr/bin/env python3
"""
Assert that two YAML data files hold equivalent data.

Used by the `tsv-roundtrip-test` Makefile target to prove that multivalued MIxS
data survives a YAML -> bare-pipe TSV -> YAML round-trip without loss. Exits
non-zero (and prints the first concrete differences) if the two files differ.
"""
import sys

import yaml


def load(path):
    with open(path) as fh:
        return yaml.safe_load(fh)


def iter_records(data):
    """Yield (label, record) pairs to compare.

    The round-trip data is a dict with a single slot holding a list of records,
    e.g. {"mims_soil_data": [{...}, {...}]}. Unwrap that into per-record rows so a
    mismatch points at one record and field rather than reporting the whole
    top-level key as a single huge difference.
    """
    if isinstance(data, dict) and len(data) == 1:
        (slot, value), = data.items()
        if isinstance(value, list):
            return [(f"{slot}[{i}]", rec) for i, rec in enumerate(value)]
    if isinstance(data, list):
        return [(f"[{i}]", rec) for i, rec in enumerate(data)]
    return [("", data)]


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit("usage: check_roundtrip_equivalence.py <original.yaml> <roundtripped.yaml>")
    original_path, roundtrip_path = sys.argv[1], sys.argv[2]
    original = load(original_path)
    roundtrip = load(roundtrip_path)

    if original == roundtrip:
        print(f"round-trip equivalence OK: {original_path} == {roundtrip_path}")
        return

    print("ROUND-TRIP MISMATCH")
    print(f"  original:      {original_path}")
    print(f"  round-tripped: {roundtrip_path}")

    orig_rows = iter_records(original)
    rt_rows = iter_records(roundtrip)
    if len(orig_rows) != len(rt_rows):
        print(f"  record count: original {len(orig_rows)} vs round-tripped {len(rt_rows)}")

    shown = 0
    for (label, a), (_, b) in zip(orig_rows, rt_rows):
        if a == b:
            continue
        if isinstance(a, dict) and isinstance(b, dict):
            for k in sorted(set(a) | set(b)):
                if a.get(k) != b.get(k):
                    print(f"  {label} field {k!r}: {a.get(k)!r} != {b.get(k)!r}")
                    shown += 1
                    if shown >= 10:
                        sys.exit(1)
        else:
            # Fallback when the records are not both dicts: show the whole-record
            # difference so the failure is still actionable.
            print(f"  {label}: {a!r} != {b!r}")
            shown += 1
            if shown >= 10:
                sys.exit(1)
    sys.exit(1)


if __name__ == "__main__":
    main()
