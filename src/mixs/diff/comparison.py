"""Format-agnostic comparison logic for MIxS schemas."""

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional, Any

from mixs.diff.models import NormalizedSchema, NormalizedTerm

logger = logging.getLogger(__name__)


@dataclass
class TermComparison:
    """Comparison result for a single term."""
    term_name: str
    old_term: Optional[NormalizedTerm]
    new_term: Optional[NormalizedTerm]
    field_differences: Dict[str, Tuple[str, str]] = field(default_factory=dict)

    def has_differences(self) -> bool:
        """Check if this term has any differences."""
        return bool(self.field_differences)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        result = {"term_name": self.term_name}
        if self.field_differences:
            result["differences"] = {
                field: {"old": old_val, "new": new_val}
                for field, (old_val, new_val) in self.field_differences.items()
            }
        return result


@dataclass
class KeyComparison:
    """Comparison of keys between old and new schemas."""
    only_in_old: Set[str] = field(default_factory=set)
    only_in_new: Set[str] = field(default_factory=set)
    shared: Set[str] = field(default_factory=set)
    expected_mappings: Set[str] = field(default_factory=set)
    expected_splits: Dict[str, List[str]] = field(default_factory=dict)  # old -> [new1, new2]
    expected_merges: Dict[str, List[str]] = field(default_factory=dict)  # new -> [old1, old2]
    expected_deletions: Dict[str, str] = field(default_factory=dict)  # old -> reason

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        result = {}
        if self.shared:
            result["shared"] = sorted(self.shared)
        if self.only_in_old:
            result["only_in_old"] = sorted(self.only_in_old)
        if self.only_in_new:
            result["only_in_new"] = sorted(self.only_in_new)
        if self.expected_mappings:
            result["expected_mappings"] = sorted(self.expected_mappings)
        if self.expected_splits:
            result["expected_splits"] = {k: sorted(v) for k, v in sorted(self.expected_splits.items())}
        if self.expected_merges:
            result["expected_merges"] = {k: sorted(v) for k, v in sorted(self.expected_merges.items())}
        if self.expected_deletions:
            result["expected_deletions"] = dict(sorted(self.expected_deletions.items()))
        return result


@dataclass
class SchemaComparisonResult:
    """Complete comparison result between two schemas."""
    old_schema_info: Dict[str, Any]
    new_schema_info: Dict[str, Any]

    # Term comparisons
    term_key_comparison: KeyComparison = field(default_factory=KeyComparison)
    term_comparisons: Dict[str, TermComparison] = field(default_factory=dict)

    # Package comparisons
    package_key_comparison: KeyComparison = field(default_factory=KeyComparison)

    # Checklist comparisons
    checklist_key_comparison: KeyComparison = field(default_factory=KeyComparison)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        # Build term differences
        term_differences = {
            "key_comparison": self.term_key_comparison.to_dict(),
        }

        # Add definition changes for terms with differences
        definition_changes = {}
        for name, comp in self.term_comparisons.items():
            if comp.has_differences():
                definition_changes[name] = comp.to_dict()["differences"]
        if definition_changes:
            term_differences["definition_changes"] = definition_changes

        result = {
            "comparison_metadata": {
                "old_schema": self.old_schema_info,
                "new_schema": self.new_schema_info,
            },
            "term_differences": term_differences,
        }

        # Add package comparison if present
        if self.package_key_comparison.shared or self.package_key_comparison.only_in_old or self.package_key_comparison.only_in_new:
            result["package_differences"] = {
                "key_comparison": self.package_key_comparison.to_dict(),
            }

        # Add checklist comparison if present
        if self.checklist_key_comparison.shared or self.checklist_key_comparison.only_in_old or self.checklist_key_comparison.only_in_new:
            result["checklist_differences"] = {
                "key_comparison": self.checklist_key_comparison.to_dict(),
            }

        return result


@dataclass
class MappingConfig:
    """Extended mapping configuration including renames, splits, merges, and deletions."""
    renames: Dict[str, str] = field(default_factory=dict)
    splits: Dict[str, List[str]] = field(default_factory=dict)  # 1:N old -> [new1, new2]
    split_descriptions: Dict[str, str] = field(default_factory=dict)
    merges: Dict[str, List[str]] = field(default_factory=dict)  # N:1 new_name -> [old1, old2]
    merge_descriptions: Dict[str, str] = field(default_factory=dict)
    deletions: Dict[str, str] = field(default_factory=dict)  # term -> reason


