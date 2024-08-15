# MIxS: Minimum Information about any (X) Sequence

⚠️ ⚠️ ⚠️ 

The GSC is preparing for the MIxS 6.2.0 release. Thanks to everyone who has contributed in any way!

The new release primarily consists of converting a spreadsheet expressing MIxS 6.1 into a [LinkML artifact, which now serves as the source of truth](https://github.com/GenomicsStandardsConsortium/mixs/blob/main/src/mixs/schema/mixs.yaml). 
We have also started to follow the [LinkML cookiecutter layout](https://github.com/linkml/linkml-project-cookiecutter).
MIxS users should see very few changes in the content, although legacy term attributes like "Definition", "Expected value", "Value syntax" and "Section" have been broken down into their LinkML equivalents, 
like `description`, `range`, `pattern` and `in_subset`.

We have [some known issues](https://github.com/GenomicsStandardsConsortium/mixs/issues?q=is%3Aissue+is%3Aopen+label%3A6.1.1-%3E6.2.0), and you may find others. [Please report them](https://github.com/GenomicsStandardsConsortium/mixs/issues) including text snippets and or screen shots!

**Until this message is removed:**
-  You can continue to use any MIxS 6.0 to 6.1.1 artifacts you have previously downloaded.
 - Or start some new downloads by browsing https://github.com/GenomicsStandardsConsortium/mixs/tree/mixs6.1.1/mixs.

If you have questions or concerns in the interim, please contact gensc-twg@groups.google.com

⚠️ ⚠️ ⚠️ 

## Documentation Website

[https://w3id.org/mixs](https://w3id.org/mixs)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [mixs](src/mixs)
    * [schema](src/mixs/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/mixs/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
