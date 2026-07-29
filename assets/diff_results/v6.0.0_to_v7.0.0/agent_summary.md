# MIxS 6.0.0 to 7.0.0: schema diff summary

Compares `mixs6.0.0` (2022-03-24, `74744ee`) to `main` (2026-07-29, `60b48ef`), whose
`version` is `7.0.0`. Source: `schema_comparison_results.yaml` in this folder.

## Read the headline numbers with care

The tool counts 409 new slots, 60 new classes, 770 slot definition changes and 287 class
definition changes. Almost all of that is one refactor, not new metadata content:

- **344 of the 409 "new" slots (84%) are `*_data` container slots**, one per
  checklist-by-extension combination class (`migs_ba_soil_data`, `mimarks_c_misip_water_data`,
  and so on). Each has `domain: MixsCompliantData`, `range: <the combination class>`,
  `multivalued: true`, `inlined: true`. They are the machinery for a new top-level
  `MixsCompliantData` holder class. Only **65 new slots are actual metadata terms**.
- **All 287 class definition changes are renames.** Every one has an entry in
  `expected_mappings`, and the only fields that differ are `name`, `class_uri` (287 classes
  gained one), `title` (287 gained one) and `description` (281).
- **All 125 enum definition changes are renames too** (`snake_case_enum` to `CamelCaseEnum`).
  Only one has any other change: `pred_genome_type_enum -> ViralGenomeTypeEnum` also changed
  its description.
- **628 of the 644 `multivalued` changes and 158 of the 553 `range` changes are the diff
  seeing a dropped-but-unchanged default.** v7 sets `default_range: string` at the schema
  level and stops writing `multivalued: false` explicitly, so `range: string -> (absent)` and
  `multivalued: false -> (absent)` mean nothing changed.

What the numbers understate: the 26 confirmed slot renames plus at least two unmapped ones
(below) would otherwise read as removals of terms that in fact survived.

## Added

### Classes (60)

| Group | Count | What it is |
|---|---|---|
| `MimsMisip*` | 24 | New MIMS-MISIP checklist ("Metagenome or Environmental with SIP") plus its 23 extension combinations |
| `MimarksCMisip*` | 24 | New MIMARKS specimen-MISIP checklist plus its 23 extension combinations |
| `Mims*Ancient` | 8 | The new `Ancient` extension combined with MIMS host-associated, human-associated, human-gut, human-oral, human-skin, plant-associated, sediment, soil |
| `Ancient` | 1 | New extension for degraded/ancient nucleic acids (alias `minas`) |
| `Checklist`, `Extension`, `MixsCompliantData` | 3 | Structural classes with no v6 counterpart. `Extension` carries alias `EnvironmentalPackage` |

So the substantive additions are two checklists (MIMS-MISIP, MIMARKS-specimen-MISIP) and one
extension (Ancient); the other 56 classes are combinations and scaffolding.

### Slots: 344 combination containers + 65 real terms

The 65 real terms fall into four coherent themes, each arriving with its own enums:

**Ancient DNA and palaeogenomics (16 terms)** — matches the new `Ancient` extension:
`biocultural_label`, `chrono_age_protocol`, `chrono_age_remarks`, `context_retrieval_date`,
`cultural_era`, `damage_treatment`, `earliest_chrono_age`, `earliest_chrono_sys`,
`geological_epoch`, `host_preserv_state`, `latest_chrono_age`, `latest_chrono_sys`,
`palaeopath_status`, `past_env_broad`, `past_env_local`, `stratigraph_context`.
New enums: `BioCulturalLabelEnum`, `ChronoAgeProtocolEnum`, `ChronoAgeSysEnum`,
`DamageTreatmentEnum`, `GeolEpochEnum`. New prefix `chrono:` (TDWG chronometric-age terms).

**Stable isotope probing (14 terms)** — matches the new MISIP checklists:
`gradient_position`, `gradient_pos_density`, `gradient_pos_rel_am`, `internal_standard`,
`isotope`, `isotopolog`, `isotopolog_approach`, `isotopolog_atom_frac`,
`isotopolog_atom_pos`, `isotopolog_dose`, `isotopolog_incu_time`, `isotopolog_label`,
`nucleobase_atom_frac`, `sip_method`.
New enums: `IsotopeEnum`, `IsotopologApproachEnum`, `IsotopologLabelEnum`.