class LegacySchemaComparator:
    """Compare two NormalizedSchema instances."""

    def __init__(
        self,
        name_mappings: Optional[Dict[str, str]] = None,
        mapping_config: Optional[MappingConfig] = None,
        ignore_fields: Optional[Set[str]] = None,
    ):
        """Initialize comparator.

        Args:
            name_mappings: Optional dict mapping old term names to new term names.
                          Deprecated: use mapping_config instead.
            mapping_config: Optional extended mapping configuration.
            ignore_fields: Optional set of field names to ignore in comparison.
        """
        # Support both old-style name_mappings and new mapping_config
        if mapping_config:
            self.mapping_config = mapping_config
            self.name_mappings = mapping_config.renames
        else:
            self.mapping_config = MappingConfig(renames=name_mappings or {})
            self.name_mappings = name_mappings or {}
        self.ignore_fields = ignore_fields or {"position", "mixs_id"}

    def compare(
        self,
        old_schema: NormalizedSchema,
        new_schema: NormalizedSchema,
    ) -> SchemaComparisonResult:
        """Compare two schemas and return detailed comparison result.

        Args:
            old_schema: The older schema to compare.
            new_schema: The newer schema to compare.

        Returns:
            SchemaComparisonResult with all comparison details.
        """
        old_info = {
            "version": old_schema.version,
            "source": old_schema.source_path,
            "format": old_schema.source_format,
            "term_count": len(old_schema.terms),
        }
        if old_schema.metadata.get("notes"):
            old_info["notes"] = old_schema.metadata["notes"]

        new_info = {
            "version": new_schema.version,
            "source": new_schema.source_path,
            "format": new_schema.source_format,
            "term_count": len(new_schema.terms),
        }
        if new_schema.metadata.get("notes"):
            new_info["notes"] = new_schema.metadata["notes"]

        result = SchemaComparisonResult(
            old_schema_info=old_info,
            new_schema_info=new_info,
        )

        # Compare terms
        self._compare_terms(old_schema, new_schema, result)

        # Compare packages
        self._compare_collections(
            old_schema.packages,
            new_schema.packages,
            result.package_key_comparison,
        )

        # Compare checklists
        self._compare_collections(
            old_schema.checklists,
            new_schema.checklists,
            result.checklist_key_comparison,
        )

        return result

    def _compare_terms(
        self,
        old_schema: NormalizedSchema,
        new_schema: NormalizedSchema,
        result: SchemaComparisonResult,
    ) -> None:
        """Compare terms between schemas."""
        old_names = set(old_schema.terms.keys())
        new_names = set(new_schema.terms.keys())

        # Track terms accounted for by splits, merges, and deletions
        accounted_old = set()
        accounted_new = set()

        # Process splits (1:N old -> [new1, new2])
        for old_name, new_names_list in self.mapping_config.splits.items():
            if old_name in old_names:
                # Check if all split targets exist in new schema
                found_targets = [n for n in new_names_list if n in new_names]
                if found_targets:
                    result.term_key_comparison.expected_splits[old_name] = found_targets
                    accounted_old.add(old_name)
                    accounted_new.update(found_targets)

        # Process merges (N:1 [old1, old2] -> new)
        for new_name, old_names_list in self.mapping_config.merges.items():
            if new_name in new_names:
                # Check if any merge sources exist in old schema
                found_sources = [n for n in old_names_list if n in old_names]
                if found_sources:
                    result.term_key_comparison.expected_merges[new_name] = found_sources
                    accounted_old.update(found_sources)
                    accounted_new.add(new_name)

        # Process deletions
        for old_name, reason in self.mapping_config.deletions.items():
            if old_name in old_names and old_name not in new_names:
                result.term_key_comparison.expected_deletions[old_name] = reason
                accounted_old.add(old_name)

        # Apply name mappings (renames)
        if self.name_mappings:
            unique_old, unique_new, expected = self._filter_expected_mappings(
                old_names - accounted_old, new_names - accounted_new, self.name_mappings
            )
            result.term_key_comparison.only_in_old = unique_old
            result.term_key_comparison.only_in_new = unique_new
            result.term_key_comparison.expected_mappings = expected
        else:
            result.term_key_comparison.only_in_old = (old_names - new_names) - accounted_old
            result.term_key_comparison.only_in_new = (new_names - old_names) - accounted_new

        result.term_key_comparison.shared = old_names & new_names

        # Compare shared terms
        for name in result.term_key_comparison.shared:
            old_term = old_schema.terms[name]
            new_term = new_schema.terms[name]
            comp = self._compare_term_fields(name, old_term, new_term)
            if comp.has_differences():
                result.term_comparisons[name] = comp

        # Compare mapped terms (renames)
        for old_name, new_name in self.name_mappings.items():
            if old_name in old_schema.terms and new_name in new_schema.terms:
                old_term = old_schema.terms[old_name]
                new_term = new_schema.terms[new_name]
                mapped_key = f"{old_name} -> {new_name}"
                comp = self._compare_term_fields(mapped_key, old_term, new_term)
                if comp.has_differences():
                    result.term_comparisons[mapped_key] = comp

    def _compare_term_fields(
        self,
        name: str,
        old_term: NormalizedTerm,
        new_term: NormalizedTerm,
    ) -> TermComparison:
        """Compare fields between two terms."""
        comp = TermComparison(
            term_name=name,
            old_term=old_term,
            new_term=new_term,
        )

        # Compare standard fields
        fields_to_compare = [
            "item", "definition", "example", "expected_value",
            "value_syntax", "occurrence", "preferred_unit", "section",
        ]

        for field_name in fields_to_compare:
            if field_name in self.ignore_fields:
                continue

            old_val = getattr(old_term, field_name, "")
            new_val = getattr(new_term, field_name, "")

            # Normalize for comparison
            old_normalized = self._normalize_value(old_val)
            new_normalized = self._normalize_value(new_val)

            if old_normalized != new_normalized:
                comp.field_differences[field_name] = (old_val, new_val)

        return comp

    def _compare_collections(
        self,
        old_collection: Dict[str, List[str]],
        new_collection: Dict[str, List[str]],
        key_comparison: KeyComparison,
    ) -> None:
        """Compare collection keys (packages or checklists)."""
        old_keys = set(old_collection.keys())
        new_keys = set(new_collection.keys())

        key_comparison.only_in_old = old_keys - new_keys
        key_comparison.only_in_new = new_keys - old_keys
        key_comparison.shared = old_keys & new_keys

    def _filter_expected_mappings(
        self,
        old_keys: Set[str],
        new_keys: Set[str],
        mappings: Dict[str, str],
    ) -> Tuple[Set[str], Set[str], Set[str]]:
        """Filter out expected name changes based on mappings."""
        unique_old = set()
        expected_mappings = set()
        accounted_new_keys = set()

        for old_key in old_keys:
            if old_key in mappings:
                expected_new_key = mappings[old_key]
                if expected_new_key in new_keys:
                    expected_mappings.add(f"{old_key} -> {expected_new_key}")
                    accounted_new_keys.add(expected_new_key)
                else:
                    unique_old.add(old_key)
            else:
                if old_key in new_keys:
                    accounted_new_keys.add(old_key)
                else:
                    unique_old.add(old_key)

        unique_new = new_keys - accounted_new_keys

        return unique_old, unique_new, expected_mappings

    def _normalize_value(self, value: str) -> str:
        """Normalize value for comparison."""
        if not value:
            return ""
        # Normalize whitespace
        normalized = " ".join(value.split())
        return normalized.lower()


