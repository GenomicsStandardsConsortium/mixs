import pprint

import click
import requests
import yaml

import csv


def read_ontologies_yml(obo_yaml_url):
    """Reads the ontologies.yml file into a Python dictionary.

    Returns:
      A dictionary of ontologies.
    """

    response = requests.get(obo_yaml_url)
    if response.status_code == 200:
        ontologies_yml = response.content
        ontologies = yaml.safe_load(ontologies_yml)
        return ontologies
    else:
        return None


def read_tsv_file(tsv_file):
    """Reads a TSV file into a list of dictionaries.

    Args:
      tsv_file: The path to the TSV file.

    Returns:
      A list of dictionaries.
    """

    with open(tsv_file, "r") as f:
        reader = csv.DictReader(f, delimiter="\t", fieldnames=None)
        data = []
        for row in reader:
            data.append(row)
        return data


def write_list_of_dicts_to_tsv(list_of_dicts, tsv_file):
    """Writes a list of dictionaries to a TSV file.

    Args:
      list_of_dicts: The list of dictionaries to write.
      tsv_file: The path to the TSV file to write to.
    """

    with open(tsv_file, "w") as f:
        writer = csv.DictWriter(f, delimiter="\t", fieldnames=list_of_dicts[0].keys())
        writer.writeheader()
        for dictionary in list_of_dicts:
            writer.writerow(dictionary)


def match_mixs_against_obo(obo_dict, mixs_lod, ignored_ontology):
    obo_abbreviations = [i['id'].upper() for i in obo_dict['ontologies']]
    matches = []
    for i in mixs_lod:
        class_name = i['class']
        scn = i['Structured comment name']
        for k, v in i.items():
            m = contains_any(v, obo_abbreviations, ignored_ontology)
            if v and m and k not in ['class', 'Structured comment name', 'MIXS ID']:
                matches.append(
                    {
                        'MIXS ID': i['MIXS ID'],
                        'Structured comment name': scn,
                        'class': class_name,
                        'mixs matching attribute': k,
                        'mixs matching value': v,
                        'ontology id': m,
                    }
                )
    return matches


def contains_any(string,
                 list_of_strings,
                 excluded_strings=(
                         'EV',
                         'FAO',
                         'MA',
                         'MI',
                         'SO',
                 )):
    """Checks if a string contains any of the strings in a list.

    Args:
      string: The string to check.
      list_of_strings: The list of strings to check against.
      excluded_strings: A list of strings to exclude from the check.

    Returns:
      True if the string contains any of the strings in the list, False otherwise.
    """

    for s in list_of_strings:
        if s in string and s not in excluded_strings:
            return s


# if __name__ == "__main__":
#     ontologies = read_ontologies_yml()
#     mixs = read_tsv_file("../../GSC-excel-harmonized-repaired/mixs_v6.xlsx.harmonized.tsv")
#     matches = match_mixs_against_obo(ontologies, mixs)
#     write_list_of_dicts_to_tsv(matches, "../../mixs-vs-obo.tsv")


@click.command()
@click.option("--obo-yaml-url", type=str, help="The path to the ontologies.yml file.",
              default="https://obofoundry.org/registry/ontologies.yml")
@click.option("--mixs-tsv", type=str, required=True, help="The path to the mixs_v6.xlsx.harmonized.tsv file.",
              default="GSC-excel-harmonized-repaired/mixs_6_2_rc.repaired.tsv")
@click.option("--results-tsv", type=str, required=True, help="The path to the mixs_v6.xlsx.harmonized.tsv file.",
              default="other-reports/mixs-vs-obo.tsv")
@click.option("--ignored-ontology", multiple=True)
def cli(obo_yaml_url, mixs_tsv, results_tsv, ignored_ontology):
    """Matches MixS terms against OBO ontologies."""
    obo_dict = read_ontologies_yml(obo_yaml_url)
    mixs_lod = read_tsv_file(mixs_tsv)

    matches = match_mixs_against_obo(obo_dict, mixs_lod, ignored_ontology)

    write_list_of_dicts_to_tsv(matches, results_tsv)


if __name__ == "__main__":
    cli()
