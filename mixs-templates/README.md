## MIxS (meta)data collection spreadsheet templates

In this folder, the GSC provides Microsoft Excel (.xlsx) spreadsheets that can be used as templates for collecting metadata according to the MIxS standard. 

The GSC appreciates that spreadsheets like these can be very useful for use in the field and lab, as well as for preparing data to be submitted to an INSDC database. However, users should be aware of the limitations of these spreadsheets, listed below.

Each of the files in this folder and its subfolders are blank template spreadsheets, with only the header row populated with the names of terms associated with a particular [Checklist](https://genomicsstandardsconsortium.github.io/mixs/#Checklists), [Extension](https://genomicsstandardsconsortium.github.io/mixs/#Extensions), or [Combination](https://genomicsstandardsconsortium.github.io/mixs/combinations/) (of one Checklist plus one Extension). 

* There is one template for each *Checklist*, *Extension* and *Combination* in the [schema](src/mixs/schema/mixs.yaml).

* There is one Checklist subfolder per Checklist, and a single Extensions-only subfolder.
  * The Checklist subfolders contain the template for that Checklist, as well as the templates for the Combinations that have been derived from that Checklist. 
  * The Extensions subfolder contains the templates for all the Extensions in the schema, independent of any Checklists.

### Limitations:
- The use of Excel spreadsheets is convenient, but is low on the [5-star linked data framework](https://www.w3.org/2011/gld/wiki/5_Star_Linked_Data), and not conducive to good implementations of the FAIR Principles. Open formats like TSV or CSV are preferred, and graph-friendly formats like JSON-LD or RDF encouraged.
- Excel files do not play well with GitHub: it is very difficult to view them or diff them within GitHub, and they take up more disk space than TSV or CSV
- These spreadsheets confound the **specification of a standard** and an **application that uses the standard** to collect data. The spreadsheets do not apply any validation to the entered metadata. They do provide one data entry convenience: pulldown menus are provided for filling out columns when there is a brief [enumeration](https://genomicsstandardsconsortium.github.io/mixs/enumerations/) of permissible values, like [window_type](https://genomicsstandardsconsortium.github.io/mixs/0000856/), but this [feature is disabled](https://linkml.io/linkml/generators/excel.html) if the total character length of the permissible values is more than 255, like [fao_class](https://genomicsstandardsconsortium.github.io/mixs/0001083/).
- Validation can be applied with the [linkml-validate](https://linkml.io/linkml/data/validating-data.html#the-linkml-validate-cli) command-line tool, but the Excel spreadsheets must be converted to TSV or CSV before running the validator.
