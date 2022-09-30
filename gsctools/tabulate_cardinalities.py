import csv
import pprint
from collections import Counter

tasks = [
    {"name": "core",
     "path": "../schemasheets/tsv_input/originals_from_gsc_google_sheets/MIxS_6_term_updates_MIxS6_Core-Final_clean.tsv",
     "first_real_row": 1,
     "col_list": ["migs_eu", "migs_ba", "migs_pl", "migs_vi", "migs_org", "mims", "mimarks_s", "mimarks_c", "misag",
                  "mimag",
                  "miuvig"]
     },
    {"name": "packages",
     "path": "../schemasheets/tsv_input/originals_from_gsc_google_sheets/MIxS_6_term_updates_MIxS6_packages-Final_clean.tsv",
     "first_real_row": 1,
     "col_list": ["Requirement"]},
]

for i in tasks:

    core_rows = []

    with open(i["path"], newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter="\t")
        for row in reader:
            selected = {key: value for key, value in row.items() if key in i["col_list"]}
            core_rows.append(selected)

    core_rows = core_rows[i["first_real_row"]:]

    # pprint.pprint(core_rows)

    counter = Counter([val for ele in core_rows for val in ele.values()])
    print(i["name"])
    pprint.pprint(dict(counter))

# core
# {'-': 469, 'C': 222, 'E': 44, 'M': 157, 'X': 175}
# packages
# {'': 3, 'C': 163, 'E': 7, 'M': 190, 'X': 1390}
