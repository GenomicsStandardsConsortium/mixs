"""Referential-integrity tests for MIxS grouping mechanisms.

LinkML does not enforce that a grouping referent has actually been defined, so a
typo (or a half-finished refactor) can leave a slot pointing at a subset, parent
slot, or slot group that does not exist. These tests close that gap for the three
grouping mechanisms MIxS cares about, using the referent type each metaslot
declares in the LinkML metamodel:

- ``is_a``      (range: definition) -> a class's parent must be a defined class;
                a slot's parent must be a defined slot.
- ``in_subset`` (range: subset_definition) -> every value must be a defined subset.
- ``slot_group``(range: slot_definition) -> every value must be a defined slot,
                including ``slot_group`` set inside a class's ``slot_usage``.

The schema is read through SchemaView so that referents defined in imported files
are resolved.
"""

import os
import unittest

from linkml_runtime.utils.schemaview import SchemaView

ROOT = os.path.join(os.path.dirname(__file__), "..")
SCHEMA_PATH = os.path.join(ROOT, "src", "mixs", "schema", "mixs.yaml")


class TestGroupingIntegrity(unittest.TestCase):
    """Every is_a / in_subset / slot_group referent must be defined."""

    @classmethod
    def setUpClass(cls):
        cls.sv = SchemaView(SCHEMA_PATH)
        cls.class_names = set(cls.sv.all_classes())
        cls.slot_names = set(cls.sv.all_slots())
        cls.subset_names = set(cls.sv.all_subsets())

    def test_class_is_a_refers_to_defined_class(self):
        for name, cls_def in self.sv.all_classes().items():
            if cls_def.is_a:
                with self.subTest(klass=name):
                    self.assertIn(
                        cls_def.is_a,
                        self.class_names,
                        f"class {name!r} is_a -> undefined class {cls_def.is_a!r}",
                    )

    def test_slot_is_a_refers_to_defined_slot(self):
        for name, slot_def in self.sv.all_slots().items():
            if slot_def.is_a:
                with self.subTest(slot=name):
                    self.assertIn(
                        slot_def.is_a,
                        self.slot_names,
                        f"slot {name!r} is_a -> undefined slot {slot_def.is_a!r}",
                    )

    def test_in_subset_refers_to_defined_subset(self):
        element_groups = (
            ("class", self.sv.all_classes()),
            ("slot", self.sv.all_slots()),
            ("enum", self.sv.all_enums()),
            ("type", self.sv.all_types()),
        )
        for kind, elements in element_groups:
            for name, element in elements.items():
                for subset in element.in_subset or []:
                    with self.subTest(kind=kind, name=name, subset=subset):
                        self.assertIn(
                            subset,
                            self.subset_names,
                            f"{kind} {name!r} in_subset -> undefined subset {subset!r}",
                        )

    def test_slot_group_refers_to_defined_slot(self):
        # slot_group set on top-level slot definitions
        for name, slot_def in self.sv.all_slots().items():
            if slot_def.slot_group:
                with self.subTest(slot=name):
                    self.assertIn(
                        slot_def.slot_group,
                        self.slot_names,
                        f"slot {name!r} slot_group -> undefined slot {slot_def.slot_group!r}",
                    )
        # slot_group set inside a class's slot_usage
        for class_name, cls_def in self.sv.all_classes().items():
            for usage_name, usage in (cls_def.slot_usage or {}).items():
                if usage.slot_group:
                    with self.subTest(klass=class_name, slot=usage_name):
                        self.assertIn(
                            usage.slot_group,
                            self.slot_names,
                            f"{class_name!r}.{usage_name!r} slot_group -> "
                            f"undefined slot {usage.slot_group!r}",
                        )


if __name__ == "__main__":
    unittest.main()
