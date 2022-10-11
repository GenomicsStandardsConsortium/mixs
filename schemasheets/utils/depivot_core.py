import pandas as pd

core_input = "../tsv_input/originals_from_gsc_google_sheets/MIxS_6_term_updates_MIxS6_Core-Final_clean.tsv"

preliminary_output = "../tsv_input/original_headers_reshaped/MIxS_6_term_updates_MIxS6_Core-Final_clean_slot_assignments_preliminary.tsv"

keep_cols = ['Structured comment name',
             'migs_ba',
             'migs_eu',
             'migs_org',
             'migs_pl',
             'migs_vi',
             'mimag',
             'mimarks_c',
             'mimarks_s',
             'mims',
             'misag',
             'miuvig',
             ]

core = pd.read_csv(core_input, sep="\t")

core = core[keep_cols]

core_long = pd.melt(core, id_vars=['Structured comment name'])

# print(core_long)
# 
# print(core_long.columns)

core_long.to_csv(preliminary_output, sep="\t", index=False)
