# MIxS Version/Release Timeline - Final Report

## Summary

This table catalogs all known MIxS-related release artifacts with dates, organized chronologically. Each entry includes the methodology used to determine the date.

## Complete Artifact Table

| Version | Artifact | Date | Confidence | Methodology |
|---------|----------|------|------------|-------------|
| 0.x (draft) | `GSC_MIGS_checklist_07.doc` | 2005-01 | High | SourceForge `OldFiles/checklist.tar.gz` (uploaded 2006-04-13); Word doc header says "DRAFT for discussion - Jan, 2005"; file metadata: created 2006-01-25, last saved 2006-02-01, last printed 2005-10-27 |
| 1.1 | `MIGS_1.1._v1.docx` | 2006-09-27 | High | mixs-legacy `pre-2009/`; Word doc track changes XML shows edits 2006-09-08 to 2006-09-27; author: DFIELD |
| | `Migs.xsd` | 2006-11-13 | High | mixs-legacy `pre-2009/`; XSD internal XML comment: "Last update: Nov 13, 2006"; editor: Kelvin LI (JCVI) |
| 1.2 | `MIGS_1.2_Candidate_v3.docx` | 2007-05-28 | High | mixs-legacy `pre-2009/`; Word doc track changes XML shows edits 2007-05-27 to 2007-05-28; author: DFIELD |
| | GCDML 1.7.0 | 2009-01-25 | High | SourceForge `gcdml/gcdml-1.7.0-src.tar.gz`; file listing shows 2009-01-25 |
| 2.0 | `Migs_mims_miens_051109.xlsx` | 2009-11-05 | High | mixs-legacy `2009/`; xlsx internal `dcterms:created` = 2009-11-05T11:58:36Z; matches filename DDMMYY encoding; creator: Pelin Yilmaz |
| 2.0 | `Migs_mims_miens_231109.xlsx` | 2009-11-23 | Medium | mixs-legacy `2009/`; filename DDMMYY encoding; xlsx metadata corrupted (shows 2019 conversion date) |
| 2.0 | `MIGS_MIMS_18_10_10.xlsx` | 2010-10-18 | Medium | mixs-legacy `2010/`; filename DD_MM_YY encoding; xlsx metadata corrupted |
| 2.0 | `MIENS_18_10_10.xlsx` | 2010-10-18 | Medium | mixs-legacy `2010/`; filename DD_MM_YY encoding; no xlsx metadata |
| 2.0 | `MIENS_12_11_10.xlsx` | 2010-11-12 | High | mixs-legacy `2010/`; xlsx internal `dcterms:created` = 2010-11-12T13:46:45Z; matches filename |
| 2.0 | `MIGS_MIMS_07_12_10.xlsx` | 2010-12-07 | Medium | mixs-legacy `2010/`; filename DD_MM_YY encoding; xlsx metadata says 2010-12-01 (6 days earlier) |
| 2.1 | `MIMARKS_26_01_11.xlsx` | 2011-01-26 | Medium | mixs-legacy `2011/`; filename DD_MM_YY encoding; xlsx metadata says 2010-11-12 (template inheritance) |
| 2.1 | `Migs_mims_miens_v2.1.xlsx` | 2011 | Low | mixs-legacy `2011/`; filename version string only; xlsx metadata corrupted |
| 3.0 | **None** | 2011-05-06 | High | Yilmaz et al. Nat Biotechnol 29:415-420 (DOI: 10.1038/nbt.1823); paper introduces MIxS framework but assigns no version number; **conceptual only - no spreadsheet artifact exists** |
| 4.0 | `MIxS_v4.xls` | 2014-05-21 | Medium | mixs-legacy root; filename; git commit 9c66dc3 (2019-04-28) message "upload mixs 4.0"; 252KB |
| 4.0 | `MIxS_210514.xls` | 2014-05-21 | Medium | mixs-legacy `mixs4/`; filename DDMMYY encoding; git commit fd5f42b (2022-02-27); 239KB; 16 package files |
| 5.0 | `mixs_v5.xlsx` | 2018-06-21 | Medium | mixs-legacy `mixs5/`; filename on package files (`*_20180621.xlsx`) YYYYMMDD encoding; xlsx `dcterms:created` unreliable (shows 2010-12-01 template date) |
| 6.0.0 | `mixs6.0.0` tag | 2022-03-24 | High | GitHub releases API; `gh release view mixs6.0.0 --json createdAt` = 2022-03-23T17:09:46Z; publishedAt = 2022-03-24T16:07:38Z |
| 6.1.0 | `mixs6.1.0` tag | 2022-07-05 | High | GitHub releases API; createdAt = 2022-07-05T23:38:50Z |
| 6.1.1 | `mixs6.1.1` tag | 2023-10-09 | High | GitHub releases API; createdAt = 2023-09-21T14:23:30Z; publishedAt = 2023-10-09T13:40:04Z |
| 6.2.0 | `v6.2.0` tag | 2023-10-18 | High | GitHub releases API; createdAt = 2023-10-18T13:40:09Z |
| 6.2.1 | **Untagged** | 2025-12-09 | High | Git commit 69445c274 "Release v6.2.1 (#116)"; no GitHub release/tag created; superseded by v6.2.2 six days later |
| 6.2.2 | `v6.2.2` tag | 2025-12-15 | High | GitHub releases API; createdAt = 2025-12-15T17:02:51Z |
| 6.2.3 | `v6.2.3` tag | 2026-01-21 | High | GitHub releases API; createdAt = 2026-01-21T18:10:11Z |

