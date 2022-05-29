import pprint
import re

import pandas as pd
from linkml_runtime import SchemaView

from sklearn.feature_extraction.text import TfidfVectorizer

mixs_root_file = "../model/schema/mixs.yaml"
#
# just_lists = ["[clean catch|catheter]",
#               "[closed|open]",
#               "[complex life cycle | simple life cycle]",
#               "[conductive|radiant]",
#               "[exterior|interior]",
#               "[facultative|obligate]",
#               "[gas burning|wood burning]",
#               "[independent sequence (UViG)|provirus (UpViG)]",
#               "[none|manually edited]",
#               "[pcr based|mda based]",
#               "[plane|glider]",
#               "[reads| contigs]",
#               "[typically occupied|typically unoccupied]",
#               "[urban|rural]",
#               "[wood frame|concrete]"]

mixs_view = SchemaView(mixs_root_file)

# mixs_slots = mixs_view.all_slots()
#
# string_sers = []
#
# slots_to_just_lists = []
#
# tokens = []
#
# for k, v in mixs_slots.items():
#     if v.string_serialization:
#         # range always string, except for "has raw value"
#         string_sers.append({"slot": k, "range": v.range, "string_ser": v.string_serialization})
#         # if v.string_serialization in just_lists:
#         #     print(f"{k}\t{v.string_serialization}")
#         tokens.append(re.findall('\{.*?\}', v.string_serialization))
#
# string_ser_frame = pd.DataFrame(string_sers)
#
# df = string_ser_frame['string_ser'].value_counts().rename_axis('string_ser').reset_index(name='counts')
#
# df.to_csv("string_ser_frame.tsv", sep="\t", index=False)
#
# flat_list = [item for sublist in tokens for item in sublist]
#
# fl_series = pd.Series(flat_list)
#
# df = fl_series.value_counts().rename_axis('string_ser').reset_index(name='counts')
#
# df.to_csv("token_frame.tsv", sep="\t", index=False)
#
# concat = ''.join(df['string_ser'])
#
# all_freq = {}
#
# for i in concat:
#     if i in all_freq:
#         all_freq[i] += 1
#     else:
#         all_freq[i] = 1
#
# df = pd.DataFrame(list(all_freq.items()), columns=['char', 'count'])
#
# df.to_csv("token_char_counts.tsv", sep="\t", index=False)

# all_classes = mixs_view.all_classes()
#
# all_class_names = list(all_classes.keys())
# all_class_names.sort()
#
# lod = []
# for current_class_name in all_class_names:
#     print(current_class_name)
#     # current_class = all_classes[current_class_name]
#     # current_su = current_class.slot_usage
#     # current_su_names = list(current_su.keys())
#     # current_su_names.sort()
#     # for current_slot_name in current_su_names:
#     #     print(f"  {current_slot_name}")
#     current_cis = mixs_view.class_induced_slots(current_class_name)
#     current_cis_names = [i.name for i in current_cis]
#     current_cis_dict = dict(zip(current_cis_names, current_cis))
#     current_cis_names.sort()
#     for current_cis_name in current_cis_names:
#         current_slot = current_cis_dict[current_cis_name]
#         current_struct_pat = current_slot.string_serialization
#         if current_struct_pat:
#             lod.append(
#                 {"class": current_class_name, "slot": current_cis_name, "structured_pattern": current_struct_pat})
#             # print(f"{current_class_name} {current_cis_name} {current_struct_pat}")
#
# df = pd.DataFrame(lod)
# df.to_csv("cssp.tsv", sep="\t", index=False)
#
# print(df)

df = pd.read_csv("cssp.tsv", sep="\t")
# print(df)

ignore_class = df[['slot', 'structured_pattern']].copy()
ignore_class.drop_duplicates(inplace=True)
ic_vc = ignore_class['slot'].value_counts()
ic_vc_max = ic_vc.max()
print(ic_vc_max)

ignore_class.to_csv("icsp.tsv", sep="\t", index=False)

ignore_class.sort_values(by=['structured_pattern', 'slot'], ascending=[True, True], inplace=True)
pattern_wise = ignore_class.groupby('structured_pattern', as_index=False).agg({'slot': '|'.join})
pattern_wise['slot_count'] = pattern_wise['slot'].str.count("\\|") + 1

# pattern_wise['potential_list'] = pattern_wise['structured_pattern'].str.count("\\[")
# pattern_wise['potential_pattern'] = pattern_wise['structured_pattern'].str.count("\\{")


pattern_wise['square_count'] = pattern_wise['structured_pattern'].str.count("\\[")
pattern_wise['curly_count'] = pattern_wise['structured_pattern'].str.count("\\{")
pattern_wise['pipe_count'] = pattern_wise['structured_pattern'].str.count("\\|")

pattern_wise['initial_square'] = pattern_wise['structured_pattern'].str[0] == '['
pattern_wise['initial_curly'] = pattern_wise['structured_pattern'].str[0] == '{'

