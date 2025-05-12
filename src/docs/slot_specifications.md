# (Unoffical) MIxS LinkML Slot Specifications

The key words “MUST”, “MUST NOT”, “SHOULD”, etc. are to be interpreted as described in RFC 2119.

| Metadata     | Value                         |
| ------------ | ----------------------------- |
| Version      | 0.0.1                         |
| Last updated | 2025-05-05                    |
| Authors      | James Fellows Yates (@jfy133) |

## 1. General

### 1.1 LinkML compatibility

A MIxS slot MUST be written in and compatible with the [LinkML](https://linkml.io/) model, and any of it's requirements (e.g. in YAML format).

It MUST conform to any MIxS specific LinkML linting requirements as defined within the [MIxS GitHub repository](https://github.com/GenomicsStandardsConsortium/mixs).

### 1.2 Slot definition

A MIxS slot is a LinkML slot object that is used to describe a MIxS metadata term - i.e. information that is used to describe a particular aspect of a sample, nucleic acid,, or sequence data.

### 1.2 Language

All MIxS LinkML slots attributes MUST be written in English.

<!-- JFY comment: may be being a bit strict here, I guess you could have 'translated name' column or something like that, should rephrase to allow those exceptions -->

## 2. Slot naming

### 2.1 Slot name format

The slot name MUST be in snake_case.

### 2.2 Slot name uniqueness

The slot name MUST be unique within the MIxS LinkML model.

### 2.3 Slot name descriptiveness

The slot name MUST be descriptive of the data it is intended to hold.

### 2.5 Slot name common prefix

When related to existing terms, the slot name SHOULD use a common prefix that allow grouping of related terms.

### 2.6 Slot name abbreviation

The slot name SHOULD be a abbreviated form of the title attribute.

## 4. Data types

### 4.1 Data types must be valid LinkML types

The data or information a slot encodes MUST be in the form of a valid LinkML `range:` type:

- `string`
- `integer`
- `float`
- `boolean`
- A MIxS defined enumeration

Refer to LinkML documentation for more information on [range types](https://linkml.io/linkml-model/latest/docs/range/).

## 3 Slot attributes

### 3.1. Minimal required slot attributes

A MIxS LinkML slot MUST at a minimum include following attributes:

- [`description`](https://linkml.io/linkml/schemas/metadata.html#providing-descriptions).
- [`title`](https://linkml.io/linkml-model/latest/docs/title/).
- [`examples`](https://linkml.io/linkml-model/latest/docs/examples/).
- [`in_subset`](https://linkml.io/linkml-model/latest/docs/in_subset/).
- [`keywords`](https://linkml.io/linkml-model/latest/docs/keywords/).
- [`slot_uri`](https://linkml.io/linkml-model/latest/docs/slot_uri/).
- [`range`](https://linkml.io/linkml/schemas/slots.html#ranges).

### 3.2. Recommended slot attributes

A MIxS LinkML slot SHOULD at a ideally include the following attributes:

- [`recommended`](https://linkml.io/linkml/schemas/slots.html#recommended)
- [`required`](https://linkml.io/linkml/schemas/slots.html#required)

## 4. Slot description attribute

### 4.1 Description contents

The description SHOULD aim to be precise enough for a user to understand the data the slot is intended to hold, how it should be filled, and used.

Links to external resources (e.g. ontologies, databases, or other documentation) SHOULD be included in the description when relevant.

### 4.2 Description length

The description MUST be at a minimum 1 sentence long that is longer than the slot title.

The description MAY be multiple sentences long, but should be as concise as possible to ensure readability.

### 4.3 Description examples

The description SHOULD NOT include basic examples of the data the slot is intended to hold (this is covered by the `examples` attribute).

The description MAY include examples when the information for the slot requires different formatting depending on certain conditions. The description MAY also include examples when it requires additional understanding that cannot be inferred by looking purely at the `examples` section.

### 4.4 Description external resources

Links or URLs used in the description to point a reader to an external resource MUST be valid and generally accessible via the public world wide web.

External resources SHOULD only be referred to when from a stable and established resource (i.e., not a personal or website, or a resource that is not widely used).

## 5. Slot title attribute

### 5.1 Title contents

The title should be a full sentence version of the slot name, and MUST be descriptive of the data it is intended to hold.

### 5.2 Title length

A slot title SHOULD be as short as possible, but as long as necessary to be sufficiently descriptive, unique, and distinguishable from other terms.

### 5.2 Title format

The title SHOULD be lower case, including first character of the title.

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

There MUST have minimum of 3 examples for a slot.

### 6.2 Scope of examples

In addition to the minimum number of examples, the examples SHOULD cover the full range of possible values, string formats, or any other way that information can be given to the slot.

For example if a slot accepts either an ontology term _or_ a free text string, there should be at least one example for each type.
If a slot accepts different unit types, there should be at least two examples of different units to demonstrate multiple units are accepted.

### 6.3 Examples for multivalued slots

If a slot is multivalued, the examples MUST include at a minimum two examples, one to show inputting a single value, and another to show how to fill the slot with multiple values.

## 7. Slot in_subset attribute

> [!WARNING]
> The guidance in this section may be replaced with the use of `slot-group` in the future.

## 7.1 All core slots must be assigned a subset

All core checklist MIxS term slots MUST be assigned to a subset.

## 7.2 All extension slots must not be assigned a subset

Slots assigned to just an extension MUST NOT be assigned to a subset.

## 8. Slot keywords attribute

### 8.1 Number of keywords

All slots MUST have at least one keyword.

### 8.3 Keywords should be re-used

Re-using existing keywords SHOULD be preferred, but new keywords MAY be created if needed.

### 8.2 Keyword types

Keywords SHOULD be descriptive of the data the slot is intended to hold in a way it can be grouped with like term slots.

This can correspond to stage of project, domain of research, or the sample type (or extension) the slot is intended to be used with.

It MAY ALSO include each descriptive part of the title in full words (e.g. `air_temp` could have keywords `air` and `temperature`).

## 9. Slot slot_uri attribute

### 9.1 URI requirement

The slot MUST have a URI that is unique within the MIxS LinkML model.

### 9.2 URI format

The URL must begin with the string `MIXS`, a colon, and followed by a 7 digit number.

## 10. Slot range attribute

### 10.1 Range options should be valid LinkML types

See section [4](#4-data-types).

### 10.2 Structured or formatted text should use a structured pattern

A slot that requires a structured string SHOULD use the `structured_pattern` attribute, where the pattern components are predefined in the `settings:` section of the schema.

A slot MAY use `pattern:` attribute when XYZ <!-- TODO -->.
