import click
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper


@click.command()
@click.option('--input-schema', '-i', type=click.Path(exists=True), required=True)
@click.option('--output-schema', '-o', type=click.Path(), required=True)
@click.option('--deprecation-val', '-d', required=True)
def main(input_schema, output_schema, deprecation_val):
    """
    Removes the classes and slots that have a specified deprecation value
    """
    schema_view = SchemaView(input_schema, merge_imports=True)

    for k, v in schema_view.all_classes().items():
        if v.deprecated == deprecation_val:
            schema_view.delete_class(k)
    for k, v in schema_view.all_slots().items():
        if v.deprecated == deprecation_val:
            del schema_view.schema.slots[k]  # AttributeError: 'SchemaDefinition' object has no attribute 'slotes'

    yaml_dumper.dump(schema_view.schema, output_schema)


if __name__ == '__main__':
    main()
