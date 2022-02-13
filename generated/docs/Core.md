
# Class: core


Core package. Do not use this directly, this is used to build other packages

URI: [mixs.vocab:Core](https://w3id.org/mixs/vocab/Core)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<samp_vol_we_dna_ext%200..1-++[Core&#124;submitted_to_insdc:string%20%3F;investigation_type:investigation_type_enum%20%3F;samp_name:string%20%3F;samp_taxon_id:string%20%3F;project_name:string%20%3F;experimental_factor:string%20%3F;lat_lon:string%20%3F;geo_loc_name:string%20%3F;collection_date:date%20%3F;neg_cont_type:neg_cont_type_enum%20%3F;pos_cont_type:string%20%3F;env_broad_scale:string%20%3F;env_local_scale:string%20%3F;env_medium:string%20%3F;env_package:env_package_enum%20%3F;subspecf_gen_lin:string%20%3F;ploidy:string%20%3F;num_replicons:integer%20%3F;extrachrom_elements:integer%20%3F;estimated_size:string%20%3F;ref_biomaterial:string%20%3F;source_mat_id:string%20%3F;pathogenicity:string%20%3F;biotic_relationship:biotic_relationship_enum%20%3F;specific_host:string%20%3F;host_spec_range:integer%20%3F;health_disease_stat:health_disease_stat_enum%20%3F;host_disease_stat:string%20%3F;trophic_level:trophic_level_enum%20%3F;propagation:string%20%3F;encoded_traits:string%20%3F;rel_to_oxygen:rel_to_oxygen_enum%20%3F;isol_growth_condt:string%20%3F;samp_collec_device:string%20%3F;samp_collec_method:string%20%3F;samp_mat_process:string%20%3F;size_frac:string%20%3F;source_uvig:source_uvig_enum%20%3F;virus_enrich_appr:virus_enrich_appr_enum%20%3F;nucl_acid_ext:string%20%3F;nucl_acid_amp:string%20%3F;lib_size:integer%20%3F;lib_reads_seqd:integer%20%3F;lib_layout:lib_layout_enum%20%3F;lib_vector:string%20%3F;lib_screen:string%20%3F;target_gene:string%20%3F;target_subfragment:string%20%3F;pcr_primers:string%20%3F;mid:string%20%3F;adapters:string%20%3F;pcr_cond:string%20%3F;seq_meth:string%20%3F;seq_quality_check:string%20%3F;chimera_check:string%20%3F;tax_ident:tax_ident_enum%20%3F;assembly_qual:assembly_qual_enum%20%3F;assembly_name:string%20%3F;assembly_software:string%20%3F;annot:string%20%3F;number_contig:integer%20%3F;feat_pred:string%20%3F;ref_db:string%20%3F;sim_search_meth:string%20%3F;tax_class:string%20%3F;x_16s_recover:string%20%3F;x_16s_recover_software:string%20%3F;trnas:integer%20%3F;trna_ext_software:string%20%3F;compl_score:compl_score_enum%20%3F;compl_software:string%20%3F;compl_appr:compl_appr_enum%20%3F;contam_score:string%20%3F;contam_screen_input:string%20%3F;contam_screen_param:contam_screen_param_enum%20%3F;decontam_software:decontam_software_enum%20%3F;sort_tech:sort_tech_enum%20%3F;single_cell_lysis_appr:single_cell_lysis_appr_enum%20%3F;single_cell_lysis_prot:string%20%3F;wga_amp_appr:string%20%3F;wga_amp_kit:string%20%3F;bin_param:bin_param_enum%20%3F;bin_software:string%20%3F;reassembly_bin:string%20%3F;mag_cov_software:mag_cov_software_enum%20%3F;vir_ident_software:string%20%3F;pred_genome_type:pred_genome_type_enum%20%3F;pred_genome_struc:pred_genome_struc_enum%20%3F;detec_type:string%20%3F;otu_class_appr:string%20%3F;otu_seq_comp_appr:string%20%3F;otu_db:string%20%3F;host_pred_appr:host_pred_appr_enum%20%3F;host_pred_est_acc:string%20%3F;associated_resource:string%20%3F;sop:string%20%3F],[QuantityValue]<samp_size%200..1-++[Core],[QuantityValue]<temp%200..1-++[Core],[QuantityValue]<elev%200..1-++[Core],[QuantityValue]<alt%200..1-++[Core],[QuantityValue]<depth%200..1-++[Core])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<samp_vol_we_dna_ext%200..1-++[Core&#124;submitted_to_insdc:string%20%3F;investigation_type:investigation_type_enum%20%3F;samp_name:string%20%3F;samp_taxon_id:string%20%3F;project_name:string%20%3F;experimental_factor:string%20%3F;lat_lon:string%20%3F;geo_loc_name:string%20%3F;collection_date:date%20%3F;neg_cont_type:neg_cont_type_enum%20%3F;pos_cont_type:string%20%3F;env_broad_scale:string%20%3F;env_local_scale:string%20%3F;env_medium:string%20%3F;env_package:env_package_enum%20%3F;subspecf_gen_lin:string%20%3F;ploidy:string%20%3F;num_replicons:integer%20%3F;extrachrom_elements:integer%20%3F;estimated_size:string%20%3F;ref_biomaterial:string%20%3F;source_mat_id:string%20%3F;pathogenicity:string%20%3F;biotic_relationship:biotic_relationship_enum%20%3F;specific_host:string%20%3F;host_spec_range:integer%20%3F;health_disease_stat:health_disease_stat_enum%20%3F;host_disease_stat:string%20%3F;trophic_level:trophic_level_enum%20%3F;propagation:string%20%3F;encoded_traits:string%20%3F;rel_to_oxygen:rel_to_oxygen_enum%20%3F;isol_growth_condt:string%20%3F;samp_collec_device:string%20%3F;samp_collec_method:string%20%3F;samp_mat_process:string%20%3F;size_frac:string%20%3F;source_uvig:source_uvig_enum%20%3F;virus_enrich_appr:virus_enrich_appr_enum%20%3F;nucl_acid_ext:string%20%3F;nucl_acid_amp:string%20%3F;lib_size:integer%20%3F;lib_reads_seqd:integer%20%3F;lib_layout:lib_layout_enum%20%3F;lib_vector:string%20%3F;lib_screen:string%20%3F;target_gene:string%20%3F;target_subfragment:string%20%3F;pcr_primers:string%20%3F;mid:string%20%3F;adapters:string%20%3F;pcr_cond:string%20%3F;seq_meth:string%20%3F;seq_quality_check:string%20%3F;chimera_check:string%20%3F;tax_ident:tax_ident_enum%20%3F;assembly_qual:assembly_qual_enum%20%3F;assembly_name:string%20%3F;assembly_software:string%20%3F;annot:string%20%3F;number_contig:integer%20%3F;feat_pred:string%20%3F;ref_db:string%20%3F;sim_search_meth:string%20%3F;tax_class:string%20%3F;x_16s_recover:string%20%3F;x_16s_recover_software:string%20%3F;trnas:integer%20%3F;trna_ext_software:string%20%3F;compl_score:compl_score_enum%20%3F;compl_software:string%20%3F;compl_appr:compl_appr_enum%20%3F;contam_score:string%20%3F;contam_screen_input:string%20%3F;contam_screen_param:contam_screen_param_enum%20%3F;decontam_software:decontam_software_enum%20%3F;sort_tech:sort_tech_enum%20%3F;single_cell_lysis_appr:single_cell_lysis_appr_enum%20%3F;single_cell_lysis_prot:string%20%3F;wga_amp_appr:string%20%3F;wga_amp_kit:string%20%3F;bin_param:bin_param_enum%20%3F;bin_software:string%20%3F;reassembly_bin:string%20%3F;mag_cov_software:mag_cov_software_enum%20%3F;vir_ident_software:string%20%3F;pred_genome_type:pred_genome_type_enum%20%3F;pred_genome_struc:pred_genome_struc_enum%20%3F;detec_type:string%20%3F;otu_class_appr:string%20%3F;otu_seq_comp_appr:string%20%3F;otu_db:string%20%3F;host_pred_appr:host_pred_appr_enum%20%3F;host_pred_est_acc:string%20%3F;associated_resource:string%20%3F;sop:string%20%3F],[QuantityValue]<samp_size%200..1-++[Core],[QuantityValue]<temp%200..1-++[Core],[QuantityValue]<elev%200..1-++[Core],[QuantityValue]<alt%200..1-++[Core],[QuantityValue]<depth%200..1-++[Core])

## Attributes


### Own

 * [submitted_to_insdc](submitted_to_insdc.md)  <sub>0..1</sub>
     * Description: Depending on the study (large-scale e.g. done with next generation sequencing technology, or small-scale) sequences have to be submitted to SRA (Sequence Read Archive), DRA (DDBJ Read Archive) or via the classical Webin/Sequin systems to Genbank, ENA and DDBJ. Although this field is mandatory, it is meant as a self-test field, therefore it is not necessary to include this field in contextual data submitted to databases
     * Range: [String](types/String.md)
     * Example: yes None
 * [investigation_type](investigation_type.md)  <sub>0..1</sub>
     * Description: Nucleic Acid Sequence Report is the root element of all MIGS/MIMS compliant reports as standardized by Genomic Standards Consortium. This field is either eukaryote,bacteria,virus,plasmid,organelle, metagenome,mimarks-survey, mimarks-specimen, metatranscriptome, single amplified genome, metagenome-assembled genome, or uncultivated viral genome
     * Range: [investigation_type_enum](investigation_type_enum.md)
     * Example: metagenome None
 * [samp_name](samp_name.md)  <sub>0..1</sub>
     * Description: A local identifier or name that for the material sample used for extracting nucleic acids, and subsequent sequencing. It can refer either to the original material collected or to any derived sub-samples. It can have any format, but we suggest that you make it concise, unique and consistent within your lab, and as informative as possible. INSDC requires every sample name from a single Submitter to be unique. Use of a globally unique identifier for the field source_mat_id is recommended in addition to sample_name.
     * Range: [String](types/String.md)
     * Example: ISDsoil1 None
 * [samp_taxon_id](samp_taxon_id.md)  <sub>0..1</sub>
     * Description: NCBI taxon id of the sample.  Maybe be a single taxon or mixed taxa sample. Use 'synthetic metagenome’ for mock community/positive controls, or 'blank sample' for negative controls.
     * Range: [String](types/String.md)
     * Example: Gut Metagenome [NCBI:txid749906] None
 * [project_name](project_name.md)  <sub>0..1</sub>
     * Description: Name of the project within which the sequencing was organized
     * Range: [String](types/String.md)
     * Example: Forest soil metagenome None
 * [experimental_factor](experimental_factor.md)  <sub>0..1</sub>
     * Description: Experimental factors are essentially the variable aspects of an experiment design which can be used to describe an experiment, or set of experiments, in an increasingly detailed manner. This field accepts ontology terms from Experimental Factor Ontology (EFO) and/or Ontology for Biomedical Investigations (OBI). For a browser of EFO (v 2.95) terms, please see http://purl.bioontology.org/ontology/EFO; for a browser of OBI (v 2018-02-12) terms please see http://purl.bioontology.org/ontology/OBI
     * Range: [String](types/String.md)
     * Example: time series design [EFO:EFO_0001779] None
 * [lat_lon](lat_lon.md)  <sub>0..1</sub>
     * Description: The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in WGS84 system
     * Range: [String](types/String.md)
     * Example: 50.586825 6.408977 None
 * [depth](depth.md)  <sub>0..1</sub>
     * Description: The vertical distance below local surface, e.g. for sediment or soil samples depth is measured from sediment or soil surface, respectively. Depth can be reported as an interval for subsurface samples.
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 10 meter None
 * [alt](alt.md)  <sub>0..1</sub>
     * Description: Altitude is a term used to identify heights of objects such as airplanes, space shuttles, rockets, atmospheric balloons and heights of places such as atmospheric layers and clouds. It is used to measure the height of an object which is above the earth's surface. In this context, the altitude measurement is the vertical distance between the earth's surface above sea level and the sampled position in the air
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 100 meter None
 * [elev](elev.md)  <sub>0..1</sub>
     * Description: Elevation of the sampling site is its height above a fixed reference point, most commonly the mean sea level. Elevation is mainly used when referring to points on the earth's surface, while altitude is used for points above the surface, such as an aircraft in flight or a spacecraft in orbit.
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 100 meter None
 * [temp](temp.md)  <sub>0..1</sub>
     * Description: Temperature of the sample at the time of sampling.
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 25 degree Celsius None
 * [geo_loc_name](geo_loc_name.md)  <sub>0..1</sub>
     * Description: The geographical origin of the sample as defined by the country or sea name followed by specific region name. Country or sea names should be chosen from the INSDC country list (http://insdc.org/country.html), or the GAZ ontology (http://purl.bioontology.org/ontology/GAZ)
     * Range: [String](types/String.md)
     * Example: USA: Maryland, Bethesda None
 * [collection_date](collection_date.md)  <sub>0..1</sub>
     * Description: The time of sampling, either as an instance (single point in time) or interval. In case no exact time is available, the date/time can be right truncated i.e. all of these are valid times: 2008-01-23T19:23:10+00:00; 2008-01-23T19:23:10; 2008-01-23; 2008-01; 2008; Except: 2008-01; 2008 all are ISO8601 compliant
     * Range: [Date](types/Date.md)
     * Example: 2018-05-11T10:00:00+01:00; 2018-05-11 None
 * [neg_cont_type](neg_cont_type.md)  <sub>0..1</sub>
     * Description: The substance or equipment used as a negative control in an investigation
     * Range: [neg_cont_type_enum](neg_cont_type_enum.md)
     * Example:  None
 * [pos_cont_type](pos_cont_type.md)  <sub>0..1</sub>
     * Description: The substance, mixture, product, or apparatus used to verify that a process which is part of an investigation delivers a true positive.
     * Range: [String](types/String.md)
     * Example:  None
 * [env_broad_scale](env_broad_scale.md)  <sub>0..1</sub>
     * Description: Report the major environmental system the sample or specimen came from. The system(s) identified should have a coarse spatial grain, to provide the general environmental context of where the sampling was done (e.g. in the desert or a rainforest). We recommend using subclasses of EnvO’s biome class:  http://purl.obolibrary.org/obo/ENVO_00000428. EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
     * Range: [String](types/String.md)
     * Example: oceanic epipelagic zone biome [ENVO:01000033] for annotating a water sample from the photic zone in middle of the Atlantic Ocean None
 * [env_local_scale](env_local_scale.md)  <sub>0..1</sub>
     * Description: Report the entity or entities which are in the sample or specimen’s local vicinity and which you believe have significant causal influences on your sample or specimen. We recommend using EnvO terms which are of smaller spatial grain than your entry for env_broad_scale. Terms, such as anatomical sites, from other OBO Library ontologies which interoperate with EnvO (e.g. UBERON) are accepted in this field. EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS.
     * Range: [String](types/String.md)
     * Example: litter layer [ENVO:01000338]; Annotating a pooled sample taken from various vegetation layers in a forest consider: canopy [ENVO:00000047]|herb and fern layer [ENVO:01000337]|litter layer [ENVO:01000338]|understory [01000335]|shrub layer [ENVO:01000336]. None
 * [env_medium](env_medium.md)  <sub>0..1</sub>
     * Description: Report the environmental material(s) immediately surrounding the sample or specimen at the time of sampling. We recommend using subclasses of 'environmental material' (http://purl.obolibrary.org/obo/ENVO_00010483). EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS . Terms from other OBO ontologies are permissible as long as they reference mass/volume nouns (e.g. air, water, blood) and not discrete, countable entities (e.g. a tree, a leaf, a table top).
     * Range: [String](types/String.md)
     * Example: soil [ENVO:00001998]; Annotating a fish swimming in the upper 100 m of the Atlantic Ocean, consider: ocean water [ENVO:00002151]. Example: Annotating a duck on a pond consider: pond water [ENVO:00002228]|air [ENVO_00002005] None
 * [env_package](env_package.md)  <sub>0..1</sub>
     * Description: MIxS extension for reporting of measurements and observations obtained from one or more of the environments where the sample was obtained. All environmental packages listed here are further defined in separate subtables. By giving the name of the environmental package, a selection of fields can be made from the subtables and can be reported
     * Range: [env_package_enum](env_package_enum.md)
     * Example: soil None
 * [subspecf_gen_lin](subspecf_gen_lin.md)  <sub>0..1</sub>
     * Description: Information about the genetic distinctness of the sequenced organism below the subspecies level, e.g., serovar, serotype, biotype, ecotype, or any relevant genetic typing schemes like Group I plasmid. Subspecies should not be recorded in this term, but in the NCBI taxonomy. Supply both the lineage name and the lineage rank separated by a colon, e.g., biovar:abc123.
     * Range: [String](types/String.md)
     * Example: serovar:Newport None
 * [ploidy](ploidy.md)  <sub>0..1</sub>
     * Description: The ploidy level of the genome (e.g. allopolyploid, haploid, diploid, triploid, tetraploid). It has implications for the downstream study of duplicated gene and regions of the genomes (and perhaps for difficulties in assembly). For terms, please select terms listed under class ploidy (PATO:001374) of Phenotypic Quality Ontology (PATO), and for a browser of PATO (v 2018-03-27) please refer to http://purl.bioontology.org/ontology/PATO
     * Range: [String](types/String.md)
     * Example: allopolyploidy [PATO:0001379] None
 * [num_replicons](num_replicons.md)  <sub>0..1</sub>
     * Description: Reports the number of replicons in a nuclear genome of eukaryotes, in the genome of a bacterium or archaea or the number of segments in a segmented virus. Always applied to the haploid chromosome count of a eukaryote
     * Range: [Integer](types/Integer.md)
     * Example: 2 None
 * [extrachrom_elements](extrachrom_elements.md)  <sub>0..1</sub>
     * Description: Do plasmids exist of significant phenotypic consequence (e.g. ones that determine virulence or antibiotic resistance). Megaplasmids? Other plasmids (borrelia has 15+ plasmids)
     * Range: [Integer](types/Integer.md)
     * Example: 5 None
 * [estimated_size](estimated_size.md)  <sub>0..1</sub>
     * Description: The estimated size of the genome prior to sequencing. Of particular importance in the sequencing of (eukaryotic) genome which could remain in draft form for a long or unspecified period.
     * Range: [String](types/String.md)
     * Example: 300000 bp None
 * [ref_biomaterial](ref_biomaterial.md)  <sub>0..1</sub>
     * Description: Primary publication if isolated before genome publication; otherwise, primary genome report.
     * Range: [String](types/String.md)
     * Example: doi:10.1016/j.syapm.2018.01.009 None
 * [source_mat_id](source_mat_id.md)  <sub>0..1</sub>
     * Description: A unique identifier assigned to a material sample (as defined by http://rs.tdwg.org/dwc/terms/materialSampleID, and as opposed to a particular digital record of a material sample) used for extracting nucleic acids, and subsequent sequencing. The identifier can refer either to the original material collected or to any derived sub-samples. The INSDC qualifiers /specimen_voucher, /bio_material, or /culture_collection may or may not share the same value as the source_mat_id field. For instance, the /specimen_voucher qualifier and source_mat_id may both contain 'UAM:Herps:14' , referring to both the specimen voucher and sampled tissue with the same identifier. However, the /culture_collection qualifier may refer to a value from an initial culture (e.g. ATCC:11775) while source_mat_id would refer to an identifier from some derived culture from which the nucleic acids were extracted (e.g. xatc123 or ark:/2154/R2).
     * Range: [String](types/String.md)
     * Example: MPI012345 None
 * [pathogenicity](pathogenicity.md)  <sub>0..1</sub>
     * Description: To what is the entity pathogenic
     * Range: [String](types/String.md)
     * Example: human, animal, plant, fungi, bacteria None
 * [biotic_relationship](biotic_relationship.md)  <sub>0..1</sub>
     * Description: Description of relationship(s) between the subject organism and other organism(s) it is associated with. E.g., parasite on species X; mutualist with species Y. The target organism is the subject of the relationship, and the other organism(s) is the object
     * Range: [biotic_relationship_enum](biotic_relationship_enum.md)
     * Example: free living None
 * [specific_host](specific_host.md)  <sub>0..1</sub>
     * Description: Report the host's taxonomic name and/or NCBI taxonomy ID.
     * Range: [String](types/String.md)
     * Example: Homo sapiens and/or 9606 None
 * [host_spec_range](host_spec_range.md)  <sub>0..1</sub>
     * Description: The range and diversity of host species that an organism is capable of infecting, defined by NCBI taxonomy identifier.
     * Range: [Integer](types/Integer.md)
     * Example: 9606 None
 * [health_disease_stat](health_disease_stat.md)  <sub>0..1</sub>
     * Description: Health or disease status of specific host at time of collection
     * Range: [health_disease_stat_enum](health_disease_stat_enum.md)
     * Example: dead None
 * [host_disease_stat](host_disease_stat.md)  <sub>0..1</sub>
     * Description: List of diseases with which the host has been diagnosed; can include multiple diagnoses. The value of the field depends on host; for humans the terms should be chosen from the DO (Human Disease Ontology) at https://www.disease-ontology.org, non-human host diseases are free text
     * Range: [String](types/String.md)
     * Example: rabies [DOID:11260] None
 * [trophic_level](trophic_level.md)  <sub>0..1</sub>
     * Description: Trophic levels are the feeding position in a food chain. Microbes can be a range of producers (e.g. chemolithotroph)
     * Range: [trophic_level_enum](trophic_level_enum.md)
     * Example: heterotroph None
 * [propagation](propagation.md)  <sub>0..1</sub>
     * Description: The type of reproduction from the parent stock. Values for this field is specific to different taxa. For phage or virus: lytic/lysogenic/temperate/obligately lytic. For plasmids: incompatibility group. For eukaryotes: sexual/asexual.
     * Range: [String](types/String.md)
     * Example: lytic None
 * [encoded_traits](encoded_traits.md)  <sub>0..1</sub>
     * Description: Should include key traits like antibiotic resistance or xenobiotic degradation phenotypes for plasmids, converting genes for phage
     * Range: [String](types/String.md)
     * Example: beta-lactamase class A None
 * [rel_to_oxygen](rel_to_oxygen.md)  <sub>0..1</sub>
     * Description: Is this organism an aerobe, anaerobe? Please note that aerobic and anaerobic are valid descriptors for microbial environments
     * Range: [rel_to_oxygen_enum](rel_to_oxygen_enum.md)
     * Example: aerobe None
 * [isol_growth_condt](isol_growth_condt.md)  <sub>0..1</sub>
     * Description: Publication reference in the form of pubmed ID (pmid), digital object identifier (doi) or url for isolation and growth condition specifications of the organism/material
     * Range: [String](types/String.md)
     * Example: doi: 10.1016/j.syapm.2018.01.009 None
 * [samp_collec_device](samp_collec_device.md)  <sub>0..1</sub>
     * Description: The device used to collect an environmental sample. This field accepts terms listed under environmental sampling device (http://purl.obolibrary.org/obo/ENVO). This field also accepts terms listed under specimen collection device (http://purl.obolibrary.org/obo/GENEPIO_0002094).
     * Range: [String](types/String.md)
     * Example: swab, biopsy, niskin bottle, push core, drag swab [GENEPIO:0002713] None
 * [samp_collec_method](samp_collec_method.md)  <sub>0..1</sub>
     * Description: The method employed for collecting the sample.
     * Range: [String](types/String.md)
     * Example: swabbing None
 * [samp_mat_process](samp_mat_process.md)  <sub>0..1</sub>
     * Description: A brief description of any processing applied to the sample during or after retrieving the sample from environment, or a link to the relevant protocol(s) performed.
     * Range: [String](types/String.md)
     * Example: filtering of seawater, storing samples in ethanol None
 * [size_frac](size_frac.md)  <sub>0..1</sub>
     * Description: Filtering pore size used in sample preparation
     * Range: [String](types/String.md)
     * Example: 0-0.22 micrometer None
 * [samp_size](samp_size.md)  <sub>0..1</sub>
     * Description: The total amount or size (volume (ml), mass (g) or area (m2) ) of sample collected.
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 5 liter None
 * [samp_vol_we_dna_ext](samp_vol_we_dna_ext.md)  <sub>0..1</sub>
     * Description: Volume (ml) or mass (g) of total collected sample processed for DNA extraction. Note: total sample collected should be entered under the term Sample Size (MIXS:0000001).
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 1500 milliliter None
 * [source_uvig](source_uvig.md)  <sub>0..1</sub>
     * Description: Type of dataset from which the UViG was obtained
     * Range: [source_uvig_enum](source_uvig_enum.md)
     * Example: viral fraction metagenome (virome) None
 * [virus_enrich_appr](virus_enrich_appr.md)  <sub>0..1</sub>
     * Description: List of approaches used to enrich the sample for viruses, if any
     * Range: [virus_enrich_appr_enum](virus_enrich_appr_enum.md)
     * Example: filtration + FeCl Precipitation + ultracentrifugation + DNAse None
 * [nucl_acid_ext](nucl_acid_ext.md)  <sub>0..1</sub>
     * Description: A link to a literature reference, electronic resource or a standard operating procedure (SOP), that describes the material separation to recover the nucleic acid fraction from a sample
     * Range: [String](types/String.md)
     * Example: https://mobio.com/media/wysiwyg/pdfs/protocols/12888.pdf None
 * [nucl_acid_amp](nucl_acid_amp.md)  <sub>0..1</sub>
     * Description: A link to a literature reference, electronic resource or a standard operating procedure (SOP), that describes the enzymatic amplification (PCR, TMA, NASBA) of specific nucleic acids
     * Range: [String](types/String.md)
     * Example: https://phylogenomics.me/protocols/16s-pcr-protocol/ None
 * [lib_size](lib_size.md)  <sub>0..1</sub>
     * Description: Total number of clones in the library prepared for the project
     * Range: [Integer](types/Integer.md)
     * Example: 50 None
 * [lib_reads_seqd](lib_reads_seqd.md)  <sub>0..1</sub>
     * Description: Total number of clones sequenced from the library
     * Range: [Integer](types/Integer.md)
     * Example: 20 None
 * [lib_layout](lib_layout.md)  <sub>0..1</sub>
     * Description: Specify whether to expect single, paired, or other configuration of reads
     * Range: [lib_layout_enum](lib_layout_enum.md)
     * Example: paired None
 * [lib_vector](lib_vector.md)  <sub>0..1</sub>
     * Description: Cloning vector type(s) used in construction of libraries
     * Range: [String](types/String.md)
     * Example: Bacteriophage P1 None
 * [lib_screen](lib_screen.md)  <sub>0..1</sub>
     * Description: Specific enrichment or screening methods applied before and/or after creating libraries
     * Range: [String](types/String.md)
     * Example: enriched, screened, normalized None
 * [target_gene](target_gene.md)  <sub>0..1</sub>
     * Description: Targeted gene or locus name for marker gene studies
     * Range: [String](types/String.md)
     * Example: 16S rRNA, 18S rRNA, nif, amoA, rpo None
 * [target_subfragment](target_subfragment.md)  <sub>0..1</sub>
     * Description: Name of subfragment of a gene or locus. Important to e.g. identify special regions on marker genes like V6 on 16S rRNA
     * Range: [String](types/String.md)
     * Example: V6, V9, ITS None
 * [pcr_primers](pcr_primers.md)  <sub>0..1</sub>
     * Description: PCR primers that were used to amplify the sequence of the targeted gene, locus or subfragment. This field should contain all the primers used for a single PCR reaction if multiple forward or reverse primers are present in a single PCR reaction. The primer sequence should be reported in uppercase letters
     * Range: [String](types/String.md)
     * Example: FWD:GTGCCAGCMGCCGCGGTAA;REV:GGACTACHVGGGTWTCTAAT None
 * [mid](mid.md)  <sub>0..1</sub>
     * Description: Molecular barcodes, called Multiplex Identifiers (MIDs), that are used to specifically tag unique samples in a sequencing run. Sequence should be reported in uppercase letters
     * Range: [String](types/String.md)
     * Example: GTGAATAT None
 * [adapters](adapters.md)  <sub>0..1</sub>
     * Description: Adapters provide priming sequences for both amplification and sequencing of the sample-library fragments. Both adapters should be reported; in uppercase letters
     * Range: [String](types/String.md)
     * Example: AATGATACGGCGACCACCGAGATCTACACGCT;CAAGCAGAAGACGGCATACGAGAT None
 * [pcr_cond](pcr_cond.md)  <sub>0..1</sub>
     * Description: Description of reaction conditions and components of PCR in the form of 'initial denaturation:94degC_1.5min; annealing=...'
     * Range: [String](types/String.md)
     * Example: initial denaturation:94_3;annealing:50_1;elongation:72_1.5;final elongation:72_10;35 None
 * [seq_meth](seq_meth.md)  <sub>0..1</sub>
     * Description: Sequencing machine used. Where possible the term should be taken from the OBI list of DNA sequencers (http://purl.obolibrary.org/obo/OBI_0400103).
     * Range: [String](types/String.md)
     * Example: 454 Genome Sequencer FLX [OBI:0000702] None
 * [seq_quality_check](seq_quality_check.md)  <sub>0..1</sub>
     * Description: Indicate if the sequence has been called by automatic systems (none) or undergone a manual editing procedure (e.g. by inspecting the raw data or chromatograms). Applied only for sequences that are not submitted to SRA,ENA or DRA
     * Range: [String](types/String.md)
     * Example: none None
 * [chimera_check](chimera_check.md)  <sub>0..1</sub>
     * Description: Tool(s) used for chimera checking, including version number and parameters, to discover and remove chimeric sequences. A chimeric sequence is comprised of two or more phylogenetically distinct parent sequences.
     * Range: [String](types/String.md)
     * Example: uchime;v4.1;default parameters None
 * [tax_ident](tax_ident.md)  <sub>0..1</sub>
     * Description: The phylogenetic marker(s) used to assign an organism name to the SAG or MAG
     * Range: [tax_ident_enum](tax_ident_enum.md)
     * Example: other: rpoB gene None
 * [assembly_qual](assembly_qual.md)  <sub>0..1</sub>
     * Description: The assembly quality category is based on sets of criteria outlined for each assembly quality category. For MISAG/MIMAG; Finished: Single, validated, contiguous sequence per replicon without gaps or ambiguities with a consensus error rate equivalent to Q50 or better. High Quality Draft:Multiple fragments where gaps span repetitive regions. Presence of the 23S, 16S and 5S rRNA genes and at least 18 tRNAs. Medium Quality Draft:Many fragments with little to no review of assembly other than reporting of standard assembly statistics. Low Quality Draft:Many fragments with little to no review of assembly other than reporting of standard assembly statistics. Assembly statistics include, but are not limited to total assembly size, number of contigs, contig N50/L50, and maximum contig length. For MIUVIG; Finished: Single, validated, contiguous sequence per replicon without gaps or ambiguities, with extensive manual review and editing to annotate putative gene functions and transcriptional units. High-quality draft genome: One or multiple fragments, totaling ≥ 90% of the expected genome or replicon sequence or predicted complete. Genome fragment(s): One or multiple fragments, totalling < 90% of the expected genome or replicon sequence, or for which no genome size could be estimated
     * Range: [assembly_qual_enum](assembly_qual_enum.md)
     * Example: High-quality draft genome None
 * [assembly_name](assembly_name.md)  <sub>0..1</sub>
     * Description: Name/version of the assembly provided by the submitter that is used in the genome browsers and in the community
     * Range: [String](types/String.md)
     * Example: HuRef, JCVI_ISG_i3_1.0 None
 * [assembly_software](assembly_software.md)  <sub>0..1</sub>
     * Description: Tool(s) used for assembly, including version number and parameters
     * Range: [String](types/String.md)
     * Example: metaSPAdes;3.11.0;kmer set 21,33,55,77,99,121, default parameters otherwise None
 * [annot](annot.md)  <sub>0..1</sub>
     * Description: Tool used for annotation, or for cases where annotation was provided by a community jamboree or model organism database rather than by a specific submitter
     * Range: [String](types/String.md)
     * Example: prokka None
 * [number_contig](number_contig.md)  <sub>0..1</sub>
     * Description: Total number of contigs in the cleaned/submitted assembly that makes up a given genome, SAG, MAG, or UViG
     * Range: [Integer](types/Integer.md)
     * Example: 40 None
 * [feat_pred](feat_pred.md)  <sub>0..1</sub>
     * Description: Method used to predict UViGs features such as ORFs, integration site, etc.
     * Range: [String](types/String.md)
     * Example: Prodigal;2.6.3;default parameters None
 * [ref_db](ref_db.md)  <sub>0..1</sub>
     * Description: List of database(s) used for ORF annotation, along with version number and reference to website or publication
     * Range: [String](types/String.md)
     * Example: pVOGs;5;http://dmk-brain.ecn.uiowa.edu/pVOGs/ Grazziotin et al. 2017 doi:10.1093/nar/gkw975 None
 * [sim_search_meth](sim_search_meth.md)  <sub>0..1</sub>
     * Description: Tool used to compare ORFs with database, along with version and cutoffs used
     * Range: [String](types/String.md)
     * Example: HMMER3;3.1b2;hmmsearch, cutoff of 50 on score None
 * [tax_class](tax_class.md)  <sub>0..1</sub>
     * Description: Method used for taxonomic classification, along with reference database used, classification rank, and thresholds used to classify new genomes
     * Range: [String](types/String.md)
     * Example: vConTACT vContact2 (references from NCBI RefSeq v83, genus rank classification, default parameters) None
 * [x_16s_recover](x_16s_recover.md)  <sub>0..1</sub>
     * Description: Can a 16S gene be recovered from the submitted SAG or MAG?
     * Range: [String](types/String.md)
     * Example: yes None
 * [x_16s_recover_software](x_16s_recover_software.md)  <sub>0..1</sub>
     * Description: Tools used for 16S rRNA gene extraction
     * Range: [String](types/String.md)
     * Example: rambl;v2;default parameters None
 * [trnas](trnas.md)  <sub>0..1</sub>
     * Description: The total number of tRNAs identified from the SAG or MAG
     * Range: [Integer](types/Integer.md)
     * Example: 18 None
 * [trna_ext_software](trna_ext_software.md)  <sub>0..1</sub>
     * Description: Tools used for tRNA identification
     * Range: [String](types/String.md)
     * Example: infernal;v2;default parameters None
 * [compl_score](compl_score.md)  <sub>0..1</sub>
     * Description: Completeness score is typically based on either the fraction of markers found as compared to a database or the percent of a genome found as compared to a closely related reference genome. High Quality Draft: >90%, Medium Quality Draft: >50%, and Low Quality Draft: < 50% should have the indicated completeness scores
     * Range: [compl_score_enum](compl_score_enum.md)
     * Example: med;60% None
 * [compl_software](compl_software.md)  <sub>0..1</sub>
     * Description: Tools used for completion estimate, i.e. checkm, anvi'o, busco
     * Range: [String](types/String.md)
     * Example: checkm None
 * [compl_appr](compl_appr.md)  <sub>0..1</sub>
     * Description: The approach used to determine the completeness of a given genomic assembly, which would typically make use of a set of conserved marker genes or a closely related reference genome. For UViG completeness, include reference genome or group used, and contig feature suggesting a complete genome
     * Range: [compl_appr_enum](compl_appr_enum.md)
     * Example: other: UViG length compared to the average length of reference genomes from the P22virus genus (NCBI RefSeq v83) None
 * [contam_score](contam_score.md)  <sub>0..1</sub>
     * Description: The contamination score is based on the fraction of single-copy genes that are observed more than once in a query genome. The following scores are acceptable for; High Quality Draft: < 5%, Medium Quality Draft: < 10%, Low Quality Draft: < 10%. Contamination must be below 5% for a SAG or MAG to be deposited into any of the public databases
     * Range: [String](types/String.md)
     * Example: 1% None
 * [contam_screen_input](contam_screen_input.md)  <sub>0..1</sub>
     * Description: The type of sequence data used as input
     * Range: [String](types/String.md)
     * Example: contigs None
 * [contam_screen_param](contam_screen_param.md)  <sub>0..1</sub>
     * Description: Specific parameters used in the decontamination sofware, such as reference database, coverage, and kmers. Combinations of these parameters may also be used, i.e. kmer and coverage, or reference database and kmer
     * Range: [contam_screen_param_enum](contam_screen_param_enum.md)
     * Example: kmer None
 * [decontam_software](decontam_software.md)  <sub>0..1</sub>
     * Description: Tool(s) used in contamination screening
     * Range: [decontam_software_enum](decontam_software_enum.md)
     * Example: anvi'o None
 * [sort_tech](sort_tech.md)  <sub>0..1</sub>
     * Description: Method used to sort/isolate cells or particles of interest
     * Range: [sort_tech_enum](sort_tech_enum.md)
     * Example: optical manipulation None
 * [single_cell_lysis_appr](single_cell_lysis_appr.md)  <sub>0..1</sub>
     * Description: Method used to free DNA from interior of the cell(s) or particle(s)
     * Range: [single_cell_lysis_appr_enum](single_cell_lysis_appr_enum.md)
     * Example: enzymatic None
 * [single_cell_lysis_prot](single_cell_lysis_prot.md)  <sub>0..1</sub>
     * Description: Name of the kit or standard protocol used for cell(s) or particle(s) lysis
     * Range: [String](types/String.md)
     * Example: ambion single cell lysis kit None
 * [wga_amp_appr](wga_amp_appr.md)  <sub>0..1</sub>
     * Description: Method used to amplify genomic DNA in preparation for sequencing
     * Range: [String](types/String.md)
     * Example: mda based None
 * [wga_amp_kit](wga_amp_kit.md)  <sub>0..1</sub>
     * Description: Kit used to amplify genomic DNA in preparation for sequencing
     * Range: [String](types/String.md)
     * Example: qiagen repli-g None
 * [bin_param](bin_param.md)  <sub>0..1</sub>
     * Description: The parameters that have been applied during the extraction of genomes from metagenomic datasets
     * Range: [bin_param_enum](bin_param_enum.md)
     * Example: coverage and kmer None
 * [bin_software](bin_software.md)  <sub>0..1</sub>
     * Description: Tool(s) used for the extraction of genomes from metagenomic datasets, where possible include a product ID (PID) of the tool(s) used.
     * Range: [String](types/String.md)
     * Example: MetaCluster-TA (RRID:SCR_004599), MaxBin (biotools:maxbin) None
 * [reassembly_bin](reassembly_bin.md)  <sub>0..1</sub>
     * Description: Has an assembly been performed on a genome bin extracted from a metagenomic assembly?
     * Range: [String](types/String.md)
     * Example: no None
 * [mag_cov_software](mag_cov_software.md)  <sub>0..1</sub>
     * Description: Tool(s) used to determine the genome coverage if coverage is used as a binning parameter in the extraction of genomes from metagenomic datasets
     * Range: [mag_cov_software_enum](mag_cov_software_enum.md)
     * Example: bbmap None
 * [vir_ident_software](vir_ident_software.md)  <sub>0..1</sub>
     * Description: Tool(s) used for the identification of UViG as a viral genome, software or protocol name including version number, parameters, and cutoffs used
     * Range: [String](types/String.md)
     * Example: VirSorter; 1.0.4; Virome database, category 2 None
 * [pred_genome_type](pred_genome_type.md)  <sub>0..1</sub>
     * Description: Type of genome predicted for the UViG
     * Range: [pred_genome_type_enum](pred_genome_type_enum.md)
     * Example: dsDNA None
 * [pred_genome_struc](pred_genome_struc.md)  <sub>0..1</sub>
     * Description: Expected structure of the viral genome
     * Range: [pred_genome_struc_enum](pred_genome_struc_enum.md)
     * Example: non-segmented None
 * [detec_type](detec_type.md)  <sub>0..1</sub>
     * Description: Type of UViG detection
     * Range: [String](types/String.md)
     * Example: independent sequence (UViG) None
 * [otu_class_appr](otu_class_appr.md)  <sub>0..1</sub>
     * Description: Cutoffs and approach used when clustering “species-level” OTUs. Note that results from standard 95% ANI / 85% AF clustering should be provided alongside OTUS defined from another set of thresholds, even if the latter are the ones primarily used during the analysis
     * Range: [String](types/String.md)
     * Example: 95% ANI;85% AF; greedy incremental clustering None
 * [otu_seq_comp_appr](otu_seq_comp_appr.md)  <sub>0..1</sub>
     * Description: Tool and thresholds used to compare sequences when computing "species-level" OTUs
     * Range: [String](types/String.md)
     * Example: blastn;2.6.0+;e-value cutoff: 0.001 None
 * [otu_db](otu_db.md)  <sub>0..1</sub>
     * Description: Reference database (i.e. sequences not generated as part of the current study) used to cluster new genomes in "species-level" OTUs, if any
     * Range: [String](types/String.md)
     * Example: NCBI Viral RefSeq;83 None
 * [host_pred_appr](host_pred_appr.md)  <sub>0..1</sub>
     * Description: Tool or approach used for host prediction
     * Range: [host_pred_appr_enum](host_pred_appr_enum.md)
     * Example: CRISPR spacer match None
 * [host_pred_est_acc](host_pred_est_acc.md)  <sub>0..1</sub>
     * Description: For each tool or approach used for host prediction, estimated false discovery rates should be included, either computed de novo or from the literature
     * Range: [String](types/String.md)
     * Example: CRISPR spacer match: 0 or 1 mismatches, estimated 8% FDR at the host genus rank (Edwards et al. 2016 doi:10.1093/femsre/fuv048) None
 * [associated resource](associated_resource.md)  <sub>0..1</sub>
     * Description: A related resource that is referenced, cited, or otherwise associated to the sequence.
     * Range: [String](types/String.md)
     * Example: http://www.earthmicrobiome.org/ None
 * [sop](sop.md)  <sub>0..1</sub>
     * Description: Standard operating procedures used in assembly and/or annotation of genomes, metagenomes or environmental sequences
     * Range: [String](types/String.md)
     * Example: http://press.igsb.anl.gov/earthmicrobiome/protocols-and-standards/its/ None