**Library prep, capture enrichment and read processing (14 terms)**:
`capt_pcr_cyc_tot`, `capt_probe_desc`, `capt_probe_src_taxid`, `reamp_pcr_cyc_tot`,
`lib_gener_technique`, `lib_mid_desc`, `lib_polymerase`, `lib_strandedness`, `library_name`,
`sop_lib_preparation`, `reads_removed`, `data_preproc_desc`, `marker_gene_recov`,
`marker_gene_recov_sw`. New enums: `LibStrandEnum`, `LibTypeEnum`.

**Sample provenance, permits and identifiers (18 terms)**:
`permit_authority`, `permit_date`, `permit_id`, `permit_scope`, `orig_site_lat`,
`orig_site_lon`, `orig_site_loc`, `orig_site_name`, `batch_ids`, `samp_alt_lab_ids`,
`samp_category`, `samp_decont_pretreat`, `samp_dna_conc`, `samp_preserv_treatm`,
`nucl_acid_extr_date`, `nucleic_acid_elution_vol`, `prev_pubs`, `sop_experimental`.
New enum: `SampCategoryEnum`.

The remaining three: `estimated_genome_size` (see missed renames), plus
`nose_mouth_teeth_throat_disord` and `urobiom_sex`.

### Enums (27 new)

The four theme clusters above account for 12. The rest are enumerations replacing free text
on existing slots (see "range changes"), plus `InsdcMissingValueEnum` (INSDC missing-value
vocabulary) and consolidations such as `MoldVisibilityEnum`, reused by five mold slots.

### Prefixes (7 new), settings (33 new), subsets (4 new)

New prefixes: `NCIT`, `SO`, `chrono`, `dc`, `schema`, `shex`, `xsd`.
The 33 new `settings` (`float`, `unit`, `termID`, `termLabel`, `software`, `version`,
`duration`, `timestamp`, ...) are interpolation variables for LinkML `structured_pattern`,
which v7 uses 307 times. This is the mechanism behind the 296 added `pattern` values.

New subsets: `environment`, `investigation`, `nucleic acid sequence source`, `sequencing`.

## Removed

**Classes (2):** `core`, `quantity value`. The removal of `quantity value` is the single
largest driver in the whole diff (173 range changes, 178 added patterns) and is discussed
below.

**Slots (18), in four groups:**

| Group | Slots | Status |
|---|---|---|
| Grouping slots turned into subsets | `environment field`, `investigation field`, `nucleic acid sequence source field`, `sequencing field` | Recorded in `assets/between_diff_mappings/6_to_pre_7/inter_type_refactoring.tsv` as slot-to-subset conversions |
| Grouping slots with no recorded fate | `core field`, `mixs extension field` | Same shape as the four above but absent from `inter_type_refactoring.tsv` |
| Attributes of the removed `quantity value` class | `has numeric value`, `has raw value`, `has unit` | Gone with the class |
| Recorded deletions | `soil_text_measure`, `texture_meth`, `tot_n_meth`, `tot_phos`, `url` | Listed in `slot_name_mappings.tsv` with an empty target |
| Not recorded anywhere | `estimated_size`, `soil_depth`, `samp_salinity`, `salinity_meth` | See missed renames |

The five "recorded deletions" are not really deletions: **each was a v6 duplicate sharing a
MIXS URI with another v6 slot, and v7 kept one of the pair.** Verified from the v6
`terms.yaml` and v7 `src/mixs/schema/mixs.yaml`:

| v6 duplicate pair | Shared URI | v7 survivor |
|---|---|---|
| `soil_text_measure`, `texture` | MIXS:0000335 | `soil_texture` |
| `texture_meth`, `soil_texture_meth` | MIXS:0000336 | `soil_texture_meth` |
| `tot_n_meth`, `tot_nitro_cont_meth` | MIXS:0000338 | `tot_nitro_cont_meth` |
| `tot_phos`, `tot_phosphate` | MIXS:0000689 | `tot_phosphate` |
| `url`, `associated resource` | MIXS:0000091 | `associated_resource` |

In each case the mapping file records the surviving name as a rename target for one member of
the pair and blanks the other. That is defensible, but a consumer reading the diff alone sees
five term deletions where the identifier actually survived under a different label.

