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

Without `--list-wrapper` / `--list-delimiter` flags, `linkml-convert`'s TSV
loader (via `json_flattener`) requires `[square bracket]` wrapping to recognize
list values. Bare pipes are treated as literal text, causing enum validation
errors or silently wrong data.

With linkml PR [#3134](https://github.com/linkml/linkml/pull/3134) (merged
2026-02-27, not yet in a PyPI release), `linkml-convert` can load and dump
all three styles using `--list-wrapper none`:

```bash
# Load bare-pipe TSV → YAML
linkml-convert -s schema.yaml -C MixsCompliantData -S mims_soil_data \
  -f tsv -t yaml --list-wrapper none --no-validate input.tsv

# Dump YAML → bare-pipe TSV
linkml-convert -s schema.yaml -C MixsCompliantData -S mims_soil_data \
  -f yaml -t tsv --list-wrapper none --no-validate input.yaml
```

Until the next linkml release, both `linkml` and `linkml-runtime` must be
installed from git main to avoid version skew
([linkml#3241](https://github.com/linkml/linkml/issues/3241)).

**Note:** `linkml-validate` uses a completely separate CSV/TSV loader (raw
`csv.DictReader`, no json_flattener) that does not support these flags. TSV
validation of multivalued fields is tracked in
[linkml#3147](https://github.com/linkml/linkml/issues/3147).

## Files

- `MimsSoil-messy-lists.tsv` — 4 rows with 3 different list formatting styles
- `normalize_tsv_lists.py` — Schema-aware normalizer that reads multivalued
  slot definitions from the LinkML schema and rewrites all list values to
  canonical `[pipe|delimited]` format
- `MimsSoil-normalized-lists.tsv` — Output after normalization (generated)
- `MimsSoil-bare-pipes.tsv` — Output after dumping with `--list-wrapper none` (generated)

## Usage

All targets below are standalone demos, not part of `make all` or `make test`.

```bash
# Step 1: Normalize messy TSV (uses schema to identify multivalued slots)
make normalize-tsv-demo

# Step 2: Round-trip normalized TSV through linkml-convert (bracket format)
make normalize-tsv-roundtrip

# Step 3: Dump YAML → bare-pipe TSV using --list-wrapper none
make src/data/examples/tsv-normalization/MimsSoil-bare-pipes.tsv

# Step 4: Full bare-pipe round-trip (dump + load; load blocked by linkml#3250)
make tsv-bare-pipe-roundtrip
```

## What This Demonstrates

1. **Schema awareness matters**: The normalizer uses `SchemaView` to find
   which columns are multivalued — it only touches those columns
2. **Bracket format was previously required**: `json_flattener` only recognized
   `[a|b|c]` as a list; bare `a|b|c` was treated as a single value
3. **`--list-wrapper none` dump works**: With both linkml packages from git main,
   `linkml-convert` dumps bare-pipe format correctly. Loading crashes on empty
   multivalued cells ([linkml#3250](https://github.com/linkml/linkml/issues/3250))
4. **Validator gap remains**: `linkml-validate` and `linkml examples` still
   cannot parse multivalued TSV fields ([linkml#3147](https://github.com/linkml/linkml/issues/3147))

## Related Issues

- [linkml#3134](https://github.com/linkml/linkml/pull/3134) — Configurable list formatting (merged, awaiting release)
- [linkml#3241](https://github.com/linkml/linkml/issues/3241) — Version skew crash when packages are from different sources
- [linkml#3147](https://github.com/linkml/linkml/issues/3147) — Validator CSV/TSV loader lacks schema-aware parsing
- [linkml#3250](https://github.com/linkml/linkml/issues/3250) — Empty multivalued cells crash loader with `--list-wrapper none`
- [linkml#2581](https://github.com/linkml/linkml/issues/2581) — Original feature request for configurable list syntax
- [mixs#1060](https://github.com/GenomicsStandardsConsortium/mixs/issues/1060) — Cardinality and syntax of env triad slots