pattern_wise['enum_candidate'] = False

pattern_wise.loc[pattern_wise['initial_square'] & pattern_wise['curly_count'].eq(0), "enum_candidate"] = True

pattern_wise['oddball'] = False

pattern_wise.loc[(~pattern_wise['initial_square']) & (~pattern_wise['initial_curly']), "oddball"] = True

pattern_wise.to_csv("pattern_wise.tsv", sep="\t", index=False)

temp = pattern_wise.loc[(~pattern_wise['enum_candidate']) & (~pattern_wise['oddball'])]
for_tm = pd.concat([temp["structured_pattern"], temp["structured_pattern"]], axis=1)
# or might want to make an index?
for_tm.columns = ['structured_pattern', 'text']
for_tm['text'] = for_tm['text'].str.replace(r'\W', ' ')
for_tm['text'] = for_tm['text'].str.replace(r' +', ' ')

# some of these don't work because of the preprocessing
vectorizer = TfidfVectorizer(vocabulary=['af cutoff',
                                         'ani cutoff',
                                         'boolean',
                                         'bp',
                                         'clustering method',
                                         'database',
                                         'day',
                                         'dna',
                                         'doi',
                                         'duration',
                                         'float',
                                         'has numeric value',
                                         'has unit',
                                         'integer',
                                         'interval',
                                         'measurement value',
                                         'ncbi taxid',
                                         'ncbi:txid',
                                         'parameters',
                                         'percentage',
                                         'period',
                                         'pid',
                                         'pmid',
                                         'rank name',
                                         'reference',
                                         'rn/start_time/end_time/duration',
                                         'software',
                                         'term',
                                         'term id',
                                         'term label',
                                         'termid',
                                         'termlabel',
                                         'text',
                                         'timestamp',
                                         'unit',
                                         'url',
                                         'version'], ngram_range=(1, 2))
doc_vec = vectorizer.fit_transform(for_tm['text'])
doc_df = pd.DataFrame(doc_vec.toarray())
doc_df.columns = vectorizer.get_feature_names()
doc_df.index = for_tm['structured_pattern']

doc_df.to_csv("doc_df.tsv", sep="\t", index=True)

for_char_count = list(temp["structured_pattern"])
for_char_count = ''.join(for_char_count)

# inefficient
char_count = {e: for_char_count.count(e) for e in set(for_char_count)}
char_keys = list(char_count.keys())
char_keys.sort()
punct_dict = {k: v for k, v in char_count.items() if not re.match('[a-zA-Z]', k)}
punct_df = pd.DataFrame(punct_dict.items(), columns=['char', 'count'])
punct_df.sort_values(by=['count', 'char'], ascending=[False, True], inplace=True)

punct_df.to_csv("punct_df.tsv", sep="\t", index=False)

# for i in char_keys:
#     if not re.match('[a-zA-Z]', i):
#         print(f"{i}: {char_count[i]}")

# a tvc_max of 1 means that no slots have a difference structured pattern depending on which class they're used in
# might just be  able to interrogate slots in terms.yaml

# cn0 = all_class_names[0]
#
# c0 = all_classes[cn0]
#
# representative_fields = list(c0.__dict__.keys())
# representative_fields.sort()
# pprint.pprint(representative_fields)
#
# # ['abstract',
# #  'aliases',
# #  'all_of',
# #  'alt_descriptions',
# #  'annotations',
# #  'any_of',
# #  'apply_to',
# #  'attributes',
# #  'broad_mappings',
# #  'children_are_mutually_disjoint',
# #  'class_uri',
# #  'classification_rules',
# #  'close_mappings',
# #  'comments',
# #  'conforms_to',
# #  'created_by',
# #  'created_on',
# #  'defining_slots',
# #  'definition_uri',
# #  'deprecated',
# #  'deprecated_element_has_exact_replacement',
# #  'deprecated_element_has_possible_replacement',
# #  'description',
# #  'disjoint_with',
# #  'exact_mappings',
# #  'exactly_one_of',
# #  'examples',
# #  'extensions',
# #  'from_schema',
# #  'id_prefixes',
# #  'imported_from',
# #  'in_language',
# #  'in_subset',
# #  'is_a',
# #  'last_updated_on',
# #  'local_names',
# #  'mappings',
# #  'mixin',
# #  'mixins',
# #  'modified_by',
# #  'name',
# #  'narrow_mappings',
# #  'none_of',
# #  'notes',
# #  'rank',
# #  'related_mappings',
# #  'represents_relationship',
# #  'rules',
# #  'see_also',
# #  'slot_conditions',
# #  'slot_names_unique',
# #  'slot_usage',
# #  'slots',
# #  'source',
# #  'status',
# #  'string_serialization',
# #  'structured_aliases',
# #  'subclass_of',
# #  'title',
# #  'todos',
# #  'tree_root',
# #  'union_of',
# #  'unique_keys',
# #  'values_from']
#
