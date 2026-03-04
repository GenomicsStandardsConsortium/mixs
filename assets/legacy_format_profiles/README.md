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

## Word Document Extraction (`word_extracted_terms.json`)

Pre-extracted terms from early MIGS Word documents (v1.1, v1.2).

### Why Pre-extraction?

The Word documents use a complex table structure that cannot be reliably parsed with rule-based code:

1. **No standard headers** - Section names (ORGANISM, ENVIRONMENT) appear as row content, not column headers
2. **Merged cells** - The table uses merged cells for visual grouping
3. **Embedded definitions** - Term names include parenthetical clarifications that need interpretation
4. **Abbreviated text** - Terms like "Reference for (" are truncated and need context to understand

### Extraction Method

Terms were extracted through interactive analysis using Claude Code:

1. The `python-docx` library read raw table data from each Word document
2. Claude Code analyzed the table structure to identify:
   - Section boundaries (uppercase headers like ORGANISM, ENVIRONMENT)
   - Term rows (lowercase text with M/X/- requirement columns)
   - Checklist columns (EU, BA, PL, VI, OR, ME)
3. For each term row, Claude Code interpreted:
   - The normalized term name (e.g., "Geographic location (latitude..." → `geographic_location`)
   - The human-readable item name
   - Any definition text extracted from parenthetical notes
   - Checklist requirements from the M/X/- columns
4. Results were saved to `word_extracted_terms.json` for use by the Word reader

### Re-extraction

If the Word documents need to be re-processed:

1. Use `python-docx` to dump the table structure:
   ```python
   from docx import Document
   doc = Document('path/to/file.docx')
   for i, row in enumerate(doc.tables[0].rows):
       cells = [c.text.strip() for c in row.cells]
       print(f'Row {i}: {cells}')
   ```
2. Manually or interactively analyze the output to identify terms
3. Update `word_extracted_terms.json` with the new extraction

No external API keys or services are required - the extraction was done interactively during development.
