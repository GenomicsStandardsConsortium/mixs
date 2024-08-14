import csv
import importlib.resources as pkg_resources
import os
import pprint
from importlib import resources
from importlib.resources import files
from typing import List, Set, Dict, Union

import click
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.linkml_model import SlotDefinition

from collections import OrderedDict
import requests

import yaml


# def get_metaview():
#     # Try to access the resource using a known part of the package structure
#     package_name = 'linkml_runtime.linkml_model.model.schema'
#     try:
#         # Dynamically obtain a reference to the package containing the resource
#         resource_package = files(package_name)
#     #
#     #     # Use this reference to open 'meta.yaml'
#     #     with pkg_resources.as_file(resource_package.joinpath('meta.yaml')) as file_path:
#     #         with open(file_path, 'r') as file:
#     #             meta_yaml_content = file.read()
#     #             return SchemaView(meta_yaml_content)
#     except Exception as e:
#         print(f"Error accessing the meta.yaml file: {e}")
#         exit()

def list_package_contents(package_name):
    try:
        # List all resources in the specified package
        entries = resources.contents(package_name)
        return list(entries)
    except Exception as e:
        print(f"Error accessing package contents: {e}")
        return []


def get_metaview():
    file_path = '/Users/MAM/Documents/gitrepos/mixs/.venv/lib/python3.9/site-packages/linkml_runtime/linkml_model/model/schema/meta.yaml'
    package_name = 'linkml_runtime.linkml_model.model.schema'
    resource_name = 'meta.yaml'
    url = 'https://w3id.org/linkml/meta.yaml'
    try:
        # Make a GET request to fetch the content of the meta.yaml file
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        meta_yaml_content = response.text
        return SchemaView(meta_yaml_content)
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None


def collect_paths(data: Union[Dict, List], current_path: List[str], paths: Set[str]):
    """
    Recursively collects paths from nested dictionaries and lists.

    Args:
        data: The current data to process (could be a dict or list).
        current_path: The path leading to the current data.
        paths: Set of paths collected.
    """
    if isinstance(data, dict):
        for key, value in data.items():
            path = current_path + [key]
            paths.add('/'.join(path))
            collect_paths(value, path, paths)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            path = current_path + [str(index)]
            paths.add('/'.join(path))
            collect_paths(item, path, paths)


@click.command()
@click.option('--schema-file', default='src/mixs/schema/mixs.yaml', type=click.Path(exists=True, dir_okay=False),
              help='Path to the schema YAML file.')
@click.option('--output-dir', default='project/class-model-tsvs', type=click.Path(dir_okay=True, file_okay=False),
              help='Directory for saving teh TSV representations of MIxS classes.')
@click.option('--include-parent-classes', is_flag=True, default=False, help='Include parent classes in the output.')
@click.option('--eligible-parent-classes', multiple=True, default=['Checklist', 'Extension'],
              help='Eligible parent classes to include in the output.')
@click.option('--delete-attributes', multiple=True, default=['domain_of', 'alias', 'from_schema', 'owner'],
              help='Attributes of the classes to delete before printing.')
@click.option('--metaslots', multiple=True,
              default=[
                  'name',
                  'title',
                  'slot_uri',
                  'comments',
                  'description',
                  'examples',
                  'in_subset',
                  'keywords',
                  'multivalued',
                  'pattern',
                  'range',
                  'recommended',
                  'required',
                  'string_serialization',
                  'structured_pattern',
              ],
              help='Metaslot names to include in the TSV output.')
@click.option('--annotations', multiple=True,
              default=[
                  'Expected_value',
                  'Preferred_unit',
              ],
              help='Metaslot names to include in the TSV output.')