**Enums (27 removed).** 18 belong to slots that dropped their enumerated range entirely (see
range changes); the other 9 (`add_recov_method_enum`, `assembly_software_enum`,
`compl_score_enum`, `door_loc_enum`, `food_quality_date_enum`, `pres_animal_insect_enum`,
`samp_purpose_enum`, `wall_loc_enum`, `window_loc_enum`) belong to slots that moved to
pattern-constrained strings.

**Subsets (2):** `checklist`, `package` (`package` is now expressed as the `Extension` class,
which carries the alias `EnvironmentalPackage`).

## Renamed

**Classes: 287 renames, all following one convention** — space-separated lowercase names
become CamelCase, with the checklist abbreviated:
`MIGS bacteria -> MigsBa`, `MIGS eukaryote -> MigsEu`, `MIGS org -> MigsOrg`,
`MIGS plant -> MigsPl`, `MIGS virus -> MigsVi`, `MIMARKS specimen -> MimarksC`,
`MIMARKS survey -> MimarksS`, `MIMS -> Mims`, `MIMAG -> Mimag`, `MISAG -> Misag`,
`MIUVIG -> Miuvig`. Combination classes concatenate the two:
`agriculture MIGS bacteria -> MigsBaAgriculture`, with the checklist moving to the front.

**Enums: 125 renames**, all `snake_case_enum` to `CamelCaseEnum`. Six of the new names absorb
more than one old enum: `CeilingWallTextureEnum` (2), `SoilHorizonEnum` (2), `GeolAgeEnum` (2),
`CompassDirections8Enum` (2, from `ext_wall_orient_enum` + `ext_window_orient_enum`),
`DamagedEnum` (3), `DamagedRupturedEnum` (3). So 125 old enums map onto 117 new ones.

**Subsets: 1** — `checklist_package_combination -> combination_classes`.

**Slots: 26 confirmed renames**, driven by three consistent conventions rather than ad hoc
edits:

1. *Abbreviate to the established MIxS style*: `assembly_quality -> assembly_qual`,
   `microbial_biomass_meth -> micro_biomass_meth`, `previous_land_use_meth -> prev_land_use_meth`,
   `non_mineral_nutr_regm -> non_min_nutr_regm`, `host_infra_specific_name -> host_infra_spec_name`,
   `host_infra_specific_rank -> host_infra_spec_rank`, `host_family_relation -> host_fam_rel`,
   `single_cell_lysis_appr -> sc_lysis_approach`, `single_cell_lysis_prot -> sc_lysis_method`,
   `air particulate matter concentration -> air_PM_concen`, `tot_car -> tot_carb`.
2. *Normalize the `samp_` family*, expanding truncated stems and standardizing on `samp_`:
   `samp_collec_device -> samp_collect_device`, `samp_collec_method -> samp_collect_method`,
   `sample_collec_method -> samp_collect_method`, `sample_name -> samp_name`,
   `samp_stor_dur -> samp_store_dur`, `samp_stor_loc -> samp_store_loc`,
   `samp_stor_temp -> samp_store_temp`.
3. *Disambiguate generic names with a domain prefix*: `horizon -> soil_horizon`,
   `texture -> soil_texture`.

Plus mechanical identifier fixes: `x_16s_recover -> x16s_recover`,
`x_16s_recover_software -> x16s_recover_software`, `Food_Product_type -> food_product_type`,
`Food_source -> food_source`, `associated resource -> associated_resource`.

Two old names collapse into one new one in each of two cases: `host_family_relation` and
`host_family_relationship` both to `host_fam_rel`; `samp_collec_method` and
`sample_collec_method` both to `samp_collect_method`.

One rename also moved its identifier: `assembly_quality -> assembly_qual` changed
`slot_uri` from `MIXS:0000058` to `MIXS:0000056`. That is the only slot_uri change on a
renamed slot, and it deserves a maintainer's eye. Separately, `prod_label_claims` gained
`slot_uri: MIXS:0001337` where it previously had none.

## Possible missed renames

This diff has no `rename_candidates` section, so the following are my own findings, each
confirmed by MIXS URI identity between the v6 and v7 schema sources. **A maintainer should
confirm these and add the real ones to `assets/between_diff_mappings/6_to_pre_7/`.**

