DIR_CREATION_MSG="this file forces the creation of the parent directory"
RUN=poetry run

.PHONY: clean_schemasheets all_schemasheets

all_schemasheets: clean_schemasheets schemasheets/yaml_output/mixs_6_2_test_generated.yaml

clean_schemasheets:
	rm -rf schemasheets/yaml_output/*
	mkdir -p schemasheets/yaml_output
	echo $(DIR_CREATION_MSG) > schemasheets/yaml_output/README.md

schemasheets/yaml_output/mixs_6_2_test.yaml: schemasheets/tsv_input/schema.tsv schemasheets/tsv_input/prefixes.tsv \
schemasheets/tsv_input/checklist_classes.tsv schemasheets/tsv_input/env_package_classes.tsv schemasheets/tsv_input/utility_classes.tsv \
schemasheets/tsv_input/sections_as_parent_slots.tsv \
schemasheets/tsv_input/core.tsv \
schemasheets/tsv_input/class_slot_assignments.tsv
	#schemasheets/tsv_input/*tsv
	# todo only one yaml output per sheets2linkml run
	# --unique-slots / --no-unique-slots
	# --repair / --no-repair
	$(RUN) sheets2linkml \
		--output $@ $^

schemasheets/yaml_output/mixs_6_2_test_generated.yaml: schemasheets/yaml_output/mixs_6_2_test.yaml
	$(RUN) gen-linkml --format yaml --output $@ $<



