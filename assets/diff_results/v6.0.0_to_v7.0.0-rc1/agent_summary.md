# MIxS schema diff: mixs6.0.0 (2022-03-24) to main / 7.0.0-rc1 (2026-07-28)

Source: `assets/diff_results/v6.0.0_to_v7.0.0-rc1/schema_comparison_results.yaml`
(old commit `74744ee`, new commit `1591e32`).

Four years of change. The raw counts (409 new slots, 553 range changes, 287 class
renames) overstate the amount of new content and understate a few things that
will actually break consumers. What follows sorts them.

## The five changes that explain most of the diff

1. **Every class and enum was renamed to CamelCase.** 287 of 287 classes and 125
   of 125 enums are renamed, not removed. `MIGS bacteria` -> `MigsBa`,
   `soil MIMS` -> `MimsSoil`, `assembly_qual_enum` -> `AssemblyQualEnum`. Nothing
   about the content of those classes is in this diff (see Caveats).
2. **The `quantity value` class was deleted and replaced by string plus regex.**
   173 slots moved from `range: quantity value` to `range: string`, and 178 of
   them gained the same numeric structured pattern
   (`^{scientific_float}( *- *{scientific_float})? *{text}$`). 6 more went to
   `float`. This, plus similar work elsewhere, accounts for 296 of the 301
   pattern changes and all 33 new `settings` entries (`scientific_float`, `unit`,
   `termID`, `text`, and so on) that the structured patterns interpolate.
3. **344 of the 409 "new" slots are generated container slots, not new terms.**
   Everything ending in `_data` (`mims_soil_data`, `migs_ba_air_data`, ...) is a
   slot on the new `MixsCompliantData` class, one per non-abstract class. Only
   **65** genuinely new terms were added.
4. **"Package" became "Extension".** Old subsets `checklist` and `package` are
   gone, replaced by abstract classes `Checklist` and `Extension`; the
   `checklist_package_combination` subset became `combination_classes`; and the
   253 combination-class descriptions were rewritten from
   "Combinatorial checklist X with environmental package Y" to
   "MIxS Data that comply with the X checklist and the Y Extension".
5. **Two new checklists (MISIP variants) and one new extension (Ancient).** The
   60 new classes are: 4 structural (`Checklist`, `Extension`, `Ancient`,
   `MixsCompliantData`), `MimarksCMisip` plus its 23 extension combinations,
   `MimsMisip` plus its 23, and 8 `Mims*Ancient` combinations. Ancient only
   combines with MIMS, and only for 8 extensions (host-associated,
   human-associated, human gut/oral/skin, plant-associated, sediment, soil).

## Things that will break or silently change consumers

**The term URI base changed.** The `MIXS` prefix went from
`https://w3id.org/mixs/terms/` to `https://w3id.org/mixs/`, and the schema `id`
from `http://w3id.org/mixs` to `https://w3id.org/mixs`. Every `slot_uri` in the
schema resolves to a different IRI than it did in v6.0.0. This is one line in the
diff and the highest-impact item in it.

**Two v6.0.0 checklist descriptions were simply wrong and are now fixed.** These
are class identity corrections, not wording changes:

| class | v6.0.0 description | v7 description |
|---|---|---|
| `MIGS plant` -> `MigsPl` | Minimal Information about a Genome Sequence: plant | ...: **plasmid** |
| `MIGS org` -> `MigsOrg` | ...: org | ...: **organelle** |
| `MIGS virus` -> `MigsVi` | ...: cultured bacteria/archaea | ...: **virus** |
| `MIMARKS specimen` -> `MimarksC` | Minimal Information about a Marker **Specimen** | ...Marker **Sequence** |
| `MIMARKS survey` -> `MimarksS` | Minimal Information about a Marker **Specimen** | ...Marker **Sequence** |

Anyone who read "MIGS plant" as the plant-genome checklist (rather than plasmid)
was using it incorrectly under v6.0.0.

