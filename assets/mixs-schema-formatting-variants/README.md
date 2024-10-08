poetry run python src/scripts/describe_enums_by_slots_using.py --schema-file src/mixs/schema/mixs.yaml --output-file assets/mixs-schema-formatting-variants/mixs_with_enum_descriptions.yaml

cp src/mixs/schema/mixs.yaml assets/mixs-schema-formatting-variants/original.yaml

poetry run gen-linkml --format yaml --no-materialize-attributes --materialize-patterns --no-mergeimports src/mixs/schema/mixs.yaml > assets/mixs-schema-formatting-variants/original-regenerated.yaml

cp src/mixs/schema/mixs.yaml assets/mixs-schema-formatting-variants/pycharm-auto.yaml # then open in pycharm, select all and hit control-alt-l aka command-option-l and save

yq eval '(.. | select(has("from_schema")) | .from_schema) style="" | del(.. | select(has("from_schema")).from_schema)' original-regenerated.yaml  |\
    yq eval '.prefixes |= map_values(.prefix_reference)' |\
    yq eval '.settings |= map_values(.setting_value)'  |\
    yq eval 'del(.classes.[].name)' |\
    yq eval 'del(.classes.[].slot_usage.[].name)'  |\
    yq eval 'del(.enums.[].name)'  |\
    yq eval 'del(.enums.[].permissible_values.[].text)' |\
    yq eval 'del(.slots.[].domain)'  |\
    yq eval 'del(.slots.[].name)' |\
    yq eval 'del(.source_file)'  |\
    yq eval 'del(.subsets.[].name)' | cat > original-regenerated-reduced.yaml