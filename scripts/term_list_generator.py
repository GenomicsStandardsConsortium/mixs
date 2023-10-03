import sys
import logging
from typing import Iterator
from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.linkml_model.meta import SlotDefinition

logging.basicConfig(
    filename="term_list_generator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def all_slot_objects(sv: SchemaView) -> Iterator[SlotDefinition]:
    """
    all slot objects in schema

    Ensures rank is non-null
    :return: iterator
    """
    elts = sv.all_slots().values()
    for e in elts:
        yield e


if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error(
            "Usage: `poetry run python scripts/term_list_generator.py <output-file.md>`"
        )
        sys.exit(1)

    output_file = sys.argv[1]

    sv = SchemaView("generated-schema/mixs_6_2_rc.yaml")
    terms = list(all_slot_objects(sv))

    try:
        with open(output_file, "w") as md_file:
            md_file.write("# List of all terms in MIXS schema\n\n")

            md_file.write("| Name | Description |\n")
            md_file.write("| --- | --- |\n")

            for t in terms:
                name = t.name
                description = t.description
                link = f"[{name}]({t.from_schema}/{t.slot_uri.split(':')[-1]})"
                md_file.write(f"| {link} | {description} |\n")

        logger.info(f"Term list table has been written to '{output_file}'.")
    except Exception as e:
        logger.error(f"Error writing to '{output_file}': {str(e)}")
