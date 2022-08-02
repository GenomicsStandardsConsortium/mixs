import csv

import yaml

packages_sheet = []

gsheet_input = "downloads/gsc_mixs6.csv"
output = "generated/variants_env_packs_report.yaml"

with open(gsheet_input, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    package_cols = reader.fieldnames
    for row in reader:
        packages_sheet.append(row)


## treating like keys
# MIXS ID
# Environmental package

## checking for variations (assuming these should be constant acoss Environmental package)
# Definition
#  what is the meaning of this term?
# Occurrence
#  is this term single- or multi-valued?
# Package item
#  what is this term's long name?
# Structured comment name
#  what is this term's short name?
# Value syntax
#  how should this term be validated?

## assuming variation is ok
# Example
# Requirement

## todo
# Expected value
# Preferred unit
# github ticket

check_for_variations = [
    "Definition",
    "Occurrence",
    "Package item",
    "Structured comment name",
    "Value syntax",
]


def get_variations():
    variations = {}
    for i in packages_sheet:
        mixs_id = i["MIXS ID"]
        # env_pack = i["Environmental package"]
        for k, v in i.items():
            if mixs_id in variations:
                if k in variations[mixs_id]:
                    variations[mixs_id][k].append(v)
                else:
                    variations[mixs_id][k] = [v]
            else:
                variations[mixs_id] = {k: [v]}
    return variations


def get_variation_dicts():
    variations = {}
    for i in packages_sheet:
        mixs_id = i["MIXS ID"]
        env_pack = i["Environmental package"]
        for k, v in i.items():
            if k in check_for_variations:
                if mixs_id in variations:
                    if k in variations[mixs_id]:
                        variations[mixs_id][k]["by_package"][env_pack] = v
                        variations[mixs_id][k]["overall"].append(v)
                    else:
                        variations[mixs_id][k] = {
                            "by_package": {env_pack: v},
                            "overall": [v],
                        }
                else:
                    variations[mixs_id] = {
                        k: {"by_package": {env_pack: v}, "overall": [v]}
                    }
    return variations


def report_variant_dicts(variants_dict):
    variants = {}
    for mixs_id, v in variants_dict.items():
        for col, values in v.items():
            unique_values = list(set(values["overall"]))
            if len(unique_values) > 1:
                if mixs_id in variants:
                    variants[mixs_id][col] = values["by_package"]
                else:
                    variants[mixs_id] = {col: values["by_package"]}
    return variants


def report_variants(variants_dict):
    variants = {}
    for mixs_id, v in variants_dict.items():
        for col, values in v.items():
            values = list(set(values))
            if len(values) > 1 and col in check_for_variations:
                for value in values:
                    if mixs_id in variants:
                        if col in variants[mixs_id]:
                            variants[mixs_id][col].append(value)
                        else:
                            variants[mixs_id][col] = [value]
                    else:
                        variants[mixs_id] = {col: [value]}
    return variants


vdd = get_variation_dicts()

vsd = report_variant_dicts(vdd)

with open(output, "w") as outfile:
    yaml.dump(vsd, outfile, default_flow_style=False)
