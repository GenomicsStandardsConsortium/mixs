RUN=poetry run

.PHONY: multival_tabular_tests_all multival_tabular_tests_clean validate

multival_tabular_tests_all: \
multival_tabular_tests_clean \
generated/multival_tabular_tests_generated.sql \
validate \
example_data/out/multival_tabular_tests_data_valid.csv \
example_data/out/multival_tabular_tests_data_valid.db \
example_data/out/multival_tabular_tests_data_valid.json \
example_data/out/multival_tabular_tests_data_valid.yaml

multival_tabular_tests_clean:
	rm -rf generated/*
	rm -rf example_data/out/*

generated/multival_tabular_tests_generated.yaml: multival_tabular_tests.yaml
	$(RUN) gen-linkml \
		--no-materialize-attributes \
		--format yaml \
		--output $@ $^

generated/multival_tabular_tests_generated.sql: generated/multival_tabular_tests_generated.yaml
	$(RUN) gen-project --dir generated $<

validate: generated/multival_tabular_tests_generated.yaml example_data/in/multival_tabular_tests_data_valid.yaml
	$(RUN) linkml-validate --schema $^

example_data/out/multival_tabular_tests_data_valid.json: \
generated/multival_tabular_tests_generated.yaml example_data/in/multival_tabular_tests_data_valid.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--schema $^

example_data/out/multival_tabular_tests_data_valid.csv: \
generated/multival_tabular_tests_generated.yaml example_data/in/multival_tabular_tests_data_valid.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--index-slot person_set \
		--schema $^

example_data/out/multival_tabular_tests_data_valid.yaml: \
generated/multival_tabular_tests_generated.yaml example_data/out/multival_tabular_tests_data_valid.csv
	$(RUN) linkml-convert \
		--output $@ \
		--index-slot person_set \
		--schema $^

example_data/out/multival_tabular_tests_data_valid.db: \
generated/multival_tabular_tests_generated.yaml example_data/in/multival_tabular_tests_data_valid.yaml
	$(RUN) linkml-sqldb dump \
		--db $@ \
		--target-class Database \
		--schema $^
	sqlite3 $@ ".header on" "select * from Person"
