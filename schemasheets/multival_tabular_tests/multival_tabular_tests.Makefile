RUN=poetry run

.PHONY: multival_tabular_tests_all multival_tabular_tests_clean

multival_tabular_tests_all: multival_tabular_tests_clean generated/multival_tabular_tests_generated.sql

multival_tabular_tests_clean:
	rm -rf generated/*

generated/multival_tabular_tests_generated.yaml: multival_tabular_tests.yaml
	$(RUN) gen-linkml \
		--no-materialize-attributes \
		--format yaml \
		--output $@ $^

generated/multival_tabular_tests_generated.sql: generated/multival_tabular_tests_generated.yaml
	$(RUN) gen-project --dir generated $<