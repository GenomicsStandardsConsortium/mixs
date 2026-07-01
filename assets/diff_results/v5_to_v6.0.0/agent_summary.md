# MIxS schema diff: v5 → v6.0.0

**v5** (600 terms, from `mixs-legacy` `mixs_v5.xlsx`) → **v6.0.0** (804 terms, from `GenomicsStandardsConsortium/mixs@mixs6.0.0`).
Headline counts: 212 added, 20 renamed, 4 removed, 3 deleted, 1 rename candidate, 65 definitions changed, 573 shared.

The 204-term net growth is real expansion, not churn: almost all of it is new measurement packages (Food, host-of-host symbiosis, animal husbandry, spike-in controls, fermentation). The removals are small and mostly structural.

## Added (212), by theme

The additions cluster into a handful of new or heavily expanded domains rather than scattered one-off fields.

- **Food package (largest single driver).** 31 slots beginning `food_` (packaging, processing, distribution, provenance, traceability: e.g. `food_pack_integrity`, `food_dis_point`, `food_trace_list`, `food_treat_proc`), plus the food-adjacent fields `cons_food_stor_dur`, `cons_food_stor_temp`, `cons_purch_date`, `cons_qty_purchased`, `dietary_claim_use`, `intended_consumer`, `spec_intended_cons`, `prod_label_claims`, `HACCP_term`, `IFSAC_category`, `facility_type`, `hygienic_area`, `env_monitoring_zone`, `lot_number`, `ster_meth_samp_room`, and the enums `Food_Product_type` / `Food_source`. This is an entire new package arriving at once.
- **Host-of-host / symbiosis (new domain).** 14 `host_of_host_*` slots (taxid, name, disease, genotype, phenotype, gravidity, total mass, environment, etc.) plus `host_symbiont`, `host_specificity`, `host_dependence`, `sym_life_cycle_type`, `symbiont_host_role`, `type_of_symbiosis`, `mode_transmission`, `route_transmission`, `association_duration`. MIxS gained the ability to describe a host that itself lives on/in another host.
- **Animal husbandry / farm.** 12 `animal_*` slots (antimicrobial use `animal_am*`, `animal_housing`, `animal_diet`, `animal_body_cond`, ...), the `farm_equip*` cluster (4), `farm_water_source`, `anim_water_method`, `fertilizer_admin`, `fertilizer_date`, `crop_yield`, `pres_animal_insect`.
- **Spike-in controls.** 8 `spikein_*` slots (`spikein_AMR`, `spikein_antibiotic`, `spikein_org`, `spikein_serovar`, `spikein_strain`, ...) plus `neg_cont_type`, `pos_cont_type`.
- **Fermentation.** 9 `ferm_*` slots (`ferm_pH`, `ferm_temp`, `ferm_time`, `ferm_vessel`, `ferm_headspace_oxy`, ...).
- **Microbial culture / enrichment.** `microb_start*` (5), `microb_cult_med`, `micro_biomass_meth`, `cult_isol_date`, `cult_result`, `cult_result_org`, `cult_target`, `growth_medium`, `enrichment_protocol`, `bacterial_density`, `serovar_or_serotype`.
- **Sample handling, storage, transport.** `samp_stor_*` (5: device/dur/loc/media/temp) + `samp_store_sol`, `samp_transport_*` (3), `samp_rep_biol`/`samp_rep_tech`, `samp_pooling`, `samp_purpose`, `samp_source_mat_cat`, `samp_taxon_id`, `samp_surf_moisture`, `samp_loc_condition`, `area_samp_size`, `num_samp_collect`.
- **Soil (expanded).** 10 `soil_*` slots (`soil_pH`, `soil_horizon`, `soil_porosity`, `soil_texture_class`, `soil_texture_meth`, ...), plus `part_plant_animal`, `plant_part_maturity`, `plant_reprod_crop`, `plant_water_method`, `photosynt_activ`(+`_meth`), `prev_land_use_meth`, `non_min_nutr_regm`.
- **Sequencing / library prep.** `library_prep_kit`, `nucl_acid_ext_kit`, `sequencing_kit`, `sequencing_location`.
- **Study design.** `study_design`, `study_inc_dur`, `study_inc_temp`, `study_timecourse`, `study_tmnt`, `timepoint`, `biocide_used`.
- **Air / weather / location context.** `air_PM_concen`, `air_flow_impede`, `adjacent_environment`, `coll_site_geo_feat`, `extr_weather_event`, `date_extr_weath`, `season_humidity`, `rel_location`, `water_source_adjac`, `water_source_shared`, `water_pH`, `water_frequency`.
- **Nutrient chemistry.** `tot_car`, `tot_phos`, `tot_n_meth`.
- **LinkML infrastructure (not measurement slots).** Several added names are the schema's own scaffolding, not sample metadata: `core field`, `environment field`, `investigation field`, `sequencing field`, `nucleic acid sequence source field`, `mixs extension field`, `associated resource`, `has numeric value`, `has raw value`, `has unit`, `repository_name`, `associated resource`. These reflect the v6 move to a normalized LinkML model with mixin "field" classes and a value/unit/raw-value pattern. Count them separately from the ~200 real new slots.

