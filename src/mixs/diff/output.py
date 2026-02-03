"""YAML output formatting for schema comparison results."""

import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

import yaml

from mixs.diff.comparison import SchemaComparisonResult

logger = logging.getLogger(__name__)


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
) -> Path:
    """Write comparison results to YAML file.

    Args:
        result: The comparison result to write.
        output_dir: Directory to write output file.
        filename: Name of the output file.

    Returns:
        Path to the written file.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filename

    # Build output dict
    output_dict = result.to_dict()

    # Add timestamp
    output_dict["comparison_metadata"]["comparison_timestamp"] = datetime.now().isoformat()

    with open(output_path, 'w') as f:
        yaml.dump(
            output_dict,
            f,
            Dumper=ComparisonYAMLDumper,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
            width=120,
        )

    logger.info(f"Wrote comparison results to {output_path}")
    return output_path


def write_summary_report(
    result: SchemaComparisonResult,
    output_dir: Path,
    filename: str = "comparison_summary.txt",
) -> Path:
    """Write human-readable summary report.

    Args:
        result: The comparison result to summarize.
        output_dir: Directory to write output file.
        filename: Name of the output file.

    Returns:
        Path to the written file.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filename

    lines = []
    lines.append("=" * 80)
    lines.append("MIXS LEGACY SCHEMA COMPARISON SUMMARY")
    lines.append("=" * 80)
    lines.append("")

    # Schema info
    old_info = result.old_schema_info
    new_info = result.new_schema_info
    lines.append(f"OLD SCHEMA: {old_info.get('version', 'unknown')}")
    lines.append(f"  Source: {old_info.get('source', 'unknown')}")
    lines.append(f"  Format: {old_info.get('format', 'unknown')}")
    lines.append(f"  Terms: {old_info.get('term_count', 0)}")
    lines.append("")
    lines.append(f"NEW SCHEMA: {new_info.get('version', 'unknown')}")
    lines.append(f"  Source: {new_info.get('source', 'unknown')}")
    lines.append(f"  Format: {new_info.get('format', 'unknown')}")
    lines.append(f"  Terms: {new_info.get('term_count', 0)}")
    lines.append("")

    # Term comparison summary
    lines.append("-" * 40)
    lines.append("TERM COMPARISON")
    lines.append("-" * 40)
    key_comp = result.term_key_comparison
    lines.append(f"  Shared terms: {len(key_comp.shared)}")
    lines.append(f"  Only in old: {len(key_comp.only_in_old)}")
    lines.append(f"  Only in new: {len(key_comp.only_in_new)}")
    if key_comp.expected_mappings:
        lines.append(f"  Expected mappings: {len(key_comp.expected_mappings)}")
    lines.append(f"  Terms with definition changes: {len(result.term_comparisons)}")
    lines.append("")

    # List expected splits
    if key_comp.expected_splits:
        lines.append("  Term splits (1 old → N new):")
        for old_name, new_names in sorted(key_comp.expected_splits.items()):
            lines.append(f"    {old_name} → {', '.join(new_names)}")
        lines.append("")

    # List expected deletions
    if key_comp.expected_deletions:
        lines.append("  Terms intentionally removed:")
        for name, reason in sorted(key_comp.expected_deletions.items()):
            lines.append(f"    - {name}: {reason}")
        lines.append("")

    # List removed terms (unexplained)
    if key_comp.only_in_old:
        lines.append("  Terms only in OLD (unexplained removals):")
        for name in sorted(key_comp.only_in_old)[:20]:
            lines.append(f"    - {name}")
        if len(key_comp.only_in_old) > 20:
            lines.append(f"    ... and {len(key_comp.only_in_old) - 20} more")
        lines.append("")

    # List added terms
    if key_comp.only_in_new:
        lines.append("  Terms only in NEW (added):")
        for name in sorted(key_comp.only_in_new)[:20]:
            lines.append(f"    + {name}")
        if len(key_comp.only_in_new) > 20:
            lines.append(f"    ... and {len(key_comp.only_in_new) - 20} more")
        lines.append("")

    # Package comparison summary
    if result.package_key_comparison.shared or result.package_key_comparison.only_in_old or result.package_key_comparison.only_in_new:
        lines.append("-" * 40)
        lines.append("PACKAGE COMPARISON")
        lines.append("-" * 40)
        pkg_comp = result.package_key_comparison
        lines.append(f"  Shared packages: {len(pkg_comp.shared)}")
        lines.append(f"  Only in old: {len(pkg_comp.only_in_old)}")
        lines.append(f"  Only in new: {len(pkg_comp.only_in_new)}")
        lines.append("")

    # Checklist comparison summary
    if result.checklist_key_comparison.shared or result.checklist_key_comparison.only_in_old or result.checklist_key_comparison.only_in_new:
        lines.append("-" * 40)
        lines.append("CHECKLIST COMPARISON")
        lines.append("-" * 40)
        cl_comp = result.checklist_key_comparison
        lines.append(f"  Shared checklists: {len(cl_comp.shared)}")
        lines.append(f"  Only in old: {len(cl_comp.only_in_old)}")
        lines.append(f"  Only in new: {len(cl_comp.only_in_new)}")
        lines.append("")

    lines.append("=" * 80)
    lines.append(f"Generated: {datetime.now().isoformat()}")
    lines.append("=" * 80)

    with open(output_path, 'w') as f:
        f.write('\n'.join(lines))

    logger.info(f"Wrote summary report to {output_path}")
    return output_path
