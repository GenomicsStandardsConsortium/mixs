# schemasheets for MIxS

Based on the assumption that LinkML is a good format for both describing the MIxS standard **and** provides good
infrastructure for collecting, converting and validating data intended to follow MIxS...

[schemasheets](https://linkml.io/schemasheets/) is a system for using delimited text files to specify
a [LinkML](https://linkml.io/) schema. The sheets are traditionally tab-separated (TSV) but CSV could also be taken into
consideration. The sheets are compiled down to a LinkML schema (serialized as
a [YAML](https://en.wikipedia.org/wiki/YAML) file) by
the [sheets2linkml](https://linkml.io/schemasheets/intro/converting/) command.

Notes:

- the standard execution of sheets2linkml converts one or more sheets into a single YAML output file. Chris Mungall has
  already demonstrated conversion of
  the [MIxS 6 term updates](https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/edit#gid=750683809)
  sheets to LinkML by using `gsctools/mixs_converter.py`. That approach generated several modular YAML files, which may
  be preferable in some circumstances. (But its inner workings were less transparent than a schemasheets approach). We
  can revisit multi-YAML output in the future. That will require adding a mode in sheets2linkml that asserts
  LinkML `import` statements.

List of MIxS schemasheets:

- sheets for describing the schema itself. these should not require ongoing maintenance, but should be spot checked
  before the first schemasheets-based MIxS release.
    - schema.tsv
    - prefixes.tsv
    - utility_classes.tsv
- The MIxS 6 term updates sheets do not provide any metadata about classes like environmental packages or checklists. We
  do specify them with schemasheets.
    - checklist_classes.tsv
    - env_package_classes.tsv
    - utility_classes.tsv
- sections_as_parent_slots.tsv
    - expresses the relationship between MIxS terms and sections
- enums.tsv
    - these are separated from teh term definitions for better reuse
- (todo) terms.tsv
    - this will aggregate term knowledge from the MIxS 6 term updates "core" and "packages" sheets. Associations between
      classes and terms will be expressed in other sheets.
- (todo) term_class_associations.tsv
    - this will aggregate term knowledge from the MIxS 6 term updates "core" and "packages" sheets. Associations between
      classes and terms will be expressed in other sheets.
- (todo) term_usage_in_packages.tsv
    - this will provide some functionality of the MIxS 6 term updates "packages" sheets, namely allowing package
      contributors to override a subset of the attributes of a term, when used in combination with a particular
      environmental package.

to be continued...

Please contribute!

- schemasheets uses multiple custom header rows. The first row can contain whatever headers are already well-known to
  the community. Second and subsequent rows require a greater than `>` symbol as the first character in the first
  column. The second row's values **must** consist of LinkML element names (or other schemasheets shortcuts). Third and
  subsequent rows specify special handling, such as indicating a separator for multivalued LinkML elements or declaring
  annotation keys.
- The LinkML common metadata page is a good place to lean about LinkML terms that could be used in almost any
  schemasheets sheet.
- 