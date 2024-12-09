import click
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper


@click.command()
@click.option('--schema_file', type=str, default="../mixs/schema/mixs.yaml", help="Path to the input schema file.")
@click.option('--output_file', type=str, default='../../mixs_with_enum_descriptions.yaml', show_default=True,
              help="Path to the output schema file with updated enum descriptions.")
def update_enum_descriptions(schema_file: str, output_file: str) -> None:
    """
    Update enum descriptions in the given schema file.

    This script updates the descriptions of enums in a schema YAML file to reflect how they are used
    by other terms (slots). The descriptions will indicate whether an enum is used by any term, and if so,
    by how many terms and which ones.

    :param schema_file: Path to the input schema file.
    :param output_file: Path to the output schema file where the updated schema will be saved.
    """
    schema_view = SchemaView(schema_file)
    schema_enums = schema_view.all_enums()

    for ek, ev in schema_enums.items():
        users = schema_view.get_slots_by_enum(ek)
        user_names = [u.name for u in users]
        user_names.sort()

        if len(user_names) == 0:
            ev.description = "Permissible values, not used by any term"
        elif len(user_names) == 1:
            ev.description = f"Permissible values, used by term {user_names[0]}"
        else:  # len(user_names) > 1
            ev.description = f"Permissible values, used by {len(user_names)} terms: {', '.join(user_names)}"

    yaml_dumper.dump(schema_view.schema, output_file)
    click.echo(f"Enum descriptions updated and saved to {output_file}")


if __name__ == '__main__':
    update_enum_descriptions()
