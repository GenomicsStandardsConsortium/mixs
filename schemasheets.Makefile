DIR_CREATION_MSG="this file forces the creation of the parent directory"
RUN=poetry run

.PHONY: clean_schemasheets all_schemasheets

all_schemasheets: clean_schemasheets schemasheets/yaml_output/mixs_6_2_test_generated.yaml

clean_schemasheets:
	rm -rf schemasheets/yaml_output/*
	mkdir -p schemasheets/yaml_output
	echo $(DIR_CREATION_MSG) > schemasheets/yaml_output/README.md

schemasheets/yaml_output/mixs_6_2_test.yaml: \
schemasheets/tsv_input/*tsv
	# todo only one yaml output per sheets2linkml run
	# --unique-slots / --no-unique-slots
	# --repair / --no-repair
	$(RUN) sheets2linkml \
		--output $@ \
		--name mixs_6_2_core_test \
		$^

schemasheets/yaml_output/mixs_6_2_test_generated.yaml: schemasheets/yaml_output/mixs_6_2_test.yaml
	$(RUN) gen-linkml --format yaml --output $@ $<



