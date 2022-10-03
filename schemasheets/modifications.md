## Principles
- should pass aggressive linting
- should pass generic/default gen-project
- should be maximally computable (minimal ignore or annotations columns)
- there should be no repetition or contradictions in slot usage
  - a maximal amount of invariant slot knowledge should  be pulled out of slot_usage and assigned at the schema's `slots` level

## Started by downloading TSV version of the Google Sheets

* `schemasheets/tsv_input/original_with_ssheaders/MIxS_6_term_updates_MIxS6_Core-Final_clean.tsv`
* `schemasheets/tsv_input/original_with_ssheaders/MIxS_6_term_updates_MIxS6_packages-Final_clean.tsv`

- inserted 1st schemasheets header row below "Structured comment name"...
- deleted headerless W columns 
  - after V "MIGS ID (mapping to GOLD)"
  - W appears narrower that all other subsequent columns, as if Excel detects some whitespace characters
  - otherwise "ValueError: Enter an interpretation for"
- started with all "ignore" in new row 2 except A2 "> slot"

```shell
make clean_schemasheets schemasheets/yaml_output/mixs_from_schema_sheets.yaml
```

## whitespace should be normalized in source file
> WARNING:root:Stripping value: "Report the entity or entities which are in the sample or specimen’s local vicinity and which you believe have significant causal influences on your sample or specimen. We recommend using EnvO terms which are of smaller spatial grain than your entry for env_broad_scale. Terms, such as anatomical sites, from other OBO Library ontologies which interoperate with EnvO (e.g. UBERON) are accepted in this field. EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS. " for Definition
> WARNING:root:Stripping value: "The material displaced by the entity at time of sampling. Recommend subclasses of environmental material [ENVO:00010483]. " for Expected value
> WARNING:root:Stripping value: "The type of reproduction from the parent stock. Values for this field is specific to different taxa. For phage or virus: lytic/lysogenic/temperate/obligately lytic. For plasmids: incompatibility group. For eukaryotes: sexual/asexual. " for Definition 
> WARNING:root:Stripping value: "A related resource that is referenced, cited, or otherwise associated to the sequence. " for Definition
> WARNING:root:Stripping value: "sample name " for Item (rdfs:label)
> WARNING:root:Stripping value: "Taxonomy ID " for Expected value
> WARNING:root:Stripping value: "The substance, mixture, product, or apparatus used to verify that a process which is part of an investigation delivers a true positive. " for Definition

## Should set a --name parameter or better, compile a sheet with schema metadata
> ERROR:root:Prefix TEMP not declared: using default
- compare to output from `gsctools/mixs_converter.py`

## After adding `--name MIXS6_2` to `sheets2linkml` command
> ERROR:root:Prefix MIXS6_2 not declared: using default


## Next steps
- add Packages sheet
- un-ignore more Core columns
- run linter
- run gen-linkml

## After 

| Structured comment name | Item (rdfs:label) | Definition  | Expected value | Value syntax | Example | Section | migs_eu | migs_ba | migs_pl | migs_vi | migs_org | mims   | mimarks_s | mimarks_c | misag  | mimag  | miuvig | Preferred unit | Occurrence | MIXS ID  | MIGS ID (mapping to GOLD) |
|-------------------------|-------------------|-------------|----------------|--------------|---------|---------|---------|---------|---------|---------|----------|--------|-----------|-----------|--------|--------|--------|----------------|------------|----------|---------------------------|
| > slot                  | title             | description | ignore         | ignore       | ignore  | ignore  | ignore  | ignore  | ignore  | ignore  | ignore   | ignore | ignore    | ignore    | ignore | ignore | ignore | ignore         | ignore     | slot_uri | ignore                    |

> ERROR:root:Prefix MIXS6_2 not declared: using default
WARNING:root:Filling in missing prefix for: MIXS => http://example.org/MIXS/

Not much change

