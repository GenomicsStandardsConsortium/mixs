import csv
import yaml

from click import command, option


@command()
@option("--ncbi-harmonized-names-file", "-n", required=True,
        help="The path to the table of NCBI Biosample harmonized names.")
@option("--mixs-scns-file", "-m", required=True, help="The path to the harmonized MixS v6.xlsx spreadsheet.")
@option("--output-file", "-o", required=True, help="The path to the output YAML file.")
def cli(ncbi_harmonized_names_file, mixs_scns_file, output_file):
    """
    A CLI tool to compare the terms in the NCBI Biosample Harmonized Attribute Usage spreadsheet and the MixS v6.xlsx spreadsheet.
    """

    with open(mixs_scns_file, mode='r') as infile:
        reader = csv.DictReader(infile, delimiter="\t")
        mixs_scns = set()
        for row in reader:
            if 'Structured comment name' in row:
                mixs_scns.add(row['Structured comment name'])

    with open(ncbi_harmonized_names_file, mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {rows[0]: rows[1] for rows in reader if rows[0] != ''}  # exclude counts if the key is ''

    mixs_scns = list(mixs_scns)
    mixs_scns.sort()

    ncbi_harmonized_names = list(mydict.keys())
    ncbi_harmonized_names.sort()

    mixs_only = list(set(mixs_scns) - set(ncbi_harmonized_names))

    mixs_only.sort()

    ncbi_only = list(set(ncbi_harmonized_names) - set(mixs_scns))
    ncbi_only.sort()

    output_dict = {
        "mixs_only": {
            "mixs_term_count": len(mixs_scns),
            "mixs_only_terms": mixs_only,
            "mixs_only_term_count": len(mixs_only)
        },
        "ncbi_only": {
            "ncbi_harmonized_name_count": len(ncbi_harmonized_names),
            "ncbi_only_terms": ncbi_only,
            "ncbi_only_term_count": len(ncbi_only)
        },
    }

    try:
        with open(output_file, "w") as output_file:
            yaml.dump(output_dict, output_file)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    cli()