**Two slot descriptions reverse the meaning of the field.** Both are size
fractionation, both flipped which side of the threshold is excluded:

- `size_frac_low`: "Materials **larger** than the size threshold are excluded"
  -> "Materials **smaller** than the size threshold are excluded"
- `size_frac_up`: "Refers to the mesh/pore size used to retain the sample.
  Materials **smaller** than the threshold are excluded" -> "Mesh or pore size of
  the device used to retain the sample. Materials **larger** than the threshold
  are excluded"

Data recorded against the v6.0.0 wording of these two slots means the opposite of
what v7 says it means.

## Added

**Classes (60)** and **subsets (4: `environment`, `investigation`,
`nucleic acid sequence source`, `sequencing`)** are described above. The four new
subsets replace four of the six removed grouping slots (`environment field`,
`investigation field`, `nucleic acid sequence source field`, `sequencing field`).

**Slots: 65 new terms** (excluding the 344 `*_data` containers). They cluster
into a small number of themes rather than being scattered:

- **Stable isotope probing / isotopolog (14):** `isotope`, `isotopolog`,
  `isotopolog_approach`, `isotopolog_atom_frac`, `isotopolog_atom_pos`,
  `isotopolog_dose`, `isotopolog_incu_time`, `isotopolog_label`,
  `nucleobase_atom_frac`, `internal_standard`, `sip_method`, plus the density
  gradient trio `gradient_position`, `gradient_pos_density`,
  `gradient_pos_rel_am`.
- **Ancient DNA / palaeo (14):** `chrono_age_protocol`, `chrono_age_remarks`,
  `earliest_chrono_age`, `earliest_chrono_sys`, `latest_chrono_age`,
  `latest_chrono_sys`, `geological_epoch`, `cultural_era`, `stratigraph_context`,
  `past_env_broad`, `past_env_local`, `palaeopath_status`, `damage_treatment`,
  `host_preserv_state`. Matches the new `Ancient` extension.
- **Permits and provenance (11):** `permit_authority`, `permit_date`,
  `permit_id`, `permit_scope`, `biocultural_label`, `prev_pubs`,
  `orig_site_name`, `orig_site_loc`, `orig_site_lat`, `orig_site_lon`,
  `context_retrieval_date`. This is new territory for MIxS: legal and ethical
  provenance rather than sample measurement.
- **Library prep / capture detail (11):** `lib_gener_technique`, `lib_mid_desc`,
  `lib_polymerase`, `lib_strandedness`, `library_name`, `capt_pcr_cyc_tot`,
  `capt_probe_desc`, `capt_probe_src_taxid`, `reamp_pcr_cyc_tot`,
  `sop_lib_preparation`, `sop_experimental`.
- **Sample handling identifiers (8):** `batch_ids`, `samp_alt_lab_ids`,
  `samp_category`, `samp_decont_pretreat`, `samp_dna_conc`, `samp_preserv_treatm`,
  `nucl_acid_extr_date`, `nucleic_acid_elution_vol`.
- **Remainder (7):** `estimated_genome_size`, `marker_gene_recov`,
  `marker_gene_recov_sw`, `reads_removed`, `data_preproc_desc`,
  `nose_mouth_teeth_throat_disord`, `urobiom_sex`.

**Enums (27 new):** `AeroStrucEnum`, `BioCulturalLabelEnum`, `BuiltStrucSetEnum`,
`CeilStrucEnum`, `ChronoAgeProtocolEnum`, `ChronoAgeSysEnum`,
`DamageTreatmentEnum`, `FireplaceTypeEnum`, `GeolEpochEnum`,
`HostDependenceEnum`, `InsdcMissingValueEnum`, `IsotopeEnum`,
`IsotopologApproachEnum`, `IsotopologLabelEnum`, `LibStrandEnum`, `LibTypeEnum`,
`MoldVisibilityEnum`, `SampCategoryEnum`, `SeasonEnum`, `SeqQualityCheckEnum`,
`ShadingDeviceLocEnum`, `SpaceTypStateEnum`, `SymLifeCycleTypeEnum`,
`UrineCollectMethEnum`, `UrobiomSexEnum`, `WgaAmpApprEnum`, `WindowStatusEnum`.
`InsdcMissingValueEnum` is worth noting: it brings the INSDC missing-value
vocabulary into the schema itself.

