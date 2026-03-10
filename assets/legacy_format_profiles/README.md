# Legacy Format Profiles

This directory contains configuration files that describe how to parse MIxS schemas
from historical Excel formats. These profiles externalize the version-specific parsing
logic so it can be maintained without code changes.

## Supported Formats

The `mixs-legacy-diff` tool supports comparing schemas from v4 onward:

- **v4 (2014)**: Excel .xls files with standardized columns (`excel_v4.yaml`)
- **v5 (2018)**: Excel .xlsx files with extended checklist columns (`excel_v5.yaml`)
- **v6+ (2022+)**: LinkML YAML (no profile needed — uses SchemaView directly)

Older formats (pre-2009 Word documents, 2009–2011 Excel variants) are cataloged in
`assets/version_history/version_registry.yaml` but are not supported by the diff tool.
See GitHub issues for re-implementation plans.

## Profile Structure

Each YAML profile contains:

```yaml
description: "MIxS v5 Excel format (2018)"

version_patterns:
  - "mixs5"
  - "*v5*"
  - "*20180621*"

sheet_names:
  main_terms: ["MIxS"]
  packages: ["environmental_packages"]

column_mappings:
  name: ["Structured comment name"]
  definition: ["Definition"]

checklist_columns:
  migs_eu: "migs_eu"
  migs_ba: "migs_ba"

normalize_term_names: false
```

## Adding a New Profile

1. Create a new YAML file named after the version (e.g., `excel_v3.yaml`)
2. Examine sample files to determine sheet names and column headers
3. Define the column mappings based on what you find
4. Test with `mixs-legacy-diff` to verify terms are extracted correctly

## Usage

The `mixs-legacy-diff` tool automatically selects a profile based on:
1. Matching `version_patterns` against the filename
2. Fallback to `excel_default.yaml`

You can also use `--profile-dir` to specify a custom profiles directory.
