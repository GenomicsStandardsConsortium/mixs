# Contributor Analysis and QC Files

This directory contains contributor-generated analysis and quality control files used for validation, testing, and development purposes. These files are not part of the official MIxS schema artifacts.

**Important:** All files in this directory are subject to GSC (Genomics Standards Consortium) approval and review.

## Structure

- `templates/` - Input template files (preserved during cleanup)
- Root level - Generated analysis outputs (can be safely deleted and regenerated)

## Cleaning

Use `make clean-contrib` to remove generated files while preserving templates, or `make clean-contrib && make all-contrib` to regenerate everything.

Generated files include:
- Schema validation and QC reports  
- Normalized and minimized schema variants
- Derived datasets for analysis
- Schemasheets and pattern materialization outputs

## Official vs. Contributor Artifacts

- **Official artifacts**: Located in `project/` and `release/` - authoritative schema files
- **Contributor analysis**: Located here in `contrib/` - analysis files subject to review
