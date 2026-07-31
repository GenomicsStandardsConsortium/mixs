# Contributing to mixs

:+1: First of all: Thank you for taking the time to contribute!

The following is a set of general guidelines for contributing to MIxS. 

For a more detailed guide to MIxS editing and contributing policies, see the [contributing documentation](https://github.com/GenomicsStandardsConsortium/mixs/blob/main/src/docs).

## Table Of Contents

* [Introduction](#introduction)
* [Code of Conduct](#code-of-conduct)
* [MIxS transition to LinkML](#linkml)
* [Guidelines for Contributions and Requests](#contributions)
* [Best Practices](#best-practices)
  * [How to write a great issue](#great-issues)
  * [How to create a great pull/merge request](#great-pulls)
* [Guidelines for GSC developers](#gsc-devs)

<a id="introduction"></a>
## Introduction

The Minimum Information about any(x) Sequence (MIxS) standard, maintained by the Genomic Standards Consortium (GSC), is community built and developed to improve FAIR (findable, accessible, interoperable, and reusable) data and data sharing. Below you'll find documentation on how to contribute to or make suggested changes to the GSC's MIxS standard. Additionally, you'll find policies about workflows and requirements for contributions.

MIxS static documentation lives in this repo under src/docs as markdown files. Where applicable, static documents will be used to create GSC website pages.

<a id="code-of-conduct"></a>
## Code of Conduct

The mixs team strives to create a welcoming environment for editors, users and other contributors.
Please carefully read our [Code of Conduct](CODE_OF_CONDUCT.md).

<a id="linkml"></a>
## MIxS transition to LinkML 

With the release of MIxS 6.0, management of MIxS switched to fully using GitHub for edits and releases and to using [Linkml](https://linkml.io/) to define the MIxS schema. The release of MIxS 6.2.0 made the switch to using "out of the box" LinkML code rather than customizations. The biggest change was to remove any dependencies on an external spreadsheet for generating LinkML YAML files. The source of truth (SOT) for editing MIxS is now [the YAML file](https://github.com/GenomicsStandardsConsortium/mixs/blob/main/src/mixs/schema/mixs.yaml). However, since this was a minor release, most repositories implementing MIxS will continue to use the generated artifacts from MIxS 6.1 until MIxS 7 is released.

This section will be update or deleted after the release of MIxS 7.

<a id="contributions"></a>
## Guidelines for Contributions and Requests

Please review the [MIxS editing policies](src/docs/policy.md) before making contributions to this repo.

For guidance on how to request a new checklist or package, request a new term or update to an existing term, or report an issue with the MIxS code, please see [the workflows document](src/docs/edit_workflow.md).

For guidance on how to use LinkML or contribute to the core LinkML code, please see [the LinkML documentation](https://linkml.io/linkml/).

<a id="best-practices"></a>
## Best Practices

<a id="great-issues"></a>
### How to write a great issue

Please review GitHub's overview article,
["Tracking Your Work with Issues"][about-issues].

<a id="great-pulls"></a>
### How to create a great pull/merge request

Please review GitHub's article, ["About Pull Requests"][about-pulls],
and make your changes on a [new branch][about-branches].

#### What to edit

`src/mixs/schema/mixs.yaml` is the only file you should edit by hand to change
the standard. Everything under `project/`, `contrib/`, `src/mixs/datamodel/`, and
`docs/` is generated from it, and an edit there is overwritten the next time the
artifacts are regenerated.

#### Naming branches and pull requests

Name things for what changed, so a reviewer can tell without opening the diff.

- **Branch**: name it for the change, not for a person or a requesting group, and
  prefix it with the issue number when you have one.
  Avoid `partner-request` or `updates`; prefer `1234-add-water-depth-enum-values`.
- **Pull request title**: state the change in the title.
  Avoid "Changes to accommodate a collaborator's needs"; prefer "Add enum values
  for water depth ranges".
- **Pull request description**: lead with why the change is needed, and link the
  issue. The diff already shows what changed, so keep any itemised list as
  supporting detail rather than the whole description.

#### Reading a Copilot review

Copilot splits its output in two, and the halves are not equally visible. Inline
comments appear against the diff. Everything else goes into a collapsed block
headed "Suppressed comments", which you have to click to open.

**Open it before approving.** On this repository that block is where most of the
substantive findings arrive, and a review can say "generated no comments" while
holding a real one. Examples from a single day of work:

- a new test file that never ran, because it was written for `pytest` while
  `make test-python` runs `python -m unittest discover`
- generated files under `contrib/` committed by accident, carrying unrelated
  schema changes into a pull request about something else
- a script that produced a stack trace on a network failure instead of naming
  the artifact it could not fetch

Suppressed comments have no reply thread, so answer them in a normal pull request
comment saying what you changed or why you disagree. Inline comments should be
answered inline.

Treat both halves as a reviewer's opinion rather than a verdict. Some findings
are wrong, and a wrong one is worth a short reply explaining why, so the next
reader does not have to work it out again.

#### Linting checks

Two checks lint the schema on every pull request that touches it, and **both fail
when they find a problem**. A red check means there is something to fix.

- **LinkML Linting** validates the schema against the LinkML metamodel.
- **Yamllint** checks the YAML formatting of `src/mixs/schema`.

Findings appear in three places, so you should not need to dig through logs:

1. The **job summary**, at the top of the workflow run page, listing every finding.
2. **Annotations on the diff** of your pull request, for Yamllint.
3. A **pull request comment**, when the pull request comes from a branch in this
   repository.

The comment is the only one of those that needs write access, and a pull request
from a fork gets a read-only token, so forks get the job summary and annotations
instead. The checks themselves, and their pass or fail result, are identical either
way. Nothing about the linting is skipped for a fork.

Trailing whitespace is the most common Yamllint failure and is invisible in most
editors. To fix it:

```bash
make fix-whitespace
```

You can run either linter locally before pushing:

```bash
make linkml-lint
make yaml-lint
```

[about-branches]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches
[about-issues]: https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues
[about-pulls]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
[issues]: https://github.com/GenomicsStandardsConsortium/mixs/issues/
[pulls]: https://github.com/GenomicsStandardsConsortium/mixs/pulls/

<a id="gsc-devs"></a>

## Guidelines for GSC developers

If you're a GSC developer with editing rights, the advice and guidelines above still hold. You should always create an issue for each proposed change (keeping them atomic: one issue per logical change), create a branch from that issue, and - once you've made your changes on the branch - create a pull request for review and validation. 

However, here are some guidelines on where and what to edit for a few routine tasks.

### Editing the MIxS specification 

To edit the MIxS terms, you'll need to edit the YAML file that drives the creation of the MIxS specification in its various serialisations.
This file is located in:
`/src/mixs/schema/`

Once you've created an issue, branch, and done some editing on that branch, create a PR to have your proposed changes reviewed by the Technical WG. 
Minor edits (e.g. fixing typos, clarifying edits of descriptions, etc) can be included in a patch, while any new terms or consequential edits to terms or their properties should be coordinated with minor / major release processes.
