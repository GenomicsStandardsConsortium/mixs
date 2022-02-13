
# Slot: pcr_primers


PCR primers that were used to amplify the sequence of the targeted gene, locus or subfragment. This field should contain all the primers used for a single PCR reaction if multiple forward or reverse primers are present in a single PCR reaction. The primer sequence should be reported in uppercase letters

URI: [mixs.vocab:pcr_primers](https://w3id.org/mixs/vocab/pcr_primers)


## Domain and Range

None &#8594;  <sub>0..1</sub> [String](types/String.md)

## Parents

 *  is_a: [sequencing field](sequencing_field.md)

## Children

 *  [MIMARKS specimen➞pcr_primers](MIMARKS_specimen_pcr_primers.md)
 *  [MIMARKS survey➞pcr_primers](MIMARKS_survey_pcr_primers.md)

## Used by

 * [Core](Core.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | pcr primers |
| **Mappings:** | | MIXS:0000046 |
| **Comments:** | | Expected value: FWD: forward primer sequence;REV:reverse primer sequence |
| **Examples:** | | Example(value='FWD:GTGCCAGCMGCCGCGGTAA;REV:GGACTACHVGGGTWTCTAAT', description=None) |