**Prefixes (7 new):** `NCIT`, `SO`, `chrono`, `dc`, `schema`, `shex`, `xsd`.

**Settings (33 new):** all of them structured-pattern building blocks
(`DOI`, `PMID`, `URL`, `scientific_float`, `unit`, `termID`, `termLabel`,
`text`, `timestamp`, `duration`, `software`, `lat`, `lon`, ...).

## Removed

**Classes (2):** `core` and `quantity value`. Both were structural. `core` was
the abstract parent holding the field-grouping slots; `quantity value` was the
value/unit wrapper now replaced by string plus pattern.

**Slots (18).** Split by why:

- *Grouping slots from the deleted `core` class (6):* `core field`,
  `environment field`, `investigation field`, `mixs extension field`,
  `nucleic acid sequence source field`, `sequencing field`. Four became subsets;
  `core field` and `mixs extension field` have no successor.
- *Slots of the deleted `quantity value` class (3):* `has numeric value`,
  `has raw value`, `has unit`.
- *Genuine term removals (9):* `estimated_size`, `salinity_meth`,
  `samp_salinity`, `soil_depth`, `soil_text_measure`, `texture_meth`,
  `tot_n_meth`, `tot_phos`, `url`. See "Possible missed renames" below; several
  of these look like renames rather than deletions.

**Enums (27).** Only 3 were folded into a surviving enum
(`door_loc_enum`, `wall_loc_enum`, `window_loc_enum` -> `CompassDirections8Enum`,
visible only through the slot range changes, not through the rename map). The
other **18 dropped enums became unconstrained text**, listed under
"Cardinality and range changes". The remaining 6 (`add_recov_method_enum`,
`assembly_software_enum`, `compl_score_enum`, `food_quality_date_enum`,
`pres_animal_insect_enum`, `samp_purpose_enum`) were not referenced as a slot
range in v6.0.0 and simply disappear.

**Prefixes (2):** `MIGS`, `mixs.vocab`.
**Subsets (2):** `checklist`, `package` (now classes).
**Imports (25):** every per-package module (`agriculture`, `air`, ... `water`).
v7 is a single schema file.

## Renamed

**Classes: all 287**, mechanically. Package-prefix word order flipped and
CamelCased: `soil MIGS bacteria` -> `MigsBaSoil`, `hydrocarbon resources-cores
MIUVIG` -> `MiuvigHydrocarbonResourcesCores`. Checklist abbreviations
regularized: `MIMARKS specimen` -> `MimarksC`, `MIMARKS survey` -> `MimarksS`,
`MIGS bacteria` -> `MigsBa`.

**Enums: all 125**, of which 108 are pure `snake_case_enum` ->
`CamelCaseEnum`. The other 17 are real consolidations or retitles:

| collapsed into | from |
|---|---|
| `DamagedEnum` | `ceil_cond_enum`, `floor_cond_enum`, `int_wall_cond_enum` |
| `DamagedRupturedEnum` | `door_cond_enum`, `shading_device_cond_enum`, `window_cond_enum` |
| `CompassDirections8Enum` | `ext_wall_orient_enum`, `ext_window_orient_enum` |
| `GeolAgeEnum` | `hcr_geol_age_enum`, `sr_geol_age_enum` |
| `SoilHorizonEnum` | `horizon_enum`, `soil_horizon_enum` |
| `CeilingWallTextureEnum` | `ceil_texture_enum`, `wall_texture_enum` |

