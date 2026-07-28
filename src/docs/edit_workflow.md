# MIxS Editing Workflows and Good Practices

Please try to follow this document. First read the [policies](policy.md) document.

# Terms

## Requesting and creating a new term

## Requesting a MIxS ID

MIxS IDs are allocated by the CIG from a registry maintained outside this
repository. **Do not assign one yourself, and do not reuse a number that looks
free in the schema.** Request one on the GitHub issue for the term, and a CIG
member with registry access will allocate it and record it there.

Terms and structural elements come from different ranges: terms use the
`slot_uri` range, and checklists, extensions and combinations use the
`class_uri` range. A CIG member will tell you which applies and what the next
number is.

The order matters. The ID is added after the term is approved and before the
pull request is merged. Placeholder values such as `MIXS:XXXXXXXXX` must not
reach `main`; 44 terms did in 2026 and had to be corrected afterwards.


## Requesting and implementing a term update


## Requesting and implementing a term deprecation 

# Checklists, extensions, and combinations

Define what they are

## Requesting and creating a new checklist or extension

## Updating an existing checklist or extension

# Releases

The GSC creates releases using semantic versioning (major.minor.patch).

## Version strings

MIxS carries two version numbers, managed differently. Both use bare `X.Y.Z` values (no `v`); the `v` is a git tag label only.

- **Python package version** (`pyproject.toml`): derived from the git tag by `poetry-dynamic-versioning`. It is not edited by hand; `pyproject.toml` holds a `0.0.0` placeholder on `main`, and the real value is stamped from the tag at build time.
- **Schema version** (`src/mixs/schema/mixs.yaml` `version:`): this is content. It flows into the generated OWL (`pav:version`), which EBI OLS reads, and into the JSON Schema and datamodel. It is bumped by hand as part of a release (see below), following the same pattern as `biolink-model`.

## Cutting a release

1. Bump the schema version by editing the `version:` field near the top of `src/mixs/schema/mixs.yaml` to the new release number (bare `X.Y.Z`). Commit it to `main` via the normal PR process. Pushing this to `main` triggers the "Regenerate and verify generated artifacts" workflow, which regenerates the OWL and other `project/` artifacts so they carry the new version.
2. Run the "Create Release PR" GitHub Action (manual dispatch) with the same version. It bumps `CITATION.cff`, `.zenodo.json`, and `release/README.md`, generates the schema diff, and opens a `release/vX.Y.Z` PR. It does not touch `pyproject.toml` (dynamic) or `mixs.yaml` (already bumped in step 1).
3. Add the schema-diff summaries to the release branch (see below).
4. **Approve the workflows on the release pull request.** It is opened by the
   workflow itself, so GitHub does not run any checks on it until a maintainer
   clicks "approve and run workflows". Until then the pull request has no checks
   at all, rather than failing ones, which is easy to miss.
