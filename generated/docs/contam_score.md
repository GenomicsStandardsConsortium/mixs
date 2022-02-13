
# Slot: contam_score


The contamination score is based on the fraction of single-copy genes that are observed more than once in a query genome. The following scores are acceptable for; High Quality Draft: < 5%, Medium Quality Draft: < 10%, Low Quality Draft: < 10%. Contamination must be below 5% for a SAG or MAG to be deposited into any of the public databases

URI: [mixs.vocab:contam_score](https://w3id.org/mixs/vocab/contam_score)


## Domain and Range

None &#8594;  <sub>0..1</sub> [String](types/String.md)

## Parents

 *  is_a: [sequencing field](sequencing_field.md)

## Children

 *  [MIMAG➞contam_score](MIMAG_contam_score.md)
 *  [MISAG➞contam_score](MISAG_contam_score.md)

## Used by

 * [Core](Core.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | contamination score |
| **Mappings:** | | MIXS:0000072 |
| **Comments:** | | Expected value: value |
| **Examples:** | | Example(value='1%', description=None) |

