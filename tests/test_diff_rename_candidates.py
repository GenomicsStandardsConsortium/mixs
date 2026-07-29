"""Rename detection in the release comparison tool.

A rename keeps an element's MIxS identifier and changes its name. Without
detection, the comparison reports the old name as removed and the new one as
added, so a term that survived reads as a term that was dropped. That happened
to ``estimated_size`` across 144 classes in the v6.0.0 to v7.0.0 comparison.

Two cases must not be reported, because they are not renames:

* a duplicate being resolved, where both names existed before and one was
  dropped, as with ``texture_meth`` and ``soil_texture_meth`` sharing
  ``MIXS:0000336`` in v6.0.0
* an ambiguous match, where one identifier arrives on more than one new name
"""
import importlib.util
import os
import unittest
from unittest.mock import Mock

ROOT = os.path.join(os.path.dirname(__file__), '..')
SCRIPT = os.path.join(ROOT, "src", "scripts", "diff_two_linkml_mixs_releases.py")

_spec = importlib.util.spec_from_file_location("diff_releases", SCRIPT)
diff_releases = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(diff_releases)


def comparator(old_uris, new_uris, field="slot_uri"):
    """A comparator whose two schemas return the given identifiers."""
    def view(uris):
        v = Mock()
        def get(name):
            if name not in uris:
                return None
            element = Mock()
            setattr(element, field, uris[name])
            return element
        v.get_slot = get
        v.get_class = get
        return v

    c = diff_releases.LinkMLComparator.__new__(diff_releases.LinkMLComparator)
    c.old_schema = view(old_uris)
    c.new_schema = view(new_uris)
    return c


class TestRenameCandidates(unittest.TestCase):

    def test_shared_identifier_is_reported_as_a_rename(self):
        c = comparator({"estimated_size": "MIXS:0000024"},
                       {"estimated_genome_size": "MIXS:0000024"})
        self.assertEqual(
            c._find_rename_candidates({"estimated_size"}, {"estimated_genome_size"}, "slots"),
            {"estimated_size": "estimated_genome_size"})

    def test_a_resolved_duplicate_is_not_a_rename(self):
        """The surviving name is not new, so it never reaches only_in_new."""
        c = comparator({"texture_meth": "MIXS:0000336"}, {})
        self.assertEqual(c._find_rename_candidates({"texture_meth"}, set(), "slots"), {})

    def test_an_ambiguous_identifier_is_left_alone(self):
        c = comparator({"old_name": "MIXS:0000001"},
                       {"new_a": "MIXS:0000001", "new_b": "MIXS:0000001"})
        self.assertEqual(
            c._find_rename_candidates({"old_name"}, {"new_a", "new_b"}, "slots"), {})

    def test_name_based_identifiers_are_ignored(self):
        """Container slots carry a name-based identifier, useless for matching."""
        c = comparator({"soil_data": "MIXS:soil_data"},
                       {"soil_data_2": "MIXS:soil_data"})
        self.assertEqual(
            c._find_rename_candidates({"soil_data"}, {"soil_data_2"}, "slots"), {})

    def test_collections_without_identifiers_are_skipped(self):
        c = comparator({"a": "MIXS:0000001"}, {"b": "MIXS:0000001"})
        self.assertEqual(c._find_rename_candidates({"a"}, {"b"}, "enums"), {})

    def test_classes_match_on_class_uri(self):
        c = comparator({"OldClass": "MIXS:0010002"},
                       {"NewClass": "MIXS:0010002"}, field="class_uri")
        self.assertEqual(
            c._find_rename_candidates({"OldClass"}, {"NewClass"}, "classes"),
            {"OldClass": "NewClass"})


if __name__ == "__main__":
    unittest.main()
