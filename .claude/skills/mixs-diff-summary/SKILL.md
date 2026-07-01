---
name: mixs-diff-summary
description: Turn a MIxS schema-diff YAML into a short, readable Markdown summary. Use when reviewing a release diff, or when asked to summarize how the MIxS schema changed between two versions. Reads the output of both the reusable diff-releases tool and the one-time v5-to-v6.0.0 diff script.
argument-hint: [path to schema_comparison_results.yaml]
allowed-tools: Read, Write, Bash
---

# Summarize a MIxS schema diff

Produce a short, readable Markdown summary of a MIxS schema-diff YAML.

The input file is `$ARGUMENTS`. If that is empty, ask which diff file to
summarize, or default to `assets/diff_results/schema_comparison_results.yaml` if
it exists.

## Step 1: read the diff and detect which tool produced it

Read the YAML. Two shapes are possible; handle both and read them the same way:

- If the top level has **`collection_differences`**, it came from the reusable
  `diff-releases` tool. Each kind (slots, classes, enums, prefixes, settings) has
  `key_comparison.{only_in_new, only_in_old, shared}` and `definition_changes`.
- If the top level has **`term_differences`**, it came from the one-time
  v5-to-v6.0.0 diff script. Use `term_differences` as the "slots" group. Renames
  are listed explicitly in `key_comparison.expected_mappings`, and structural
  deletions in `key_comparison.expected_deletions`. Its
  `package_differences`/`checklist_differences` sections may be summarized in one
  line each if present.

Use `comparison_metadata` for the two versions and dates.

## Step 2: separate real change from cosmetic mass-edits

For each entry in a collection's `definition_changes`, compare the old and new
definition field by field. If the only differing fields are text fields
(`description`, `title`) and they are equal after lowercasing and collapsing
whitespace, treat the change as cosmetic. When many entries in one collection
share the same cosmetic change, report them as a single grouped line with a count
and one example, never one line per entry.

## Step 3: write the summary

Emit these sections, in order, omitting any that are empty:

1. A one-line header naming both versions and their dates.
2. **Added** named elements (`only_in_new`), by kind.
3. **Removed** named elements (`only_in_old`), by kind.
4. **Renamed** (from `expected_mappings` when present).
5. **Cardinality and range changes**: any `required`, `multivalued`, or `range`
   change in `definition_changes`. List these individually; they change what data
   is valid.
6. **Pattern changes**: changes to `pattern` or `structured_pattern`, summarized
   (do not paste every regex).
7. **Cosmetic changes (grouped)**: one line per shared mass-edit, with a count.
8. **Notes**: anything that needed a judgment call.

List added, removed, renamed, cardinality, range, and pattern changes
individually. Group cosmetic text-only changes. Keep the whole summary under one
page. State plainly anything you were unsure how to classify.

Write the result to `agent_summary.md` in the same directory as the input file,
and also print it.

## Worked example

`assets/diff_results/v5_to_v6.0.0/agent_summary.md` is a summary produced by this
skill from the v5-to-v6.0.0 diff. Match that structure so summaries from
different diffs read like siblings.
