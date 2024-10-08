import sys
import logging
from linkml.generators.docgen import DocGenerator

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error(
            "Usage: `poetry run python scripts/term_list_generator.py <output-file.md>`"
        )
        sys.exit(1)

    output_file = sys.argv[1]

    docgen = DocGenerator(
        "src/mixs/schema/mixs.yaml",
        template_directory="src/doc-templates",
        directory="docs",
        use_slot_uris=True,
        use_class_uris=True,
    )
    classes = list(docgen.all_class_objects())

    try:
        with open(output_file, "w") as md_file:
            md_file.write("# All combinations in MIxS schema\n\n")

            md_file.write("| Name | Description |\n")
            md_file.write("| --- | --- |\n")

            for c in classes:
                if c.mixins and c.is_a:
                    description = c.description
                    link = docgen.link(c.name)
                    md_file.write(f"| {link} | {description} |\n")

        logger.info(f"Combinations page has been written to '{output_file}'.")
    except Exception as e:
        logger.error(f"Error writing to '{output_file}': {str(e)}")
