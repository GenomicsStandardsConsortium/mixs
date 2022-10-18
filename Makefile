# document installation of poetry application and `poetry install`

RUN=poetry run

#.PHONY: all clean gh_docs docserve
#
## html_docs
#all: clean generated/mixs.py mkdocs_html/index.html
#
## ---------------------------------------
## TSVs from google drive
## ---------------------------------------
## for seeding
#
#clean:
#	#rm -rf downloads/*tsv
#	rm -rf generated/*
#	rm -rf logs/*
#	rm -rf mkdocs_html/
#	#rm -rf model/schema/*yaml
#
##model/schema/mixs.yaml: downloads/mixs6.tsv downloads/mixs6_core.tsv
##	$(RUN) python -m gsctools.mixs_converter  2>&1 | tee -a logs/sheet2linkml.log
##
##downloads/mixs6.tsv:
##	curl -L -s 'https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/export?format=tsv&gid=750683809' > $@
##downloads/mixs6_core.tsv:
##	curl -L -s 'https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/export?format=tsv&gid=178015749' > $@
#
## todo add owl back in and make it awesome
## todo derive output path from target file name
## 		--exclude owl \
#
#generated/mixs.py: model/schema/mixs.yaml
#	$(RUN) gen-project \
#		--exclude java \
#		--exclude markdown \
#		--dir $(dir $@) $< 2>&1 | tee -a logs/linkml_artifact_generation.log
#
## 		--exclude excel \
#
##	mkdir generated/excel
##	$(RUN) gen-excel --output generated/excel/mixs.xlsx $<
##	# skipping jinja --template_file
##	mkdir generated/java
##	$(RUN) gen-java --package mixs --output_directory generated/java $<
#
### ---------------------------------------
### MARKDOWN DOCS
###      Generate documentation ready for mkdocs
### ---------------------------------------
### For help with mkdocs see https://www.mkdocs.org/.
#
#generated/docs/index.md: model/schema/mixs.yaml generated/mixs.py
#	$(RUN) gen-doc $< --directory $(dir $@) --template-directory doc_templates --use-slot-uris
#
#generated/docs/introduction/%.md: generated/docs/index.md
#	cp -R static_md/* $(dir $@)
#
## add more logging?
## some docs pages not being created
## usage of schemasheets_mkdocs.yml attributes like analytics?
#
#mkdocs_html/index.html: generated/docs/index.md
#	poetry run mkdocs build
#
## test docs locally.
## repeats build
#docserve:
#	$(RUN) mkdocs serve
#
## repeats build
## pushes to gh-pages branch
## exposes at https://GenomicsStandardsConsortium.github.io/mixs/
#gh_docs:
#	poetry run mkdocs gh-deploy

# ---------------------------------------

.PHONY: schemasheets_clean schemasheets_all validation_expected_pass validation_missing validation_extra bare_jsonschema

schemasheets_all: \
schemasheets_clean \
schemasheets/yaml_out/mixs_schemasheets.yaml \
schemasheets/logs/mixs_schemasheets_linting_log.tsv \
schemasheets/generated/mixs_schemasheets_generated.yaml \
schemasheets/generated/mixs_schemasheets_generated.sql \
validation_expected_pass validation_missing validation_extra bare_jsonschema \
schemasheets/example_data/out/mims_soil_set_database.json \
schemasheets/example_data/out/mims_soil_set_database.ttl \
schemasheets/mkdocs_html/index.md

# todo slow
#   schemasheets/example_data/out/mixs_database.db \

# this could be a circular dependency
# silently depends on schemasheets/yaml_out/mixs_schemasheets.yaml
# but also prepares schemasheets/tsv_in/generated/mixs_combination_classes.tsv
# which will be one of the inputs into generating schemasheets/yaml_out/mixs_schemasheets.yaml
# so don't put into schemasheets_all
schemasheets/tsv_in/generated/mixs_combination_classes.tsv:
	$(RUN) python gsctools/gen_mixs_combination_classes.py

