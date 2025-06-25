# MIxS term specifications in the LinkML framework

| Metadata     | Value                         |
| ------------ | ----------------------------- |
| Version      | 0.0.1                         |
| Last updated | 2025-05-05                    |
| Authors      | James Fellows Yates (@jfy133) |

## Preamble

This document describes how MIxS metadata terms are represented within the LinkML framework of the MIxS schema.

### Terminology

The key words “MUST”, “MUST NOT”, “SHOULD”, etc. are to be interpreted as described in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119).

This specification documentation refers to both MIxS and LinkML terminology.
The following table can guide readers to how the terminology can be linked.

| MIxS           | LinkML               | Description                                                                                                                                |
| -------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Term           | `slot`               | A single discrete bit of information (metadata) that has various attributes on how this information should be represented and formatted    |
| Item           | `title`              | A short human readable name for the metadata term/slot                                                                                     |
| MIXS ID        | `slot_uri`           |                                                                                                                                            |
| Definition     | `description`        | A detailed human-readable explanation of what information the metadata term/slot should be holding                                         |
| Expected value | `range`              | The category of metadata the term/slot will hold (text, numbers, etc.)                                                                     |
| Value syntax   | `structured_pattern` | A way of defining how a term/slot should be filled in, e.g. with a specific format or structure                                            |
| Section        | `slot_group`         | A way of grouping similar or related terms/slots together to assist users in filling metadata tables following a logical progression       |
| Section        | `subset`             | Another way of grouping similar or related terms/slots together to assist users in filling metadata tables following a logical progression |
| Requirement    | `recommended`        | Specifying the whether a term is optional but should be to be filled in for a sample                                                       |
| Requirement    | `required`           | Specifying the whether a term is mandatory to be filled in for a sample                                                                    |
| Occurrence     | `multivalued`        | The number of times a particular term/slot can be used for a specific sample                                                               |

This document will generally use MIxS terminology, but where helpful more relevant use the LinkML equivalent, with the other form in parentheses afterwards.

## 1. General

### 1.1 LinkML compatibility

