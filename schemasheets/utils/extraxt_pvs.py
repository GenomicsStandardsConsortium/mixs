import csv
import pprint
import re

slotdef_files = [
    "../tsv_in/MIxS_6_term_updates_MIxS6_Core-Final_clean_slotdefs.tsv",
    "../tsv_in/MIxS_6_term_updates_MIxS6_packages-Final_clean_slotdefs_conflicting_defer_to_soil.tsv",
    "../tsv_in/MIxS_6_term_updates_MIxS6_packages-Final_clean_slotdefs_non_conflicting_shared.tsv"
]
# assuming the same keys across slotdef_files
slot_key = 'SAFE Structured comment name'
pvs_key = 'Value syntax'

keys = ['enum', 'permissible_values', 'suspect', 'single', 'source']
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

raw_enums_file = "../tsv_in/generated/mixs_potential_enums.tsv"

outer_lod = []
for sdf in slotdef_files:
    base = sdf.split("/")[-1].split(".")[0]
    print(base)
    inner_lod = []
    suspects = []
    singles = []
    with open(sdf) as tsvfile:
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
                inner_lod.append(temp_dict)

        for i in inner_lod:
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
            i['source'] = base

        pprint.pprint(inner_lod)
        outer_lod.extend(inner_lod)

with open(raw_enums_file, 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys, delimiter='\t')
    dict_writer.writeheader()
    dict_writer.writerows(outer_lod)
