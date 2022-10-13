import csv
import pprint

import yaml

input_tsv_file = "../example_data/in/MimsSoil_data.tsv"
output_yaml_file = "../example_data/in/mims_soil_set_database.yaml"

lod = []
with open(input_tsv_file) as tsvfile:
    reader = csv.DictReader(tsvfile, dialect='excel-tab')
    for row in reader:
        print(row)
        lod.append(row)

with open(output_yaml_file, 'w') as outfile:
    yaml.dump(lod, outfile, default_flow_style=False)
