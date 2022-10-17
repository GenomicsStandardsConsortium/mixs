# document installation of poetry application and `poetry install`

RUN=poetry run

.PHONY: all clean gh_docs docserve

# html_docs
all: clean generated/mixs.py mkdocs_html/index.html

# ---------------------------------------
# TSVs from google drive
# ---------------------------------------
# for seeding

clean:
	#rm -rf downloads/*tsv
	rm -rf generated/*
	rm -rf logs/*
	rm -rf mkdocs_html/
	#rm -rf model/schema/*yaml

#model/schema/mixs.yaml: downloads/mixs6.tsv downloads/mixs6_core.tsv
#	$(RUN) python -m gsctools.mixs_converter  2>&1 | tee -a logs/sheet2linkml.log
#
#downloads/mixs6.tsv:
#	curl -L -s 'https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/export?format=tsv&gid=750683809' > $@
#downloads/mixs6_core.tsv:
#	curl -L -s 'https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/export?format=tsv&gid=178015749' > $@

# todo add owl back in and make it awesome
# todo derive output path from target file name
# 		--exclude owl \

generated/mixs.py: model/schema/mixs.yaml
	$(RUN) gen-project \
		--exclude java \
		--exclude markdown \
		--dir $(dir $@) $< 2>&1 | tee -a logs/linkml_artifact_generation.log

# 		--exclude excel \

#	mkdir generated/excel
#	$(RUN) gen-excel --output generated/excel/mixs.xlsx $<
#	# skipping jinja --template_file
#	mkdir generated/java
#	$(RUN) gen-java --package mixs --output_directory generated/java $<

## ---------------------------------------
## MARKDOWN DOCS
##      Generate documentation ready for mkdocs
## ---------------------------------------
## For help with mkdocs see https://www.mkdocs.org/.

generated/docs/index.md: model/schema/mixs.yaml generated/mixs.py
	$(RUN) gen-doc $< --directory $(dir $@) --template-directory doc_templates --use-slot-uris

generated/docs/introduction/%.md: generated/docs/index.md
	cp -R static_md/* $(dir $@)

# add more logging?
# some docs pages not being created
# usage of mkdocs.yml attributes like analytics?

mkdocs_html/index.html: generated/docs/index.md
	poetry run mkdocs build

# test docs locally.
# repeats build
docserve:
	$(RUN) mkdocs serve

# repeats build
# pushes to gh-pages branch
# exposes at https://GenomicsStandardsConsortium.github.io/mixs/
gh_docs:
	poetry run mkdocs gh-deploy

# ---------------------------------------

.PHONY: schemasheets_clean schemasheets_all validation_expected_pass validation_missing validation_extra bare_jsonschema_invalid

schemasheets_all: \
schemasheets_clean \
schemasheets/logs/mixs_schemasheets_linting_log.tsv \
schemasheets/generated/mixs_schemasheets_generated.sql \
schemasheets/example_data/out/mixs_database.json schemasheets/example_data/out/mixs_database.db \
validation_expected_pass validation_missing validation_extra bare_jsonschema_invalid \
schemasheets/example_data/out/mims_soil_set_database.ttl

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

schemasheets/yaml_out/mixs_schemasheets.yaml: \
schemasheets/tsv_in/MIxS_6_term_updates_MIxS6_Core-Final_clean_classdefs.tsv \
schemasheets/tsv_in/MIxS_6_term_updates_MIxS6_Core-Final_clean_slot_assignments.tsv \
schemasheets/tsv_in/MIxS_6_term_updates_MIxS6_Core-Final_clean_slotdefs.tsv \
schemasheets/tsv_in/MIxS_6_term_updates_MIxS6_packages-Final_clean_classdefs.tsv \
schemasheets/tsv_in/MIxS_6_term_updates_MIxS6_packages-Final_clean_slot_assignments.tsv \
schemasheets/tsv_in/MIxS_6_term_updates_MIxS6_packages-Final_clean_slotdefs_conflicting_defer_to_soil.tsv \
schemasheets/tsv_in/MIxS_6_term_updates_MIxS6_packages-Final_clean_slotdefs_non_conflicting_shared.tsv \
schemasheets/tsv_in/generated/mixs_combination_classes.tsv \
schemasheets/tsv_in/mixs_clear_cut_enums.tsv \
schemasheets/tsv_in/mixs_prefixes.tsv \
schemasheets/tsv_in/mixs_schema_annotations.tsv \
schemasheets/tsv_in/mixs_utility.tsv
	$(RUN) sheets2linkml --output $@ $^

# schemasheets/tsv_in/enums_generated_keep.tsv \

# --fix / --no-fix
# see https://github.com/linkml/linkml/blob/main/linkml/linter/config/default.yaml
schemasheets/logs/mixs_schemasheets_linting_log.tsv: schemasheets/yaml_out/mixs_schemasheets.yaml
	- $(RUN) linkml-lint \
		--format tsv \
		--output $@ $< \
		--config schemasheets/configs/linter_config_default.yaml

# \
#		--ignore-warnings

# todo capture log?
schemasheets/generated/mixs_schemasheets_generated.yaml: schemasheets/yaml_out/mixs_schemasheets.yaml
	$(RUN) gen-linkml \
		--format yaml  \
		--no-materialize-attributes $^ > $@

# todo capture log?
schemasheets/generated/mixs_schemasheets_generated.sql: \
schemasheets/generated/mixs_schemasheets_generated.yaml
	$(RUN) gen-project \
		--exclude excel \
		--dir schemasheets/generated $<

# todo excel has duplicate tabs
#  also slow
#  sqlschema only models mixs_database class
#  I didn't say that it was the tree_root
# markdown generaton slow but may reveal subtle problems
# how to test serve?

validation_expected_pass: \
schemasheets/generated/mixs_schemasheets_generated.yaml schemasheets/example_data/in/mixs_database.yaml
	$(RUN) linkml-validate \
		--target-class Database \
		--schema $^


validation_missing: \
schemasheets/generated/mixs_schemasheets_generated.yaml schemasheets/example_data/in/mixs_database_missing.yaml
	! $(RUN) linkml-validate \
		--target-class Database \
		--schema $^


validation_extra: \
schemasheets/generated/mixs_schemasheets_generated.yaml schemasheets/example_data/in/mixs_database_extra.yaml
	! $(RUN) linkml-validate \
		--target-class Database \
		--schema $^

schemasheets/example_data/out/mixs_database.json: \
schemasheets/generated/mixs_schemasheets_generated.yaml \
schemasheets/example_data/in/mixs_database.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--target-class Database \
		--schema $^

schemasheets/example_data/out/mixs_database.db: \
schemasheets/generated/mixs_schemasheets_generated.yaml \
schemasheets/example_data/in/mixs_database.yaml
	$(RUN) linkml-sqldb dump --db $@ --target-class Database --schema $^
	sqlite3 $@ ".header on" "select * from Mims"

bare_jsonschema_invalid: \
schemasheets/example_data/in/mixs_database_missing.json \
schemasheets/generated/jsonschema/mixs_schemasheets_generated.schema.json
	! jsonschema -i $^

#schemasheets/example_data/out/mims_soil_set_database.yaml: \
#schemasheets/generated/mixs_schemasheets_generated.yaml \
#schemasheets/example_data/in/MimsSoil_data.tsv.minimal
#	$(RUN) linkml-convert \
#		--output $@ \
#		--target-class Database \
#		--index-slot mims_soil_set \
#		--schema $^

schemasheets/example_data/out/mims_soil_set_database.ttl: \
schemasheets/generated/mixs_schemasheets_generated.yaml \
schemasheets/example_data/in/mims_soil_set_database.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--target-class Database \
		--index-slot mims_soil_set \
		--schema $^

#csv/tsv
#json
#json-ld
#rdf/ttl
#yml/yaml

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

all_owl_enums: clean_owl_enums schemasheets/generated/MIxS_6_term_updates_MIxS6_Core-Final_clean_enums.owl.ttl

clean_owl_enums:
	rm -f schemasheets/yaml_out/MIxS_6_term_updates_MIxS6_Core-Final_clean_enums.yaml
	rm -f schemasheets/generated/MIxS_6_term_updates_MIxS6_Core-Final_clean_enums.owl.ttl

schemasheets/yaml_out/MIxS_6_term_updates_MIxS6_Core-Final_clean_enums.yaml: \
schemasheets/tsv_in/MIxS_6_term_updates_MIxS6_Core-Final_clean_enums.tsv
	$(RUN) sheets2linkml $< > $@

schemasheets/generated/MIxS_6_term_updates_MIxS6_Core-Final_clean_enums.owl.ttl: \
schemasheets/yaml_out/MIxS_6_term_updates_MIxS6_Core-Final_clean_enums.yaml
	$(RUN) gen-owl \
		--format ttl \
		--output $@ $<

#enums_reality_check:
#	$(RUN) sheets2linkml \
#		--gsheet-id 1wVoaiFg47aT9YWNeRfTZ8tYHN8s8PAuDx5i2HUcDpvQ test+enums

schemasheets/yaml_out/test_enums.yaml: schemasheets/tsv_in/mixs_clear_cut_enums.tsv
	$(RUN) sheets2linkml \
		--output $@ $<

#schemasheets/example_data/out/mims_soil_set_database.tsv: \
#schemasheets/yaml_out/mixs_schemasheets.yaml \
#schemasheets/example_data/in/mims_soil_set_database.yaml
#	$(RUN) linkml-convert \
#		--output $@ \
#		--target-class Database \
#		--index-slot mims_soil_set \
#		--schema $^
