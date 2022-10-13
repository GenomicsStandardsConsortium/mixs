from linkml_runtime.dumpers import yaml_dumper

import mixs_schemasheets_generated

d = mixs_schemasheets_generated.Database()

ms1 = mixs_schemasheets_generated.MimsSoil(
    collection_date="2021-01-01",
    env_broad_scale="ENVO:00000000",
    env_local_scale="ENVO:00000000",
    env_medium="ENVO:00000000",
    geo_loc_name="ENVO:00000000",
    lat_lon="ENVO:00000000",
    samp_taxon_id="ENVO:00000000",
    seq_meth="ENVO:00000000",
)

d.mims_soil_set.append(ms1)

ms2 = mixs_schemasheets_generated.MimsSoil(
    collection_date="2021-01-01",
    env_broad_scale="ENVO:00000000",
    env_local_scale="ENVO:00000000",
    env_medium="ENVO:00000000",
    geo_loc_name="ENVO:00000000",
    lat_lon="ENVO:00000000",
    samp_taxon_id="ENVO:00000000",
    seq_meth="ENVO:00000000",
)

d.mims_soil_set.append(ms2)

print(yaml_dumper.dumps(d))
