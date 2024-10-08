import unittest
import os

import src.mixs.datamodel.mixs as mixs

from linkml_runtime import SchemaView

ROOT = os.path.join(os.path.dirname(__file__), '..')
SCHEMA_DIR = os.path.join(ROOT, "src", "mixs", "schema")
SCHEMA_FILE = "mixs.yaml"
SCHEMA_PATH = os.path.join(SCHEMA_DIR, SCHEMA_FILE)


class TestTermNameLength(unittest.TestCase):
    """Test term name length."""

    def test_term_name_length(self):
        """Test term name length."""

        print("\n")
        slot_length_name_limit = 20
        slot_name_length_ok = []
        slot_name_length_too_long = {}

        schema_view = SchemaView(SCHEMA_PATH)
        slots = schema_view.all_slots()
        slot_names = [str(sk) for sk, sv in slots.items()]
        slot_names.sort()
        for slot_name in slot_names:

            if slots[slot_name].domain == "MixsCompliantData":
                continue
            elif len(slot_name) <= slot_length_name_limit:
                slot_name_length_ok.append(slot_name)
            else:
                slot_name_length_too_long[slot_name] = len(slot_name)

        self.assertDictEqual(slot_name_length_too_long, {},
                             f"Slots whose names are greater than {slot_length_name_limit} characters: {slot_name_length_too_long}")