| v6 slot (reported as removed) | Shared URI | v7 slot (reported as added or shared) | Evidence |
|---|---|---|---|
| `estimated_size` | MIXS:0000024 | `estimated_genome_size` | Same URI. The class `cascaded` entries show `estimated_size` removed from exactly 144 classes and `estimated_genome_size` added to exactly 144. Not in `slot_name_mappings.tsv` at all. |
| `soil_depth` | MIXS:0000018 | `depth` | Same URI. `soil_depth` was a v6 duplicate of `depth`; v7 kept `depth`. Not in `slot_name_mappings.tsv` at all, not even as a blank-target deletion like the other four duplicate cleanups. |

`estimated_size -> estimated_genome_size` is the more consequential of the two: it is a real
rename of a live term across 144 classes, currently presented as one deletion plus one
addition.

Two further v6 slots have no v7 successor carrying their URI and appear to be genuine
retirements, but they are absent from the mapping files entirely, so nothing records the
decision: `samp_salinity` (MIXS:0000109) and `salinity_meth` (MIXS:0000341). Both were
dropped from 24 classes each. `salinity` (MIXS:0000183) survives, so a reader may reasonably
wonder whether these were meant to merge into it.

Finally, `core field` and `mixs extension field` look like the same slot-to-subset conversion
recorded for the other four grouping slots, but no target subset exists for either. Worth a
line in `inter_type_refactoring.tsv` even if the answer is "dropped".

## Cardinality and range changes

### The `quantity value` class is gone: 173 slots, the largest single change in the diff

v6 modeled measurements as a `quantity value` class with `has numeric value`, `has raw value`
and `has unit`. v7 removes the class and replaces it with pattern-constrained strings.
Concretely, **173 slots changed `range: quantity value -> string`** and 178 slots that
previously had `range: quantity value` gained the pattern
`^[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?( *- *[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)? *.*$`
(a number, or a numeric range, optionally followed by a unit). This covers the chemistry,
physical-measurement and morphometric terms: `temp`, `depth`, `alt`, `elev`, `salinity`,
`nitrate`, `phosphate`, `diss_oxygen`, `host_age`, `wind_speed`, `samp_size` and so on.

**This is a validation loosening, not a tightening.** A structured object with a typed numeric
field and a unit field became a free-text string checked by a regex that ends in `.*`. Anyone
who parsed `quantity value` structurally must change their code, and the new form cannot
enforce that the unit is meaningful.

A minority of former `quantity value` slots went to a real numeric type instead:
`rel_air_humidity`, `carb_nitro_ratio`, `surf_humidity`, `season_humidity`, `iwf`,
`animal_am_freq` (6 slots to `float`). `ferm_ch`-style percent slots and a few others moved
`string -> float`: `contam_score`, `ferm_headspace_oxy`, `ferm_chem_add_perc`.

### Other range changes worth listing individually

- **127 enum-range renames** (`window_cond_enum -> DamagedRupturedEnum` and similar). No
  semantic change; they follow the enum renames above.
- **21 slots gained an enumerated range where they previously accepted any string.** This is a
  genuine tightening: `aero_struc`, `assembly_qual`, `built_struc_set`, `ceil_struc`,
  `ceil_water_mold`, `contam_screen_input`, `door_water_mold`, `fireplace_type`,
  `heat_sys_deliv_meth`, `host_dependence`, `season`, `seq_quality_check`,
  `shad_dev_water_mold`, `shading_device_loc`, `space_typ_state`, `sym_life_cycle_type`,
  `urine_collect_meth`, `wall_water_mold`, `wga_amp_appr`, `window_status`,
  `window_water_mold`. Five of them (`ceil_water_mold`, `door_water_mold`,
  `shad_dev_water_mold`, `wall_water_mold`, `window_water_mold`) share one new
  `MoldVisibilityEnum`.
- **18 slots lost their enumerated range entirely** and now accept any string. This is a
  genuine loosening: `cur_land_use`, `decontam_software`, `door_type_wood`, `drug_usage`,
  `floor_finish_mat`, `host_sex`, `microb_start_count`, `organism_count`, `plant_growth_med`,
  `room_type`, `samp_floor`, `samp_md`, `source_uvig`, `special_diet`, `spikein_count`,
  `study_complt_stat`, `vis_media`, `water_source_shared`.
- **17 date slots became `datetime`**: `collection_date`, `cult_isol_date`, `pregnancy`,
  `menarche`, `menopause`, `hrt`, `douche`, `flooding`, `fire`, `extreme_event`,
  `last_clean`, `date_last_rain`, `date_extr_weath`, `fertilizer_date`, `cons_purch_date`,
  `prod_start_date`, `iw_bt_date_well`. Existing date-only values remain valid ISO 8601, so
  this widens what is accepted.
