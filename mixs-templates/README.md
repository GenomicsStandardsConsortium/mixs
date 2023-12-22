## MIxS (meta)data collection spreadsheet templates

This folder contains the MIxS schema (meta)data collection templates in the Excel spreadsheet (.xlsx) format. Each of the templates in this folder are blank spreadsheet templates with only the header row populated with the names of the terms that are associated with a particular [checklist](https://sujaypatil96.github.io/mixs/#checklists), [extension](https://sujaypatil96.github.io/mixs/#extensions), or [combination](https://sujaypatil96.github.io/mixs/combinations/) (of one checklist plus one extension). The templates offer pulldown menus for filling out columns for which there is a brief [enumeration](https://sujaypatil96.github.io/mixs/enumerations/) of permissible values, like [window_type](https://sujaypatil96.github.io/mixs/0000856/), but this [feature is disabled](https://linkml.io/linkml/generators/excel.html) if the total character length of the permissible values is more than 255, like [fao_class](https://sujaypatil96.github.io/mixs/0001083/).

Note: The [linkml-validate](https://linkml.io/linkml/data/validating-data.html#the-linkml-validate-cli) command-line tool can be used to check the validity of a completed template, but no validation is provided in the template itself.

* There is one template for each *checklist*, *extension* and *combination* in the [schema](src/mixs/schema/mixs.yaml).

* The organization of files in this folder is such that there is one checklist subfolder per checklist, and an extensions subfolder.
  * The checklist subfolders contain the template for that checklist, as well as the templates for the combinations that have been derived from that checklist. 
  * The extensions subfolder contains the templates for all the extensions in the schema.
