# Introduction

The MIxS standard maintained by the Genomic Standards Consortium (GSC) is community built and developed to improve FAIR data and data sharing. Below you'll find documentation on how to contribute to or make suggested changes to the GSC's MIxS standard. Additionally, you'll find policy around workflow and requirements for contributions.

The GSC's static documentation will live under src/docs as markdown files. Anywhere applicable, these will be used to create GSC websites.

_add more_

## GSC transition to LinkML Details

_links to LinkML documentation about classes_

- This should maybe go somewhere else?

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