- **9 `double -> float`** (`soil_pH`, `water_pH`, `root_med_ph`, `ferm_pH`,
  `surf_moisture_ph`, `ph`, `avg_occup`, `typ_occup_density`, `occup_density_samp`) plus one
  `integer -> float` (`occup_samp`).
- **8 `integer -> string`** (a loosening on counts):
  `number_plants`, `max_occup`, `number_pets`, `room_occup`, `exp_pipe`, `freq_cook`,
  `host_occupation`, `number_resident`.
- **6 `string -> boolean`** (a tightening): `reassembly_bin`, `hysterectomy`, `smoker`,
  `twin_sibling`, `medic_hist_perform`, `x16s_recover`.
- **`timepoint`: `double -> string`**, and `samp_time_out`: `double -> (absent)`.
- **Ranges dropped without a replacement type**, so they fall back to the new
  `default_range: string`: `trnas` (was `integer`), `host_spec_range` (was `integer`),
  `host_of_host_taxid` (was `integer`), `ferm_chem_add` (was `quantity value`). `trnas` and
  `host_of_host_taxid` losing `integer` looks like an oversight worth checking.

### Multivalued

Of 644 flagged changes, 628 are `false -> (absent)` (no change). The 16 real ones:

- **Became multivalued (11)**: `source_mat_id`, `experimental_factor`, `host_spec_range`,
  `ventilation_type`, `biotic_regm`, `env_medium`, `food_dis_point_city`, `sop`,
  `solar_irradiance`, `associated_resource` (renamed), `host_fam_rel` (renamed).
  `env_medium` becoming multivalued is notable: it is a required core term that many archives
  treat as single-valued.
- **Stopped being multivalued (5)**: `farm_water_source`, `food_clean_proc`,
  `photosynt_activ`, `food_product_type`, `soil_temp`. These four-plus-one are a narrowing;
  any existing record with multiple values is no longer valid.

### Required

36 slots gained `required: true` on the global slot definition. **This is largely a relocation,
not 36 new obligations.** v6 never set `required` on a global slot (zero occurrences in the v6
`terms.yaml`); it set requiredness per class in `slot_usage`. For example `env_broad_scale` was
`required: true` in 11 v6 checklist classes and is now declared required once on the slot.

The slots: `abs_air_humidity`, `add_recov_method`, `api`, `basin`, `build_occup_type`,
`building_setting`, `coll_site_geo_feat`, `collection_date`, `env_broad_scale`,
`env_local_scale`, `env_medium`, `filter_type`, `geo_loc_name`, `hc_produced`, `hcr`,
`heat_cool_type`, `host_dependence`, `IFSAC_category`, `indoor_space`, `iwf`, `lat_lon`,
`light_type`, `occup_density_samp`, `occup_samp`, `project_name`, `rel_air_humidity`,
`samp_collect_point`,
`samp_name`, `samp_taxon_id`, `samp_type`, `seq_meth`, `space_typ_state`,
`sym_life_cycle_type`, `typ_occup_density`, `water_cut`, plus `sample_name -> samp_name`.

Where the diff reports a class-level requiredness change, it is confined to 23 classes and one
removal, concentrated in two extensions: `indoor_surf` and `surf_material` became required in
all 12 BuiltEnvironment classes, and `samp_vol_we_dna_ext` (11), `samp_size` (6),
`assembly_qual` (5), `lib_reads_seqd` (5), `lib_screen` (5), `lib_vector` (5),
`samp_mat_process` (5), `host_spec_range` (4), `specific_host` (2), `pathogenicity` (1) in
Agriculture classes. `isol_growth_condt` stopped being required in `MimarksSAgriculture`.
See the caveat in Notes before acting on these.

## Pattern changes

301 slots changed a `pattern`: 296 added, 4 removed, 1 modified. The additions are not
hand-written; they are materialized from 307 `structured_pattern` declarations that use the 33
new `settings` as interpolation variables. Only 27 distinct regexes cover all 296 slots:

