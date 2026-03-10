# TSV List Format Normalization and Bare-Pipe Round-Trip Demo

This directory demonstrates two things:

1. **The mixed-format problem** — real-world MIxS TSV files contain
   inconsistent list syntax, and `linkml-convert` expects one style per file.
2. **The bare-pipe round-trip** — with recent linkml features, MIxS data can
   be dumped and loaded as bare-pipe TSV (no brackets) via `linkml-convert`.

## Background: Why List Formatting Matters

MIxS slot descriptions say multivalued fields "can be separated by pipes",
but submitters format them inconsistently:

| Style | Example | `linkml-convert` default | `--list-wrapper none` |
|-------|---------|--------------------------|----------------------|
| Bracketed pipes | `[chisel\|ridge till]` | Parsed as list | Parsed as list |
| Bare pipes | `chisel\|ridge till` | **Single string** | Parsed as list |
| Spaced pipes | `chisel \| ridge till` | **Single string** | Parsed as list |

Without `--list-wrapper none`, `linkml-convert`'s TSV loader (via
`json_flattener`) requires `[square bracket]` wrapping to recognize lists.
Bare pipes are treated as literal text, causing enum validation errors or
silently wrong data.

### What linkml provides now

With linkml PR [#3134](https://github.com/linkml/linkml/pull/3134) (merged
2026-02-27, not yet in a PyPI release), `linkml-convert` supports
`--list-wrapper none` for both loading and dumping bare-pipe TSV:

```bash
# Load bare-pipe TSV → YAML
linkml-convert -s schema.yaml -C MixsCompliantData -S mims_soil_data \
  -f tsv -t yaml --list-wrapper none --no-validate input.tsv

# Dump YAML → bare-pipe TSV
linkml-convert -s schema.yaml -C MixsCompliantData -S mims_soil_data \
  -f yaml -t tsv --list-wrapper none --no-validate input.yaml
```

