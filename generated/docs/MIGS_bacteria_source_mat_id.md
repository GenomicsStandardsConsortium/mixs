
# Slot: source_mat_id


A unique identifier assigned to a material sample (as defined by http://rs.tdwg.org/dwc/terms/materialSampleID, and as opposed to a particular digital record of a material sample) used for extracting nucleic acids, and subsequent sequencing. The identifier can refer either to the original material collected or to any derived sub-samples. The INSDC qualifiers /specimen_voucher, /bio_material, or /culture_collection may or may not share the same value as the source_mat_id field. For instance, the /specimen_voucher qualifier and source_mat_id may both contain 'UAM:Herps:14' , referring to both the specimen voucher and sampled tissue with the same identifier. However, the /culture_collection qualifier may refer to a value from an initial culture (e.g. ATCC:11775) while source_mat_id would refer to an identifier from some derived culture from which the nucleic acids were extracted (e.g. xatc123 or ark:/2154/R2).

URI: [mixs.vocab:MIGS_bacteria_source_mat_id](https://w3id.org/mixs/vocab/MIGS_bacteria_source_mat_id)


## Domain and Range

[MIGSBacteria](MIGSBacteria.md) &#8594;  <sub>0..1</sub> [String](types/String.md)

## Parents

 *  is_a: [source_mat_id](source_mat_id.md)

## Children


## Used by

 * [MIGSBacteria](MIGSBacteria.md)
 * [AirMIGSBacteria](AirMIGSBacteria.md)
 * [BuiltEnvironmentMIGSBacteria](BuiltEnvironmentMIGSBacteria.md)
 * [Host-associatedMIGSBacteria](Host-associatedMIGSBacteria.md)
 * [Human-associatedMIGSBacteria](Human-associatedMIGSBacteria.md)
 * [Human-gutMIGSBacteria](Human-gutMIGSBacteria.md)
 * [Human-oralMIGSBacteria](Human-oralMIGSBacteria.md)
 * [Human-skinMIGSBacteria](Human-skinMIGSBacteria.md)
 * [Human-vaginalMIGSBacteria](Human-vaginalMIGSBacteria.md)
 * [HydrocarbonResources-coresMIGSBacteria](HydrocarbonResources-coresMIGSBacteria.md)
 * [HydrocarbonResources-fluidsSwabsMIGSBacteria](HydrocarbonResources-fluidsSwabsMIGSBacteria.md)
 * [MicrobialMatBiofilmMIGSBacteria](MicrobialMatBiofilmMIGSBacteria.md)
 * [MiscellaneousNaturalOrArtificialEnvironmentMIGSBacteria](MiscellaneousNaturalOrArtificialEnvironmentMIGSBacteria.md)
 * [Plant-associatedMIGSBacteria](Plant-associatedMIGSBacteria.md)
 * [SedimentMIGSBacteria](SedimentMIGSBacteria.md)
 * [SoilMIGSBacteria](SoilMIGSBacteria.md)
 * [WastewaterSludgeMIGSBacteria](WastewaterSludgeMIGSBacteria.md)
 * [WaterMIGSBacteria](WaterMIGSBacteria.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | source material identifiers |
| **Mappings:** | | MIXS:0000026 |
| **Comments:** | | Expected value: for cultures of microorganisms: identifiers for two culture collections; for other material a unique arbitrary identifer |
| **Examples:** | | Example(value='MPI012345', description=None) |

