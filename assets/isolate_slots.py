import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://postgres:wildcard-purebred-recognize-thumb-quilt@localhost:15432/ncbi_biosamples_feb26')
destination_table_name = 'mixs_global_slots'

df = pd.read_csv('mixs-schemasheets-concise.tsv', sep='\t')

# # Keep the first row
df = df[1:]

# Remove rows where the first column value starts with ">"
df = df[~df.iloc[:, 0].astype(str).str.startswith(">")]

# Keep rows with a value for "slot" but no value for "class"
df = df[df['slot'].notnull() & df['class'].isnull()]

# Remove rows where "domain" equals "MixsCompliantData"
df = df[df['domain'] != 'MixsCompliantData']

# Remove columns that are all null
df = df.dropna(axis=1, how='all')

df.to_csv('mixs-schemasheets-concise-global-slots.tsv', sep='\t', index=False)

# Create a table with the same columns as the DataFrame
df.to_sql(destination_table_name, engine, if_exists='replace', index=False)

# Commit the transaction
engine.dispose()
