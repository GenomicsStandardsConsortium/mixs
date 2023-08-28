## MixsCompliantData-MimsSoil-example
### Input
```yaml
mims_soil_data:
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
## MixsCompliantData-MimsSoil-extra-slot
### Input
```yaml
mims_soil_data:
- collection_date: '2013-03-25T12:42:31+01:00'
  depth: 1.234 units
  elev: 1.234 units
  env_broad_scale: term [ONTOLOGY:123]
  env_local_scale: term [ONTOLOGY:123]
  env_medium: term [ONTOLOGY:123]
  flavor: grape
  geo_loc_name: absolutely any text
  lat_lon: absolutely any text
  project_name: absolutely any text
  samp_name: msd1
  samp_taxon_id: absolutely any text
  seq_meth: absolutely any text

```
## MixsCompliantData-MimsSoil-bad-geo_loc_name
### Input
```yaml
mims_soil_data:
- collection_date: '2013-03-25T12:42:31+01:00'
  depth: 1.234 units
  elev: 1.234 units
  env_broad_scale: term [ONTOLOGY:123]
  env_local_scale: term [ONTOLOGY:123]
  env_medium: term [ONTOLOGY:123]
  geo_loc_name: absolutely any text
  lat_lon: 45.1 45.9
  project_name: absolutely any text
  samp_name: msd1
  samp_taxon_id: absolutely any text
  seq_meth: absolutely any text

```
## MixsCompliantData-MimsSoil-missing-samp_name
### Input
```yaml
mims_soil_data:
- collection_date: '2013-03-25T12:42:31+01:00'
  depth: 1.234 units
  elev: 1.234 units
  env_broad_scale: term [ONTOLOGY:123]
  env_local_scale: term [ONTOLOGY:123]
  env_medium: term [ONTOLOGY:123]
  geo_loc_name: absolutely any text
  lat_lon: absolutely any text
  project_name: absolutely any text
  samp_taxon_id: absolutely any text
  seq_meth: absolutely any text

```
