import click
from rdflib import Graph


@click.command()
@click.option("--rdf-file", required=True, help="The RDF file to validate.")
@click.option("--rdf-format", default='turtle',
              help="The format of the RDF data. Defaults to 'turtle' See https://rdflib.readthedocs.io/en/stable/intro_to_parsing.html.")
def main(rdf_file, rdf_format):
    """Validates RDF data using rdflib."""

    # open the RDF file
    with open(rdf_file, "r") as f:
        rdf_data = f.read()
        is_valid = is_rdf_valid(rdf_data, rdf_format)
        if is_valid:
            print(f"{rdf_file} is valid.")


def is_rdf_valid(rdf_data, rdf_format):
    """Validates RDF data using rdflib."""

    try:
        g = Graph()
        g.parse(data=rdf_data, format=rdf_format)
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    main()

# see also riot --validate data.ttl