Loading also requires the empty-cell crash fix from
[linkml#3251](https://github.com/linkml/linkml/pull/3251).

### What linkml does NOT handle

`linkml-convert` expects a **single wrapper style per invocation**. If a TSV
file mixes bracketed and bare-pipe rows (common when data comes from multiple
submitters), `linkml-convert` cannot parse it directly.

That is the gap `normalize_tsv_lists.py` fills — it's a **pre-processing
step** that normalizes all multivalued cells to one style before handing the
file to `linkml-convert`.

**Note:** `linkml-validate` uses a completely separate CSV/TSV loader (raw
`csv.DictReader`, no `json_flattener`) that does not support `--list-wrapper`
at all. TSV validation of multivalued fields is tracked in
[linkml#3147](https://github.com/linkml/linkml/issues/3147).

## Files

| File | Committed? | Description |
|------|-----------|-------------|
| `MimsSoil-messy-lists.tsv` | Yes | 4 rows with 3 different list styles (brackets, bare, spaced) |
| `normalize_tsv_lists.py` | Yes | Schema-aware normalizer: mixed styles → canonical `[pipe\|delimited]` |
| `MimsSoil-normalized-lists.tsv` | Yes (generated, committed for reference) | Output of normalization step |
| `MimsSoil-normalized.yaml` | Yes (generated, committed for reference) | YAML from round-tripping the normalized TSV |
| `MimsSoil-bare-pipes.tsv` | No (generated) | Bare-pipe TSV dumped with `--list-wrapper none` |
| `MimsSoil-bare-pipes-reloaded.yaml` | No (generated) | YAML from loading the bare-pipe TSV back |

## Usage

All targets below are **standalone demos**, not part of `make all` or `make test`.

```bash
# Step 1: Normalize mixed-format TSV → canonical bracketed format
#   Uses SchemaView to identify multivalued slots, only touches those columns.
make normalize-tsv-demo

# Step 2: Round-trip normalized TSV through linkml-convert (bracket format)
#   Proves linkml-convert can parse the normalized output.
make normalize-tsv-roundtrip

# Step 3: Dump YAML → bare-pipe TSV using --list-wrapper none
make src/data/examples/tsv-normalization/MimsSoil-bare-pipes.tsv

# Step 4: Full bare-pipe round-trip (dump + load)
#   Requires linkml with PR #3134 + #3251 (empty-cell fix).
make tsv-bare-pipe-roundtrip
```

### Dependencies

Both `linkml` and `linkml-runtime` must be installed from git (the
`fix-3250-empty-cell-crash` branch or later) until these features ship in a
PyPI release. See `pyproject.toml` for the current pinning. Version skew
between the two packages causes crashes
([linkml#3241](https://github.com/linkml/linkml/issues/3241)).

## What Each Step Demonstrates

1. **Schema awareness matters**: The normalizer uses
   `SchemaView.induced_slot()` to find which columns are multivalued — it
   only touches those columns, respecting class-level `slot_usage` overrides.

2. **Mixed-format files need pre-processing**: `linkml-convert` expects one
   wrapper style per file. The normalizer handles the common case of data
   merged from multiple submitters using different conventions.

3. **`--list-wrapper none` round-trip works**: With the empty-cell crash fix,
   `linkml-convert` dumps and loads bare-pipe format correctly — no brackets
   needed.

4. **Validator gap remains**: `linkml-validate` and `linkml examples` still
   cannot parse multivalued TSV fields
   ([linkml#3147](https://github.com/linkml/linkml/issues/3147)).

## Next Steps

### Boolean slot demo

MIxS has 6 boolean slots (`reassembly_bin`, `x16s_recover`, `smoker`,
`twin_sibling`, `medic_hist_perform`, `hysterectomy`) but **none appear in
any existing example data**. The current demos only exercise list formatting.

linkml PR [#3144](https://github.com/linkml/linkml/pull/3144) adds
`--boolean-truthy`, `--boolean-falsy`, and `--boolean-output` flags to
`linkml-convert`. To demonstrate both features together:

1. Create a **Mimag** or **HumanAssociated** example YAML/TSV that includes
   boolean slots (e.g. `reassembly_bin: yes`, `x16s_recover: no`) alongside
   multivalued list slots
2. Add a Makefile target that round-trips with both `--list-wrapper none` and
   `--boolean-truthy yes,no` — showing lists and booleans handled in one pass
3. Show the before/after: without `--boolean-truthy`, `yes`/`no` stay as
   strings; with it, they coerce to `true`/`false`

This requires either merging #3144 to main or pointing MIxS at a branch that
combines #3251 (empty-cell fix) + #3144 (boolean handling).

### Validator integration

`linkml-validate` uses a separate CSV/TSV code path (raw `csv.DictReader`)
that doesn't support `--list-wrapper` or boolean coercion. Once
[linkml#3147](https://github.com/linkml/linkml/issues/3147) is addressed,
add validation targets that confirm TSV example data passes schema validation.

### Schema-level annotations

Instead of passing `--list-wrapper none` on the CLI every time, MIxS could
add schema-level annotations so the loader/dumper picks up defaults
automatically:

```yaml
annotations:
  list_wrapper: none
  inner_delimiter: "|"
  list_strip_whitespace: true
  boolean_truthy: "yes,on,1"
  boolean_falsy: "no,off,0"
```

This would make `linkml-convert -s mixs.yaml -f tsv -t yaml` do the right
thing without extra flags.

## Related Issues

- [linkml#3134](https://github.com/linkml/linkml/pull/3134) — Configurable list formatting (merged, awaiting PyPI release)
- [linkml#3144](https://github.com/linkml/linkml/pull/3144) — Boolean truthy/falsy handling for CSV/TSV
- [linkml#3251](https://github.com/linkml/linkml/pull/3251) — Empty multivalued cells crash fix
- [linkml#3250](https://github.com/linkml/linkml/issues/3250) — Empty multivalued cells crash with `--list-wrapper none`
- [linkml#3241](https://github.com/linkml/linkml/issues/3241) — Version skew crash between linkml and linkml-runtime
- [linkml#3147](https://github.com/linkml/linkml/issues/3147) — Validator CSV/TSV loader lacks schema-aware parsing
- [linkml#2581](https://github.com/linkml/linkml/issues/2581) — Original feature request for configurable list syntax
- [mixs#1060](https://github.com/GenomicsStandardsConsortium/mixs/issues/1060) — Cardinality and syntax of env triad slots
