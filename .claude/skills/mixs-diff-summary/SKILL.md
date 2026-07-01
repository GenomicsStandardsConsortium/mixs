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
  The two versions and dates are in `comparison_metadata`.
- If the top level has **`added` / `removed` / `renamed`** (and a `comparison`
  block), it came from the one-time v5-to-v6.0.0 diff script. Read `added`,
  `removed`, `renamed`, `deleted`, `definition_changed`, and `rename_candidates`
  directly; the two versions are in `comparison`.

If the diff has a **`rename_candidates`** section (removed names that closely
match an added name but are not in the confirmed rename map), always call it out
in the summary: these are likely missed renames that a maintainer should confirm
and promote into the tool's rename map. Do not silently treat them as removals.

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
2. **Added** named elements, by kind.
3. **Removed** named elements, by kind.
4. **Renamed**, listed old to new.
5. **Possible missed renames**: the `rename_candidates`, if any, with a note that
   a maintainer should confirm and add real ones to the rename map.
6. **Cardinality and range changes**: any `required`, `multivalued`, or `range`
   change. List these individually; they change what data is valid. (The
   v5-to-v6.0.0 diff has no such fields, so omit this section for it.)
7. **Pattern changes**: changes to `pattern` or `structured_pattern`, summarized
   (do not paste every regex).
8. **Cosmetic changes (grouped)**: one line per shared mass-edit, with a count.
9. **Notes**: anything that needed a judgment call.

List added, removed, renamed, cardinality, range, and pattern changes
individually. Group cosmetic text-only changes. Keep the whole summary under one
page. State plainly anything you were unsure how to classify.

Write the result to `agent_summary.md` in the same directory as the input file,
and also print it.

## Worked example

`assets/diff_results/v5_to_v6.0.0/agent_summary.md` is a summary produced by this
skill from the v5-to-v6.0.0 diff. Match that structure so summaries from
different diffs read like siblings.
