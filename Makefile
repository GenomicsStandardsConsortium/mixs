# RELEASE SOP: make install clean all all-assets test

MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

RUN = poetry run

SCHEMA_NAME = mixs
SOURCE_SCHEMA_PATH = src/mixs/schema/mixs.yaml
SOURCE_SCHEMA_DIR = $(dir $(SOURCE_SCHEMA_PATH))
SRC = src
DEST = project
PYMODEL = $(SRC)/$(SCHEMA_NAME)/datamodel
DOCDIR = docs
TEMPLATEDIR = $(SRC)/doc-templates
TERM_LIST_FILE = $(DOCDIR)/term_list.md
COMBINATIONS_FILE = $(DOCDIR)/combinations.md
ENUMERATIONS_FILE = $(DOCDIR)/enumerations.md
EXAMPLEDIR = examples

SHEET_MODULE_PATH = $(SOURCE_SCHEMA_DIR)/$(SHEET_MODULE).yaml
EXCEL_TEMPLATES_DIR = mixs-templates

GEN_PARGS = --exclude excel --exclude graphql --exclude markdown --exclude prefixmap  --exclude protobuf  --exclude shacl  --exclude shex

GEN_DARGS =

# note: "help" MUST be the first target in the file,
# when the user types "make" they should get help info
help: status
	@echo ""
	@echo "make help -- show this help"
	@echo "make install -- install dependencies"
	@echo "make linkml-lint -- perform linkml linting"
	@echo "make yaml-lint -- perform yaml linting"
	@echo "make yamlfmt-beta -- experimental yaml formatting"
	@echo "make site -- makes site locally"
	@echo "make test -- runs tests"
	@echo "make testdoc -- builds docs and runs local test server"
	@echo ""

.PHONY: all all-assets clean install help status linkml-lint yaml-lint yamlfmt-beta test testdoc serve gen-project gendoc test-schema test-python test-examples ensure-dirs

ensure-dirs:
	mkdir -p assets
	mkdir -p $(DEST)
	mkdir -p $(DOCDIR)
	mkdir -p $(PYMODEL)
	mkdir -p examples/output
	mkdir -p $(EXCEL_TEMPLATES_DIR)
	mkdir -p project/class-model-tsvs-organized
	mkdir -p $(DOCDIR)/javascripts

status:
	@echo "Project: $(SCHEMA_NAME)"
	@echo "Source: $(SOURCE_SCHEMA_PATH)"

# install any dependencies required for building
install:
	poetry install --all-extras

# EXPERIMENTAL
create-data-harmonizer:
	npm init data-harmonizer $(SOURCE_SCHEMA_PATH)

all: ensure-dirs site linkml-lint yaml-lint qc gen-excel project/class-model-tsvs-organized

all-assets: ensure-dirs assets/mixs_structured_patterns_preferred.yaml assets/mixs-pattern-materialized-normalized-minimized.yaml assets/mixs_derived_class_term_schemasheet.tsv assets/required_and_recommended_slot_usages.tsv assets/extensions-dendrogram.pdf assets/soil-vs-water-slot-usage.yaml assets/class_summary_results.tsv assets/mixs-schemasheets-concise.tsv assets/mixs-schemasheets-concise-global-slots.tsv assets/mixs-patterns-materialized.yaml

site: gen-project gendoc
%.yaml: gen-project

