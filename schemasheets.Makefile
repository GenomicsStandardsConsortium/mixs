DIR_CREATION_MSG="this file forces the creation of the parent directory"
RUN=poetry run

.PHONY: clean_schemasheets all_schemasheets

all_schemasheets: clean_schemasheets schemasheets/example_data/out/mims_data.json

clean_schemasheets:
	rm -rf schemasheets/example_data/out/mims_data.json
	rm -rf schemasheets/yaml_output/mixs_from_schema_sheets.yaml
	mkdir -p schemasheets/yaml_output
	echo $(DIR_CREATION_MSG) > schemasheets/yaml_output/README.md
	mkdir -p schemasheets/example_data/out
	echo $(DIR_CREATION_MSG) > schemasheets/example_data/out/README.md

schemasheets/yaml_output/mixs_from_schema_sheets.yaml: \
schemasheets/tsv_input/checklist_classes.tsv \
schemasheets/tsv_input/core.tsv \
schemasheets/tsv_input/core_enums.tsv \
schemasheets/tsv_input/env_package_classes.tsv \
schemasheets/tsv_input/prefixes.tsv \
schemasheets/tsv_input/schema.tsv \
schemasheets/tsv_input/utility_classes.tsv \
schemasheets/tsv_input/utility_slots.tsv \
schemasheets/tsv_input/packages_slots_used_by_soil.tsv \
schemasheets/tsv_input/packages_soil_slot_usage.tsv
	$(RUN) sheets2linkml --output $@ $^

schemasheets/example_data/out/mims_data.json: schemasheets/example_data/in/soil_mims_data.yaml schemasheets/yaml_output/mixs_from_schema_sheets.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--schema $(word 2,$^) \
		--target-class SoilMims \
		$<

# todo work on settings and structured patterns (gen-linkml expansion)