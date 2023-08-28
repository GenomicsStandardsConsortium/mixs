from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

schema_file = "../../generated-schema/mixs_6_2_rc.yaml"
target_class_name = "MimsSoil"

schema_view = SchemaView(schema_file)

all_class_names = schema_view.all_classes()
for c_name in all_class_names:
    print(c_name)

    class_induced_slots = schema_view.class_induced_slots(c_name)
    for cis in class_induced_slots:
        # print(yaml_dumper.dumps(cis))
        print(f"{c_name}: {cis.name}")
