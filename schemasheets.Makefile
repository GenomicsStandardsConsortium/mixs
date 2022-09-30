DIR_CREATION_MSG="this file forces the creation of the parent directory"
RUN=poetry run

.PHONY: clean_schemasheets all_schemasheets

all_schemasheets: \
clean_schemasheets \
schemasheets/yaml_output/mixs_from_schema_sheets.yaml \
schemasheets/lint_log.tsv \
schemasheets/generated/mixs_from_schema_sheets_generated.yaml \
schemasheets/generated/jsonschema/mixs_from_schema_sheets.schema.json \
schemasheets/example_data/out/mims_soil_data.json

clean_schemasheets:
	rm -rf schemasheets/example_data/out/mims_data.json
	rm -rf schemasheets/lint_log.tsv
	rm -rf schemasheets/mixs_reference_no_empty_slot_examples.yaml
	rm -rf schemasheets/mixs_reference_no_explicit_falses.yaml
	rm -rf schemasheets/tsv_output/classes.tsv
	rm -rf schemasheets/tsv_output/slots.tsv
	rm -rf schemasheets/yaml_output/classes_roundtrip.yaml
	rm -rf schemasheets/yaml_output/mixs_from_schema_sheets.yaml
	rm -rf schemasheets/yaml_output/mixs_from_schema_sheets_generated.yaml
	rm -rf schemasheets/yaml_output/mixs_reference_generated.yaml
	rm -rf schemasheets/yaml_output/mixs_reference_merged.yaml
	rm -rf schemasheets/yaml_output/mixs_reference_no_empty_slot_examples.yaml
	rm -rf schemasheets/yaml_output/mixs_reference_no_explicit_falses.yaml
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

# partial list of problematics package slots

  # assembly_software	assembly softwar	MIXS:0000056
  #    conflicts with assembly_qual MIXS:0000056 from core sheet
  # nose_throat_disord	nose/mouth/teeth/throat disorder	MIXS:0000283
  # host_sex	host sex	MIXS:0000811
  # host_body_product	host body product	MIXS:0000888
  # soil_horizon	soil horizon	MIXS:0001082	horizon|horizon
  # host_symbiont	observed host symbionts	MIXS:0001298

# todo work on settings and structured patterns (gen-linkml expansion)

convenience: clean_schemasheets

schemasheets/yaml_output/mixs_from_schema_sheets.yaml: \
schemasheets/tsv_input/database_support/database_classes.tsv \
schemasheets/tsv_input/database_support/database_slots.tsv \
schemasheets/tsv_input/generated/combination_classes.tsv \
schemasheets/tsv_input/mixs_converter_inspired_additionals/checklist_classes.tsv \
schemasheets/tsv_input/mixs_converter_inspired_additionals/env_package_classes.tsv \
schemasheets/tsv_input/mixs_converter_inspired_additionals/prefixes.tsv \
schemasheets/tsv_input/mixs_converter_inspired_additionals/schema.tsv \
schemasheets/tsv_input/mixs_converter_inspired_additionals/subsets.tsv \
schemasheets/tsv_input/mixs_converter_inspired_additionals/utility_classes.tsv \
schemasheets/tsv_input/original_with_ss_headers/MIxS_6_term_updates_MIxS6_Core-Final_clean.tsv \
schemasheets/tsv_input/original_with_ss_headers/MIxS_6_term_updates_MIxS6_packages-Final_clean.tsv \
schemasheets/tsv_input/structured_pattern_support/schema_settings.tsv
	$(RUN) sheets2linkml --output $@ $^

# --fix / --no-fix
# see https://github.com/linkml/linkml/blob/main/linkml/linter/config/default.yaml
schemasheets/lint_log.tsv: schemasheets/yaml_output/mixs_from_schema_sheets.yaml
	$(RUN) linkml-lint --config schemasheets/linter_config_default.yaml --format tsv --output $@ $<

schemasheets/generated/mixs_from_schema_sheets_generated.yaml: \
schemasheets/yaml_output/mixs_from_schema_sheets.yaml
	$(RUN) gen-linkml \
		--format yaml \
		--no-materialize-attributes $^ > $@

schemasheets/generated/jsonschema/mixs_from_schema_sheets.schema.json: \
schemasheets/yaml_output/mixs_from_schema_sheets.yaml
	$(RUN) gen-project --dir schemasheets/generated $<


schemasheets/example_data/out/mims_soil_data.json: \
schemasheets/example_data/in/mims_soil_data.yaml \
schemasheets/yaml_output/mixs_from_schema_sheets.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--schema $(word 2,$^) \
		--target-class mims_soil \
		$<


