# Contributing to mixs

:+1: First of all: Thank you for taking the time to contribute!

The following is a set of general guidelines for contributing to MIxS. 

For a more detailed guide to MIxS editing and contributing policies, see the [contributing documentation](https://github.com/GenomicsStandardsConsortium/mixs/blob/main/src/docs).

## Table Of Contents

* [Introduction](#introduction)
* [Code of Conduct](#code-of-conduct)
* [MIxS transition to LinkML ](linkml)
* [Guidelines for Contributions and Requests](#contributions)
* [Best Practices](#best-practices)
  * [How to write a great issue](#great-issues)
  * [How to create a great pull/merge request](#great-pulls)

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

Please review the [MIxS editing policies](policy.md) before making contributions to this repo.

For guidance on how to request a new checklist or package, request a new term or update to an existing term, or report an issue with the MIxS code, please see [the workflows document](worklow.md).

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

[about-branches]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches
[about-issues]: https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues
[about-pulls]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
[issues]: https://github.com/GenomicsStandardsConsortium/mixs/issues/
[pulls]: https://github.com/GenomicsStandardsConsortium/mixs/pulls/
