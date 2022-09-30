import pprint

import yaml
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

configschema_url = "https://raw.githubusercontent.com/linkml/schemasheets/main/schemasheets/conf/configschema.yaml"

configschema_view = SchemaView(configschema_url)

cardinality_enum = configschema_view.get_enum("Cardinality")

cardinality_pvs = cardinality_enum.permissible_values

cp_string = yaml_dumper.dumps(cardinality_pvs)

cp_dict = yaml.load(cp_string, Loader=yaml.Loader)

pprint.pprint(cp_dict)

flattened_dict = {}
for pv_label, pv_def in cp_dict.items():
    # print(f"{pv_label} = {pv_def}")
    for pv_attrib_label, pv_attrib_def in pv_def.items():
        # print(f"    {pv_attrib_label} = {pv_attrib_def}")
        if type(pv_attrib_def) == list:
            pv_attrib_def = '|'.join(pv_attrib_def)
        # elif type(pv_attrib_def) == dict:
        #     pv_attrib_def = '|'.join(pv_attrib_def.values())

pprint.pprint(cp_dict)