plus four retitles: `contam_screen_param_enum` -> `ContamScreenInputEnum`,
`pred_genome_type_enum` -> `ViralGenomeTypeEnum` (and it gained a description,
"Types of viral genomes based on Baltimore classification"),
`single_cell_lysis_appr_enum` -> `ScLysisApproachEnum`, `heat_deliv_loc_enum` ->
`HeatSysDelivMethEnum` (questionable, see Notes). Net: 125 old enums to 117 new
names.

**Slots: 26 mappings, but only 10 are renames.** The other **16 are merges of
near-duplicate slots that both existed in v6.0.0**. This is the most useful thing
in the slot rename map and it does not read as a merge anywhere else in the diff:

| v6.0.0 had both | v7 keeps |
|---|---|
| `sample_name` + `samp_name` | `samp_name` |
| `samp_collec_method` + `sample_collec_method` + `samp_collect_method` | `samp_collect_method` |
| `samp_collec_device` + `samp_collect_device` | `samp_collect_device` |
| `samp_stor_dur` + `samp_store_dur` | `samp_store_dur` |
| `samp_stor_loc` + `samp_store_loc` | `samp_store_loc` |
| `samp_stor_temp` + `samp_store_temp` | `samp_store_temp` |
| `assembly_quality` + `assembly_qual` | `assembly_qual` |
| `air particulate matter concentration` + `air_PM_concen` | `air_PM_concen` |
| `Food_Product_type` + `food_product_type` | `food_product_type` |
| `Food_source` + `food_source` | `food_source` |
| `horizon` + `soil_horizon` | `soil_horizon` |
| `microbial_biomass_meth` + `micro_biomass_meth` | `micro_biomass_meth` |
| `non_mineral_nutr_regm` + `non_min_nutr_regm` | `non_min_nutr_regm` |
| `previous_land_use_meth` + `prev_land_use_meth` | `prev_land_use_meth` |
| `tot_car` + `tot_carb` | `tot_carb` |
| `host_family_relation` + `host_family_relationship` | `host_fam_rel` |

True renames (10), all abbreviation tightening or prefix fixes:
`associated resource` -> `associated_resource`,
`host_infra_specific_name` -> `host_infra_spec_name`,
`host_infra_specific_rank` -> `host_infra_spec_rank`,
`single_cell_lysis_appr` -> `sc_lysis_approach`,
`single_cell_lysis_prot` -> `sc_lysis_method`,
`texture` -> `soil_texture`,
`x_16s_recover` -> `x16s_recover`,
`x_16s_recover_software` -> `x16s_recover_software`.

**Subsets (1):** `checklist_package_combination` -> `combination_classes`.

## Possible missed renames

This diff shape has no `rename_candidates` block, so the following are my own
nearest-name matches against the surviving slot set. A maintainer should confirm
each and promote the real ones into the tool's rename map, because right now they
are reported as removals:

| removed | likely successor | confidence |
|---|---|---|
| `estimated_size` | `estimated_genome_size` (new) | high |
| `texture_meth` | `soil_texture_meth` (existing) | high |
| `soil_text_measure` | `soil_texture_meth` or `soil_texture_class` (existing) | medium |
| `tot_n_meth` | `tot_nitro_cont_meth` (existing) | medium |
| `tot_phos` | `tot_phosp` or `tot_phosphate` (both existing) | medium |
| `samp_salinity` | `salinity` (existing) | medium |
| `salinity_meth` | no clear successor | low |
| `soil_depth` | `depth` (existing) | low |
| `url` | no successor found | low |

Of the removed enums, none has a CamelCase counterpart in the new schema, which
supports reading them as genuine removals rather than missed renames. The three
`*_loc_enum` cases are the exception: they are real consolidations into
`CompassDirections8Enum` that the rename map does not record.

## Cardinality and range changes

