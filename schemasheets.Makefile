DIR_CREATION_MSG="this file forces the creation of the parent directory"
RUN=poetry run

.PHONY: clean_schemasheets all_schemasheets

all_schemasheets: clean_schemasheets schemasheets/yaml_output/mixs_6_2_test_generated.yaml

clean_schemasheets:
	rm -rf schemasheets/yaml_output/*
	mkdir -p schemasheets/yaml_output
	echo $(DIR_CREATION_MSG) > schemasheets/yaml_output/README.md
	rm -rf schemasheets/test_mims_data.yaml
	rm -rf schemasheets/test_schema_generated.yaml

schemasheets/yaml_output/mixs_6_2_test.yaml: schemasheets/tsv_input/schema.tsv schemasheets/tsv_input/prefixes.tsv \
schemasheets/tsv_input/checklist_classes.tsv schemasheets/tsv_input/env_package_classes.tsv schemasheets/tsv_input/utility_classes.tsv \
schemasheets/tsv_input/sections_as_parent_slots.tsv schemasheets/tsv_input/utility_slots.tsv \
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

# simpler testing:

.PHONY: clean_simpler simpler_testing

clean_simpler:
	rm -rf schemasheets/simple_test/target/*
	mkdir -p schemasheets/simple_test/target
	echo $(DIR_CREATION_MSG) > schemasheets/simple_test/target/README.md

simpler_testing: clean_simpler schemasheets/simple_test/target/test_mims_data.yaml schemasheets/simple_test/target/test_invalid_mims_data.csv

schemasheets/simple_test/target/simple_test.yaml: schemasheets/simple_test/tsv_input/*.tsv
	$(RUN) sheets2linkml \
		--no-repair \
		--unique-slots \
		--verbose \
		--output $@ $^

schemasheets/simple_test/target/simple_test_generated.yaml: schemasheets/simple_test/target/simple_test.yaml
	$(RUN) gen-linkml \
		--format yaml \
		--verbose \
		--no-materialize-attributes \
		--output $@ $<

schemasheets/simple_test/target/test_mims_data.yaml: schemasheets/simple_test/data/test_mims_data.tsv schemasheets/simple_test/target/simple_test_generated.yaml
	$(RUN) linkml-convert \
		--output $@ --schema $(word 2,$^) \
		--target-class Database \
		--index-slot mims_set $<

schemasheets/simple_test/target/test_invalid_mims_data.csv: schemasheets/simple_test/data/test_invalid_mims_data.yaml schemasheets/simple_test/target/simple_test_generated.yaml
	! $(RUN) linkml-convert \
		--output $@ --schema $(word 2,$^) \
		--target-class Database \
		--index-slot mims_set $<
	@echo "Make rule will progress only if previous recipe fails."

