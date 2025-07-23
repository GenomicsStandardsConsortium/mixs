# Introduction

This document records policies about editing and contributing to MIxS which are enacted via [editing workflows](edit_workflow.md). Documentation in this repository is considered authoritative and supercedes any previous documentation in Google Drive or the gensc.org website, although content from this repository may be duplicated in those or other locations. All new editing and contributing policies must be approved by the Technical Working Group (TWG) and Compliance and Interoperability Group (CIG).

## MIxS transition to LinkML Details

With the release of MIxS 6.0, management of MIxS switched to fulling using GitHub for edits and releases and to using [Linkml](https://linkml.io/). The release of MIxS 6.2.0 made the switch to using "out of the box" LinkML code rather than customizations. The biggest changes was to remove any dependencies on an external spreadsheet for generating the LinkML YAML file. The source of truth (SOT) for editing MIxS is now [the YAML file](https://github.com/GenomicsStandardsConsortium/mixs/blob/main/src/mixs/schema/mixs.yaml). However, since this was a minor release, most repositories implementing MIxS will continue to use the generated artifacts from MIxS 6.1 until MIxS 7 is released.

NOTE: Update this section after the release of MIxS 7.

# GitHub Editing Policies

The GSC leverages GitHub tools to manage MIxS terms, checklists, extensions, and releases. GSC meeting notes, including CIG, TWG, and Board meetings, are NOT authoritative but exist to support development in this repository. GitHub issues, pull requests, and releases will contain the source of truth. Documentation will be generated from GitHub. Below are guidance and policies on how to contribute to MIxS. Specific details on how to use GitHub for contributions are available in the [editing workflows](edit_workflow.md) document.

### Editing policies
* All change requests to the GSC should be captured in an issue.
  * Issues should be descriptive and provide clear requests and changes. Issue templates are available and should be used when possible.
  *  One change should be proposed per issue. If multiple issues are related, you can leverage a GitHub super issue to connect related items.
* All branches should be tied to issues and the branch name should relate to the issue it's tied to.
  * More details on how to easily accomplish this using the GitHub "create a branch" tool are provided in the editing workflows.
* All pushes, pull requests, and changes should be related to a single issue, and issues should be a single change per issue.
  * Issues and their associated pull requests should be small and targeted. One change per issue and pull request.
* All pull requests (PRs) must be reviewed by at least one other person besides the requester who is a member of the TWG. Additional reviewers are encouraged.
  * If the issue author does not make the PR, they should be included as a pull request reviewer.

**TODO:** Add policy about who can commit directly to mixs repo and merge pull requests. CREATE AN ISSUE FOR THIS!!!
* should anyone be allowed to commit directly to main (PRs are merged, not committed)
* rules  allow us to control this
* Who has permission to create branches is controlled by roles

# Release Policies
The GSC (through the CIG and with support from the TWG) creates major releases for MIxS approximately one time per year. MIxS uses semantic versioning for releases: 3 digits (major, minor, patch).

## Major Releases
* Before a major release, the CIG and TWG must generate a release candidate.
* Major releases contain new checklists, extensions, and terms.
* Major releases may also include the types of changes allowed in minor or patch releases.
* Major releases must be reviewed by the CIG, TWG, GSC board, and the list of repositories using MIxS.
  * TODO: Create a list in this repo of who are external reviews. Assign a responsible person to maintain that list and to maintain the emails in a separate private document.
* The CIG manages the distribution of and feedback from major releases and provides outreach about new releases.
* At least x months must be provided for feedback on major releases before they are published.
* Repositories that are MIxS compliant must adopt major releases within X months of their release.

## Minor Releases
* Before a minor release, the CIG and TWG must generate a release candidate.
* Minor releases CANNOT contain new checklists or extensions.
* Minor releases can include updates to existing terms.
* Minor releases may include new terms, but those terms are not consider "official" until the next major release. **TODO:**  Discuss this policy
* Minor releases must be reviewed by the CIG and TWG. Other interested parties may review minor releases using GitHub.
* Depending on whether the minor release is more technical or content focused, either the TWG or CIG manages the distribution of and feedback and provides outreach about new minor releases.
* At least x weeks must be provided for feedback on major releases before they are published.
* Repositories that are MIxS compliant are not required to adopt minor releases.

## Patch Releases
* Patch releases are used to correct errors in elements (checklists, extensions, or terms) that do no substantively change the content of the element.
* Patch releases may be used to update documentation.

# Policies for Community Contributions to MIxS

This section provides policies about contributing to MIxS. See the [editing workflows](edit_workflow.md) document for how to request, update, or deprecate a checklist, extension, or term.

It is the responsibility of the CIG to work with contributors to ensure that their proposal meets MIxS and GSC requirements for content. It is the responsibility of the TWG to work with the CIG and external contributors to ensure that proposed changes meet MIxS technical requirments. 

## Checklists and Extension

Most new checklists, extensions, and combinations are contributed to MIxS by external research communities. If an indivudual or single organization wants a new checklist or extension, we strongly recommend that they first enlist broad participation from the relevant community to ensure that the request is supported by community consensus. Often, the community has spent considerable time defining their contribution before approaching MIxS, but we encourage communities to engage with the GSC as early as possible. 

See the MIxS documentation for a definitions of checklist, extension, and combination. **TODO:** Add link when it is ready.

## Terms

Changes to terms (addtion, deletion/deprecation, modification) are made by individuals, organizations (e.g., repositories working with MIxS), or communities. They may stand along or part of a new checklist or extension.

Procedures for changing terms are described in the [editing workflows](edit_workflow.md) document. All terms related requests must come through an issue in this GitHub repository. 

# What it means to be MIxS Compliant
As a standards organization, GSC has expections of what it means to be compliant with their standards. For MIxS, this  means...

**TODO:** Decide on and document what MIxS Compliant means and if/how to enforce it.