**Gained `required: true` (35 slots), where v6.0.0 had none at the slot level:**
`abs_air_humidity`, `add_recov_method`, `api`, `basin`, `build_occup_type`,
`building_setting`, `coll_site_geo_feat`, `collection_date`, `env_broad_scale`,
`env_local_scale`, `env_medium`, `filter_type`, `geo_loc_name`, `hc_produced`,
`hcr`, `heat_cool_type`, `IFSAC_category`, `indoor_space`, `iwf`, `lat_lon`,
`light_type`, `occup_density_samp`, `occup_samp`, `project_name`,
`rel_air_humidity`, `samp_collect_point`, `samp_name`, `samp_taxon_id`,
`samp_type`, `seq_meth`, `space_typ_state`, `sym_life_cycle_type`,
`typ_occup_density`, `water_cut`. (`samp_name` is required both under its own
name and as the target of the `sample_name` merge.)

**Became multivalued (11):** `biotic_regm`, `env_medium`, `experimental_factor`,
`food_dis_point_city`, `host_spec_range`, `solar_irradiance`, `sop`,
`source_mat_id`, `ventilation_type`, `associated_resource` (from
`associated resource`), `host_fam_rel` (from `host_family_relationship`).

**Stopped being multivalued (5):** `soil_temp`, `food_clean_proc`,
`farm_water_source`, `food_product_type`, `photosynt_activ`. These narrow what
was previously valid.

**Range changes (553 total):**

| change | count | note |
|---|---|---|
| enum renamed | 123 | naming only; permissible values not compared |
| `quantity value` -> `string` | 173 | class deleted; 178 slots gained the numeric pattern |
| `quantity value` -> `float` | 6 | `iwf`, `animal_am_freq`, `carb_nitro_ratio`, `season_humidity`, `surf_humidity`, `rel_air_humidity` |
| `string` -> absent | 158 | no effect; `default_range: string` is now declared schema-wide |
| `date` -> `datetime` | 17 | `collection_date`, `cult_isol_date`, `date_extr_weath`, `date_last_rain`, `douche`, `extreme_event`, `fertilizer_date`, `fire`, `flooding`, `hrt`, `iw_bt_date_well`, `last_clean`, `menarche`, `menopause`, `pregnancy`, `prod_start_date`, `cons_purch_date` |
| `double` -> `float` | 9 | all pH slots plus occupancy density |
| `integer` -> `string` | 8 | `number_resident`, `max_occup`, `freq_cook`, `room_occup`, `exp_pipe`, `host_occupation`, `number_plants`, `number_pets` (loosens) |
| `integer`/`double`/`quantity value` -> absent | 5 | loosens to string |
| `integer` -> `float`, `double` -> `string` | 2 | `occup_samp`, `timepoint` |
| `string` -> `boolean` | 6 | `hysterectomy`, `twin_sibling`, `smoker`, `reassembly_bin`, `medic_hist_perform`, `x16s_recover` (tightens) |
| `string` -> new enum | 21 | tightens; `assembly_qual`, `contam_screen_input`, `heat_sys_deliv_meth`, `season`, `aero_struc`, `urine_collect_meth`, `host_dependence`, `fireplace_type`, `built_struc_set`, `seq_quality_check`, `shading_device_loc`, `window_status`, `ceil_struc`, `wga_amp_appr`, `sym_life_cycle_type`, `space_typ_state`, and the 5 `*_water_mold` slots (ceil, door, shad_dev, wall, window) |
| `string` -> `float` | 3 | tightens |
| `*_loc_enum` -> `CompassDirections8Enum` | 4 | `door_loc`, `wall_loc`, `window_loc`, `heat_deliv_loc`; a consolidation the rename map does not record |
| **enum -> absent (free text)** | **18** | **loosens; listed below** |

