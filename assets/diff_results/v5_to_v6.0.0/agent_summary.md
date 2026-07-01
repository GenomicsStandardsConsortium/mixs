# MIxS v5 (2018, Excel) to v6.0.0 (2022, LinkML)

Summary of `schema_comparison_results.yaml` in this directory: the change from the
last Excel MIxS (v5, 600 terms) to the first LinkML MIxS (v6.0.0, 804 terms).

**Added:** 226 terms (only in v6.0.0). **Removed:** 18 terms (only in v5).
**Shared:** 573 terms kept the same name.

**Renamed (6):** `16s_recover` to `x_16s_recover`, `16s_recover_software` to
`x_16s_recover_software`, `health_disease_stat` to `host_disease_stat`,
`votu_class_appr` to `otu_class_appr`, `votu_db` to `otu_db`,
`votu_seq_comp_appr` to `otu_seq_comp_appr`. (The `16s` terms gain an `x_` prefix
because LinkML names cannot start with a digit; `votu` became `otu`.)

**Removed on purpose (3):** `env_package` (package membership is now handled by
the class hierarchy), `investigation_type` (now implicit in checklist selection),
`submitted_to_insdc` (INSDC submission status is no longer tracked).

**Definitions changed:** 62 terms that kept their name have a different definition
between v5 and v6.0.0.

**Notes:** the diff compares term names and definitions. The 18 removals were each
checked to be absent from v6.0.0, and the 6 rename targets to be present, against
the real `mixs6.0.0` tag. Because both versions are finished releases, this result
never changes.
