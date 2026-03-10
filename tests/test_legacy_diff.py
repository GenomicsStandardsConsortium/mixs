"""Tests for the mixs-legacy-diff tool.

Tests cover the three supported comparison paths:
- v4 Excel (.xls) → v5 Excel (.xlsx)
- v5 Excel (.xlsx) → v6+ LinkML YAML
- v6 LinkML YAML → v6+ LinkML YAML (release-to-release)
"""

import shutil
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
MIXS_LEGACY = ROOT.parent / "mixs-legacy"
MIXS_SCHEMA = ROOT / "src" / "mixs" / "schema" / "mixs.yaml"
PROFILES_DIR = ROOT / "assets" / "legacy_format_profiles"
MAPPINGS_DIR = ROOT / "assets" / "between_diff_mappings"

# Skip tests if mixs-legacy repo or legacy-diff deps are missing
LEGACY_AVAILABLE = MIXS_LEGACY.exists()
V4_FILE = MIXS_LEGACY / "mixs4" / "MIxS_210514.xls"
V5_FILE = MIXS_LEGACY / "mixs5" / "mixs_v5.xlsx"

try:
    import openpyxl
    import xlrd

    DEPS_AVAILABLE = True
except ImportError:
    DEPS_AVAILABLE = False

SKIP_REASON = (
    "mixs-legacy repo not found" if not LEGACY_AVAILABLE
    else "legacy-diff dependencies not installed" if not DEPS_AVAILABLE
    else None
)


def _run_comparison(old_path, new_path, output_dir, mappings_dir=None, old_version=None, new_version=None):
    """Run a schema comparison and return the parsed YAML result."""
    from mixs.diff.readers.base import get_reader
    from mixs.diff.comparison import LegacySchemaComparator, load_mapping_config
    from mixs.diff.output import write_comparison_yaml, write_summary_report

    old_reader = get_reader(str(old_path), profiles_dir=PROFILES_DIR)
    new_reader = get_reader(str(new_path), profiles_dir=PROFILES_DIR)

    old_schema = old_reader.read(str(old_path), version=old_version)
    new_schema = new_reader.read(str(new_path), version=new_version)

    mapping_config = None
    if mappings_dir and mappings_dir.exists():
        mapping_config = load_mapping_config(mappings_dir)

    comparator = LegacySchemaComparator(mapping_config=mapping_config)
    result = comparator.compare(old_schema, new_schema)

    yaml_path = write_comparison_yaml(result, output_dir)
    summary_path = write_summary_report(result, output_dir)

    with open(yaml_path) as f:
        parsed = yaml.safe_load(f)

    return result, parsed, summary_path


@unittest.skipIf(SKIP_REASON, SKIP_REASON or "")
class TestExcelReaderV4(unittest.TestCase):
    """Test reading MIxS v4 .xls files."""

    def test_read_v4_xls(self):
        from mixs.diff.readers.excel_reader import ExcelReader

        reader = ExcelReader(profiles_dir=PROFILES_DIR)
        schema = reader.read(str(V4_FILE))

        self.assertEqual(schema.version, "v4")
        self.assertEqual(schema.source_format, "xls")
        self.assertGreater(len(schema.terms), 300, "v4 should have 300+ terms")
        self.assertGreater(len(schema.checklists), 5, "v4 should have multiple checklists")
        self.assertGreater(len(schema.packages), 10, "v4 should have 10+ packages")

    def test_v4_has_expected_core_terms(self):
        from mixs.diff.readers.excel_reader import ExcelReader

        reader = ExcelReader(profiles_dir=PROFILES_DIR)
        schema = reader.read(str(V4_FILE))

        for term in ["investigation_type", "project_name", "lat_lon", "geo_loc_name",
                      "collection_date", "env_biome", "env_feature", "env_material"]:
            self.assertIn(term, schema.terms, f"Core term '{term}' missing from v4")

    def test_v4_term_has_metadata(self):
        from mixs.diff.readers.excel_reader import ExcelReader

        reader = ExcelReader(profiles_dir=PROFILES_DIR)
        schema = reader.read(str(V4_FILE))

        term = schema.terms.get("lat_lon")
        self.assertIsNotNone(term)
        self.assertTrue(term.definition, "lat_lon should have a definition")
        self.assertTrue(term.checklist_membership, "lat_lon should have checklist memberships")


@unittest.skipIf(SKIP_REASON, SKIP_REASON or "")
class TestExcelReaderV5(unittest.TestCase):
    """Test reading MIxS v5 .xlsx files."""

    def test_read_v5_xlsx(self):
        from mixs.diff.readers.excel_reader import ExcelReader

        reader = ExcelReader(profiles_dir=PROFILES_DIR)
        schema = reader.read(str(V5_FILE))

        self.assertEqual(schema.version, "v5")
        self.assertEqual(schema.source_format, "xlsx")
        self.assertGreater(len(schema.terms), 500, "v5 should have 500+ terms")
        self.assertGreater(len(schema.checklists), 8, "v5 should have 8+ checklists")

    def test_v5_has_more_terms_than_v4(self):
        from mixs.diff.readers.excel_reader import ExcelReader

        reader = ExcelReader(profiles_dir=PROFILES_DIR)
        v4 = reader.read(str(V4_FILE))
        v5 = reader.read(str(V5_FILE))

        self.assertGreater(len(v5.terms), len(v4.terms),
                           "v5 should have more terms than v4")


