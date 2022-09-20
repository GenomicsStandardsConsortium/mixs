DIR_CREATION_MSG="this file forces the creation of the parent directory"
RUN=poetry run

.PHONY: clean_schemasheets all_schemasheets

all_schemasheets: clean_schemasheets schemasheets/example_data/out/mims_data.json

clean_schemasheets:
	rm -rf schemasheets/example_data/out/mims_data.json
	rm -rf schemasheets/lint_log.tsv
	rm -rf schemasheets/tsv_output/classes.tsv
	rm -rf schemasheets/tsv_output/slots.tsv
	rm -rf schemasheets/yaml_output/classes_roundtrip.yaml
	rm -rf schemasheets/yaml_output/mixs_from_schema_sheets.yaml
	rm -rf schemasheets/yaml_output/mixs_from_schema_sheets_generated.yaml
	rm -rf schemasheets/yaml_output/mixs_reference_generated.yaml
	rm -rf schemasheets/yaml_output/mixs_reference_merged.yaml
	rm -rf schemasheets/yaml_output/reference_classes_only.yaml
	rm -rf schemasheets/yaml_output/reference_slots_only.yaml
	rm -rf schemasheets/yaml_output/reference_slots_only_generated.yaml
	rm -rf schemasheets/yaml_output/slots_roundtrip.yaml
	mkdir -p schemasheets/yaml_output
	echo $(DIR_CREATION_MSG) > schemasheets/yaml_output/README.md
	mkdir -p schemasheets/example_data/out
	echo $(DIR_CREATION_MSG) > schemasheets/example_data/out/README.md
	mkdir -p schemasheets/tsv_output
	echo $(DIR_CREATION_MSG) > schemasheets/tsv_output/README.md

# skipping enums.tsv schema_settings.tsv subsets.tsv packages_slots_used_by_soil.tsv packages_soil_slot_usage.tsv

# problematics package slots

  # assembly_software	assembly softwar	MIXS:0000056
  #    conflicts with assembly_qual MIXS:0000056 from core sheet
  # nose_throat_disord	nose/mouth/teeth/throat disorder	MIXS:0000283
  # host_sex	host sex	MIXS:0000811
  # host_body_product	host body product	MIXS:0000888
  # soil_horizon	soil horizon	MIXS:0001082	horizon|horizon
  # host_symbiont	observed host symbionts	MIXS:0001298

# todo work on settings and structured patterns (gen-linkml expansion)

schemasheets/yaml_output/mixs_from_schema_sheets.yaml: \
schemasheets/tsv_input/checklist_classes.tsv \
schemasheets/tsv_input/combination_classes.tsv \
schemasheets/tsv_input/core.tsv \
schemasheets/tsv_input/core_enums.tsv \
schemasheets/tsv_input/env_package_classes.tsv \
schemasheets/tsv_input/package_slot_usage.tsv \
schemasheets/tsv_input/package_slots.tsv \
schemasheets/tsv_input/prefixes.tsv \
schemasheets/tsv_input/schema.tsv \
schemasheets/tsv_input/utility_classes.tsv \
schemasheets/tsv_input/utility_slots.tsv
	$(RUN) sheets2linkml --output $@ $^


# --materialize-patterns / --no-materialize-patterns
schemasheets/yaml_output/mixs_from_schema_sheets_generated.yaml: schemasheets/yaml_output/mixs_from_schema_sheets.yaml
	$(RUN) gen-linkml \
		--format yaml \
		--no-materialize-attributes $^ | \
		yq 'del(.. | select(has("from_schema")).from_schema)' | \
		yq 'del(.. | select(has("source_file")).source_file)' | \
		yq '(... | select(type == "!!seq")) |= unique' > $@

schemasheets/yaml_output/mixs_reference_merged.yaml: model/schema/mixs.yaml
	$(RUN) python gsctools/merge_view.py \
		--input_schema $< \
		--output $@

# todo gen-linkml not merging imports
# Error: sort only works for scalars, got !!map
# todo try deepdiff again for list order insensitivity, or sort and otherwise repair with python code
schemasheets/yaml_output/mixs_reference_generated.yaml: schemasheets/yaml_output/mixs_reference_merged.yaml
	$(RUN) gen-linkml \
		--format yaml \
		--mergeimports \
		--no-materialize-attributes $< | \
		yq 'del(.. | select(has("from_schema")).from_schema)' | \
		yq 'del(.. | select(has("source_file")).source_file)' | \
		yq '(... | select(type == "!!seq")) |= unique' > $@

