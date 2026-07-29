"""Constraints on MIxS term identifiers.

These tests guard the reporting terms, which are the slots a submitter fills in.
The 344 container slots carrying ``domain: MixsCompliantData`` are generated, one
per non-abstract class, and are excluded.

Both constraints pass on the schema as it stands, so these are regression
guards: they exist because nothing checked, and 44 terms reached main carrying
an identical placeholder identifier as a result.
"""
import os
import re
import unittest
from collections import Counter, defaultdict

from linkml_runtime import SchemaView

ROOT = os.path.join(os.path.dirname(__file__), '..')
SCHEMA_PATH = os.path.join(ROOT, "src", "mixs", "schema", "mixs.yaml")

#: Generated container slots, one per non-abstract class, not reporting terms.
CONTAINER_DOMAIN = "MixsCompliantData"

#: ``MIXS:`` followed by exactly seven digits.
SLOT_URI_PATTERN = re.compile(r"^MIXS:\d{7}$")

#: A combination identifier: two or more zero-padded seven-digit numbers,
#: joined by underscores, after the ``MIXS:`` prefix.
COMBINATION_URI_PATTERN = re.compile(r"^MIXS:\d{7}(_\d{7})+$")

#: Marks the classes that pair a checklist with one or more extensions.
COMBINATION_SUBSET = "combination_classes"

#: The three root classes carry no ``class_uri``; they are structural, not
#: identified elements of the standard.
UNIDENTIFIED_CLASSES = {"Checklist", "Extension", "MixsCompliantData"}


def reporting_terms():
    """Every slot a submitter fills in, excluding generated containers."""
    view = SchemaView(SCHEMA_PATH)
    return {name: slot for name, slot in view.all_slots().items()
            if slot.domain != CONTAINER_DOMAIN}


class TestSlotUri(unittest.TestCase):
    """A MIxS ID identifies a term, so it has to be present, well formed and unique."""

    @classmethod
    def setUpClass(cls):
        cls.terms = reporting_terms()

    def test_slot_uri_is_well_formed(self):
        """Every reporting term has a MIxS ID of MIXS: plus seven digits.

        Placeholders such as MIXS:XXXXXXXXX have reached main before, because
        nothing checked. See issue 1304.
        """
        malformed = {name: str(slot.slot_uri)
                     for name, slot in self.terms.items()
                     if not SLOT_URI_PATTERN.match(str(slot.slot_uri))}
        self.assertEqual(
            malformed, {},
            f"{len(malformed)} reporting terms have a slot_uri that is not "
            f"MIXS: followed by seven digits: {malformed}")

    def test_slot_uri_is_unique(self):
        """No two reporting terms share a MIxS ID.

        Placeholders are identical to each other, so this catches them even if
        the format check were relaxed.
        """
        counts = Counter(str(slot.slot_uri) for slot in self.terms.values())
        shared = defaultdict(list)
        for name, slot in self.terms.items():
            if counts[str(slot.slot_uri)] > 1:
                shared[str(slot.slot_uri)].append(name)
        self.assertEqual(
            dict(shared), {},
            f"{len(shared)} MIxS IDs are used by more than one term: {dict(shared)}")


class TestClassUri(unittest.TestCase):
    """Checklists, extensions and combinations are identified too."""

    @classmethod
    def setUpClass(cls):
        view = SchemaView(SCHEMA_PATH)
        cls.classes = view.all_classes()

    def test_identified_classes_have_a_class_uri(self):
        """Every class except the three structural roots carries a class_uri."""
        missing = sorted(name for name, cls in self.classes.items()
                         if not cls.class_uri and name not in UNIDENTIFIED_CLASSES)
        self.assertEqual(
            missing, [],
            f"{len(missing)} classes have no class_uri: {missing}")

    def test_class_uri_is_unique(self):
        """No two classes share an identifier.

        A combination composes its parents' numbers, so a duplicate here means
        two combinations claim the same checklist and extension pairing.
        """
        counts = Counter(str(cls.class_uri)
                         for cls in self.classes.values() if cls.class_uri)
        shared = defaultdict(list)
        for name, cls in self.classes.items():
            if cls.class_uri and counts[str(cls.class_uri)] > 1:
                shared[str(cls.class_uri)].append(name)
        self.assertEqual(
            dict(shared), {},
            f"{len(shared)} class_uri values are used more than once: {dict(shared)}")


class TestDescriptions(unittest.TestCase):
    """Descriptions are universal in the schema, so a missing one is a regression.

    This guards existing practice rather than imposing a new rule: every class
    and every slot carries a description today.
    """

    @classmethod
    def setUpClass(cls):
        view = SchemaView(SCHEMA_PATH)
        cls.classes = view.all_classes()
        cls.slots = view.all_slots()

    def test_every_class_has_a_description(self):
        missing = sorted(name for name, cls in self.classes.items()
                         if not (cls.description or "").strip())
        self.assertEqual(
            missing, [],
            f"{len(missing)} classes have no description: {missing}")

    def test_every_slot_has_a_description(self):
        missing = sorted(name for name, slot in self.slots.items()
                         if not (slot.description or "").strip())
        self.assertEqual(
            missing, [],
            f"{len(missing)} slots have no description: {missing}")


if __name__ == "__main__":
    unittest.main()
