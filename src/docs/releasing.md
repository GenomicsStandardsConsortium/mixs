# Releasing MIxS

This covers what happens in this repository: the version numbers, the release
action, the schema comparisons and publishing the release. The steps that
happen outside it, such as notifying the board, the CIG mailing list and the
repositories that implement MIxS, are not described here.

For requesting and editing terms, checklists and extensions, see
[the editing workflows](edit_workflow.md). For the policies these steps enact,
see [the policies](policy.md).

The GSC creates releases using semantic versioning (major.minor.patch).

## Version strings

MIxS carries two version numbers, and they are set in different ways.

A **git tag** marks one commit as a named point in the history. MIxS tags carry
a `v` prefix, as in `v7.0.0`. The prefix belongs to the tag only, never to a
version written inside a file. Publishing a GitHub Release is what creates the
tag, so there is no separate tagging step.

- **Python package version** (`pyproject.toml`): never edited by hand.
  `poetry-dynamic-versioning` reads the git tag and stamps the version at build
  time, so `pyproject.toml` holds a `0.0.0` placeholder on `main`.
- **Schema version** (`version:` in `src/mixs/schema/mixs.yaml`): edited by hand
  as part of a release. It is part of the schema itself, not build metadata, so
  it travels into everything generated from the schema, including the OWL that
  EBI OLS loads and the JSON Schema that validators use. Whatever you type here
  is what downstream consumers will report as their MIxS version.

## Cutting a release

