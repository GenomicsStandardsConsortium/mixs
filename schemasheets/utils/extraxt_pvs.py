import csv
import pprint
import re

enums_prep_file = "../tsv_in/MIxS_6_term_updates_MIxS6_Core-Final_clean_slotdefs.tsv"
# slot_key = 'SAFE Structured comment name'
# pvs_key = 'Value syntax'

# enums_prep_file = "../tsv_in/MIxS_6_term_updates_MIxS6_packages-Final_clean_slotdefs_non_conflicting_shared.tsv"
slot_key = 'SAFE Structured comment name'
pvs_key = 'Value syntax'

keys = ['enum', 'permissible_values', 'suspect', 'single']
prob_chars = [
    "'",
    "(",
    ")",
    "+",
    ";",
    "{",
    "}",
    '"',
]
pvs_prep_file = "../tsv_in/enums_generated.tsv"

lod = []
suspects = []
singles = []
with open(enums_prep_file) as tsvfile:
    reader = csv.DictReader(tsvfile, dialect='excel-tab')
    for row in reader:
        suspect = False
        if slot_key not in row:
            exit
        if pvs_key not in row:
            exit
        pvs_list = row[pvs_key].split('|')
        # todo this removes all square brackets, which may result in reporting PVs that don't match the Google sheet
        #   but there shouldn't be square brackets in PVs anyway
        pvs_list = [re.sub(r"\]|\[", "", i).strip() for i in pvs_list]
        pvs_list.sort()
        list_len = len(pvs_list)
        for pv in pvs_list:
            any_prob_chars = any([char in pv for char in prob_chars])
            if any_prob_chars:
                suspects.append(row[slot_key])
            if row[slot_key] in suspects:
                suspect = True
            if list_len < 2:
                singles.append(row[slot_key])
            temp_dict = {"enum": row[slot_key], "permissible_values": pv}
            lod.append(temp_dict)

for i in lod:
    if i['enum'] in suspects:
        i['suspect'] = True
    else:
        i['suspect'] = False
    if i['enum'] in singles:
        i['single'] = True
        i['suspect'] = True
    else:
        i['single'] = False
    i['enum'] = i['enum'] + "_enum"

with open(pvs_prep_file, 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys, delimiter='\t')
    dict_writer.writeheader()
    dict_writer.writerows(lod)
