# Diff summary skill

A repeatable way to turn the structured output of `diff-releases` into a short,
human-readable Markdown summary.

The diff tool writes `schema_comparison_results.yaml`, which is complete but
large and reports every change with equal weight. A reader who sees "279 classes
changed" cannot tell a sweeping structural change from a one-line wording fix
applied to many classes at once. This skill produces a summary that makes that
distinction.

## Input

- `schema_comparison_results.yaml` (required): the structured diff.
- `releases.yaml` (optional): the two versions compared, for the header.

The skill accepts the output of **either** MIxS diff tool and produces the same
kind of summary from both:

1. the reusable LinkML tool `diff-releases`
   (see [`../docs/SCHEMA_DIFFING.md`](../docs/SCHEMA_DIFFING.md)), and
2. the one-time v5-to-v6.0.0 reproducer
   (see [`../v5_to_v6_onetime_diff/README.md`](../v5_to_v6_onetime_diff/README.md)).

## Two input shapes, one summary

The two tools write slightly different YAML. Detect which you have and read it
the same way, so the summaries come out consistent:

| what you need | reusable `diff-releases` | one-time v5-to-v6 engine |
|---|---|---|
| versions and dates | `comparison_metadata` | `comparison_metadata` |
| added / removed / shared | `collection_differences.<kind>.key_comparison.{only_in_new, only_in_old, shared}` for each kind (slots, classes, enums, ...) | `term_differences.key_comparison.{only_in_new, only_in_old, shared}` |
| field-level changes | `collection_differences.<kind>.definition_changes` | `term_differences.definition_changes` |
| renames | already folded in (mapped names appear as shared) | listed explicitly in `key_comparison.expected_mappings` |
| deletions called out | not marked | `key_comparison.expected_deletions` |

Detection: if the top level has `collection_differences`, it is the reusable
tool; if it has `term_differences`, it is the one-time engine. Treat the reusable
tool's per-kind collections as separate groups; treat the one-time engine's
`term_differences` as the "slots" group (its extra `package_differences` and
`checklist_differences` sections can be summarized in one line each if present).

Whichever shape you read, emit the **same sections** described below. That is what
keeps a v5-to-v6 summary and a v6.2.0-to-main summary looking like siblings.

## What the summary should contain

1. A header naming the two versions, their commits, and their dates.
2. **Added and removed** named elements (slots, classes, enums), from
   `key_comparison.only_in_new` and `only_in_old`. These are the changes most
   likely to break downstream use.
3. **Cardinality and range changes** on slots: any change to `required`,
   `multivalued`, or `range` in `definition_changes`. List these individually;
   they change what data validates.
4. **Pattern changes**: changes to `pattern` or `structured_pattern`. Summarize
   the kind of change (for example, a CURIE syntax loosened) rather than pasting
   every regex.
5. **Cosmetic mass-edits, grouped not listed.** When many elements change only a
   text field (`description`, `title`) and the changes share a pattern, report
   them as one line, for example: "279 combination-class descriptions: wording
   fix (`data that complies` to `Data that comply`)." Do not emit one row per
   element.
6. A short closing note on anything that needed a judgment call.

## How to detect a cosmetic mass-edit

For each entry in a collection's `definition_changes`, compare the old and new
definition field by field. If the only differing fields are text fields and the
differences are equal after lowercasing and collapsing whitespace, treat the
change as cosmetic. If many entries in the same collection share the same
cosmetic change, group them into one line.

## Prompt

> You are summarizing a MIxS schema diff for readers who work with biological
> metadata standards but have not read the raw diff. You are given
> `schema_comparison_results.yaml` and `releases.yaml`.
>
> Write a Markdown summary with these sections, in order: a one-line header with
> both versions and dates; Added elements; Removed elements; Cardinality and
> range changes; Pattern changes; Cosmetic changes (grouped); Notes. Omit any
> section that has no content.
>
> List added, removed, cardinality, range, and pattern changes individually,
> because they affect what data is valid. Group cosmetic text-only changes that
> share a pattern into a single line with a count and an example, never one line
> per element. Quote at most one short example regex; describe the rest. Keep the
> whole summary under one page. State plainly anything you were unsure how to
> classify.

## Worked example

Running `diff-releases` for v6.2.0 to main (computed 2026-06-30) produced a diff
whose faithful summary is:

> ### MIxS schema: v6.2.0 (2023-10-18) to main (2026-06-17)
>
> **Added:** 67 slots, 48 classes. **Removed:** 1 slot.
>
> **Cardinality and range changes:** 187 slots changed `range`. No `required` or
> `multivalued` changes.
>
> **Pattern changes:** 266 slots. The CURIE pattern was loosened (prefix
> `[a-zA-Z]{2,}` to `[a-zA-Z][a-zA-Z0-9._]*`); `env_local_scale` gained a pattern
> it previously lacked.
>
> **Cosmetic changes (grouped):** 279 combination-class descriptions changed only
> in wording (`data that complies` to `Data that comply`); this is one templated
> edit, not 279 separate decisions.
>
> **Notes:** the three environmental-context slots (`env_broad_scale`,
> `env_local_scale`, `env_medium`) changed only their pattern; their meaning and
> cardinality are unchanged.

Without grouping, the same diff reads as "751 slots and 279 classes changed,"
which hides that most of the class changes are a single wording fix.
