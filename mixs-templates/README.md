## MIxS (meta)data collection spreadsheet templates

In this folder, the GSC provides Microsoft Excel (.xlsx) spreadsheets for collecting metadata that is roughly aligned with the MIxS standard. THe GSC appreciates that spreadsheets like these can be very useful for preparing data to be submitted to an INSDC database. Users should be aware of the limitations of these spreadsheets, listed below.

Each of the templates in this folder are blank spreadsheet templates with only the header row populated with the names of the terms that are associated with a particular [checklist](https://sujaypatil96.github.io/mixs/#checklists), [extension](https://sujaypatil96.github.io/mixs/#extensions), or [combination](https://sujaypatil96.github.io/mixs/combinations/) (of one checklist plus one extension). 

* There is one template for each *checklist*, *extension* and *combination* in the [schema](src/mixs/schema/mixs.yaml).

* The organization of files in this folder is such that there is one checklist subfolder per checklist, and an extensions subfolder.
  * The checklist subfolders contain the template for that checklist, as well as the templates for the combinations that have been derived from that checklist. 
  * The extensions subfolder contains the templates for all the extensions in the schema.

### Limitations:
- The use of Excel spreadsheets is a violation of the 5-star linked data standards, which require the use of an open format like TSV or CSV
- Excel files do not play well with GitHub: it is very difficult to view them or diff them within GH, and they take up more disk space than TSV or CSV
- These spreadsheets confuse the **specification of a standard** and an **application that uses the standard** to collect data. THe spreadsheets do not apply any validation to the entered metadata. They do provide one data entry convenience: pulldown menus are provided for filling out columns when there is a brief [enumeration](https://sujaypatil96.github.io/mixs/enumerations/) of permissible values, like [window_type](https://sujaypatil96.github.io/mixs/0000856/), but this [feature is disabled](https://linkml.io/linkml/generators/excel.html) if the total character length of the permissible values is more than 255, like [fao_class](https://sujaypatil96.github.io/mixs/0001083/).
- Validation can be applied with the [linkml-validate](https://linkml.io/linkml/data/validating-data.html#the-linkml-validate-cli) command-line tool, but the Excel spreadsheets must be converted to TSV or CSV before running the validator.