A MIxS term (slot) MUST be written in and compatible with the [LinkML](https://linkml.io/) model, and any of it's requirements (e.g. in YAML format).

It MUST conform to any MIxS specific LinkML linting requirements as defined within the [MIxS GitHub repository](https://github.com/GenomicsStandardsConsortium/mixs).

### 1.2 Slot definition

A LinkML slot is the object that is used to describe a MIxS term - i.e. information that is used to describe a particular aspect of a sample, nucleic acid,, or sequence data.

### 1.2 Language

All MIxS terms attributes MUST be written in English.

<!-- JFY comment: may be being a bit strict here, I guess you could have 'translated name' column or something like that, should rephrase to allow those exceptions -->

## 2. Term naming

### 2.1 Term name format

The term (slot) name MUST be in [snake_case](https://en.wikipedia.org/wiki/Snake_case).

All words must be lower case and underscores (`_`) MUST be used to separate words in the slot name.

### 2.1 Term name length

The term (slot) name must be a maximum of 20 characters in length.

### 2.4 Term name uniqueness

The term (slot) name MUST be unique within the MIxS LinkML model.

### 2.5 Term name descriptiveness

The term (slot) name MUST be descriptive of the data it is intended to hold.

### 2.6 Term name common prefix

When related to existing terms, the term (slot) name SHOULD use a common prefix that allow grouping of related terms.

### 2.7 Term name abbreviation

The term (slot) name SHOULD be a abbreviated form of the item (title) attribute.

## 4. Data types

### 4.1 Data types must be valid LinkML types

The data or information a term (slot) encodes MUST be in the form of a valid LinkML `range:` type:

- `string`
- `integer`
- `float`
- `boolean`
- A MIxS defined enumeration

Refer to LinkML documentation for more information on [range types](https://linkml.io/linkml-model/latest/docs/range/).

## 3 Slot attributes

### 3.1. Minimal required LinkML slot attributes

A LinkML slot of a MIxS term MUST at a minimum include following attributes:

- [`description`](https://linkml.io/linkml/schemas/metadata.html#providing-descriptions).
- [`title`](https://linkml.io/linkml-model/latest/docs/title/).
- [`examples`](https://linkml.io/linkml-model/latest/docs/examples/).
- [`in_subset`](https://linkml.io/linkml-model/latest/docs/in_subset/).
- [`keywords`](https://linkml.io/linkml-model/latest/docs/keywords/).
- [`slot_uri`](https://linkml.io/linkml-model/latest/docs/slot_uri/).
- [`range`](https://linkml.io/linkml/schemas/slots.html#ranges).

### 3.2. Recommended LinkML slot attributes

A LinkML slot of a MIxS term SHOULD at a ideally include the following attributes:

- [`recommended`](https://linkml.io/linkml/schemas/slots.html#recommended)
- [`required`](https://linkml.io/linkml/schemas/slots.html#required)

## 4. Term definition attribute

### 4.1 Description contents

The description SHOULD aim to be precise enough for a user to understand the data the term is intended to hold, how it should be filled, and used.

Links to external resources (e.g. ontologies, databases, or other documentation) SHOULD be included in the description when relevant.

### 4.2 Description length

The description MUST be at a minimum 1 sentence long that is longer than the term title.

The description MAY be multiple sentences long, but should be as concise as possible to ensure readability.

### 4.3 Description examples

The description SHOULD NOT include basic examples of the data the term is intended to hold (this is covered by the `examples` attribute).

The description MAY include examples when the information for the term requires different formatting depending on certain conditions. The description MAY also include examples when it requires additional understanding that cannot be inferred by looking purely at the `examples` section.

### 4.4 Description external resources

Links or URLs used in the description to point a reader to an external resource MUST be valid and generally accessible via the public world wide web.

External resources SHOULD only be referred to when from a stable and established resource (i.e., not a personal or website, or a resource that is not widely used).

## 5. Term item attribute

### 5.1 Title contents

The item (title) should be a full sentence version of the term (slot) name, and MUST be descriptive of the data it is intended to hold.

### 5.2 Title length

A term (slot) item (title) attribute SHOULD be as short as possible, but as long as necessary to be sufficiently descriptive, unique, and distinguishable from other terms.

### 5.2 Title format

The item (title) SHOULD be lower case, including first character of the item.

- Valid example: `library size`.
- Invalid examples:
  - `Library size` (capitalisation of first character).
  - `Library Size` (capitalisation of of all words).

Capitalisation MAY be used when it is an acronym or abbreviation that typically used capitalisation in the English language (e.g. `DNA`, `API`, `pH`).

- Valid example: `MAG coverage software`.
- Valid example: `API gravity`.

## 6. Slot examples attribute

<!-- JFY comment: this is a new guideline I would like to propose, so requires discussion  -->

### 6.1 Minimum number of examples

There MUST have minimum of 3 examples for a term (slot).

### 6.2 Scope of examples

In addition to the minimum number of examples, the examples SHOULD cover the full range of possible values, string formats, or any other way that information can be given to the term (slot).

For example if a term (slot) accepts either an ontology term _or_ a free text string, there should be at least one example for each type.
If a term (slot) accepts different unit types, there should be at least two examples of different units to demonstrate multiple units are accepted.

### 6.3 Examples for multivalued term

If a term (slot) is 'multivalued', the examples MUST include at a minimum two examples, one to show inputting a single value, and another to show how to fill the term with multiple values.

## 7. Slot in_subset attribute

> [!WARNING]
> The guidance in this section may be replaced with the use of `slot-group` in the future.

## 7.1 All core slots must be assigned a subset

All core checklist LinkML slots (terms) MUST be assigned to a subset.

## 7.2 All extension terms must not be assigned a subset

A slot (term) assigned to just an extension MUST NOT be assigned to a subset.

## 8. Term keywords attribute

### 8.1 Number of keywords

All term (slots) MUST have at least one keyword.

### 8.3 Keywords should be re-used

Re-using existing keywords SHOULD be preferred, but new keywords MAY be created if needed.

### 8.2 Keyword types

Keywords SHOULD be descriptive of the data the term is intended to hold in a way it can be grouped with with other terms (slots).

This can correspond to stage of project, domain of research, or the sample type (or extension) the term is intended to be used with.

It MAY ALSO include each descriptive part of the title (item) in full words (e.g. `air_temp` could have keywords `air` and `temperature`).

## 9. Term MIXS ID attribute

### 9.1 MIXS ID requirement

The term MUST have a MIXS ID (slot_uri) that is unique within the MIxS model.

### 9.2 MIXS ID format

The MIXS ID (slot_uri) must begin with the string `MIXS`, a colon, and followed by a 7 digit number.

## 10. Slot range attribute

### 10.1 Range options should be valid LinkML types

See section [4](#4-data-types).

### 10.2 Structured or formatted text should use a structured pattern

A term that requires a structured string layout SHOULD use the `structured_pattern` slot attribute, where the pattern components are predefined in the `settings:` section of the schema.

A slot MAY use `pattern:` attribute when XYZ <!-- TODO -->.
