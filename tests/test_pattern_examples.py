"""Values that each patterned slot must accept, and must reject.

The example files under ``src/data/examples`` do not cover the rejecting half.
``linkml examples`` fails the build when a file in ``valid/`` does not validate,
but a file in ``counter-example-input-directory`` that *does* validate is not
reported and does not fail. Checked by planting a valid file in ``invalid/``: the
run still exited 0. So the negative cases live here, where ``unittest discover``
runs them.

Patterns are read from ``contrib/mixs-patterns-materialized.yaml``, because that
is the schema data is validated against. A slot's ``structured_pattern`` is
expanded there, and for several slots it differs from the literal ``pattern`` in
``src/mixs/schema/mixs.yaml``.
"""

import os
import re
import unittest

import yaml

ROOT = os.path.join(os.path.dirname(__file__), '..')
MATERIALIZED = os.path.join(ROOT, "contrib", "mixs-patterns-materialized.yaml")

#: slot -> (values it must accept, values it must reject)
CASES = {
    "sip_method": (
        ["PMID:12345678", "doi:10.1038/nbt.1823",
         "https://doi.org/10.1038/s41396-018-0279-6"],
        ["Smith et al 2019, Journal of Stable Isotope Probing",
         "see the supplementary methods section"],
    ),
    "internal_standard": (
        ["PMID:87654321", "doi:10.17504/protocols.io.abc123",
         "https://www.protocols.io/view/internal-standard"],
        ["described in the methods", "no reference given"],
    ),
    "prev_pubs": (
        ["PMID:12345678", "doi:10.1038/nbt.1823", "https://example.org/prior-study"],
        ["Smith et al 2019, Journal of Ancient DNA"],
    ),
}


def materialized_patterns():
    with open(MATERIALIZED) as handle:
        schema = yaml.safe_load(handle)
    return {name: slot.get("pattern")
            for name, slot in schema["slots"].items()
            if isinstance(slot, dict) and slot.get("pattern")}


class TestPatternExamples(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.patterns = materialized_patterns()

    def test_accepted_values(self):
        for slot, (accepted, _) in CASES.items():
            pattern = self.patterns.get(slot)
            self.assertIsNotNone(pattern, f"{slot} has no materialized pattern")
            for value in accepted:
                with self.subTest(slot=slot, value=value):
                    self.assertTrue(
                        re.search(pattern, value),
                        f"{slot} must accept {value!r}. It is one of the documented "
                        f"forms, so rejecting it would break real submissions.",
                    )

    def test_rejected_values(self):
        for slot, (_, rejected) in CASES.items():
            pattern = self.patterns.get(slot)
            self.assertIsNotNone(pattern, f"{slot} has no materialized pattern")
            for value in rejected:
                with self.subTest(slot=slot, value=value):
                    self.assertFalse(
                        re.search(pattern, value),
                        f"{slot} must reject {value!r}. Accepting free text here "
                        f"defeats the point of the pattern.",
                    )


if __name__ == "__main__":
    unittest.main()
