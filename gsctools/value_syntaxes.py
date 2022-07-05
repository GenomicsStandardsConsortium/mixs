import math
import pprint
import re

import pandas as pd

# use gsc versions
# why?
core_file = "downloads/mixs6_core.tsv"
packages_file = "downloads/mixs6.tsv"

core_frame = pd.read_csv(core_file, sep="\t")

packages_frame = pd.read_csv(packages_file, sep="\t")

mixs_frame = pd.concat([core_frame, packages_frame])

temp = list(mixs_frame.columns)
temp.sort()

id_to_vs = mixs_frame[["MIXS ID", "Value syntax"]].copy()

id_to_vs.drop_duplicates(inplace=True)

vs_valcounts = (
    id_to_vs["Value syntax"]
    .value_counts()
    .rename_axis("Value syntax")
    .reset_index(name="term count")
)

id_to_vs_dol = id_to_vs.to_dict(orient="records")

usage_list = []
vs_extractor = re.compile(r"({[^{}]*})")
for current_id_vs in id_to_vs_dol:
    term_id = current_id_vs["MIXS ID"]
    val_syn = current_id_vs["Value syntax"]
    # todo won't get {{text}|{float} {unit}};{float} {unit}
    if val_syn is not None and val_syn != "":
        extracted = vs_extractor.findall(str(val_syn))
        for match in extracted:
            usage_list.append({"Value syntax": val_syn, "token": match})
usage_frame = pd.DataFrame(usage_list)

vs_valcounts.to_csv("generated/vs_usage.tsv", sep="\t", index=False)

token_valcounts = (
    usage_frame["token"]
    .value_counts()
    .rename_axis("token")
    .reset_index(name="Value syntax count")
)

token_valcounts.to_csv("generated/vs_token_usage.tsv", sep="\t", index=False)

all_vses = set(id_to_vs["Value syntax"])
tokenized_vses = set(usage_frame["Value syntax"])

untokenized = list(all_vses - tokenized_vses)
# untokenized = [str(i) for i in untokenized if i is not math.nan]
untokenized = [str(i) for i in untokenized if str(i) != "nan"]
untokenized.sort()

with open("generated/vs_untokenized.txt", "w") as fp:
    for current_ut in untokenized:
        fp.write("%s\n" % current_ut)