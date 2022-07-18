# depth (_inferred title, i.e. title or slot name_)

### _Questions_

* _what LinkML prefix should that path use?_
* _what w3id redirection rules?_

### _style notes_:

- _term names should start with a lowercase letter_
- _term names should not contain any whitespace or non-ASCII characters_
- _presumably, the URI would be path/mixs/0000018.html_
- _show the cardinality code meanings_

_Here's the  way [MIxS 6 term updates:MIxS6 Core- Final_clean](https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/edit#gid=178015749) models slots:_

| Structured comment name   | depth                                                                                                                                                                                                    |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Item (rdfs:label)         | depth                                                                                                                                                                                                    |
| Definition                | The vertical distance below local surface, e.g. for sediment or soil samples depth is measured from sediment or soil surface, respectively. Depth can be reported as an interval for subsurface samples. |
| Expected value            | measurement value                                                                                                                                                                                        |
| Value syntax              | {float} {unit}                                                                                                                                                                                           |
| Example                   | 10 meter                                                                                                                                                                                                 |
| Section                   | environment                                                                                                                                                                                              |
| migs_eu                   | E                                                                                                                                                                                                        |
| migs_ba                   | E                                                                                                                                                                                                        |
| migs_pl                   | E                                                                                                                                                                                                        |
| migs_vi                   | E                                                                                                                                                                                                        |
| migs_org                  | E                                                                                                                                                                                                        |
| mims                      | E                                                                                                                                                                                                        |
| mimarks_s                 | E                                                                                                                                                                                                        |
| mimarks_c                 | E                                                                                                                                                                                                        |
| misag                     | E                                                                                                                                                                                                        |
| mimag                     | E                                                                                                                                                                                                        |
| miuvig                    | E                                                                                                                                                                                                        |
| Preferred unit            |                                                                                                                                                                                                          |
| Occurence                 | 1                                                                                                                                                                                                        |
| MIXS ID                   | MIXS:0000018                                                                                                                                                                                             |
| MIGS ID (mapping to GOLD) | MIGS-4.3                                                                                                                                                                                                 |

## aliases:

- depth

## description (_definition?_)

- The vertical distance below local surface, e.g. for sediment or soil
  samples depth is measured from sediment or soil surface, respectively. Depth
  can be reported as an interval for subsurface samples.

## multivalued:

- False

## parent

- [environment field](environment_field.md)

## range:

- quantity value (_link!_)

## required (_may depend on usage_):

- False

## slot_uri

- MIXS:0000018

## _show slot usage inline or as links_

## YAML Source

```yaml
depth:
name: depth
title: depth
description: The vertical distance below local surface, e.g. for sediment or soil
  samples depth is measured from sediment or soil surface, respectively. Depth
  can be reported as an interval for subsurface samples.
is_a: environment field
range: quantity value
slot_uri: MIXS:0000018
multivalued: false
aliases:
  - depth

annotations:
  expected_value:
    tag: expected_value
    value: measurement value
examples:
  - value: 10 meter

from_schema: http://w3id.org/mixs
```

