import pprint

import click

from linkml_runtime import SchemaView

import yaml


def compare_slots_by_extension(ext_slot_pairings, ext1, ext2):
    """
    Compares slots for two extensions in a list of dictionaries.

    Args:
      ext_slot_pairings: A list of dictionaries, each with "extension" and "slot" keys.
      ext1: The first extension to compare.
      ext2: The second extension to compare.

    Returns:
      A dictionary with two keys:
        - ext1_only: A list of slots unique to the first extension.
        - ext2_only: A list of slots unique to the second extension.
    """
    ext1_slots = set()
    ext2_slots = set()
    for item in ext_slot_pairings:
        if item["extension"] == ext1:
            ext1_slots.add(item["slot"])
        elif item["extension"] == ext2:
            ext2_slots.add(item["slot"])

    return {
        f"{ext1}_only": sorted(list(ext1_slots - ext2_slots)),
        f"{ext2}_only": sorted(list(ext2_slots - ext1_slots)),
        f"intersection": sorted(ext1_slots.intersection(ext2_slots)),
    }


@click.command()
@click.option('--schema', '-s',
              default='src/mixs/schema/mixs.yaml',
              required=True,
              help='Path to the schema file')
@click.option('--ext1', default="Soil", type=str, help='Enter the first extension name:')
@click.option('--ext2', default="Water", type=str, help='Enter the second extension name:')
def set_arithmatic(schema, ext1, ext2):
    schema_view = SchemaView(schema)

    extension_class_names = schema_view.class_descendants('Extension')
    checklist_class_names = schema_view.class_descendants('Checklist')

    lod = []

    for current_extension in extension_class_names:
        if current_extension in checklist_class_names:
            continue
        extension_obj = schema_view.induced_class(current_extension)

        extension_slots = list(extension_obj.attributes.keys())
        for current_slot in extension_slots:
            temp_dict = {
                "extension": str(current_extension),
                "slot": str(current_slot)
            }
            lod.append(temp_dict)

    result = compare_slots_by_extension(lod, ext1, ext2)

    # pprint.pprint(result)

    # create a yaml representation of the result
    yaml_string = yaml.dump(result)
    print(yaml_string)


if __name__ == '__main__':
    set_arithmatic()
