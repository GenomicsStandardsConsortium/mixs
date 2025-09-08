## Add your own custom Makefile targets here

RUN=poetry run

contrib/mixs_derived_class_term_schemasheet.tsv: src/mixs/schema/mixs.yaml
	mkdir -p contrib
	$(RUN) linkml2schemasheets-template \
		--source-path $< \
		--output-path $@ \
		--debug-report-path contrib/mixs_derived_class_term_schemasheet_debug.txt \
		--log-file contrib/mixs_derived_class_term_schemasheet_log.txt \
		--report-style concise

contrib/required_and_recommended_slot_usages.tsv: src/mixs/schema/mixs.yaml
	mkdir -p contrib
	$(RUN) required-supersedes-recommended \
		--input-schema $< \
		--output $@

contrib/extensions-dendrogram.pdf:
	mkdir -p contrib
	$(RUN) extension-distances \
		--schema src/mixs/schema/mixs.yaml \
		--output $@

contrib/soil-vs-water-slot-usage.yaml: src/mixs/schema/mixs.yaml
	mkdir -p contrib
	$(RUN) extension-differences \
		--schema $< \
		--ext1 Soil \
		--ext2 Water > $@

contrib/class_summary_results.tsv: src/mixs/schema/mixs.yaml contrib/templates/class_summary_template.tsv
	mkdir -p contrib
	$(RUN) linkml2sheets \
		--schema $(word 1,$^) \
		 --output $@ $(word 2,$^)

contrib/mixs-schemasheets-concise.tsv: src/mixs/schema/mixs.yaml
	mkdir -p contrib
	$(RUN) linkml2schemasheets-template \
		--source-path $< \
		--output-path $@ \
		--debug-report-path contrib/mixs-schemasheets-concise-report.txt \
		--log-file contrib/mixs-schemasheets-concise-log.txt \
		--report-style concise

contrib/mixs-schemasheets-concise-global-slots.tsv: contrib/mixs-schemasheets-concise.tsv
	$(RUN) isolate-global-slots --source-file $< --output-file $@
