# MIxS Editing Workflows and Good Practices

Please try to follow this document. First read the [policies](policies) document.

# Terms

## Requesting and creating a new term

## Requesting and implementing a term update


## Requesting and implementing a term deprecation 

# Checklists, extensions, and combinations

Define what they are

## Requesting and creating a new checklist or extension

## Updating an existing checklist or extension

# Releases

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
