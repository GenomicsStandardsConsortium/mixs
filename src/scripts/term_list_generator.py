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
              default='docs/term_list.md',
              help='Output Markdown file for term list documentation')
@click.option('--schema-file', '-s',
              default='src/mixs/schema/mixs.yaml',
              help='Input MIxS schema YAML file')
def generate_term_list(output_file, schema_file):

    """Generate Markdown documentation of all terms in MIxS schema."""
    
    docgen = DocGenerator(
        schema_file,
        template_directory="src/doc-templates",
        directory="docs",
        use_slot_uris=True,
        use_class_uris=True,
    )
    terms = list(docgen.all_slot_objects())

    try:
        with open(output_file, "w") as md_file:
            md_file.write("# All terms in MIxS schema\n\n")

            md_file.write("| Title (Name) | Description |\n")
            md_file.write("| --- | --- |\n")

            for t in terms:
                if t.domain == "MixsCompliantData":
                    continue

                description = t.description
                link = docgen.link(t.name)
                md_file.write(f"| {t.title} ({link}) | {description} |\n")

        logger.info(f"Term list table has been written to '{output_file}'.")
    except Exception as e:
        logger.error(f"Error writing to '{output_file}': {str(e)}")


if __name__ == '__main__':
    generate_term_list()
