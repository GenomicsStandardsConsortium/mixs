
# Slot: host_disease_stat


List of diseases with which the host has been diagnosed; can include multiple diagnoses. The value of the field depends on host; for humans the terms should be chosen from the DO (Human Disease Ontology) at https://www.disease-ontology.org, non-human host diseases are free text

URI: [mixs.vocab:human_associated_host_disease_stat](https://w3id.org/mixs/vocab/human_associated_host_disease_stat)


## Domain and Range

[Human-associated](Human-associated.md) &#8594;  <sub>0..1</sub> [String](types/String.md)

## Parents

 *  is_a: [host_disease_stat](host_disease_stat.md)

## Children


## Used by

 * [Human-associated](Human-associated.md)
 * [Human-associatedMIGSBacteria](Human-associatedMIGSBacteria.md)
 * [Human-associatedMIGSEukaryote](Human-associatedMIGSEukaryote.md)
 * [Human-associatedMIGSOrg](Human-associatedMIGSOrg.md)
 * [Human-associatedMIGSPlant](Human-associatedMIGSPlant.md)
 * [Human-associatedMIGSVirus](Human-associatedMIGSVirus.md)
 * [Human-associatedMIMAG](Human-associatedMIMAG.md)
 * [Human-associatedMIMARKSSpecimen](Human-associatedMIMARKSSpecimen.md)
 * [Human-associatedMIMARKSSurvey](Human-associatedMIMARKSSurvey.md)
 * [Human-associatedMIMS](Human-associatedMIMS.md)
 * [Human-associatedMISAG](Human-associatedMISAG.md)
 * [Human-associatedMIUVIG](Human-associatedMIUVIG.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | host disease status |
| **Mappings:** | | MIXS:0000031 |
| **Comments:** | | Expected value: disease name or Disease Ontology term |
| **Examples:** | | Example(value='rabies [DOID:11260]', description=None) |