## Removed (4) and deleted (3)

The diff distinguishes two removal categories:

- **`removed` (4):** `extreme_salinity`, `nose_mouth_teeth_throat_disord`, `pres_animal`, `resp_part_matter`.
- **`deleted` (3):** `env_package`, `investigation_type`, `submitted_to_insdc`. These three are administrative/structural fields, dropped as part of the v6 model reorganization rather than retired measurements.

Two of the four `removed` slots look like replacements rather than losses: `pres_animal` is the rename candidate below (`pres_animal_insect` was added), and `resp_part_matter` (respirable particulate matter) is plausibly superseded by the new air-particulate fields `air_PM_concen` / `air particulate matter concentration`. `nose_mouth_teeth_throat_disord` overlaps the surviving `nose_throat_disord`. None of these are stated as renames, so I have not treated them as such beyond flagging.

## Renamed (20), old → new

Three consistent conventions explain nearly all 20 renames:

1. **Abbreviation truncation** (the dominant pattern): `treatment→treat`, `system→sys`, `content→cont`, `production→prod`, `collection→collect`, `element→elem`, `damage→dam`, `device→dev`, `shading→shad`, `pressure→press`, `organism→org`.
   - `chem_treatment_method→chem_treat_method`, `heat_system_deliv_meth→heat_sys_deliv_meth`, `tot_nitro_content_meth→tot_nitro_cont_meth`, `water_content_soil_meth→water_cont_soil_meth`, `water_production_rate→water_prod_rate`, `samp_collection_point→samp_collect_point`, `room_architec_element→room_architec_elem`, `room_moist_damage_hist→room_moist_dam_hist`, `shading_device_water_mold→shad_dev_water_mold`, `tvdss_of_hcr_pressure→tvdss_of_hcr_press`, `organism_count_qpcr_info→org_count_qpcr_info`.
2. **`vOTU → OTU`** terminology change (drop the leading `v`): `votu_class_appr→otu_class_appr`, `votu_db→otu_db`, `votu_seq_comp_appr→otu_seq_comp_appr`. (The matching definitions also change vOTU→OTU wording, see below.)
3. **Leading `x_` added to digit-initial names** (LinkML identifiers cannot start with a digit): `16s_recover→x_16s_recover`, `16s_recover_software→x_16s_recover_software`.

The remaining renames drop a semantic prefix: `host_blood_press_diast→blood_press_diast`, `host_blood_press_syst→blood_press_syst`, `ihmc_ethnicity→ethnicity`, and `health_disease_stat→host_disease_stat` (a `health→host` reframing that is also a definition change; see Notes).

## Possible missed renames

- `pres_animal → pres_animal_insect` (1 candidate). `pres_animal` appears in the `removed` list and `pres_animal_insect` in `added`. This is almost certainly a real rename that a maintainer should confirm and promote into the tool's rename map, so it stops being reported as a removal + an unrelated addition.

## Definition changes (65)

Two cross-cutting drivers account for most of the substantive edits; a third large group is purely cosmetic.

