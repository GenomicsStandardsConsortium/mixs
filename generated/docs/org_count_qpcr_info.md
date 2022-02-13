
# Slot: org_count_qpcr_info


If qpcr was used for the cell count, the target gene name, the primer sequence and the cycling conditions should also be provided. (Example: 16S rrna; FWD:ACGTAGCTATGACGT REV:GTGCTAGTCGAGTAC; initial denaturation:90C_5min; denaturation:90C_2min; annealing:52C_30 sec; elongation:72C_30 sec; 90 C for 1 min; final elongation:72C_5min; 30 cycles)

URI: [mixs.vocab:org_count_qpcr_info](https://w3id.org/mixs/vocab/org_count_qpcr_info)


## Domain and Range

None &#8594;  <sub>0..1</sub> [String](types/String.md)

## Parents

 *  is_a: [core field](core_field.md)

## Children

 *  [hydrocarbon resources-cores➞org_count_qpcr_info](hydrocarbon_resources_cores_org_count_qpcr_info.md)
 *  [hydrocarbon resources-fluids_swabs➞org_count_qpcr_info](hydrocarbon_resources_fluids_swabs_org_count_qpcr_info.md)

## Used by


## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | organism count qPCR information |
| **Mappings:** | | MIXS:0000099 |
| **Comments:** | | Expected value: gene name;FWD:forward primer sequence;REV:reverse primer sequence;initial denaturation:degrees_minutes;denaturation:degrees_minutes;annealing:degrees_minutes;elongation:degrees_minutes;final elongation:degrees_minutes; total cycles |
|  | | Preferred unit: number of cells per gram (or ml or cm^2) |
| **Examples:** | | Example(value='', description=None) |

