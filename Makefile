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
	rm -rf mkdocs_html/*
	#rm -rf model/schema/*yaml
	mkdir -p logs
	touch logs/.gitkeep

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
#		--exclude excel \

# excel completes now but takes ~ 1.5 hours!
generated/mixs.py: model/schema/mixs.yaml
	$(RUN) gen-project \
		--exclude java \
		--exclude markdown \
		--dir $(dir $@) $< 2>&1 | tee -a logs/linkml_artifact_generation.log
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

# see https://github.com/microbiomedata/mixs/issues/57
# --use-slot-uris
generated/docs/index.md: model/schema/mixs.yaml
	$(RUN) gen-doc $< --directory $(dir $@) --template-directory doc_templates

generated/docs/introduction/%.md: generated/docs/index.md
	cp -R static_md/* $(dir $@)
	cp citation.ris $(dir $@)/..

# add more logging?
# some docs pages not being created
# usage of mkdocs.yml attributes like analytics?

mkdocs_html/index.html: generated/docs/introduction/background.md
	poetry run mkdocs build

# test docs locally.
# repeats build
docserve: generated/docs/introduction/background.md
	$(RUN) mkdocs serve

# repeats build
# pushes to gh-pages branch
# exposes at https://GenomicsStandardsConsortium.github.io/mixs/
gh_docs: generated/docs/introduction/background.md
	poetry run mkdocs gh-deploy
