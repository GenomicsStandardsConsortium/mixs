#
## ----------------------------------------
## Model documentation and schema directory
## ----------------------------------------
#SRC_DIR = model
#PKG_DIR = .
#SCHEMA_DIR = $(SRC_DIR)/schema
#MODEL_DOCS_DIR = $(SRC_DIR)/docs
#SOURCE_FILES := $(shell find $(SCHEMA_DIR) -name '*.yaml')
#SCHEMA_NAMES = $(patsubst $(SCHEMA_DIR)/%.yaml, %, $(SOURCE_FILES))
#RUN = pipenv run
#
#SCHEMA_NAME = mixs
#SCHEMA_SRC = $(SCHEMA_DIR)/$(SCHEMA_NAME).yaml
##PKG_TGTS = graphql json  jsonschema owl rdf jsonld shex
#PKG_TGTS =  json  jsonschema owl
#TGTS = docs $(PKG_TGTS)
#
## Global generation options
#GEN_OPTS =
#
## ----------------------------------------
## TOP LEVEL TARGETS
## ----------------------------------------
## all: env.lock gen unlock
#all: clean env.lock generated unlock
#
## ---------------------------------------
## env.lock:  set up pipenv
## ---------------------------------------
#export PIPENV_VERBOSITY = -1
#env.lock:
#	pipenv install --dev
#	cp /dev/null env.lock
#unlock:
##	pipenv --rm
#	rm env.lock
#
#generated: model/schema/mixs.yaml
#	$(RUN) gen-project --dir . $< 2> generated.log
#
#
## ---------------------------------------
## GEN: run generator for each target
## ---------------------------------------
#gen: $(patsubst %,gen-%,$(TGTS))
#
## ---------------------------------------
## CLEAN: clear out all of the targets
## ---------------------------------------
#clean:
#	rm -rf target/
#	rm -rf generated/
#	rm -f env.lock
#	rm -rf downloads/mixs6*
#	rm -f model/schema/mixs.yaml
##	pipenv --rm
#.PHONY: clean
#
## ---------------------------------------
## SQUEAKY_CLEAN: remove all of the final targets to make sure we don't leave old artifacts around
## ---------------------------------------
#squeaky_clean: clean $(patsubst %,squeaky_clean-%,$(PKG_TGTS))
#	find docs/*  ! -name 'README.*' -exec rm -rf {} +
#	find $(PKG_DIR)/model/schema  ! -name 'README.*' -type f -exec rm -f {} +
#	find $(PKG_DIR) -name "*.py" ! -name "__init__.py" ! -name "linkml_files.py" -exec rm -f {} +
#
#squeaky_clean-%: clean
#	find $(PKG_DIR)/$* ! -name 'README.*' ! -name $*  -type f -exec rm -f {} +
#
## ---------------------------------------
## T: List files to generate
## ---------------------------------------
#t:
#	echo $(SCHEMA_NAMES)
#
## ---------------------------------------
## ECHO: List all targets
## ---------------------------------------
#echo:
#	echo $(patsubst %,gen-%,$(TGTS))
#
#
#tdir-%:
#	mkdir -p target/$*
#
#docs:
#	mkdir -p $@
#
#
## ---------------------------------------
## Move the model across
## ---------------------------------------
##move-model:
##	mkdir -p $(PKG_DIR)/model/schema
##	cp -r model/schema/* $(PKG_DIR)/model/schema
#
#
## ---------------------------------------
## MARKDOWN DOCS
##      Generate documentation ready for mkdocs
## ---------------------------------------
## For help with mkdocs see https://www.mkdocs.org/.
#
#gen-docs: docs/index.md env.lock
#.PHONY: gen-docs
#
#docs/index.md: target/docs/index.md
#	cp -R $(MODEL_DOCS_DIR)/*.md target/docs
#	$(RUN) mkdocs build
#target/docs/index.md: $(SCHEMA_DIR)/$(SCHEMA_NAME).yaml tdir-docs env.lock
#	$(RUN) gen-markdown -M slot=term -M class=package -M mixin=checklist -M enum=dropdown $(GEN_OPTS) --no-mergeimports --dir target/docs $<
#
## test docs locally.
#docserve:
#	$(RUN) mkdocs serve
#
#gh-deploy:
#	$(RUN) mkdocs gh-deploy
#


.PHONY: all clean html_docs cp_static_md

# ---------------------------------------
# TSVs from google drive
# ---------------------------------------
# for seeding

RUN=poetry run

downloads/mixs6.tsv:
	curl -L -s 'https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/export?format=tsv&gid=750683809' > $@
downloads/mixs6_core.tsv:
	curl -L -s 'https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/export?format=tsv&gid=178015749' > $@

model/schema/mixs.yaml: downloads/mixs6.tsv downloads/mixs6_core.tsv
	$(RUN) python -m gsctools.mixs_converter  2>&1 | tee -a logs/sheet2linkml.log

clean:
	rm -rf logs/*
	rm -rf downloads/*tsv
	rm -rf model/schema/*yaml

all: clean model/schema/mixs.yaml generated html_docs

generated: model/schema/mixs.yaml
	$(RUN) gen-project --dir $@ $< 2>&1 | tee -a logs/linkml_artifact_generation.log

generated/docs/: model/schema/mixs.yaml
	$(RUN) gen-doc $< --directory $@ --template-directory templates

cp_static_md: generated/docs/
	cp -R static_md/* $<

# add log file
# some pages not being created
# be careful not to hose any existing GH ages content
# how to add static content
# usage of mkdocs.yml attributes like analytics, nav.Index, site_url, repo_url
html_docs: cp_static_md
	poetry run mkdocs build

gh_docs:
	poetry run mkdocs gh-deploy
