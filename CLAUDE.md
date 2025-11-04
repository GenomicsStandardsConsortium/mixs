# MIxS Project Guidelines

## Build & Test Commands
- `make help` - Show available commands
- `make all` - Generate all project files
- `make test` - Run all tests
- `make test-schema` - Test schema validation
- `make test-python` - Run Python unit tests
- `make test-examples` - Test example data files
- `make lint` - Run LinkML linter on schema
- `make install` - Install dependencies
- `poetry run python -m unittest tests/test_data.py` - Run specific test file

## Code Style & Conventions
- **Schema Format**: LinkML YAML schema in `src/mixs/schema/mixs.yaml`
- **Example Data**: Valid examples in `src/data/examples/valid/`, invalid in `src/data/examples/invalid/`
- **Naming**: Use CamelCase for classes, snake_case for attributes/slots
- **Schema Elements**: Include descriptions for all classes, slots, and enums
- **Documentation**: Add Markdown docs in `src/docs/` for website generation
- **Scripts**: Python utilities in `src/scripts/` follow Python code style (Black formatter)
- **Version Control**: Use descriptive commit messages; branch for new features
- **Pull Requests**: Include clear descriptions and reference issues when applicable

For more project details, see README.md and CONTRIBUTING.md

# MIxS Makefile Documentation

## Makefile Structure Overview

The MIxS project uses two Makefiles:
1. **Main Makefile (`Makefile`)** - Core build system and standard LinkML operations
2. **Project Makefile (`project.Makefile`)** - MIxS-specific custom targets

The two-file approach separates general LinkML targets from project-specific operations, making the system more maintainable.

## Main Makefile (`Makefile`)

### Key Variables

```makefile
RUN = poetry run                      # Command prefix to run Python tools within Poetry environment
SCHEMA_NAME                           # Project name from about.yaml
SOURCE_SCHEMA_PATH                    # Path to main schema file from about.yaml
SRC = src                             # Source directory
DEST = project                        # Output directory for generated artifacts
PYMODEL = src/$(SCHEMA_NAME)/datamodel # Python datamodel directory
DOCDIR = docs                         # Documentation directory
TEMPLATEDIR = src/doc-templates       # Jinja2 templates for documentation
```

### Core Target Groups

#### Setup and Installation
- `make setup` - Initial project setup (installation, generation, Git initialization)
- `make install` - Install dependencies via Poetry
- `make update` - Update LinkML and template dependencies
- `make check-config` - Verify project configuration

#### Schema and Artifact Generation
- `make gen-project` - Generate all project artifacts from schema
- `make gen-examples` - Generate example data
- `make compile-sheets` - Generate schema from Google Sheets (when configured)

#### Testing and Validation
- `make test` - Run all tests (schema, Python, examples)
- `make test-schema` - Validate schema structure
- `make test-python` - Run Python unit tests
- `make test-examples` - Test example data files
- `make lint` - Run LinkML linter on schema

#### Documentation
- `make gendoc` - Generate documentation from schema
- `make testdoc` - Generate documentation and serve locally
- `make serve` - Run local documentation server
- `make deploy` - Deploy documentation to GitHub Pages

#### Utility Targets
- `make clean` - Remove generated files
- `make help` - Display help information

## Project Makefile (`project.Makefile`)

This file contains MIxS-specific targets that extend the core functionality.

### Key Targets

#### Excel Generation and Organization
- `make gen-excel` - Generate Excel templates from schema and organize by class

#### Schema Visualization and Analysis
- `make extensions-dendrogram.pdf` - Generate dendrograms showing extension relationships
- `make soil-vs-water-slot-usage.yaml` - Compare slot usage between extensions
- `make assets/class_summary_results.tsv` - Generate class summary tables

#### Schema Transformation
- `make assets/mixs-patterns-materialized.yaml` - Materialize schema patterns
- `make assets/mixs-schemasheets-concise.tsv` - Create concise schema sheets
- `make assets/mixs-schemasheets-concise-global-slots.tsv` - Extract global slots

#### Metadata Generation
- `make project/class-model-tsvs-organized` - Generate and organize class model TSVs

## Common Workflows

### Initial Setup
```
make install     # Install dependencies
make gen-project # Generate initial project artifacts
```

### Schema Development
```
make lint        # Validate schema syntax
make test-schema # Test schema structure
```

### Building Documentation
```
make gendoc      # Generate documentation
make serve       # View documentation locally
```

### Release Preparation
```
make all         # Generate all artifacts
make test        # Run all tests
```

### Excel Template Generation
```
make gen-excel   # Generate and organize Excel templates
```

## Integration with LinkML Tools

The Makefiles leverage several LinkML command-line tools:
- `gen-doc` - Generate Markdown documentation
- `gen-excel` - Generate Excel templates
- `linkml-lint` - Validate schema syntax
- `linkml2schemasheets-template` - Generate schema sheets templates
- `linkml-convert` - Convert between formats
- `linkml-run-examples` - Test examples against schema

## Custom Scripts

The Makefiles also integrate custom Python scripts:
- `term_list_generator.py` - Generate term lists
- `combinations_list_generator.py` - Generate combination lists
- `enumerations_list_generator.py` - List enumerations
- `organize_files.py` - Organize generated files
- `linkml2class-tsvs` - Generate class TSVs