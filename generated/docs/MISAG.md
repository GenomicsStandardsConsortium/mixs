
# Class: MISAG


Minimum Information About a Single Amplified Genome

URI: [mixs.vocab:MISAG](https://w3id.org/mixs/vocab/MISAG)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<samp_vol_we_dna_ext%200..1-++[MISAG&#124;submitted_to_insdc:string;investigation_type:investigation_type_enum;samp_name:string;samp_taxon_id:string;project_name:string;experimental_factor:string%20%3F;lat_lon:string;geo_loc_name:string;collection_date:date;neg_cont_type:neg_cont_type_enum%20%3F;pos_cont_type:string%20%3F;env_broad_scale:string;env_local_scale:string;env_medium:string;env_package:env_package_enum%20%3F;ref_biomaterial:string%20%3F;source_mat_id:string%20%3F;rel_to_oxygen:rel_to_oxygen_enum%20%3F;samp_collec_device:string%20%3F;samp_collec_method:string%20%3F;samp_mat_process:string%20%3F;size_frac:string%20%3F;nucl_acid_ext:string%20%3F;nucl_acid_amp:string%20%3F;lib_size:integer%20%3F;lib_reads_seqd:integer%20%3F;lib_layout:lib_layout_enum%20%3F;lib_vector:string%20%3F;lib_screen:string%20%3F;mid:string%20%3F;adapters:string%20%3F;seq_meth:string;tax_ident:tax_ident_enum;assembly_qual:assembly_qual_enum;assembly_name:string%20%3F;assembly_software:string;annot:string%20%3F;number_contig:integer%20%3F;feat_pred:string%20%3F;ref_db:string%20%3F;sim_search_meth:string%20%3F;tax_class:string%20%3F;x_16s_recover:string%20%3F;x_16s_recover_software:string%20%3F;trnas:integer%20%3F;trna_ext_software:string%20%3F;compl_score:compl_score_enum;compl_software:string;compl_appr:compl_appr_enum%20%3F;contam_score:string;contam_screen_input:string%20%3F;contam_screen_param:contam_screen_param_enum%20%3F;decontam_software:decontam_software_enum%20%3F;sort_tech:sort_tech_enum;single_cell_lysis_appr:single_cell_lysis_appr_enum;single_cell_lysis_prot:string%20%3F;wga_amp_appr:string;wga_amp_kit:string%20%3F;associated_resource:string%20%3F;sop:string%20%3F],[QuantityValue]<samp_size%200..1-++[MISAG],[WaterMISAG]uses%20-.->[MISAG],[WastewaterSludgeMISAG]uses%20-.->[MISAG],[SoilMISAG]uses%20-.->[MISAG],[SedimentMISAG]uses%20-.->[MISAG],[Plant-associatedMISAG]uses%20-.->[MISAG],[MiscellaneousNaturalOrArtificialEnvironmentMISAG]uses%20-.->[MISAG],[MicrobialMatBiofilmMISAG]uses%20-.->[MISAG],[HydrocarbonResources-fluidsSwabsMISAG]uses%20-.->[MISAG],[HydrocarbonResources-coresMISAG]uses%20-.->[MISAG],[Human-vaginalMISAG]uses%20-.->[MISAG],[Human-skinMISAG]uses%20-.->[MISAG],[Human-oralMISAG]uses%20-.->[MISAG],[Human-gutMISAG]uses%20-.->[MISAG],[Human-associatedMISAG]uses%20-.->[MISAG],[Host-associatedMISAG]uses%20-.->[MISAG],[BuiltEnvironmentMISAG]uses%20-.->[MISAG],[AirMISAG]uses%20-.->[MISAG],[WaterMISAG],[WastewaterSludgeMISAG],[SoilMISAG],[SedimentMISAG],[Plant-associatedMISAG],[MiscellaneousNaturalOrArtificialEnvironmentMISAG],[MicrobialMatBiofilmMISAG],[HydrocarbonResources-fluidsSwabsMISAG],[HydrocarbonResources-coresMISAG],[Human-vaginalMISAG],[Human-skinMISAG],[Human-oralMISAG],[Human-gutMISAG],[Human-associatedMISAG],[Host-associatedMISAG],[BuiltEnvironmentMISAG],[AirMISAG])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<samp_vol_we_dna_ext%200..1-++[MISAG&#124;submitted_to_insdc:string;investigation_type:investigation_type_enum;samp_name:string;samp_taxon_id:string;project_name:string;experimental_factor:string%20%3F;lat_lon:string;geo_loc_name:string;collection_date:date;neg_cont_type:neg_cont_type_enum%20%3F;pos_cont_type:string%20%3F;env_broad_scale:string;env_local_scale:string;env_medium:string;env_package:env_package_enum%20%3F;ref_biomaterial:string%20%3F;source_mat_id:string%20%3F;rel_to_oxygen:rel_to_oxygen_enum%20%3F;samp_collec_device:string%20%3F;samp_collec_method:string%20%3F;samp_mat_process:string%20%3F;size_frac:string%20%3F;nucl_acid_ext:string%20%3F;nucl_acid_amp:string%20%3F;lib_size:integer%20%3F;lib_reads_seqd:integer%20%3F;lib_layout:lib_layout_enum%20%3F;lib_vector:string%20%3F;lib_screen:string%20%3F;mid:string%20%3F;adapters:string%20%3F;seq_meth:string;tax_ident:tax_ident_enum;assembly_qual:assembly_qual_enum;assembly_name:string%20%3F;assembly_software:string;annot:string%20%3F;number_contig:integer%20%3F;feat_pred:string%20%3F;ref_db:string%20%3F;sim_search_meth:string%20%3F;tax_class:string%20%3F;x_16s_recover:string%20%3F;x_16s_recover_software:string%20%3F;trnas:integer%20%3F;trna_ext_software:string%20%3F;compl_score:compl_score_enum;compl_software:string;compl_appr:compl_appr_enum%20%3F;contam_score:string;contam_screen_input:string%20%3F;contam_screen_param:contam_screen_param_enum%20%3F;decontam_software:decontam_software_enum%20%3F;sort_tech:sort_tech_enum;single_cell_lysis_appr:single_cell_lysis_appr_enum;single_cell_lysis_prot:string%20%3F;wga_amp_appr:string;wga_amp_kit:string%20%3F;associated_resource:string%20%3F;sop:string%20%3F],[QuantityValue]<samp_size%200..1-++[MISAG],[WaterMISAG]uses%20-.->[MISAG],[WastewaterSludgeMISAG]uses%20-.->[MISAG],[SoilMISAG]uses%20-.->[MISAG],[SedimentMISAG]uses%20-.->[MISAG],[Plant-associatedMISAG]uses%20-.->[MISAG],[MiscellaneousNaturalOrArtificialEnvironmentMISAG]uses%20-.->[MISAG],[MicrobialMatBiofilmMISAG]uses%20-.->[MISAG],[HydrocarbonResources-fluidsSwabsMISAG]uses%20-.->[MISAG],[HydrocarbonResources-coresMISAG]uses%20-.->[MISAG],[Human-vaginalMISAG]uses%20-.->[MISAG],[Human-skinMISAG]uses%20-.->[MISAG],[Human-oralMISAG]uses%20-.->[MISAG],[Human-gutMISAG]uses%20-.->[MISAG],[Human-associatedMISAG]uses%20-.->[MISAG],[Host-associatedMISAG]uses%20-.->[MISAG],[BuiltEnvironmentMISAG]uses%20-.->[MISAG],[AirMISAG]uses%20-.->[MISAG],[WaterMISAG],[WastewaterSludgeMISAG],[SoilMISAG],[SedimentMISAG],[Plant-associatedMISAG],[MiscellaneousNaturalOrArtificialEnvironmentMISAG],[MicrobialMatBiofilmMISAG],[HydrocarbonResources-fluidsSwabsMISAG],[HydrocarbonResources-coresMISAG],[Human-vaginalMISAG],[Human-skinMISAG],[Human-oralMISAG],[Human-gutMISAG],[Human-associatedMISAG],[Host-associatedMISAG],[BuiltEnvironmentMISAG],[AirMISAG])

## Mixin for

 * [AirMISAG](AirMISAG.md) (mixin)  - Combinatorial checklist Minimum Information About a Single Amplified Genome with environmental package air
 * [BuiltEnvironmentMISAG](BuiltEnvironmentMISAG.md) (mixin)  - Combinatorial checklist Minimum Information About a Single Amplified Genome with environmental package built environment
 * [Host-associatedMISAG](Host-associatedMISAG.md) (mixin)  - Combinatorial checklist Minimum Information About a Single Amplified Genome with environmental package host-associated
 * [Human-associatedMISAG](Human-associatedMISAG.md) (mixin)  - Combinatorial checklist Minimum Information About a Single Amplified Genome with environmental package human-associated
 * [Human-gutMISAG](Human-gutMISAG.md) (mixin)  - Combinatorial checklist Minimum Information About a Single Amplified Genome with environmental package human-gut
 * [Human-oralMISAG](Human-oralMISAG.md) (mixin)  - Combinatorial checklist Minimum Information About a Single Amplified Genome with environmental package human-oral
 * [Human-skinMISAG](Human-skinMISAG.md) (mixin)  - Combinatorial checklist Minimum Information About a Single Amplified Genome with environmental package human-skin
 * [Human-vaginalMISAG](Human-vaginalMISAG.md) (mixin)  - Combinatorial checklist Minimum Information About a Single Amplified Genome with environmental package human-vaginal
 * [HydrocarbonResources-coresMISAG](HydrocarbonResources-coresMISAG.md) (mixin)  - Combinatorial checklist Minimum Information About a Single Amplified Genome with environmental package hydrocarbon resources-cores
 * [HydrocarbonResources-fluidsSwabsMISAG](HydrocarbonResources-fluidsSwabsMISAG.md) (mixin)  - Combinatorial checklist Minimum Information About a Single Amplified Genome with environmental package hydrocarbon resources-fluids_swabs
 * [MicrobialMatBiofilmMISAG](MicrobialMatBiofilmMISAG.md) (mixin)  - Combinatorial checklist Minimum Information About a Single Amplified Genome with environmental package microbial mat_biofilm
 * [MiscellaneousNaturalOrArtificialEnvironmentMISAG](MiscellaneousNaturalOrArtificialEnvironmentMISAG.md) (mixin)  - Combinatorial checklist Minimum Information About a Single Amplified Genome with environmental package miscellaneous natural or artificial environment
 * [Plant-associatedMISAG](Plant-associatedMISAG.md) (mixin)  - Combinatorial checklist Minimum Information About a Single Amplified Genome with environmental package plant-associated
 * [SedimentMISAG](SedimentMISAG.md) (mixin)  - Combinatorial checklist Minimum Information About a Single Amplified Genome with environmental package sediment
 * [SoilMISAG](SoilMISAG.md) (mixin)  - Combinatorial checklist Minimum Information About a Single Amplified Genome with environmental package soil
 * [WastewaterSludgeMISAG](WastewaterSludgeMISAG.md) (mixin)  - Combinatorial checklist Minimum Information About a Single Amplified Genome with environmental package wastewater_sludge
 * [WaterMISAG](WaterMISAG.md) (mixin)  - Combinatorial checklist Minimum Information About a Single Amplified Genome with environmental package water

## Referenced by Class


## Attributes


### Own

 * [MISAG➞submitted_to_insdc](MISAG_submitted_to_insdc.md)  <sub>1..1</sub>
     * Description: Depending on the study (large-scale e.g. done with next generation sequencing technology, or small-scale) sequences have to be submitted to SRA (Sequence Read Archive), DRA (DDBJ Read Archive) or via the classical Webin/Sequin systems to Genbank, ENA and DDBJ. Although this field is mandatory, it is meant as a self-test field, therefore it is not necessary to include this field in contextual data submitted to databases
     * Range: [String](types/String.md)
     * Example: yes None
 * [MISAG➞investigation_type](MISAG_investigation_type.md)  <sub>1..1</sub>
     * Description: Nucleic Acid Sequence Report is the root element of all MIGS/MIMS compliant reports as standardized by Genomic Standards Consortium. This field is either eukaryote,bacteria,virus,plasmid,organelle, metagenome,mimarks-survey, mimarks-specimen, metatranscriptome, single amplified genome, metagenome-assembled genome, or uncultivated viral genome
     * Range: [investigation_type_enum](investigation_type_enum.md)
     * Example: metagenome None
 * [MISAG➞samp_name](MISAG_samp_name.md)  <sub>1..1</sub>
     * Description: A local identifier or name that for the material sample used for extracting nucleic acids, and subsequent sequencing. It can refer either to the original material collected or to any derived sub-samples. It can have any format, but we suggest that you make it concise, unique and consistent within your lab, and as informative as possible. INSDC requires every sample name from a single Submitter to be unique. Use of a globally unique identifier for the field source_mat_id is recommended in addition to sample_name.
     * Range: [String](types/String.md)
     * Example: ISDsoil1 None
 * [MISAG➞samp_taxon_id](MISAG_samp_taxon_id.md)  <sub>1..1</sub>
     * Description: NCBI taxon id of the sample.  Maybe be a single taxon or mixed taxa sample. Use 'synthetic metagenome’ for mock community/positive controls, or 'blank sample' for negative controls.
     * Range: [String](types/String.md)
     * Example: Gut Metagenome [NCBI:txid749906] None
 * [MISAG➞project_name](MISAG_project_name.md)  <sub>1..1</sub>
     * Description: Name of the project within which the sequencing was organized
     * Range: [String](types/String.md)
     * Example: Forest soil metagenome None
 * [MISAG➞experimental_factor](MISAG_experimental_factor.md)  <sub>0..1</sub>
     * Description: Experimental factors are essentially the variable aspects of an experiment design which can be used to describe an experiment, or set of experiments, in an increasingly detailed manner. This field accepts ontology terms from Experimental Factor Ontology (EFO) and/or Ontology for Biomedical Investigations (OBI). For a browser of EFO (v 2.95) terms, please see http://purl.bioontology.org/ontology/EFO; for a browser of OBI (v 2018-02-12) terms please see http://purl.bioontology.org/ontology/OBI
     * Range: [String](types/String.md)
     * Example: time series design [EFO:EFO_0001779] None
 * [MISAG➞lat_lon](MISAG_lat_lon.md)  <sub>1..1</sub>
     * Description: The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in WGS84 system
     * Range: [String](types/String.md)
     * Example: 50.586825 6.408977 None
 * [MISAG➞geo_loc_name](MISAG_geo_loc_name.md)  <sub>1..1</sub>
     * Description: The geographical origin of the sample as defined by the country or sea name followed by specific region name. Country or sea names should be chosen from the INSDC country list (http://insdc.org/country.html), or the GAZ ontology (http://purl.bioontology.org/ontology/GAZ)
     * Range: [String](types/String.md)
     * Example: USA: Maryland, Bethesda None
 * [MISAG➞collection_date](MISAG_collection_date.md)  <sub>1..1</sub>
     * Description: The time of sampling, either as an instance (single point in time) or interval. In case no exact time is available, the date/time can be right truncated i.e. all of these are valid times: 2008-01-23T19:23:10+00:00; 2008-01-23T19:23:10; 2008-01-23; 2008-01; 2008; Except: 2008-01; 2008 all are ISO8601 compliant
     * Range: [Date](types/Date.md)
     * Example: 2018-05-11T10:00:00+01:00; 2018-05-11 None
 * [MISAG➞neg_cont_type](MISAG_neg_cont_type.md)  <sub>0..1</sub>
     * Description: The substance or equipment used as a negative control in an investigation
     * Range: [neg_cont_type_enum](neg_cont_type_enum.md)
     * Example:  None
 * [MISAG➞pos_cont_type](MISAG_pos_cont_type.md)  <sub>0..1</sub>
     * Description: The substance, mixture, product, or apparatus used to verify that a process which is part of an investigation delivers a true positive.
     * Range: [String](types/String.md)
     * Example:  None
 * [MISAG➞env_broad_scale](MISAG_env_broad_scale.md)  <sub>1..1</sub>
     * Description: Report the major environmental system the sample or specimen came from. The system(s) identified should have a coarse spatial grain, to provide the general environmental context of where the sampling was done (e.g. in the desert or a rainforest). We recommend using subclasses of EnvO’s biome class:  http://purl.obolibrary.org/obo/ENVO_00000428. EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
     * Range: [String](types/String.md)
     * Example: oceanic epipelagic zone biome [ENVO:01000033] for annotating a water sample from the photic zone in middle of the Atlantic Ocean None
 * [MISAG➞env_local_scale](MISAG_env_local_scale.md)  <sub>1..1</sub>
     * Description: Report the entity or entities which are in the sample or specimen’s local vicinity and which you believe have significant causal influences on your sample or specimen. We recommend using EnvO terms which are of smaller spatial grain than your entry for env_broad_scale. Terms, such as anatomical sites, from other OBO Library ontologies which interoperate with EnvO (e.g. UBERON) are accepted in this field. EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS.
     * Range: [String](types/String.md)
     * Example: litter layer [ENVO:01000338]; Annotating a pooled sample taken from various vegetation layers in a forest consider: canopy [ENVO:00000047]|herb and fern layer [ENVO:01000337]|litter layer [ENVO:01000338]|understory [01000335]|shrub layer [ENVO:01000336]. None
 * [MISAG➞env_medium](MISAG_env_medium.md)  <sub>1..1</sub>
     * Description: Report the environmental material(s) immediately surrounding the sample or specimen at the time of sampling. We recommend using subclasses of 'environmental material' (http://purl.obolibrary.org/obo/ENVO_00010483). EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS . Terms from other OBO ontologies are permissible as long as they reference mass/volume nouns (e.g. air, water, blood) and not discrete, countable entities (e.g. a tree, a leaf, a table top).
     * Range: [String](types/String.md)
     * Example: soil [ENVO:00001998]; Annotating a fish swimming in the upper 100 m of the Atlantic Ocean, consider: ocean water [ENVO:00002151]. Example: Annotating a duck on a pond consider: pond water [ENVO:00002228]|air [ENVO_00002005] None
 * [MISAG➞env_package](MISAG_env_package.md)  <sub>0..1</sub>
     * Description: MIxS extension for reporting of measurements and observations obtained from one or more of the environments where the sample was obtained. All environmental packages listed here are further defined in separate subtables. By giving the name of the environmental package, a selection of fields can be made from the subtables and can be reported
     * Range: [env_package_enum](env_package_enum.md)
     * Example: soil None
 * [MISAG➞ref_biomaterial](MISAG_ref_biomaterial.md)  <sub>0..1</sub>
     * Description: Primary publication if isolated before genome publication; otherwise, primary genome report.
     * Range: [String](types/String.md)
     * Example: doi:10.1016/j.syapm.2018.01.009 None
 * [MISAG➞source_mat_id](MISAG_source_mat_id.md)  <sub>0..1</sub>
     * Description: A unique identifier assigned to a material sample (as defined by http://rs.tdwg.org/dwc/terms/materialSampleID, and as opposed to a particular digital record of a material sample) used for extracting nucleic acids, and subsequent sequencing. The identifier can refer either to the original material collected or to any derived sub-samples. The INSDC qualifiers /specimen_voucher, /bio_material, or /culture_collection may or may not share the same value as the source_mat_id field. For instance, the /specimen_voucher qualifier and source_mat_id may both contain 'UAM:Herps:14' , referring to both the specimen voucher and sampled tissue with the same identifier. However, the /culture_collection qualifier may refer to a value from an initial culture (e.g. ATCC:11775) while source_mat_id would refer to an identifier from some derived culture from which the nucleic acids were extracted (e.g. xatc123 or ark:/2154/R2).
     * Range: [String](types/String.md)
     * Example: MPI012345 None
 * [MISAG➞rel_to_oxygen](MISAG_rel_to_oxygen.md)  <sub>0..1</sub>
     * Description: Is this organism an aerobe, anaerobe? Please note that aerobic and anaerobic are valid descriptors for microbial environments
     * Range: [rel_to_oxygen_enum](rel_to_oxygen_enum.md)
     * Example: aerobe None
 * [MISAG➞samp_collec_device](MISAG_samp_collec_device.md)  <sub>0..1</sub>
     * Description: The device used to collect an environmental sample. This field accepts terms listed under environmental sampling device (http://purl.obolibrary.org/obo/ENVO). This field also accepts terms listed under specimen collection device (http://purl.obolibrary.org/obo/GENEPIO_0002094).
     * Range: [String](types/String.md)
     * Example: swab, biopsy, niskin bottle, push core, drag swab [GENEPIO:0002713] None
 * [MISAG➞samp_collec_method](MISAG_samp_collec_method.md)  <sub>0..1</sub>
     * Description: The method employed for collecting the sample.
     * Range: [String](types/String.md)
     * Example: swabbing None
 * [MISAG➞samp_mat_process](MISAG_samp_mat_process.md)  <sub>0..1</sub>
     * Description: A brief description of any processing applied to the sample during or after retrieving the sample from environment, or a link to the relevant protocol(s) performed.
     * Range: [String](types/String.md)
     * Example: filtering of seawater, storing samples in ethanol None
 * [MISAG➞size_frac](MISAG_size_frac.md)  <sub>0..1</sub>
     * Description: Filtering pore size used in sample preparation
     * Range: [String](types/String.md)
     * Example: 0-0.22 micrometer None
 * [MISAG➞samp_size](MISAG_samp_size.md)  <sub>0..1</sub>
     * Description: The total amount or size (volume (ml), mass (g) or area (m2) ) of sample collected.
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 5 liter None
 * [MISAG➞samp_vol_we_dna_ext](MISAG_samp_vol_we_dna_ext.md)  <sub>0..1</sub>
     * Description: Volume (ml) or mass (g) of total collected sample processed for DNA extraction. Note: total sample collected should be entered under the term Sample Size (MIXS:0000001).
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 1500 milliliter None
 * [MISAG➞nucl_acid_ext](MISAG_nucl_acid_ext.md)  <sub>0..1</sub>
     * Description: A link to a literature reference, electronic resource or a standard operating procedure (SOP), that describes the material separation to recover the nucleic acid fraction from a sample
     * Range: [String](types/String.md)
     * Example: https://mobio.com/media/wysiwyg/pdfs/protocols/12888.pdf None
 * [MISAG➞nucl_acid_amp](MISAG_nucl_acid_amp.md)  <sub>0..1</sub>
     * Description: A link to a literature reference, electronic resource or a standard operating procedure (SOP), that describes the enzymatic amplification (PCR, TMA, NASBA) of specific nucleic acids
     * Range: [String](types/String.md)
     * Example: https://phylogenomics.me/protocols/16s-pcr-protocol/ None
 * [MISAG➞lib_size](MISAG_lib_size.md)  <sub>0..1</sub>
     * Description: Total number of clones in the library prepared for the project
     * Range: [Integer](types/Integer.md)
     * Example: 50 None
 * [MISAG➞lib_reads_seqd](MISAG_lib_reads_seqd.md)  <sub>0..1</sub>
     * Description: Total number of clones sequenced from the library
     * Range: [Integer](types/Integer.md)
     * Example: 20 None
 * [MISAG➞lib_layout](MISAG_lib_layout.md)  <sub>0..1</sub>
     * Description: Specify whether to expect single, paired, or other configuration of reads
     * Range: [lib_layout_enum](lib_layout_enum.md)
     * Example: paired None
 * [MISAG➞lib_vector](MISAG_lib_vector.md)  <sub>0..1</sub>
     * Description: Cloning vector type(s) used in construction of libraries
     * Range: [String](types/String.md)
     * Example: Bacteriophage P1 None
 * [MISAG➞lib_screen](MISAG_lib_screen.md)  <sub>0..1</sub>
     * Description: Specific enrichment or screening methods applied before and/or after creating libraries
     * Range: [String](types/String.md)
     * Example: enriched, screened, normalized None
 * [MISAG➞mid](MISAG_mid.md)  <sub>0..1</sub>
     * Description: Molecular barcodes, called Multiplex Identifiers (MIDs), that are used to specifically tag unique samples in a sequencing run. Sequence should be reported in uppercase letters
     * Range: [String](types/String.md)
     * Example: GTGAATAT None
 * [MISAG➞adapters](MISAG_adapters.md)  <sub>0..1</sub>
     * Description: Adapters provide priming sequences for both amplification and sequencing of the sample-library fragments. Both adapters should be reported; in uppercase letters
     * Range: [String](types/String.md)
     * Example: AATGATACGGCGACCACCGAGATCTACACGCT;CAAGCAGAAGACGGCATACGAGAT None
 * [MISAG➞seq_meth](MISAG_seq_meth.md)  <sub>1..1</sub>
     * Description: Sequencing machine used. Where possible the term should be taken from the OBI list of DNA sequencers (http://purl.obolibrary.org/obo/OBI_0400103).
     * Range: [String](types/String.md)
     * Example: 454 Genome Sequencer FLX [OBI:0000702] None
 * [MISAG➞tax_ident](MISAG_tax_ident.md)  <sub>1..1</sub>
     * Description: The phylogenetic marker(s) used to assign an organism name to the SAG or MAG
     * Range: [tax_ident_enum](tax_ident_enum.md)
     * Example: other: rpoB gene None
 * [MISAG➞assembly_qual](MISAG_assembly_qual.md)  <sub>1..1</sub>
     * Description: The assembly quality category is based on sets of criteria outlined for each assembly quality category. For MISAG/MIMAG; Finished: Single, validated, contiguous sequence per replicon without gaps or ambiguities with a consensus error rate equivalent to Q50 or better. High Quality Draft:Multiple fragments where gaps span repetitive regions. Presence of the 23S, 16S and 5S rRNA genes and at least 18 tRNAs. Medium Quality Draft:Many fragments with little to no review of assembly other than reporting of standard assembly statistics. Low Quality Draft:Many fragments with little to no review of assembly other than reporting of standard assembly statistics. Assembly statistics include, but are not limited to total assembly size, number of contigs, contig N50/L50, and maximum contig length. For MIUVIG; Finished: Single, validated, contiguous sequence per replicon without gaps or ambiguities, with extensive manual review and editing to annotate putative gene functions and transcriptional units. High-quality draft genome: One or multiple fragments, totaling ≥ 90% of the expected genome or replicon sequence or predicted complete. Genome fragment(s): One or multiple fragments, totalling < 90% of the expected genome or replicon sequence, or for which no genome size could be estimated
     * Range: [assembly_qual_enum](assembly_qual_enum.md)
     * Example: High-quality draft genome None
 * [MISAG➞assembly_name](MISAG_assembly_name.md)  <sub>0..1</sub>
     * Description: Name/version of the assembly provided by the submitter that is used in the genome browsers and in the community
     * Range: [String](types/String.md)
     * Example: HuRef, JCVI_ISG_i3_1.0 None
 * [MISAG➞assembly_software](MISAG_assembly_software.md)  <sub>1..1</sub>
     * Description: Tool(s) used for assembly, including version number and parameters
     * Range: [String](types/String.md)
     * Example: metaSPAdes;3.11.0;kmer set 21,33,55,77,99,121, default parameters otherwise None
 * [MISAG➞annot](MISAG_annot.md)  <sub>0..1</sub>
     * Description: Tool used for annotation, or for cases where annotation was provided by a community jamboree or model organism database rather than by a specific submitter
     * Range: [String](types/String.md)
     * Example: prokka None
 * [MISAG➞number_contig](MISAG_number_contig.md)  <sub>0..1</sub>
     * Description: Total number of contigs in the cleaned/submitted assembly that makes up a given genome, SAG, MAG, or UViG
     * Range: [Integer](types/Integer.md)
     * Example: 40 None
 * [MISAG➞feat_pred](MISAG_feat_pred.md)  <sub>0..1</sub>
     * Description: Method used to predict UViGs features such as ORFs, integration site, etc.
     * Range: [String](types/String.md)
     * Example: Prodigal;2.6.3;default parameters None
 * [MISAG➞ref_db](MISAG_ref_db.md)  <sub>0..1</sub>
     * Description: List of database(s) used for ORF annotation, along with version number and reference to website or publication
     * Range: [String](types/String.md)
     * Example: pVOGs;5;http://dmk-brain.ecn.uiowa.edu/pVOGs/ Grazziotin et al. 2017 doi:10.1093/nar/gkw975 None
 * [MISAG➞sim_search_meth](MISAG_sim_search_meth.md)  <sub>0..1</sub>
     * Description: Tool used to compare ORFs with database, along with version and cutoffs used
     * Range: [String](types/String.md)
     * Example: HMMER3;3.1b2;hmmsearch, cutoff of 50 on score None
 * [MISAG➞tax_class](MISAG_tax_class.md)  <sub>0..1</sub>
     * Description: Method used for taxonomic classification, along with reference database used, classification rank, and thresholds used to classify new genomes
     * Range: [String](types/String.md)
     * Example: vConTACT vContact2 (references from NCBI RefSeq v83, genus rank classification, default parameters) None
 * [MISAG➞x_16s_recover](MISAG_x_16s_recover.md)  <sub>0..1</sub>
     * Description: Can a 16S gene be recovered from the submitted SAG or MAG?
     * Range: [String](types/String.md)
     * Example: yes None
 * [MISAG➞x_16s_recover_software](MISAG_x_16s_recover_software.md)  <sub>0..1</sub>
     * Description: Tools used for 16S rRNA gene extraction
     * Range: [String](types/String.md)
     * Example: rambl;v2;default parameters None
 * [MISAG➞trnas](MISAG_trnas.md)  <sub>0..1</sub>
     * Description: The total number of tRNAs identified from the SAG or MAG
     * Range: [Integer](types/Integer.md)
     * Example: 18 None
 * [MISAG➞trna_ext_software](MISAG_trna_ext_software.md)  <sub>0..1</sub>
     * Description: Tools used for tRNA identification
     * Range: [String](types/String.md)
     * Example: infernal;v2;default parameters None
 * [MISAG➞compl_score](MISAG_compl_score.md)  <sub>1..1</sub>
     * Description: Completeness score is typically based on either the fraction of markers found as compared to a database or the percent of a genome found as compared to a closely related reference genome. High Quality Draft: >90%, Medium Quality Draft: >50%, and Low Quality Draft: < 50% should have the indicated completeness scores
     * Range: [compl_score_enum](compl_score_enum.md)
     * Example: med;60% None
 * [MISAG➞compl_software](MISAG_compl_software.md)  <sub>1..1</sub>
     * Description: Tools used for completion estimate, i.e. checkm, anvi'o, busco
     * Range: [String](types/String.md)
     * Example: checkm None
 * [MISAG➞compl_appr](MISAG_compl_appr.md)  <sub>0..1</sub>
     * Description: The approach used to determine the completeness of a given genomic assembly, which would typically make use of a set of conserved marker genes or a closely related reference genome. For UViG completeness, include reference genome or group used, and contig feature suggesting a complete genome
     * Range: [compl_appr_enum](compl_appr_enum.md)
     * Example: other: UViG length compared to the average length of reference genomes from the P22virus genus (NCBI RefSeq v83) None
 * [MISAG➞contam_score](MISAG_contam_score.md)  <sub>1..1</sub>
     * Description: The contamination score is based on the fraction of single-copy genes that are observed more than once in a query genome. The following scores are acceptable for; High Quality Draft: < 5%, Medium Quality Draft: < 10%, Low Quality Draft: < 10%. Contamination must be below 5% for a SAG or MAG to be deposited into any of the public databases
     * Range: [String](types/String.md)
     * Example: 1% None
 * [MISAG➞contam_screen_input](MISAG_contam_screen_input.md)  <sub>0..1</sub>
     * Description: The type of sequence data used as input
     * Range: [String](types/String.md)
     * Example: contigs None
 * [MISAG➞contam_screen_param](MISAG_contam_screen_param.md)  <sub>0..1</sub>
     * Description: Specific parameters used in the decontamination sofware, such as reference database, coverage, and kmers. Combinations of these parameters may also be used, i.e. kmer and coverage, or reference database and kmer
     * Range: [contam_screen_param_enum](contam_screen_param_enum.md)
     * Example: kmer None
 * [MISAG➞decontam_software](MISAG_decontam_software.md)  <sub>0..1</sub>
     * Description: Tool(s) used in contamination screening
     * Range: [decontam_software_enum](decontam_software_enum.md)
     * Example: anvi'o None
 * [MISAG➞sort_tech](MISAG_sort_tech.md)  <sub>1..1</sub>
     * Description: Method used to sort/isolate cells or particles of interest
     * Range: [sort_tech_enum](sort_tech_enum.md)
     * Example: optical manipulation None
 * [MISAG➞single_cell_lysis_appr](MISAG_single_cell_lysis_appr.md)  <sub>1..1</sub>
     * Description: Method used to free DNA from interior of the cell(s) or particle(s)
     * Range: [single_cell_lysis_appr_enum](single_cell_lysis_appr_enum.md)
     * Example: enzymatic None
 * [MISAG➞single_cell_lysis_prot](MISAG_single_cell_lysis_prot.md)  <sub>0..1</sub>
     * Description: Name of the kit or standard protocol used for cell(s) or particle(s) lysis
     * Range: [String](types/String.md)
     * Example: ambion single cell lysis kit None
 * [MISAG➞wga_amp_appr](MISAG_wga_amp_appr.md)  <sub>1..1</sub>
     * Description: Method used to amplify genomic DNA in preparation for sequencing
     * Range: [String](types/String.md)
     * Example: mda based None
 * [MISAG➞wga_amp_kit](MISAG_wga_amp_kit.md)  <sub>0..1</sub>
     * Description: Kit used to amplify genomic DNA in preparation for sequencing
     * Range: [String](types/String.md)
     * Example: qiagen repli-g None
 * [MISAG➞associated resource](MISAG_associated_resource.md)  <sub>0..1</sub>
     * Description: A related resource that is referenced, cited, or otherwise associated to the sequence.
     * Range: [String](types/String.md)
     * Example: http://www.earthmicrobiome.org/ None
 * [MISAG➞sop](MISAG_sop.md)  <sub>0..1</sub>
     * Description: Standard operating procedures used in assembly and/or annotation of genomes, metagenomes or environmental sequences
     * Range: [String](types/String.md)
     * Example: http://press.igsb.anl.gov/earthmicrobiome/protocols-and-standards/its/ None

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | MISAG |

