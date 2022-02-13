
# Slot: host_disease_stat


List of diseases with which the host has been diagnosed; can include multiple diagnoses. The value of the field depends on host; for humans the terms should be chosen from the DO (Human Disease Ontology) at https://www.disease-ontology.org, non-human host diseases are free text

URI: [mixs.vocab:host_associated_host_disease_stat](https://w3id.org/mixs/vocab/host_associated_host_disease_stat)


## Domain and Range

[Host-associated](Host-associated.md) &#8594;  <sub>0..1</sub> [String](types/String.md)

## Parents

 *  is_a: [host_disease_stat](host_disease_stat.md)

## Children


## Used by

 * [Host-associated](Host-associated.md)
 * [Host-associatedMIGSBacteria](Host-associatedMIGSBacteria.md)
 * [Host-associatedMIGSEukaryote](Host-associatedMIGSEukaryote.md)
 * [Host-associatedMIGSOrg](Host-associatedMIGSOrg.md)
 * [Host-associatedMIGSPlant](Host-associatedMIGSPlant.md)
 * [Host-associatedMIGSVirus](Host-associatedMIGSVirus.md)
 * [Host-associatedMIMAG](Host-associatedMIMAG.md)
 * [Host-associatedMIMARKSSpecimen](Host-associatedMIMARKSSpecimen.md)
 * [Host-associatedMIMARKSSurvey](Host-associatedMIMARKSSurvey.md)
 * [Host-associatedMIMS](Host-associatedMIMS.md)
 * [Host-associatedMISAG](Host-associatedMISAG.md)
 * [Host-associatedMIUVIG](Host-associatedMIUVIG.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | host disease status |
| **Mappings:** | | MIXS:0000031 |
| **Comments:** | | Expected value: disease name or Disease Ontology term |
| **Examples:** | | Example(value='rabies [DOID:11260]', description=None) |