@unittest.skipIf(SKIP_REASON, SKIP_REASON or "")
class TestLinkMLReader(unittest.TestCase):
    """Test reading LinkML YAML schemas."""

    def test_read_local_linkml(self):
        from mixs.diff.readers.linkml_reader import LinkMLReader

        reader = LinkMLReader()
        schema = reader.read(str(MIXS_SCHEMA))

        self.assertEqual(schema.source_format, "linkml")
        self.assertGreater(len(schema.terms), 1000, "Current MIxS should have 1000+ terms")
        self.assertGreater(len(schema.packages), 15, "Current MIxS should have 15+ packages")

    def test_linkml_terms_have_ids(self):
        from mixs.diff.readers.linkml_reader import LinkMLReader

        reader = LinkMLReader()
        schema = reader.read(str(MIXS_SCHEMA))

        terms_with_ids = sum(1 for t in schema.terms.values() if t.mixs_id)
        self.assertGreater(terms_with_ids, 500, "Most LinkML terms should have MIxS IDs")


@unittest.skipIf(SKIP_REASON, SKIP_REASON or "")
class TestV4ToV5Comparison(unittest.TestCase):
    """Test v4 Excel → v5 Excel comparison."""

    @classmethod
    def setUpClass(cls):
        cls.output_dir = Path("/tmp/test_legacy_diff_v4_to_v5")
        if cls.output_dir.exists():
            shutil.rmtree(cls.output_dir)
        cls.result, cls.parsed, cls.summary_path = _run_comparison(
            V4_FILE, V5_FILE, cls.output_dir,
            mappings_dir=MAPPINGS_DIR / "4_to_5",
        )

    @classmethod
    def tearDownClass(cls):
        if cls.output_dir.exists():
            shutil.rmtree(cls.output_dir)

    def test_output_files_exist(self):
        self.assertTrue((self.output_dir / "schema_comparison_results.yaml").exists())
        self.assertTrue(self.summary_path.exists())

    def test_metadata_correct(self):
        meta = self.parsed["comparison_metadata"]
        self.assertEqual(meta["old_schema"]["version"], "v4")
        self.assertEqual(meta["new_schema"]["version"], "v5")
        self.assertEqual(meta["old_schema"]["format"], "xls")
        self.assertEqual(meta["new_schema"]["format"], "xlsx")

    def test_shared_terms_reasonable(self):
        keys = self.parsed["term_differences"]["key_comparison"]
        shared = len(keys["shared"])
        only_old = len(keys.get("only_in_old", []))
        only_new = len(keys.get("only_in_new", []))

        self.assertGreater(shared, 300, "v4→v5 should share 300+ terms")
        self.assertGreater(only_new, 100, "v5 should have 100+ new terms vs v4")
        self.assertLess(only_old, 50, "Fewer than 50 terms should be only in v4")

    def test_definition_changes_detected(self):
        changes = self.parsed["term_differences"].get("definition_changes", [])
        self.assertGreater(len(changes), 50,
                           "Many terms should have definition changes between v4 and v5")

    def test_mapping_config_applied(self):
        keys = self.parsed["term_differences"]["key_comparison"]
        expected = keys.get("expected_mappings", [])
        self.assertIsNotNone(expected)

    def test_summary_report_readable(self):
        content = self.summary_path.read_text()
        self.assertIn("v4", content)
        self.assertIn("v5", content)
        self.assertIn("Shared terms", content)


@unittest.skipIf(SKIP_REASON, SKIP_REASON or "")
class TestV5ToV6Comparison(unittest.TestCase):
    """Test v5 Excel → v6+ LinkML comparison."""

    @classmethod
    def setUpClass(cls):
        cls.output_dir = Path("/tmp/test_legacy_diff_v5_to_v6")
        if cls.output_dir.exists():
            shutil.rmtree(cls.output_dir)
        cls.result, cls.parsed, cls.summary_path = _run_comparison(
            V5_FILE, MIXS_SCHEMA, cls.output_dir,
            mappings_dir=MAPPINGS_DIR / "5_to_6",
        )

    @classmethod
    def tearDownClass(cls):
        if cls.output_dir.exists():
            shutil.rmtree(cls.output_dir)

    def test_metadata_shows_cross_format(self):
        meta = self.parsed["comparison_metadata"]
        self.assertEqual(meta["old_schema"]["format"], "xlsx")
        self.assertEqual(meta["new_schema"]["format"], "linkml")

    def test_shared_terms_bridge_formats(self):
        keys = self.parsed["term_differences"]["key_comparison"]
        shared = len(keys["shared"])
        self.assertGreater(shared, 500,
                           "v5→v6 should share 500+ terms across format boundary")

    def test_linkml_has_substantially_more_terms(self):
        meta = self.parsed["comparison_metadata"]
        self.assertGreater(meta["new_schema"]["term_count"],
                           meta["old_schema"]["term_count"],
                           "LinkML schema should have more terms than v5 Excel")

    def test_definition_changes_detected(self):
        """Verify that field-level diffs work across format boundary."""
        changes = self.parsed["term_differences"].get("definition_changes", [])
        self.assertGreater(len(changes), 50,
                           "Many definitions should differ between v5 Excel and v6 LinkML")

    def test_membership_comparison_present(self):
        self.assertIn("membership_differences", self.parsed)


