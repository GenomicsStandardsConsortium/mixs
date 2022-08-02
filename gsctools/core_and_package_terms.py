import csv
import pprint

packages_sheet = []
packages_terms = set()
core_sheet = []
core_terms = set()

packages_input = "../downloads/gsc_mixs6.csv"
core_input = "../downloads/gsc_mixs6_core.csv"

output = ""

with open(packages_input, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    package_cols = reader.fieldnames
    for row in reader:
        packages_sheet.append(row)
        packages_terms.add(row["Structured comment name"])

with open(core_input, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    package_cols = reader.fieldnames
    for row in reader:
        core_sheet.append(row)
        core_terms.add(row["Structured comment name"])

core_and_packages_terms = list(packages_terms.intersection(core_terms))
core_and_packages_terms.sort()

row_list = []
for i in packages_sheet:
    if i['Structured comment name'] in core_and_packages_terms:
        row_list.append({'MIXS ID': i['MIXS ID'], 'Structured comment name': i['Structured comment name'],
                         'Environmental package': i['Environmental package']})
        # print(f"{i['MIXS ID']} {i['Structured comment name']} {i['Environmental package']}")


pprint.pprint(row_list)
# pprint.pprint(core_and_packages_terms)
