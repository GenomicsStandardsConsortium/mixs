import click
import pandas as pd

# from sqlalchemy import create_engine

# for optional insertion into a NMDC/BBOP Biosample Postgres database
# engine = create_engine(
#     'postgresql://biosample_guest:Arose-Urology0-Quaintly@localhost:15432/ncbi_biosamples_feb26')

@click.command()
@click.option('--source-file', '-s', 
              default='contrib/mixs-schemasheets-concise.tsv',
              help='Source schemasheets TSV file')
@click.option('--output-file', '-o',
              default='contrib/mixs-schemasheets-concise-global-slots.tsv', 
              help='Output file for global slots TSV')
@click.option('--table-name', '-t',
              default='mixs_global_slots',
              help='Table name for optional database insertion')
def isolate_global_slots(source_file, output_file, table_name):
    """Extract global slots from MIxS schemasheets by filtering for slots without class assignments."""
    
    df = pd.read_csv(source_file, sep='\t')

    # Remove rows where the first column value starts with ">"
    df = df[~df.iloc[:, 0].astype(str).str.startswith(">")]

    # Keep rows with a value for "slot" but no value for "class"
    df = df[df['slot'].notnull() & df['class'].isnull()]

    # Remove rows where "domain" equals "MixsCompliantData"
    df = df[df['domain'] != 'MixsCompliantData']

    # Remove columns that are all null
    df = df.dropna(axis=1, how='all')

    df.to_csv(output_file, sep='\t', index=False)
    click.echo(f"Global slots extracted to: {output_file}")

    # # Create a table with the same columns as the DataFrame
    # df.to_sql(table_name, engine, if_exists='replace', index=False)
    #
    # # Commit the transaction
    # engine.dispose()

if __name__ == '__main__':
    isolate_global_slots()
