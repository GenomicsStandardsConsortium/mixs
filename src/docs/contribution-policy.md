# Introduction

This documentation is intended to guide MIxS editors, including TWG editors who can commit to this repository, external working groups who would like to contribute a new checklist or package, and external individuals or groups who want to request a new term or term update. This documentaiton is not meant for external users, such as repositories or researchers, who want to know [how to use MIxS](https://github.com/GenomicsStandardsConsortium/mixs/blob/main/src/mixs/schema/mixs.yaml). 

The MIxS standard, maintained by the Genomic Standards Consortium (GSC), is community built and developed to improve FAIR data and data sharing. Below you'll find documentation on how to contribute to or make suggested changes to the GSC's MIxS standard. Additionally, you'll find policy around workflows and requirements for contributions.

MIxS static documentation lives in this repo under src/docs as markdown files. Where applicable, static documents will be used to create GSC website pages.

## MIxS transition to LinkML Details

With the release of MIxS 6.0, management of MIxS switched to fulling using GitHub for edits and releases and to using [Linkml](https://linkml.io/). The release of MIxS 6.2.0 made the switch to using "out of the box" LinkML code rather than customizations. The biggest changes was to remove any dependencies on an external spreadsheet for generating the LinkML YAML file. The source of truth (SOT) for editing MIxS is now [the YAML file](https://github.com/GenomicsStandardsConsortium/mixs/blob/main/src/mixs/schema/mixs.yaml). However, since this was a minor release, most repositories implementing MIxS will continue to use the generated artifacts from MIxS 6.1 until MIxS 7 is released.

NOTE: Update this section after the release of MIxS 7.

## GitHub Policy

The GSC leverages GitHub tools to manage its extensions, checklists, and releases. GSC meeting notes are NOT authoritative. GitHub issues, pull requests, and releases will contain the source of truth. Documentation will be generated from GitHub. Below are guidance and policies on how to contribute to the GSC and appropriately use the available tools.

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

## Community Contributions to GSC

### Suggesting a new term

### Requesting a term update

### Requesting a term deprecation 

### Requesting a new Checklist or Extension

- Add require a description to the suggested new thing to the requirements
- New extensions or checklists should be tracked using GitHub Projects
