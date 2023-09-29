
###only if running the postgres queries
#include local/.env # for PGPASSWORD, BIOSAMPLE_DB_USER etc
#export $(shell sed 's/=.*//'  local/.env)

.PHONY: all clean squeaky-clean conflicts-cleanup conflicts-all-reports linkml-validate-build-test-only linkml-validate-extracted

RUN = poetry run
LEGACY_PREFIX=mixs_v6.xlsx
RC_PREFIX=mixs_6_2_rc

SOURCE_SCHEMA_PATH = generated-schema/$(RC_PREFIX).yaml

DOCDIR = mixs-docs-md
TEMPLATEDIR = mixs-docs-templates

# converted-data/data-conversion-report.md validate-linkml-rdf-data-pure-python

all: squeaky-clean \
generated-schema/mixs_6_2_rc.yaml \
other-reports/build-test-data-coverage-report.yaml linkml-validate-build-test-only \
other-reports/extracted-data-coverage-report.yaml linkml-validate-extracted \
text-mining-results/mixs-v6-repaired-term-title-token-matrix.tsv \
schema-derivatives/$(RC_PREFIX).json data_harmonizer/menu.json \
schema-derivatives/$(RC_PREFIX).owl.ttl validate-linkml-rdf-schema-pure-python \
schema-derivatives/$(RC_PREFIX).schema.json \
validate-multiple-mims-soil converted-data/MimsSoil-example.tsv \
converted-data/data-conversion-report.md validate-linkml-rdf-data-pure-python \
conflicts-all-reports \
other-reports/mixs-scns-vs-ncbi-harmonized-attributes.yaml \
other-reports/slot-usage-report.tsv \
other-reports/schema-lint-report.tsv \
schemasheets-usage-output/$(RC_PREFIX).yaml.concise.usage-report.tsv \
schemasheets-usage-output/$(RC_PREFIX).yaml.exhaustive.usage-report.tsv \
other-reports/mixs-ontology-mentions.tsv \
generated-schema/final-mixs_6_2_rc.yaml \
post-clean


pre-clean:
	rm -rf curated-data/unwrapped-curated-data-for-slot-coverage-check.yaml
	rm -rf extracted-data/unwrapped.mixs_6_2_rc.extracted-examples.yaml
	rm -rf schemasheets-usage-output/mixs_6_2_rc-concise-usage-for-text-mining.tsv

post-clean:
	date > other-reports/make-all-finished.txt
	rm -rf curated-data/unwrapped-curated-data-for-slot-coverage-check.yaml
	rm -rf extracted-data/unwrapped.mixs_6_2_rc.extracted-examples.yaml
	rm -rf schemasheets-usage-output/mixs_6_2_rc-concise-usage-for-text-mining.tsv