schemasheets_clean:
	rm -rf schemasheets/example_data/out/*
	rm -rf schemasheets/generated/*
	rm -rf schemasheets/logs/*
	rm -rf schemasheets/yaml_out/*
	rm -rf schemasheets/mkdocs_html/*
	rm -rf schemasheets/generated/gen_docs_docs/*

schemasheets/yaml_out/mixs_schemasheets.yaml: \
schemasheets/tsv_in/MIxS_6_term_updates_classdefs.tsv \
schemasheets/tsv_in/MIxS_6_term_updates_partial_slotdefs_more_constraints.tsv \
schemasheets/tsv_in/MIxS_6_term_updates_slot_assignments.tsv \
schemasheets/tsv_in/generated/mixs_combination_classes.tsv \
schemasheets/tsv_in/mixs_clear_cut_enums.tsv \
schemasheets/tsv_in/mixs_prefixes.tsv \
schemasheets/tsv_in/mixs_schema_annotations.tsv \
schemasheets/tsv_in/mixs_subsets.tsv \
schemasheets/tsv_in/mixs_utility.tsv
	$(RUN) sheets2linkml --output $@ $^


# --fix / --no-fix
# see https://github.com/linkml/linkml/blob/main/linkml/linter/config/default.yaml
# enum names should be upper camel case
schemasheets/logs/mixs_schemasheets_linting_log.tsv: schemasheets/yaml_out/mixs_schemasheets.yaml
	- $(RUN) linkml-lint \
		--format tsv \
		--output $@ $< \
		--config schemasheets/configs/linter_config_default.yaml

#		--ignore-warnings

# todo capture log?
#  isn't merging imports
schemasheets/generated/mixs_schemasheets_generated.yaml: schemasheets/yaml_out/mixs_schemasheets.yaml
	$(RUN) gen-linkml \
		--format yaml  \
		--no-materialize-attributes $^ > $@

# todo capture log?
# todo excel artifact has duplicate tabs (with numerical suffixes)
#  but explore whether this would be a useful data collection tool
#  also slow
# markdown generation slow but may reveal subtle problems
# shacl slowish
schemasheets/generated/%: \
schemasheets/generated/mixs_schemasheets_generated.yaml
	$(RUN) gen-project \
		--exclude excel \
		--exclude markdown \
		--dir schemasheets/generated $<

# this doesn't generate the left hand navigation or the index page
schemasheets/generated/gen_docs_docs/index.md: schemasheets/yaml_out/mixs_schemasheets.yaml
	$(RUN) gen-doc $< --directory $(dir $@) --template-directory doc_templates --use-slot-uris

schemasheets/mkdocs_html/index.md: schemasheets/generated/gen_docs_docs/index.md
	cp -R static_md/* $(dir $<)
	$(RUN) mkdocs build --config-file schemasheets_mkdocs.yml
	# then `make schemasheets_docserve` and or `make schemasheets_gh_docs` if desired

schemasheets_docserve:
	$(RUN) mkdocs serve --config-file schemasheets_mkdocs.yml


validation_expected_pass: \
schemasheets/generated/mixs_schemasheets_generated.yaml schemasheets/example_data/in/mims_soil_set_database.yaml
	$(RUN) linkml-validate \
		--target-class Database \
		--schema $^

validation_missing: \
schemasheets/generated/mixs_schemasheets_generated.yaml schemasheets/example_data/in/mims_soil_set_database_missing.yaml
	! $(RUN) linkml-validate \
		--target-class Database \
		--schema $^

validation_extra: \
schemasheets/generated/mixs_schemasheets_generated.yaml schemasheets/example_data/in/mims_soil_set_database_extra.yaml
	! $(RUN) linkml-validate \
		--target-class Database \
		--schema $^

schemasheets/example_data/out/mims_soil_set_database.json: \
schemasheets/generated/mixs_schemasheets_generated.yaml \
schemasheets/example_data/in/mims_soil_set_database.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--target-class Database \
		--schema $^

bare_jsonschema: \
schemasheets/example_data/out/mims_soil_set_database.json \
schemasheets/generated/jsonschema/mixs_schemasheets_generated.schema.json
	$(RUN) jsonschema -i $^


# todo slow
schemasheets/example_data/out/mixs_database.db: \
schemasheets/generated/mixs_schemasheets_generated.yaml \
schemasheets/example_data/out/mims_soil_set_database.json
	$(RUN) linkml-sqldb dump --db $@ --target-class Database --schema $^
	sqlite3 $@ ".header on" "select * from Mims"

schemasheets/example_data/out/mims_soil_set_database.ttl: \
schemasheets/generated/mixs_schemasheets_generated.yaml \
schemasheets/example_data/in/mims_soil_set_database.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--target-class Database \
		--index-slot mims_soil_set \
		--schema $^

# CONVERSION TARGETS
#csv/tsv
#json
#json-ld
#rdf/ttl
#yml/yaml

# GENERAL NOTES
# added xsd prefix for converting non-string values to rdf/ttl
# datetime ranges incompatible with sqlite dump
# may not be possible to convert to or from csv or tsv due to multivalued slots (even is they're not populated?!)
# schemasheets will compile slots starting with digits and generators don't complain either
#   but the jsonschema utility won't validate against the generated jsonschema
# expected problems with enum/pv names/texts
# gen-linkml not merging (for example the "free" linkml:types
# date_or_datetime not implemented yet, and might have some disadvantageous
# what patterns in the schema or data break which tools?
# no good regex for lat_lon?
# multivalued slots with scalar values might be repaired in some situations but don't count on it
