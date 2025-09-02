import csv
import pprint

import click
from linkml_runtime import SchemaView
import logging

from linkml_runtime.dumpers import yaml_dumper

logging.basicConfig(level=logging.INFO)


def save_list_of_dicts_to_tsv(list_of_dicts, tsv_file_path, fieldnames):
    """Saves a list of dicts to a TSV file using the DictWriter class.

    Args:
      list_of_dicts: A list of dicts to save to the TSV file.
      tsv_file_path: The path to the TSV file.
      fieldnames: A list of the fieldnames for the TSV file.
    """

    with open(tsv_file_path, "w", newline="") as tsv_file:
        writer = csv.DictWriter(tsv_file, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        for dict in list_of_dicts:
            writer.writerow(dict)


@click.command()
@click.option('--input-schema', required=True, type=click.Path(exists=True),
              help='The path to a LinkML YAML schema file.')
@click.option('--output', required=True, type=click.Path(), help='The path where a TSV report should be written.')
def find_required_and_recommended_usages(input_schema, output):
    """Will report and optionally fix slot_usages with both required and recommended asserted."""

    logging.info(f"Loading schema from {input_schema}")
    schema_view = SchemaView(input_schema)
    logging.info(f"Loaded {schema_view.schema.name}")

    class_names = list(schema_view.all_classes().keys())
    class_names.sort()

    required_and_recommended_usages = []

    for class_name in class_names:
        logging.info(f"Checking {class_name}")
        class_def = schema_view.get_class(class_name)
        is_combination = "combination_classes" in (class_def.in_subset or [])
        
        induced_slots = schema_view.class_induced_slots(class_name)
        for induced_slot in induced_slots:
            required_state = induced_slot.required
            recommended_state = induced_slot.recommended
            if required_state and recommended_state:
                logging.info(f"\trequired and recommended: {class_name} {induced_slot.name}")
                required_and_recommended_usages.append({
                    "class_name": class_name, 
                    "slot_name": induced_slot.name,
                    "is_combination": is_combination
                })

    # logging.info(pprint.pformat(required_and_recommended_usages))

    save_list_of_dicts_to_tsv(required_and_recommended_usages, output, required_and_recommended_usages[0].keys())


if __name__ == '__main__':
    find_required_and_recommended_usages()