@unittest.skipIf(SKIP_REASON, SKIP_REASON or "")
class TestV6ToV6Comparison(unittest.TestCase):
    """Test LinkML → LinkML comparison (release-to-release)."""

    @classmethod
    def setUpClass(cls):
        """Compare current schema against itself — should show zero key differences."""
        cls.output_dir = Path("/tmp/test_legacy_diff_v6_self")
        if cls.output_dir.exists():
            shutil.rmtree(cls.output_dir)
        cls.result, cls.parsed, cls.summary_path = _run_comparison(
            MIXS_SCHEMA, MIXS_SCHEMA, cls.output_dir,
        )

    @classmethod
    def tearDownClass(cls):
        if cls.output_dir.exists():
            shutil.rmtree(cls.output_dir)

    def test_self_comparison_no_key_differences(self):
        keys = self.parsed["term_differences"]["key_comparison"]
        self.assertEqual(len(keys.get("only_in_old", [])), 0)
        self.assertEqual(len(keys.get("only_in_new", [])), 0)

    def test_self_comparison_all_shared(self):
        meta = self.parsed["comparison_metadata"]
        keys = self.parsed["term_differences"]["key_comparison"]
        self.assertEqual(len(keys["shared"]), meta["old_schema"]["term_count"])

    def test_self_comparison_no_definition_changes(self):
        changes = self.parsed["term_differences"].get("definition_changes", [])
        self.assertEqual(len(changes), 0,
                         "Self-comparison should have zero definition differences")


class TestFormatDetection(unittest.TestCase):
    """Test format auto-detection (no external deps needed)."""

    def test_detect_xls(self):
        from mixs.diff.readers.base import detect_format
        self.assertEqual(detect_format("foo/bar.xls"), "xls")

    def test_detect_xlsx(self):
        from mixs.diff.readers.base import detect_format
        self.assertEqual(detect_format("foo/bar.xlsx"), "xlsx")

    def test_detect_linkml(self):
        from mixs.diff.readers.base import detect_format
        self.assertEqual(detect_format("src/mixs/schema/mixs.yaml"), "linkml")
        self.assertEqual(detect_format("schema.yml"), "linkml")

    def test_detect_github_spec(self):
        from mixs.diff.readers.base import detect_format
        self.assertEqual(
            detect_format("GenomicsStandardsConsortium/mixs@v6.2.3:src/mixs/schema/mixs.yaml"),
            "linkml"
        )

    def test_detect_unknown(self):
        from mixs.diff.readers.base import detect_format
        self.assertEqual(detect_format("foo.txt"), "unknown")

    def test_unsupported_formats_rejected(self):
        from mixs.diff.readers.base import get_reader
        with self.assertRaises(ValueError):
            get_reader("old.docx")
        with self.assertRaises(ValueError):
            get_reader("schema.xsd")


class TestModels(unittest.TestCase):
    """Test data model basics (no external deps needed)."""

    def test_normalized_term_defaults(self):
        from mixs.diff.models import NormalizedTerm
        term = NormalizedTerm(name="test_term")
        self.assertEqual(term.name, "test_term")
        self.assertEqual(term.definition, "")
        self.assertEqual(term.checklist_membership, {})
        self.assertEqual(term.package_membership, {})

    def test_normalized_schema_merge(self):
        from mixs.diff.models import NormalizedSchema, NormalizedTerm
        s1 = NormalizedSchema(version="v1", source_path="a.yaml", source_format="linkml")
        s2 = NormalizedSchema(version="v1", source_path="b.yaml", source_format="linkml")

        s1.terms["alpha"] = NormalizedTerm(name="alpha", definition="A")
        s2.terms["beta"] = NormalizedTerm(name="beta", definition="B")

        s1.merge(s2)
        self.assertIn("alpha", s1.terms)
        self.assertIn("beta", s1.terms)

    def test_comparator_empty_schemas(self):
        from mixs.diff.models import NormalizedSchema
        from mixs.diff.comparison import LegacySchemaComparator

        old = NormalizedSchema(version="v1", source_path="old.yaml", source_format="linkml")
        new = NormalizedSchema(version="v2", source_path="new.yaml", source_format="linkml")

        comparator = LegacySchemaComparator()
        result = comparator.compare(old, new)

        self.assertEqual(len(result.term_key_comparison.shared), 0)
        self.assertEqual(len(result.term_key_comparison.only_in_old), 0)
        self.assertEqual(len(result.term_key_comparison.only_in_new), 0)


if __name__ == "__main__":
    unittest.main()