# generates all project files
gen-project: ensure-dirs $(PYMODEL)
	$(RUN) linkml generate project --log_level INFO --config-file project-generator-config.yaml $(SOURCE_SCHEMA_PATH) && mv $(DEST)/*.py $(PYMODEL)

test: linkml-lint yaml-lint qc test-schema test-python test-examples

test-schema:
	@echo "Schema generation eliminated due to runtime concerns - validation handled by gen-project"

test-python:
	$(RUN) python -m unittest discover

linkml-lint: # was previously just "lint"
	-$(RUN) linkml lint $(SOURCE_SCHEMA_PATH)

yaml-lint: # Run yamllint on schema files
	@echo "Running yamllint on src/mixs/schema..."
	$(RUN) yamllint -c .yamllint src/mixs/schema

test-examples: examples/output

examples/output: src/mixs/schema/mixs.yaml
	mkdir -p $@
	$(RUN) linkml examples \
		--output-formats json \
		--output-formats yaml \
		--counter-example-input-directory src/data/examples/invalid \
		--input-directory src/data/examples/valid \
		--output-directory $@ \
		--schema $< > $@/README.md


#  |\
  #	yamlfmt -in -conf .yamlfmt >

assets/mixs_structured_patterns_preferred.yaml: src/mixs/schema/mixs.yaml
	mkdir -p assets
	yq '(.slots[] | select(has("structured_pattern") and has("pattern"))) |= del(.pattern)' $< > $@

assets/mixs-pattern-materialized-normalized-minimized.yaml: assets/mixs_structured_patterns_preferred.yaml
	mkdir -p assets
	$(RUN) linkml generate linkml \
		--format yaml \
		--no-mergeimports \
		--no-materialize-attributes \
		--materialize-patterns $< |\
	yq eval '(.. | select(has("from_schema")) | .from_schema) style="" | del(.. | select(has("from_schema")).from_schema)' |\
	yq eval '.classes[] |= select(has("annotations")).annotations |= map_values(.value)' |\
	yq eval '.prefixes |= map_values(.prefix_reference)' |\
	yq eval '.settings |= map_values(.setting_value)'  |\
	yq eval '.slots[] |= select(has("annotations")).annotations |= map_values(.value)' |\
	yq eval 'del(.classes.[].name)' |\
	yq eval 'del(.classes.[].slot_usage.[].name)'  |\
	yq eval 'del(.enums.[].name)'  |\
	yq eval 'del(.enums.[].permissible_values.[].text)' |\
	yq eval 'del(.slots[] | select(.domain != "MixsCompliantData") | .domain)'  |\
	yq eval 'del(.slots.[].name)' |\
	yq eval 'del(.source_file)'  |\
	yq eval 'del(.subsets.[].name)' > $@

yamlfmt-beta: # was test1
	echo $$PATH
	yamlfmt -conf .yamlfmt src/mixs/schema/mixs.yaml > src/mixs/schema/mixs_standardized.yaml

# Test documentation locally
serve: mkd-serve

# Python datamodel
$(PYMODEL):
	mkdir -p $@

$(DOCDIR):
	mkdir -p $@

gendoc: ensure-dirs $(DOCDIR)
	cp $(SRC)/docs/*md $(DOCDIR) ; \
	$(RUN) linkml generate doc ${GEN_DARGS} $(SOURCE_SCHEMA_PATH) -d $(DOCDIR) --template-directory $(TEMPLATEDIR) --use-slot-uris --use-class-uris --include src/mixs/schema/deprecated.yaml
	$(RUN) python $(SRC)/scripts/term_list_generator.py $(TERM_LIST_FILE)
	$(RUN) python $(SRC)/scripts/combinations_list_generator.py $(COMBINATIONS_FILE)
	$(RUN) python $(SRC)/scripts/enumerations_list_generator.py $(ENUMERATIONS_FILE)
	mkdir -p $(DOCDIR)/javascripts
	$(RUN) cp $(SRC)/scripts/javascripts/* $(DOCDIR)/javascripts/

testdoc: gendoc serve

MKDOCS = $(RUN) mkdocs
mkd-%:
	$(MKDOCS) $*

PROJECT_FOLDERS = sqlschema shex shacl protobuf prefixmap owl jsonschema jsonld graphql excel

clean: clean-assets
	rm -rf $(DEST)
	rm -rf tmp
	rm -fr docs/*
	rm -fr $(PYMODEL)/*
	rm -rf $(EXCEL_TEMPLATES_DIR)
	rm -rf examples/output

.PHONY: qc clean-assets

qc:
	poetry run deptry . --ignore DEP004

clean-assets:
	rm -rf assets/class_summary_results.* \
	       assets/mixs_derived_class_term_schemasheet.* \
	       assets/mixs-patterns-materialized.yaml \
	       assets/mixs_structured_patterns_preferred.yaml \
	       assets/mixs-pattern-materialized-normalized-minimized.yaml \
	       assets/mixs-schemasheets-concise* \
	       assets/required_and_recommended_slot_usages.tsv \
	       assets/mixs_derived_class_term_schemasheet_* \
	       assets/extensions-dendrogram.pdf \
	       assets/soil-vs-water-slot-usage.yaml

include project.Makefile
