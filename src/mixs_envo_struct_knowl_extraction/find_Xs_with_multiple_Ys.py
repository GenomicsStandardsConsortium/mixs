import click
import pandas as pd

pd.set_option('display.max_columns', None)


@click.command()
@click.option('--input-file', '-i', default="generated/mixs_v6.xlsx.harmonized.tsv",
              help='Path to the input harmonized file')  # OR generated/mixs_v6.xlsx.repaired.tsv
@click.option('--x-column', '-x', default='Structured comment name', help='Column name for X')
@click.option('--y-column', '-y', default='Item', help='Column name for Y')
@click.option('--output-file', '-o', default="generated/mixs_v6.xlsx.harmonized.conflicts.tsv",
              help='Path to the output file')
def main(input_file, x_column, y_column, output_file):
    harmonized_frame = pd.read_csv(input_file, sep='\t')

    Xs = harmonized_frame[x_column].unique()

    dataframes = []

    for x in Xs:
        Ys = harmonized_frame[harmonized_frame[x_column] == x][y_column].unique()
        if len(Ys) > 1:
            Y_details = harmonized_frame.loc[harmonized_frame[x_column] == x, ['class', x_column, y_column]]
            Y_freqs = Y_details[y_column].value_counts(normalize=True, dropna=False).reset_index()
            Y_freqs.columns = [y_column, 'Frequency']
            merged_df = Y_details.merge(Y_freqs, on=y_column)
            dataframes.append(merged_df)

    if len(dataframes) > 0:
        combined_df = pd.concat(dataframes, ignore_index=True)

        combined_df = combined_df.sort_values(by=[x_column, y_column, 'class'], ascending=[True, True, True])

        combined_df.to_csv(output_file, sep='\t', index=False)


if __name__ == '__main__':
    main()
