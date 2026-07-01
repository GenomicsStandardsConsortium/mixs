#!/usr/bin/env python3
"""
One-time, hardcoded reproducer for the MIxS v5 (2018 Excel) -> v6.0.0 (2022 LinkML) diff.

This is NOT the reusable, forward-compatible diff tool. For comparing any two
LinkML versions of MIxS (v6 onward), use `diff-releases`
(src/scripts/diff_two_linkml_mixs_releases.py). See ./README.md for why this one
exists and how it was validated.

Both inputs are frozen historical releases pinned by commit/tag, so this script
takes no arguments. Running it reproduces the committed output in ./output/.

Requires the v5 Excel reader dependency (openpyxl). Install with:
    poetry install --with legacy-v5-diff
"""
import logging
import os
import sys
import tempfile
import urllib.request
from pathlib import Path

# Pin the hash seed so set iteration (and thus list ordering in the output) is
# deterministic; without this, re-runs produce the same content in a different
# order. Re-exec once with the seed fixed if it is not already.
if os.environ.get("PYTHONHASHSEED") != "0":
    os.environ["PYTHONHASHSEED"] = "0"
    os.execv(sys.executable, [sys.executable, *sys.argv])

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))  # make ./engine importable when run from anywhere

from engine.readers.base import get_reader  # noqa: E402
from engine.comparison import LegacySchemaComparator, load_mapping_config  # noqa: E402
from engine.output import write_comparison_yaml, write_summary_report  # noqa: E402

# --- hardcoded, frozen inputs -------------------------------------------------
# v5: last pre-LinkML formulation, an Excel file pinned to the "final version"
# commit in the public GenomicsStandardsConsortium/mixs-legacy repo. The Excel
# reader takes a local path, so we fetch this pinned binary at runtime.
OLD_XLSX_URL = (
    "https://raw.githubusercontent.com/GenomicsStandardsConsortium/mixs-legacy/"
    "9628b5e5aa89/mixs5/mixs_v5.xlsx"
)
OLD_VERSION = "v5"
# v6.0.0: first LinkML release, pinned to the tag (imports resolved by the reader).
NEW_SPEC = "GenomicsStandardsConsortium/mixs@mixs6.0.0:model/schema/mixs.yaml"
NEW_VERSION = "v6.0.0"

MAPPINGS_DIR = HERE                 # holds mapping_config.yaml (validated)
PROFILE_DIR = HERE / "profiles"     # holds excel_v5.yaml (Excel parse profile)
OUTPUT_DIR = HERE / "output"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%H:%M:%S")
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info("Reproducing the one-time MIxS v5 -> v6.0.0 diff")
    logger.info(f"OLD (fetched): {OLD_XLSX_URL}")
    logger.info(f"NEW: {NEW_SPEC}")

    with tempfile.TemporaryDirectory() as tmp:
        old_xlsx = Path(tmp) / "mixs_v5.xlsx"
        logger.info("Downloading pinned v5 Excel file...")
        urllib.request.urlretrieve(OLD_XLSX_URL, old_xlsx)

        old_reader = get_reader(str(old_xlsx), profiles_dir=PROFILE_DIR)
        new_reader = get_reader(NEW_SPEC, profiles_dir=PROFILE_DIR)

        old_schema = old_reader.read(str(old_xlsx), version=OLD_VERSION)
        new_schema = new_reader.read(NEW_SPEC, version=NEW_VERSION)

    mapping_config = load_mapping_config(MAPPINGS_DIR)
    logger.info(f"Loaded validated mapping from {MAPPINGS_DIR / 'mapping_config.yaml'}")

    result = LegacySchemaComparator(mapping_config=mapping_config).compare(old_schema, new_schema)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    yaml_path = write_comparison_yaml(result, OUTPUT_DIR, include_membership=True)
    summary_path = write_summary_report(result, OUTPUT_DIR, include_membership=True)

    print(f"\nWrote: {yaml_path}")
    print(f"Wrote: {summary_path}")
    print("\nSummary:")
    print(f"  Old: {old_schema.version} ({old_schema.source_format}) - {len(old_schema.terms)} terms")
    print(f"  New: {new_schema.version} ({new_schema.source_format}) - {len(new_schema.terms)} terms")
    print(f"  Shared: {len(result.term_key_comparison.shared)}")
    print(f"  Only in v5 (removed): {len(result.term_key_comparison.only_in_old)}")
    print(f"  Only in v6.0.0 (added): {len(result.term_key_comparison.only_in_new)}")


if __name__ == "__main__":
    main()
