import click
import json
from linkml_runtime import SchemaView


@click.command()
@click.option("--schema-input-file", "-i", type=str, help="The input schema file")
@click.option("--menu-json-out", "-o", type=str, help="The output menu JSON file")
def cli(schema_input_file, menu_json_out):
    schema_view = SchemaView(schema_input_file)

    schema_name = schema_view.schema.name

    schema_classes = schema_view.all_classes()
    collection_root_label = ""
    for ck, cv in schema_classes.items():
        if cv.tree_root:
            collection_root_label = ck

    collection_root_slot_names = schema_view.class_slots(collection_root_label)

    inner_menu_dict = {}

    for i in collection_root_slot_names:
        slot_obj = schema_view.get_slot(i)
        inner_menu_dict[slot_obj.range] = {
            "display": True,
            "name": slot_obj.range,
            "status": "published",
        }

    outer_menu_dict = {schema_name: inner_menu_dict}

    with open(menu_json_out, 'w') as fp:
        json.dump(outer_menu_dict, fp, indent=2)


if __name__ == "__main__":
    cli()
