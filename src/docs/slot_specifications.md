# MIxS term specifications in the LinkML framework

| Metadata         | Value                                                                               |
| ---------------- | ----------------------------------------------------------------------------------- |
| Version          | 0.0.1                                                                               |
| Last updated     | 2025-05-05                                                                          |
| Document Authors | James Fellows Yates (@jfy133), Mark Miller (@turbomam), Chris Hunter (@only1chunts) |

## Preamble

This document describes how MIxS metadata terms are represented within the LinkML framework of the MIxS schema.

### Terminology

The key words “MUST”, “MUST NOT”, “SHOULD”, etc. are to be interpreted as described in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119).

This specification documentation refers to both MIxS and LinkML terminology.
The following table can guide readers to how the terminology can be linked.

| MIxS                    | LinkML               | Description                                                                                                                                                    |
| ----------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Term                    | `slot`               | A single field of information (metadata) that has various attributes on how this information should be represented and formatted                               |
| Structured comment name | `name`               | A short computer compatible key or ID for a given metadata field that is used to refer to the particular term (typically) within the schema internally         |
| Item                    | `title`              | A short human readable name for the metadata term/slot                                                                                                         |
| MIxS ID                 | `slot_uri`           | The resolvable globally unique persistent identifier associated with a MIxS metadata field with the prefix 'MIXS' that expands to https://w3id.org/gensc/mixs/ |
| Definition              | `description`        | A detailed human-readable explanation of what information the metadata field should be holding                                                                 |
| Expected value          | `range`              | The category of metadata the metadata field will hold (text, numbers, etc.)                                                                                    |
| Value syntax            | `structured_pattern` | A way of defining how the metadata field should be filled in, e.g. with a specific format or structure                                                         |
| Example                 | `examples`           | Examples of values for an item, i.e., different examples how metadata field should be filled in                                                                |
| Section                 | `slot_group`         | A way of grouping similar or related metadata fields together to assist users in filling metadata tables following a logical progression                       |
| Section                 | `subset`             | Another way of grouping similar or related metadata fields together to assist users in filling metadata tables following a logical progression                 |
| Requirement             | `recommended`        | Specifying the whether a metadata field is optional but should be to be filled in for a sample                                                                 |
| Requirement             | `required`           | Specifying the whether a metadata field is mandatory to be filled in for a sample                                                                              |
| Occurrence              | `multivalued`        | The number of times a particular metadata field can be used for a specific sample                                                                              |

This document will generally use MIxS terminology, but where helpful more relevant use the LinkML equivalent, with the other form in parentheses afterwards.

## 1. General

### 1.1 LinkML compatibility

