# Comparing two versions of the MIxS schema

This document explains how to compare two versions of the MIxS schema and turn
the result into a readable summary.

The tool compares two **LinkML YAML** versions of MIxS. MIxS has been authored
in LinkML since v6.0.0 (2022); earlier Excel, Word, and XSD formulations are not
supported (see [Scope](#scope-and-history) at the end). The release workflow
(`.github/workflows/create-release-pr.yaml`) runs this same tool to attach a diff
to every release pull request.

## From a clean machine to a working diff

Follow these steps even if you already have a MIxS clone somewhere on disk.

> **Use a fresh clone, not an old one.** MIxS computes its version from git tags
> (`poetry-dynamic-versioning`), so a clone that is missing tags, or an old fork,
> will fail to build or report the wrong version. A stale checkout can also have a
> `main` that is months behind. Start clean in a known location.

### 1. Clone the canonical repository

```bash
mkdir -p ~/gitrepos && cd ~/gitrepos
git clone https://github.com/GenomicsStandardsConsortium/mixs.git
cd mixs
```

Confirm you got the tags (dynamic versioning needs them):

```bash
git tag | grep -E '^v6' | head     # should list v6.x tags, e.g. v6.2.0
```

If no tags appear, fetch them: `git fetch --tags`.

### 2. Use a supported Python

The project supports Python 3.10 through 3.13. Use **3.13**; some dependencies do
not yet resolve on 3.14. Point Poetry at the right interpreter before installing:

```bash
poetry env use python3.13     # or the full path to a 3.13 interpreter
```

### 3. Install the project

This installs MIxS and registers the `diff-releases` command:

```bash
poetry install --all-extras   # the Makefile target `make install` does the same
```

Installing is required. Without it, `poetry run diff-releases` reports
`No module named 'scripts'`.

### 4. Provide a GitHub token (recommended)

The tool fetches schema files through the GitHub API. Without a token you share
the anonymous limit of 60 requests per hour, which a multi-version diff can
exhaust. With a token the limit is 5000 per hour. The tool reads `GITHUB_TOKEN`
from the environment first, then from a `.env` file in the repo root.

```bash
export GITHUB_TOKEN=$(gh auth token)     # if you use the GitHub CLI
# or add a line GITHUB_TOKEN=ghp_... to a .env file (never commit it)
```

### 5. Verify

```bash
poetry run diff-releases --help
poetry run diff-releases --list-releases   # lists taggable versions it can fetch
```

## End to end: regenerate the v5 to v6.0.0 diff

To go from nothing to a fresh clone, a built environment, cleared old outputs, the
one-time v5 to v6.0.0 diff, and a readable summary, run these in order:

```bash
# 1. Clone and enter the repository
mkdir -p ~/gitrepos && cd ~/gitrepos
git clone https://github.com/GenomicsStandardsConsortium/mixs.git
cd mixs

# 2. Build the environment (Python 3.13; installs openpyxl and the rest)
poetry env use python3.13
poetry install

# 3. Clear previously generated diff outputs.
#    DANGER: these files are committed. If you clear them and then commit and
#    push, you remove them from the repository. Do not run this if you intend to
#    push your current work. See the Makefile comment on this target.
make clean-diff-results

# 4. Run the one-time v5 to v6.0.0 diff (no arguments; the inputs are fixed).
poetry run python src/scripts/v5_to_v6_onetime_diff.py
```

Step 4 writes `assets/diff_results/v5_to_v6.0.0/schema_comparison_results.yaml`
(the structured diff) and `tool_summary.md` (a short summary). Then, in Claude
Code, write the readable summary with the skill:

```
/mixs-diff-summary assets/diff_results/v5_to_v6.0.0/schema_comparison_results.yaml
```

That writes `assets/diff_results/v5_to_v6.0.0/agent_summary.md`.

The rest of this document describes the reusable, forward-looking tool for
comparing any two LinkML versions of MIxS.

## Running a diff

Each side is given as `owner/repo@ref:path`, where `ref` is a tag, branch, or
commit, and `path` is the schema file at that ref. Always pass `--mappings-dir`
so renamed elements are recognized as renames rather than as one deletion plus
one addition (see [Maintaining the mappings](#maintaining-the-rename-mapping-files)).

**A tagged release against current main:**

```bash
poetry run diff-releases \
  --old "GenomicsStandardsConsortium/mixs@v6.2.0:src/mixs/schema/mixs.yaml" \
  --new "GenomicsStandardsConsortium/mixs@main:src/mixs/schema/mixs.yaml" \
  --mappings-dir assets/between_diff_mappings/6_to_pre_7 \
  --output-dir /tmp/mixs_diff
```

**Two tagged releases:**

```bash
poetry run diff-releases \
  --old "GenomicsStandardsConsortium/mixs@v6.1.0:src/mixs/schema/mixs.yaml" \
  --new "GenomicsStandardsConsortium/mixs@v6.2.0:src/mixs/schema/mixs.yaml" \
  --mappings-dir assets/between_diff_mappings/6_to_pre_7
```

**Your fork against upstream** (review a branch before opening a PR):

```bash
poetry run diff-releases \
  --old "GenomicsStandardsConsortium/mixs@main:src/mixs/schema/mixs.yaml" \
  --new "your-handle/mixs@your-branch:src/mixs/schema/mixs.yaml" \
  --mappings-dir assets/between_diff_mappings/6_to_pre_7
```

### What it writes

Into the output directory (default `assets/diff_results/`):

- `releases.yaml`: which two versions were compared, with commit and date.
- `schema_comparison_results.yaml`: the structured diff. Each collection (slots,
  classes, enums, prefixes, settings) splits into `key_comparison` (added or
  removed names) and `definition_changes` (same name, changed body, field by
  field).

The structured output reports every change equally, including cosmetic ones. For
example, a one-line edit to a templated description can show as a change on every
combination class at once. The summary step below is where that gets explained.

## Turning the YAML diff into a readable summary

`schema_comparison_results.yaml` is thorough but large. To produce a short,
human-readable Markdown summary from it, use the `mixs-diff-summary` skill
(`/mixs-diff-summary <path-to-schema_comparison_results.yaml>`), defined in
`.claude/skills/mixs-diff-summary/`. It reads the structured YAML and writes a
summary that groups cosmetic mass-edits, highlights structural changes, and calls
out cardinality and range changes. A worked example is
`assets/diff_results/v5_to_v6.0.0/agent_summary.md`.

At release time, the release workflow generates the structured diff on the
release branch, and a maintainer runs this skill on that branch to add the
summary before review. See `src/docs/edit_workflow.md`, section "Releases". The
summary step is deliberately not run in CI, so it needs no API keys.

## Maintaining the rename-mapping files

The mapping files live in `assets/between_diff_mappings/<from>_to_<to>/`. They
let the tool recognize that, for example, `texture` became `soil_texture` rather
than reporting one slot removed and a different one added. Today the LinkML-era
mappings are in `6_to_pre_7/`, split by element kind:

- `slot_name_mappings.tsv`, `class_name_mappings.tsv`, `enum_name_mappings.tsv`,
  `subset_name_mappings.tsv`: two columns, `old_name` then `new_name`.
- `inter_type_refactoring.tsv`: for elements that changed kind, for example a
  slot that became a subset.

**When you need a new mapping file.** Create a new `<from>_to_<to>/` directory
whenever a release renames, splits, merges, changes the kind of, or removes
named elements (slots, classes, enums, subsets). A release that only edits
descriptions, examples, or patterns needs no new mappings.

**How likely is that.** Fairly likely at each significant release. The move
toward v7 renamed many elements to CamelCase, so `6_to_pre_7/` is large. Most
minor releases need a handful of entries or none. The effort is small: add the
old and new names to the matching TSV.

## Scope and history

This tool compares LinkML versions only. The general multi-format diff machinery
(v4 Excel, Word, XSD) has been retired. The one transition worth recording, v5
(2018 Excel) to v6.0.0 (2022 LinkML), is kept as a separate, clearly labeled
one-time diff: the code is the single file `src/scripts/v5_to_v6_onetime_diff.py`
and its finished output is in `assets/diff_results/v5_to_v6.0.0/`. It is kept apart from this
reusable tool: the two versions are set in the script, and it is not part of the
release workflow.
