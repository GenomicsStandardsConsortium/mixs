
# Slot: source_mat_id


A unique identifier assigned to a material sample (as defined by http://rs.tdwg.org/dwc/terms/materialSampleID, and as opposed to a particular digital record of a material sample) used for extracting nucleic acids, and subsequent sequencing. The identifier can refer either to the original material collected or to any derived sub-samples. The INSDC qualifiers /specimen_voucher, /bio_material, or /culture_collection may or may not share the same value as the source_mat_id field. For instance, the /specimen_voucher qualifier and source_mat_id may both contain 'UAM:Herps:14' , referring to both the specimen voucher and sampled tissue with the same identifier. However, the /culture_collection qualifier may refer to a value from an initial culture (e.g. ATCC:11775) while source_mat_id would refer to an identifier from some derived culture from which the nucleic acids were extracted (e.g. xatc123 or ark:/2154/R2).

URI: [mixs.vocab:source_mat_id](https://w3id.org/mixs/vocab/source_mat_id)


## Domain and Range

None &#8594;  <sub>0..1</sub> [String](types/String.md)

## Parents

 *  is_a: [nucleic acid sequence source field](nucleic_acid_sequence_source_field.md)

## Children

 *  [MIGS bacteria➞source_mat_id](MIGS_bacteria_source_mat_id.md)
 *  [MIGS eukaryote➞source_mat_id](MIGS_eukaryote_source_mat_id.md)
 *  [MIGS org➞source_mat_id](MIGS_org_source_mat_id.md)
 *  [MIGS plant➞source_mat_id](MIGS_plant_source_mat_id.md)
 *  [MIGS virus➞source_mat_id](MIGS_virus_source_mat_id.md)
 *  [MIMAG➞source_mat_id](MIMAG_source_mat_id.md)
 *  [MIMARKS specimen➞source_mat_id](MIMARKS_specimen_source_mat_id.md)
 *  [MIMARKS survey➞source_mat_id](MIMARKS_survey_source_mat_id.md)
 *  [MIMS➞source_mat_id](MIMS_source_mat_id.md)
 *  [MISAG➞source_mat_id](MISAG_source_mat_id.md)
 *  [MIUVIG➞source_mat_id](MIUVIG_source_mat_id.md)

## Used by

 * [Core](Core.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | source material identifiers |
| **Mappings:** | | MIXS:0000026 |
| **Comments:** | | Expected value: for cultures of microorganisms: identifiers for two culture collections; for other material a unique arbitrary identifer |
| **Examples:** | | Example(value='MPI012345', description=None) |

