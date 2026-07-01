# One-time, hardcoded MIxS v5 to v6.0.0 diff

> **This is not the reusable diff tool.** It is a single-purpose, hardcoded
> reproducer for one historical comparison: MIxS v5 (2018, Excel) to MIxS v6.0.0
> (2022, the first LinkML release). Both inputs are frozen releases, so the script
> takes no arguments and the result never changes.
>
> To compare any two **LinkML** versions of MIxS (v6 onward), use the reusable,
> forward-compatible tool instead: `diff-releases`
> (`src/scripts/diff_two_linkml_mixs_releases.py`), documented in
> [`../docs/SCHEMA_DIFFING.md`](../docs/SCHEMA_DIFFING.md).

## Why this exists separately

MIxS switched authoring format at v6.0.0 (Excel to LinkML). That one transition
is worth recording, but it needs an Excel reader, which the reusable LinkML tool
deliberately does not carry. Rather than keep general multi-format diff machinery
alive, this directory quarantines everything needed for the single v5-to-v6.0.0
comparison: a trimmed engine, the validated mapping, the parse profile, the
hardcoded runner, and the frozen output.

## Contents

- `diff_v5_to_v6.py`: the hardcoded, zero-argument runner. Fetches the pinned v5
  Excel file and the v6.0.0 tag, applies the validated mapping, writes `output/`.
- `engine/`: a trimmed copy of the diff engine from the closed PR #1115 (v5 Excel
  reader, LinkML reader, comparison, output). Not a maintained package.
- `mapping_config.yaml`: the validated rename and deletion mapping (see below).
- `profiles/`: the Excel parse profiles the v5 reader needs.
- `output/`: the frozen result: `schema_comparison_results.yaml` (structured),
  `comparison_summary.txt` (plain text), and `summary.md` (the readable summary
  produced by the [diff-summary skill](../diff-summary-skill/README.md)).

## Inputs (frozen and pinned)

- **Old:** `GenomicsStandardsConsortium/mixs-legacy@9628b5e5aa89:mixs5/mixs_v5.xlsx`
  (MIxS v5, 600 terms; public repo, pinned commit).
- **New:** `GenomicsStandardsConsortium/mixs@mixs6.0.0:model/schema/mixs.yaml`
  (MIxS v6.0.0, 804 terms with imports resolved).

## How to run

```bash
poetry install --with legacy-v5-diff   # adds openpyxl for reading the .xlsx
python contrib/v5_to_v6_onetime_diff/diff_v5_to_v6.py
```

The runner pins `PYTHONHASHSEED=0`, so re-runs reproduce the committed output
byte-for-byte (apart from the timestamp).

## The mapping was validated, not inherited

An earlier version of this diff (in the closed PR #1115) was wrong twice: it
compared v5 against `main` (about four years past v6.0.0) while labeling the
result "v6.0.0", and its rename targets were main-era names. Both errors inflated
the counts and turned later renames into false removals.

This version was rebuilt against the real `mixs6.0.0` tag, and every mapping entry
was checked against that tag:

- Each of the 6 rename targets is confirmed present in v6.0.0.
- Renames whose old name still exists in v6.0.0 were dropped (those terms are
  shared, not renamed). `soil_horizon`, `soil_texture`, and `soil_texture_meth`
  were removed from the mapping for this reason; they are post-v6.0.0 renames.
- Each of the 18 removed terms is confirmed absent from v6.0.0.
- The 3 structural deletions are confirmed absent from v6.0.0.

## Scope notes (what is and is not compared)

- **Patterns are not compared, and nothing is materialized.** The v5 Excel model
  asserts no regex patterns; it has a free-text `Value syntax` column, which maps
  to the `value_syntax` field. MIxS v6.0.0 has zero `structured_pattern`s (those
  were added after v6.0.0). So there is nothing to materialize on either side.
  (The reusable `diff-releases` tool does call `materialize_patterns()`, which is
  correct for modern MIxS where 298 slots use structured patterns.)
- **The comparison is a flat term list.** LinkML slot attributes are read with
  induction on (`induced_slot`), so slot-level `is_a`/mixin resolution is
  respected. Per-class `slot_usage` variation is not flattened into the term
  attributes; it is captured only as checklist/package membership requiredness.
- **Most "changes" are the format migration.** Almost every shared term shows a
  change in `value_syntax`, `occurrence`, and `expected_value`, because those v5
  Excel columns map onto different LinkML representations. See `output/summary.md`
  for how the substantive signal is separated from the migration noise.

## Result

573 shared, 226 added, 18 removed, 6 renames, 3 structural deletions. Most of the
raw "changed term" count is the Excel-to-LinkML format migration rather than
semantic change; see `output/summary.md`.