The 18 slots that lost their enumeration and are now unconstrained text:
`cur_land_use`, `decontam_software`, `door_type_wood`, `drug_usage`,
`floor_finish_mat`, `host_sex`, `microb_start_count`, `organism_count`,
`plant_growth_med`, `room_type`, `samp_md`, `source_uvig`, `special_diet`,
`spikein_count`, `vis_media`, `water_source_shared`, plus `samp_floor` and
`study_complt_stat`, which at least gained a regex in exchange. Spot-checking
`organism_count` in the v7 source confirms it now carries only an advisory
`string_serialization`, no `range` and no `pattern`. Sixteen previously
enumerated fields becoming free text is the largest validation loosening in this
release and is not visible in any headline count.

## Pattern changes

301 slots changed `pattern`: **296 added**, 4 removed, 1 modified. Note these are
LinkML-materialized patterns; in the v7 source most are `structured_pattern`
blocks interpolating the 33 new `settings`.

Added patterns, by shape:

| count | what it constrains |
|---|---|
| 178 | numeric value or range, optional units: `^{scientific_float}( *- *{scientific_float})? *{text}$` (the `quantity value` replacement) |
| 32 | PMID / DOI / URL citation form (24 single-valued, 8 a variant) |
| 19 | ontology term as `label [PREFIX:id]` |
| 13 | positive integer followed by free text |
| 9 | ISO 8601 duration |
| 26 | assorted composite forms: `term;value unit` (7), three semicolon-separated terms (6), `term [ID]` or integer (5), free text or `term [ID]` (4), numeric range with unit (3), and singletons including a floor-number pattern for `samp_floor` |

Removed patterns (4), each a loosening: `compl_score`
(`^(high|med|low);(0|[0-9]{1,2}|100)%$`), `contam_screen_param`
(`^(ref db|kmer|coverage|combination);.+`), `pres_animal_insect`
(`^(cat|dog|rodent|snake|other);\d+$`), `food_quality_date`
(`^(best by|best if used by|freeze by||use by);YYYY-MM-DD$`).

Modified (1): `add_recov_method` kept its controlled first field and replaced a
sprawling ISO 8601 date alternation with a simpler, stricter one.

## Title changes

ENA uses MIxS titles as controlled nomenclature, so these are listed individually.

**All 287 renamed classes gained a title; none had one in v6.0.0.** Titles are
generated: `MigsBaAgriculture` -> "MigsBa combined with Agriculture", `Air` ->
"air", `MigsBa` -> "MIGS bacteria". Note the combination-class titles are built
from the *new* CamelCase class names, so the human-readable label is now
"MigsBa combined with Agriculture" rather than anything resembling the v6.0.0
class name "agriculture MIGS bacteria".

**Slot titles changed (12):**

| slot | v6.0.0 title | v7 title |
|---|---|---|
| `nose_throat_disord` | lung/nose-throat disorder | nose throat disorder |
| `sieving` | composite design/sieving | sieving |
| `horizon_meth` | soil horizon method | horizon method |
| `samp_taxon_id` | Taxonomy ID of DNA sample | taxonomy ID of DNA sample |
| `samp_transport_cont` | sample transport&nbsp;&nbsp;container (double space) | sample transport container |
| `food_trav_vehic` | Food shipping transportation vehicle | food shipping transportation vehicle |
| `host_of_host_env_med` | host of the symbiotic host environemental medium | host of the symbiotic host environmental medium |
| `air_PM_concen` (was `air particulate matter concentration`) | air_PM_concen | air particulate matter concentration |
| `food_product_type` (was `Food_Product_type`) | Foodon product type | food product type |
| `food_source` (was `Food_source`) | Food source | food source |
| `soil_horizon` (was `horizon`) | horizon | soil horizon |
| `soil_texture` (was `texture`) | texture | soil texture |

Four of these (`nose_throat_disord`, `sieving`, `horizon_meth`,
`food_product_type`) change what the title asserts, not just its case. The
`air_PM_concen` row is the interesting one: the merge swapped which of the two
duplicate slots supplied the title, so the machine name and the title effectively
traded places.

## Cosmetic changes (grouped)

