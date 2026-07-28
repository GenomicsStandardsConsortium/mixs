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


if __name__ == "__main__":
    unittest.main()
