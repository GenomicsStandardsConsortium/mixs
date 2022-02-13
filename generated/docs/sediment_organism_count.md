
# Slot: organism_count


Total cell count of any organism (or group of organisms) per gram, volume or area of sample, should include name of organism followed by count. The method that was used for the enumeration (e.g. qPCR, atp, mpn, etc.) Should also be provided. (example: total prokaryotes; 3.5e7 cells per ml; qpcr)

URI: [mixs.vocab:sediment_organism_count](https://w3id.org/mixs/vocab/sediment_organism_count)


## Domain and Range

[Sediment](Sediment.md) &#8594;  <sub>0..\*</sub> [organism_count_enum](organism_count_enum.md)

## Parents

 *  is_a: [organism_count](organism_count.md)

## Children


## Used by

 * [Sediment](Sediment.md)
 * [SedimentMIGSBacteria](SedimentMIGSBacteria.md)
 * [SedimentMIGSEukaryote](SedimentMIGSEukaryote.md)
 * [SedimentMIGSOrg](SedimentMIGSOrg.md)
 * [SedimentMIGSPlant](SedimentMIGSPlant.md)
 * [SedimentMIGSVirus](SedimentMIGSVirus.md)
 * [SedimentMIMAG](SedimentMIMAG.md)
 * [SedimentMIMARKSSpecimen](SedimentMIMARKSSpecimen.md)
 * [SedimentMIMARKSSurvey](SedimentMIMARKSSurvey.md)
 * [SedimentMIMS](SedimentMIMS.md)
 * [SedimentMISAG](SedimentMISAG.md)
 * [SedimentMIUVIG](SedimentMIUVIG.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | organism count |
| **Mappings:** | | MIXS:0000103 |
| **Comments:** | | Expected value: organism name;measurement value;enumeration |
|  | | Preferred unit: number of cells per cubic meter, number of cells per milliliter, number of cells per cubic centimeter |
| **Examples:** | | Example(value='total prokaryotes;3.5e7 cells per milliliter;qPCR', description=None) |

