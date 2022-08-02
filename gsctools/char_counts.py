import csv
import pprint
import re
from collections import Counter

# todo refactor into methods
# todo reconcile with similar code
# todo remove hardcoded paths

packages_file = "../downloads/gsc_mixs6.csv"
core_file = "../downloads/gsc_mixs6_core.csv"

list_style_char_count_file = "../generated/list_style_valsyns_char_count.tsv"

packages_lod = []
core_lod = []

with open(packages_file) as f:
    DictReader_obj = csv.DictReader(f)

    for row in DictReader_obj:
        packages_lod.append(row)

with open(core_file) as f:
    DictReader_obj = csv.DictReader(f)

    for row in DictReader_obj:
        core_lod.append(row)

# pprint.pprint(packages_lod)

# value_syntaxes are a special case because they require parsing into tokens

list_style_valsyns = []
pattern_style_valsyns = []
hybrid_valsyns = []
other_valsyns = []

hybrid_pattern = "[;\{]"

for i in packages_lod:
    valsyn = i["Value syntax"]
    if valsyn and valsyn != "":
        if valsyn.startswith("["):
            # if re.match(hybrid_pattern, valsyn):
            if "{" in valsyn or ";" in valsyn:
                hybrid_valsyns.append(valsyn)
            else:
                list_style_valsyns.append(valsyn)
        elif valsyn.startswith("{"):
            pattern_style_valsyns.append(valsyn)
        else:
            other_valsyns.append(valsyn)

for i in core_lod:
    valsyn = i["Value syntax"]
    if valsyn and valsyn != "":
        if valsyn.startswith("["):
            # if re.match(hybrid_pattern, valsyn):
            if "{" in valsyn or ";" in valsyn:
                hybrid_valsyns.append(valsyn)
            else:
                list_style_valsyns.append(valsyn)
        elif valsyn.startswith("{"):
            pattern_style_valsyns.append(valsyn)
        else:
            other_valsyns.append(valsyn)

print("list_style_valsyns")
list_style_counts = Counter(list_style_valsyns)
pprint.pprint(list_style_counts)

list_style_vals = []
for i in list_style_counts:
    list_style_vals.append(i)

list_style_vals = "".join(list_style_vals)
list_style_char_count = dict(Counter(list_style_vals))
list_style_char_count = [{"char": k, "count": v} for k, v in list_style_char_count.items()]

with open(list_style_char_count_file, 'w', newline='') as csvfile:
    fieldnames = ['char', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()
    writer.writerows(list_style_char_count)

print(list_style_vals)

print("pattern_style_valsyns")
pattern_style_counts = Counter(pattern_style_valsyns)
pprint.pprint(pattern_style_counts)

print("hybrid_valsyns")
hybrid_counts = Counter(hybrid_valsyns)
pprint.pprint(hybrid_counts)

print("other_valsyns")
other_counts = Counter(other_valsyns)
pprint.pprint(other_counts)
