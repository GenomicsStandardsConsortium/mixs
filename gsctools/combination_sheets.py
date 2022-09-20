import csv
import pprint

from linkml_runtime import SchemaView

# from linkml_runtime.dumpers import yaml_dumper

schema_file = "../schemasheets/yaml_output/mixs_from_schema_sheets.yaml"
tsv_output = "../schemasheets/tsv_input/combination_classes.tsv"

view = SchemaView(schema_file)

checklists_names = view.class_children("Checklist")
checklists_names.sort()

env_package_names = view.class_children("EnvPackage")
env_package_names.sort()

row_list = []

for current_env_package_name in env_package_names:
    current_env_package = view.get_class(current_env_package_name)
    for current_checklist_name in checklists_names:
        current_checklist = view.get_class(current_checklist_name)
        row_list.append(
            {"class": f"{current_env_package_name}{current_checklist_name}",
             "class_uri": "",
             "description": f"{current_checklist.description} with environmental package {current_env_package.description}",
             "is_a": current_env_package_name,
             "mixins": current_checklist_name}
        )

row_list.insert(0, {"class": "> class",
                    "class_uri": "class_uri",
                    "description": "description",
                    "is_a": "is_a",
                    "mixins": "mixins"})

row_list.insert(1, {"class": ">",
                    "class_uri": "",
                    "description": "",
                    "is_a": "",
                    "mixins": 'internal_separator: "|"'})

with open(tsv_output, 'w', newline='') as csvfile:
    fieldnames = list(row_list[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()
    for i in row_list:
        writer.writerow(i)
