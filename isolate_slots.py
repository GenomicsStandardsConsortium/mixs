import pandas as pd

# Read the TSV file
df = pd.read_csv('mixs-schemasheets-concise.tsv', sep='\t')

# Keep the first row
header = df.iloc[0]
df = df[1:]

# Remove rows where the first column value starts with ">"
df = df[~df.iloc[:, 0].astype(str).str.startswith(">")]

# Keep rows with a value for "slot" but no value for "class"
df = df[df['slot'].notnull() & df['class'].isnull()]

# Remove columns that are all null
df = df.dropna(axis=1, how='all')

# Reset the index
df.reset_index(drop=True, inplace=True)

# Write the cleaned DataFrame to a new TSV file
df.to_csv('mixs-schemasheets-concise-global-slots.tsv', sep='\t', index=False)
