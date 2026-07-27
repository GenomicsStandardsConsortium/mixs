# MIxS Scripts Documentation

This directory contains utility scripts for processing and analyzing MIxS schema data. These scripts are called by various Makefile targets and generate documentation, analysis files, and organizational outputs.

## Scripts Overview

### Documentation Generators

#### `combinations_list_generator.py`
Generates a Markdown document based on the classes defined in a YAML schema using the `linkml` framework. Used in the `gendoc` Makefile target. 

**Features:**
- Creates combinations documentation from schema classes
- Filters classes with mixins and superclasses
- Outputs structured Markdown tables
- **Click CLI** with `--output-file` and `--schema-file` options

#### `enumerations_list_generator.py` 
Generates a Markdown document that details all the enumerations from a LinkML schema. Used in the `gendoc` Makefile target.

**Features:**
- Documents all schema enumerations
- Creates Markdown tables of permissible values
- Uses `DocGenerator` for enhanced linking
- **Click CLI** with `--output-file` and `--schema-file` options

#### `term_list_generator.py`
Generates a Markdown file documenting all terms in a MIxS schema using `DocGenerator` from linkml. Used in the `gendoc` Makefile target.

**Features:**
- Creates comprehensive term documentation
- Filters out MixsCompliantData domain terms
- Generates clickable links using DocGenerator
- **Click CLI** with `--output-file` and `--schema-file` options

### Analysis Tools

#### `extension_distances.py` ⭐ Click CLI
Generates a dendrogram visualizing similarity between different classes (extensions) using hierarchical clustering. Has `tool.poetry.scripts` alias: `extension-distances`. Called by `contrib/extensions-dendrogram.pdf` Makefile target.

**Features:**
- Hierarchical clustering of schema extensions
- PDF dendrogram output using matplotlib
- Euclidean distance calculations
- **Click CLI** with `--schema` and `--output` options

#### `extension_slot_differences.py` ⭐ Click CLI  
Compares slot definitions between two specified extensions using set operations. Has `tool.poetry.scripts` alias: `extension-differences`. Used by `contrib/soil-vs-water-slot-usage.yaml` Makefile target.

**Features:**
- Set arithmetic comparison between extensions
- YAML output of unique slots per extension
- **Click CLI** with `--schema`, `--ext1`, `--ext2` options
- Note: Script name has typo (_diffrences_)

#### `isolate_slots.py` ⭐ Click CLI
Extracts global slots from MIxS schemasheets by filtering for slots without class assignments. Used by `contrib/mixs-schemasheets-concise-global-slots.tsv` Makefile target.

**Features:** 
- Filters schemasheets for global slots
- Removes MixsCompliantData domain entries
- **Click CLI** with `--source-file`, `--output-file`, `--table-name` options
- Optional database integration (commented out)

#### `required_supersedes_recommended.py`
Processes schema to generate required and recommended slot usage information. Used by `contrib/required_and_recommended_slot_usages.tsv` Makefile target.

### File Organization

#### `organize_files.py`
Organizes Excel files based on MIxS schema categorization, sorting into directories for Checklists and Extensions. Used by `gen-excel` Makefile target.

**Features:**
- Schema-based file organization 
- Creates checklist and extension directories
- **Click CLI** with schema, source, and destination path options
- Class-based design with logging

#### `linkml2class_tsvs.py`
Processes schema classes and generates TSV files. Has `tool.poetry.scripts` alias: `linkml2class-tsvs`. Used by `project/class-model-tsvs-organized` Makefile target.

## CLI Framework Usage

**All scripts now use Click CLI** for consistent command-line interface handling with standardized options like `--output-file` and `--schema-file`.

## Poetry Script Aliases

Several scripts have Poetry aliases defined in `pyproject.toml`:
- `extension-distances` → `extension_distances.py`
- `extension-differences` → `extension_slot_differences.py`
- `linkml2class-tsvs` → `linkml2class_tsvs.py`

## Integration with Build System

These scripts are integral to the MIxS build pipeline:
- **Documentation**: Generate term lists, combinations, and enumerations for site
- **Analysis**: Create QC files and validation reports in `contrib/`
- **Organization**: Structure Excel templates and TSV outputs
- **Validation**: Support testing and quality control processes