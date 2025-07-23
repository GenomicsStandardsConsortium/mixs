## Add your own custom Makefile targets here

RUN=poetry run

assets/mixs_derived_class_term_schemasheet.tsv: src/mixs/schema/mixs.yaml
	mkdir -p assets
	$(RUN) linkml2schemasheets-template \
		--source-path $< \
		--output-path $@ \
		--debug-report-path assets/mixs_derived_class_term_schemasheet_debug.txt \
		--log-file assets/mixs_derived_class_term_schemasheet_log.txt \
		--report-style concise

assets/required_and_recommended_slot_usages.tsv: src/mixs/schema/mixs.yaml
	mkdir -p assets
	$(RUN) python src/scripts/required_supersedes_recommended.py \
		--input-schema $< \
		--output $@

assets/extensions-dendrogram.pdf:
	mkdir -p assets
	$(RUN) extension-distances \
		--schema src/mixs/schema/mixs.yaml \
		--output $@

assets/soil-vs-water-slot-usage.yaml: src/mixs/schema/mixs.yaml
	mkdir -p assets
	$(RUN) extension-differences \
		--schema $< \
		--ext1 Soil \
		--ext2 Water > $@

assets/class_summary_results.tsv: src/mixs/schema/mixs.yaml assets/templates/class_summary_template.tsv
	mkdir -p assets
	$(RUN) linkml2sheets \
		--schema $(word 1,$^) \
		 --output $@ $(word 2,$^)

assets/mixs-schemasheets-concise.tsv: src/mixs/schema/mixs.yaml
	mkdir -p assets
	$(RUN) linkml2schemasheets-template \
		--source-path $< \
		--output-path $@ \
		--debug-report-path assets/mixs-schemasheets-concise-report.txt \
		--log-file assets/mixs-schemasheets-concise-log.txt \
		--report-style concise

assets/mixs-schemasheets-concise-global-slots.tsv: assets/mixs-schemasheets-concise.tsv
	$(RUN) python src/scripts/isolate_slots.py