def load_name_mappings(mappings_dir: Path) -> Dict[str, str]:
    """Load term name mappings from TSV file.

    Args:
        mappings_dir: Directory containing mapping TSV files.

    Returns:
        Dict mapping old term names to new term names.
    """
    mappings = {}
    mapping_file = mappings_dir / "slot_name_mappings.tsv"

    if not mapping_file.exists():
        logger.warning(f"Mapping file not found: {mapping_file}")
        return mappings

    try:
        with open(mapping_file, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i == 0:  # Skip header
                    continue
                parts = line.strip().split('\t')
                if len(parts) >= 2:
                    old_name, new_name = parts[0], parts[1]
                    mappings[old_name] = new_name
        logger.info(f"Loaded {len(mappings)} name mappings")
    except Exception as e:
        logger.error(f"Could not load name mappings: {e}")

    return mappings


def load_mapping_config(mappings_dir: Path) -> MappingConfig:
    """Load extended mapping configuration from YAML file.

    Args:
        mappings_dir: Directory containing mapping files.

    Returns:
        MappingConfig with renames, splits, and deletions.
    """
    import yaml

    config = MappingConfig()
    config_file = mappings_dir / "mapping_config.yaml"

    if not config_file.exists():
        # Fall back to TSV-only mode
        config.renames = load_name_mappings(mappings_dir)
        return config

    try:
        with open(config_file, 'r') as f:
            data = yaml.safe_load(f) or {}

        config.renames = data.get('renames', {}) or {}

        # Load splits with descriptions (1:N old -> [new1, new2])
        splits_data = data.get('splits', {}) or {}
        for old_name, split_info in splits_data.items():
            if isinstance(split_info, list):
                config.splits[old_name] = split_info
            elif isinstance(split_info, dict):
                config.splits[old_name] = split_info.get('targets', split_info.get('new_names', []))
                if 'description' in split_info:
                    config.split_descriptions[old_name] = split_info['description']

        # Load merges with descriptions (N:1 [old1, old2] -> new)
        merges_data = data.get('merges', {}) or {}
        for new_name, merge_info in merges_data.items():
            if isinstance(merge_info, list):
                config.merges[new_name] = merge_info
            elif isinstance(merge_info, dict):
                config.merges[new_name] = merge_info.get('sources', merge_info.get('old_names', []))
                if 'description' in merge_info:
                    config.merge_descriptions[new_name] = merge_info['description']

        # Load deletions with reasons
        deletions_data = data.get('deletions', {}) or {}
        for old_name, deletion_info in deletions_data.items():
            if isinstance(deletion_info, str):
                config.deletions[old_name] = deletion_info
            elif isinstance(deletion_info, dict):
                config.deletions[old_name] = deletion_info.get('reason', 'Removed')

        logger.info(f"Loaded mapping config: {len(config.renames)} renames, "
                   f"{len(config.splits)} splits, {len(config.merges)} merges, "
                   f"{len(config.deletions)} deletions")

    except Exception as e:
        logger.error(f"Could not load mapping config: {e}")

    return config
