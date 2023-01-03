import itertools
import pandas as pd


def class_defs(path_to_classdefs):
    classdefs_df = pd.read_csv(path_to_classdefs, delimiter="\t")
    classdefs_list = list(classdefs_df["SAFE checklist"])
    for c in classdefs_list:
        if c == ">":
            idx = classdefs_list.index(c)
            return classdefs_list[idx + 1 :]


def slot_defs(path_to_slotdefs):
    slotdefs_df = pd.read_csv(path_to_slotdefs, delimiter="\t")
    slotdefs_list = list(slotdefs_df["SAFE Structured comment name"])
    for c in slotdefs_list:
        if c == ">":
            idx = slotdefs_list.index(c)
            return slotdefs_list[idx + 1 :]


def slot_usage_defs(path_to_slot_usage_defs):
    slot_usage_defs_df = pd.read_csv(path_to_slot_usage_defs, delimiter="\t")
    slot_usage_defs_df = slot_usage_defs_df[
        slot_usage_defs_df[slot_usage_defs_df["class"] == ">"].index[0] + 1 :
    ]
    slot_usage_defs_df = slot_usage_defs_df[["class", "Structured comment name"]]
    temp = (
        slot_usage_defs_df.groupby(["class"])
        .apply(lambda x: x["Structured comment name"].tolist())
        .to_dict()
    )
    return [temp.keys(), list(set(list(itertools.chain.from_iterable(temp.values()))))]


if __name__ == "__main__":
    class_names = class_defs(
        "/Users/sujaypatil/Desktop/mixs/schemasheets/tsv_in/MIxS_6_term_updates_classdefs.tsv"
    )
    slot_names = slot_defs(
        "/Users/sujaypatil/Desktop/mixs/schemasheets/tsv_in/MIxS_6_term_updates_partial_slotdefs.tsv"
    )
    class_slot_assignments = slot_usage_defs(
        "/Users/sujaypatil/Desktop/mixs/schemasheets/tsv_in/MIxS_6_term_updates_slot_assignments.tsv"
    )

    list1 = class_names
    list2 = slot_names
    list3 = list(class_slot_assignments[0])
    list4 = class_slot_assignments[1]

    print(
        "Difference between MIxS_6_term_updates_classdefs.tsv and MIxS_6_term_updates_slot_assignments.tsv"
    )
    list1_list3_diff = [x for x in list1 if x not in list3]
    print(list1_list3_diff)

    print(
        "Difference between MIxS_6_term_updates_slot_assignments.tsv and MIxS_6_term_updates_classdefs.tsv"
    )
    list3_list1_diff = [x for x in list3 if x not in list1]
    print(list3_list1_diff)

    print(
        "Difference between MIxS_6_term_updates_partial_slotdefs.tsv and MIxS_6_term_updates_slot_assignments.tsv"
    )
    list2_list4_diff = [x for x in list2 if x not in list4]
    print(list2_list4_diff)

    print(
        "Difference between MIxS_6_term_updates_partial_slotdefs.tsv and MIxS_6_term_updates_slot_assignments.tsv"
    )
    list4_list2_diff = [x for x in list4 if x not in list2]
    print(list4_list2_diff)
