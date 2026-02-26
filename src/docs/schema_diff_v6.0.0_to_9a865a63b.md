# MIxS Schema Diff: v6.0.0 (74744ee) to Main Branch (9a865a63b)

This document compares two specific points in the MIxS schema history:

- **Before:** MIxS v6.0.0, commit `74744ee`, dated 2022-03-23
- **After:** Main branch, commit `9a865a63b`, dated 2025-07-02

The "after" commit represents the state of main in anticipation of MIxS v7.0.0. This analysis was originally compiled in [GitHub Issue #845](https://github.com/GenomicsStandardsConsortium/mixs/issues/845). The release workflow now generates structured diffs in `assets/diff_results/schema_comparison_results.yaml`.

## Maintenance Note

This document should be regenerated periodically. Consider creating a new diff and curated summary when:

- A **major release** (e.g., v7.0.0) is published
- A **minor release** introduces significant schema changes (new classes, slots, or structural reorganization)
- A **significant PR** is merged that substantially changes the schema

Patch releases that only fix typos, descriptions, or examples typically do not warrant a new curated summary, though the automated `schema_comparison_results.yaml` will still capture these changes.

When regenerating, update:
1. The filename to reflect the new comparison endpoints
2. The commit hashes and dates in the header
3. All sections with current analysis

## Release Timeline

| Version | Date | Tag |
|---------|------|-----|
| MIxS5 | Feb 27, 2022 | MIxS5 |
| v6.0.0 | Mar 24, 2022 | mixs6.0.0 |
| v6.1.0 | Jul 5, 2022 | mixs6.1.0 |
| v6.1.1 | Oct 9, 2023 | mixs6.1.1 |
| v6.2.0 | Oct 18, 2023 | v6.2.0 |

## Schema Structure Changes

### v6.0.0 Structure (Modular)

- **Schema root:** `model/schema/mixs.yaml`
- **Commit:** 74744ee (2022-03-23)
- **Organization:** Individual modules for each environment/checklist

**Schema files (28 total):**
- agriculture.yaml, air.yaml, built_environment.yaml, checklists.yaml, core.yaml
- food_animal_and_animal_feed.yaml, food_farm_environment.yaml, food_food_production_facility.yaml, food_human_foods.yaml
- host_associated.yaml, human_associated.yaml, human_gut.yaml, human_oral.yaml, human_skin.yaml, human_vaginal.yaml
- hydrocarbon_resources_cores.yaml, hydrocarbon_resources_fluids_swabs.yaml
- microbial_mat_biofilm.yaml, miscellaneous_natural_or_artificial_environment.yaml, mixs.yaml
- plant_associated.yaml, ranges.yaml, sediment.yaml, soil.yaml, symbiont_associated.yaml
- terms.yaml, wastewater_sludge.yaml, water.yaml

### Main Branch at 9a865a63b (Consolidated)

- **Schema root:** `src/mixs/schema/mixs.yaml`
- **Commit:** 9a865a63b (2025-07-02)
- **Organization:** Monolithic schema with deprecated.yaml

**Schema files (2 total):**
- mixs.yaml
- deprecated.yaml

## Root Scalar Differences

| Field | v6.0.0 (74744ee) | Main (9a865a63b) |
|-------|------------------|------------------|
| `default_prefix` | mixs.vocab | MIXS |
| `description` | Minimal Information about any Sequence Standard | Extended description with LinkML and GSC references |
| `id` | http://w3id.org/mixs | https://w3id.org/mixs |
| `name` | MIxS | mixs |

### Added in Main Branch (9a865a63b)

- `comments` - Notes about slot titles associated with multiple slot names
- `source` - Reference to mixs_v6.xls spreadsheet
- `version` - v6.2.0
- `default_range` - string
- `settings` - Structured pattern definitions (see below)

### Removed from Main Branch

- `types` (moved to LinkML defaults)
- `source_file`

## Settings (Structured Patterns)

Settings were added post-v6.0.0 to build `structured_pattern`s reminiscent of the "Value syntax" in the MIxS 6 spreadsheet.

```yaml
# Frequently used patterns
text: '.*'
float: '[-+]?[0-9]*\.?[0-9]+'
integer: '[1-9][0-9]*'
scientific_float: '[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?'
boolean: '(?:yes|no)'

# Date/time patterns
date_time_stamp: '(\d{4})(-(0[1-9]|1[0-2])(-(0[1-9]|[12]\d|3[01])(T([01]\d|2[0-3]):([0-5]\d):([0-5]\d)(\.\d+)?(Z|([+-][01]\d:[0-5]\d))?)?)?)?$'
duration: 'P(?:(?:\d+D|\d+M(?:\d+D)?|\d+Y(?:\d+M(?:\d+D)?)?)...)'

# Reference patterns
DOI: '^doi:10.\d{2,9}/.*$'
PMID: '^PMID:\d+$'
URL: '^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}...'
NCBItaxon_id: 'NCBITaxon:\d+'

# Sequence patterns
dna: '^[ACGT]+$'
ambiguous_nucleotides: '[ACGTRKSYMWBHDVN]+'

# Geographic patterns
lat: '(-?((?:[0-8]?[0-9](?:\.\d{0,8})?)|90))'
lon: '-?[0-9]+(?:\.[0-9]{0,8})?$|^-?(1[0-7]{1,2})'

# Term patterns
termID: '[a-zA-Z]{2,}:[a-zA-Z0-9]\d+'
termLabel: '([^\s-]{1,2}|[^\s-]+.+[^\s-]+)'
unit: '([^\s-]{1,2}|[^\s-]+.+[^\s-]+)'
```

### Settings Usage Analysis

**Low usage patterns (1 use each):**
- NCBItaxon_id, adapter_A_DNA_sequence, adapter_B_DNA_sequence
- add_recov_methods, agrochemical_name, amount, boolean
- lat, lon, particulate_matter_name

**Unused settings (6 total):**
- adapter, country, dna, region, specific_location, storage_condition_type

## Prefix Changes

| Change Type | Prefix | v6.0.0 | Main |
|-------------|--------|--------|------|
| Removed | mixs.vocab | https://w3id.org/mixs/vocab/ | - |
| Removed | MIGS | https://w3id.org/mixs/migs/ | - |
| Changed | MIXS | https://w3id.org/mixs/terms/ | https://w3id.org/mixs/ |
| Added | SO | - | http://purl.obolibrary.org/obo/SO_ |
| Unchanged | linkml, xsd, shex, schema | (same) | (same) |

## Subset Reorganization

The organizational approach changed completely:

### v6.0.0 Subsets (Structural - All Removed)

| Subset | Description |
|--------|-------------|
| checklist | A MIxS checklist. These can be combined with packages |
| package | A MIxS package. These can be combined with checklists |
| checklist_package_combination | A combination of a checklist and a package |

### Main Branch Subsets (Functional/Thematic - All New)

| Subset | Usage Count |
|--------|-------------|
| combination_classes | 253 |
| sequencing | 57 |
| nucleic acid sequence source | 25 |
| environment | 10 |
| investigation | 6 |

**Key observation:** The knowledge that a class is a Checklist or Extension is now communicated via `is_a` relationships, not `in_subset`.

## Class Changes

### Naming Transformation

| Aspect | v6.0.0 | Main |
|--------|--------|------|
| Total classes | 289 | 290 |
| Naming style | Space-delimited ("soil MIGS bacteria") | CamelCase ("MigsBaSoil") |
| Order | {environment} {checklist} | {checklist}{environment} |

### New Base Classes in Main

- `Checklist` - Abstract base for all checklists
- `Extension` - Abstract base for all extensions
- `MixsCompliantData` - Required for validating collections (CSV files, etc.)

### Removed Classes

- `core`
- `quantity value`

### Class Metadata Fields

| Field | v6.0.0 | Main |
|-------|--------|------|
| `name` | Yes | Yes |
| `description` | Yes | Yes |
| `from_schema` | Yes | Yes |
| `aliases` | Yes | Yes |
| `mixin` | Yes | Yes |
| `slot_usage` | Yes | Yes |
| `title` | No | **Added** |
| `is_a` | No | **Added** |
| `class_uri` | No | **Added** |
| `tree_root` | No | **Added** (to MixsCompliantData) |

### Inheritance Changes

- **v6.0.0:** Flat structure, no inheritance
- **Main:** Hierarchical structure with `is_a` relationships

## Slot Renamings/Normalizations

| Old Name (v6.0.0) | New Name (Main) |
|-------------------|-----------------|
| `air particulate matter concentration` | `air_PM_concen` |
| `assembly_quality` | `assembly_qual` |
| `associated resource` | `associated_resource` |
| `Food_Product_type` | `food_product_type` |
| `Food_source` | `food_source` |
| `host_family_relation` | `host_fam_rel` |
| `host_family_relationship` | `host_fam_rel` |
| `horizon` | `soil_horizon` |
| `host_infra_specific_name` | `host_infra_spec_name` |
| `host_infra_specific_rank` | `host_infra_spec_rank` |
| `microbial_biomass_meth` | `micro_biomass_meth` |
| `non_mineral_nutr_regm` | `non_min_nutr_regm` |
| `previous_land_use_meth` | `prev_land_use_meth` |
| `samp_collec_device` | `samp_collect_device` |
| `samp_collec_method` | `samp_collect_method` |
| `samp_salinity` | `salinity` |
| `samp_stor_dur` | `samp_store_dur` |
| `samp_stor_loc` | `samp_store_loc` |
| `samp_stor_temp` | `samp_store_temp` |
| `sample_name` | `samp_name` |
| `single_cell_lysis_appr` | `sc_lysis_approach` |
| `single_cell_lysis_prot` | `sc_lysis_method` |
| `soil_text_measure` | `soil_texture_meth` |
| `texture_meth` | `soil_texture_meth` |
| `texture` | `soil_texture` |
| `tot_car` | `tot_carb` |
| `tot_n_meth` | `tot_nitro_cont_meth` |
| `tot_nitro` | `tot_nitro_content` |
| `tot_phos` | `tot_phosphate` |
| `x_16s_recover_software` | `x16s_recover_software` |
| `x_16s_recover` | `x16s_recover` |

### New Slot

- `urobiom_sex` - New content field

### Removed Slots

- `salinity_meth`
- `url` (replaced by `associated_resource`)

### Removed Organizational Fields (Refactored as Subsets)

- `core field`
- `environment field`
- `investigation field`
- `mixs extension field`
- `nucleic acid sequence source field`

## Slot-to-Class Assignment Changes

### General Patterns

1. **Core checklists** (MIGS, MIMS, MIMARKS, etc.) all gained: `alt`, `depth`, `elev`, `temp`
2. **Environmental extensions** generally lost core metadata fields (`collection_date`, `env_broad_scale`, `env_local_scale`, `env_medium`, `geo_loc_name`, `lat_lon`) while gaining project-specific fields (`project_name`, `samp_name`, `samp_vol_we_dna_ext`)
3. **Single-cell specific changes** in MISAG/MIUVIG where slot names were updated

### Checklist Changes

| Class | Added Slots | Removed Slots |
|-------|-------------|---------------|
| MigsEu | alt, depth, elev, temp | - |
| MigsBa | alt, depth, elev, temp | - |
| MigsPl | alt, depth, elev, temp | - |
| MigsVi | alt, depth, elev, temp | - |
| MigsOrg | alt, depth, elev, temp | - |
| Mims | alt, depth, elev, temp | - |
| MimarksS | alt, depth, elev, temp | - |
| MimarksC | alt, depth, elev, temp | - |
| Misag | alt, depth, elev, sc_lysis_approach, sc_lysis_method, temp, x16s_recover, x16s_recover_software | single_cell_lysis_appr, single_cell_lysis_prot, x_16s_recover, x_16s_recover_software |
| Mimag | alt, depth, elev, temp, x16s_recover, x16s_recover_software | x_16s_recover, x_16s_recover_software |
| Miuvig | alt, depth, elev, sc_lysis_approach, sc_lysis_method, temp | single_cell_lysis_appr, single_cell_lysis_prot |

### Extension Changes

| Class | Added Slots | Removed Slots |
|-------|-------------|---------------|
| Air | air_PM_concen, project_name, samp_name, samp_vol_we_dna_ext | air_particulate_matter_concentration, collection_date, depth, env_broad_scale, env_local_scale, env_medium, geo_loc_name, lat_lon |
| BuiltEnvironment | project_name, samp_name | alt, collection_date, depth, elev, env_broad_scale, env_local_scale, env_medium, geo_loc_name, lat_lon, temp |
| HostAssociated | host_disease_stat, host_fam_rel, project_name, samp_name, samp_vol_we_dna_ext | collection_date, env_broad_scale, env_local_scale, env_medium, geo_loc_name, host_family_relation, lat_lon |
| Soil | project_name, samp_name, samp_vol_we_dna_ext, soil_texture | alt, collection_date, env_broad_scale, env_local_scale, env_medium, geo_loc_name, lat_lon, salinity_meth, soil_text_measure |
| Water | project_name, samp_name, samp_vol_we_dna_ext | alt, collection_date, env_broad_scale, env_local_scale, env_medium, geo_loc_name, lat_lon |

*(See [Issue #845](https://github.com/GenomicsStandardsConsortium/mixs/issues/845) for complete extension changes)*

## Extension Use Cases

The main branch adds use case annotations on Extension classes:

| Extension | Example Use Cases |
|-----------|-------------------|
| Agriculture | Agricultural Microbiomes Research Coordination Network; microbiome studies in agricultural sites; eDNA in manure samples |
| Air | bioaerosol samples; pathogen load in urban air; aerosols |
| BuiltEnvironment | NASA space station sampling; MetaSUB transit system sampling; hospitals; office buildings |
| FoodHumanFoods | Microbiome of foods intended for human consumption |
| HostAssociated | elephant fecal matter; cat oral cavity |
| HumanGut | human stool or fecal samples; samples collected directly from the gut |
| PlantAssociated | plant surface swabs; root soil or rhizosphere; plant phenotyping |
| Soil | soil collection; island microbiome sampling; farm land or forest floor |
| Water | sea or river water; global ocean sampling day |

## Generating Structured Diffs

### Automatic Generation (Release Workflow)

The structured diff (`assets/diff_results/schema_comparison_results.yaml`) is **automatically generated** when running the release workflow at `.github/workflows/create-release-pr.yaml`.

**The before/after versions are specified via workflow input parameters:**

| Parameter | Description | Format | Example |
|-----------|-------------|--------|---------|
| `version` | The new version number being released | `X.Y.Z` (no `v` prefix) | `6.2.3` |
| `diff_old` | The "before" version - a git tag or branch name | Exact git tag or branch | `v6.2.2`, `mixs6.0.0` |
| `diff_new` | The "after" version - a git tag or branch name | Exact git tag or branch | `main` |

The workflow automatically constructs the full schema path as:
`GenomicsStandardsConsortium/mixs@{diff_old}:src/mixs/schema/mixs.yaml`

**To trigger via GitHub Actions UI:**
1. Go to Actions > "Create Release PR"
2. Click "Run workflow"
3. Fill in the three parameters above

### Why the Formats Differ

The `version` and `diff_old`/`diff_new` parameters use different formats for different reasons:

- **`version`** is used to update version strings in files like `pyproject.toml`, `CITATION.cff`, and `.zenodo.json`. These files conventionally use bare version numbers without a `v` prefix (e.g., `version = "6.2.3"`).

- **`diff_old`/`diff_new`** must match actual git references (tags or branches) exactly. Git tags in this repo use different naming conventions depending on when they were created:
  - Pre-v6.2.0 tags: `mixs6.0.0`, `mixs6.1.0`, `mixs6.1.1`
  - Post-v6.2.0 tags: `v6.2.0`, `v6.2.1`, `v6.2.2`, `v6.2.3`

### Common Pitfall

In PR #1102, `diff_old` was set to `6.2.2` instead of `v6.2.2`. Because `6.2.2` is not a valid git reference, the diff tool fell back to cached data from an older version, producing an incorrect diff.

**Always verify:**
1. `version` = bare number, no `v` prefix (e.g., `6.2.3`)
2. `diff_old` = exact git tag with correct prefix (e.g., `v6.2.2` not `6.2.2`)
3. Check that the tag exists: `git tag -l "v6.2.2"`

See [issue #1104](https://github.com/GenomicsStandardsConsortium/mixs/issues/1104) for proposed workflow improvements to validate tags before running.

### Manual Generation (CLI)

To regenerate the structured diff locally:

```shell
poetry run diff-releases \
    --old "GenomicsStandardsConsortium/mixs@v6.0.0:src/mixs/schema/mixs.yaml" \
    --new "GenomicsStandardsConsortium/mixs@main:src/mixs/schema/mixs.yaml" \
    --output-dir assets/diff_results \
    --mappings-dir assets/between_diff_mappings/6_to_pre_7
```

**Parameters:**
- `--old`: Reference to old schema (`{repo}@{tag/branch}:{path}`)
- `--new`: Reference to new schema
- `--output-dir`: Where to write `schema_comparison_results.yaml` and `releases.yaml`
- `--mappings-dir`: Directory containing slot/class/enum name mapping TSVs for renamed elements

### Helper Commands for Manual Analysis

**Merge modular v6.0.0 schema files:**
```shell
poetry run linkml generate linkml \
    --format yaml \
    --no-materialize model/schema/mixs.yaml > mixs_6_0_0_merged.yaml
```

**Extract element lists for comparison:**
```shell
yq 'keys' mixs_6_0_0_merged.yaml > mixs_6_0_0_root_keys.txt
yq '.classes | keys' mixs_6_0_0_merged.yaml > mixs_6_0_0_classes.txt
yq '.slots | keys' mixs_6_0_0_merged.yaml > mixs_6_0_0_slots.txt
```

**Materialize patterns for validation:**
```shell
poetry run linkml generate linkml \
    --format yaml \
    --no-materialize-attributes \
    --materialize-patterns src/mixs/schema/mixs.yaml > mixs_main_materialized.yaml
```

**Validate data against schema:**
```shell
poetry run linkml-validate \
    --schema mixs_main_materialized.yaml \
    --target-class MixsCompliantData your_data.yaml
```

## Related Resources

- **Structured diff:** `assets/diff_results/schema_comparison_results.yaml`
- **Release registry:** `assets/diff_results/releases.yaml`
- **Mapping files:** `assets/between_diff_mappings/6_to_pre_7/`
- **GitHub Issue:** [#845](https://github.com/GenomicsStandardsConsortium/mixs/issues/845)

## Related Issues

- [#356](https://github.com/GenomicsStandardsConsortium/mixs/issues/356) - Set up autogenerated release notes
- [#537](https://github.com/GenomicsStandardsConsortium/mixs/issues/537) - Change log to be included with new releases
- [#835](https://github.com/GenomicsStandardsConsortium/mixs/issues/835) - Table of release dates
- [#882](https://github.com/GenomicsStandardsConsortium/mixs/issues/882) - Version update tracking for consumers
- [#1085](https://github.com/GenomicsStandardsConsortium/mixs/issues/1085) - LLM-generated narrative summaries
