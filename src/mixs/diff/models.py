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
from typing import Dict, List, Optional, Any, Set


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
class MembershipChange:
    """Track a single membership change for a term in a checklist or package.

    This captures when a term is added to, removed from, or has its requirement
    level changed within a specific checklist or package.
    """
    term_name: str
    group_name: str  # checklist or package name
    group_type: str  # "checklist" or "package"
    old_requirement: Optional[str]  # None if added
    new_requirement: Optional[str]  # None if removed

    @property
    def change_type(self) -> str:
        """Determine the type of change."""
        if self.old_requirement is None:
            return "added"
        elif self.new_requirement is None:
            return "removed"
        elif self.old_requirement != self.new_requirement:
            return "requirement_changed"
        return "unchanged"

    @property
    def is_strengthened(self) -> bool:
        """Check if requirement was strengthened (X/- → M).

        Only applies to requirement changes, not additions/removals.
        """
        if self.change_type != "requirement_changed":
            return False
        weak = {"X", "x", "-", ""}
        strong = {"M", "m"}
        return (
            self.old_requirement in weak and
            self.new_requirement in strong
        )

    @property
    def is_weakened(self) -> bool:
        """Check if requirement was weakened (M → X/-).

        Only applies to requirement changes, not additions/removals.
        """
        if self.change_type != "requirement_changed":
            return False
        weak = {"X", "x", "-", ""}
        strong = {"M", "m"}
        return (
            self.old_requirement in strong and
            self.new_requirement in weak
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "term_name": self.term_name,
            "group_name": self.group_name,
            "group_type": self.group_type,
            "old_requirement": self.old_requirement,
            "new_requirement": self.new_requirement,
            "change_type": self.change_type,
        }


@dataclass
class MembershipComparison:
    """Complete membership comparison between two schemas.

    Tracks all changes in term membership within checklists and packages,
    including additions, removals, and requirement level changes.
    """
    # Individual changes
    checklist_changes: List[MembershipChange] = field(default_factory=list)
    package_changes: List[MembershipChange] = field(default_factory=list)

    # Aggregated views by group
    terms_added_to_checklists: Dict[str, List[str]] = field(default_factory=dict)
    terms_removed_from_checklists: Dict[str, List[str]] = field(default_factory=dict)
    terms_added_to_packages: Dict[str, List[str]] = field(default_factory=dict)
    terms_removed_from_packages: Dict[str, List[str]] = field(default_factory=dict)

    # Requirement changes
    made_mandatory: List[MembershipChange] = field(default_factory=list)  # X/- → M
    made_optional: List[MembershipChange] = field(default_factory=list)  # M → X/-

    def add_checklist_change(self, change: MembershipChange) -> None:
        """Add a checklist membership change and update aggregations."""
        self.checklist_changes.append(change)

        if change.change_type == "added":
            if change.group_name not in self.terms_added_to_checklists:
                self.terms_added_to_checklists[change.group_name] = []
            self.terms_added_to_checklists[change.group_name].append(change.term_name)
        elif change.change_type == "removed":
            if change.group_name not in self.terms_removed_from_checklists:
                self.terms_removed_from_checklists[change.group_name] = []
            self.terms_removed_from_checklists[change.group_name].append(change.term_name)

        if change.is_strengthened:
            self.made_mandatory.append(change)
        elif change.is_weakened:
            self.made_optional.append(change)

    def add_package_change(self, change: MembershipChange) -> None:
        """Add a package membership change and update aggregations."""
        self.package_changes.append(change)

        if change.change_type == "added":
            if change.group_name not in self.terms_added_to_packages:
                self.terms_added_to_packages[change.group_name] = []
            self.terms_added_to_packages[change.group_name].append(change.term_name)
        elif change.change_type == "removed":
            if change.group_name not in self.terms_removed_from_packages:
                self.terms_removed_from_packages[change.group_name] = []
            self.terms_removed_from_packages[change.group_name].append(change.term_name)

        if change.is_strengthened:
            self.made_mandatory.append(change)
        elif change.is_weakened:
            self.made_optional.append(change)

    def has_changes(self) -> bool:
        """Check if there are any membership changes."""
        return bool(self.checklist_changes or self.package_changes)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        result: Dict[str, Any] = {}

        # Build checklist changes grouped by checklist
        if self.checklist_changes:
            checklist_summary: Dict[str, Dict[str, Any]] = {}
            for change in self.checklist_changes:
                if change.group_name not in checklist_summary:
                    checklist_summary[change.group_name] = {
                        "terms_added": [],
                        "terms_removed": [],
                        "requirement_changes": {},
                    }
                summary = checklist_summary[change.group_name]
                if change.change_type == "added":
                    summary["terms_added"].append(change.term_name)
                elif change.change_type == "removed":
                    summary["terms_removed"].append(change.term_name)
                elif change.change_type == "requirement_changed":
                    summary["requirement_changes"][change.term_name] = {
                        "old": change.old_requirement,
                        "new": change.new_requirement,
                    }
            result["checklist_changes"] = checklist_summary

        # Build package changes grouped by package
        if self.package_changes:
            package_summary: Dict[str, Dict[str, Any]] = {}
            for change in self.package_changes:
                if change.group_name not in package_summary:
                    package_summary[change.group_name] = {
                        "terms_added": [],
                        "terms_removed": [],
                        "requirement_changes": {},
                    }
                summary = package_summary[change.group_name]
                if change.change_type == "added":
                    summary["terms_added"].append(change.term_name)
                elif change.change_type == "removed":
                    summary["terms_removed"].append(change.term_name)
                elif change.change_type == "requirement_changed":
                    summary["requirement_changes"][change.term_name] = {
                        "old": change.old_requirement,
                        "new": change.new_requirement,
                    }
            result["package_changes"] = package_summary

        # Add summary statistics
        result["summary"] = {
            "total_checklist_changes": len(self.checklist_changes),
            "total_package_changes": len(self.package_changes),
            "made_mandatory": len(self.made_mandatory),
            "made_optional": len(self.made_optional),
        }

        return result