A MIxS term (slot) MUST be written in and compatible with the [LinkML](https://linkml.io/) model, and any of it's requirements (e.g. in YAML format).

It MUST conform to any MIxS specific LinkML linting requirements as defined within the [MIxS GitHub repository](https://github.com/GenomicsStandardsConsortium/mixs).

### 1.2 Slot definition

A LinkML slot is the object that is used to describe a MIxS term - i.e. information that is used to describe a particular aspect of a sample, nucleic acid,, or sequence data.

### 1.3 Language

All MIxS terms attributes MUST be written in English.

<!-- JFY comment: may be being a bit strict here, I guess you could have 'translated name' column or something like that, should rephrase to allow those exceptions -->

## 2. Term structured naming

### 2.1 (Structured comment) name format

The term (slot) structured comment name (`name`) MUST be in [snake_case](https://en.wikipedia.org/wiki/Snake_case).

All words must be lower case and underscores (`_`) MUST be used to separate words in the slot name.

### 2.2 (Structured comment) name length

The term (slot) structured comment name (`name`) must be a maximum of 20 characters in length as per INSDC guidelines ([https://www.insdc.org/submitting-standards/feature-table/#3.1](https://www.insdc.org/submitting-standards/feature-table/#3.1)).

### 2.3 (Structured comment) name uniqueness

The term (slot) structured comment name (`name`) MUST be unique within the MIxS LinkML model.

### 2.4 (Structured comment) name descriptiveness

The term (slot) structured comment name (`name`) MUST be descriptive of the data it is intended to hold.

The term (slot) structured comment name (`name`) SHOULD NOT include a checklist or extension specific prefix (e.g. `mimarks_`, `humanskin_`), to ensure re-use across different checklists and extensions.

### 2.5 (Structured comment) name abbreviation

The term (slot) structured comment name (`name`) SHOULD be a abbreviated form of the item (title) attribute.

Examples:

| Term Item / `title`                             | Structured comment name / `name` |
| ----------------------------------------------- | -------------------------------- |
| geographic location (country and/or sea,region) | `geo_loc_name`                   |
| isolation and growth condition                  | `isol_growth_condt`              |
| pcr conditions                                  | `pcr_cond`                       |
| sample volume or weight for DNA extraction      | `samp_vol_we_dna_ext`            |
| collection site geographic feature              | `coll_site_geo_feat`             |

### 2.6 (Structured comment) name common prefix

When related to existing terms, the term (slot) structured comment name (`name`) SHOULD use a common prefix that allow grouping of related terms.

Examples:

- Terms related to `sample` should use the prefix `samp_`.

  | Term Item / `title`              | Structured comment name / `name` |
  | -------------------------------- | -------------------------------- |
  | sample storage temperature       | `samp_store_temp`                |
  | sample storage duration          | `samp_store_dur`                 |
  | sample volume for DNA extraction | `samp_vol_we_dna_ext`            |

- Terms related to assembly metadata term (slots) should use the prefix `assembly_`.

  | Term Item / `title`          | Structured comment name / `name` |
  | ---------------------------- | -------------------------------- |
  | name and version of assembly | `assembly_name`                  |
  | assembly software            | `assembly_software`              |
  | assembly quality             | `assembly_qual`                  |

## 3. Term expected value types

### 3.1 Term expected value must be valid LinkML range types

The type of data specified in the expected value (`range`) of a slot (term) MUST be in the form of a valid LinkML `range` type:

- `string`
- `integer`
- `float`
- `boolean`
- A MIxS defined value set ([enumeration](#143-enumerations))

Refer to LinkML documentation for more information on [range types](https://linkml.io/linkml-model/latest/docs/range/).

## 4. LinkML slot attributes for MIxS terms

### 4.1. Minimal required LinkML slot attributes

A term MUST at a minimum include following LinkML slot attributes:

- [`name`](https://linkml.io/linkml-model/latest/docs/name/) (MIxS: Structured comment name).
- [`description`](https://linkml.io/linkml/schemas/metadata.html#providing-descriptions) (MIxS: Definition).
- [`title`](https://linkml.io/linkml-model/latest/docs/title/) (MIxS: Item).
- [`examples`](https://linkml.io/linkml-model/latest/docs/examples/) (MIxS: Example).
- [`in_subset`](https://linkml.io/linkml-model/latest/docs/in_subset/) (MIxS: Section).
- [`slot_uri`](https://linkml.io/linkml-model/latest/docs/slot_uri/) (MIxS: MIxS ID).
- [`range`](https://linkml.io/linkml/schemas/slots.html#ranges) (MIxS: Expected value).

### 4.2. Recommended LinkML slot attributes

A term (slot) that has some level of 'requirement' (mandatory, conditional mandatory, optional) SHOULD include the following LinkML attributes:

- [`recommended`](https://linkml.io/linkml/schemas/slots.html#recommended) (MIxS: Requirement).
- [`required`](https://linkml.io/linkml/schemas/slots.html#required) (MIxS: Requirement).

## 5. Term definition

### 5.1 Definition contents

The definition (description) SHOULD aim to be precise enough for a user to understand the data the term (slot) is intended to hold, how it should be filled, and used.

Links to external resources (e.g. ontologies, databases, or other documentation) SHOULD be included in the definition (description) when relevant.

### 5.2 Definition length

The definition (description) MUST be at a minimum 1 sentence long that is longer than the term (slot) title.

The definition (description) MAY be multiple sentences long, but should be as concise as possible to ensure readability.

### 5.3 Definition examples

The definition (description) SHOULD NOT include basic examples of the data the term (slot) is intended to hold (this is covered by the `examples` attribute).

The definition (description) MAY include examples when the information for the term (slot) requires different formatting depending on certain conditions. The definition (description) MAY also include examples when it requires additional understanding that cannot be inferred by looking purely at the `examples` section.

### 5.4 Definition external resources

Links or URLs used in the definition (description) to point a reader to an external resource MUST be valid and generally accessible via the public world wide web.

External resources SHOULD only be referred to when from a stable and established resource (i.e., not a personal or website, or a resource that is not widely used).

URLs in external resources specified within descriptions SHOULD also be defined within a LinkML [`see_also` slot attribute](https://linkml.io/linkml-model/latest/docs/see_also/).

## 6. Term item title attribute

### 6.1 Title contents

The item (title) should be a full sentence version of the term (slot) name, and MUST be descriptive of the data it is intended to hold.

### 6.2 Title length

A term (slot) item (title) attribute SHOULD be as short as possible, but as long as necessary to be sufficiently descriptive, unique, and distinguishable from other terms.

### 6.3 Title format

The item (title) SHOULD be lower case, including first character of the item.

- Valid example: `library size`.
- Invalid examples:
  - `Library size` (capitalisation of first character).
  - `Library Size` (capitalisation of of all words).

Capitalisation MAY be used when it is an acronym or abbreviation that typically used capitalisation in the English language (e.g. `DNA`, `API`, `pH`).

- Valid example: `MAG coverage software`.
- Valid example: `API gravity`.

## 7. Term examples attribute

<!-- JFY comment: this is a new guideline I would like to propose, so requires discussion  -->

### 7.1 Minimum number of examples

There MUST have minimum of 1 examples for a term (slot).
Ideally, there SHOULD be a minimum of 3 examples for a term (slot).

### 7.2 Scope of examples

Examples SHOULD cover the full range of possible values, string formats, or any other way that information can be given to the term (slot).

For example if a term (slot) accepts either an [ontology](#14-ontology-and-value-sets) term _or_ a free text string, there should be at least one example for each type.
If a term (slot) accepts different unit types, there should be at least two examples of different units to demonstrate multiple units are accepted.

### 7.3 Examples for terms that allow more than one entry

If a term (slot) allows multiple occurrences ('multivalued'), the examples MUST include at a minimum two examples, one to show inputting a single value, and another to show how to fill the term with multiple values.

## 8. Term section attribute

> [!WARNING]
> The guidance in this section regarding `subset`s may be replaced with the use of `slot-group` in the future.

### 8.1 All core terms must be assigned a subset

All core checklist terms (slot) MUST be assigned to a section (subset).

### 8.2 All extension terms must be assigned the environment subset

A term (slot) defined in an extension (rather than a core checklist term) MUST be assigned to the 'Environment' section (subset).

## 9. Term keywords attribute

### 9.1 Number of keywords

All term (slots) MUST have at least one keyword.

### 9.2 Keywords should be re-used

Re-using existing keywords SHOULD be preferred, but new keywords MAY be created if needed.

### 9.3 Keyword types

Keywords SHOULD be descriptive of the data the term is intended to hold in a way it can be grouped with with other terms (slots).

This can correspond to stage of project, domain of research, or the sample type (or extension) the term is intended to be used with.

It MAY ALSO include each descriptive part of the title (item) in full words (e.g. `air_temp` could have keywords `air` and `temperature`).

## 10. Term MIxS ID attribute

### 10.1 MIxS ID requirement

The term MUST have a MIxS ID (slot_uri) that is unique within the MIxS model.

### 10.2 MIxS ID format

The MIxS ID (slot_uri) must begin with the string `MIXS`, a colon, and followed by a 7 digit number.

Example: `MIXS:0000010`.

> [!NOTE]
> MIxS IDs are only able to be assigned by the GSC's Compliance and Integration Working Group (CIG).

## 11. Slot range attribute

### 11.1 Range options should be valid LinkML types

See section [4](#4-data-types).

### 11.2 Structured or formatted text should use a structured pattern

A term that requires a specific value syntax or a structured string layout SHOULD use the `structured_pattern` slot attribute, where the pattern components SHOULD be predefined in the `settings:` section of the schema when theoretically could be used more than once.

A slot MAY use `pattern:` attribute when XYZ <!-- TODO -->.

### 11.3 Structured or formatted text components should be reused

A structured pattern SHOULD re-use existing pattern components when as far as possible.

Additional pattern components MAY be created when needed after consultation with the GSC's Compliance and Integration Working Group (CIG).

### 11.4 Specifying units

Term (slots) that record a measurement SHOULD use a [structured pattern](#112-structured-or-formatted-text-should-use-a-structured-pattern) that includes a component for the unit of measurement.

Example:

```yaml
structured_pattern:
  syntax: ^{particulate_matter_name};{float} {unit}$
```

### 11.4 Preferred units

Terms (slots) that record a measurement SHOULD specify the preferred unit of measurement for the term (slot) within a LinkmL `annotation` slot sub-attribute called `Preferred_unit:`.

Example:

```yaml
annotations:
  Preferred_unit: degree Celsius
```

## 12. Multiple occurrence

A term (slot) that allows multiple values for a single sample SHOULD be specified by setting the LinkML `multivalued` boolean to `true`.

## 13. Level of requirement

### 13.1 Mandatory terms

A term (slot) that is required to be filled in for a sample MUST have the `required` attribute set to `true`.

### 13.2 Conditional mandatory terms

A conditional term (slot) SHOULD NOT be specified as `required` as a LinkML slot attribute.

A conditional term (slot) SHOULD be specified within the `slot_usage` attribute of a LinkML class attribute for a given extension.

### 13.3 Environment dependent terms

An environment dependent term (slot) SHOULD NOT be specified as `required` as a LinkML slot attribute.

An environment dependent term (slot) SHOULD be specified within the `slot_usage` attribute of a LinkML class attribute for a given extension.

### 13.4 Optional terms

A term (slot) that is not required for a given sample MUST NOT have either the `recommended` and `required` LinkML attributes specified.
By default LinkML attributes are assumed `false` unless specified.

## 14. Ontology and Value sets

### 14.1 Ontology and controlled values recommended

Where possible, terms (slots) with controlled vocabularies SHOULD use standardised ontology terms or controlled vocabulary terms to specify the value of the term (slot).

### 14.2 Recommended ontologies

Ontologies SHOULD be from established and widely used ontologies, such as those found in the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols4/), [Open Biological and Biomedical Ontology Foundry (OBO)](https://obofoundry.org/), or [BioPortal](https://bioportal.bioontology.org/).

Common ontologies used in MIxS include:

- [Environment Ontology (ENVO)](https://sites.google.com/site/environmentontology/)
- [Uberon anatomy ontology (UBERON)](https://obophenotype.github.io/uberon/)
- [Disease Ontology (DOID)](https://disease-ontology.org/)
- [Ontology for Biomedical Investigations (OBI)](https://obi-ontology.org/)
- [Experimental Factor Ontology (EFO)](https://www.ebi.ac.uk/efo/)
- [Phenotypic Quality Ontology (PATO)](https://pato-ontology.github.io/pato/)
- [Plant Ontology (PO)](https://browser.planteome.org/amigo)

### 14.3 Ontology term value format

A term (slot) using an ontology term value MUST be written in the `termLabel [termID]` syntax, where the label is followed by the identifier code in square brackets.

Example of ontology terms:

- `Tundra biome [ENVO:01000180]`
- `Rumen [UBERON:0007365]`
- `Rabies [DOID:11260]`
- `454 Genome Sequencer FLX [OBI:0000702]`

### 14.4 Value sets

For terms (slots) that only allow a small number fixed set of values, and otherwise no standardised ontology exists, an enumeration SHOULD be used be used to define the allowed values.

The set of allowed values

### 14.5 Enumerations

Value sets (enumerations) MUST be defined within the `enums:` section of the LinkML schema.

The name of the enumeration MUST be formatted in [Pascal Case](https://en.wikipedia.org/wiki/Camel_case), i.e. each word is capitalised and no spaces or underscores are used.

For example, the value set for the term (slot) `assembly_qual` is named `AssemblyQualEnum`.

## 15. Interoperability with other standards

### 15.1 Importing of existing terms in other standards

<!-- TODO  need decision from GSC-->

## References

- [https://www.gensc.org/pages/standards-intro.html#term](https://www.gensc.org/pages/standards-intro.html#term)
- Eloe-Fadrosh, E.A., Mungall, C.J., Miller, M.A., Smith, M., Patil, S.S., Kelliher, J.M., Johnson, L.Y.D., Rodriguez, F.E., Chain, P.S.G., Hu, B., Thornton, M.B., McCue, L.A., McHardy, A.C., Harris, N.L., Reddy, T.B.K., Mukherjee, S., Hunter, C.I., Walls, R., Schriml, L.M., 2024. A practical approach to using the Genomic Standards Consortium MIxS reporting standard for comparative genomics and metagenomics. Methods Mol. Biol. 2802, 587–609. [https://doi.org/10.1007/978-1-0716-3838-5_20](https://doi.org/10.1007/978-1-0716-3838-5_20)
- [https://linkml.io/linkml/](https://linkml.io/linkml/)
