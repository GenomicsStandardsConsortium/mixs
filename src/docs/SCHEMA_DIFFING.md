# Comparing two versions of the MIxS schema

This document explains how to compare two versions of the MIxS schema and turn
the result into a readable summary.

The tool compares two **LinkML YAML** versions of MIxS. MIxS has been authored
in LinkML since v6.0.0 (2022); earlier Excel, Word, and XSD formulations are not
supported (see [Scope](#scope-and-history) at the end). The release workflow
(`.github/workflows/create-release-pr.yaml`) runs this same tool to attach a diff
to every release pull request.

## Setup

First set up the MIxS environment as described in the repository README's "Local
setup" section (clone the repo, use Python 3.10 through 3.13, run `poetry
install`). That installs the dependencies and registers the `diff-releases`
command. If `poetry run diff-releases` reports `No module named 'scripts'`, the
project was not installed; run `poetry install` first.

Three things are specific to diffing:

**Use a fresh clone with its tags.** MIxS computes its version from git tags
(`poetry-dynamic-versioning`), so a clone that is missing tags, or an old fork,
can build wrong or report the wrong version. After cloning, confirm the tags
arrived; if none appear, run `git fetch --tags`:

```bash
git tag | grep -E '^v6' | head     # should list v6.x tags, e.g. v6.2.0
```

**Provide a GitHub token (recommended).** The tool fetches schema files through
the GitHub API. Without a token you share the anonymous limit of 60 requests per
hour, which a multi-version diff can exhaust; with a token it is 5000 per hour.
The tool reads `GITHUB_TOKEN` from the environment first, then from a `.env` file
in the repo root:

```bash
export GITHUB_TOKEN=$(gh auth token)     # if you use the GitHub CLI
# or add a line GITHUB_TOKEN=ghp_... to a .env file (never commit it)
```

**Verify:**

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

# 2. Build the environment. Requires a Python 3.10-3.13 interpreter already
#    installed and on PATH (3.13 recommended, not 3.14); install one first if you
#    have none. This installs openpyxl and the rest.
poetry env use python3.13
poetry install

# 3. Purge this diff's previously generated outputs so you regenerate them fresh.
#    You name the diff, so nothing else is touched. The files are committed, so
#    steps 4 and 5 write them back (or recover with git restore).
make purge-diff DIFF=v5_to_v6.0.0

# 4. Run the one-time v5 to v6.0.0 diff (no arguments; the inputs are fixed).
poetry run python src/scripts/v5_to_v6_onetime_diff.py
```

Step 4 writes `assets/diff_results/v5_to_v6.0.0/schema_comparison_results.yaml`
(the structured diff) and `tool_summary.md` (a short summary). Then, in Claude
Code, write the readable summary with the skill:

```
/mixs-diff-summary assets/diff_results/v5_to_v6.0.0/schema_comparison_results.yaml
```

That writes `assets/diff_results/v5_to_v6.0.0/agent_summary.md`, which completes
the three files in that directory.

To purge a diff you no longer want, run `make purge-diff DIFF=<name>` (with no
name it lists the diffs you can purge). It removes only the folder you name, and
because the outputs are committed you can undo it with
`git restore assets/diff_results/<name>`.

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

Into the output directory (default `assets/diff_results/<old_ref>_to_<new_ref>/`, a
per-release folder; pass `--output-dir` to override):

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
summary that groups repetitive edits, highlights the changes that affect data,
and surfaces patterns spread across the file (naming conventions behind renames,
themes among additions, a common driver behind definition changes). Running it on
the v5-to-v6.0.0 diff writes `assets/diff_results/v5_to_v6.0.0/agent_summary.md`.
The summary is only produced by invoking the skill, not by editing that file by
hand.

At release time, the release workflow generates the structured diff on the
release branch, and a maintainer runs this skill on that branch to add the
summary before review. See [edit_workflow.md](edit_workflow.md), section
"Releases". The summary step is deliberately not run in CI, so it needs no API keys.

### Cost, model, and portability

The summary is one small model call: it reads the structured diff (tens of
thousands of input tokens, most of them cacheable) and writes about a page (a few
hundred to a couple of thousand output tokens). Any current Claude model can do
it; the task is not demanding, so a mid-tier model such as Sonnet is enough. A
larger model such as Opus also works but is slower and costs more for no real gain
on a diff this size.

To see what a run actually used, run Claude Code's `/usage` command, which breaks
token use down by skill. On a Claude Max or Pro subscription the dollar figure it
shows is a local estimate, not a bill. `npx ccusage@latest` gives per-session
totals from the local logs.

A single run is roughly 10,000 input tokens and 3,000 output tokens (the
structured diff in, the one-page summary out), costing on the order of a few cents
on Opus and less on a mid-tier model.

There is no shared or central billing for this. The MIxS repository does not
provide an account that runs the skill on anyone's behalf. Whoever runs it must
install their own coding-assistant tool (such as Claude Code) on their own
computer, sign in with their own credentials, and pay for their own usage; a run
draws on that person's own subscription or API billing.

The skill's `SKILL.md` format and the `/mixs-diff-summary` invocation are specific
to Claude Code, so other agent command-line tools will not discover or run it
automatically. The instructions themselves are plain, model-agnostic Markdown, so
a user of another tool could point that tool at `SKILL.md` and the diff file and
get the same kind of summary.

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