## --materialize-patterns / --no-materialize-patterns
#schemasheets/yaml_output/mixs_from_schema_sheets_generated.yaml: schemasheets/yaml_output/mixs_from_schema_sheets.yaml
#	$(RUN) gen-linkml \
#		--format yaml \
#		--no-materialize-attributes $^ | \
#		yq 'del(.. | select(has("from_schema")).from_schema)' | \
#		yq 'del(.. | select(has("source_file")).source_file)' | \
#		yq '(... | select(type == "!!seq")) |= unique' > $@
#
#schemasheets/yaml_output/mixs_reference_merged.yaml: model/schema/mixs.yaml
#	$(RUN) python gsctools/merge_view.py \
#		--input_schema $< \
#		--output $@
#
## todo gen-linkml not merging imports
## Error: sort only works for scalars, got !!map
## todo try deepdiff again for list order insensitivity, or sort and otherwise repair with python code
#schemasheets/yaml_output/mixs_reference_generated.yaml: schemasheets/yaml_output/mixs_reference_merged.yaml
#	$(RUN) gen-linkml \
#		--format yaml \
#		--mergeimports \
#		--no-materialize-attributes $< > $@
#
#schemasheets/yaml_output/mixs_reference_no_explicit_falses.yaml: schemasheets/yaml_output/mixs_reference_generated.yaml
#	cat $< | yq 'del(.. | select(. == false))' | yq 'del(.. | select(tag == "!!seq" and length == 0))' > $@
#
#schemasheets/yaml_output/mixs_reference_no_empty_slot_examples.yaml: schemasheets/yaml_output/mixs_reference_no_explicit_falses.yaml
#	cat $< | yq '.slots |= (to_entries | map(select(.value.examples[].value != "")) | map(select(.value.examples | length >0)) | from_entries)' > $@
#
#
## yq e 'del(.. | select(. == false))' input3
#
## todo
## yq '.slots |= (to_entries | map(select(.value.examples[].value != "")) map(select(.value.examples | length >0)) | from_entries)' $< > $@
#
#
##| \
##		yq 'del(.. | select(has("from_schema")).from_schema)' | \
##		yq 'del(.. | select(has("source_file")).source_file)' | \
##		yq '(... | select(type == "!!seq")) |= unique' > $@
#
#
#
#schema_diff: schemasheets/yaml_output/mixs_reference_generated.yaml schemasheets/yaml_output/mixs_from_schema_sheets.yaml
#	- jd --yaml $^

#schemasheets/tsv_output/classes.tsv: schemasheets/yaml_output/mixs_from_schema_sheets.yaml
#	$(RUN) linkml2sheets \
#		--schema $< \
#		--output-directory schemasheets/tsv_output schemasheets/templates/classes.tsv
#
##
##schemasheets/tsv_output/slots.tsv: model/schema/mixs.yaml
##	$(RUN) linkml2sheets \
##		--schema $< \
##		--output-directory schemasheets/tsv_output schemasheets/templates/slots.tsv
##
##schemasheets/yaml_output/classes_roundtrip.yaml: \
##schemasheets/tsv_input/prefixes.tsv \
##schemasheets/tsv_input/schema.tsv \
##schemasheets/tsv_output/classes.tsv
##	$(RUN) sheets2linkml $^ | \
##	yq 'del(.. | select(has("from_schema")).from_schema)' | \
##	yq 'del(.. | select(has("source_file")).source_file)' | \
##	yq '(... | select(type == "!!seq")) |= unique' > $@
##
##schemasheets/yaml_output/slots_roundtrip.yaml: \
##schemasheets/tsv_input/prefixes.tsv \
##schemasheets/tsv_input/schema.tsv \
##schemasheets/tsv_output/slots.tsv
##	$(RUN) sheets2linkml $^ | \
##	yq '(... | select(type == "!!seq")) |= unique' | \
##	yq '.slots | to_entries | map(select(.value.examples[].value != "")) | map(select(.value.examples | length >0)) | from_entries ' | \
##	yq 'del(.. | select(has("from_schema")).from_schema)' | \
##	yq 'del(.. | select(has("source_file")).source_file)' | \
##	egrep -v 'comments: \[\]' | egrep -v ': false' > $@
##
##schemasheets/yaml_output/reference_classes_only.yaml:
##	$(RUN) python gsctools/classes_only.py | \
##	yq 'del(.. | select(has("from_schema")).from_schema)' | \
##	yq 'del(.. | select(has("source_file")).source_file)' | \
##	yq '(... | select(type == "!!seq")) |= unique' > $@
##
##
##schemasheets/yaml_output/reference_slots_only.yaml:
##	$(RUN) python gsctools/slots_only.py > $@
##
### add annotations and structured_pattern
##
##schemasheets/yaml_output/reference_slots_only_generated.yaml: schemasheets/yaml_output/reference_slots_only.yaml
##	$(RUN) gen-linkml \
##		--format yaml \
##		--mergeimports \
##		--no-materialize-attributes $< | \
##	yq '(... | select(type == "!!seq")) |= unique' | \
##	yq '.slots | to_entries | map(select(.value.examples[].value != "")) | map(select(.value.examples | length >0)) | from_entries ' | \
##	yq 'del(.. | select(has("from_schema")).from_schema)' | \
##	yq 'del(.. | select(has("source_file")).source_file)' | \
##	egrep -v 'comments: \[\]' | egrep -v ': false' > $@
##
##
##classes_diff: schemasheets/yaml_output/reference_classes_only.yaml schemasheets/yaml_output/classes_roundtrip.yaml
##	- jd --yaml $^
##
##slots_diff: schemasheets/yaml_output/reference_slots_only_generated.yaml schemasheets/yaml_output/slots_roundtrip.yaml
##	- jd --yaml $^
#
