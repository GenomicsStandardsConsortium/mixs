import click
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from yaml import load, FullLoader
from typing import List, Set, Dict, Any, Union


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
@click.option('--include-parent-classes', is_flag=True, help='Include parent classes in the output.')
@click.option('--eligible-parent-classes', multiple=True, default=['Checklist', 'Extension'],
              help='Eligible parent classes to include in the output.')
@click.option('--delete-attributes', multiple=True, default=['domain_of', 'alias', 'from_schema', 'owner'],
              help='Attributes of the classes to delete before printing.')
def process_schema_classes(schema_file: str, include_parent_classes: bool, eligible_parent_classes: List[str],
                           delete_attributes: List[str]):
    """
    Processes eligible classes from a given schema, filtering based on specified parent classes,
    and modifies attributes of these classes based on specified operations.
    """
    schema_view = SchemaView(schema_file)
    all_paths: Set[str] = set()

    eligible_leaves: Set[str] = set()
    for parent_class in eligible_parent_classes:
        current_eligible_leaves = schema_view.class_descendants(parent_class, reflexive=include_parent_classes)
        eligible_leaves.update(current_eligible_leaves)

    eligible_leaves = sorted(eligible_leaves)
    for class_name in eligible_leaves:
        print(class_name)
        induced_class = schema_view.induced_class(class_name)
        induced_attributes = induced_class.attributes
        for attribute_name, attribute_value in induced_attributes.items():
            for attribute in delete_attributes:
                if hasattr(attribute_value, attribute):
                    delattr(attribute_value, attribute)
    #         yaml_output = yaml_dumper.dumps(attribute_value)
    #         attribute_data = load(yaml_output,
    #                               Loader=FullLoader)  # parse the YAML back to a Python object # todo inefficient
    #         collect_paths(attribute_data, [], all_paths)  # collect paths
    #
    # print("Collected Paths:")
    # for path in sorted(all_paths):
    #     print(path)

    # Collected Paths:
    # annotations
    # annotations/Expected_value
    # annotations/Expected_value/tag
    # annotations/Expected_value/value
    # annotations/Preferred_unit
    # annotations/Preferred_unit/tag
    # annotations/Preferred_unit/value
    # comments
    # comments/0
    # comments/1
    # description
    # examples
    # examples/0
    # examples/0/description
    # examples/0/value
    # examples/1
    # examples/1/description
    # examples/1/value
    # in_subset
    # in_subset/0
    # keywords
    # keywords/0
    # keywords/1
    # keywords/2
    # keywords/3
    # keywords/4
    # keywords/5
    # multivalued
    # name
    # pattern
    # range
    # recommended
    # required
    # slot_uri
    # string_serialization
    # structured_pattern
    # structured_pattern/interpolated
    # structured_pattern/partial_match
    # structured_pattern/syntax
    # title


if __name__ == "__main__":
    process_schema_classes()
