<h1>Harmonized MIxS 6.2 Release Candidate</h1>

Documentation and data validator: http://w3id.org/mixs-6-2-rc/
- This validator does not submit data to any repository

<nav>
  <a href="https://github.com/turbomam/mixs-envo-struct-knowl-extraction">Repo</a>
  |
  <a href="https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues">Report Bug</a>
  |
  <a href="https://github.com/turbomam/mixs-envo-struct-knowl-extraction/releases">Releases</a>
</nav>

<!-- TABLE OF CONTENTS -->

<br><br>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>
<br><br>
<!-- ABOUT THE PROJECT -->

## About The Project

The _Minimal Information about any (x) Sequence_ (MIxS) standard is a product of the _[Genomic Standards Consortium](http://www.gensc.org/)_ (GSC). 
The GSC has a mission of enabling genomic data integration, discovery, and comparison through international community-driven standards.

This code repository was developed in collaboration between the _[National Microbiome Data Collaborative](https://microbiomedata.org/)_ (NMDC) and the GSC. It  transitions
a [spreadsheet version of the MIxS standard](https://github.com/GenomicsStandardsConsortium/mixs/blob/main/mixs/excel/mixs_v6.xlsx) into a machine-actionable, self-documenting schema adhering to the _[Linked Data Modelling Language](https://linkml.io/)_ (LinkML).

- Term attributes are harmonized
- Previously informal data constraints are formalized
- Implicit classes are made explicit
- Example data is provided
- Validation tools are provided

This work is provided for consideration as MIxS 6.2 and will be presented at the [23rd Genomic Standards Consortium Meeting](https://genomicsstandardsconsortium.github.io/GSC23-Bangkok/) in August 2023 in Bangkok, Thailand.

<!-- 
<h2>And future site of MIxS/EnvO Structured Knowledge Extraction</h2>

<p>Extracting structured knowledge from MIxS and finding EnvO terms that would be reasonable answers to scoped MIxS questions</p>
-->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

This is a standard Python project that runs on the CLI. No installation is required for 
- [viewing the schema file](https://github.com/microbiomedata/mixs-6-2-release-candidate/blob/main/generated-schema/mixs_6_2_rc.yaml)
- [accessing the schema in other formats](https://github.com/microbiomedata/mixs-6-2-release-candidate/tree/main/schema-derivatives)
- accessing examples of [valid](https://github.com/microbiomedata/mixs-6-2-release-candidate/tree/main/curated-data/valid) and [invalid](https://github.com/microbiomedata/mixs-6-2-release-candidate/tree/main/curated-data/invalid) [data in various formats](https://github.com/microbiomedata/mixs-6-2-release-candidate/tree/main/converted-data)
- [accessing reports about modifications applied](https://github.com/microbiomedata/mixs-6-2-release-candidate/tree/main/conflict-reports) 
- [visiting the documentation and ephemeral validator](http://w3id.org/mixs-6-2-rc/)

### Prerequisites for Rebuilding Locally

- software build tools like [GNU Make](https://www.gnu.org/software/make/) that are often present on many Linux and MacOS systems
  - or Windows systems using interoperability layers like [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
- python >= 3.9
- poetry >= 1.2

### First Time Setup

1. [Install Poetry](https://python-poetry.org/docs/#installation) if necessary
1. Install dependencies `> poetry install`
1. Run with `> make all`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

<!-- ## Usage

[TODO] Use this space to show useful examples of how a project can be used.

<p align="right">(<a href="#readme-top">back to top</a>)</p>  -->

<!-- ROADMAP -->

See the [open issues](https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues) for a full list of proposed
features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also
simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See [LICENSE.md](./LICENSE.md) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Contact

Mark Andrew Miller, [National Microbiome Data Collaborative](https://microbiomedata.org/), Lawrence Berkeley National Laboratory
- MAM@lbl.gov

<p align="right">(<a href="#readme-top">back to top</a>)</p>
