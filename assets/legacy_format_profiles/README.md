# Legacy Format Profiles

This directory contains configuration files that describe how to parse MIxS schemas
from different historical formats and versions. These profiles externalize the
version-specific parsing logic so it can be maintained without code changes.

## Purpose

MIxS schemas have been distributed in different formats over the years:
- **Pre-2009**: Word documents (.docx) and XML Schema (.xsd)
- **2009-2011**: Excel spreadsheets with varying column structures
- **v4 (2014)**: Excel .xls files with standardized columns
- **v5 (2018)**: Excel .xlsx files with extended checklist columns
- **v6+ (2020+)**: LinkML YAML (no profile needed - uses SchemaView directly)

Each Excel version has slightly different:
- Sheet names (e.g., "MIxS" vs "Recovered_Sheet1")
- Column headers (e.g., "Item" vs "Structured comment name")
- Checklist column names (e.g., "EU" vs "migs_eu")

## Profile Structure

Each YAML profile contains:

```yaml
# Human-readable description
description: "MIxS v5 Excel format (2018)"

# Version pattern matching (regex or glob)
version_patterns:
  - "mixs5"
  - "*v5*"
  - "*20180621*"

# Sheet names to look for (in priority order)
sheet_names:
  main_terms: ["MIxS"]
  packages: ["environmental_packages"]

# Column header mappings: normalized_field -> [possible_headers]
column_mappings:
  name: ["Structured comment name"]
  definition: ["Definition"]
  # ...

# Checklist column mappings: header -> normalized_checklist_name
checklist_columns:
  migs_eu: "migs_eu"
  migs_ba: "migs_ba"
  # ...

# Whether to normalize term names (convert spaces to underscores, lowercase)
normalize_term_names: false
```

## Adding a New Profile

1. Create a new YAML file named after the version (e.g., `excel_v3.yaml`)
2. Examine sample files to determine sheet names and column headers
3. Define the column mappings based on what you find
4. Test with `mixs-legacy-diff` to verify terms are extracted correctly

## Usage

The `mixs-legacy-diff` tool automatically selects a profile based on:
1. Explicit `--profile` argument
2. Matching `version_patterns` against the filename
3. Fallback to a default profile

You can also use `--profile-dir` to specify a custom profiles directory.
