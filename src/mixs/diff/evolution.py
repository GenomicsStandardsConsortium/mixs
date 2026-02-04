"""Term evolution tracking across MIxS versions.

This module generates cross-version evolution reports showing the history
of each term through all schema versions.
"""

import yaml
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Any


@dataclass
class TermVersionState:
    """State of a term in a specific version."""
    exists: bool = False
    checklists: Dict[str, str] = field(default_factory=dict)  # checklist -> requirement
    packages: Dict[str, str] = field(default_factory=dict)  # package -> requirement
    definition: str = ""
    notes: str = ""


@dataclass
class TermEvolution:
    """Complete evolution history of a term."""
    canonical_name: str
    aliases: List[str] = field(default_factory=list)  # Other names this term has had
    versions: Dict[str, TermVersionState] = field(default_factory=dict)
    events: List[Dict[str, Any]] = field(default_factory=list)  # Timeline of changes


def load_diff_result(diff_dir: Path) -> Optional[Dict]:
    """Load a schema comparison result YAML."""
    yaml_path = diff_dir / "schema_comparison_results.yaml"
    if not yaml_path.exists():
        return None
    with open(yaml_path) as f:
        return yaml.safe_load(f)


def load_mapping_config(mapping_dir: Path) -> Optional[Dict]:
    """Load a mapping config YAML."""
    config_path = mapping_dir / "mapping_config.yaml"
    if not config_path.exists():
        return None
    with open(config_path) as f:
        return yaml.safe_load(f)


def build_term_evolution(
    diff_results_dir: Path,
    mappings_dir: Path,
) -> Dict[str, TermEvolution]:
    """Build term evolution from all diff results.

    Returns a dict mapping canonical term names to their evolution history.
    """
    # Define the version order with (diff_dir_name, mapping_dir_name, old_ver, new_ver)
    version_order = [
        ("v1.1_to_v1.2", "v1.1_to_v1.2", "v1.1", "v1.2"),
        ("v1.2_to_may2009", "v1.2_to_may2009", "v1.2", "v1.5-may2009"),
        ("may2009_to_nov2009", "may2009_to_nov2009", "v1.5-may2009", "v1.6-nov2009"),
        ("nov2009_to_oct2010", "nov2009_to_oct2010", "v1.6-nov2009", "v1.8-oct2010"),
        ("oct2010_to_v2.0", "oct2010_to_v2.0", "v1.8-oct2010", "v2.0"),
        ("v2.0_to_v2.1", "2.0_to_2.1", "v2.0", "v2.1"),
        ("v2.1_to_v4", "2.1_to_4", "v2.1", "v4"),
        ("v4_to_v5", "4_to_5", "v4", "v5"),
        ("v5_to_v6.0.0", "5_to_6", "v5", "v6.0.0"),
    ]

    # Track all terms and their states
    all_terms: Dict[str, TermEvolution] = {}

    # Track name mappings (old_name -> canonical_name)
    name_to_canonical: Dict[str, str] = {}

    # Process each diff in order
    for diff_dir_name, mapping_dir_name, old_ver, new_ver in version_order:
        diff_dir = diff_results_dir / diff_dir_name
        mapping_dir = mappings_dir / mapping_dir_name

        diff_result = load_diff_result(diff_dir)
        if not diff_result:
            continue

        mapping_config = load_mapping_config(mapping_dir) if mapping_dir.exists() else None

        # Get term info from diff
        term_diff = diff_result.get("term_differences", {})
        key_comp = term_diff.get("key_comparison", {})

        shared_terms = set(key_comp.get("shared", []))
        old_only = set(key_comp.get("only_in_old", []))
        new_only = set(key_comp.get("only_in_new", []))

        # Process mapping config to understand renames/splits/merges
        renames = {}
        splits = {}
        merges = {}
        deletions = {}

        if mapping_config:
            renames = mapping_config.get("renames", {})
            splits = mapping_config.get("splits", {})
            merges = mapping_config.get("merges", {})
            deletions = mapping_config.get("deletions", {})

        # Process renames
        for old_name, new_name in renames.items():
            canonical = name_to_canonical.get(old_name, old_name)
            name_to_canonical[new_name] = canonical
            name_to_canonical[old_name] = canonical

            if canonical not in all_terms:
                all_terms[canonical] = TermEvolution(canonical_name=canonical)

            if old_name != canonical and old_name not in all_terms[canonical].aliases:
                all_terms[canonical].aliases.append(old_name)
            if new_name != canonical and new_name not in all_terms[canonical].aliases:
                all_terms[canonical].aliases.append(new_name)

            all_terms[canonical].events.append({
                "version": new_ver,
                "event": "renamed",
                "from": old_name,
                "to": new_name,
            })

        # Process splits
        for old_name, new_names in splits.items():
            canonical = name_to_canonical.get(old_name, old_name)

            if canonical not in all_terms:
                all_terms[canonical] = TermEvolution(canonical_name=canonical)

            all_terms[canonical].events.append({
                "version": new_ver,
                "event": "split",
                "from": old_name,
                "to": new_names,
            })

            # Create entries for split targets
            for new_name in new_names:
                name_to_canonical[new_name] = new_name  # Each becomes its own canonical
                if new_name not in all_terms:
                    all_terms[new_name] = TermEvolution(canonical_name=new_name)
                all_terms[new_name].events.append({
                    "version": new_ver,
                    "event": "created_from_split",
                    "source": old_name,
                })

        # Process deletions
        for del_name, del_info in deletions.items():
            canonical = name_to_canonical.get(del_name, del_name)

            if canonical not in all_terms:
                all_terms[canonical] = TermEvolution(canonical_name=canonical)

            reason = del_info.get("reason", "") if isinstance(del_info, dict) else str(del_info)
            all_terms[canonical].events.append({
                "version": new_ver,
                "event": "removed",
                "reason": reason.strip(),
            })

        # Process shared terms (exist in both versions)
        for term in shared_terms:
            canonical = name_to_canonical.get(term, term)
            if canonical not in all_terms:
                all_terms[canonical] = TermEvolution(canonical_name=canonical)
                name_to_canonical[term] = canonical

            # Mark existence in both versions
            if old_ver not in all_terms[canonical].versions:
                all_terms[canonical].versions[old_ver] = TermVersionState(exists=True)
            if new_ver not in all_terms[canonical].versions:
                all_terms[canonical].versions[new_ver] = TermVersionState(exists=True)

        # Process terms only in old (removed or renamed)
        for term in old_only:
            if term in renames or term in splits or term in deletions:
                continue  # Already handled

            canonical = name_to_canonical.get(term, term)
            if canonical not in all_terms:
                all_terms[canonical] = TermEvolution(canonical_name=canonical)
                name_to_canonical[term] = canonical

            if old_ver not in all_terms[canonical].versions:
                all_terms[canonical].versions[old_ver] = TermVersionState(exists=True)

        # Process terms only in new (added)
        for term in new_only:
            # Check if this came from a split
            is_from_split = False
            for old_name, new_names in splits.items():
                if term in new_names:
                    is_from_split = True
                    break

            if is_from_split:
                continue  # Already handled

            canonical = name_to_canonical.get(term, term)
            if canonical not in all_terms:
                all_terms[canonical] = TermEvolution(canonical_name=canonical)
                name_to_canonical[term] = canonical
                all_terms[canonical].events.append({
                    "version": new_ver,
                    "event": "added",
                })

            if new_ver not in all_terms[canonical].versions:
                all_terms[canonical].versions[new_ver] = TermVersionState(exists=True)

        # Add membership info from diff results
        membership = diff_result.get("membership_differences", {})
        checklist_changes = membership.get("checklist_changes", {})

        for checklist, changes in checklist_changes.items():
            req_changes = changes.get("requirement_changes", {})
            for term, req_info in req_changes.items():
                canonical = name_to_canonical.get(term, term)
                if canonical in all_terms:
                    if new_ver not in all_terms[canonical].versions:
                        all_terms[canonical].versions[new_ver] = TermVersionState(exists=True)
                    all_terms[canonical].versions[new_ver].checklists[checklist] = req_info.get("new", "")

    return all_terms


