# MIxS v5 (2018, Excel) to v6.0.0 (2022, LinkML)

Summary of `schema_comparison_results.yaml` in this directory: the change from the
last Excel MIxS (v5, 600 terms) to the first LinkML MIxS (v6.0.0, 804 terms).
This diff compares term names and their definitions, so there are no cardinality,
range, or pattern sections.

**Counts:** 573 shared, 20 renamed, 4 removed, 3 deleted, 212 added, 65
definitions changed, 1 possible missed rename to review.

## Added (212)

Grouped by theme (full list in the YAML): a large food package (HACCP_term,
IFSAC_category, food_contact_surf, food_origin, and related), fermentation and
starter-culture fields (ferm_*, microb_start*), spike-in controls (spikein_*,
neg_cont_type, pos_cont_type), host-of-host and symbiosis fields (host_of_host_*,
type_of_symbiosis, mode_transmission), animal husbandry and agriculture
(animal_*, farm_*, fertilizer_*, plant_*), soil fields (soil_pH, soil_temp,
soil_horizon), sampling, storage and transport (samp_stor_*, samp_transport_*),
sequencing, library and culturing (library_prep_kit, sequencing_kit, cult_*),
host measurements and study design (study_*, blood_press_*), and a handful of
structural LinkML scaffolding slots (core field, has unit, has raw value).

## Renamed (20)

Abbreviations and prefix changes introduced at v6.0.0: `16s_recover` and
`16s_recover_software` gain an `x_` prefix (LinkML names cannot start with a
digit); `votu_*` became `otu_*`; `health_disease_stat` became `host_disease_stat`;
and many were shortened, for example `chem_treatment_method` to
`chem_treat_method`, `heat_system_deliv_meth` to `heat_sys_deliv_meth`,
`host_blood_press_diast`/`_syst` to `blood_press_diast`/`_syst`, `ihmc_ethnicity`
to `ethnicity`, `organism_count_qpcr_info` to `org_count_qpcr_info`,
`room_architec_element` to `room_architec_elem`, `room_moist_damage_hist` to
`room_moist_dam_hist`, `samp_collection_point` to `samp_collect_point`,
`shading_device_water_mold` to `shad_dev_water_mold`, `tot_nitro_content_meth` to
`tot_nitro_cont_meth`, `tvdss_of_hcr_pressure` to `tvdss_of_hcr_press`,
`water_content_soil_meth` to `water_cont_soil_meth`, and `water_production_rate`
to `water_prod_rate`.

## Possible missed renames (1, review)

`pres_animal` closely matches the added `pres_animal_insect`. A maintainer should
decide whether this is a rename (and add it to the rename map) or a narrowing to
a new term.

## Removed (4) and deleted (3)

Removed (no clear replacement in v6.0.0): `extreme_salinity`,
`nose_mouth_teeth_throat_disord`, `pres_animal` (see above), `resp_part_matter`.
Removed on purpose (structural): `env_package` (package membership is now handled
by the class hierarchy), `investigation_type` (now implicit in checklist
selection), `submitted_to_insdc` (INSDC submission status is no longer tracked).

## Definitions changed (65)

65 terms that kept their name have a different definition between v5 and v6.0.0.

## Notes

Every rename target was checked to exist in the `mixs6.0.0` tag, and every
removed term to be absent from it. The rename map started with 6 entries; a
fuzzy self-check surfaced 14 more abbreviation-renames that were being reported as
removals, which have been added. The one remaining candidate above is left for a
maintainer to judge. Because both versions are finished releases, this result
never changes.
