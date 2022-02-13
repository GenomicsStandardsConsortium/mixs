
# Slot: seq_quality_check


Indicate if the sequence has been called by automatic systems (none) or undergone a manual editing procedure (e.g. by inspecting the raw data or chromatograms). Applied only for sequences that are not submitted to SRA,ENA or DRA

URI: [mixs.vocab:seq_quality_check](https://w3id.org/mixs/vocab/seq_quality_check)


## Domain and Range

None &#8594;  <sub>0..1</sub> [String](types/String.md)

## Parents

 *  is_a: [sequencing field](sequencing_field.md)

## Children

 *  [MIMARKS specimen➞seq_quality_check](MIMARKS_specimen_seq_quality_check.md)
 *  [MIMARKS survey➞seq_quality_check](MIMARKS_survey_seq_quality_check.md)

## Used by

 * [Core](Core.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | sequence quality check |
| **Mappings:** | | MIXS:0000051 |
| **Comments:** | | Expected value: none or manually edited |
| **Examples:** | | Example(value='none', description=None) |

