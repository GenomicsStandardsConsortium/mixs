# start by extracting something that will fit in Clause's 200k token context window
#  or smaller for other LLMSs!

import csv
import os
import pprint
from collections import defaultdict

import yaml

schema_file = '../mixs/schema/mixs.yaml'
slots_output_yaml = '../../assets/mixs_slots_report.yaml'
# claude wants csv?
slots_output_csv = '../../assets/mixs_slots_report.csv'


def load_yaml_file(filepath):
    with open(filepath, 'r') as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(f'Error parsing YAML file: {exc}')
            return None


if os.path.exists(schema_file):
    schema_dict = load_yaml_file(schema_file)
    if schema_dict is None:
        print(f'Failed to load {schema_file}')
        exit()
    else:
        print(f'Successfully loaded {schema_file}')
else:
    print(f'File not found: {schema_file}')
    exit()

slots_dict = schema_dict['slots']

all_keys = {k for dct in slots_dict.values() for k in dct}

# pprint.pprint(all_keys)

# {'annotations',
#  'comments',
#  'description',
#  'domain',
#  'examples',
#  'in_subset',
#  'inlined',
#  'inlined_as_list',
#  'keywords',
#  'multivalued',
#  'pattern',
#  'range',
#  'recommended',
#  'required',
#  'slot_uri',
#  'string_serialization',
#  'structured_pattern',
#  'title'}

# unsure: annotations, in_subset, examples
# to mine: comments, description, title
#   add the key as 'name'
# ignore: domain, inlined, inlined_as_list, multivalued, recommended, required, slot_uri
# to normalize: range, keywords, structured_pattern, pattern
# to redirect: string_serialization

# the comments aren't really mine-able. they are more like notes to self

# note: we are not examining the classes' slot_usages

anno_counts = defaultdict(int)  # int values default to 0
for d in slots_dict.values():
    if "annotations" in d:
        for key in d["annotations"]:
            anno_counts[key] += 1

print("Annotation counts:")
print(dict(anno_counts))


# {'Expected_value': 227, 'Preferred_unit': 238}


def flatten(v):
    if isinstance(v, dict):
        return str(v)
    elif isinstance(v, list):
        return ' '.join(str(x) for x in v)
    else:
        return str(v)


cleaned = []
for slot_id, slots in slots_dict.items():

    if "domain" in slots and slots["domain"] == "MixsCompliantData":
        continue

    cleaned_dict = {'name': slot_id}

    if "annotations" in slots and "Expected_value" in slots["annotations"]:
        cleaned_dict["expected_value"] = slots["annotations"]["Expected_value"]

    for key in ('description', 'title'):
        if key in slots:
            cleaned_dict[key] = flatten(slots[key])

    cleaned.append(cleaned_dict)

with open(slots_output_csv, 'w') as f:
    # , delimiter='\t'
    writer = csv.DictWriter(f, fieldnames=['name', 'description', 'title', 'expected_value'])
    writer.writeheader()
    for d in cleaned:
        writer.writerow(d)

with open(slots_output_yaml, 'w') as file:
    yaml.dump(slots_dict, file, sort_keys=False)