def process_schema_classes(schema_file: str, include_parent_classes: bool, eligible_parent_classes: List[str],
                           delete_attributes: List[str], metaslots: List[str], annotations: List[str],
                           output_dir: str):
    """
    Processes eligible classes from a given schema, filtering based on specified parent classes,
    and generates a directory of TSV files representing the attributes of these classes.
    """
    schema_view = SchemaView(schema_file)

    metaview = get_metaview()

    metaslots_helper = {}
    for metaslot in metaslots:
        metaslot_obj = metaview.get_slot(metaslot)
        fallback_range = metaslot_obj.range if metaslot_obj.range else metaview.schema.default_range
        range_element = metaview.get_element(fallback_range)

        range_element_ccc = range_element.class_class_curie
        if fallback_range == "boolean":
            fallback = False
        else:
            fallback = None

        metaslots_helper[metaslot] = {
            "fallback": fallback,
            "metatype": range_element_ccc,
            "multivalued": metaslot_obj.multivalued if metaslot_obj.multivalued is not None else False,
            "range": fallback_range,
        }

    # pprint.pprint(metaslots_helper)

    eligible_leaves: Set[str] = set()
    for parent_class in eligible_parent_classes:
        current_eligible_leaves = schema_view.class_descendants(parent_class, reflexive=include_parent_classes)
        eligible_leaves.update(current_eligible_leaves)

    sorted_eligible_leaves = sorted(eligible_leaves)
    os.makedirs(output_dir, exist_ok=True)

    for class_name in sorted_eligible_leaves:
        induced_class = schema_view.induced_class(class_name)
        induced_attributes = induced_class.attributes

        # Sorting the keys based on the 'name' field in each object
        sorted_keys = sorted(induced_attributes, key=lambda x: induced_attributes[x]['name'])

        # Creating a new OrderedDict that preserves the new order
        sorted_induced_attributes = OrderedDict((k, induced_attributes[k]) for k in sorted_keys)

        with open(f"{output_dir}/{class_name}.tsv", 'w', newline='') as tsvfile:
            writer = csv.DictWriter(tsvfile, fieldnames=(metaslots + annotations), delimiter='\t')
            writer.writeheader()

            rows = []

            for iak, iav in sorted_induced_attributes.items():
                temp_dict = {}
                for mhk, mhv in metaslots_helper.items():
                    # Attempt to fetch the value for the current metaslot from the induced attribute
                    iav_mhk_val = getattr(iav, mhk, metaslots_helper[mhk]["fallback"])

                    if mhk == "examples":
                        if iav_mhk_val:
                            example_reprs = []
                            for current_example in iav_mhk_val:
                                examples_dict = {
                                    "value": current_example.value,
                                }
                                if current_example.description:
                                    examples_dict["description"] = current_example.description
                                example_reprs.append(temp_dict)
                            temp_dict[mhk] = examples_dict.__repr__()

                    elif mhk == "structured_pattern":
                        if iav_mhk_val:
                            structured_pattern_dict = {
                                "syntax": iav_mhk_val.syntax,
                                "interpolated": iav_mhk_val.interpolated if iav_mhk_val.interpolated is not None else False,
                                "partial_match": iav_mhk_val.partial_match if iav_mhk_val.partial_match is not None else False,
                            }
                            temp_dict[mhk] = structured_pattern_dict.__repr__()

                    # Check conditions for metatype and whether it is multivalued
                    elif not mhv["multivalued"] and mhv["metatype"] in ["linkml:TypeDefinition",
                                                                        "linkml:ClassDefinition"]:
                        # For non-multivalued metatypes that are TypeDefinition or ClassDefinition
                        temp_dict[mhk] = iav_mhk_val
                    elif mhv["multivalued"] and mhv["metatype"] in ["linkml:TypeDefinition", "linkml:ClassDefinition"]:
                        # For multivalued metatypes that are TypeDefinition or ClassDefinition
                        # Ensure it's a list, join it into a string, and assign
                        if isinstance(iav_mhk_val, list):
                            iav_mhk_val = '|'.join(iav_mhk_val)
                        temp_dict[mhk] = iav_mhk_val
                    else:
                        # Handle other cases or unknowns
                        print(f"Unhandled case for {class_name}, {iak}, {mhk} with type {mhv['metatype']}")
                        temp_dict[mhk] = None
                for annotation_name in annotations:
                    if annotation_name in iav.annotations:
                        # print(class_name, annotation_name, iav.annotations[annotation_name].value)
                        temp_dict[annotation_name] = iav.annotations[annotation_name].value
                    else:
                        # print(f"didn't see {annotation_name} annotation in {class_name}'s {iak}")
                        pass

                rows.append(temp_dict)
                writer.writerow(temp_dict)


if __name__ == "__main__":
    process_schema_classes()
