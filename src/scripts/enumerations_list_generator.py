import click
import logging
from linkml.generators.docgen import DocGenerator

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@click.command()
@click.option('--output-file', '-o',
              default='docs/enumerations.md',
              help='Output Markdown file for enumerations documentation')
@click.option('--schema-file', '-s',
              default='src/mixs/schema/mixs.yaml',
              help='Input MIxS schema YAML file')
def generate_enumerations(output_file, schema_file):

    """Generate Markdown documentation of all enumerations in MIxS schema."""
    
    docgen = DocGenerator(
        schema_file,
        template_directory="src/doc-templates",
        directory="docs",
        use_slot_uris=True,
        use_class_uris=True,
    )
    enums = list(docgen.all_enum_objects())

    try:
        with open(output_file, "w") as md_file:
            md_file.write("# All enumerations in MIxS schema\n\n")

            for e in enums:
                md_file.write(f"## {docgen.link(e.name)}\n\n")
                md_file.write("| Permissible Values |\n")
                md_file.write("| --- |\n")
                for pv_name, _ in e.permissible_values.items():
                    md_file.write(f"| {pv_name} |\n")

                md_file.write("\n")

        logger.info(f"Enumerations documentation has been written to '{output_file}'.")
    except Exception as e:
        logger.error(f"Error writing to '{output_file}': {str(e)}")


if __name__ == '__main__':
    generate_enumerations()