> WARNING:root:Stripping value: "Report the entity or entities which are in the sample or specimen’s local vicinity and which you believe have significant causal influences on your sample or specimen. We recommend using EnvO terms which are of smaller spatial grain than your entry for env_broad_scale. Terms, such as anatomical sites, from other OBO Library ontologies which interoperate with EnvO (e.g. UBERON) are accepted in this field. EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS. " for Definition
WARNING:root:Stripping value: "The material displaced by the entity at time of sampling. Recommend subclasses of environmental material [ENVO:00010483]. " for Expected value
WARNING:root:Stripping value: "The type of reproduction from the parent stock. Values for this field is specific to different taxa. For phage or virus: lytic/lysogenic/temperate/obligately lytic. For plasmids: incompatibility group. For eukaryotes: sexual/asexual. " for Definition
WARNING:root:Stripping value: "A related resource that is referenced, cited, or otherwise associated to the sequence. " for Definition
WARNING:root:Stripping value: "sample name " for Item (rdfs:label)
WARNING:root:Stripping value: "Taxonomy ID " for Expected value
WARNING:root:Stripping value: "The substance, mixture, product, or apparatus used to verify that a process which is part of an investigation delivers a true positive. " for Definition
ERROR:root:Prefix MIXS6_2 not declared: using default
WARNING:root:Filling in missing prefix for: MIXS => http://example.org/MIXS/

## Start ignoring the description in C and try applies_to_class: "migs_eu" etc.

| Structured comment   name | Item (rdfs:label) | Definition | Expected value | Value syntax | Example | Section | migs_eu                     | migs_ba                     | migs_pl                     | migs_vi                     | migs_org                     | mims                     | mimarks_s                     | mimarks_c                     | misag                     | mimag                     | miuvig                     | Preferred unit | Occurrence | MIXS ID  | MIGS ID (mapping to GOLD) |
|---------------------------|-------------------|------------|----------------|--------------|---------|---------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|------------------------------|--------------------------|-------------------------------|-------------------------------|---------------------------|---------------------------|----------------------------|----------------|------------|----------|---------------------------|
| > slot                    | title             | ignore     | ignore         | ignore       | ignore  | ignore  | description                 | description                 | description                 | description                 | description                  | description              | description                   | description                   | description               | description               | description                | ignore         | ignore     | slot_uri | ignore                    |
| >                         |                   |            |                |              |         |         | applies_to_class: "migs_eu" | applies_to_class: "migs_ba" | applies_to_class: "migs_pl" | applies_to_class: "migs_vi" | applies_to_class: "migs_org" | applies_to_class: "mims" | applies_to_class: "mimarks_s" | applies_to_class: "mimarks_c" | applies_to_class: "misag" | applies_to_class: "mimag" | applies_to_class: "miuvig" |                |            |          |                           |

`applies_to_class` implementation in `slot_usage` looks good

Try replacing `applies_to_class` in the `description/applies_to_class` columns with the schemasheets `cardinality` shortcuts: https://linkml.io/schemasheets/datamodel/Cardinality/. See esp `mixs_notation`

> Traceback (most recent call last):
  File "/Users/MAM/Library/Caches/pypoetry/virtualenvs/mixs-linkml-GchukLmP-py3.9/lib/python3.9/site-packages/schemasheets/schemamaker.py", line 105, in merge_sheet
    self.add_row(row, schemasheet.table_config)
  File "/Users/MAM/Library/Caches/pypoetry/virtualenvs/mixs-linkml-GchukLmP-py3.9/lib/python3.9/site-packages/schemasheets/schemamaker.py", line 133, in add_row
    self.set_cardinality(actual_element, v)
  File "/Users/MAM/Library/Caches/pypoetry/virtualenvs/mixs-linkml-GchukLmP-py3.9/lib/python3.9/site-packages/schemasheets/schemamaker.py", line 479, in set_cardinality
    raise ValueError(f'Cannot parse cardinality: {card} // {pvs.keys()}')
ValueError: Cannot parse cardinality: X // dict_keys(['mandatory', 'optional', 'recommended', 'not_recommended', 'applicable', 'not_applicable', 'zero_or_one', 'exactly_one', 'zero_to_many', 'one_to_many', 'single_valued', 'multi_valued', 'conditional', 'unconditional', 'conditional_mandatory'])

> The above exception was the direct cause of the following exception:

