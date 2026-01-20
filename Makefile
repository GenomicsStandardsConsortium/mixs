# RELEASE SOP: make install clean all all-contrib test

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
	@echo "Core workflow: make install clean all test"
	@echo ""
	@echo "Main targets:"
	@echo "  install       -- install Python dependencies (used by all GH Actions)"
	@echo "  clean         -- remove all generated files (calls clean-contrib; used by main & docs GH Actions)"
	@echo "  all           -- complete build (calls site, qc, gen-excel, project/class-model-tsvs-organized, all-contrib, linkml-lint, yaml-lint; used by main GH Action)"
	@echo "  test          -- validation & tests (calls qc, test-schema, test-python, test-examples, linkml-lint, yaml-lint; used by main GH Action)"
	@echo ""
	@echo "Output to directories:"
	@echo "  site          -- build website (called by all; calls gen-project, gendoc)"
	@echo "  gen-project   -- generate project/ artifacts (called by all via site)"
	@echo "  gendoc        -- generate docs/ website files (called by all via site, testdoc; used by docs GH Actions)"
	@echo "  gen-excel     -- generate mixs-templates/ Excel files (called by all)"
	@echo "  project/class-model-tsvs-organized -- generate organized TSV files (called by all)"
	@echo "  all-contrib   -- generate contrib/ schema transformation pipeline (called by all; used by main GH Action):"
	@echo "                   1. structured-patterns-preferred (remove pattern field)"
	@echo "                   2. normalized-minimized (yq cleanup, no imports)"
	@echo "                   3. patterns-materialized (expand patterns from step 2)"
	@echo "                   + schemasheets, dendrograms, slot usage reports"
	@echo "  test-examples -- generate examples/output/ validated data (called by test)"
	@echo ""
	@echo "Quality checks:"
	@echo "  qc            -- dependency validation with deptry (called by all, test; can fail)"
	@echo "  linkml-lint   -- schema validation warnings (called by all, test; non-failing; has GH Action)"
	@echo "  yaml-lint     -- YAML format warnings (called by all, test; non-failing; has GH Action)"
	@echo ""
	@echo "Individual tests:"
	@echo "  test-schema   -- schema validation tests (called by test)"
	@echo "  test-python   -- Python unit tests (called by test)"
	@echo ""
	@echo "Cleanup:"
	@echo "  clean-contrib -- remove contrib/ files (called by clean)"
	@echo ""
	@echo "Standalone utilities:"
	@echo "  help          -- show this help"
	@echo "  status        -- show project info (called by help)"
	@echo "  testdoc       -- build & serve docs locally (calls gendoc, serve)"
	@echo "  serve         -- serve existing docs locally via mkdocs (called by testdoc)"
	@echo "  yamlfmt-beta  -- experimental YAML formatter"
	@echo "  create-data-harmonizer -- experimental npm tool"
	@echo ""

.PHONY: all all-contrib clean install help status linkml-lint yaml-lint yamlfmt-beta test testdoc serve gen-project gendoc test-schema test-python test-examples ensure-dirs clean-contrib

ensure-dirs:
	mkdir -p contrib
	mkdir -p $(DEST)
	mkdir -p $(DOCDIR)
	mkdir -p $(PYMODEL)
	mkdir -p $(EXCEL_TEMPLATES_DIR)
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

all: ensure-dirs site qc gen-excel project/class-model-tsvs-organized all-contrib linkml-lint yaml-lint

all-contrib: ensure-dirs contrib/mixs_structured_patterns_preferred.yaml contrib/mixs-normalized-minimized.yaml contrib/mixs_derived_class_term_schemasheet.tsv contrib/required_and_recommended_slot_usages.tsv contrib/extensions-dendrogram.pdf contrib/soil-vs-water-slot-usage.yaml contrib/class_summary_results.tsv contrib/mixs-schemasheets-concise.tsv contrib/mixs-schemasheets-concise-global-slots.tsv contrib/mixs-patterns-materialized.yaml

site: gen-project gendoc
%.yaml: gen-project

