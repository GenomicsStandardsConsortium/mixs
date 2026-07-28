# MIxS term specifications in the LinkML framework

> **Important**
> This specification governs **new and revised terms**. Existing terms are not
> retrofitted to it, and many predate it: a requirement here being unmet by a term
> already in MIxS is expected, not a defect to be fixed in bulk. Where a rule would
> change an existing term, that change goes through the normal proposal process.

| Metadata         | Value                                                                                                                                          |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Version          | 0.0.1                                                                                                                                          |
| Last updated     | 2026-07-27                                                                                                                                     |
| Document Authors | James Fellows Yates (@jfy133), Mark Miller (@turbomam), Chris Hunter (@only1chunts), Peter Woollard (@Woolly-at-EBI), Lynn Schriml (@lschriml) |

## Preamble

This document describes how MIxS metadata terms are represented within the LinkML framework of the MIxS schema.

### Terminology

The key words “MUST”, “MUST NOT”, “SHOULD”, etc. are to be interpreted as described in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119).

This specification documentation refers to both MIxS and LinkML terminology.
The following table can guide readers to how the terminology can be linked.

| MIxS                    | LinkML               | Description                                                                                                                                                                    |
| ----------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Term                    | `slot`               | A single field of information (metadata) that has various attributes on how this information should be represented and formatted                                               |
| Structured comment name | `name`               | A short and unique computer compatible key or name for a given metadata field that is used to refer to the particular term (typically) within the schema internally [^1]       |
| Item                    | `title`              | A short and unique human readable name for the metadata term/slot [^2]                                                                                                         |
| MIxS ID                 | `slot_uri`           | The resolvable globally unique persistent identifier associated with a MIxS metadata field with the prefix 'MIXS' that expands to https://w3id.org/gensc/mixs/                 |
| Definition              | `description`        | A detailed human-readable explanation describing the context of the metadata field.                                                                                            |
| Expected value          | `range`              | The category of metadata the metadata field will hold (text, numbers, etc.)                                                                                                    |
| Expected format         | `structured_pattern` | A way of defining how the metadata field should be filled in, e.g. with a specific format or structure                                                                         |
| Example                 | `examples`           | Examples of values for an item, i.e., different examples how metadata field could be filled in                                                                                 |
| Section                 | `slot_group`         | A way of grouping similar or related metadata fields together to assist users in filling metadata tables following a logical progression                                       |
| Section                 | `in_subset`          | Another way of grouping similar or related metadata fields together to assist users in filling metadata tables following a logical progression                                 |
| Requirement             | `recommended`        | Specifying that a metadata field is optional, but if the information is available, it is highly recommended to be filled in to increase the scientific usefulness of your data |
| Requirement             | `required`           | Specifying whether a metadata field is mandatory to be filled in for a sample                                                                                                  |
| Occurrence              | `multivalued`        | That a term can be recorded more than once for a single sample                                                                                                              |

[^1]: This structured name is used by many implementers as a key e.g. NCBI and DDBJ

[^2]: This title name is used by many implementers as a key e.g. ENA

This document generally uses MIxS terminology, giving the LinkML equivalent in parentheses where that is more helpful.

## 1. General

### 1.1 LinkML compatibility

