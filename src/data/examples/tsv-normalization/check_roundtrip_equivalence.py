#!/usr/bin/env python3
"""
Assert that two YAML data files hold equivalent data.

Used by the `tsv-roundtrip-test` Makefile target to prove that multivalued MIxS
data survives a YAML -> bare-pipe TSV -> YAML round-trip without loss. Exits
non-zero (and prints the first differences) if the two files differ.
"""
import sys
import yaml


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit("usage: check_roundtrip_equivalence.py <original.yaml> <roundtripped.yaml>")
    original_path, roundtrip_path = sys.argv[1], sys.argv[2]
    original = yaml.safe_load(open(original_path))
    roundtrip = yaml.safe_load(open(roundtrip_path))

    if original == roundtrip:
        print(f"round-trip equivalence OK: {original_path} == {roundtrip_path}")
        return

    print("ROUND-TRIP MISMATCH")
    print(f"  original:     {original_path}")
    print(f"  round-tripped: {roundtrip_path}")
    # Show the first few concrete differences to make failures actionable.
    orig_rows = original if isinstance(original, list) else [original]
    rt_rows = roundtrip if isinstance(roundtrip, list) else [roundtrip]
    if len(orig_rows) != len(rt_rows):
        print(f"  row count: original {len(orig_rows)} vs round-tripped {len(rt_rows)}")
    shown = 0
    for i, (a, b) in enumerate(zip(orig_rows, rt_rows)):
        if a == b:
            continue
        keys = set(a) | set(b) if isinstance(a, dict) and isinstance(b, dict) else set()
        for k in sorted(keys):
            if a.get(k) != b.get(k):
                print(f"  row {i} field {k!r}: {a.get(k)!r} != {b.get(k)!r}")
                shown += 1
                if shown >= 10:
                    sys.exit(1)
    sys.exit(1)


if __name__ == "__main__":
    main()
