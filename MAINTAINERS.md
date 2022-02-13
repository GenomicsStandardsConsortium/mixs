# Maintaining the MIxS Schema
## Dependencies
In order to make new release of the schema, you must have the following installed on your sytem:
- [pipenv](https://pypi.org/project/pipenv/)
- [pandoc](https://pandoc.org/installing.html)
- [linkml](https://github.com/linkml/linkml)

A Pipfile.lock is include in the repository, but you can rebuild the lock file by executing `pipenv install -d`.

## Making changes to the MIxS Schema

**NOTE: This process will change. Do not follow it yet!**
In order to track changes made to the MIxS Schema, it is best maintained by following these steps:
1. Submit an [issue](https://github.com/microbiomedata/nmdc-schema/issues) detailing the desired changes.
2. Create a branch to address this issue that uses the same number as the issue tracker. For example, if the issue is `#50` in the issue tracker, name the branch `issue-50`. This allows other developers to easily know which branch needs to be checked out in order to contribute.
3. Create a pull request that fixes the issue. If possible, create a draft (or WIP) branch early in the process.
4. Merge pull request once all the necessary changes have been made. If needed, tag other developers to review pull request. 
5. Delete the issue branch (e.g., branch `issue-50`).

As you make you make changes to the MIxS Schema, it is **HIGHLY** recomended that you update the [Change log](add link) in order to easily document the changes when a release is made. In the [Change log](add link), the set of changes that have **not** been released appear under the section titled `Current (update before releasing)`. As you update the schema, add information to the following sections:
#### Added
  - Add information about new classes, slots, enums, etc. added to the schema.
#### Fixed
  - Add information about changes made to the schema that **fixes** a problem.
#### Changed 
  - Add information about changes made to the schema that were not made to fix a problem.
#### Removed
  - Add information about classes, slot, enums etc. removed from the schema

In each of the [Change log](add link) sections, it is helpful if you mention the issue that the change was meant to address. For example:  
#### Added
  - `alternative identifiers` slot added to biosamples (cf. issue 75).

See the [Change log](add link) for other examples.

When the pull request is merged into the `main` branch, new documentaiton will be generated for changes to the schema.


## Making a PyPI release of the NMDC Schema

**This section needs to be updated.**

The NMDC Schema is deployed to [PyPI](https://pypi.org/project/nmdc-schema/) via the [pypi-publish](https://github.com/microbiomedata/nmdc-schema/blob/main/.github/workflows/pypi-publish.yml) github action.

The steps for making a release are:
1. Generate the set of artifacts by running `make clean` followed by `make all`.
2. If **#1** succeeds and changes have been made to the schema, update the `version` in [nmdc.yaml](https://github.com/microbiomedata/nmdc-schema/blob/main/src/schema/nmdc.yaml) using the format `YYYY.MM.DD`. Note: Changes can be made to the Python package (e.g., functionality added to the CLI) that do not affect the schema. In these cases, the schema does not need to be changed.
3. If **#1** succeeds:
  * Make the sure the sections of the [Change log](https://github.com/microbiomedata/nmdc-schema/blob/main/CHANGELOG.md) (discussed above) have been updated appropriately.
  * Change the `Current (update before releasing)` section of the [Change log](https://github.com/microbiomedata/nmdc-schema/blob/main/CHANGELOG.md) into a hyperlink that matches the tag you assign to the release in step **#4** below.  
  For example if the tag assigned for the release is `2021.07.01rc1`, change the section to:  
  ```
  [2021.07.01rc1](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.07.01rc1)
  ```
4. Create a Github release of the schema using the `Releases -> Draft new release` links. The tag of the release must conform to the format `YYYY.MM.DDrc<num>`, where `<num>` is a sequential number of the releases made for that day. For example, if two releases were made on `2021-07-01`, then the tags for that day would be `2021-07-01rc1`, `2021-07-01rc2`. The value of this tag needs to match the value you assigned to the `Current (update before releasing)` section in the [Change log](https://github.com/microbiomedata/nmdc-schema/blob/main/CHANGELOG.md) (discussed above).
5. Name the release using the format `release-<tag>`, where tag matches the value of the tag you created in **#4**.
6. Fill in the changes made for this release. This is most easily done by copying the information you recorded in the [Change log](https://github.com/microbiomedata/nmdc-schema/blob/main/CHANGELOG.md).
7. Click `Publish release` button. This fires the action to update the [PyPI package](https://pypi.org/project/nmdc-schema/).


## Maintaining the Documentation
Do **not** git add the files in `docs`. Custom documentation is added to (or edited in) the `src/docs/` directory.

The new documentation is deployed when changes are pushed to the main branch via the [build-deploy-documentation](https://github.com/microbiomedata/nmdc-schema/blob/main/.github/workflows/build-deploy-documentation.yaml) workflow.


After the github action completes, the documentation will be available from a URL [https://microbiomedata.github.io/nmdc-schema](https://microbiomedata.github.io/nmdc-schema/)


# mixs-source


This repo contains the draft MIxS schema for environmental packages and checklists. 

Pages generated by this code will be served via https://github.com/GenomicsStandardsConsortium/gensc.github.io.

This repo may be merged with https://github.com/GenomicsStandardsConsortium/mixs

The source files are here:

 * model/
    * [schema/](model/schema/) -- schema files
       * [mixs.yaml](model/schema/mixs.yaml) - container module
       * [terms.yaml](model/schema/terms.yaml) - all terms (fields/slots)
       * [checklists.yaml](model/schema/checklists.yaml) - checklists, e.g. MIMAG
       * [soil.yaml](model/schema/soil.yaml) - soil package
       * ...OTHER PACKAGES HERE

These are the files that should be edited

## Workflow for adding new CHECKLISTS

Edit [checklists.yaml](model/schema/checklists.yaml)

The easiest thing to do is to copy and paste an existing checklist, modifying the values

You will need to specify both `slots` and `slot_usage`

## Workflow for adding new TERMS

Edit [terms.yaml](model/schema/terms.yaml)

The easiest thing to do is to copy and paste an existing term, e.g.

```yaml
  barometric_press:
    is_a: environment field
    aliases:
    - barometric pressure
    description: Force per unit area exerted against a surface by the weight of air
      above that surface
    range: quantity value
    examples:
    - value: 5 millibar
    comments:
    - 'Preferred unit: millibar'
    slot_uri: MIXS:0000096
```

The range field will be one of:

 - string
 - integer
 - float
 - quantity value
 - an enum

## Workflow for creating a new ENUM

TODO

## Workflow for adding new ENVIRONMENTAL PACKAGES

Create a NEW file in [model/schema](model/schema/)

The easiest thing to do is to copy a 

## Deploying Documentation

This is currently in a different repo

There is a demo of a fork of the github pages repo with markdown generated in this repo copied over:

[https://cmungall.github.io/gensc.github.io/mixs6/](https://cmungall.github.io/gensc.github.io/mixs6/)

We can consider merging repos, but for now these are distinct, and docs are copied from one to another like this:

```bash
make gen-docs
cp docs/*.md ../gensc.github.io/mixs6/
```

## Seeding the schema from google sheets

An early version of terms.yaml was by converting the legacy spreadhseet for MIxS6 using [mixs_converter.py](https://github.com/GenomicsStandardsConsortium/mixs-source/blob/main/gsctools/mixs_converter.py). After the release of MIxS6, the yaml will switch to being Source of Truth, and there will be no need to generate from sheets.

In the interim phase, see the Makefile for details on regenerating the yaml from google sheets/excel.


