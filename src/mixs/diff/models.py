"""Dataclasses for normalized schema representation across all MIxS formats.

IMPORTANT: INTERNAL USE ONLY
============================
These data models are strictly for internal use by the mixs-legacy-diff tool.
They are NOT intended for:
- End-user applications
- External integrations
- Programmatic access to MIxS data
- Any use outside of generating comparison diffs

The structure of these classes may change without notice between versions.
For programmatic access to MIxS data, use the official LinkML-generated
data classes from `mixs.datamodel`.

Purpose:
    These models provide a common normalized representation that allows
    comparison between MIxS schemas from different eras and formats:
    - Excel spreadsheets (v2-v5, 2009-2018)
    - Word documents (pre-2009)
    - XSD schemas (2006)
    - LinkML YAML (v6+, 2020+)

    By normalizing to a common structure, we can generate meaningful diffs
    between any two versions regardless of their original format.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any


@dataclass
class NormalizedTerm:
    """Normalized representation of a MIxS term/field.

    This provides a common structure for terms from Excel, Word, XSD, or LinkML sources.
    """
    name: str  # Structured comment name (the unique identifier)
    item: str = ""  # Human-readable item name
    definition: str = ""
    example: str = ""
    expected_value: str = ""
    value_syntax: str = ""
    occurrence: str = ""  # M (mandatory), X (optional), etc.
    preferred_unit: str = ""
    section: str = ""  # Section/category the term belongs to
    position: str = ""  # Ordering position
    mixs_id: str = ""  # MIXS ID (v5+)

    # Package/checklist membership - maps package/checklist name to requirement level
    # e.g., {"migs_eu": "M", "migs_ba": "X", "air": "M"}
    checklist_membership: Dict[str, str] = field(default_factory=dict)
    package_membership: Dict[str, str] = field(default_factory=dict)

    # Additional metadata that may vary by format
    extra: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        result = {
            "name": self.name,
            "item": self.item,
            "definition": self.definition,
            "example": self.example,
            "expected_value": self.expected_value,
            "value_syntax": self.value_syntax,
            "occurrence": self.occurrence,
            "preferred_unit": self.preferred_unit,
            "section": self.section,
            "position": self.position,
            "mixs_id": self.mixs_id,
        }
        if self.checklist_membership:
            result["checklist_membership"] = self.checklist_membership
        if self.package_membership:
            result["package_membership"] = self.package_membership
        if self.extra:
            result["extra"] = self.extra
        return result


@dataclass
class NormalizedSchema:
    """Normalized representation of a complete MIxS schema.

    This provides a common structure regardless of source format.
    """
    version: str  # Version identifier (e.g., "v4", "v5", "v6.2.3")
    source_path: str  # Original file path or URL
    source_format: str  # Format: "xlsx", "xls", "docx", "xsd", "linkml"

    # Core term dictionary: name -> NormalizedTerm
    terms: Dict[str, NormalizedTerm] = field(default_factory=dict)

    # Package/checklist definitions
    # Maps package name to list of term names
    packages: Dict[str, List[str]] = field(default_factory=dict)

    # Maps checklist name to list of term names
    checklists: Dict[str, List[str]] = field(default_factory=dict)

    # Additional schema-level metadata
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "version": self.version,
            "source_path": self.source_path,
            "source_format": self.source_format,
            "term_count": len(self.terms),
            "package_count": len(self.packages),
            "checklist_count": len(self.checklists),
            "terms": {name: term.to_dict() for name, term in self.terms.items()},
            "packages": self.packages,
            "checklists": self.checklists,
            "metadata": self.metadata,
        }

    def get_term_names(self) -> List[str]:
        """Get sorted list of all term names."""
        return sorted(self.terms.keys())

    def get_package_names(self) -> List[str]:
        """Get sorted list of all package names."""
        return sorted(self.packages.keys())

    def get_checklist_names(self) -> List[str]:
        """Get sorted list of all checklist names."""
        return sorted(self.checklists.keys())

    def merge(self, other: "NormalizedSchema") -> None:
        """Merge another schema into this one.

        This combines terms, packages, and checklists from another schema.
        If a term exists in both, the existing term is preserved (first wins).

        Args:
            other: The schema to merge into this one.
        """
        # Merge terms (existing terms take precedence)
        for name, term in other.terms.items():
            if name not in self.terms:
                self.terms[name] = term

        # Merge packages (combine term lists, avoid duplicates)
        for pkg_name, term_names in other.packages.items():
            if pkg_name not in self.packages:
                self.packages[pkg_name] = []
            for term_name in term_names:
                if term_name not in self.packages[pkg_name]:
                    self.packages[pkg_name].append(term_name)

        # Merge checklists (combine term lists, avoid duplicates)
        for checklist_name, term_names in other.checklists.items():
            if checklist_name not in self.checklists:
                self.checklists[checklist_name] = []
            for term_name in term_names:
                if term_name not in self.checklists[checklist_name]:
                    self.checklists[checklist_name].append(term_name)
