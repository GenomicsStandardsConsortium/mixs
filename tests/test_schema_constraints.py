"""Constraints on MIxS term names and identifiers.

These tests guard the reporting terms, which are the slots a submitter fills in.
The 344 container slots carrying ``domain: MixsCompliantData`` are generated, one
per non-abstract class, and are excluded throughout.

Two of the four constraints have pre-existing violations. Those are listed in
explicit allowlists below rather than being skipped, so the tests still fail on
anything new. Each allowlist entry is a term that predates the test, not a
decision that the constraint does not apply to it.
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

#: The INSDC feature table caps component names at 20 characters. MIxS holds
#: itself to that figure by convention; see issue 736.
NAME_LENGTH_LIMIT = 20

#: Names starting with a digit, or with ``x`` followed by a digit, which is the
#: workaround that produced them. See issue 754.
DIGIT_FIRST_PATTERN = re.compile(r"^\d|^x\d")

#: Terms longer than NAME_LENGTH_LIMIT that predate this test. Do not add to
#: this list to make a new term pass; shorten the name instead.
KNOWN_LONG_NAMES = {
    "context_retrieval_date",
    "estimated_genome_size",
    "nose_mouth_teeth_throat_disord",
    "nucleic_acid_elution_vol",
    "x16s_recover_software",
}

#: Digit-first names that predate this test. Both are proposed for deprecation.
KNOWN_DIGIT_FIRST_NAMES = {
    "x16s_recover",
    "x16s_recover_software",
}


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


class TestTermNames(unittest.TestCase):
    """Naming constraints on the structured comment name."""

    @classmethod
    def setUpClass(cls):
        cls.terms = reporting_terms()

    def test_names_are_not_too_long(self):
        """Term names are at most 20 characters, apart from known exceptions."""
        too_long = {name: len(name) for name in self.terms
                    if len(name) > NAME_LENGTH_LIMIT
                    and name not in KNOWN_LONG_NAMES}
        self.assertEqual(
            too_long, {},
            f"{len(too_long)} term names exceed {NAME_LENGTH_LIMIT} characters: "
            f"{too_long}. Shorten the name rather than adding it to "
            f"KNOWN_LONG_NAMES.")

    def test_no_new_digit_first_names(self):
        """Term names do not start with a digit, or with x followed by a digit."""
        offenders = sorted(name for name in self.terms
                           if DIGIT_FIRST_PATTERN.match(name)
                           and name not in KNOWN_DIGIT_FIRST_NAMES)
        self.assertEqual(
            offenders, [],
            f"{len(offenders)} term names start with a digit or with x plus a "
            f"digit: {offenders}")

    def test_allowlists_are_still_needed(self):
        """Fail once an allowlisted term is fixed or removed, so the list shrinks.

        Without this, the allowlists would silently outlive the problems they
        record.
        """
        stale_long = sorted(KNOWN_LONG_NAMES - set(self.terms))
        stale_digit = sorted(KNOWN_DIGIT_FIRST_NAMES - set(self.terms))
        fixed_long = sorted(n for n in KNOWN_LONG_NAMES & set(self.terms)
                            if len(n) <= NAME_LENGTH_LIMIT)
        self.assertEqual(
            (stale_long, stale_digit, fixed_long), ([], [], []),
            "Allowlisted terms no longer need to be: remove them from the "
            f"allowlist. Gone from the schema: {stale_long + stale_digit}. "
            f"Now short enough: {fixed_long}.")


if __name__ == "__main__":
    unittest.main()
