# MIxS LinkML Slot Specifications

The key words “MUST”, “MUST NOT”, “SHOULD”, etc. are to be interpreted as described in RFC 2119.

## 1. Slot attributes

<!-- TODO: Add point about slot must be written in LinkML etc.  -->

### 1.1. Minimal required slot attributes

A MIxS LinkML slot MUST at a minimum include following attributes:

- [`description`](https://linkml.io/linkml/schemas/metadata.html#providing-descriptions)
- [`title`](https://linkml.io/linkml-model/latest/docs/title/)
- [`examples`](https://linkml.io/linkml-model/latest/docs/examples/)
- [`in_subset`](https://linkml.io/linkml-model/latest/docs/in_subset/)
- [`keywords`](https://linkml.io/linkml-model/latest/docs/keywords/)
- [`slot_uri`](https://linkml.io/linkml-model/latest/docs/slot_uri/)
- [`range`](https://linkml.io/linkml/schemas/slots.html#ranges)

### 1.2. Recommended slot attributes

A MIxS LinkML slot SHOULD at a ideally include the following attributes:

- [`recommended`](https://linkml.io/linkml/schemas/slots.html#recommended)
- [`required`](https://linkml.io/linkml/schemas/slots.html#required)

## 2. Naming

A MIxS LinkML slot MUST be named according to the following rules:

- The slot name MUST be in snake_case.
- The slot name MUST be unique within the MIxS LinkML model.
- The slot name MUST be descriptive of the data it is intended to hold.
- The slot name MUST be in English.
- When related to existing terms, the slot name SHOULD use a common prefix that allow grouping of related terms.
- The slot name SHOULD be a abbreviated form of the title attribute.

## 3. Data types

### 3.1 Range types

The slot MUST have a range type from the following options:

- `string`
- `integer`
- `float`
- `boolean`
- A MIxS defined enumeration

### 3.2 Structured string slots

A slot that requires a structured string SHOULD use the `structured_pattern` attribute, where the pattern components are predefined in the `settings:` section of the schema.

A slot MAY use `pattern:` attribute when XYZ <!-- TODO -->.

## 4. Slot URI

### 4.1 URI requirement

The slot MUST have a URI that is unique within the MIxS LinkML model.

### 4.2 URI format

The URL must begin with the string `MIXS`, a colon, and followed by a 7 digit number.
