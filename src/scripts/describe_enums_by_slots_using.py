from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

schema_file = "src/mixs/schema/mixs.yaml"  # if being run from the src/scripts directory
schema_view = SchemaView(schema_file)

schema_enums = schema_view.all_enums()

for ek, ev in schema_enums.items():
    users = schema_view.get_slots_by_enum(ek)
    user_names = [u.name for u in users]
    user_names.sort()
    # if len(user_names) != 1:
    #     print(f"Enum: {ek} used by: {len(user_names)} terms: {user_names}")
    if len(user_names) == 0:
        ev.description = f"permissible values, not used by any term"
    elif len(user_names) == 1:
        ev.description = f"permissible values, used by term {user_names[0]}"
    else:  # len(user_names) > 1
        ev.description = f"permissible values, used by {len(user_names)} terms: {', '.join(user_names)}"

yaml_dumper.dump(schema_view.schema, "mixs_with_enum_descriptions.yaml")