- **628 slots dropped a redundant `multivalued: false`.** No semantic effect;
  `false` is the LinkML default. This alone is 97% of the 644 `multivalued`
  changes.
- **158 slots dropped an explicit `range: string`.** No semantic effect; v7
  declares `default_range: string` schema-wide, which v6.0.0 did not.
- **236 slot descriptions differ only in trailing punctuation or capitalization**,
  almost all of them a stripped trailing period. Example: `samp_purpose`,
  "The reason that the sample was collected." -> "The reason that the sample was
  collected".
- **253 combination-class descriptions were reworded by template** from
  "Combinatorial checklist X with environmental package Y" to "MIxS Data that
  comply with the X checklist and the Y Extension".
- **22 extension classes replaced a description that just repeated the class name
  with real prose.** Example: `air`, description "air" -> "A collection of terms
  appropriate when collecting and sequencing samples obtained from a gaseous
  environment...".
- **6 slot descriptions are mojibake repairs**, non-breaking spaces and degree
  signs that had been mangled: `api`, `root_med_suppl`, `root_med_micronutr`,
  `root_med_macronutr`, `root_med_regl`, `samp_transport_cond`.
- **25 slot descriptions are typo or grammar fixes** with no change of meaning:
  `animal_am_route` (adminstered), `diss_oxygen_fluid` (oxgen),
  `food_source_age` (organim), `samp_transport_cont` (Conatiner), and 21 others.

That leaves **26 slot descriptions with substantive rewrites**, of which the two
size-fraction reversals are called out above. The rest are clarifications
(`alt`, `depth`, `pcr_cond`, `host_body_site`, `host_body_product`, `season`,
`store_cond`, `lat_lon` now capping latitude/longitude at 8 decimal places,
`samp_name` rewritten around material-sample identity).

## Notes and judgment calls

1. **The diff compares only 8 fields:** `name`, `description`, `title`,
   `meaning`, `pattern`, `range`, `required`, `multivalued`
   (`src/scripts/diff_two_linkml_mixs_releases.py:171`). It does **not** compare
   `is_a`, `mixins`, class `slots` lists, `slot_usage`, enum permissible values,
   `slot_uri`, `annotations`, `examples`, `comments`, `keywords`, or
   `string_serialization`. So "125 enums renamed" says nothing about whether
   their members changed, and the class-level story here is names and
   descriptions only. A structural comparison is still needed before calling this
   release reviewed.
2. **`heat_deliv_loc_enum -> HeatSysDelivMethEnum` in the enum rename map looks
   wrong.** The slot `heat_deliv_loc` actually moved to `CompassDirections8Enum`,
   while `HeatSysDelivMethEnum` is the new range of a different slot,
   `heat_sys_deliv_meth`, which was `string` in v6.0.0. I would treat
   `heat_deliv_loc_enum` as consolidated into `CompassDirections8Enum` alongside
   `door_loc_enum`, `wall_loc_enum`, and `window_loc_enum`, and drop that map
   entry.
3. **The `required: true` readings are slot-level only.** MIxS expresses most
   requirement rules per class via `slot_usage`, which this tool does not
   compare. The 35 slots above gained a top-level requirement; that is not the
   same as saying 35 fields became mandatory where they were not before, and it
   is not the same as saying nothing else changed.
4. **The schema itself flags a collision:** the new schema's `comments` say
   "slot titles that are associated with more than one slot name/SCN: host sex".
   Worth resolving before release, given the ENA title dependency.
5. **`main` is not a tag.** This diff compares `mixs6.0.0` to the `main` branch at
   commit `1591e32`, whose declared `version` is `7.0.0-rc1`. The sibling
   `v6.0.0_to_v7.0.0` folder may point at a different commit; re-run against the
   release tag before publishing anything from this.
6. I could not classify `url` (removed slot) or `salinity_meth` against any
   surviving slot, and I did not attempt to trace the 6 dropped enums that were
   never used as a slot range in v6.0.0.