1. Bump the schema version. Edit `version:` near the top of
   `src/mixs/schema/mixs.yaml` to the new number, bare `X.Y.Z` with no `v`, and
   merge it to `main` through a pull request like any other change (see
   [CONTRIBUTING.md](https://github.com/GenomicsStandardsConsortium/mixs/blob/main/CONTRIBUTING.md)).
2. Run the "Create Release PR" action from the
   [Actions tab](https://github.com/GenomicsStandardsConsortium/mixs/actions/workflows/create-release-pr.yaml),
   using "Run workflow", with the same version. It bumps `CITATION.cff`,
   `.zenodo.json` and `release/README.md`, generates the schema diff, and opens
   a `release/vX.Y.Z` pull request. It does not touch `pyproject.toml`, which is
   dynamic, or `mixs.yaml`, which you bumped in step 1.
3. Add the schema-diff summaries to the release branch, as described in the next
   section.
4. Approve the workflows on the release pull request. The pull request was
   opened by a workflow, so GitHub runs no checks on it until a maintainer
   clicks "Approve and run workflows". Until someone does, the pull request
   shows no checks at all rather than failing ones, which is easy to read as
   passing.
5. Review and merge the release pull request. A TWG member other than its
   author reviews the version bumps and the schema-diff summary; the pre-merge
   checklist is in the pull request body.
6. Publish the release from the
   [new release page](https://github.com/GenomicsStandardsConsortium/mixs/releases/new).
   Create the tag `vX.Y.Z` there, set the target to `main` so the tag lands on
   the merge commit rather than the release branch, and use "Generate release
   notes" with the previous release as the "Previous tag". For a release
   candidate see [Publishing a release candidate](#publishing-a-release-candidate).

The structured diff in step 2 is produced by the reusable `diff-releases` tool;
see [SCHEMA_DIFFING.md](SCHEMA_DIFFING.md). It can compare any release that has
a LinkML schema, but it needs the right path for each side, and releases before
v6.2.0 keep the schema somewhere else. Check the table in SCHEMA_DIFFING.md
before choosing a base older than v6.2.0.

Leave the action's `diff_old` input empty and it compares against the most
recent full release, so there is no default to keep up to date. Fill it in for a
major release, where the useful baseline is the previous major rather than the
last patch: v7.0.0 was compared against v6.0.0, not v6.3.1. A base older than
v6.2.0 needs `diff_old_path` changed too.

The generated release notes cover the span between two tags, which is not
necessarily the span the schema comparisons cover. When they differ, say so in
the release body, or a reader will assume the pull requests listed are what
produced the schema changes reported.

## Publishing a release candidate

`policy.md` requires a release candidate before every major and minor release. A
candidate follows the steps above with three differences:

- Use a version of the form `X.Y.Z-rcN`, for example `7.0.0-rc1`. The workflow
  accepts a semver pre-release suffix, and the schema version in step 1 must
  match it.
- Tick "Set as a pre-release" when publishing. This keeps the candidate off
  `/releases/latest`, so anything resolving "the current MIxS" still gets the
  last full release.
- Do not tick "Set as the latest release".

The schema version on `main` reads `X.Y.Z-rcN` for as long as the candidate
stands. Before cutting the real release, bump it back to `X.Y.Z` and merge that
first, or the release will ship a schema that declares itself a candidate.

## Adding the schema-diff summaries and publishing them

The structured diff is complete but large. Before the release pull request is
reviewed, add a readable summary to the release branch and put it on the docs
site:

1. Check out the `release/vX.Y.Z` branch.
2. The release action already wrote the diff into a folder under
   `assets/diff_results/`, named from the two refs you gave it. If both were
   release refs the name is already what you want. If either was a moving ref,
   the name follows it: dispatching with `diff_new` `main` produces
   `mixs6.0.0_to_main/`, which should be renamed to the versions it compares,
   `v6.0.0_to_v7.0.0/`, so the published page is named for releases rather than
   for a branch that keeps moving. Work in that folder; the docs build publishes
   summaries only from folders under `assets/diff_results/`.
3. Write `agent_summary.md` next to the structured diff. The repository carries
   a Claude Code skill for this, invoked as
   `/mixs-diff-summary assets/diff_results/<old>_to_<new>/schema_comparison_results.yaml`,
   which reads the diff and writes the summary. The skill is a convenience, not
   a requirement: it lives in `.claude/skills/mixs-diff-summary/SKILL.md`, and
   anyone not using Claude Code can read that file and write the summary the
   same way by hand, or with another assistant.
4. Commit both `agent_summary.md`, the readable summary you just wrote, and
   `tool_summary.md`, the counts the tool wrote alongside the structured diff.
   Do not write `tool_summary.md` by hand; if it is missing, rerun the tool.
5. Add both pages to the site nav. In `mkdocs.yml`, under the `Version changes`
   group, add two lines for this release:
   ```yaml
     - <old> to <new>: version-changes/<old>_to_<new>.md
     - <old> to <new> (counts): version-changes/<old>_to_<new>-counts.md
   ```
   Older releases have a second `(counts)` line pointing at a `-counts.md` page,
   generated from `tool_summary.md`. Add one only if the comparison actually has
   that file. The `gendoc` build step copies the summaries out of
   `assets/diff_results/<old>_to_<new>/` into `docs/version-changes/`, so no
   other change is needed.

This is done on the branch by a maintainer, not in CI. It needs no API keys, and
it is reviewed like any other change before merge.

## Generated files, and when they are refreshed

The files under `project/`, `src/mixs/datamodel/` and `contrib/` are generated
from `src/mixs/schema/mixs.yaml` by `make`, and they are committed because
downstream consumers fetch them directly. EBI OLS reads
`project/owl/mixs.owl.ttl` from raw `main`.

Four things can update them, and it is worth knowing which is which:

- **A pull request that edits only the schema** does neither. The "Regenerate
  and verify generated artifacts" workflow does not run on it, so the generated
  files in such a pull request are whatever its author put there, which is
  usually nothing. This is deliberate: it keeps a local build and a diff of
  several hundred generated files off contributors.
- **A pull request that edits a build input** (`Makefile`, `src/sparql/**`,
  `project-generator-config.yaml`) runs the workflow, which runs `make
  gen-project` and fails if `project/jsonschema/` no longer matches what is
  committed. That is the whole check: it does not regenerate or compare the OWL,
  `contrib/`, or the Python datamodel, so a build-input change that affects only
  those passes.
- **A push to `main`** runs nothing. The workflow's push trigger is disabled
  while [issue 1303](https://github.com/GenomicsStandardsConsortium/mixs/issues/1303)
  is open, so merging a schema change refreshes no generated files.
- **The "Create Release PR" action** runs `make install clean all` on the branch
  it creates and commits everything that produces, so a release cut this way
  carries generated files built from the schema it ships. This is the action
  doing it, not the branch: a release branch assembled by hand gets no rebuild,
  and would carry whatever `main` had at the time.

### What this means if you merge a schema change

Merging a pull request that changes only the schema leaves the committed
generated files describing the state before your change. Nothing refreshes them
on merge, and nothing warns you either way. The
committed files on `main` are not guaranteed to match
`src/mixs/schema/mixs.yaml` at any given moment.

This matters because consumers read those files rather than building the schema
themselves, so a stale file is what they get.

Cutting a release is what brings them back into agreement, because the release
action rebuilds everything from the schema and commits the result.

Do not commit generated files built on your own machine. Building locally to
check something is fine, and `make install clean all` is how, but the output is
not identical to what the release action produces: a local build of an unchanged
schema still differs from the committed copy in the JSON-LD context and in
generation timestamps. Committing that replaces files built by the release with
files built somewhere else, in a diff of several hundred files that no reviewer
can meaningfully read.

Do not assume the committed files match `main`. Check the file you care about.

Whether this should stay as it is, and what to do instead, is open in
[issue 1303](https://github.com/GenomicsStandardsConsortium/mixs/issues/1303).
Nothing here describes a settled decision.

Do not hand-edit generated artifacts.
