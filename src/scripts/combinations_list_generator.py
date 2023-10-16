import sys
import logging
from linkml_runtime.utils.schemaview import SchemaView

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

    sv = SchemaView("src/mixs_6_2_for_merge/schema/mixs_6_2_for_merge.yaml")

    try:
        with open(output_file, "w") as md_file:
            md_file.write("# Combinations\n\n")

            md_file.write("| Name | Description |\n")
            md_file.write("| --- | --- |\n")

            for c in sv.all_classes().values():
                if c.mixins and c.is_a:
                    name = c.name
                    description = c.description
                    link = f"[{name}]({c.from_schema}/{name})"
                    md_file.write(f"| {link} | {description} |\n")

        logger.info(f"Combinations page has been written to '{output_file}'.")
    except Exception as e:
        logger.error(f"Error writing to '{output_file}': {str(e)}")
