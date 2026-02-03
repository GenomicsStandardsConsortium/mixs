# XSD Parallel Branch Analysis

## Summary

The 2006 `Migs.xsd` file represents a **parallel implementation branch** that was not adopted into the main MIxS specification lineage. This document explains why it is not included in the main diff chain.

## Evidence

### Term Count Disparity

| Schema | Term Count |
|--------|------------|
| Word v1.2 | 19 |
| XSD | 161 |
| May 2009 Excel | 57 |

The XSD has 8x more terms than the Word spec it supposedly succeeds, and 3x more than the Excel that follows.

### Overlap Analysis

| Comparison | Shared Terms | Percentage |
|------------|--------------|------------|
| v1.2 Word → May 2009 | 11 / 19 | 58% |
| XSD → May 2009 | 16 / 161 | 10% |

May 2009 Excel has much stronger continuity with the Word docs than with the XSD.

### Unique XSD Terms

139 terms appear ONLY in the XSD and never in any Word doc or Excel file. These include:
- Environmental measurement parameters: `alkalinity`, `chlorophyl`, `conductivity`, `dissolved_oxygen`, `nitrogen_speciation`, `phosphate`, `pressure`, `salinity`, `temperature`
- XML infrastructure: `decimal`, `degrees`, `direction_latitude`, `direction_longitude`, `unit`, `value`
- Detailed metadata: `accession`, `biosample`, `gcat_identifier`, `genome_project_id`, `ncbi_status`, `taxid`

## Interpretation

The XSD appears to be a **detailed implementation schema** created for:
1. XML-based data validation and submission
2. Environmental parameter capture (what later became "environmental packages")
3. Integration with NCBI/GOLD databases

It was likely a parallel effort that ran alongside the main specification development (Word → Excel) but was never fully adopted as THE specification.

## Main Lineage

The correct main lineage is:

```
Word v1.1 → Word v1.2 → May 2009 Excel → Nov 2009 → Oct 2010 → v2.0 → v2.1 → v4 → v5 → v6.0.0
```

## XSD Content Summary

For reference, the XSD contains 161 terms across these categories:

### Core MIGS Fields (shared with main lineage)
- `assembly`, `biotic_relationship`, `encoded_traits`, `estimated_size`
- `finishing_strategy`, `host`, `propagation`, `sequencing_method`
- `source_material_identifiers`, `trophic_level`

### Environmental Measurements (never adopted)
- Physical: `altitude`, `depth`, `pressure`, `temperature`
- Chemical: `alkalinity`, `conductivity`, `dissolved_oxygen`, `e_h`, `ph`
- Nutrients: `nitrogen_speciation`, `phosphate`, `phosphorus_speciation`
- Biological: `chlorophyl`, `light_intensity`

### Database Integration (partially adopted later)
- `accession`, `biosample`, `taxid`, `genome_project_id`

## File Location

The original XSD file: `mixs-legacy/pre-2009/Migs.xsd`
