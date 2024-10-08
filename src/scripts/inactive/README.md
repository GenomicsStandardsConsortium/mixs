The Python scripts in this file illustrate methods for examining or modifying the schem through SchemaView(), but are
not run as part of any automated build process. They are lacking some best practices like using a click CLI. Maintenance
is deferred until we need to use them again.

`camel_case_enums.py` was run once and the changes were committed. It wouldn't need to be run again unless someone added
new enums and failed to stick to the CameCase naming convention.

Most of the functionality in `mixs_slots_report.py` is redundant to the functionality added
in https://github.com/GenomicsStandardsConsortium/mixs/pull/870