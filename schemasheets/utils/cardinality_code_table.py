import pprint

import linkml_runtime
import pandas as pd
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

pd.set_option('display.max_columns', None)

ss_config_url = "https://raw.githubusercontent.com/linkml/schemasheets/main/schemasheets/conf/configschema.yaml"

cardinality_tsv = "../cardinality_frame.tsv"

ss_config_view = SchemaView(ss_config_url)

cardinality_pvs = ss_config_view.get_enum("Cardinality").permissible_values

# print(yaml_dumper.dumps(cardinality_pvs))

cardinality_dict = {}
cardinality_lod = []
for pvk, pvv in cardinality_pvs.items():
    inner_dict = dict()
    inner_dict["permissible_value"] = pvk
    inner_dict["description"] = pvv.description
    if "annotations" in pvv:
        for ak, av in pvv.annotations.items():
            if type(av.value) in [str, linkml_runtime.utils.yamlutils.extended_str]:
                inner_dict[ak] = av.value
            else:
                print(f"skipping {av.value} with type {type(av.value)}")
        # inner_dict["annotations"] = pvv.annotations
    # cardinality_dict[pvk] = inner_dict
    cardinality_lod.append(inner_dict)

# pprint.pprint(cardinality_lod)

cardinality_frame = pd.DataFrame(cardinality_lod)

# print(cardinality_frame)

cardinality_frame.to_csv(cardinality_tsv, sep="\t", index=False)
