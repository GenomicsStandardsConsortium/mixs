## Add your own custom Makefile targets here
#
## we won't need to rerun this once we agree that we are done with bulk updating
#src/mixs_6_2_for_merge/schema/mixs_6_2_for_merge.yaml:
#	curl https://raw.githubusercontent.com/GenomicsStandardsConsortium/mixs6.2_release_candidate/main/generated-schema/mixs_6_2_rc.yaml > $@

RUN=poetry run

gen-excel: $(SOURCE_SCHEMA_PATH)
	$(RUN) gen-excel $< \
		--include-mixins \
		--split-workbook-by-class \
		--output $(DEST)/excel
	mkdir -p $(EXCEL_TEMPLATES_DIR)
	$(RUN) python src/scripts/organize_excel_files.py \
		--mixs-schema-file $< \
		--source-directory $(DEST)/excel \
		--base-destination-folder $(EXCEL_TEMPLATES_DIR)

assets/mixs_derived_class_term_schemasheet.tsv: src/mixs/schema/mixs.yaml
	$(RUN) linkml2schemasheets-template \
		--source-path $< \
		--output-path $@ \
		--debug-report-path assets/mixs_derived_class_term_schemasheet_debug.txt \
		--log-file assets/mixs_derived_class_term_schemasheet_log.txt \
		--report-style concise

extensions-dendrogram.pdf:
	$(RUN) extension-distances \
		--schema src/mixs/schema/mixs.yaml \
		--output $@


soil-vs-water-slot-usage.yaml: src/mixs/schema/mixs.yaml
	$(RUN) extension-differences \
		--schema $< \
		--ext1 Soil \
		--ext2 Water > $@

assets/class_summary_results.tsv: src/mixs/schema/mixs.yaml assets/class_summary_template.tsv
	$(RUN) linkml2sheets \
		--schema $(word 1,$^) \
		 --output $@ $(word 2,$^)

assets/mixs-schemasheets-concise.tsv: src/mixs/schema/mixs.yaml
	$(RUN) linkml2schemasheets-template \
		--source-path $< \
		--output-path $@ \
		--debug-report-path assets/mixs-schemasheets-concise-report.txt \
		--log-file assets/mixs-schemasheets-concise-log.txt \
		--report-style concise

assets/mixs-patterns-materialized.yaml: src/mixs/schema/mixs.yaml
	$(RUN) gen-linkml \
		--format yaml \
		--materialize-patterns \
		--no-materialize-attributes $< > $@

assets/mixs-schemasheets-concise-global-slots.tsv: assets/mixs-schemasheets-concise.tsv
	$(RUN) python src/scripts/isolate_slots.py
