DIR_CREATION_MSG="this file forces the creation of the parent directory"
RUN=poetry run

.PHONY: clean_schemasheets all_schemasheets

all_schemasheets: \
clean_schemasheets \
schemasheets/yaml_output/mixs_from_schema_sheets.yaml \
schemasheets/generated/mixs_from_schema_sheets_generated.yaml \
schemasheets/generated/sqlschema/mixs_from_schema_sheets.sql \
schemasheets/yaml_output/mixs_reference_merged.yaml

# schemasheets/lint_log.tsv \

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
	rm -rf schemasheets/generated/*
	echo $(DIR_CREATION_MSG) > schemasheets/generated/README.md


# partial list of problematics package slots

  # assembly_software	assembly softwar	MIXS:0000056
  #    conflicts with assembly_qual MIXS:0000056 from core sheet
  # nose_throat_disord	nose/mouth/teeth/throat disorder	MIXS:0000283
  # host_sex	host sex	MIXS:0000811
  # host_body_product	host body product	MIXS:0000888
  # soil_horizon	soil horizon	MIXS:0001082	horizon|horizon
  # host_symbiont	observed host symbionts	MIXS:0001298

# todo work on settings and structured patterns (gen-linkml expansion)

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

schemasheets/generated/sqlschema/mixs_from_schema_sheets.sql: \
schemasheets/generated/mixs_from_schema_sheets_generated.yaml
	$(RUN) gen-project \
		--exclude excel \
		--exclude markdown \
		--dir schemasheets/generated $<


#gen_debug: \
#schemasheets/yaml_output/mixs_from_schema_sheets.yaml
#	mkdir -p schemasheets/generated/docs
#	$(RUN) gen-project \
#		--include markdown \
#		--dir schemasheets/generated $<

# INFO:root:Generating: excel
  #  File "/Users/MAM/Library/Caches/pypoetry/virtualenvs/mixs-linkml-GchukLmP-py3.9/lib/python3.9/site-packages/openpyxl/workbook/child.py", line 93, in title
  #    raise ValueError(msg)
  #ValueError: Invalid character / found in sheet title

# INFO:root:Generating: markdown
  #  File "/Users/MAM/Library/Caches/pypoetry/virtualenvs/mixs-linkml-GchukLmP-py3.9/lib/python3.9/site-packages/linkml/generators/markdowngen.py", line 280, in visit_slot
  #    with open(
  #FileNotFoundError: [Errno 2] No such file or directory: 'schemasheets/generated/docs/hydrocarbon_resources_fluids/swabs_add_recov_method.md'

schemasheets/yaml_output/mixs_from_schema_sheets_repaired.yaml: \
schemasheets/tsv_input/database_support/database_classes.tsv \
schemasheets/tsv_input/database_support/database_slots.tsv \
schemasheets/tsv_input/original_headers_repairs/MIxS_6_term_updates_MIxS6_Core-Final_clean.tsv \
schemasheets/tsv_input/original_headers_repairs/MIxS_6_term_updates_MIxS6_packages-Final_clean.tsv \
schemasheets/tsv_input/repair_support/combo_classes_subset.tsv
	$(RUN) sheets2linkml --output $@ $^

schemasheets/tsv_input/generated/mixs_from_schema_sheets_repaired.py: schemasheets/yaml_output/mixs_from_schema_sheets_repaired.yaml
	$(RUN) gen-python $< > $@

schemasheets/example_data/out/mims_soil_data_via_repaired.json: \
schemasheets/example_data/in/mims_soil_data.yaml \
schemasheets/yaml_output/mixs_from_schema_sheets_repaired.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--schema $(word 2,$^) \
		--target-class MimsSoil $<

#   File "/Users/MAM/Library/Caches/pypoetry/virtualenvs/mixs-linkml-GchukLmP-py3.9/lib/python3.9/site-packages/linkml_runtime/utils/compile_python.py", line 30, in compile_python
  #    spec = compile(python_txt, 'test', 'exec')
  #  File "test", line 136
  #    16s_recover: Optional[str] = None
  #      ^
  #SyntaxError: invalid syntax

#   File "/Users/MAM/Library/Caches/pypoetry/virtualenvs/mixs-linkml-GchukLmP-py3.9/lib/python3.9/site-packages/linkml_runtime/utils/compile_python.py", line 30, in compile_python
  #    spec = compile(python_txt, 'test', 'exec')
  #  File "test", line 17860
  #    class Food-animalAndAnimalFeed(EnvPackage):
  #              ^
  #SyntaxError: invalid syntax

### --materialize-patterns / --no-materialize-patterns
##schemasheets/yaml_output/mixs_from_schema_sheets_generated.yaml: schemasheets/yaml_output/mixs_from_schema_sheets.yaml
##	$(RUN) gen-linkml \
##		--format yaml \
##		--no-materialize-attributes $^ | \
##		yq 'del(.. | select(has("from_schema")).from_schema)' | \
##		yq 'del(.. | select(has("source_file")).source_file)' | \
##		yq '(... | select(type == "!!seq")) |= unique' > $@

schemasheets/yaml_output/mixs_reference_merged.yaml: model/schema/mixs.yaml
	$(RUN) python gsctools/merge_view.py \
		--input_schema $< \
		--output $@

### todo gen-linkml not merging imports
### Error: sort only works for scalars, got !!map
### todo try deepdiff again for list order insensitivity, or sort and otherwise repair with python code
##schemasheets/yaml_output/mixs_reference_generated.yaml: schemasheets/yaml_output/mixs_reference_merged.yaml
##	$(RUN) gen-linkml \
##		--format yaml \
##		--mergeimports \
##		--no-materialize-attributes $< > $@
##
##schemasheets/yaml_output/mixs_reference_no_explicit_falses.yaml: schemasheets/yaml_output/mixs_reference_generated.yaml
##	cat $< | yq 'del(.. | select(. == false))' | yq 'del(.. | select(tag == "!!seq" and length == 0))' > $@
##
##schemasheets/yaml_output/mixs_reference_no_empty_slot_examples.yaml: schemasheets/yaml_output/mixs_reference_no_explicit_falses.yaml
##	cat $< | yq '.slots |= (to_entries | map(select(.value.examples[].value != "")) | map(select(.value.examples | length >0)) | from_entries)' > $@
##
##
### yq e 'del(.. | select(. == false))' input3
##
### todo
### yq '.slots |= (to_entries | map(select(.value.examples[].value != "")) map(select(.value.examples | length >0)) | from_entries)' $< > $@
##
##
###| \
###		yq 'del(.. | select(has("from_schema")).from_schema)' | \
###		yq 'del(.. | select(has("source_file")).source_file)' | \
###		yq '(... | select(type == "!!seq")) |= unique' > $@
##
##
##
##schema_diff: schemasheets/yaml_output/mixs_reference_generated.yaml schemasheets/yaml_output/mixs_from_schema_sheets.yaml
##	- jd --yaml $^
#
##schemasheets/tsv_output/classes.tsv: schemasheets/yaml_output/mixs_from_schema_sheets.yaml
##	$(RUN) linkml2sheets \
##		--schema $< \
##		--output-directory schemasheets/tsv_output schemasheets/templates/classes.tsv
##
###
###schemasheets/tsv_output/slots.tsv: model/schema/mixs.yaml
###	$(RUN) linkml2sheets \
###		--schema $< \
###		--output-directory schemasheets/tsv_output schemasheets/templates/slots.tsv
###
###schemasheets/yaml_output/classes_roundtrip.yaml: \
###schemasheets/tsv_input/prefixes.tsv \
###schemasheets/tsv_input/schema.tsv \
###schemasheets/tsv_output/classes.tsv
###	$(RUN) sheets2linkml $^ | \
###	yq 'del(.. | select(has("from_schema")).from_schema)' | \
###	yq 'del(.. | select(has("source_file")).source_file)' | \
###	yq '(... | select(type == "!!seq")) |= unique' > $@
###
###schemasheets/yaml_output/slots_roundtrip.yaml: \
###schemasheets/tsv_input/prefixes.tsv \
###schemasheets/tsv_input/schema.tsv \
###schemasheets/tsv_output/slots.tsv
###	$(RUN) sheets2linkml $^ | \
###	yq '(... | select(type == "!!seq")) |= unique' | \
###	yq '.slots | to_entries | map(select(.value.examples[].value != "")) | map(select(.value.examples | length >0)) | from_entries ' | \
###	yq 'del(.. | select(has("from_schema")).from_schema)' | \
###	yq 'del(.. | select(has("source_file")).source_file)' | \
###	egrep -v 'comments: \[\]' | egrep -v ': false' > $@
###
###schemasheets/yaml_output/reference_classes_only.yaml:
###	$(RUN) python gsctools/classes_only.py | \
###	yq 'del(.. | select(has("from_schema")).from_schema)' | \
###	yq 'del(.. | select(has("source_file")).source_file)' | \
###	yq '(... | select(type == "!!seq")) |= unique' > $@
###
###
###schemasheets/yaml_output/reference_slots_only.yaml:
###	$(RUN) python gsctools/slots_only.py > $@
###
#### add annotations and structured_pattern
###
###schemasheets/yaml_output/reference_slots_only_generated.yaml: schemasheets/yaml_output/reference_slots_only.yaml
###	$(RUN) gen-linkml \
###		--format yaml \
###		--mergeimports \
###		--no-materialize-attributes $< | \
###	yq '(... | select(type == "!!seq")) |= unique' | \
###	yq '.slots | to_entries | map(select(.value.examples[].value != "")) | map(select(.value.examples | length >0)) | from_entries ' | \
###	yq 'del(.. | select(has("from_schema")).from_schema)' | \
###	yq 'del(.. | select(has("source_file")).source_file)' | \
###	egrep -v 'comments: \[\]' | egrep -v ': false' > $@
###
###
###classes_diff: schemasheets/yaml_output/reference_classes_only.yaml schemasheets/yaml_output/classes_roundtrip.yaml
###	- jd --yaml $^
###
###slots_diff: schemasheets/yaml_output/reference_slots_only_generated.yaml schemasheets/yaml_output/slots_roundtrip.yaml
###	- jd --yaml $^
##

.PHONY: mims_set_data_missing_validation mims_set_data_extra_validation

all_reshaped: \
clean_reshaped \
schemasheets/logs/mixs_core_reshaped_linting_log.tsv \
schemasheets/generated/sqlschema/mixs_core_reshaped.sql \
mims_set_data_missing_validation \
mims_set_data_extra_validation

# todo excel and sqlddl artifacts look wierd
#   direct jsonschema and linkml-validate not working as expected
#   should I be setting tree root?

clean_reshaped:
	rm -rf schemasheets/yaml_output/mixs_core_reshaped.yaml
	rm -rf schemasheets/logs/mixs_core_reshaped*
	rm -rf schemasheets/generated/*
	mkdir -p schemasheets/generated
	mkdir -p schemasheets/logs
	mkdir -p schemasheets/yaml_output
	echo $(DIR_CREATION_MSG) > schemasheets/generated/README.md
	echo $(DIR_CREATION_MSG) > schemasheets/logs/README.md
	echo $(DIR_CREATION_MSG) > schemasheets/yaml_output/README.md

# todo document how .../MIxS_6_term_updates_MIxS6_Core-Final_clean_slotdefs.tsv etc were generated
schemasheets/yaml_output/mixs_core_reshaped.yaml: \
schemasheets/tsv_input/original_headers_reshaped/MIxS_6_term_updates_MIxS6_Core-Final_clean_classdefs.tsv \
schemasheets/tsv_input/original_headers_reshaped/MIxS_6_term_updates_MIxS6_Core-Final_clean_slot_assignments.tsv \
schemasheets/tsv_input/original_headers_reshaped/MIxS_6_term_updates_MIxS6_Core-Final_clean_slotdefs.tsv \
schemasheets/tsv_input/original_headers_reshaped/mixs_prefixes.tsv \
schemasheets/tsv_input/original_headers_reshaped/mixs_schema_annotations.tsv \
schemasheets/tsv_input/original_headers_reshaped/mixs_utility.tsv
	$(RUN) sheets2linkml --output $@ $^ 2>&1 | tee schemasheets/logs/$(basename $(notdir $@)).log

# --fix / --no-fix
# see https://github.com/linkml/linkml/blob/main/linkml/linter/config/default.yaml
schemasheets/logs/mixs_core_reshaped_linting_log.tsv: schemasheets/yaml_output/mixs_core_reshaped.yaml
	- $(RUN) linkml-lint \
		--format tsv \
		--output $@ $< \
		--config schemasheets/linter_config_default.yaml


# todo capture log?
schemasheets/generated/mixs_core_reshaped_generated.yaml: schemasheets/yaml_output/mixs_core_reshaped.yaml
	$(RUN) gen-linkml \
		--format yaml \
		--no-materialize-attributes $^ > $@

# todo capture log?
schemasheets/generated/sqlschema/mixs_core_reshaped.sql: \
schemasheets/generated/mixs_core_reshaped_generated.yaml
	$(RUN) gen-project \
		--dir schemasheets/generated $<

mims_set_data_missing_validation: \
schemasheets/generated/mixs_core_reshaped_generated.yaml schemasheets/example_data/in/mims_set_data_missing.json
	! $(RUN) linkml-validate \
		--target-class Database \
		--schema $^

mims_set_data_extra_validation: \
schemasheets/generated/mixs_core_reshaped_generated.yaml schemasheets/example_data/in/mims_set_data_extra.json
	! $(RUN) linkml-validate \
		--target-class Database \
		--schema $^

mims_set_data_validation: \
schemasheets/generated/mixs_core_reshaped_generated.yaml schemasheets/example_data/in/mims_set_data.json
	$(RUN) linkml-validate \
		--target-class Database \
		--schema $^

# jsonschema.exceptions.RefResolutionError: Unresolvable JSON pointer: '$defs/Mims'

# additonal linkml-validate options
 #  -m, --module TEXT               Path to python
 #                                  datamodel module
 #  -o, --output TEXT               Path to output
 #                                  file
 #  -f, --input-format [yaml|json|rdf|ttl|json-ld|csv|tsv]
 #                                  Input format.
 #                                  Inferred from
 #                                  input suffix if
 #                                  not specified
 #  -C, --target-class TEXT         name of class in
 #                                  datamodel that
 #                                  the root node
 #                                  instantiates
 #  -S, --index-slot TEXT           top level slot.
 #                                  Required for CSV
 #                                  dumping/loading
 #  -s, --schema TEXT               Path to schema
 #                                  specified as
 #                                  LinkML yaml

# additional gen-project options
  #  -A, --generator-arguments TEXT  yaml configuration for generators
  #  -C, --config-file FILENAME      path to yaml configuration
  #  -X, --exclude TEXT              list of artefacts to be excluded
  #  -I, --include TEXT              list of artefacts to be included. If not
  #                                  set, defaults to all
  #  --mergeimports / --no-mergeimports
  #                                  Merge imports into source file  [default:
  #                                  mergeimports]

# additional gen-linkml options
  #  --materialize-patterns / --no-materialize-patterns
  #                                  Materialize structured patterns as patterns
  #                                  [default: no-materialize-patterns]
  #  --materialize-attributes / --no-materialize-attributes
  #                                  Materialize induced slots as attributes
  #                                  [default: materialize-attributes]
  #  --metadata / --no-metadata      Include metadata in output  [default:
  #                                  metadata]
  #  --useuris / --metauris          Include metadata in output  [default:
  #                                  useuris]
  #  -im, --importmap FILENAME       Import mapping file
  #  --log_level [CRITICAL|ERROR|WARNING|INFO|DEBUG]
  #                                  Logging level  [default: WARNING]
  #  -v, --verbose                   verbosity
  #  --mergeimports / --no-mergeimports
  #                                  Merge imports into source file
  #                                  (default=mergeimports)

# Additional sheets2linkml Options:
  #  -n, --name TEXT                 name of the
  #                                  schema
  #  --unique-slots / --no-unique-slots
  #                                  All slots are
  #                                  treated as
  #                                  unique and top
  #                                  level and do not
  #                                  belong to the
  #                                  specified class
  #                                  [default: no-
  #                                  unique-slots]
  #  --repair / --no-repair          Auto-repair
  #                                  schema
  #                                  [default:
  #                                  repair]
  #  --gsheet-id TEXT                Google sheets
  #                                  ID. If this is
  #                                  specified then
  #                                  the arguments
  #                                  MUST be sheet
  #                                  names
  #  -v, --verbose