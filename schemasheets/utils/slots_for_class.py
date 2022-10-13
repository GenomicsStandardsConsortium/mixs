import pprint

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

schema_file = "../generated/mixs_schemasheets_generated.yaml"

current_class = "MimsSoil"

view = SchemaView(schema_file)

cis = view.class_induced_slots(current_class)

requireds = []
optionals = []
multivalueds = []
for ci in cis:
    if ci.required:
        requireds.append(ci.name)
    else:
        optionals.append(ci.name)
    if ci.multivalued:
        multivalueds.append(ci.name)

requireds.sort()
optionals.sort()
multivalueds.sort()
requireds = requireds + optionals

# cis_names = [ci.name for ci in cis]

pprint.pprint(requireds)

pprint.pprint(multivalueds)

# print(yaml_dumper.dumps(view.class_induced_slots(current_class)))
