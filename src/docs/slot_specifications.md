# MIxS LinkML Slot Specifications

The key words “MUST”, “MUST NOT”, “SHOULD”, etc. are to be interpreted as described in RFC 2119.

## 1. Slot attributes

### 1.1. Minimal required slot attributes

A MIxS LinkML slot MUST at a minimum include following attributes:

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

The slot MUST have a range type from the following options.

## 4. Slot URI

### 4.1 URI requirement

The slot MUST have a URI that is unique within the MIxS LinkML model.

### 4.2 URI format

The URL must begin with the string `MIXS`, a colon, and followed by a 7 digit number.
