## MIxS (meta)data collection spreadsheet templates

This folder contains the MIxS schema (meta)data collection templates in the Excel spreadsheet (.xlsx) format. Each of the Excel files in this folder are blank spreadsheet templates with only the header row populated with the names of the terms that are associated with a particular checklist/extension/combination. One validation feature baked into these spreadsheet templates is that some columns will be constrained using dropdowns, but we should be careful to note the [caveat](https://linkml.io/linkml/generators/excel.html) from the linkml library.

* There is one Excel file/template for each *checklist*, *extension* and *combination* class in the [schema](src/mixs/schema/mixs.yaml).

* The organization of files in this folder is such that there is one checklist-level subfolder per checklist, and an extensions subfolder.
  * The checklist-level subfolders contain the Excel file for that checklist class, as well as the Excel files for the combination classes that have been derived from that checklist. 
  * The extensions subfolder contains the Excel files for all the extension classes in the schema.