> Traceback (most recent call last):
  File "/Users/MAM/Library/Caches/pypoetry/virtualenvs/mixs-linkml-GchukLmP-py3.9/bin/sheets2linkml", line 8, in <module>
    sys.exit(convert())
  File "/Users/MAM/Library/Caches/pypoetry/virtualenvs/mixs-linkml-GchukLmP-py3.9/lib/python3.9/site-packages/click/core.py", line 1130, in __call__
    return self.main(*args, **kwargs)
  File "/Users/MAM/Library/Caches/pypoetry/virtualenvs/mixs-linkml-GchukLmP-py3.9/lib/python3.9/site-packages/click/core.py", line 1055, in main
    rv = self.invoke(ctx)
  File "/Users/MAM/Library/Caches/pypoetry/virtualenvs/mixs-linkml-GchukLmP-py3.9/lib/python3.9/site-packages/click/core.py", line 1404, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/Users/MAM/Library/Caches/pypoetry/virtualenvs/mixs-linkml-GchukLmP-py3.9/lib/python3.9/site-packages/click/core.py", line 760, in invoke
    return __callback(*args, **kwargs)
  File "/Users/MAM/Library/Caches/pypoetry/virtualenvs/mixs-linkml-GchukLmP-py3.9/lib/python3.9/site-packages/schemasheets/schemamaker.py", line 585, in convert
    schema = sm.create_schema(list(tsv_files))
  File "/Users/MAM/Library/Caches/pypoetry/virtualenvs/mixs-linkml-GchukLmP-py3.9/lib/python3.9/site-packages/schemasheets/schemamaker.py", line 61, in create_schema
    self.merge_sheet(f, **kwargs)
  File "/Users/MAM/Library/Caches/pypoetry/virtualenvs/mixs-linkml-GchukLmP-py3.9/lib/python3.9/site-packages/schemasheets/schemamaker.py", line 108, in merge_sheet
    raise SchemaSheetRowException(f'Error in line {line_num}, row={row}') from e
schemasheets.schemamaker.SchemaSheetRowException: Error in line 3, row={'Structured comment name': 'samp_size', 'Item (rdfs:label)': 'amount or size of sample collected', 'Definition': 'The total amount or size (volume (ml), mass (g) or area (m2) ) of sample collected.', 'Expected value': 'measurement value', 'Value syntax': '{float} {unit}', 'Example': '5 liter', 'Section': 'nucleic acid sequence source', 'migs_eu': 'X', 'migs_ba': 'X', 'migs_pl': 'X', 'migs_vi': 'X', 'migs_org': 'X', 'mims': 'C', 'mimarks_s': 'C', 'mimarks_c': 'X', 'misag': 'C', 'mimag': 'C', 'miuvig': 'C', 'Preferred unit': 'millliter, gram, milligram, liter', 'Occurrence': '1', 'MIXS ID': 'MIXS:0000001', 'MIGS ID (mapping to GOLD)': ''}

MIXS `X` is supposed to be mapped to [schemasheeets cardinality `optional`](https://github.com/linkml/schemasheets/blob/dcdce0abf1b6170f946ed6720aee339a7032074d/schemasheets/conf/configschema.yaml#L119-L129)

Replace `X` with `O` in H4..R101

> ValueError: Cannot parse cardinality: C

Replace C with EM

> ValueError: Cannot parse cardinality: E

Replace E with E+

Result: requireds are asserted. Maybe also takes care of not-applicables? But the various codes don't all map to a unique configuration, so a round trip won't be possible. 

**Therefore,** revert to GSC's cardinality codes, but implement as weaker annotations. 
Also:
- Resuming use of `description` for "Definition" column
- Using annotations to models several other columns
- For "Example" column, use `examples` with `internal_separator: "|"`
- Include TSVs in `schemasheets/tsv_input/mixs_converter_inspired_additionals`
- protect 16s... terms with initial x_


## To do
- multi-example values should then have delimiters inserted. Doesn't have to be `|`
- Many "Value syntax"es need to be broken into enumerations, but many of those are invalid in some way. Illegal characters, enum/pattern hybrids, etc.
- Most of the "Definitions" are actually hybrids of `descriptions`, `examples`, `comments` etc.
- Generate and assign compound class uris to combinations in `gsctools/combination_sheets.py`
- resume diffs

## Questions

## Problems from Chris Hunter

## Deferred Problems from Mark