5. Review and merge the release pull request.
6. Create a GitHub Release. Tag `vX.Y.Z`, target `main` so the tag lands on the
   merge commit rather than the release branch, and generate release notes
   against the previous release as the "Previous tag". For a release candidate,
   see [Publishing a release candidate](#publishing-a-release-candidate) below.

The structured diff in step 2 is produced by the reusable `diff-releases` tool; see [SCHEMA_DIFFING.md](SCHEMA_DIFFING.md). Note that it can only reach back to v6.2.0, because the workflow asks for `src/mixs/schema/mixs.yaml` on both sides and that path does not exist in earlier releases.

The release notes cover the span between two tags, which is not necessarily the span the schema comparisons cover. If they differ, say so in the release body, or a reader will assume the pull requests listed produced the schema changes reported.

## Publishing a release candidate

`policy.md` requires a release candidate before every major and minor release. A candidate goes through the same steps above, with three differences:

- Use a version of the form `X.Y.Z-rcN`, for example `7.0.0-rc1`. The workflow accepts a semver pre-release suffix, and the schema version in step 1 must match it.
- Tick **Set as a pre-release** when creating the GitHub Release. This keeps the candidate off `/releases/latest`, so anything resolving "the current MIxS" continues to get the last full release.
- Do not tick **Set as the latest release**.

The schema version on `main` will read `X.Y.Z-rcN` for as long as the candidate stands. Before cutting the real release, bump it back to `X.Y.Z` and merge that first, or the release will ship a schema declaring itself a candidate.

## Adding the schema-diff summaries and publishing them

The structured diff is complete but large. Before the release PR is reviewed, add
readable summaries to the release branch and put them on the docs site:

1. Check out the `release/vX.Y.Z` branch.
2. The release action already wrote the diff into a per-release folder,
   `assets/diff_results/<old>_to_<new>/` (for example `v6.2.0_to_v6.3.0/`). Work
   in that folder. (The docs build publishes summaries only from these
   per-release folders.)
3. Run the `mixs-diff-summary` skill on the structured diff, for example
   `/mixs-diff-summary assets/diff_results/<old>_to_<new>/schema_comparison_results.yaml`.
   It writes `agent_summary.md` next to the structured diff.
4. Commit `agent_summary.md` (the readable summary). Older comparisons also
   carry a `tool_summary.md` with raw counts, but the reusable `diff-releases`
   tool does not write one, so a new comparison will not have it. Do not write
   one by hand: it would claim to be tool output that cannot be regenerated.
   See issue 1318.
5. Add the two pages to the site nav. In `mkdocs.yml`, under the `Version changes`
   group, add two lines for this release:
   ```yaml
     - <old> to <new>: version-changes/<old>_to_<new>.md
     - <old> to <new> (counts): version-changes/<old>_to_<new>-counts.md
   ```
   The `gendoc` build step copies the two summaries out of
   `assets/diff_results/<old>_to_<new>/` into `docs/version-changes/`
   automatically, so no other change is needed.

This runs on the branch, done by a maintainer or an agent, not in CI. It needs no
API keys, and everything is reviewed like any other change before merge.

## Reviewing and publishing

- A TWG member other than the PR author reviews the version bumps and the schema
  diff summary. The pre-merge checklist is in the PR body.
- After merge, create the GitHub Release with tag `vX.Y.Z` and publish.

## Keeping generated artifacts current

The committed artifacts under `project/`, `src/mixs/datamodel/`, and `contrib/` are generated from the schema. The "Regenerate and verify generated artifacts" workflow keeps them in sync. On a push to `main` that changes the schema or its build inputs, it regenerates everything and commits the refreshed artifacts. On a pull request it regenerates and fails if the committed artifacts are stale.

The check uses `project/jsonschema/mixs.schema.json` as its signal, because that file regenerates deterministically. The OWL (`project/owl/mixs.owl.ttl`) is not byte-reproducible: RDF/Turtle serialization reorders triples and blank nodes on every run, so it is regenerated and committed but not compared by diff. Do not hand-edit generated artifacts.


# LinkML Updates 

# Documentation
Autogenerated documentation is created with every PR
Sujay's fork allows you to preview what will be regenerated. Important for when the documentation technology changes.

------------------
Content copied over:

- All change requests to the GSC should be captured in an issue.
   - Issues should be descriptive and provide clear requests and changes. Issue templates are available and should be used when possible.
   - One change should be proposed per issue. If multiple issues are related, you can leverage a GitHub super issue to connect related items.

- All branches should be tied to issues and the branch name should relate to the issue it's tied to.
  - This can be accomplished easily using the GitHub "create a branch" tool when viewing the issue on the webpage.

- All pushes, pull requests, and changes should be related to a single issue, and issues should be a single change per issue.
  - Issues and their associated pull requests should be small and targeted. One change per issue and pull request.

- All branches and pull requests should be tied to an issue.

- When making a pull request, contributions can continue to be made and built, but within scope of the related issue.
  - Making a draft pull request can be done to confirm changes are being done correctly

- Provide a reviewer for pull requests. 
  - Pull requests must be reviewed by a member of the GSC Technical Working Group
  - A Pull request requires someone other than the person that created the pull request
  - Include issue author as a pull request reviewer

- Once a pull request is started, all further discussion, review, and changes, happen in the pull request (rather than the issue). 
  - ?? Using conversations within PRs (TODO: add links to GH documentation)

- When a pull request is merged, the associated branch should be deleted and issue closed.

- The GSC will create releases (ADD Details, # of PRs? on a schedule?)
  - The GSC will use semantic versioning for releases: 3 digits (major, minor, patch)
  - Create a project for the release or other large change set
  - A change log for a release will be generated from all the pull requests that are part of the repository since the last release.

- All issues that pertain to a release should be part of a project for that release.

- Contributions should NOT be made in a fork. 
  - If external parties make a fork, it should be tied to an issue. Forks will only be merged back in following the above criteria for branches and small changes.
  - It is expected that external parties will discuss with the Technical Working Group before making changes on a scale that require a fork (e.g. a new checklist or extension).
  - The preference is to avoid forks and will be reviewed on a case by case basis.
  - Whenever a fork is created, a Technical Working Group member will reach out to the creator

- Add require a description to the suggested new thing to the requirements
- New extensions or checklists should be tracked using GitHub Projects

- Add require a description to the suggested new thing to the requirements
- New extensions or checklists should be tracked using GitHub Projects
