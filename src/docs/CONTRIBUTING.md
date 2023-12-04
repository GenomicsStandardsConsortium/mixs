# Contributing to MIxS

:+1: First of all: Thank you for taking the time to contribute!

This documentation is intended to guide MIxS editors, including TWG editors who can commit to this repository, external working groups who would like to contribute a new checklist or package, and external individuals or groups who want to request a new term or term update. This documentaiton is not meant for external users, such as repositories or researchers, who want to know [how to use MIxS](https://github.com/GenomicsStandardsConsortium/mixs/blob/main/src/mixs/schema/mixs.yaml).  

These guidelines are still under development. Feel free to propose changes to this document in a pull request.

## Code of Conduct

The MIxS team strives to create a welcoming environment for editors, users and other contributors.
Please carefully read our [Code of Conduct](CODE_OF_CONDUCT.md) before making a contribution.

# Introduction


The Minimum Information about any(x) Sequence (MIxS) standard, maintained by the Genomic Standards Consortium (GSC), is community built and developed to improve FAIR data and data sharing. Below you'll find documentation on how to contribute to or make suggested changes to the GSC's MIxS standard. Additionally, you'll find policy around workflows and requirements for contributions.

MIxS static documentation lives in this repo under src/docs as markdown files. Where applicable, static documents will be used to create GSC website pages.

## MIxS transition to LinkML Details

With the release of MIxS 6.0, management of MIxS switched to fulling using GitHub for edits and releases and to using [Linkml](https://linkml.io/). The release of MIxS 6.2.0 made the switch to using "out of the box" LinkML code rather than customizations. The biggest changes was to remove any dependencies on an external spreadsheet for generating the LinkML YAML file. The source of truth (SOT) for editing MIxS is now [the YAML file](https://github.com/GenomicsStandardsConsortium/mixs/blob/main/src/mixs/schema/mixs.yaml). However, since this was a minor release, most repositories implementing MIxS will continue to use the generated artifacts from MIxS 6.1 until MIxS 7 is released.

NOTE: Update or delete this section after the release of MIxS 7.

# Guidelines for Contributions and Requests

For guidance on how to request a new checklist or package, request a new term or update to an existing term, or report an issue with the MIxS code, please see [the workflows document](worklows.md).

For MIxS editing policies please see the [editing policies document](policies.md).

To guidance on how to use LinkML or contribute to the core LinkML code, please see [the LinkML documentation](https://linkml.io/linkml/).

## GitHub Best Practices

### How to write a great issue

Please review GitHub's overview article,
["Tracking Your Work with Issues"][about-issues].

### How to create a great pull/merge request

Please review GitHub's article, ["About Pull Requests"][about-pulls],
and make your changes on a [new branch][about-branches].

[about-branches]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches
[about-issues]: https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues
[about-pulls]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
[issues]: https://github.com/GenomicsStandardsConsortium/mixs/issues/
[pulls]: https://github.com/GenomicsStandardsConsortium/mixs/pulls/
