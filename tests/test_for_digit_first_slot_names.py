import unittest
import os

import src.mixs.datamodel.mixs as mixs

from linkml_runtime import SchemaView

ROOT = os.path.join(os.path.dirname(__file__), '..')
SCHEMA_DIR = os.path.join(ROOT, "src", "mixs", "schema")
SCHEMA_FILE = "mixs.yaml"
SCHEMA_PATH = os.path.join(SCHEMA_DIR, SCHEMA_FILE)


class TestDigitFirstTermName(unittest.TestCase):
    """Test term name length."""

    def test_digit_first_term_name(self):
        """Test term name length."""

        print("\n")
        slot_name_digit_first = []
        slot_name_x_digit = []

        schema_view = SchemaView(SCHEMA_PATH)
        slots = schema_view.all_slots()
        slot_names = [str(sk) for sk, sv in slots.items()]
        slot_names.sort()
        for slot_name in slot_names:

            if slots[slot_name].domain == "MixsCompliantData":
                continue
            elif slot_name[0].isdigit():
                slot_name_digit_first.append(slot_name)
            elif slot_name.startswith('x') and len(slot_name) > 1 and slot_name[1].isdigit():
                slot_name_x_digit.append(slot_name)
            else:
                continue

        self.assertListEqual(slot_name_digit_first, [],
                             f"Slots whose names start with a digit: {slot_name_digit_first}")

        self.assertListEqual(slot_name_x_digit, [],
                             f"Slots whose names start with 'x' and a digit: {slot_name_x_digit}")