| Slots | What it constrains |
|---|---|
| 178 | Number or numeric range, optional trailing unit (the `quantity value` replacement) |
| 32 | `PMID:`, `doi:`, or an http(s) URL (two near-identical variants; the citation/reference terms) |
| 19 | `term label [PREFIX:id]` (the ontology-term style used by `env_broad_scale` and similar) |
| 13 | Positive integer plus free text |
| 9 | ISO 8601 duration |
| 7 | `text;number unit` |
| 6 | Three semicolon-separated fields |
| 5 | Either an ontology term or a positive integer |
| 4 each | Free text or ontology term; `text;positive integer` |
| 3 | Numeric range plus unit |
| the rest | One-off shapes such as `95% ANI; 85% AF; ...` for `otu_class_appr` |

**Four slots lost their pattern**, which is a loosening on already-structured fields:
`food_quality_date` (was `^(best by|best if used by|freeze by||use by);YYYY-MM-DD$`),
`contam_screen_param` (was `^(ref db|kmer|coverage|combination);.+`),
`compl_score` (was `^(high|med|low);(0|[0-9]{1,2}|100)%$`),
`pres_animal_insect` (was `^(cat|dog|rodent|snake|other);\d+$`).
All four also lost their enum in the same release, so these terms went from doubly constrained
to free text in one step. That may be intentional, but it is the sharpest validation
regression in the diff and is easy to miss among 296 additions.

**One pattern modified**: `add_recov_method`. The old regex embedded a sprawling inline ISO
8601 datetime; the new one is a readable equivalent. The accepted-value list is unchanged, but
the two regexes are not exactly equivalent at the edges (the old one accepted week dates like
`W05` and ordinal dates; the new one does not).

## Title changes

ENA uses the MIxS `title` as its controlled nomenclature, so these are identifier changes for
downstream consumers even where the edit looks like tidying. Eleven titles changed:

**Meaning changed:**

| Slot | Old title | New title |
|---|---|---|
| `nose_throat_disord` | lung/nose-throat disorder | nose throat disorder |
| `horizon_meth` | soil horizon method | horizon method |
| `sieving` | composite design/sieving | sieving |
| `horizon -> soil_horizon` | horizon | soil horizon |
| `texture -> soil_texture` | texture | soil texture |
| `air particulate matter concentration -> air_PM_concen` | air_PM_concen | air particulate matter concentration |

Note that `horizon_meth` moves the other way from `horizon -> soil_horizon`: the slot renamed
toward `soil_`, its method partner renamed away from it. Worth checking that this is deliberate.

**Case, spacing or spelling only** (still visible to ENA users):

| Slot | Old title | New title |
|---|---|---|
| `food_trav_vehic` | Food shipping transportation vehicle | food shipping transportation vehicle |
| `samp_taxon_id` | Taxonomy ID of DNA sample | taxonomy ID of DNA sample |
| `Food_Product_type -> food_product_type` | Foodon product type | food product type |
| `Food_source -> food_source` | Food source | food source |
| `samp_transport_cont` | sample transport  container (double space) | sample transport container |
| `host_of_host_env_med` | host of the symbiotic host environemental medium | host of the symbiotic host environmental medium |

## Cosmetic changes (grouped)

293 slot descriptions changed. Only 60 carry any information:

- **233: trailing period removed.** A single mass edit stripping the final `.` from
  descriptions. Example: `heavy_metals`, `... add multiple copies of this field.` to
  `... add multiple copies of this field`.
- **3: whitespace or case only.** `wind_speed` ("Speed" to "speed"), `ph_meth` ("ph" to "pH"),
  `ph` (whitespace).
- **13 of the 57 remaining changes are mojibake repair**, not editorial: v6 had UTF-8 read as
  Latin-1 (`¬∞` for `°`, `¬†` for a non-breaking space) in `api`, `aromatics_pc`,
  `asphaltenes_pc`, `pour_point`, `resins_pc`, `root_med_macronutr`, `root_med_micronutr`,
  `root_med_regl`, `root_med_suppl`, `samp_transport_cond`, `saturates_pc`, `tan`,
  `viscosity`. All 13 are clean in v7. The repair replaced the corrupted degree signs with
  spaces rather than `°`, so `api` now reads `e.g. 31.1   API`.
