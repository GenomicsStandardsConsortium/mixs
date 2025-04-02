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
            "Usage: `poetry run python src/scripts/enumerations_list_generator.py <output-file.md>`"
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

        logger.info(f"Term list table has been written to '{output_file}'.")
    except Exception as e:
        logger.error(f"Error writing to '{output_file}': {str(e)}")
