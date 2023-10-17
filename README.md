# mixs

MIxS: the Minimum Information about any (X) Sequence standard

## Website

[https://GenomicsStandardsConsortium.github.io/mixs](https://GenomicsStandardsConsortium.github.io/mixs)

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