## Methodology Summary

### Source Types and Reliability

| Source Type | Confidence | Notes |
|-------------|------------|-------|
| GitHub releases API | High | Precise timestamps from `gh release view <tag> --json createdAt,publishedAt` |
| Git commit dates | High | `git log --format="%ai"` |
| xlsx internal metadata | High (when matches filename) | `unzip -p <file> docProps/core.xml` extracts `dcterms:created` |
| Word doc track changes | High | `unzip -p <file> word/document.xml` extracts `w:date` attributes from revision history |
| XSD/XML internal comments | High | Direct inspection of file content |
| Filename date encoding | Medium | DDMMYY, DD_MM_YY, or YYYYMMDD patterns; no secondary confirmation |
| xlsx metadata (corrupted) | Low | Many files show 2019 conversion dates from Ramona Walls' xlsx conversion work |
| Publication DOI | High | Formal publication dates from PubMed/Nature |

### Key Findings

1. **Earliest artifact**: `GSC_MIGS_checklist_07.doc` from January 2005 (SourceForge)
2. **Version 3.0 never existed as a spreadsheet**: The 2011 Yilmaz paper introduced MIxS conceptually but the paper contains no version number; mixs-legacy has no v3 files
3. **v6.2.1 was created but never released**: Commit exists (2025-12-09) but no tag; superseded by v6.2.2
4. **Two different v4 files exist**: Root `MIxS_v4.xls` (252KB) differs from `mixs4/MIxS_210514.xls` (239KB)
5. **Date formats changed over time**: DDMMYY (2009-2014) → YYYYMMDD (2018)

### Data Sources

1. **GitHub repos**:
   - https://github.com/GenomicsStandardsConsortium/mixs (main repo, v6+)
   - https://github.com/GenomicsStandardsConsortium/mixs-legacy (pre-v6 spreadsheets)

2. **SourceForge**: https://sourceforge.net/projects/gensc/files/
   - `OldFiles/checklist.tar.gz` (2006-04-13) contains 2005 draft
   - `gcdml/gcdml-1.7.0-src.tar.gz` (2009-01-25)

3. **Publications**:
   - Field et al. 2008 (MIGS): DOI 10.1038/nbt1360
   - Yilmaz et al. 2011 (MIxS): DOI 10.1038/nbt.1823

### Commands Used

```bash
# GitHub releases
gh release list -R GenomicsStandardsConsortium/mixs
gh release view <tag> --json createdAt,publishedAt

# xlsx metadata extraction
unzip -p <file>.xlsx docProps/core.xml | xmllint --format -

# Word doc track changes dates
unzip -p <file>.docx word/document.xml | grep -oE 'w:date="[^"]+"' | sort -u

# XSD inspection
head -50 Migs.xsd | grep -i date

# Git history
git log --oneline --all | grep -i release
```

## Monotonicity Check

When ordered by date, versions increase monotonically with these caveats:
- XSD (2006-11-13) has no version number but falls between 1.1 and 1.2
- Version 2.0 spans ~14 months (2009-11 to 2010-12) with multiple file releases
- Version 3.0 is conceptual only (2011 publication)
