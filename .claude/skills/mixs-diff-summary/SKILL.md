---
name: mixs-diff-summary
description: Turn a MIxS schema-diff YAML into a short, readable Markdown summary. Use when reviewing a release diff, or when asked to summarize how the MIxS schema changed between two versions. Reads the output of both the reusable diff-releases tool and the one-time v5-to-v6.0.0 diff script.
argument-hint: [path to schema_comparison_results.yaml]
allowed-tools: Read, Write, Bash
---

# Summarize a MIxS schema diff

## Why a change was made, not just what changed

The structured diff describes the schema and nothing else, so on its own it can
say that 409 slots were added but never that 44 of them are the MInAS ancient DNA
extension. The release history says that, and you can read it.

Use it to attribute changes and to explain removals, and cite rather than assert.
A pull request title is written by whoever opened it and is sometimes wrong or
vague, so link the pull request and let a reader judge. Where a title does not
support a claim, leave the claim out rather than inferring intent.

The pull requests merged between the two refs being compared:

```bash
gh pr list --state merged --search "merged:<old date>..<new date>" \
   --limit 200 --json number,title,author,labels,url
```

That is 50 for v6.3.1 to v7.0.0 and around 200 for a comparison reaching back to
MIxS 6.0.0, whose tag is `mixs6.0.0` rather than `v6.0.0`. Either is small enough
to read.

Two other sources already at hand:

- **`deprecated:` strings in the schema itself**, which carry the reason a term
  was retired and often an issue link. They explain a removal better than a diff
  can infer, and they are in the file you are already reading.
- **Labels on the pull requests**, such as `2-NewTerm` and `3-CIG`, which show
  whether a change went through term review.

Attribution will sometimes be wrong. Prefer "added by" with a link over "in order
to", and do not describe motivation the history does not state.

## Working in this repository

Run Python with `poetry run python`. This is a poetry project, and `uv run`
creates a `.venv` and a `uv.lock` inside it that then have to be cleaned up.

The two schemas being compared are cached under `assets/releases_for_diffing/`,
one directory per ref, if you need to check something the diff does not record.

Read the diff once into a script rather than shelling out repeatedly; it is
around a megabyte of YAML and reparsing it per question is slow.


Produce a short, readable Markdown summary of a MIxS schema-diff YAML.

The input file is `$ARGUMENTS`. If that is empty, ask which diff file to
summarize. Diffs live in per-release folders, so the file is usually
`assets/diff_results/<old>_to_<new>/schema_comparison_results.yaml`; if there is
exactly one such folder, you may use its `schema_comparison_results.yaml`.

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
definition field by field. If the only differing field is `description` and the
two are equal after lowercasing and collapsing whitespace, treat the change as
cosmetic. When many entries in one collection share the same cosmetic change,
report them as a single grouped line with a count and one example, never one line
per entry.

`title` is not cosmetic, even when the only difference is case or whitespace.
Downstream archives key on it: ENA uses the MIxS title as its controlled
nomenclature, so a change there is a change to an identifier its users see.
Report `title` changes individually under their own section.

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
8. **Title changes**: listed individually, old to new. ENA treats the title as
   controlled nomenclature, so these matter to consumers even when the edit looks
   like tidying.
9. **Cosmetic changes (grouped)**: one line per shared mass-edit, with a count.
   `description` only.
10. **Notes**: anything that needed a judgment call.

## What makes a good summary

The structured YAML and the tool's own `tool_summary.md` already carry the raw
counts and the full lists. Do not just restate them. The value of this summary is
to help a reader understand **patterns whose evidence is spread across the large
diff file** and would take a long time to see by hand. It is fine for the summary
to run longer than the tool summary if the extra length adds understanding; avoid
repeating the same item in several sections.

Look for cross-cutting patterns such as:

- **Systematic naming conventions** behind the renames (for example, consistent
  abbreviations like `content` to `cont`, or dropped prefixes), rather than
  listing every rename.
- **Thematic clusters** among the added elements (for example, a whole new
  package or domain arriving at once), by grouping shared name stems.
- **A common driver** behind the definition changes (for example, many
  definitions gaining an ontology reference they lacked before, or shifting from
  describing a concept to naming a tool), rather than one line per changed
  definition.
- **What the numbers overstate or understate** once you account for those
  patterns (for example, renames that would otherwise read as removals).

Group individual items under the pattern that explains them. Keep the concrete
lists for the things that genuinely need to be seen one by one (structural
removals, cardinality and range changes, rename candidates). State plainly
anything you were unsure how to classify.

Write the result to `agent_summary.md` in the same directory as the input file,
and also print it.
