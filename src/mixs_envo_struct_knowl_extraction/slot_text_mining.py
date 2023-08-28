import click
import pandas as pd
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from sklearn.feature_extraction.text import CountVectorizer


@click.command()
@click.option('--dtm-input-slot', default='title', help='Input slot for document-term matrix')
@click.option('--input-dtm-notes-mapping', required=True)
@click.option('--input-schema-file', required=True)
@click.option('--input-usage-report', help='Schema sheet file', required=True)
@click.option('--dtm-output', required=True)
@click.option('--output-schema-file', required=True)
@click.option('--input-col-vals-file', required=True)
def cli(dtm_input_slot, input_usage_report, input_dtm_notes_mapping, input_col_vals_file, dtm_output,
        input_schema_file, output_schema_file):
    """
    Script to create a document-term matrix from a usage report, and add notes to the corresponding slots in a schema.

    Args:
        dtm_input_slot (str): The name of the slot in the usage report to use for the document-term matrix.
        input_usage_report (str): The path to the usage report file.
        input_dtm_notes_mapping (str): The path to the file mapping DTM values to notes.
        input_col_vals_file (str): The path to the file to write the raw DTM column names to.
        dtm_output (str): The path to the file to write the DTM to.
        input_schema_file (str): The path to the schema file.
        output_schema_file (str): The path to the file to write the updated schema to.
    """

    df_raw = pd.read_csv(f"{input_usage_report}", sep='\t', dtype=str)
    print(f"Dimensions of {input_usage_report} before deduplication: {df_raw.shape}")

    df_desc = df_raw[~df_raw[dtm_input_slot].isnull()].copy()
    df_desc['unique'] = df_desc['slot'] + "|" + df_desc.index.astype(str)
    print(f"Dimensions of {input_usage_report} after deduplication: {df_desc.shape}")

    # todo: UserWarning: The parameter 'token_pattern' will not be used since 'tokenizer' is not None'

    vectorizer = CountVectorizer(
        stop_words='english',
        tokenizer=lambda text: text.split(),
    )
    matrix = vectorizer.fit_transform(df_desc[dtm_input_slot])
    feature_names = vectorizer.get_feature_names_out()
    dtm_df = pd.DataFrame(matrix.toarray(), columns=feature_names, index=df_desc['unique'])
    row_slot = dtm_df.index.str.split('|', expand=True)
    dtm_df.index = row_slot

    view = SchemaView(input_schema_file)
    target_schema = view.schema

    dtm_to_notes_frame = pd.read_csv(input_dtm_notes_mapping, sep='\t', dtype=str)
    dtm_to_notes_frame.dropna(subset=['slot_note_to_insert'], inplace=True)
    dtm_to_notes_lod = dtm_to_notes_frame.to_dict('records')

    for dtm_to_note_dict in dtm_to_notes_lod:
        dtm_val = dtm_to_note_dict['token_from_text_mining']
        note_val = dtm_to_note_dict['slot_note_to_insert']
        try:
            filtered_df = dtm_df.loc[dtm_df[dtm_val] > 0]
            matched_rows = filtered_df.shape[0]
            if matched_rows > 0:
                # print(f"Found {matched_rows} rows for {dtm_val} with note {note_val}")
                index_values = filtered_df.index.values
                for index_tuple in index_values:
                    slot_name = index_tuple[0]
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
        except ValueError as e:
            print(e)
            pass

        except KeyError as e:
            # print(f"token {e} not found in input")
            pass

    dtm_df.to_csv(dtm_output, index=True, sep='\t')

    raw_dtm_columns = dtm_df.columns.tolist()

    with open(input_col_vals_file, "w") as file:
        for string in raw_dtm_columns:
            file.write(string + "\n")

    yaml_dumper.dump(target_schema, output_schema_file)


if __name__ == '__main__':
    cli()
