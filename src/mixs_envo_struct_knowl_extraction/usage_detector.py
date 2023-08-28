import csv

from click import command, option
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper


@command()
@option('--schema-file', '-s', type=str, required=True, help='The path to the schema file.')
@option('--report-yaml-file', '-y', type=str, help='The path to the YAML report file.')
@option('--report-tsv-file', '-t', type=str, required=True, help='The path to the TSV report file.')
@option('--ignore-attributes', '-i', type=str, multiple=True,
        default=['annotations', 'examples', 'name', 'recommended', 'required', 'string_serialization'],
        help='Attributes to ignore.')
def main(schema_file, report_yaml_file, report_tsv_file, ignore_attributes):
    """Generate a slot usage report."""

    report_rows = []

    schema_view = SchemaView(schema_file)

    schema_classes = schema_view.all_classes()

    for sck, scv in schema_classes.items():
        su = scv.slot_usage
        for suk, suv in su.items():
            suvd = suv.__dict__
            for suvdk, suvdv in suvd.items():
                if suvdv and suvdk not in ignore_attributes:
                    report_rows.append({"class": sck, "slot": suk, "attribute": suvdk, "value": suvdv})

    if report_yaml_file:
        yaml_dumper.dump(report_rows, report_yaml_file)

    with open(report_tsv_file, 'w', newline='') as tsvfile:
        writer = csv.DictWriter(tsvfile, fieldnames=report_rows[0].keys(), delimiter='\t')
        writer.writeheader()
        writer.writerows(report_rows)


if __name__ == '__main__':
    main()
