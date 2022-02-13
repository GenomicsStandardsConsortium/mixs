
# Slot: propagation


The type of reproduction from the parent stock. Values for this field is specific to different taxa. For phage or virus: lytic/lysogenic/temperate/obligately lytic. For plasmids: incompatibility group. For eukaryotes: sexual/asexual.

URI: [mixs.vocab:propagation](https://w3id.org/mixs/vocab/propagation)


## Domain and Range

None &#8594;  <sub>0..1</sub> [String](types/String.md)

## Parents

 *  is_a: [nucleic acid sequence source field](nucleic_acid_sequence_source_field.md)

## Children

 *  [MIGS eukaryote➞propagation](MIGS_eukaryote_propagation.md)
 *  [MIGS plant➞propagation](MIGS_plant_propagation.md)
 *  [MIGS virus➞propagation](MIGS_virus_propagation.md)

## Used by

 * [Core](Core.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | propagation |
| **Mappings:** | | MIXS:0000033 |
| **Comments:** | | Expected value: for virus: lytic, lysogenic, temperate, obligately lytic; for plasmid: incompatibility group; for eukaryote: asexual, sexual; other more specific values (e.g., incompatibility group) are allowed |
| **Examples:** | | Example(value='lytic', description=None) |

