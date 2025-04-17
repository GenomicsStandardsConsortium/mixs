# Gold Standard MIxS LinkML Slots

## Introduction

This page lists a range of 'gold standard' examples of slots that are used in the MIxS LinkML schema.

There are examples of slots that cover a range of common types of data, including:

- [Integer](#integer) (numeric)
- [Float](#float) (numeric)
- [String](#string) (free text)
- [Fixed list](#fixed-list) (enumeration)
- [Boolean](#boolean)
- [Structured text (text only)](#structured-text-text-only) (text only)
- [Structured text (with unit)](#structured-text-numeric-with-units) (numeric with units)
- [Structured text (ontology term)](#structured-text-ontology-term)
- [URL](#url) (or other link utilising a URL like structure)
- [Mixed type](#mixed-type) (either free text, or from an ontology)

You can use these as templates on how to construct your own new slot to the highest quality level expected.

## Overview

Every MIxS LinkML slot should have at a minimum the following attributes:

- [`description`](https://linkml.io/linkml/schemas/metadata.html#providing-descriptions): the description of what the metadata term is for
- [`title`](https://linkml.io/linkml-model/latest/docs/title/): a short human readable 'title' for the slot
- [`examples`](https://linkml.io/linkml-model/latest/docs/examples/): examples values demonstrating how the slot should be used
- [`in_subset`](https://linkml.io/linkml-model/latest/docs/in_subset/): the section of the schema that the slot belongs based on a [fix list of MIxS categories](https://github.com/GenomicsStandardsConsortium/mixs/blob/609b0f567486f64cb7061246588d8006f87fa138/src/mixs/schema/mixs.yaml#L21-L26)
  - Note: this may be replaced in the near future!
- [`keywords`](https://linkml.io/linkml-model/latest/docs/keywords/): useful keywords to allow grouping of related slots together
- [`slot_uri`](https://linkml.io/linkml-model/latest/docs/slot_uri/): a unique ID assigned by MIxS
  - This likely only gets assigned upon acceptance and merging by the core GSC MIxS team
  - During development you can use a dummy value for this
- [`range`](https://linkml.io/linkml/schemas/slots.html#ranges): specifying the type of 'object' that put in the slot (numeric, string, etc.)

And for some slots, the following attributes are also recommended:

- If a term should be either mandatory or optional
  - [`recommended`](https://linkml.io/linkml/schemas/slots.html#recommended): a boolean value indicating if the slot is recommended be filled
  - [`required`](https://linkml.io/linkml/schemas/slots.html#required): a boolean value indicating if the slot is mandatory to be filled
- If a term should be allowed multiple entries

  - [`multivalued`](https://linkml.io/linkml/schemas/slots.html#multivalued)
    - Essentially indicates the contents of the slot can be a list, and each element is evaluated independently against the remaining slot attributes

- If a string or mix-`range`-based term has a particular format it should follow:

  - [structured_pattern](https://linkml.io/linkml/schemas/constraints.html#structured-patterns): a particular regex-like pattern that includes pre-defined components that describe how each component should be formatted
    - In the MIxS LinkML schema, these preset formats can be seen under the [`settings`](https://github.com/GenomicsStandardsConsortium/mixs/blob/609b0f567486f64cb7061246588d8006f87fa138/src/mixs/schema/mixs.yaml#L21852-L21887) section of the schema
  - [pattern](https://linkml.io/linkml/schemas/constraints.html#patterns): a regex pattern that the string will be compared against for validation
    - This is a more generalised version of `structured_pattern`, and can be used for any string-based slot
    - It is typically used for 'one-off' formats that would not be reused in other metadata schemas

## Examples

### Integer

An example of a close-to gold standard _integer_ slot is [`lib_reads_seqd`](https://genomicsstandardsconsortium.github.io/mixs/0000040/):

```yaml
lib_reads_seqd:
  description: Total number of clones sequenced from the library
  title: library reads sequenced
  examples:
    - value: "20"
  in_subset:
    - sequencing
  keywords:
    - library
  slot_uri: MIXS:0000040
  range: integer
```

<!--
JFY comment: I don't like this so much as:

- the description is very minimal, the example value is in quotes
- single example (I like a few, even for very simple terms)
- only one keyword
- no recommended or required
-->

<!--
TODO: for all examples, explain why it's good/the particularties
-->

### Float

An example of a close-to gold standard _float_ slot is [`-s`](https://genomicsstandardsconsortium.github.io/mixs/0001001/):

```yaml
ph:
  description:
    Ph measurement of the sample, or liquid portion of sample, or aqueous
    phase of the fluid
  title: pH
  examples:
    - value: "7.2"
  keywords:
    - ph
  slot_uri: MIXS:0001001
  range: float
```

<!--
JFY comment: I don't like this so much as:

- the description is very minimal, the example value is in quotes
- single example (I like a few, even for very simple terms)
- only one keyword
- no recommended or required
-->

### String

An example of a close-to gold standard _string (freetext)_ slot is [`wga_amp_kit`](https://genomicsstandardsconsortium.github.io/mixs/0000006/):

```yaml
wga_amp_kit:
  annotations:
    Expected_value: kit name
  description: Kit used to amplify genomic DNA in preparation for sequencing
  title: WGA amplification kit
  examples:
    - value: qiagen repli-g
  in_subset:
    - sequencing
  keywords:
    - kit
  range: string
  slot_uri: MIXS:0000006
```

<!--
JFY comment: I don't like this so much as:

- single example
- missing subset
- single keyword
-->

### Fixed list

An example of a close-to gold standard _enum_ slot is [`assembly_qual`](https://genomicsstandardsconsortium.github.io/mixs/0000056/):

```yaml
assembly_qual:
  description:
    "The assembly quality category is based on sets of criteria outlined
    for each assembly quality category. For MISAG/MIMAG; Finished: Single, validated,
    contiguous sequence per replicon without gaps or ambiguities with a consensus
    error rate equivalent to Q50 or better. High Quality Draft:Multiple fragments
    where gaps span repetitive regions. Presence of the large subunit (LSU) RNA, small
    subunit (SSU) and the presence of 5.8S rRNA or 5S rRNA depending on whether it is
    a eukaryotic or prokaryotic genome, respectively.
    Medium Quality Draft:Many fragments with little to no
    review of assembly other than reporting of standard assembly statistics. Low
    Quality Draft:Many fragments with little to no review of assembly other than
    reporting of standard assembly statistics. Assembly statistics include, but
    are not limited to total assembly size, number of contigs, contig N50/L50, and
    maximum contig length. For MIUVIG; Finished: Single, validated, contiguous sequence
    per replicon without gaps or ambiguities, with extensive manual review and editing
    to annotate putative gene functions and transcriptional units. High-quality
    draft genome: One or multiple fragments, totaling   90% of the expected genome
    or replicon sequence or predicted complete. Genome fragment(s): One or multiple
    fragments, totalling < 90% of the expected genome or replicon sequence, or for
    which no genome size could be estimated"
  title: assembly quality
  examples:
    - value: High-quality draft genome
  in_subset:
    - sequencing
  keywords:
    - quality
  range: AssemblyQualEnum
  slot_uri: MIXS:0000056
```

<!--
JFY comment: I don't like this so much as:

- single example
-->

### Boolean

An example of a close-to gold standard _boolean_ slot is [`x16s_recover`](https://genomicsstandardsconsortium.github.io/mixs/0000065/):

```yaml
x16s_recover:
  description: Can a 16S gene be recovered from the submitted SAG or MAG?
  title: 16S recovered
  examples:
    - value: "yes"
  in_subset:
    - sequencing
  keywords:
    - recover
  slot_uri: MIXS:0000065
  range: boolean
```

<!--
JFY comment: I don't like this so much as:

- no recommended or required
-->

### Structured text (text only)

An example of a close-to gold standard _Structured text (text only)_ slot is [`adapters`](https://genomicsstandardsconsortium.github.io/mixs/0000048/):

```yaml
adapters:
  description:
    Adapters provide priming sequences for both amplification and sequencing
    of the sample-library fragments. Both adapters should be reported; in uppercase
    letters
  title: adapters
  examples:
    - value: AATGATACGGCGACCACCGAGATCTACACGCT;CAAGCAGAAGACGGCATACGAGAT
  in_subset:
    - sequencing
  structured_pattern:
    syntax: ^{adapter_A_DNA_sequence};{adapter_B_DNA_sequence}$
    interpolated: true
    partial_match: true
  slot_uri: MIXS:0000048
```

<!--
JFY comment: I don't like this so much as:

- single example
- no keywords
-->

### Structured text (numeric with units)

An example of a close-to gold standard _Structured text (numeric with units)_ slot is [`size_frac`](https://genomicsstandardsconsortium.github.io/mixs/0000017/):

```yaml
size_frac:
  annotations:
    Expected_value: filter size value range
  description: Filtering pore size used in sample preparation
  title: size fraction selected
  examples:
    - value: 0-0.22 micrometer
  in_subset:
    - nucleic acid sequence source
  keywords:
    - fraction
    - size
  string_serialization: "{float}-{float} {unit}"
  slot_uri: MIXS:0000017
```

<!--
JFY comment: I don't like this so much as:

- single example
- is a value range not a single value
- missing range? (but possibly assumed default)
-->

### Structured text (ontology term)

An example of a close-to gold standard _Structured text (ontology term)_ slot is [`env_medium`](https://genomicsstandardsconsortium.github.io/mixs/0000014/)

```yaml
env_medium:
  description: "Report the environmental material(s) immediately surrounding the
    sample or specimen at the time of sampling. We recommend using subclasses of
    'environmental material' (http://purl.obolibrary.org/obo/ENVO_00010483). EnvO
    documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
    . Terms from other OBO ontologies are permissible as long as they reference
    mass/volume nouns (e.g. air, water, blood) and not discrete, countable entities
    (e.g. a tree, a leaf, a table top)"
  title: environmental medium
  examples:
    - value: bluegrass field soil [ENVO:00005789]
  in_subset:
    - environment
  keywords:
    - environmental
  slot_uri: MIXS:0000014
  range: string
  required: true
  pattern: ^([^\s-]{1,2}|[^\s-]+.+[^\s-]+) \[[a-zA-Z]{2,}:[a-zA-Z0-9]\d+\]$
  structured_pattern:
    syntax: ^{termLabel} \[{termID}\]$
    interpolated: true
    partial_match: true
```

<!--
JFY comment: I don't like this so much as:

- Why pattern AND structured_pattern?
-->

### URL

An example of a close-to gold standard _URL_ slot is [`isol_growth_condt`](https://genomicsstandardsconsortium.github.io/mixs/0000003/):

```yaml
isol_growth_condt:
  description:
    Publication reference in the form of pubmed ID (pmid), digital object
    identifier (doi) or url for isolation and growth condition specifications of
    the organism/material
  title: isolation and growth condition
  examples:
    - value: doi:10.1016/j.syapm.2018.01.009
  in_subset:
    - nucleic acid sequence source
  keywords:
    - condition
    - growth
    - isolation
  slot_uri: MIXS:0000003
  range: string
  pattern: ^^PMID:\d+$|^doi:10.\d{2,9}/.*$|^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$$
  structured_pattern:
    syntax: ^{PMID}|{DOI}|{URL}$
    interpolated: true
    partial_match: true
```

<!--
JFY comment: I don't like this so much as:

- Single example, even though multiple URL types
-->

### Mixed type

An example of a close-to gold standard _mixed type_ slot is [`microb_cult_med`](https://genomicsstandardsconsortium.github.io/mixs/0001216/):

```yaml
microb_cult_med:
  description:
    A culture medium used to select for, grow, and maintain prokaryotic
    microorganisms. Can be in either liquid (broth) or solidified (e.g. with agar)
    forms. This field accepts terms listed under microbiological culture medium
    (http://purl.obolibrary.org/obo/MICRO_0000067). If the proper descriptor is
    not listed please use text to describe the culture medium
  title: microbiological culture medium
  examples:
    - value: brain heart infusion agar [MICRO:0000566]
  keywords:
    - culture
    - microbiological
  slot_uri: MIXS:0001216
  range: string
  pattern: ^([^\s-]{1,2}|[^\s-]+.+[^\s-]+)|(([^\s-]{1,2}|[^\s-]+.+[^\s-]+) \[[a-zA-Z]{2,}:[a-zA-Z0-9]\d+\])$
  structured_pattern:
    syntax: ^{text}|({termLabel} \[{termID}\])$
    interpolated: true
    partial_match: true
```

<!--
JFY comment: I don't like this so much as:

- Single example, even though it can be an ontology term OR a free text
-->
