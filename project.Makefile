## Add your own custom Makefile targets here
#
## we won't need to rerun this once we agree that we are done with bulk updating
#src/mixs_6_2_for_merge/schema/mixs_6_2_for_merge.yaml:
#	curl https://raw.githubusercontent.com/GenomicsStandardsConsortium/mixs6.2_release_candidate/main/generated-schema/mixs_6_2_rc.yaml > $@

RUN=poetry run

assets/mixs_derived_class_term_schemasheet.tsv: src/mixs/schema/mixs.yaml
	$(RUN) linkml2schemasheets-template \
		--source-path $< \
		--output-path $@ \
		--debug-report-path assets/mixs_derived_class_term_schemasheet_debug.txt \
		--log-file assets/mixs_derived_class_term_schemasheet_log.txt \
		--report-style concise