@dataclass
class PackageCompositionChange:
    """Track composition changes for a single package."""
    package_name: str
    terms_added: List[str] = field(default_factory=list)
    terms_removed: List[str] = field(default_factory=list)

    def has_changes(self) -> bool:
        """Check if there are any composition changes."""
        return bool(self.terms_added or self.terms_removed)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "terms_added": sorted(self.terms_added),
            "terms_removed": sorted(self.terms_removed),
        }


@dataclass
class PackageCompositionComparison:
    """Complete package composition comparison between two schemas.

    Tracks which terms exist in each package, independent of membership
    requirement levels (which are tracked by MembershipComparison).
    """
    # Package name -> composition change
    changes: Dict[str, PackageCompositionChange] = field(default_factory=dict)

    # Packages only in old/new
    packages_only_in_old: Set[str] = field(default_factory=set)
    packages_only_in_new: Set[str] = field(default_factory=set)

    def has_changes(self) -> bool:
        """Check if there are any composition changes."""
        return bool(
            self.changes or
            self.packages_only_in_old or
            self.packages_only_in_new
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        result: Dict[str, Any] = {}

        if self.changes:
            result["composition_changes"] = {
                name: change.to_dict()
                for name, change in sorted(self.changes.items())
                if change.has_changes()
            }

        if self.packages_only_in_old:
            result["packages_only_in_old"] = sorted(self.packages_only_in_old)

        if self.packages_only_in_new:
            result["packages_only_in_new"] = sorted(self.packages_only_in_new)

        # Summary
        total_added = sum(len(c.terms_added) for c in self.changes.values())
        total_removed = sum(len(c.terms_removed) for c in self.changes.values())
        result["summary"] = {
            "packages_with_changes": len([c for c in self.changes.values() if c.has_changes()]),
            "total_terms_added": total_added,
            "total_terms_removed": total_removed,
        }

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
