# todo document installation of poetry application and `poetry install`

RUN=poetry run

.PHONY: all clean gh_docs docserve value_syntax_research gsc_vs_nmdc_packages gsc_vs_nmdc_core all_diffs

all: clean alldiffs value_syntax_research model/schema/mixs.yaml generated/mixs.py mkdocs_html/index.html

clean:
	rm -rf downloads/*.*sv
	rm -rf generated/*
	rm -rf logs/*
	rm -rf mkdocs_html/
	rm -rf model/schema/*.yaml


model/schema/mixs.yaml: downloads/mixs6.tsv downloads/mixs6_core.tsv
	$(RUN) python -m gsctools.mixs_converter  2>&1 | tee -a logs/sheet2linkml.log


# ---------------------------------------
# TSVs from google drive
# ---------------------------------------
# for seeding

downloads/mixs6.tsv:
	curl -L -s 'https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/export?format=tsv&gid=750683809' > $@
downloads/mixs6_core.tsv:
	curl -L -s 'https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/export?format=tsv&gid=178015749' > $@


# GSC: MIxS 6 term updates:MIxS6 Core- Final_clean
#   https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/edit#gid=178015749
# GSC: MIxS 6 term updates:MIxS6 packages - Final_clean
#   https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/edit#gid=750683809

# NMDC: NMDC copy of MIxS 6 term updates:
#   https://docs.google.com/spreadsheets/d/1-ocpwjx6nkBod6aj4kcYeSB5NRlhXaYCcuk3ooX2OV4/edit#gid=178015749
# NMDC MIxS 6 term updates:MIxS6 packages - Final_clean
#   https://docs.google.com/spreadsheets/d/1-ocpwjx6nkBod6aj4kcYeSB5NRlhXaYCcuk3ooX2OV4/edit#gid=750683809

alldiffs: clean gsc_vs_nmdc_packages gsc_vs_nmdc_core

downloads/gsc_mixs6.csv:
	curl -L -s 'https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/export?format=csv&gid=750683809' > $@
downloads/gsc_mixs6_core.csv:
	curl -L -s 'https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/export?format=csv&gid=178015749' > $@

downloads/nmdc_mixs6.csv:
	curl -L -s 'https://docs.google.com/spreadsheets/d/1-ocpwjx6nkBod6aj4kcYeSB5NRlhXaYCcuk3ooX2OV4/export?format=csv&gid=750683809' > $@
downloads/nmdc_mixs6_core.csv:
	curl -L -s 'https://docs.google.com/spreadsheets/d/1-ocpwjx6nkBod6aj4kcYeSB5NRlhXaYCcuk3ooX2OV4/export?format=csv&gid=178015749' > $@

gsc_vs_nmdc_packages: downloads/gsc_mixs6.csv downloads/nmdc_mixs6.csv
	# colored display
	csvdiff \
		--primary-key 0,1 \
		--format word-diff $^
	# to file
	csvdiff \
		--primary-key 0,1 \
		--format word-diff $^ > generated/gsc_vs_nmdc_packages.txt

gsc_vs_nmdc_core: downloads/gsc_mixs6_core.csv downloads/nmdc_mixs6_core.csv
	# colored display
	csvdiff \
		--primary-key 1 \
		--format word-diff $^
	# to file
	csvdiff \
		--primary-key 1 \
		--format word-diff $^ > generated/gsc_vs_nmdc_core.txt
# --format string         Available (rowmark|json|legacy-json|diff|word-diff|color-words) (default "diff")

value_syntax_research: downloads/mixs6.tsv downloads/mixs6_core.tsv
	$(RUN) python gsctools/value_syntaxes.py

invariants_research:
	$(RUN) python gsctools/invariants.py

# todo add owl back in and make it awesome
# 		--exclude owl \
# todo what artifacts do we really want?
generated/mixs.py: model/schema/mixs.yaml
	$(RUN) gen-project \
 		--exclude owl \
		--exclude excel \
		--exclude java \
		--exclude markdown \
		--exclude owl \
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

# first documentation step
# ~ 3 minutes
# gen-doc needs to know where the filesystem location of the schema (model/schema/mixs.yaml)
# and a place to put the output
#   can;t remember why I wanted to be fancy and discover the destination from the directory portion of generated/mixs.py
generated/docs/index.md: model/schema/mixs.yaml generated/mixs.py
	$(RUN) gen-doc $< --directory $(dir $@) --template-directory doc_templates

# second documentation step:
# instantaneous
# (otherwise all of the introduction/ pages are 404)
# don't start unless generated/docs/index.md is complete
# determine the input path from the directory portion of generated/docs/index.md
generated/docs/introduction/%.md: generated/docs/index.md
	cp -R static_md/* $(dir $@)

# third/last documentation step
# can trigger the previous two
# ~ 2 minutes
# add more logging?
# some docs pages not being created
# usage of mkdocs.yml attributes like analytics?
mkdocs_html/index.html: generated/docs/introduction/background.md
	$(RUN) mkdocs build

# test docs locally.
docserve: generated/docs/introduction/background.md
	$(RUN) mkdocs serve

# pushes to gh-pages branch
# exposes at https://GenomicsStandardsConsortium.github.io/mixs/
gh_docs: generated/docs/introduction/background.md
	$(RUN) mkdocs gh-deploy


