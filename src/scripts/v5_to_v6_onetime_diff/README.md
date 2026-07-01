# One-time MIxS v5 to v6.0.0 diff

> **This is not the reusable diff tool.** It is a single-purpose script for one
> historical comparison: MIxS v5 (2018, Excel) to MIxS v6.0.0 (2022, the first
> LinkML release). Both versions are finished releases that will not change, so
> the script takes no arguments (the two versions are set in the script) and the
> result is always the same.
>
> To compare any two **LinkML** versions of MIxS (v6 onward), use the reusable
> tool instead: `diff-releases` (`src/scripts/diff_two_linkml_mixs_releases.py`),
> documented in `contrib/docs/SCHEMA_DIFFING.md`.

## Why this is separate

MIxS changed authoring format at v6.0.0 (from Excel to LinkML). That one change is
worth recording, but reading it needs an Excel reader, which the reusable LinkML
tool does not carry. Rather than keep general Excel/Word/XSD diff code alive, this
directory holds only the code for the single v5-to-v6.0.0 comparison: a trimmed
engine, the checked mapping, and the Excel parse profiles. The finished result
lives with the other diff outputs, in `assets/diff_results/v5_to_v6.0.0/`.

## Contents (the code)

- `diff_v5_to_v6.py`: the script. It takes no arguments. It fetches the pinned v5
  Excel file and the v6.0.0 tag, applies the checked mapping, and writes the
  structured diff and a tool summary to `assets/diff_results/v5_to_v6.0.0/`.
- `engine/`: a trimmed copy of the diff engine from the closed PR #1115 (v5 Excel
  reader, LinkML reader, comparison, output). Not a maintained package.
- `mapping_config.yaml`: the checked rename and deletion mapping (see below).
- `profiles/`: the Excel parse profiles the v5 reader needs.

## Output (in `assets/diff_results/v5_to_v6.0.0/`)

Three files, with distinct names so their sources are clear:

- `schema_comparison_results.yaml`: the structured, machine-readable diff.
- `tool_summary.md`: a Markdown summary written by this script (counts and lists).
  The script produces the same file each time it runs.
- `agent_summary.md`: a readable Markdown summary written by the `mixs-diff-summary`
  skill (`/mixs-diff-summary`). It groups the change-of-format noise and points
  out the meaningful changes. It reads from the same structured diff, but because
  it is written by an agent it is not identical on every run.

## Inputs (pinned)

- **Old:** `GenomicsStandardsConsortium/mixs-legacy@9628b5e5aa89:mixs5/mixs_v5.xlsx`
  (MIxS v5, 600 terms; public repository, pinned commit).
- **New:** `GenomicsStandardsConsortium/mixs@mixs6.0.0:model/schema/mixs.yaml`
  (MIxS v6.0.0, 804 terms with imports resolved).

## How to run

```bash
poetry install --with legacy-v5-diff   # adds openpyxl for reading the .xlsx
python src/scripts/v5_to_v6_onetime_diff/diff_v5_to_v6.py
```

The script sets `PYTHONHASHSEED=0`, so re-running writes the same
`schema_comparison_results.yaml` and `tool_summary.md` each time (apart from the
timestamp). To remove the regeneratable outputs, use `make clean-diff-results`.

## The mapping was checked, not inherited

An earlier version of this diff (in the closed PR #1115) was wrong twice: it
compared v5 against `main` (about four years past v6.0.0) while labeling the
result "v6.0.0", and its rename targets were the names used on `main`. Both
mistakes inflated the counts and turned later renames into false removals.

This version was rebuilt against the real `mixs6.0.0` tag, and every mapping entry
was checked against that tag:

- Each of the 6 rename targets is present in v6.0.0.
- Renames whose old name still exists in v6.0.0 were dropped (those terms are
  shared, not renamed). `soil_horizon`, `soil_texture`, and `soil_texture_meth`
  were removed from the mapping for this reason; those renames happened after
  v6.0.0.
- Each of the 18 removed terms is absent from v6.0.0.
- The 3 structural deletions are absent from v6.0.0.

## What is and is not compared

- **Patterns are not compared, and nothing is materialized.** The v5 Excel model
  has no regex patterns; it has a free-text `Value syntax` column, which maps to
  the `value_syntax` field. MIxS v6.0.0 has no `structured_pattern`s (those were
  added after v6.0.0). So there is nothing to materialize on either side. (The
  reusable `diff-releases` tool does call `materialize_patterns()`, which is
  correct for current MIxS, where 298 slots use structured patterns.)
- **The comparison is a flat term list.** LinkML slot attributes are read with
  induction on (`induced_slot`), so slot-level `is_a` and mixin resolution is
  included. Per-class `slot_usage` differences are not folded into the term
  attributes; they are captured only as checklist and package membership.
- **Most "changes" are the change of format.** Almost every shared term shows a
  change in `value_syntax`, `occurrence`, and `expected_value`, because those v5
  Excel columns map onto different LinkML fields. See
  `assets/diff_results/v5_to_v6.0.0/agent_summary.md` for how the meaningful
  changes are separated from that noise.

## Result

573 shared, 226 added, 18 removed, 6 renames, 3 structural deletions. Most of the
raw "changed term" count is the change from Excel to LinkML rather than a change
in meaning; see `assets/diff_results/v5_to_v6.0.0/agent_summary.md`.