# --fix / --no-fix
# see https://github.com/linkml/linkml/blob/main/linkml/linter/config/default.yaml
schemasheets/lint_log.tsv: schemasheets/yaml_output/mixs_from_schema_sheets.yaml
	$(RUN) linkml-lint --config schemasheets/linter_config_default.yaml --format tsv --output $@ $<

schema_diff: schemasheets/yaml_output/mixs_reference_generated.yaml schemasheets/yaml_output/mixs_from_schema_sheets.yaml
	- jd --yaml $^

schemasheets/example_data/out/mims_data.json: schemasheets/example_data/in/soil_mims_data.yaml schemasheets/yaml_output/mixs_from_schema_sheets.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--schema $(word 2,$^) \
		--target-class SoilMims \
		$<

schemasheets/tsv_output/classes.tsv: schemasheets/yaml_output/mixs_from_schema_sheets.yaml
	$(RUN) linkml2sheets \
		--schema $< \
		--output-directory schemasheets/tsv_output schemasheets/templates/classes.tsv

#
#schemasheets/tsv_output/slots.tsv: model/schema/mixs.yaml
#	$(RUN) linkml2sheets \
#		--schema $< \
#		--output-directory schemasheets/tsv_output schemasheets/templates/slots.tsv
#
#schemasheets/yaml_output/classes_roundtrip.yaml: \
#schemasheets/tsv_input/prefixes.tsv \
#schemasheets/tsv_input/schema.tsv \
#schemasheets/tsv_output/classes.tsv
#	$(RUN) sheets2linkml $^ | \
#	yq 'del(.. | select(has("from_schema")).from_schema)' | \
#	yq 'del(.. | select(has("source_file")).source_file)' | \
#	yq '(... | select(type == "!!seq")) |= unique' > $@
#
#schemasheets/yaml_output/slots_roundtrip.yaml: \
#schemasheets/tsv_input/prefixes.tsv \
#schemasheets/tsv_input/schema.tsv \
#schemasheets/tsv_output/slots.tsv
#	$(RUN) sheets2linkml $^ | \
#	yq '(... | select(type == "!!seq")) |= unique' | \
#	yq '.slots | to_entries | map(select(.value.examples[].value != "")) | map(select(.value.examples | length >0)) | from_entries ' | \
#	yq 'del(.. | select(has("from_schema")).from_schema)' | \
#	yq 'del(.. | select(has("source_file")).source_file)' | \
#	egrep -v 'comments: \[\]' | egrep -v ': false' > $@
#
#schemasheets/yaml_output/reference_classes_only.yaml:
#	$(RUN) python gsctools/classes_only.py | \
#	yq 'del(.. | select(has("from_schema")).from_schema)' | \
#	yq 'del(.. | select(has("source_file")).source_file)' | \
#	yq '(... | select(type == "!!seq")) |= unique' > $@
#
#
#schemasheets/yaml_output/reference_slots_only.yaml:
#	$(RUN) python gsctools/slots_only.py > $@
#
## add annotations and structured_pattern
#
#schemasheets/yaml_output/reference_slots_only_generated.yaml: schemasheets/yaml_output/reference_slots_only.yaml
#	$(RUN) gen-linkml \
#		--format yaml \
#		--mergeimports \
#		--no-materialize-attributes $< | \
#	yq '(... | select(type == "!!seq")) |= unique' | \
#	yq '.slots | to_entries | map(select(.value.examples[].value != "")) | map(select(.value.examples | length >0)) | from_entries ' | \
#	yq 'del(.. | select(has("from_schema")).from_schema)' | \
#	yq 'del(.. | select(has("source_file")).source_file)' | \
#	egrep -v 'comments: \[\]' | egrep -v ': false' > $@
#
#
#classes_diff: schemasheets/yaml_output/reference_classes_only.yaml schemasheets/yaml_output/classes_roundtrip.yaml
#	- jd --yaml $^
#
#slots_diff: schemasheets/yaml_output/reference_slots_only_generated.yaml schemasheets/yaml_output/slots_roundtrip.yaml
#	- jd --yaml $^

