"""CLI entry point for mixs-legacy-diff tool.

This tool compares MIxS schemas across any combination of formats and versions:
- Excel (.xls, .xlsx) from MIxS v2-v5
- Word (.docx) from pre-2009
- XSD (.xsd) from 2006
- LinkML YAML from v6+

Usage Examples:
    # Compare v4 .xls to v5 .xlsx
    mixs-legacy-diff \\
        --old ../mixs-legacy/mixs4/MIxS_210514.xls \\
        --new ../mixs-legacy/mixs5/mixs_v5.xlsx \\
        --output-dir assets/diff_results/v4_to_v5

    # Compare v5 .xlsx to v6 LinkML YAML (from GitHub)
    mixs-legacy-diff \\
        --old ../mixs-legacy/mixs5/mixs_v5.xlsx \\
        --new GenomicsStandardsConsortium/mixs@v6.2.3:src/mixs/schema/mixs.yaml \\
        --output-dir assets/diff_results/v5_to_v6

    # Compare with name mappings
    mixs-legacy-diff \\
        --old ../mixs-legacy/mixs5/mixs_v5.xlsx \\
        --new src/mixs/schema/mixs.yaml \\
        --mappings-dir assets/between_diff_mappings/5_to_6
"""

import logging
import sys
from pathlib import Path
from typing import Optional

import click

from mixs.diff.readers.base import get_reader, detect_format
from mixs.diff.comparison import LegacySchemaComparator, load_name_mappings
from mixs.diff.output import write_comparison_yaml, write_summary_report

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)


def validate_path_or_spec(ctx, param, value: str) -> str:
    """Validate that path exists or is a valid GitHub spec."""
    if not value:
        return value

    # Check if it's a GitHub spec
    if "@" in value and ":" in value:
        return value

    # Check if local file exists
    path = Path(value)
    if not path.exists():
        raise click.BadParameter(f"File not found: {value}")

    return value


@click.command()
@click.option(
    '--old',
    required=True,
    callback=validate_path_or_spec,
    help='Old schema path (local file) or GitHub spec (owner/repo@commit:path).'
)
@click.option(
    '--new',
    required=True,
    callback=validate_path_or_spec,
    help='New schema path (local file) or GitHub spec (owner/repo@commit:path).'
)
@click.option(
    '--old-format',
    type=click.Choice(['auto', 'xlsx', 'xls', 'docx', 'xsd', 'linkml']),
    default='auto',
    help='Force format for old schema (default: auto-detect).'
)
@click.option(
    '--new-format',
    type=click.Choice(['auto', 'xlsx', 'xls', 'docx', 'xsd', 'linkml']),
    default='auto',
    help='Force format for new schema (default: auto-detect).'
)
@click.option(
    '--old-version',
    default=None,
    help='Version string for old schema (default: auto-detect).'
)
@click.option(
    '--new-version',
    default=None,
    help='Version string for new schema (default: auto-detect).'
)
@click.option(
    '--output-dir',
    type=click.Path(path_type=Path),
    default=Path.cwd() / "diff_output",
    help='Directory to save output files (default: ./diff_output).'
)
@click.option(
    '--mappings-dir',
    type=click.Path(path_type=Path, exists=True),
    default=None,
    help='Directory containing name mapping TSV files.'
)
@click.option(
    '--profile-dir',
    type=click.Path(path_type=Path, exists=True),
    default=None,
    help='Directory containing Excel format profile YAML files (default: assets/legacy_format_profiles).'
)
@click.option(
    '--log-level',
    type=click.Choice(['DEBUG', 'INFO', 'WARNING', 'ERROR']),
    default='INFO',
    help='Set logging level (default: INFO).'
)
@click.option(
    '--summary/--no-summary',
    default=True,
    help='Generate human-readable summary report (default: yes).'
)
def main(
    old: str,
    new: str,
    old_format: str,
    new_format: str,
    old_version: Optional[str],
    new_version: Optional[str],
    output_dir: Path,
    mappings_dir: Optional[Path],
    profile_dir: Optional[Path],
    log_level: str,
    summary: bool,
):
    """Compare MIxS schemas across formats and versions.

    This tool compares MIxS schemas from different eras and formats,
    producing a normalized comparison output. Supports Excel (v2-v5),
    Word (pre-2009), XSD (2006), and LinkML YAML (v6+).

    Examples:

        # Compare v4 Excel to v5 Excel
        mixs-legacy-diff --old ../mixs-legacy/mixs4/MIxS_210514.xls --new ../mixs-legacy/mixs5/mixs_v5.xlsx

        # Compare v5 Excel to current LinkML
        mixs-legacy-diff --old ../mixs-legacy/mixs5/mixs_v5.xlsx --new src/mixs/schema/mixs.yaml

        # Compare with GitHub spec for new schema
        mixs-legacy-diff --old ../mixs-legacy/mixs5/mixs_v5.xlsx --new GenomicsStandardsConsortium/mixs@v6.2.3:src/mixs/schema/mixs.yaml
    """
    # Set logging level
    logging.getLogger().setLevel(getattr(logging, log_level))

    logger.info(f"Starting MIxS legacy schema comparison")
    logger.info(f"Old schema: {old}")
    logger.info(f"New schema: {new}")

    try:
        # Get readers
        old_fmt = detect_format(old) if old_format == 'auto' else old_format
        new_fmt = detect_format(new) if new_format == 'auto' else new_format

        logger.info(f"Detected formats - Old: {old_fmt}, New: {new_fmt}")

        old_reader = get_reader(old, profiles_dir=profile_dir)
        new_reader = get_reader(new, profiles_dir=profile_dir)

        # Read schemas
        logger.info("Reading old schema...")
        old_schema = old_reader.read(old, version=old_version)

        logger.info("Reading new schema...")
        new_schema = new_reader.read(new, version=new_version)

        # Load name mappings if provided
        name_mappings = {}
        if mappings_dir:
            logger.info(f"Loading name mappings from {mappings_dir}")
            name_mappings = load_name_mappings(mappings_dir)

        # Compare schemas
        logger.info("Comparing schemas...")
        comparator = LegacySchemaComparator(name_mappings=name_mappings)
        result = comparator.compare(old_schema, new_schema)

        # Write outputs
        logger.info(f"Writing outputs to {output_dir}")
        yaml_path = write_comparison_yaml(result, output_dir)
        click.echo(f"Wrote comparison results to: {yaml_path}")

        if summary:
            summary_path = write_summary_report(result, output_dir)
            click.echo(f"Wrote summary report to: {summary_path}")

        # Print brief summary to console
        click.echo("")
        click.echo("Comparison Summary:")
        click.echo(f"  Old: {old_schema.version} ({old_schema.source_format}) - {len(old_schema.terms)} terms")
        click.echo(f"  New: {new_schema.version} ({new_schema.source_format}) - {len(new_schema.terms)} terms")
        click.echo(f"  Shared terms: {len(result.term_key_comparison.shared)}")
        click.echo(f"  Only in old: {len(result.term_key_comparison.only_in_old)}")
        click.echo(f"  Only in new: {len(result.term_key_comparison.only_in_new)}")
        click.echo(f"  Terms with changes: {len(result.term_comparisons)}")

        logger.info("Comparison complete!")

    except ImportError as e:
        logger.error(f"Missing dependency: {e}")
        logger.error("Install legacy-diff dependencies with: poetry install --with legacy-diff")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error during comparison: {e}")
        if log_level == 'DEBUG':
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
