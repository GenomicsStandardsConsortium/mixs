# Contributing to mixs

:+1: First of all: Thank you for taking the time to contribute!

The following is a set of guidelines for contributing to
mixs. These guidelines are not strict rules.
Use your best judgment, and feel free to propose changes to this document
in a pull request.

## Table Of Contents

* [Code of Conduct](#code-of-conduct)
* [Guidelines for Contributions and Requests](#contributions)
  * [Reporting problems with the data model](#reporting-bugs)
  * [Requesting new terms](#requesting-terms)
  * [Adding new terms yourself](#adding-terms)
* [Best Practices](#best-practices)
  * [How to write a great issue](#great-issues)
  * [How to create a great pull/merge request](#great-pulls)
* [Guidelines for GSC developers](#gsc-devs)

<a id="code-of-conduct"></a>

## Code of Conduct

The mixs team strives to create a
welcoming environment for editors, users and other contributors.
Please carefully read our [Code of Conduct](CODE_OF_CONDUCT.md).

<a id="contributions"></a>

## Guidelines for Contributions and Requests

<a id="reporting-bugs"></a>

### Reporting problems with the data model

Please use our [Issue Tracker][issues] to report problems with the ontology.

<a id="requesting-terms"></a>

### Requesting new terms

Please use our [Issue Tracker][issues] to request a new term for the ontology.

<a id="adding-terms"></a>

### Adding new terms yourself

Please submit a [Pull Request][pulls] to submit a new term for consideration.

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

[about-branches]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches
[about-issues]: https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues
[about-pulls]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
[issues]: https://github.com/GenomicsStandardsConsortium/mixs-6-2-for-merge/issues/
[pulls]: https://github.com/GenomicsStandardsConsortium/mixs-6-2-for-merge/pulls/

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
