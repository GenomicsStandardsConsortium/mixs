# MIxS LinkML Schema Quickstart

This page aims to help to quickly orient newcomers (or refamiliarise returners) to the MIxS LinkML schema file, without needing to do a deep dive into the official [LinkmL documentation](https://linkml.io/linkml/).
The descriptions here are written in a way to be practical and specific to the MIxS schema, and may not fully represent how LinkML theoretically should work.

## MIxS Schema

The LinkML schema for the MIxS metadata standards can be found on this [GitHub repository](https://github.com/GenomicsStandardsConsortium/mixs) under [`src/mixs/schema/mixs.yaml`](https://github.com/GenomicsStandardsConsortium/mixs/blob/main/src/mixs/schema/mixs.yaml).
This `.yaml` file includes the information about all MIxS metadata terms, checklists, and extensions (including internal fixed-list enumerations) and how each object are defined.
This `.yaml` file is the 'ground truth' source, from which all other formats of the schema are generated from. 


### Schema Section Overview

The schema is currently (as of Jan 2025) a very large file of more than 20,000 lines, making it somewhat difficult to explore when trying to gain understanding of how LinkmL works.

The following table provides a description of each top-level element of the `.yaml` file:

| Element | Description | Can you modify\* |
|---------|--------------|-------------------|
| `name:` | name of the overall schema itself | No |
| `description:` | short description of what the schema is for | No |
| `comments:` | additional general information about the schema (e.g. like code comments) | No |
| `source:` | original source of the information encoded in schema (e.g. URL) | No |
| `id:` | A w3id linked-data URL | No |
| `version:` | version of the schema | No |
| `imports:` | specifications of internal linkml packages/modules used | No |
| `prefixes:` | additional URL prefixes for call out different things within the schema where prefix + object makes a full URL | No |
| `default_prefix`: | default prefix to append to each 'slot' (term) ID | No |
| `default_range`: | default slot (term) object type (e.g., integer, string)  | No |
| `subsets`: | section or term group category definitions | No |
| `enums`: | definitions of drop down menu/fixed lists used by metadata term slots  | Yes |
| `slots`: | definition of each MIxS metadata term; basic summary information of each MIxS checklist and extension | Yes |
| `classes`: | definition of the contents of each checklists, extensions, combinations (e.g., which metadata term slot is included)  | Yes |
| `settings`: | definitions of regex patterns etc. (a bit like variables) that are then be used inside `string_serialisation:` attribute of a slot | No |

\* where 'you' refers to someone contributing to a occasional contributor of metadata terms, rather than a schema developer.

### Gold MIxS Standard Metadata Slot

A gold standard MIxS metadata slot within the LinkML schema should have the following attributes:

TODO

### Exploring the Schema

The GSC MIxS schema is designed to closely match LinkML standards.
Therefore you can use the `linkml` tooling that can be installed following the instructions [here](https://linkml.io/linkml/intro/install.html).

If using the command-line tool, useful commands when a schema are:

- `linkml validate --schema src/mixs/schema/mixs.yaml` which can tell you what sort of things are best-practises when it comes to LinkML.

You can also explore more interactively through the MIxS documentation webpage [here](https://genomicsstandardsconsortium.github.io/mixs/).

