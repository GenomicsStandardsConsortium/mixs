# MIxS Evolution: From Spreadsheets to LinkML- A Guide to Recent Changes and Current Structure

Welcome to the Minimum Information about any (x) Sequence (MIxS) standard, maintained by the Genomic Standards
Consortium (GSC). MIxS provides a framework for describing sequences and samples across different environments.

## [Accessing MIxS Versions](#accessing-mixs-versions)

- Current version: [MIxS v6.2.0](https://github.com/GenomicsStandardsConsortium/mixs/releases/tag/v6.2.0)
- Last major release: [mixs6.0.0](https://github.com/GenomicsStandardsConsortium/mixs/releases/tag/mixs6.0.0)
- [View all releases on GitHub](https://github.com/GenomicsStandardsConsortium/mixs/releases)
- [Report issues or contribute](https://github.com/GenomicsStandardsConsortium/mixs/issues)

## [Official Releases and Versioning](#offical-releases-and-versioning)

The Genomic Standards Consortium (GSC) is the provider of official MIxS releases. MIxS uses a versioning system loosely
based on [semver](https://semver.org/), with major, minor and patch releases.

- Conceptual major versions (e.g., "v6") represent significant milestones in MIxS development but do not directly
  correspond to specific release tags.
- Actual releases are tagged with more specific version numbers (e.g., mixs6.0.0, mixs6.1.0, v6.2.0).
- The last release that could be considered a "major" release in terms of significant changes
  is [mixs6.0.0](https://github.com/GenomicsStandardsConsortium/mixs/releases/tag/mixs6.0.0).
    - [release/excel/mixs_v6.xlsx](excel/mixs_v6.xlsx) is an XLSX-formatted release file, with the terms assigned to
      each Checklist and Extension
- Subsequent releases (e.g., mixs6.1.0, v6.2.0) have introduced significant changes to technical implementation, but
  generally only minor changes to existing terms.

When referring to MIxS versions, it's best to use the specific release tags (e.g., mixs6.0.0, v6.2.0) rather than
general concepts like "v6".

What’s included in a release?  
**From a GitHub perspective**, the entire `GenomicsStandardsConsortium/mixs` GitHub repository is frozen at some point
in time as a release, and associated with a version tag. That includes the `mixs/schema/mixs.yaml` LinkML file, which
serves as the source of truth for MIxS. It also includes numerous configuration files, representations of MIxS in
formats other than YAML (like JSON schema and OWL), and code used to maintain the repository.

Since there wasn’t any LinkML YAML file before version mixs6.0.0, a community-reviewed, **all-encompassing XLSX
spreadsheet was designated as the “release file”** in those historical versions, and was shared with external
stakeholders. The v6 release file was lost with the release of 6.1 and have been re-added to the GitHub directory (
PATH). MIxS will continue to include tabular summaries in future releases. Since the content of these spreadsheets is
just a small subset of the current MIxS schemas, calling them “release files” is now misleading.

### [Versioning and Tracking Changes](#versioning-and-tracking-changes)

Anyone interested in contributing to or expanding their knowledge of MIxS is encouraged to engage with
the [MIxS community](#contributing-to-mixs). Changes to MIxS over time can be found by:

1. Referencing [GitHub releases and release notes](https://github.com/GenomicsStandardsConsortium/mixs/releases) for
   high-level summaries of changes.
2. Use GitHub's diff tools to compare specific files between versions, being aware of their limitations for complex
   changes.
    - Examining GitHub pull requests
3. Comparing .yaml files in the GitHub directory between versions
    - Comparing .xlsx files can be difficult, is manual, and visual comparison is error prone. For this reason, we do
      not suggest visually comparing .xlsx files. Rather, compare the .yaml files which can be used to generate .xslx
      files.

In addition to the multiple releases of MIxS provided by GSC, there are various implementations of MIxS within partner
systems, like the ENA and NCBI Biosample databases that participate in the International Sequence Database Collection.
The INSDC databases generally update their implantation after each **major** MIxS release by GSC, and changes from *
*minor** releases may not be reflected. As such, when using the MIxS standard, users are responsible to understand the
version they’re accessing and how it may differ from the most recent GSC release. GSC’s Technical Working Group is
working to develop more robust methods to detect differences between MIxS releases.

## [Key Changes](#key-changes)

MIxS has transitioned from using spreadsheets as the source of truth to using a [LinkML schema](#explanation), improving
computability and interoperability. The authoritative representation is now a LinkML YAML file, with efforts ongoing to
provide accessible, shareable formats alongside it. Some of the following changes can be seen in the mixs.yaml source
file while others can be found in the Makefile.

- Added a schema description
- Introduction of deprecation protocols
- Reintroduction
  of [Excel data collection templates](https://github.com/GenomicsStandardsConsortium/mixs/tree/main/mixs-templates)
- Creation of visual aids (
  e.g., [Extension distance dendrogram](https://github.com/GenomicsStandardsConsortium/mixs/blob/main/assets/extensions-dendrogram.png),
  based on use of similar terms)
- Enhanced documentation structure and search functionality, such as an
  isolated “[Full term table](https://genomicsstandardsconsortium.github.io/mixs/term\_list/)”
- Adoption of CamelCase for enumeration names
- Implementation of LinkML
- Comprehensive linting of YAML schema files

### [Evolution of MIxS Representation](#evolution-of-mixs-representation)

- Pre-v6: Spreadsheets were both the source of truth and shareable format.
- v6.0.0 to v6.1.1: LinkML YAML files became the source of truth, with spreadsheets as shareable formats.
- v6.2.0 and later: A single LinkML YAML file (src/mixs/schema/mixs.yaml) is the authoritative source of truth. XLSX
  summaries are provided as a supplement for those that don’t need to see the full expressiveness of the MIxS schema.

## [How to Use MIxS](#how-to-use-mixs)

### [Current Structure (v6.2.0 and later)](#current-structure)

- Source of Truth: src/mixs/schema/mixs.yaml
- Shareable Formats: Under development to complement the LinkML schema

### [Finding the Current MIxS Version](#finding-the-current-mixs-version)

1. Visit the [MIxS GitHub repository](https://github.com/GenomicsStandardsConsortium/mixs)
2. Check the latest release in the Releases section

Note: Visual comparison of spreadsheets, while sometimes used, is not a reliable method for comprehensive change
detection. See Versioning and Tracking Changes section above.

### [Contributing to MIxS](#contributing-to-mixs)

1. Raise an issue in the MIxS issue tracker. Please use the newest MIxS language found in this document, like
   Extension (not Environment or Package)
2. Make a branch of [MIxS repository](https://github.com/GenomicsStandardsConsortium/mixs)
3. Make your changes in a new branch
4. Submit a pull request with a clear description of your changes
5. Assign reviewers. Reviewers should include the individual that raised the original issue (if not the PR author) and
   TWG leads (Add GitHub tags, Pier, Montana, Mark).

Consider attending one of these meetings

* [GSC Technical Working Group (2024 Meeting Notes)](https://docs.google.com/document/d/1MG9JBj9m8Lnev7UBnPGpbQO9ReovswASGNouidjmfx4/edit\#heading=h.2989lvv9mqv5)
* [Compliance and Interoperability Group (CIG) Agenda and Actions](https://docs.google.com/document/d/19CWWf1oqMlyH7prteVC5k4eYF\_JzJbNqNcvGUyX\_U50/edit\#heading=h.mget0ilzdhks)

## [Understanding MIxS Structure](#understanding-mixs-structure)

The MIxS terms are assigned to Checklist and Extension classes:

1. Checklists: e.g., MIGS (Microbial Genome Sequence)
2. Extensions: e.g., Soil, Water, Host-associated

### [Key Terminology](#key-terminology)

- Checklist: A core set of terms applicable across environments
- Extension: Environment-specific terms that complement checklists
- Slot/Term: Individual fields in the schema (formerly "Structure comment name")
- Slot Title: Human-readable name for a slot (formerly "Package item")
- Description: Explanation of a term's meaning (formerly "Definition")
- Range: The type of data expected for a term (formerly "Expected value")
- Pattern: Regular expression defining valid values (formerly "Value syntax")

### [LinkML Schema Structure](#linkml-schema-structure)

- `mixs.yaml`: Main schema file
- Classes: Represent extensions and checklists
- Slots: Represent individual terms
- LinkML attributes: Properties of classes and slots (e.g., `required`, `range`, `pattern`)

### [Terminology Evolution and Current Status](#terminology-evolution-and-current-status)

1. Environmental Packages are now Environmental Extensions. Speaking strictly in terms of the MIxS v6.2.0+ LinkML model,
   “Combinations” refer to an Extension plus a Checklist. Partnering institutions may refer to any of these things as
   Packages, Models, etc.

2. Structured comment names can now be found in the `name` metaslot when viewing MIxS GitHub generated documentation. (
   See [abs\_air\_humidity](https://genomicsstandardsconsortium.github.io/mixs/0000122/\#linkml-source) example). The
   `name` metaslot can be inferred by the documentation generator, is **not** required in the source yaml, and is not
   asserted in the source mixs.yaml. You will not find the `name` metaslot in the source yaml (mix.yaml). New term
   requests should use lower snake case (e.g., samp\_name, host\_sex).

3. "Package item" or "Item (rdfs:label)" now appear as slot `title`s, These should be fully spelled out. Whitespace and
   most punctuation characters are allowed (e.g., "sample name", "host sex", “history/extreme events”, ).

4. Definitions now appear as LinkML `description`s. Note that descriptions should not include examples or valid
   structures, which are captured in other LinkML attributes.

5. Expected values are now generally reflected with the LinkML `range` attribute. While not an exact match, many
   previous expected values have intuitively similar LinkML `range`s (e.g., text and free text \= `string`). List-like
   Expected values now use the LinkML enumeration and permissible values system.

6. Value syntaxes are now generally reflected with the LinkML `structured_pattern` attribute, where the reusable
   elements of `structured_pattern`s are formally defined as LinkML `settings`. For example, `geo_loc_name` has
   `range: string`, and the `structured_pattern` `^{text}: {text}, {text}$`, which LinkML compiles to a regular
   expression of `^([^\s-]{1,2}|[^\s-]+.+[^\s-]+): ([^\s-]{1,2}|[^\s-]+.+[^\s-]+), ([^\s-]{1,2}|[^\s-]+.+[^\s-]+)$`,
   which is roughly intended to enforce the values in conceptual patterns like "Country: region, site".

7. Examples or example-like content from previous Descriptions appear as LinkML `example`s, which can also capture
   clarifying comments. It is the expectation that all provided `example.values` will validate against the provided
   `range` and `pattern` constraints.

8. Requirement values (C, E, M, X, \-) are now reflected with the LinkML `recommended` (X) and `required` (M)
   attributes. The Extension conditional value (E) is accounted for with the advanced LinkML `slot_usage` mechanism. The
   not applicable state (-) is no longer asserted. Slots that are not applicable to a class simply are not listed in
   that Class’s `slots` section, where the classes are the `Extension`s and `Checklist`s. The conditional Requirement
   value (C) has not yet been implemented in LinkML. Discussion of this continues
   in [GitHub issue \#468](https://github.com/GenomicsStandardsConsortium/mixs/issues/468).

9. Section values have preliminarily been expressed as LinkML `subsets`, but this approach is still under discussion
   in  [GitHub issue \#772](https://github.com/GenomicsStandardsConsortium/mixs/issues/772).

## [Explanation](#explanation)

### [Why LinkML?](#why-linkml)
[Practical Approach to Using the Genomic Standards Consortium MIxS Reporting Standard for Comparative Genomics and Metagenomics](https://link.springer.com/protocol/10.1007/978-1-0716-3838-5_20)
The transition to LinkML offers several advantages:

1. Improved interoperability with other data standards
2. Enhanced computability and validation capabilities
3. Better support for semantic web technologies
4. Easier integration with modern data management tools

### [Balancing Tradition and Innovation](#balancing-tradition-and-innovation)

While we've adopted LinkML as the authoritative representation, we recognize the familiarity and utility of spreadsheet
formats for many users. Our ongoing efforts include:

1. Developing tools to generate accessible formats from the LinkML schema
2. Providing comprehensive documentation to support users in transitioning to and understanding the LinkML-based
   standard
3. Maintaining a balance between technical advancement and user accessibility

## [Future Directions](#future-directions)

We are actively working on:

1. Developing robust difference detection methods for easier tracking of changes between versions
2. Improving our documentation to clearly distinguish between authoritative representations and derived, shareable
   formats
3. Expanding community engagement to ensure MIxS continues to meet the evolving needs of its users

For the most up-to-date information on MIxS development and to contribute to these efforts, please visit
our [GitHub repository](https://github.com/GenomicsStandardsConsortium/mixs).  
