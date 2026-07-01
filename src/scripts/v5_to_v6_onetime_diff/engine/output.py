"""YAML output formatting for schema comparison results."""

import logging
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path
from typing import List

import yaml

from .comparison import SchemaComparisonResult

logger = logging.getLogger(__name__)


def compute_inline_diff(old_text: str, new_text: str, max_len: int = 100) -> str:
    """Compute a simple inline diff showing changes.

    Returns a string like: "old text [-removed-] [+added+] more text"
    Truncates if result is too long.
    """
    if not old_text and not new_text:
        return "(no change)"
    if not old_text:
        return f"[+{new_text[:max_len]}+]" + ("..." if len(new_text) > max_len else "")
    if not new_text:
        return f"[-{old_text[:max_len]}-]" + ("..." if len(old_text) > max_len else "")

    # For short texts, just show old -> new
    if len(old_text) < 30 and len(new_text) < 30:
        return f"'{old_text}' → '{new_text}'"

    # Use SequenceMatcher for longer texts
    matcher = SequenceMatcher(None, old_text.split(), new_text.split())
    result_parts: List[str] = []

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        old_words = old_text.split()[i1:i2]
        new_words = new_text.split()[j1:j2]

        if tag == 'equal':
            # Show context (first/last few words)
            if len(old_words) <= 4:
                result_parts.append(' '.join(old_words))
            else:
                result_parts.append(' '.join(old_words[:2]) + ' ... ' + ' '.join(old_words[-2:]))
        elif tag == 'delete':
            result_parts.append('[-' + ' '.join(old_words[:5]) + ('-...]' if len(old_words) > 5 else '-]'))
        elif tag == 'insert':
            result_parts.append('[+' + ' '.join(new_words[:5]) + ('+...]' if len(new_words) > 5 else '+]'))
        elif tag == 'replace':
            result_parts.append('[-' + ' '.join(old_words[:3]) + '-]')
            result_parts.append('[+' + ' '.join(new_words[:3]) + '+]')

    result = ' '.join(result_parts)
    if len(result) > max_len:
        result = result[:max_len] + "..."
    return result


class ComparisonYAMLDumper(yaml.SafeDumper):
    """Custom YAML dumper for clean output."""
    pass


def str_representer(dumper, data):
    """Represent strings with proper formatting."""
    if '\n' in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)


ComparisonYAMLDumper.add_representer(str, str_representer)