- **44 substantive rewrites.** Two drivers dominate. First, **de-soiling**: definitions written
  for the soil package were generalized, e.g. `tot_org_carb` from "Definition for soil: total
  organic carbon content of the soil, definition otherwise: total organic carbon content" to
  "Total organic carbon content"; `store_cond` from "how and for how long the soil sample was
  stored" to "how and for how long the sample was stored", with added guidance. Second,
  **typo and reference fixes**: `hall_count` (cooridors to corridors), `samp_transport_cont`
  (Conatiner to Container), `plant_growth_med` (EO to PECO), `otu_class_appr` (OTUS to OTUs),
  `lat_lon` (added "limited to 8 decimal points"). One rewrite reverses a stated meaning:
  `size_frac_up` went from "Materials smaller than the size threshold are excluded" to
  "Materials larger than the size threshold are excluded" — worth confirming which is correct.

281 class descriptions also changed, but 253 of them are one template swap for the combination
classes: "Combinatorial checklist <long checklist name> with environmental package <package>"
became "MIxS Data that comply with the <Checklist> checklist and the <Extension> Extension".
Buried among them are four real corrections that the template swap hides:

- `MIGS org`: "Minimal Information about a Genome Sequence: org" to "... organelle"
- `MIGS plant`: "... plant" to "... plasmid"
- `MIGS virus`: was "... cultured bacteria/archaea" (a copy-paste error in v6), now "... virus"
- `MIMARKS specimen` and `MIMARKS survey`: "Minimal Information about a Marker **Specimen**"
  to "... Marker **Sequence**"

## Notes

**The `MIXS:` prefix now expands to a different IRI.** v6 had
`MIXS: https://w3id.org/mixs/terms/` with `default_prefix: mixs.vocab`; v7 has
`MIXS: https://w3id.org/mixs/` with `default_prefix: MIXS`. Every `slot_uri` and `class_uri`
in the schema therefore resolves to a different absolute IRI than it did in v6
(`MIXS:0000018` was `https://w3id.org/mixs/terms/0000018`, now `https://w3id.org/mixs/0000018`).
The diff reports this as one line in `prefixes.definition_changes` and it is easy to overlook,
but it affects every RDF consumer. The schema `id` also changed from `http://w3id.org/mixs`
to `https://w3id.org/mixs` (scheme only). Confirm this is intended and that the old IRIs
still resolve.

**The class-level `cascaded` entries are not trustworthy as content changes.** The tool reports
`required added: assembly_qual` for `agriculture MIGS bacteria -> MigsBaAgriculture`, but in
v6 that class declared no slots at all: it got them via `is_a: agriculture` plus
`mixins: [MIGS bacteria]`, and `MIGS bacteria` already declared `assembly_qual` as required.
The `ancestors added: Extension` (276) and `ancestors added: Checklist` (264) counts confirm
the tool tracks `is_a` ancestry. I could not determine from the diff whether it resolves
`mixins`, and the evidence above suggests it does not, or does so inconsistently. That would
explain why the same slots appear as both added (`adapters` 25 times) and removed
(`adapters` 23 times) across classes. **Treat every `cascaded` entry, including the
class-level required and recommended lists above, as a pointer to check against the schema
rather than as a finding.** The one cascade I did verify independently is
`estimated_size` / `estimated_genome_size` (144 removals, 144 additions, same MIXS URI).

**`recommended` shifted almost everywhere.** `elev` (261 classes), `depth` (260), `alt` (256)
and `temp` (253) became recommended nearly across the board. Same caveat as above.

**No `rename_candidates` section.** This tool does not emit one, so the "Possible missed
renames" section is my own URI-identity analysis rather than the tool's. A `rename_candidates`
pass in `diff-releases` would have caught `estimated_size` and `soil_depth` automatically.

**Version label.** The new side is tagged `main`, not `v7.0.0`; the `version` scalar reads
`7.0.0` and the commit is `60b48ef`. The comparison was generated from
`assets/releases_for_diffing/main_60b48ef`, which is not among the two `main_*` snapshots
currently in that folder (`main_07b5360`, `main_1591e32`). URI checks in this summary were run
against the repository's working `src/mixs/schema/mixs.yaml` on branch `release-v7.0.0-local`,
not against `60b48ef` directly.

**Left unclassified.** Both `nose_throat_disord` and the new
`nose_mouth_teeth_throat_disord` exist in v7, and their content crossed over:
`nose_mouth_teeth_throat_disord` carries essentially v6's `nose_throat_disord` description
(the Human Disease Ontology guidance), while `nose_throat_disord`'s description was replaced
with the shorter "Report any history of nose, mouth, teeth and/or throat disorders". That
looks like a rename that left the old slot in place rather than a deliberate split, but
nothing in the mapping files records it and I could not tell from the diff alone.