# might not want to automatically clean/delete slow-to generate ncbi-biosample-sql/results files
squeaky-clean: pre-clean
	@for dir in conflict-reports converted-data downloads extracted-data generated-schema GSC-excel-harmonized-repaired \
		mixs-docs-md other-reports schema-derivatives schemasheets-usage-output text-mining-results ; do \
		rm -rf $$dir/*; \
		mkdir -p $$dir; \
		touch $$dir/.gitkeep; \
	done
	rm -rf curated-data/unwrapped-curated-data-for-slot-coverage-check.yaml
	date > other-reports/make-all-started.txt

# 	 	 --combo-checklists MigsEu \
# 		 --combo-checklists MimarksS \
#  		 --combo-environments HostAssociated \
#  		 --combo-environments HumanGut \
# 		 --combo-environments PlantAssociated \
#  		 --combo-environments Water \
#  		 --combo-environments HumanAssociated \
#  		 --combo-environments HumanOral \

generated-schema/mixs_6_2_rc.yaml:
	$(RUN) write-mixs-linkml \
		 --gsc-excel-input 'https://github.com/only1chunts/mixs-cih-fork/raw/main/mixs/excel/mixs_v6.xlsx' \
		 --gsc-excel-output-dir downloads \
		 --combo-checklists MigsEu \
	 	 --combo-checklists Mims \
 		 --combo-checklists MimarksS \
 		 --combo-environments PlantAssociated \
  		 --combo-environments HostAssociated \
  		 --combo-environments HumanAssociated \
  		 --combo-environments HumanGut \
  		 --combo-environments HumanOral \
  		 --combo-environments Soil \
  		 --combo-environments Water \
		 --classes-ssheet config/build-test-only/schema-for-classes-schemasheet.tsv \
		 --classes-ssheet config/build-test-only/prefixes-for-classes-schemasheet.tsv \
		 --classes-ssheet config/classes-schemasheet.tsv \
		 --non-ascii-replacement ' ' \
		 --schema-name $(RC_PREFIX) \
		 --textual-key 'Structured comment name' \
		 --linkml-stage-mods-file config/linkml-stage-mixs-modifications.yaml \
		 --range-pattern-inference-file config/mixs-valsyns-expvals-to-linkml-ranges-patterns.tsv \
		 --tables-stage-mods-file config/mixs-tables-stage-modifications.tsv \
		 --harmonized-mixs-tables-file GSC-excel-harmonized-repaired/$(LEGACY_PREFIX).harmonized.tsv \
		 --repaired-mixs-tables-file GSC-excel-harmonized-repaired/$(RC_PREFIX).repaired.tsv \
		 --extracted-examples-out extracted-data/$(RC_PREFIX).extracted-examples.yaml \
		 --repair-report conflict-reports/conflict-repair-report.tsv \
		 --unmapped-report other-reports/un-handled-stringsers-expvals.tsv \
		 --schema-file-out $@
#	$(RUN)  vskit expand \
#		--schema $@.temp \
#		--output $@ FARM_EQUIP_ENUM PLANT_WATER_METHOD_ENUM FERTILIZER_ADMIN_ENUM
#	rm -rf $@.temp

generated-schema/mixs_6_2_rc.yaml.notated.yaml: text-mining-results/mixs-v6-repaired-term-title-token-matrix.tsv

# https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/63
text-mining-results/mixs-v6-repaired-term-title-token-matrix.tsv: config/curated-slot-notes-by-text-mining.tsv \
$(SOURCE_SCHEMA_PATH) schemasheets-usage-output/$(RC_PREFIX)-concise-usage-for-text-mining.tsv
	$(RUN) add-notes-from-text-mining \
		--dtm-input-slot title \
		--input-col-vals-file text-mining-results/mixs-v6-repaired-term-title-token-list.tsv \
		--input-dtm-notes-mapping $(word 1,$^) \
		--input-schema-file $(word 2,$^) \
		--input-usage-report $(word 3,$^) \
		--output-schema-file generated-schema/mixs_6_2_rc.yaml.notated.yaml \
		--dtm-output $@

other-reports/build-test-data-coverage-report.yaml: curated-data/unwrapped-curated-data-for-slot-coverage-check.yaml $(SOURCE_SCHEMA_PATH)
	poetry run exhaustion-check \
		--class-name "AllSlotsTestClass" \
		--instance-yaml-file $(word 1,$^) \
		--output-yaml-file $@ \
		--schema-path $(word 2,$^)

other-reports/extracted-data-coverage-report.yaml: extracted-data/unwrapped.$(RC_PREFIX).extracted-examples.yaml $(SOURCE_SCHEMA_PATH)
	poetry run exhaustion-check \
		--class-name "AllSlotsTestClass" \
		--instance-yaml-file $(word 1,$^) \
		--output-yaml-file $@ \
		--schema-path $(word 2,$^)

linkml-validate-build-test-only: $(SOURCE_SCHEMA_PATH) curated-data/build-test-only/AllSlotsTestClassCollection-wrapped-example-data.yaml
	$(RUN) linkml-validate --target-class AllSlotsTestClassCollection --schema $^

linkml-validate-extracted: $(SOURCE_SCHEMA_PATH) extracted-data/$(RC_PREFIX).extracted-examples.yaml
	$(RUN) linkml-validate --target-class AllSlotsTestClassCollection --schema $^

curated-data/unwrapped-curated-data-for-slot-coverage-check.yaml: curated-data/build-test-only/AllSlotsTestClassCollection-wrapped-example-data.yaml
	$(RUN) get-first-of-first \
		--input_data $< \
		--output_data $@.temp
	$(RUN) pretty-sort-yaml \
		-i $@.temp \
		-o $@
	rm -rf $@.temp

extracted-data/unwrapped.$(RC_PREFIX).extracted-examples.yaml: extracted-data/$(RC_PREFIX).extracted-examples.yaml
	$(RUN) get-first-of-first \
		--input_data $< \
		--output_data $@.temp
	$(RUN) pretty-sort-yaml \
		-i $@.temp \
		-o $@
	rm -rf $@.temp


# https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/62
schemasheets-usage-output/$(RC_PREFIX)-concise-usage-for-text-mining.tsv: $(SOURCE_SCHEMA_PATH)
	$(RUN) linkml2schemasheets-template \
		--debug-report-path other-reports/notated-populated-generated-debug-report.yaml \
		--log-file other-reports/populated-with-generated-spec-log.txt \
		--output-path $@.tmp \
		--report-style concise \
		--source-path $<
	grep -v -e '^>' $@.tmp > $@
	rm -rf $@.tmp

schemasheets-usage-output/$(RC_PREFIX).yaml.exhaustive.schemasheet.tsv: generated-schema/mixs_6_2_rc.yaml.notated.yaml
	$(RUN) linkml2schemasheets-template \
		--debug-report-path other-reports/notated-populated-generated-debug-report.yaml \
		--log-file other-reports/populated-with-generated-spec-log.txt \
		--output-path $@ \
		--report-style exhaustive \
		--source-path $<

schemasheets-usage-output/$(RC_PREFIX).yaml.exhaustive.usage-report.tsv: schemasheets-usage-output/$(RC_PREFIX).yaml.exhaustive.schemasheet.tsv
	grep -v -e '^>' $< > $@

schemasheets-usage-output/$(RC_PREFIX).yaml.concise.schemasheet.tsv: generated-schema/mixs_6_2_rc.yaml.notated.yaml
	$(RUN) linkml2schemasheets-template \
		--debug-report-path other-reports/notated-populated-generated-debug-report.yaml \
		--log-file other-reports/populated-with-generated-spec-log.txt \
		--output-path $@ \
		--report-style concise \
		--source-path $<

schemasheets-usage-output/$(RC_PREFIX).yaml.concise.usage-report.tsv: schemasheets-usage-output/$(RC_PREFIX).yaml.concise.schemasheet.tsv
	grep -v -e '^>' $< > $@


# # # #

conflicts-cleanup:
	rm -rf conflict-reports/$(RC_PREFIX)*conflicts*tsv

# generalize this
conflicts-all-reports: conflicts-cleanup \
conflict-reports/$(RC_PREFIX).SCN.Def.conflicts.pre.tsv \
conflict-reports/$(RC_PREFIX).SCN.Def.conflicts.post.tsv \
conflict-reports/$(RC_PREFIX).SCN.Example.conflicts.pre.tsv \
conflict-reports/$(RC_PREFIX).SCN.Example.conflicts.post.tsv \
conflict-reports/$(RC_PREFIX).SCN.expval.conflicts.pre.tsv \
conflict-reports/$(RC_PREFIX).SCN.expval.conflicts.post.tsv \
conflict-reports/$(RC_PREFIX).SCN.Item.conflicts.pre.tsv \
conflict-reports/$(RC_PREFIX).SCN.Item.conflicts.post.tsv \
conflict-reports/$(RC_PREFIX).SCN.Occurrence.conflicts.pre.tsv \
conflict-reports/$(RC_PREFIX).SCN.Occurrence.conflicts.post.tsv \
conflict-reports/$(RC_PREFIX).SCN.prefunit.conflicts.pre.tsv \
conflict-reports/$(RC_PREFIX).SCN.prefunit.conflicts.post.tsv \
conflict-reports/$(RC_PREFIX).SCN.Section.conflicts.pre.tsv \
conflict-reports/$(RC_PREFIX).SCN.Section.conflicts.post.tsv \
conflict-reports/$(RC_PREFIX).SCN.valsyn.conflicts.pre.tsv \
conflict-reports/$(RC_PREFIX).SCN.valsyn.conflicts.post.tsv \
conflict-reports/$(RC_PREFIX).SCN.ID.conflicts.pre.tsv \
conflict-reports/$(RC_PREFIX).SCN.ID.conflicts.post.tsv \
conflict-reports/$(RC_PREFIX).ID.SCN.conflicts.pre.tsv \
conflict-reports/$(RC_PREFIX).ID.SCN.conflicts.post.tsv \


#https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/66

conflict-reports/$(RC_PREFIX).SCN.ID.conflicts.pre.tsv: GSC-excel-harmonized-repaired/$(LEGACY_PREFIX).harmonized.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column 'MIXS ID' \
		--output-file $@

# can also run the conflict check on the repaired file
conflict-reports/$(RC_PREFIX).SCN.ID.conflicts.post.tsv: GSC-excel-harmonized-repaired/$(RC_PREFIX).repaired.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column 'MIXS ID' \
		--output-file $@


conflict-reports/$(RC_PREFIX).ID.SCN.conflicts.pre.tsv: GSC-excel-harmonized-repaired/$(LEGACY_PREFIX).harmonized.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Structured comment name' \
		--output-file $@

# can also run the conflict check on the repaired file
conflict-reports/$(RC_PREFIX).ID.SCN.conflicts.post.tsv: GSC-excel-harmonized-repaired/$(RC_PREFIX).repaired.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Structured comment name' \
		--output-file $@

# https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/64
conflict-reports/$(RC_PREFIX).SCN.Def.conflicts.pre.tsv: GSC-excel-harmonized-repaired/$(LEGACY_PREFIX).harmonized.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column 'Definition' \
		--output-file $@

conflict-reports/$(RC_PREFIX).SCN.Def.conflicts.post.tsv: GSC-excel-harmonized-repaired/$(RC_PREFIX).repaired.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column 'Definition' \
		--output-file $@


# https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/64
conflict-reports/$(RC_PREFIX).SCN.expval.conflicts.pre.tsv: GSC-excel-harmonized-repaired/$(LEGACY_PREFIX).harmonized.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column 'Expected value' \
		--output-file $@

conflict-reports/$(RC_PREFIX).SCN.expval.conflicts.post.tsv: GSC-excel-harmonized-repaired/$(RC_PREFIX).repaired.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column 'Expected value' \
		--output-file $@


conflict-reports/$(RC_PREFIX).SCN.Item.conflicts.pre.tsv: GSC-excel-harmonized-repaired/$(LEGACY_PREFIX).harmonized.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column 'Item' \
		--output-file $@

conflict-reports/$(RC_PREFIX).SCN.Item.conflicts.post.tsv: GSC-excel-harmonized-repaired/$(RC_PREFIX).repaired.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column 'Item' \
		--output-file $@


# https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/64
conflict-reports/$(RC_PREFIX).SCN.Occurrence.conflicts.pre.tsv: GSC-excel-harmonized-repaired/$(LEGACY_PREFIX).harmonized.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column 'Occurrence' \
		--output-file $@

conflict-reports/$(RC_PREFIX).SCN.Occurrence.conflicts.post.tsv: GSC-excel-harmonized-repaired/$(RC_PREFIX).repaired.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column 'Occurrence' \
		--output-file $@


conflict-reports/$(RC_PREFIX).SCN.prefunit.conflicts.pre.tsv: GSC-excel-harmonized-repaired/$(LEGACY_PREFIX).harmonized.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column 'Preferred unit' \
		--output-file $@

conflict-reports/$(RC_PREFIX).SCN.prefunit.conflicts.post.tsv: GSC-excel-harmonized-repaired/$(RC_PREFIX).repaired.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column 'Preferred unit' \
		--output-file $@


conflict-reports/$(RC_PREFIX).SCN.Section.conflicts.pre.tsv: GSC-excel-harmonized-repaired/$(LEGACY_PREFIX).harmonized.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column 'Section' \
		--output-file $@

conflict-reports/$(RC_PREFIX).SCN.Section.conflicts.post.tsv: GSC-excel-harmonized-repaired/$(RC_PREFIX).repaired.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column 'Section' \
		--output-file $@


conflict-reports/$(RC_PREFIX).SCN.valsyn.conflicts.pre.tsv: GSC-excel-harmonized-repaired/$(LEGACY_PREFIX).harmonized.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column 'Value syntax' \
		--output-file $@

conflict-reports/$(RC_PREFIX).SCN.valsyn.conflicts.post.tsv: GSC-excel-harmonized-repaired/$(RC_PREFIX).repaired.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column 'Value syntax' \
		--output-file $@


conflict-reports/$(RC_PREFIX).SCN.Example.conflicts.pre.tsv: GSC-excel-harmonized-repaired/$(LEGACY_PREFIX).harmonized.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column Example \
		--output-file $@

conflict-reports/$(RC_PREFIX).SCN.Example.conflicts.post.tsv: GSC-excel-harmonized-repaired/$(RC_PREFIX).repaired.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column Example \
		--output-file $@

# # # #

# todo how to communicate/save download date?
ncbi-biosample-sql/results/minimal.csv: ncbi-biosample-sql/queries/minimal.sql
	# ~ 5 minutes
	date
	psql --csv \
		-U $(BIOSAMPLE_DB_USER) \
		-h $(BIOSAMPLE_DB_HOST) -p $(BIOSAMPLE_DB_PORT) \
		-d $(BIOSAMPLE_DB_DB_NAME) \
		-f $< > $@
	date

ncbi-biosample-sql/results/ncbi-biosample-harmonized-attribute-usage.csv: ncbi-biosample-sql/queries/harmonized-name-usage-counts.sql
	# ~ 5 minutes
	date
	psql --csv \
		-U $(BIOSAMPLE_DB_USER) \
		-h $(BIOSAMPLE_DB_HOST) -p $(BIOSAMPLE_DB_PORT) \
		-d $(BIOSAMPLE_DB_DB_NAME) \
		-f $< > $@
	date

GSC-excel-harmonized-repaired/$(LEGACY_PREFIX).harmonized.tsv: $(SOURCE_SCHEMA_PATH)

# note one TSV and one CSV
other-reports/mixs-scns-vs-ncbi-harmonized-attributes.yaml: GSC-excel-harmonized-repaired/$(LEGACY_PREFIX).harmonized.tsv \
ncbi-biosample-sql/results/ncbi-biosample-harmonized-attribute-usage.csv
	$(RUN) mixs-scns-vs-ncbi-harmonized-attributes \
		--mixs-scns-file $(word 1,$^) \
		--ncbi-harmonized-names-file $(word 2,$^) \
		--output-file $@

# gen-owl isn't honoring --output any more?
schema-derivatives/$(RC_PREFIX).owl.ttl: $(SOURCE_SCHEMA_PATH)
	$(RUN) gen-owl \
		--output $@ \
		--format ttl \
		--metadata-profile rdfs $< > $@

schema-derivatives/$(RC_PREFIX).schema.json: $(SOURCE_SCHEMA_PATH)
	$(RUN) gen-json-schema --closed $< > $@

# --materialize-patterns
# --materialize-attributes / --no-materialize-attributes
schema-derivatives/$(RC_PREFIX).json: $(SOURCE_SCHEMA_PATH)
	$(RUN) gen-linkml \
		--materialize-patterns \
		--materialize-attributes \
		--output $@ $<
	cp $@ data_harmonizer/schemas

generated-schema/final-mixs_6_2_rc.yaml: generated-schema/mixs_6_2_rc.yaml.notated.yaml
	$(RUN) remove-elements-by-deprecation-val \
		--input-schema $< \
		--deprecation-val "for build-time testing of all slots" \
		--output-schema $@
	rm -rf $<
	mv $@ $(SOURCE_SCHEMA_PATH)

.PHONY: validate-multiple-mims-soil

validate-multiple-mims-soil: $(SOURCE_SCHEMA_PATH) curated-data/valid/MixsCompliantData-MimsSoil-example.yaml
	$(RUN) linkml-validate \
		--schema $^

converted-data/data-conversion-report.md: $(SOURCE_SCHEMA_PATH) curated-data/valid curated-data/invalid
	$(RUN) linkml-run-examples \
		--schema $(word 1,$^) \
		--input-directory  $(word 2,$^) \
		--output-directory converted-data \
		--counter-example-input-directory $(word 3,$^) \
		--output $@

## linkml-run-examples does not handle XSV conversion
converted-data/MimsSoil-example.tsv: $(SOURCE_SCHEMA_PATH) curated-data/valid/MixsCompliantData-MimsSoil-example.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--target-class MixsCompliantData \
		--index-slot mims_soil_data \
		--schema $^

$(DOCDIR):
	mkdir -p $@

gendoc: $(DOCDIR)
#	# copying of images and static content
#	cp $(SRC)/docs/*md $(DOCDIR) ; \
#	cp -r $(SRC)/docs/images $(DOCDIR) ;
	$(RUN) gen-doc -d $(DOCDIR) --template-directory $(TEMPLATEDIR)  --use-slot-uris $(SOURCE_SCHEMA_PATH)
	#mv $(DOCDIR)/TEMP.md $(DOCDIR)/temp.md

MKDOCS = $(RUN) mkdocs
mkd-%:
	$(MKDOCS) $*

testdoc: gendoc serve

# Test documentation locally
serve: mkd-serve

# Test data harmonizer locally
dh-dev: schema-derivatives/$(RC_PREFIX).json
	cd data_harmonizer && npm run dev

# GH pages deployment including data harmonizer is handled by .github/workflows/deploy-docs.yaml

# some mkdocs commands create a site directory
#  which is gitignored
# so removed unnecessary mixs-docs-html

other-reports/slot-usage-report.tsv:
	$(RUN) usage-detector \
		--ignore-attributes 'annotations' \
		--ignore-attributes 'examples' \
		--ignore-attributes 'name' \
		--ignore-attributes 'recommended' \
		--ignore-attributes 'required' \
		--ignore-attributes string_serialization \
		--report-tsv-file $@ \
		--schema-file $(SOURCE_SCHEMA_PATH)

other-reports/schema-lint-report.tsv: $(SOURCE_SCHEMA_PATH)
	- $(RUN) linkml-lint --format tsv \
		--output $@ $<

converted-data/MixsCompliantData-MimsSoil-example.ttl: converted-data/data-conversion-report.md

.PHONY: validate-linkml-rdf-data-pure-python validate-linkml-rdf-schema-pure-python
validate-linkml-rdf-data-pure-python: converted-data/MixsCompliantData-MimsSoil-example.ttl
	$(RUN) rdflib-validation \
		--rdf-file $<

validate-linkml-rdf-schema-pure-python: schema-derivatives/mixs_6_2_rc.owl.ttl
	$(RUN) rdflib-validation \
		--rdf-file  $<
		
data_harmonizer/menu.json: $(SOURCE_SCHEMA_PATH)
	$(RUN) regenerate-data-harmonizer-menu \
		--schema-input-file $< \
		--menu-json-out $@

GSC-excel-harmonized-repaired/mixs_6_2_rc.repaired.tsv: generated-schema/mixs_6_2_rc.yaml

other-reports/mixs-ontology-mentions.tsv: GSC-excel-harmonized-repaired/mixs_6_2_rc.repaired.tsv
	$(RUN) find-ontology-mentions \
		--ignored-ontology CRO \
		--ignored-ontology EPIO \
		--ignored-ontology EV \
		--ignored-ontology FAO \
		--ignored-ontology MA \
		--ignored-ontology MI \
		--ignored-ontology MP \
		--ignored-ontology MS \
		--ignored-ontology PR \
		--ignored-ontology RO \
		--ignored-ontology SO \
		--ignored-ontology TO \
		--ignored-ontology VO \
		--mixs-tsv $< \
		--obo-yaml-url "https://obofoundry.org/registry/ontologies.yml" \
		--results-tsv $@

### targets below are not included in make all

schema-derivatives/mixs_6_2_rc.schema.open.json: $(SOURCE_SCHEMA_PATH)
	$(RUN) gen-json-schema $< > $@

schema-derivatives/mixs_6_2_rc.form.xlsx: $(SOURCE_SCHEMA_PATH)
	$(RUN) gen-excel --output $@ $<

# requires Jena riot
RIOT_PATH = ~/apache-jena/bin/riot
validate_rdf_data: converted-data/MixsCompliantData-MimsSoil-example.ttl
	$(RIOT_PATH) --validate $<

validate_rdf_schema: schema-derivatives/mixs_6_2_rc.owl.ttl
	$(RIOT_PATH) --validate $<

# for https://github.com/microbiomedata/mixs-6-2-release-candidate/issues/186
converted-data/MimsSoil-example.ttl: $(SOURCE_SCHEMA_PATH) curated-data/valid/MixsCompliantData-MimsSoil-example.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--target-class MixsCompliantData \
		--index-slot mims_soil_data \
		--schema $^