def write_comparison_yaml(
    result: SchemaComparisonResult,
    output_dir: Path,
    filename: str = "schema_comparison_results.yaml",
    include_membership: bool = True,
) -> Path:
    """Write comparison results to YAML file.

    Args:
        result: The comparison result to write.
        output_dir: Directory to write output file.
        filename: Name of the output file.
        include_membership: Whether to include membership comparison in output.

    Returns:
        Path to the written file.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filename

    # Build output dict
    output_dict = result.to_dict()

    # Optionally remove membership sections
    if not include_membership:
        output_dict.pop("membership_differences", None)
        output_dict.pop("package_composition_differences", None)

    # Add timestamp
    output_dict["comparison_metadata"]["comparison_timestamp"] = datetime.now().isoformat()

    with open(output_path, 'w') as f:
        yaml.dump(
            output_dict,
            f,
            Dumper=ComparisonYAMLDumper,
            default_flow_style=False,
            sort_keys=True,  # stable key order so re-runs write the same file
            allow_unicode=True,
            width=120,
        )

    logger.info(f"Wrote comparison results to {output_path}")
    return output_path


def write_summary_report(
    result: SchemaComparisonResult,
    output_dir: Path,
    filename: str = "comparison_summary.md",
    include_membership: bool = True,
) -> Path:
    """Write human-readable summary report.

    Args:
        result: The comparison result to summarize.
        output_dir: Directory to write output file.
        filename: Name of the output file.
        include_membership: Whether to include membership comparison in output.

    Returns:
        Path to the written file.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filename

    old_info = result.old_schema_info
    new_info = result.new_schema_info
    md = []
    md.append(f"# MIxS schema comparison: {old_info.get('version', 'unknown')} to {new_info.get('version', 'unknown')}")
    md.append("")
    md.append(f"- **Old:** {old_info.get('version', 'unknown')} "
              f"({old_info.get('format', 'unknown')}), {old_info.get('term_count', 0)} terms. "
              f"Source: `{old_info.get('source', 'unknown')}`")
    md.append(f"- **New:** {new_info.get('version', 'unknown')} "
              f"({new_info.get('format', 'unknown')}), {new_info.get('term_count', 0)} terms. "
              f"Source: `{new_info.get('source', 'unknown')}`")
    md.append("")

    # Term comparison
    key_comp = result.term_key_comparison
    md.append("## Term comparison")
    md.append("")
    md.append(f"- Shared terms: {len(key_comp.shared)}")
    md.append(f"- Only in old: {len(key_comp.only_in_old)}")
    md.append(f"- Only in new: {len(key_comp.only_in_new)}")
    if key_comp.expected_mappings:
        md.append(f"- Renames applied: {len(key_comp.expected_mappings)}")
    md.append(f"- Terms with definition changes: {len(result.term_comparisons)}")
    md.append("")

    if key_comp.expected_mappings:
        md.append("### Renames applied")
        md.append("")
        for mapping in sorted(key_comp.expected_mappings)[:15]:
            md.append(f"- {mapping}")
        if len(key_comp.expected_mappings) > 15:
            md.append(f"- ... and {len(key_comp.expected_mappings) - 15} more")
        md.append("")

    if key_comp.expected_splits:
        md.append("### Term splits (1 old to N new)")
        md.append("")
        for old_name, new_names in sorted(key_comp.expected_splits.items()):
            md.append(f"- {old_name} to {', '.join(new_names)}")
        md.append("")

    if key_comp.expected_merges:
        md.append("### Term merges (N old to 1 new)")
        md.append("")
        for new_name, old_names in sorted(key_comp.expected_merges.items()):
            md.append(f"- {', '.join(old_names)} to {new_name}")
        md.append("")

    if key_comp.expected_deletions:
        md.append("### Terms intentionally removed")
        md.append("")
        for name, reason in sorted(key_comp.expected_deletions.items()):
            md.append(f"- {name}: {reason}")
        md.append("")

    if key_comp.only_in_old:
        md.append("### Terms only in old (removed)")
        md.append("")
        for name in sorted(key_comp.only_in_old)[:20]:
            md.append(f"- {name}")
        if len(key_comp.only_in_old) > 20:
            md.append(f"- ... and {len(key_comp.only_in_old) - 20} more")
        md.append("")

    if key_comp.only_in_new:
        md.append("### Terms only in new (added)")
        md.append("")
        for name in sorted(key_comp.only_in_new)[:20]:
            md.append(f"- {name}")
        if len(key_comp.only_in_new) > 20:
            md.append(f"- ... and {len(key_comp.only_in_new) - 20} more")
        md.append("")

    if result.term_comparisons:
        def_changes = [
            (name, comp)
            for name, comp in sorted(result.term_comparisons.items())
            if 'definition' in comp.field_differences
        ]
        if def_changes:
            md.append("## Definition changes")
            md.append("")
            for name, comp in def_changes[:10]:
                old_def, new_def = comp.field_differences.get('definition', ('', ''))
                diff_text = compute_inline_diff(old_def, new_def, max_len=120)
                md.append(f"- **{name}:** {diff_text}")
            if len(def_changes) > 10:
                md.append(f"- ... and {len(def_changes) - 10} more definition changes")
            md.append("")

    if result.package_key_comparison.shared or result.package_key_comparison.only_in_old or result.package_key_comparison.only_in_new:
        pkg_comp = result.package_key_comparison
        md.append("## Package comparison")
        md.append("")
        md.append(f"- Shared packages: {len(pkg_comp.shared)}")
        md.append(f"- Only in old: {len(pkg_comp.only_in_old)}")
        md.append(f"- Only in new: {len(pkg_comp.only_in_new)}")
        md.append("")

    if result.checklist_key_comparison.shared or result.checklist_key_comparison.only_in_old or result.checklist_key_comparison.only_in_new:
        cl_comp = result.checklist_key_comparison
        md.append("## Checklist comparison")
        md.append("")
        md.append(f"- Shared checklists: {len(cl_comp.shared)}")
        md.append(f"- Only in old: {len(cl_comp.only_in_old)}")
        md.append(f"- Only in new: {len(cl_comp.only_in_new)}")
        md.append("")

    if include_membership and result.membership_comparison.has_changes():
        mem_comp = result.membership_comparison
        checklist_added = sum(len(terms) for terms in mem_comp.terms_added_to_checklists.values())
        checklist_removed = sum(len(terms) for terms in mem_comp.terms_removed_from_checklists.values())
        package_added = sum(len(terms) for terms in mem_comp.terms_added_to_packages.values())
        package_removed = sum(len(terms) for terms in mem_comp.terms_removed_from_packages.values())
        md.append("## Membership changes")
        md.append("")
        md.append(f"- Terms added to checklists: {checklist_added}")
        md.append(f"- Terms removed from checklists: {checklist_removed}")
        md.append(f"- Terms added to packages: {package_added}")
        md.append(f"- Terms removed from packages: {package_removed}")
        md.append(f"- Made mandatory (was optional): {len(mem_comp.made_mandatory)}")
        md.append(f"- Made optional (was mandatory): {len(mem_comp.made_optional)}")
        md.append("")
        if mem_comp.made_mandatory:
            md.append("### Made mandatory")
            md.append("")
            for change in mem_comp.made_mandatory[:10]:
                md.append(f"- {change.term_name} in {change.group_name}: {change.old_requirement} to {change.new_requirement}")
            if len(mem_comp.made_mandatory) > 10:
                md.append(f"- ... and {len(mem_comp.made_mandatory) - 10} more")
            md.append("")
        if mem_comp.made_optional:
            md.append("### Made optional")
            md.append("")
            for change in mem_comp.made_optional[:10]:
                md.append(f"- {change.term_name} in {change.group_name}: {change.old_requirement} to {change.new_requirement}")
            if len(mem_comp.made_optional) > 10:
                md.append(f"- ... and {len(mem_comp.made_optional) - 10} more")
            md.append("")

    if include_membership and result.package_composition.has_changes():
        pkg_comp = result.package_composition
        md.append("## Package composition changes")
        md.append("")
        changes_with_content = [
            (name, change)
            for name, change in sorted(pkg_comp.changes.items())
            if change.has_changes()
        ]
        if changes_with_content:
            for pkg_name, change in changes_with_content[:15]:
                added_count = len(change.terms_added)
                removed_count = len(change.terms_removed)
                md.append(f"- **{pkg_name}:** +{added_count} terms, -{removed_count} terms")
                if change.terms_added:
                    added_list = sorted(change.terms_added)[:5]
                    added_str = ", ".join(added_list)
                    if len(change.terms_added) > 5:
                        added_str += f" (+{len(change.terms_added) - 5} more)"
                    md.append(f"    - added: {added_str}")
                if change.terms_removed:
                    removed_list = sorted(change.terms_removed)[:5]
                    removed_str = ", ".join(removed_list)
                    if len(change.terms_removed) > 5:
                        removed_str += f" (+{len(change.terms_removed) - 5} more)"
                    md.append(f"    - removed: {removed_str}")
            if len(changes_with_content) > 15:
                md.append(f"- ... and {len(changes_with_content) - 15} more packages")
            md.append("")
        if pkg_comp.packages_only_in_new:
            md.append("### Packages added")
            md.append("")
            for pkg in sorted(pkg_comp.packages_only_in_new):
                md.append(f"- {pkg}")
            md.append("")
        if pkg_comp.packages_only_in_old:
            md.append("### Packages removed")
            md.append("")
            for pkg in sorted(pkg_comp.packages_only_in_old):
                md.append(f"- {pkg}")
            md.append("")

    md.append("---")
    md.append(f"_Generated: {datetime.now().isoformat()}_")

    with open(output_path, 'w') as f:
        f.write('\n'.join(md) + '\n')

    logger.info(f"Wrote summary report to {output_path}")
    return output_path