def generate_evolution_report(
    diff_results_dir: Path,
    mappings_dir: Path,
    output_path: Path,
) -> None:
    """Generate a term evolution YAML report."""

    evolution = build_term_evolution(diff_results_dir, mappings_dir)

    # Convert to serializable format
    report = {
        "metadata": {
            "description": "MIxS term evolution across all versions",
            "version_chain": [
                "v1.1", "v1.2", "v1.5-may2009", "v1.6-nov2009",
                "v1.8-oct2010", "v2.0", "v2.1", "v4", "v5", "v6.0.0"
            ],
        },
        "terms": {},
    }

    for name, term_evo in sorted(evolution.items()):
        term_data = {
            "canonical_name": term_evo.canonical_name,
        }

        if term_evo.aliases:
            term_data["aliases"] = term_evo.aliases

        if term_evo.events:
            term_data["events"] = term_evo.events

        if term_evo.versions:
            term_data["versions"] = {
                ver: {
                    "exists": state.exists,
                    **({"checklists": state.checklists} if state.checklists else {}),
                    **({"packages": state.packages} if state.packages else {}),
                }
                for ver, state in sorted(term_evo.versions.items())
            }

        report["terms"][name] = term_data

    # Write report
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        yaml.dump(report, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    print(f"Generated evolution report: {output_path}")
    print(f"  Total terms tracked: {len(report['terms'])}")

    # Summary stats
    total_events = sum(len(t.get("events", [])) for t in report["terms"].values())
    print(f"  Total evolution events: {total_events}")


if __name__ == "__main__":
    import sys

    diff_results_dir = Path("assets/diff_results")
    mappings_dir = Path("assets/between_diff_mappings")
    output_path = Path("assets/diff_results/term_evolution.yaml")

    if len(sys.argv) > 1:
        output_path = Path(sys.argv[1])

    generate_evolution_report(diff_results_dir, mappings_dir, output_path)