A MIxS term MUST be written in and compatible with the [LinkML](https://linkml.io/) model, and any of its requirements (e.g. in YAML format).

It MUST conform to any MIxS specific LinkML linting requirements as defined within the [MIxS GitHub repository](https://github.com/GenomicsStandardsConsortium/mixs).

### 1.2 Slot definition

A LinkML slot is the object that is used to describe a MIxS term - i.e. information that is used to describe a particular aspect of a sample, its nucleic acids, or resulting sequence data.

### 1.3 Language

All MIxS term attributes SHOULD be written in English.

> **Note**
> Every term in the schema is currently in English, and nothing in the build
> checks this. Whether English is required has not been decided; if there is a
> community need for other languages, raise it with the CIG.

## 2. Term structured naming

### 2.1 (Structured comment) name format

The term structured comment name (`name`) MUST be in [snake_case](https://en.wikipedia.org/wiki/Snake_case).

All words MUST be lower case and underscores (`_`) MUST be used to separate words in the term name.

### 2.2 (Structured comment) name length

The term structured comment name (`name`) MUST be a maximum of 20 characters in length.

The figure comes from the [INSDC feature table, section 3.1](https://www.insdc.org/submitting-standards/feature-table/#3.1): "Component names may be no more than 20 characters long (Feature keys 15, Feature qualifiers 20)". That sentence constrains feature keys and feature qualifiers rather than structured comment keys, so MIxS is holding itself to the same figure by convention rather than because INSDC requires it of these names.

### 2.3 (Structured comment) name uniqueness

The term structured comment name (`name`) MUST be unique within MIxS and the MIxS LinkML model.

### 2.4 (Structured comment) name descriptiveness

The term structured comment name (`name`) MUST be descriptive of the data it is intended to represent.

The term structured comment name (`name`) SHOULD NOT include a checklist or extension specific prefix (e.g. `mimarks_`, `soil_`), to ensure re-use across different checklists and extensions.

### 2.5 (Structured comment) name abbreviations

The term structured comment name (`name`) SHOULD be an abbreviated form of the item (title) attribute.

Examples:

| Term Item / `title`                             | Structured comment name / `name` |
| ----------------------------------------------- | -------------------------------- |
| geographic location (country and/or sea,region) | `geo_loc_name`                   |
| isolation and growth condition                  | `isol_growth_condt`              |
| pcr conditions                                  | `pcr_cond`                       |
| sample volume or weight for DNA extraction      | `samp_vol_we_dna_ext`            |
| collection site geographic feature              | `coll_site_geo_feat`             |

### 2.6 (Structured comment) name abbreviations should be reused

The term structured comment name (`name`) SHOULD reuse commonly used abbreviations when using the same word.

Examples:

| Word        | Abbreviation | Structured comment name / `name` |
| ----------- | ------------ | -------------------------------- |
| `culture`   | `cult_`      | `cult_isol_date`                 |
| `culture`   | `cult_`      | `cult_result`                    |
| `culture`   | `cult_`      | `cult_result_org`                |
| `culture`   | `cult_`      | `cult_root_med`                  |
| `dissolved` | `diss_`      | `diss_carb_dioxide`              |
| `dissolved` | `diss_`      | `diss_hydrogen`                  |
| `dissolved` | `diss_`      | `diss_inorg_carb`                |
| `dissolved` | `diss_`      | `diss_inorg_nitro`               |

### 2.7 (Structured comment) name common prefix of related terms

When related to existing terms, the term structured comment name (`name`) SHOULD use a common prefix that allow grouping of related terms.

Examples:

- Terms related to `sample` should use the prefix `samp_`.

  | Term Item / `title`              | Structured comment name / `name` |
  | -------------------------------- | -------------------------------- |
  | sample storage temperature       | `samp_store_temp`                |
  | sample storage duration          | `samp_store_dur`                 |
  | sample volume or weight for DNA extraction | `samp_vol_we_dna_ext`  |

- Terms related to assembly metadata terms should use the prefix `assembly_`.

  | Term Item / `title`          | Structured comment name / `name` |
  | ---------------------------- | -------------------------------- |
  | assembly name                | `assembly_name`                  |
  | assembly software            | `assembly_software`              |
  | assembly quality             | `assembly_qual`                  |

## 3. Term expected value types

### 3.1 Term expected value must be valid LinkML range types

The type of data specified in the expected value (`range`) of a term MUST be in the form of a valid LinkML `range` type:

- `string`
- `integer`
- `float`
- `boolean`
- An [enumeration](#125-enumerations), that is a controlled vocabulary, predefined by MIxS (see top of the [schema](https://github.com/GenomicsStandardsConsortium/mixs/blob/main/src/mixs/schema/mixs.yaml#L36)).

Refer to LinkML documentation for more information on [range types](https://linkml.io/linkml-model/latest/docs/range/).

## 4. Attributes for MIxS terms

### 4.1. Minimal required MIxS term (LinkML slot) attributes

A term MUST at a minimum include the following attributes:

- [`name`](https://linkml.io/linkml-model/latest/docs/name/) (MIxS: Structured comment name).
- [`description`](https://linkml.io/linkml/schemas/metadata.html#providing-descriptions) (MIxS: Definition).
- [`title`](https://linkml.io/linkml-model/latest/docs/title/) (MIxS: Item).
- [`examples`](https://linkml.io/linkml-model/latest/docs/examples/) (MIxS: Example).
- [`in_subset`](https://linkml.io/linkml-model/latest/docs/in_subset/) (MIxS: Section).
- [`slot_uri`](https://linkml.io/linkml-model/latest/docs/slot_uri/) (MIxS: MIxS ID).
- [`range`](https://linkml.io/linkml/schemas/slots.html#ranges) (MIxS: Expected value).

### 4.2. Recommended LinkML slot attributes

A term that is mandatory for a sample sets [`required`](https://linkml.io/linkml/schemas/slots.html#required), and a term that is worth filling in when the information exists sets [`recommended`](https://linkml.io/linkml/schemas/slots.html#recommended). Both are MIxS Requirement.

Conditional, environment dependent and optional terms do not set either attribute on the term itself. See section [11](#11-level-of-requirement).

## 5. Term definition

### 5.1 Definition contents

The definition (description) SHOULD aim to be precise enough for a user to understand the data the term is intended to hold, how it should be filled, and used.

Links to external resources MUST NOT be written into the definition (description). A link that asserts the term is equivalent or related to a term in another vocabulary belongs in a mapping attribute (`exact_mappings`, `close_mappings`, `related_mappings`, `narrow_mappings`, `broad_mappings`). Any other link, such as a definition source or background reading, belongs in [`see_also`](https://linkml.io/linkml-model/latest/docs/see_also/).

### 5.2 Definition length

The definition (description) MUST be at a minimum 1 sentence long that is longer than the term title.

The definition (description) MAY be multiple sentences long, but should be as concise as possible to ensure readability.

### 5.3 Definition examples

The definition (description) SHOULD NOT include basic examples of the data the term is intended to hold (this is covered by the `examples` attribute).

The definition (description) MAY include examples when the information for the term requires different formatting depending on certain conditions. The definition (description) MAY also include examples when it requires additional understanding that cannot be inferred by looking purely at the `examples` section.

### 5.4 Definition external resources

An external resource MUST be valid and generally accessible over the public web, and SHOULD be a stable and established resource rather than a personal site or one that is not widely used.

Put it in a mapping attribute if it asserts a relationship to a term in another vocabulary, and in [`see_also`](https://linkml.io/linkml-model/latest/docs/see_also/) otherwise. Keeping links out of the prose means a consumer reading the definition gets the definition, and a consumer that wants the reference can find it in a field it can parse.

## 6. Term item title attribute

### 6.1 Title contents

The item (title) SHOULD be the term name written out in full words, and MUST be descriptive of the data it is intended to hold.

### 6.2 Title length

A term item (title) attribute SHOULD be as short as possible, but as long as necessary to be sufficiently descriptive, unique, and distinguishable from other terms.

### 6.3 Title format

The item (title) SHOULD be in most circumstances lower case, including first character of the item.

- Valid example: `library size`.
- Invalid examples:
  - `Library size` (capitalisation of first character).
  - `Library Size` (capitalisation of all words).

Capitalisation MAY be used when it is an acronym or abbreviation that typically uses capitalisation in the English language (e.g. `DNA`, `API`, `pH`).

- Valid example: `MAG coverage software`.
- Valid example: `API gravity`.

### 6.4 Title uniqueness

The term item (title) MUST be unique within the MIxS standard (LinkML model).

## 7. Term examples attribute

### 7.1 Minimum number of examples

There MUST be a minimum of 1 example for a term.
Ideally, there SHOULD be a minimum of 3 examples for a term.

### 7.2 Scope of examples

Examples SHOULD cover the full range of possible values, string formats, or any other way that information can be given to the term.

For example if a term accepts either an [ontology](#12-ontology-and-value-sets) term _or_ a free text string, there should be at least one example for each type.
If a term accepts different unit types, there should be at least two examples of different units to demonstrate multiple units are accepted.

### 7.3 Examples for terms that allow more than one entry

If a term allows multiple occurrences ('multivalued'), the examples MUST include at a minimum two examples, one to show inputting a single value, and another to show how to fill the term with multiple values.

## 8. Term section attribute

> **Note**
> What a section means, and which sections exist, is still under discussion in
> [Define "in_subset"](https://github.com/GenomicsStandardsConsortium/mixs/issues/931).

A section is recorded with the term's `in_subset` attribute, which refers to a subset defined under the schema's top-level `subsets:` block. There is no `subset` attribute on a term.

### 8.1 All checklist terms must be assigned a section

All terms defined in a checklist MUST name a section in `in_subset`.

### 8.2 All extension terms must be assigned the environment section

A term defined in an extension, rather than in a core checklist, MUST include the Environment section in `in_subset`.

## 9. Term MIxS ID attribute

### 9.1 MIxS ID requirement

The term MUST have a MIxS ID (slot_uri) that is unique within the MIxS ID space.

### 9.2 MIxS ID format

The MIxS ID (`slot_uri`) MUST begin with the string `MIXS`, followed by a colon, followed by a 7 digit number.

Example: `MIXS:0000010`.

> **Note**
> MIxS IDs are only able to be assigned by the GSC's Compliance and Integration Working Group (CIG).

## 10. Slot range attribute

### 10.1 Range options should be valid LinkML types

See section [3](#3-term-expected-value-types).

### 10.2 Structured or formatted text should use a structured pattern

A term that requires a specific format or a structured string layout MUST use the `structured_pattern` attribute, with the pattern components predefined in the schema's `settings:` block where a component could be used more than once.

New terms MUST NOT use `string_serialization`. It appears on terms that predate this guidance, it is not checked by any validator, and it is being retired.


### 10.3 Structured or formatted text components should be reused

A structured pattern SHOULD re-use existing pattern components as far as possible.

Additional pattern components MAY be created when needed after consultation with the GSC's Compliance and Integration Working Group (CIG).

### 10.4 Specifying units

Terms that record a measurement SHOULD use a [structured pattern](#102-structured-or-formatted-text-should-use-a-structured-pattern) that includes a component for the unit of measurement.

Example:

```yaml
structured_pattern:
  syntax: ^{particulate_matter_name};{float} {unit}$
```

### 10.5 Preferred units

Terms that record a measurement SHOULD specify the preferred unit of measurement in the `Preferred_unit` annotation.

`Preferred_unit` is the only annotation a new term should use. Many existing terms also carry `Expected_value`; those stay as they are, but new terms do not add it. Anything else a term needs to say belongs in a LinkML attribute, not in `annotations:`, which no validator checks and no generator reads.

Example:

```yaml
annotations:
  Preferred_unit: degree Celsius
```

## 11. Level of requirement

### 11.1 Mandatory terms

A term that is required to be filled in for a sample MUST have the `required` attribute set to `true`.

### 11.2 Conditional mandatory terms

A conditional term SHOULD NOT be specified as `required` as a LinkML slot attribute.

A conditional term SHOULD be specified within the `slot_usage` attribute of a LinkML class attribute for a given extension.

### 11.3 Environment dependent terms

An environment dependent term SHOULD NOT be specified as `required` as a LinkML slot attribute.

An environment dependent term SHOULD be specified within the `slot_usage` attribute of a LinkML class attribute for a given extension.

### 11.4 Optional terms

A term that is not required for a given sample MUST NOT have either the `recommended` or the `required` LinkML attribute specified.
By default LinkML attributes are assumed `false` unless specified.

## 12. Ontology and Value sets

### 12.1 Ontology and controlled values recommended

Where possible, terms (slots) with controlled vocabularies SHOULD use standardised terms from ontologies.
When not possible, controlled vocabulary terms (value sets) MAY be used to specify the value of the term.

### 12.2 Recommended ontologies

Ontologies SHOULD be from established and widely used ontologies, such as those found in the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols4/), [Open Biological and Biomedical Ontology Foundry (OBO)](https://obofoundry.org/), or [BioPortal](https://bioportal.bioontology.org/).

Common ontologies used in MIxS include:

- [Environment Ontology (ENVO)](https://sites.google.com/site/environmentontology/)
- [Uberon anatomy ontology (UBERON)](https://obophenotype.github.io/uberon/)
- [Disease Ontology (DOID)](https://disease-ontology.org/)
- [Ontology for Biomedical Investigations (OBI)](https://obi-ontology.org/)
- [Experimental Factor Ontology (EFO)](https://www.ebi.ac.uk/efo/)
- [Phenotypic Quality Ontology (PATO)](https://pato-ontology.github.io/pato/)
- [Plant Ontology (PO)](https://browser.planteome.org/amigo)

### 12.3 Ontology term value format

A term using an ontology term value MUST be written in the `termLabel [termID]` syntax, where the label is followed by the identifier code in square brackets.

Example of ontology terms:

- `Tundra biome [ENVO:01000180]`
- `Rumen [UBERON:0007365]`
- `Rabies [DOID:11260]`
- `454 Genome Sequencer FLX [OBI:0000702]`

### 12.4 Value sets

For a term that allows only a small fixed set of values, and for which no suitable standardised ontology exists, an enumeration SHOULD be used to define the allowed values.

The set of allowed values is defined in the `enums:` section of the schema, as described in 12.5.

### 12.5 Enumerations

Value sets (enumerations) MUST be defined within the `enums:` section of the LinkML schema.

The name of the enumeration MUST be formatted in [Pascal Case](https://en.wikipedia.org/wiki/Camel_case), i.e. each word is capitalised and no spaces or underscores are used.

For example, the value set for the term `assembly_qual` is named `AssemblyQualEnum`.

## 13. Mapping terms to other standards

### 13.1 Align with an existing term where one exists

Where an established standard already has a term with the same purpose and meaning as a proposed MIxS term, the MIxS term SHOULD align with it rather than define the concept differently.

Examples of established standards include:

- [Darwin Core (DwC)](https://dwc.tdwg.org/)

### 13.2 Record the correspondence as a mapping

A MIxS term that corresponds to a term in another standard SHOULD record that correspondence using the appropriate LinkML [mapping](https://linkml.io/linkml-model/latest/docs/mappings/) attribute (`exact_mappings`, `close_mappings`, `related_mappings`, `narrow_mappings`, `broad_mappings`), naming the other term by its CURIE ([Compact URI](https://en.wikipedia.org/wiki/CURIE)).

MIxS has no mechanism for importing a term definition from another standard. The MIxS term is defined in MIxS; the mapping records what it corresponds to.

### 13.3 The MIxS name follows MIxS conventions

The structured comment (name) of a MIxS term MUST follow the [MIxS naming conventions](#2-term-structured-naming), including [snake_case](https://en.wikipedia.org/wiki/Snake_case), regardless of how the corresponding term is named in the other standard.

## References

- [https://www.gensc.org/pages/standards-intro.html#term](https://www.gensc.org/pages/standards-intro.html#term)
- Eloe-Fadrosh, E.A., Mungall, C.J., Miller, M.A., Smith, M., Patil, S.S., Kelliher, J.M., Johnson, L.Y.D., Rodriguez, F.E., Chain, P.S.G., Hu, B., Thornton, M.B., McCue, L.A., McHardy, A.C., Harris, N.L., Reddy, T.B.K., Mukherjee, S., Hunter, C.I., Walls, R., Schriml, L.M., 2024. A practical approach to using the Genomic Standards Consortium MIxS reporting standard for comparative genomics and metagenomics. Methods Mol. Biol. 2802, 587–609. [https://doi.org/10.1007/978-1-0716-3838-5_20](https://doi.org/10.1007/978-1-0716-3838-5_20)
- [https://linkml.io/linkml/](https://linkml.io/linkml/)
