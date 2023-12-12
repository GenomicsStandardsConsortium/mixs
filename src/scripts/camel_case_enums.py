import copy

from linkml.utils.schema_fixer import SchemaFixer
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.utils.formatutils import camelcase

schema_file = "../mixs/schema/mixs.yaml"

schema_view = SchemaView(schema_file)

schema_enums = schema_view.all_enums()
schema_classes = schema_view.all_classes()

class_names = list(schema_classes.keys())
class_names = [str(x) for x in class_names]
class_names.sort()

range_modifying_slot_usages = []

# are there any slot_usage range assertions, or can we just update the slots ranges globally?
for current_class in class_names:
    slot_usage = schema_classes[current_class].slot_usage
    if slot_usage:
        if "range" in slot_usage and slot_usage["range"]:
            print(
                f"{current_class} asserts a range of {slot_usage['range']} in it's slot_usage"
            )
            range_modifying_slot_usages.append((current_class, slot_usage["range"]))
        else:
            pass
    else:
        pass
if len(range_modifying_slot_usages) > 0:
    exit()

enum_names = list(schema_enums.keys())
enum_names = [str(x) for x in enum_names]
enum_names.sort()

schema_slots = schema_view.all_slots()
slot_names = list(schema_slots.keys())
slot_names = [str(x) for x in slot_names]
slot_names.sort()

for current_slot_name in slot_names:
    current_slot = schema_slots[current_slot_name]
    slot_range = current_slot.range
    if str(slot_range) in enum_names:
        as_camel = camelcase(slot_range.lower())
        schema_view.schema.slots[current_slot_name].range = as_camel

print(yaml_dumper.dumps(schema_view.schema.slots))

for current_enum_name in enum_names:
    current_enum = schema_enums[current_enum_name]
    as_camel = camelcase(current_enum_name.lower())
    new_enum = copy.deepcopy(current_enum)
    new_enum.name = as_camel
    del schema_view.schema.enums[current_enum_name]
    schema_view.schema.enums[as_camel] = new_enum

print(yaml_dumper.dumps(schema_view.schema.enums))

yaml_dumper.dump(schema_view.schema, "camel_case_enums.yaml")

x = SchemaFixer()
