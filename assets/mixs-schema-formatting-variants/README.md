poetry run python src/scripts/describe_enums_by_slots_using.py --schema-file src/mixs/schema/mixs.yaml --output-file assets/mixs-schema-formatting-variants/mixs_with_enum_descriptions.yaml

cp src/mixs/schema/mixs.yaml assets/mixs-schema-formatting-variants/original.yaml

poetry run gen-linkml --format yaml --no-materialize-attributes --materialize-patterns --no-mergeimports src/mixs/schema/mixs.yaml > assets/mixs-schema-formatting-variants/original-regenerated.yaml

cp src/mixs/schema/mixs.yaml assets/mixs-schema-formatting-variants/pycharm-auto.yaml # then open in pycharm, select all and hit control-alt-l aka command-option-l and save

