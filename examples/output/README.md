## MixsCompliantData-MimsSoil-pattern-fixes
### Input
```yaml
mims_soil_data:
- al_sat_meth: PMID:12345678
  collection_date: '2024-05-20T09:15:00-05:00'
  depth: 0.5 m
  elev: 200 m
  env_broad_scale: agricultural ecosystem [ENVO:01001245]
  env_local_scale: agricultural soil [ENVO:00002259]
  env_medium: soil [ENVO:00001998]
  geo_loc_name: 'USA: Iowa, Ames'
  lat_lon: 41.9 -93.6
  previous_land_use: corn cultivation;2020-09-15T10:00:00Z
  project_name: Soil pattern validation test
  samp_name: soil-pattern-test-1
  samp_taxon_id: soil metagenome [NCBITaxon:410658]
  seq_meth: PMID:98765432
- al_sat_meth: doi:10.1016/j.soilbio.2020.107890
  collection_date: '2024-04-10T00:00:00Z'
  depth: 1.0 m
  elev: 150 m
  env_broad_scale: grassland ecosystem [ENVO:01001206]
  env_local_scale: grassland soil [ENVO:00005750]
  env_medium: soil [ENVO:00001998]
  geo_loc_name: 'USA: Kansas, Topeka'
  lat_lon: 38.5 -98.8
  previous_land_use: wheat farming;2019-06-20
  project_name: Soil timestamp test
  samp_name: soil-pattern-test-2
  samp_taxon_id: soil metagenome [NCBITaxon:410658]
  seq_meth: doi:10.1126/science.abc1234
- al_sat_meth: https://www.sciencedirect.com/science/article/pii/S0038071720301234
  collection_date: '2024-03-01T08:00:00+01:00'
  depth: 0.3 m
  elev: 180 m
  env_broad_scale: forest ecosystem [ENVO:01001179]
  env_local_scale: forest soil [ENVO:00002261]
  env_medium: soil [ENVO:00001998]
  geo_loc_name: 'Germany: Bavaria, Munich'
  lat_lon: 48.1 11.6
  previous_land_use: fallow;2018-05-11T14:30Z
  project_name: Soil minimal timestamp test
  samp_name: soil-pattern-test-3
  samp_taxon_id: soil metagenome [NCBITaxon:410658]
  seq_meth: https://www.ebi.ac.uk/ena/browser/view/PRJEB12345

```
## MixsCompliantData-MimsSoil-example
### Input
```yaml
mims_soil_data:
- agrochem_addition:
  - roundup;5 milligram per liter;2018-06-21
  collection_date: '2013-03-25T12:42:31+01:00'
  depth: 1.234 units
  elev: 1.234 units
  env_broad_scale: term [ONTOLOGY:123]
  env_local_scale: term [ONTOLOGY:123]
  env_medium: term [ONTOLOGY:123]
  geo_loc_name: 'text: text, text'
  lat_lon: 45.1 45.9
  project_name: absolutely any text
  samp_name: msd1
  samp_taxon_id: Gut Metagenome [NCBITaxon:749906]
  seq_meth: absolutely any text
- collection_date: '2013-03-25T12:42:31+01:00'
  depth: 1.234 units
  elev: 1.234 units
  env_broad_scale: term [ONTOLOGY:123]
  env_local_scale: term [ONTOLOGY:123]
  env_medium: term [ONTOLOGY:123]
  geo_loc_name: 'text: text, text'
  lat_lon: 45.1 45.9
  project_name: absolutely any text
  samp_name: msd2
  samp_taxon_id: Gut Metagenome [NCBITaxon:749906]
  seq_meth: absolutely any text

```
## MixsCompliantData-MIMS-HCRFS-example
### Input
```yaml
mims_hydrocarbon_resources_fluids_swabs_data:
- add_recov_method: Dump Flood;2011-11-11T11:11:11.11Z
  api: 1.234 - 9.999 units
  basin: term [ONTOLOGY:123]
  collection_date: '2013-03-25T12:42:31+01:00'
  depth: 1.234 units
  elev: 1.234 units
  env_broad_scale: term [ONTOLOGY:123]
  env_local_scale: term [ONTOLOGY:123]
  env_medium: term [ONTOLOGY:123]
  geo_loc_name: 'text: text, text'
  hc_produced: Bitumen
  hcr: Coalbed
  iwf: 1.234
  lat_lon: 45.1 45.9
  nitrate: 1.234 units
  project_name: absolutely any text
  samp_collect_point: other
  samp_name: msd1
  samp_taxon_id: Gut Metagenome [NCBITaxon:749906]
  samp_type: term [ONTOLOGY:123]
  seq_meth: absolutely any text
  sulfate: 1.234 units
  sulfide: 1.234 units
  temp: 1.234 units
  water_cut: 1.234 units

```
## MixsCompliantData-MIMS-HCRFS-pattern-fixes
### Input
```yaml
mims_hydrocarbon_resources_fluids_swabs_data:
- add_recov_method: Water Injection;2020-01-15T08:00:00Z
  api: 35 degree API
  basin: Permian Basin [ENVO:00000215]
  collection_date: '2024-06-15T10:30:00Z'
  depth: 100 m
  elev: 50 m
  env_broad_scale: petroleum reservoir [ENVO:00000453]
  env_local_scale: oil reservoir [ENVO:00000453]
  env_medium: petroleum [ENVO:00002984]
  geo_loc_name: 'USA: Texas, Permian Basin'
  hc_produced: Oil
  hcr: Oil Sand
  iwf: 0.85
  lat_lon: 31.8 -102.3
  nitrate: 10 milligram per liter
  project_name: Structured pattern validation test
  samp_collect_point: well
  samp_name: pattern-test-1
  samp_taxon_id: Bacteria [NCBITaxon:2]
  samp_type: oil [ENVO:00002984]
  seq_meth: PMID:12345678
  sulfate: 250 milligram per liter
  sulfide: 5 milligram per liter
  temp: 85 degree Celsius
  water_cut: 15 percent
- add_recov_method: Gas Injection;2019-06-01T12:00:00Z
  api: 10 degree API
  basin: Athabasca [ENVO:00000215]
  collection_date: '2024-07-20T14:45:30-06:00'
  depth: 150 m
  elev: 75 m
  env_broad_scale: petroleum reservoir [ENVO:00000453]
  env_local_scale: oil reservoir [ENVO:00000453]
  env_medium: petroleum [ENVO:00002984]
  geo_loc_name: 'Canada: Alberta, Athabasca'
  hc_produced: Bitumen
  hcr: Oil Sand
  iwf: 0.75
  lat_lon: 56.7 -111.4
  nitrate: 15 milligram per liter
  project_name: DOI pattern test
  samp_collect_point: well
  samp_name: pattern-test-2
  samp_taxon_id: Archaea [NCBITaxon:2157]
  samp_type: bitumen [ENVO:00002984]
  seq_meth: doi:10.1038/s41586-020-2649-2
  sulfate: 300 milligram per liter
  sulfide: 8 milligram per liter
  temp: 90 degree Celsius
  water_cut: 20 percent
- add_recov_method: Polymer Addition;2021-03-15
  api: 40 degree API
  basin: North Sea Basin [ENVO:00000215]
  collection_date: '2024-08-10T00:00:00Z'
  depth: 200 m
  elev: 100 m
  env_broad_scale: petroleum reservoir [ENVO:00000453]
  env_local_scale: oil reservoir [ENVO:00000453]
  env_medium: petroleum [ENVO:00002984]
  geo_loc_name: 'Norway: North Sea, Troll Field'
  hc_produced: Oil
  hcr: Oil Reservoir
  iwf: 0.65
  lat_lon: 60.5 2.5
  nitrate: 8 milligram per liter
  project_name: URL pattern test
  samp_collect_point: well
  samp_name: pattern-test-3
  samp_taxon_id: Bacteria [NCBITaxon:2]
  samp_type: oil [ENVO:00002984]
  seq_meth: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC123456/
  sulfate: 200 milligram per liter
  sulfide: 3 milligram per liter
  temp: 95 degree Celsius
  water_cut: 25 percent

```
## MixsCompliantData-MimsSoil-invalid-al_sat_meth-pmid-trailing
### Input
```yaml
mims_soil_data:
- al_sat_meth: PMID:12345678 - see methods section
  collection_date: '2024-05-20T09:15:00-05:00'
  depth: 0.5 m
  elev: 200 m
  env_broad_scale: agricultural ecosystem [ENVO:01001245]
  env_local_scale: agricultural soil [ENVO:00002259]
  env_medium: soil [ENVO:00001998]
  geo_loc_name: 'USA: Iowa, Ames'
  lat_lon: 41.9 -93.6
  project_name: PMID at start with trailing text
  samp_name: soil-invalid-pmid-trailing
  samp_taxon_id: soil metagenome [NCBITaxon:410658]
  seq_meth: PMID:98765432

```
## MixsCompliantData-MimsSoil-example-undefined-slot
### Input
```yaml
undefined_slot:
- collection_date: '2013-03-25T12:42:31+01:00'
  depth: 1.234 units
  elev: 1.234 units
  env_broad_scale: term [ONTOLOGY:123]
  env_local_scale: term [ONTOLOGY:123]
  env_medium: term [ONTOLOGY:123]
  geo_loc_name: 'text: text, text'
  lat_lon: 45.1 45.9
  project_name: absolutely any text
  samp_name: msd1
  samp_taxon_id: Gut Metagenome [NCBITaxon:749906]
  seq_meth: absolutely any text
- collection_date: '2013-03-25T12:42:31+01:00'
  depth: 1.234 units
  elev: 1.234 units
  env_broad_scale: term [ONTOLOGY:123]
  env_local_scale: term [ONTOLOGY:123]
  env_medium: term [ONTOLOGY:123]
  geo_loc_name: 'text: text, text'
  lat_lon: 45.1 45.9
  project_name: absolutely any text
  samp_name: msd2
  samp_taxon_id: Gut Metagenome [NCBITaxon:749906]
  seq_meth: absolutely any text

```
## MixsCompliantData-MimsSoil-invalid-al_sat_meth-url-leading
### Input
```yaml
mims_soil_data:
- al_sat_meth: 'see link: https://example.com/method'
  collection_date: '2024-03-01T08:00:00+01:00'
  depth: 0.3 m
  elev: 180 m
  env_broad_scale: forest ecosystem [ENVO:01001179]
  env_local_scale: forest soil [ENVO:00002261]
  env_medium: soil [ENVO:00001998]
  geo_loc_name: 'Germany: Bavaria, Munich'
  lat_lon: 48.1 11.6
  project_name: URL at end with leading text
  samp_name: soil-invalid-url-leading
  samp_taxon_id: soil metagenome [NCBITaxon:410658]
  seq_meth: https://www.ebi.ac.uk/ena/browser/view/PRJEB12345

```
## MixsCompliantData-MimsSoil-invalid-al_sat_meth-doi-leading
### Input
```yaml
mims_soil_data:
- al_sat_meth: method from doi:10.1016/j.soilbio.2020.107890
  collection_date: '2024-04-10T00:00:00Z'
  depth: 1.0 m
  elev: 150 m
  env_broad_scale: grassland ecosystem [ENVO:01001206]
  env_local_scale: grassland soil [ENVO:00005750]
  env_medium: soil [ENVO:00001998]
  geo_loc_name: 'USA: Kansas, Topeka'
  lat_lon: 38.5 -98.8
  project_name: DOI with leading text
  samp_name: soil-invalid-doi-leading
  samp_taxon_id: soil metagenome [NCBITaxon:410658]
  seq_meth: doi:10.1126/science.abc1234

```
