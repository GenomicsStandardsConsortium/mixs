from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

import click


@click.command()
@click.option('--input_schema', type=click.Path(exists=True), help='LinkML schema to merge')
@click.option('--output', prompt='Your name', help='Destination for merged file')
def cli(input_schema, output):
    """Merges a schema's import closure and writes to an output file."""

    # todo test for write-ability first

    view = SchemaView(input_schema)

    view.merge_imports()

    yaml_dumper.dump(view.schema, output)


if __name__ == '__main__':
    cli()
