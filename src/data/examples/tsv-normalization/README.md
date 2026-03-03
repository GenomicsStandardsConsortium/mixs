# TSV List Normalization Demo

Demonstrates the problem of heterogeneous list formatting in MIxS TSV data
and a schema-aware normalization workflow.

## The Problem

MIxS descriptions say multivalued fields "can be separated by pipes", but
submitters format them inconsistently:

| Style | Example | Parseable? |
|-------|---------|------------|
| Bracketed pipes | `[chisel\|ridge till]` | Yes (json_flattener default) |
| Bare pipes | `chisel\|ridge till` | **No** — treated as single string |
| Spaced pipes | `chisel \| ridge till` | **No** — treated as single string |

The `linkml-convert` TSV loader (via `json_flattener`) requires `[square bracket]`
wrapping to recognize list values. Without brackets, pipes are literal text,
causing enum validation errors or silently wrong data.

## Files

- `MimsSoil-messy-lists.tsv` — 4 rows with 3 different list formatting styles
- `normalize_tsv_lists.py` — Schema-aware normalizer that reads multivalued
  slot definitions from the LinkML schema and rewrites all list values to
  canonical `[pipe|delimited]` format
- `MimsSoil-normalized-lists.tsv` — Output after normalization (generated)

## Usage

```bash
# Step 1: Normalize messy TSV (uses schema to identify multivalued slots)
make normalize-tsv-demo

# Step 2: Verify normalized TSV loads cleanly
make normalize-tsv-roundtrip
```

## What This Demonstrates

1. **Schema awareness matters**: The normalizer uses `SchemaView` to find
   which columns are multivalued — it only touches those columns
2. **Bracket format is currently required**: `json_flattener` 0.1.9 only
   recognizes `[a|b|c]` as a list; bare `a|b|c` is treated as a single value
3. **Future**: linkml PR #3134 added `--list-wrapper` and `--list-delimiter`
   CLI flags to `linkml-convert`, but the runtime/json_flattener plumbing
   (linkml/linkml#3147) needs updating before they work end-to-end

## Related Issues

- [linkml#2581](https://github.com/linkml/linkml/issues/2581) — Configurable inlined multivalued strings syntax
- [linkml#3147](https://github.com/linkml/linkml/issues/3147) — Validator CSV/TSV loader lacks schema-aware parsing
- [mixs#1060](https://github.com/GenomicsStandardsConsortium/mixs/issues/1060) — Cardinality and syntax of env triad slots
