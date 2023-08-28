import pprint

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

schema_file = "../../generated-schema/mixs_6_2_rc.yaml"

schema_view = SchemaView(schema_file)

enums = schema_view.all_enums()

for ek, ev in enums.items():
    if ev.reachable_from:
        print(ek)

