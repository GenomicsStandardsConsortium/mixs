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

.PHONY: schemasheets_clean schemasheets_all validation_expected_pass validation_missing validation_extra bare_jsonschema

schemasheets_all: \
schemasheets_clean \
schemasheets/logs/database_test_linting_log.tsv \
schemasheets/generated/database_test_generated.sql \
schemasheets/example_data/out/database.json schemasheets/example_data/out/database.db \
validation_expected_pass validation_missing validation_extra bare_jsonschema

schemasheets_clean:
	rm -rf schemasheets/example_data/out/*
	rm -rf schemasheets/generated/*
	rm -rf schemasheets/logs/*
	rm -rf schemasheets/yaml_out/*

schemasheets/yaml_out/database_test.yaml: \
schemasheets/tsv_in/database_test.tsv \
schemasheets/tsv_in/mixs_schema_annotations.tsv \
schemasheets/tsv_in/mixs_prefixes.tsv
	$(RUN) sheets2linkml --output $@ $^

# --fix / --no-fix
# see https://github.com/linkml/linkml/blob/main/linkml/linter/config/default.yaml
schemasheets/logs/database_test_linting_log.tsv: schemasheets/yaml_out/database_test.yaml
	- $(RUN) linkml-lint \
		--format tsv \
		--output $@ $< \
		--config schemasheets/configs/linter_config_default.yaml

# \
#		--ignore-warnings

# todo capture log?
schemasheets/generated/database_test_generated.yaml: schemasheets/yaml_out/database_test.yaml
	$(RUN) gen-linkml \
		--format yaml  \
		--no-materialize-attributes $^ > $@

# todo capture log?
schemasheets/generated/database_test_generated.sql: \
schemasheets/generated/database_test_generated.yaml
	$(RUN) gen-project \
		--dir schemasheets/generated $<

# todo excel has duplicate tabs
#  sqlschema only models database class
#  I didn't say that it was the tree_root

validation_expected_pass: \
schemasheets/generated/database_test_generated.yaml schemasheets/example_data/in/database.yaml
	$(RUN) linkml-validate \
		--target-class Database \
		--schema $^


validation_missing: \
schemasheets/generated/database_test_generated.yaml schemasheets/example_data/in/database_missing.yaml
	! $(RUN) linkml-validate \
		--target-class Database \
		--schema $^


validation_extra: \
schemasheets/generated/database_test_generated.yaml schemasheets/example_data/in/database_extra.yaml
	! $(RUN) linkml-validate \
		--target-class Database \
		--schema $^

schemasheets/example_data/out/database.json: \
schemasheets/example_data/in/database.yaml \
schemasheets/generated/database_test_generated.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--target-class Database $< \
		--schema $(word 2,$^)

schemasheets/example_data/out/database.db: \
schemasheets/generated/database_test_generated.yaml \
schemasheets/example_data/in/database.yaml
	$(RUN) linkml-sqldb dump --db $@ --schema $^
	sqlite3 $@ ".header on" "select * from Mims"

bare_jsonschema: \
schemasheets/example_data/in/database_missing.json \
schemasheets/generated/jsonschema/database_test_generated.schema.json
	- ! jsonschema -i $^