**Driver 1: adding controlled-vocabulary / ontology references.** The clearest single theme. Roughly ten disease-history fields all gained a Human Disease Ontology (DO) reference they lacked in v5: `blood_blood_disord`, `dermatology_disord`, `gastrointest_disord`, `gynecologic_disord`, `kidney_disord`, `liver_disord`, `nose_throat_disord`, `pulmonary_disord`, `urogenit_disord`, `urogenit_tract_disor`. Beyond disease fields, many slots shifted from a prose definition to pointing at an OBO term list: `samp_collect_device` (ENVO + GENEPIO), `samp_type` (GENEPIO), `soil_type` (ENVO), `season` (NCIT), `seq_meth` (OBI DNA-sequencer list), and the env_* triad `env_broad_scale` / `env_local_scale` / `env_medium` (EnvO usage-wiki links). v6 is systematically wiring free-text fields to ontologies.

**Driver 2: concept → tool/method, and genuine redefinitions.** A cluster of fields moved from *describing a concept* to *naming the tool or measurement*:
- `chimera_check`: v5 defined what a chimera is; v6 makes it the tool used for chimera checking.
- `seq_meth`: "sequencing method" → "sequencing machine" (OBI list).
- `bin_software`: now asks for a product ID.

Genuine meaning changes that could affect existing data (worth individual attention):
- **`host_spec_range`**: v5 = "NCBI taxid of the specific host"; v6 = "the range and diversity of host species an organism can infect." The field's meaning was effectively inverted.
- **`health_disease_stat`→`host_disease_stat`**: v5 = "health or disease status"; v6 = "list of diseases diagnosed." Rename + redefinition together.
- **`propagation`**: expanded and re-scoped (phage/virus/plasmid/eukaryote reproduction types).
- **`specific_host`**: narrowed to "host's taxonomic name and/or NCBI taxonomy ID."
- Generalizations: `compl_appr` (SAG/MAG → any genomic assembly), `salinity` (water → liquid or solid), `freq_clean` (building/week → any sample location, any cadence), `samp_size` / `samp_vol_we_dna_ext` (units clarified), `depth` (v5 punted to package docs; v6 gives a real definition), `host_sex` ("physical sex" → "gender or physical sex").
- `url`: v5 description was empty; v6 supplies one (previously-undocumented field now documented).
- `votu_class_appr` / `votu_db` / `votu_seq_comp_appr`: definitions change vOTU→OTU to match the renames above.

**Cosmetic changes (grouped).** Around 20 of the 65 entries are text-only edits with no change of meaning:
- **Mojibake / encoding cleanup** (v5 had `‚Äô`, `¬†`, `¬∞` artifacts from the xlsx export): `alt`, `pour_point`, `viscosity`, and others where the only diff is a curly apostrophe or non-breaking space becoming clean text.
- **Double-space collapsed to single space**: `chem_treatment`, `fungicide_regm`, `hcr`, `iw_bt_date_well`, `pcr_cond`, `samp_collection_point`, `vir_ident_software`, and more.
- **Trailing period added**: `biol_stat`, `elev`, `host_family_relationship`, `host_infra_specific_name`, `host_substrate`, `ref_biomaterial`, `temp`, `texture_meth`, `tvdss_of_hcr_temp`, `tvdss_of_hcr_pressure`.

These are reported as three grouped mass-edits, not ~20 separate changes.

## Notes (judgment calls and data-quality flags)

- **Near-duplicate new slot names.** The added list contains what look like three spellings of one concept: `samp_collec_method`, `samp_collect_method`, and `sample_collec_method`; plus two "sample name" spellings: `samp_name` and `sample_name`; and `samp_collec_device` alongside them. These are probably the same measurement named inconsistently across packages. A maintainer should confirm whether they are intentional distinct fields or accidental variants.
- **Copy-paste bug in `gastrointest_disord`.** Its v6 definition contains a stray "History of blood disorders; can include multiple disorders." pasted in from `blood_blood_disord`. Introduced in v6, worth a fix upstream.
- **`health_disease_stat` / `host_disease_stat` double-accounting.** `health_disease_stat→host_disease_stat` appears as a rename, and both names also appear under `definition_changed`. Reading it as a single rename-plus-redefinition (not two independent slot edits) avoids overcounting.
- **`geo_loc_name`** dropped the GAZ ontology version pin "(v 1.512)"; minor content deletion, not cosmetic.
- **No cardinality, range, or pattern data** is present in this diff shape, so those sections are omitted. If those changed between v5 and v6, they are not captured here.
