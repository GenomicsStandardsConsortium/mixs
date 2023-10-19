import click
from linkml_runtime import SchemaView
import logging

logging.basicConfig(level=logging.INFO)


@click.command()
@click.option('--input-schema', type=click.Path(exists=True), help='The path to a LinkML YAML schema file.')
def find_required_and_recommended_usages(input_schema):
    """Will report and optionally fix slot_usages with both required and recommended asserted."""
    schema_view = SchemaView(input_schema)
    logging.info(schema_view.schema.name)


if __name__ == '__main__':
    find_required_and_recommended_usages()
