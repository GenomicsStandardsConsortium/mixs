import pandas as pd

# from sqlalchemy import create_engine

# for optional insertion into a NMDC/BBOP Biosample Postgres database
# engine = create_engine(
#     'postgresql://biosample_guest:Arose-Urology0-Quaintly@localhost:15432/ncbi_biosamples_feb26')

source_schemasheets_file = "assets/mixs-schemasheets-concise.tsv"
destination_file = "assets/mixs-schemasheets-concise-global-slots.tsv"
destination_table_name = 'mixs_global_slots'

df = pd.read_csv(source_schemasheets_file, sep='\t')

# Remove rows where the first column value starts with ">"
df = df[~df.iloc[:, 0].astype(str).str.startswith(">")]

# Keep rows with a value for "slot" but no value for "class"
df = df[df['slot'].notnull() & df['class'].isnull()]

# Remove rows where "domain" equals "MixsCompliantData"
df = df[df['domain'] != 'MixsCompliantData']

# Remove columns that are all null
df = df.dropna(axis=1, how='all')

df.to_csv(destination_file, sep='\t', index=False)

# # Create a table with the same columns as the DataFrame
# df.to_sql(destination_table_name, engine, if_exists='replace', index=False)
#
# # Commit the transaction
# engine.dispose()
