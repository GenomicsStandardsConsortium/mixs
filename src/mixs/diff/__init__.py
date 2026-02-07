"""MIxS Legacy Diff Tool - Compare MIxS schemas across any combination of formats and versions.

This module provides tools for comparing MIxS schemas across different formats:
- Excel (.xls, .xlsx) from MIxS v2-v5 (2009-2018)
- Word (.docx) from pre-2009 specifications
- XSD (.xsd) from 2006 MIGS schema
- LinkML YAML from v6+ (2020+)

Installation:
    This tool requires optional dependencies. Install with:
        poetry install --with legacy-diff

Usage:
    The primary interface is the `mixs-legacy-diff` CLI command:

        mixs-legacy-diff --old path/to/old.xlsx --new path/to/new.yaml

    See `mixs-legacy-diff --help` for full documentation.

IMPORTANT: Internal Data Models
==============================
The NormalizedTerm and NormalizedSchema classes exported from this module
are INTERNAL data structures used only for generating comparison diffs.
They are NOT intended for end-user applications or external integrations.
The structure may change without notice. For programmatic MIxS access,
use the official LinkML data classes from `mixs.datamodel`.
"""

from mixs.diff.models import NormalizedTerm, NormalizedSchema
from mixs.diff.comparison import LegacySchemaComparator

__all__ = ["NormalizedTerm", "NormalizedSchema", "LegacySchemaComparator"]