# generates all project files
gen-project: ensure-dirs $(PYMODEL)
	$(RUN) linkml generate project --log_level WARNING --config-file project-generator-config.yaml $(SOURCE_SCHEMA_PATH) && mv $(DEST)/*.py $(PYMODEL)

test: qc test-schema test-python test-examples linkml-lint yaml-lint

test-schema:
	@echo "Schema re-generation in test phase eliminated due to long run time"

test-python:
	$(RUN) python -m unittest discover

linkml-lint: # was previously just "lint"
	$(RUN) linkml lint $(SOURCE_SCHEMA_PATH) || true

yaml-lint: # Run yamllint on schema files
	@echo "Running yamllint on src/mixs/schema..."
	$(RUN) yamllint -c .yamllint src/mixs/schema || true

test-examples: examples/output

examples/output: contrib/mixs-patterns-materialized.yaml
	mkdir -p $@
	$(RUN) linkml examples \
		--output-formats json \
		--output-formats yaml \
		--counter-example-input-directory src/data/examples/invalid \
		--input-directory src/data/examples/valid \
		--output-directory $@ \
		--schema $< > $@/README.md

contrib/mixs_structured_patterns_preferred.yaml: src/mixs/schema/mixs.yaml
	mkdir -p contrib
	yq '(.slots[] | select(has("structured_pattern") and has("pattern"))) |= del(.pattern)' $< > $@

contrib/mixs-normalized-minimized.yaml: contrib/mixs_structured_patterns_preferred.yaml
	mkdir -p contrib
	$(RUN) linkml generate linkml \
		--format yaml \
		--no-mergeimports \
		--no-materialize-attributes \
		--no-materialize-patterns $< |\
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

contrib/mixs-patterns-materialized.yaml: contrib/mixs-normalized-minimized.yaml
	mkdir -p contrib
	$(RUN) gen-linkml \
		--format yaml \
		--materialize-patterns \
		--no-materialize-attributes $< |\
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

.PHONY: gen-excel

gen-excel: $(SOURCE_SCHEMA_PATH)
	mkdir -p $(DEST)/excel
	$(RUN) gen-excel $< \
		--include-mixins \
		--split-workbook-by-class \
		--output $(DEST)/excel
	mkdir -p $(EXCEL_TEMPLATES_DIR)
	$(RUN) organize-files \
		--mixs-schema-file $< \
		--source-directory $(DEST)/excel \
		--base-destination-folder $(EXCEL_TEMPLATES_DIR) \
		--extensions xlsx

project/class-model-tsvs-organized: src/mixs/schema/mixs.yaml
	$(RUN) linkml2class-tsvs \
		--eligible-parent-classes Checklist \
		--eligible-parent-classes Extension \
		--output-dir project/class-model-tsvs \
		--schema-file src/mixs/schema/mixs.yaml
	mkdir -p project/class-model-tsvs-organized
	$(RUN) organize-files \
		--mixs-schema-file $< \
		--source-directory project/class-model-tsvs \
		--base-destination-folder project/class-model-tsvs-organized \
		--extensions tsv
	rm -rf project/class-model-tsvs
	mv project/class-model-tsvs-organized project/class-model-tsvs

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
	rm -f $(DOCDIR)/README.md ; \
	$(RUN) linkml generate doc ${GEN_DARGS} $(SOURCE_SCHEMA_PATH) -d $(DOCDIR) --template-directory $(TEMPLATEDIR) --use-slot-uris --use-class-uris --include src/mixs/schema/deprecated.yaml
	$(RUN) generate-term-list --output-file $(TERM_LIST_FILE)
	$(RUN) generate-combinations --output-file $(COMBINATIONS_FILE)
	$(RUN) generate-enumerations --output-file $(ENUMERATIONS_FILE)
	mkdir -p $(DOCDIR)/javascripts
	$(RUN) cp $(SRC)/scripts/javascripts/* $(DOCDIR)/javascripts/

testdoc: gendoc serve

MKDOCS = $(RUN) mkdocs
mkd-%:
	$(MKDOCS) $*

PROJECT_FOLDERS = sqlschema shex shacl protobuf prefixmap owl jsonschema jsonld graphql excel

clean: clean-contrib
	rm -rf $(DEST)
	rm -rf tmp
	rm -fr docs/*
	rm -fr $(PYMODEL)/*
	rm -rf $(EXCEL_TEMPLATES_DIR)
	rm -rf examples/output

.PHONY: qc clean-assets

qc:
	poetry run deptry . --ignore DEP004

clean-contrib:
	rm -rf contrib/class_summary_results.* \
	       contrib/mixs_derived_class_term_schemasheet.* \
	       contrib/mixs-patterns-materialized.yaml \
	       contrib/mixs_structured_patterns_preferred.yaml \
	       contrib/mixs-normalized-minimized.yaml \
	       contrib/mixs-schemasheets-concise* \
	       contrib/required_and_recommended_slot_usages.tsv \
	       contrib/mixs_derived_class_term_schemasheet_* \
	       contrib/extensions-dendrogram.pdf \
	       contrib/soil-vs-water-slot-usage.yaml

include contrib.Makefile
