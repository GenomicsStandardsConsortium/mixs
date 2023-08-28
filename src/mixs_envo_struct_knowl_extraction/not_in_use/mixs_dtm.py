import pprint
import random
import re
import string

import nltk
import pandas as pd
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from nltk.corpus import words
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

# todo: ONE example task: find slots that are ambiguous about phosphate vs phosphorus
#  another: update slot names so that the tokens that represent the concepts in the notes are more consistent

# todo this current technique includes all slot usages in the mining, even duplicates
#  what are the performance and signal:noise costs/benefits of making input unique first?
#  do we really even want to include slot usage at all?
#  are there slots which don't have a global definition?

# todo would preprocessing decrease the number of associations we need to make in data/curated_slot_notes_by_text_mining.tsv ?

# todo what kind of string preprocessing would be ideal for the dtm?
#  - remove punctuation?
#  - remove numbers?
#  - remove stop words?
#  - remove words that are too short?
#  - remove words that are not in a dictionary?
#  - stemming ?
#  - n-grams ?

# todo how much of a priority do we put on making the dtm output narrow enough that it could be browsed in a spreadsheet?

# todo are we going to do another gen-pop after this?

nltk.download('words')

dtm_input_slot = "title"

schema_sheet = "GSC_MIxS_6_usage_populated_no_blank_cols.tsv"
dest_dir = "generated"
config_dir = 'config'

dtm_to_notes_file = f"{config_dir}/dtm_to_slot_notes.tsv"

output_file = f"{dest_dir}/{schema_sheet}.dtm.tsv"
schema_file = f"{dest_dir}/GSC_MIxS_6.yaml"

raw_dtm_columns_file = f"{dest_dir}/raw_dtm_columns.txt"
notated_schema_file = f"{schema_file}.notated.yaml"

df_raw = pd.read_csv(f"{dest_dir}/{schema_sheet}", sep='\t', dtype=str)

print(df_raw.shape)

df_desc = df_raw[~df_raw[dtm_input_slot].isnull()].copy()

df_desc['unique'] = df_desc['slot'] + "|" + df_desc.index.astype(str)

print(df_desc.shape)

# # dl_slot_desc = df_desc[["slot", "description"]]
# # # remove duplicate rows
# # dl_slot_desc = dl_slot_desc.drop_duplicates()
# # print(dl_slot_desc.shape)
# #
# # dl_slot_desc_unique = dl_slot_desc.copy()
#
# # dl_slot_desc_unique['unique'] = dl_slot_desc_unique['slot'] + "|" + dl_slot_desc_unique.index.astype(str)

# Create an instance of CountVectorizer with stop word removal, custom tokenizer, and modified token pattern
vectorizer = CountVectorizer(
    stop_words='english',
    tokenizer=lambda text: text.split(),
    # token_pattern=r'[a-zA-Z]{2,}',
    # max_features=2500,
    # max_df=0.01
)

# Fit the vectorizer on the Definition column and transform it into a document-term matrix
matrix = vectorizer.fit_transform(df_desc[dtm_input_slot])

# Get the feature names (terms)
feature_names = vectorizer.get_feature_names_out()

# # # Load a dictionary of valid words (e.g., from NLTK's word corpus)
# # valid_words = set(words.words())
# #
# # # Filter the feature names to include only dictionary words
# # dictionary_feature_names = [word for word in feature_names if word in valid_words]
# #
# # # Apply stemming to the dictionary feature names using PorterStemmer
# # stemmer = PorterStemmer()
# # stemmed_feature_names = [stemmer.stem(word) for word in dictionary_feature_names]
#
# # # Filter the document-term matrix to include only the columns corresponding to the dictionary feature names
# # filtered_matrix = matrix[:, [vectorizer.vocabulary_[word] for word in dictionary_feature_names]]

dtm_df = pd.DataFrame(matrix.toarray(), columns=feature_names, index=df_desc['unique'])

row_slot = dtm_df.index.str.split('|', expand=True)

dtm_df.index = row_slot

view = SchemaView(schema_file)
target_schema = view.schema

dtm_to_notes_frame = pd.read_csv(dtm_to_notes_file, sep='\t', dtype=str)

dtm_to_notes_frame.dropna(subset=['note'], inplace=True)

# dump dtm_to_notes_frame to a list of dictionaries
dtm_to_notes_lod = dtm_to_notes_frame.to_dict('records')

for dtm_to_note_dict in dtm_to_notes_lod:
    dtm_val = dtm_to_note_dict['dtm']
    note_val = dtm_to_note_dict['note']
    try:
        filtered_df = dtm_df.loc[dtm_df[dtm_val] > 0]
        matched_rows = filtered_df.shape[0]
        if matched_rows > 0:
            index_values = filtered_df.index.values
            for index_tuple in index_values:
                slot_name = index_tuple[0]
                # print(
                #     f"slot {slot_name} has the string '{dtm_val}' in it's {dtm_input_slot} so gets the note '{note_val}'")

                if target_schema.slots[slot_name].notes and len(target_schema.slots[slot_name].notes) > 0:
                    temp_notes = target_schema.slots[slot_name].notes
                    temp_notes = set(temp_notes)
                    if note_val:
                        temp_notes.add(note_val)
                    temp_notes = list(temp_notes)
                    temp_notes.sort()
                else:
                    temp_notes = [note_val]

                target_schema.slots[slot_name].notes = temp_notes

        else:
            pass
            # print(f"{dtm_val}: no matches")
    except ValueError:
        pass
        # print(f"{dtm_val}: no matches")
    except KeyError:
        pass
        # print(f"{dtm_val}: no matches")

dtm_df.to_csv(output_file, index=True, sep='\t')

raw_dtm_columns = dtm_df.columns.tolist()

with open(raw_dtm_columns_file, "w") as file:
    for string in raw_dtm_columns:
        file.write(string + "\n")

yaml_dumper.dump(target_schema, notated_schema_file)
