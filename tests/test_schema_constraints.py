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

import yaml
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



def has_top_level_alternation(pattern):
    """True if ``pattern`` contains a ``|`` that splits the whole expression.

    Only an unescaped pipe outside any group and outside any character class is
    an alternation at the top level. ``\\|`` is a literal pipe, ``[a|b]`` is a
    character class containing one, and ``\\(`` is a literal parenthesis that must
    not be counted as opening a group.
    """
    depth = 0
    in_class = False
    escaped = False
    for char in pattern:
        if escaped:
            escaped = False
        elif char == "\\":
            escaped = True
        elif in_class:
            if char == "]":
                in_class = False
        elif char == "[":
            in_class = True
        elif char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
        elif char == "|" and depth == 0:
            return True
    return False


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


class TestCombinationUri(unittest.TestCase):
    """A combination identifier is built from the identifiers it combines.

    ``MigsBaAgriculture`` is ``MigsBa`` (``MIXS:0010003``) applied to
    ``Agriculture`` (``MIXS:0016018``), and its identifier is
    ``MIXS:0010003_0016018``. The parts are not free text: each one is the
    identifier of a class in this schema, so a wrong or invented part points at
    a checklist or extension that does not exist.
    """

    @classmethod
    def setUpClass(cls):
        view = SchemaView(SCHEMA_PATH)
        cls.classes = view.all_classes()
        cls.combinations = {
            name: c for name, c in cls.classes.items()
            if COMBINATION_SUBSET in (c.in_subset or [])}
        cls.known_numbers = {
            str(c.class_uri).split(":", 1)[1]
            for c in cls.classes.values()
            if c.class_uri and "_" not in str(c.class_uri)}

    def test_combination_uri_is_well_formed(self):
        """Each part is MIXS: plus seven digits, underscore separated.

        Unpadded parts break sorting and string matching against the checklist
        and extension identifiers they are supposed to be built from.
        """
        malformed = {name: str(c.class_uri)
                     for name, c in self.combinations.items()
                     if not COMBINATION_URI_PATTERN.match(str(c.class_uri or ""))}
        self.assertEqual(
            malformed, {},
            f"{len(malformed)} combination class_uri values are not "
            f"underscore-joined seven-digit MIXS numbers: {malformed}")

    def test_combination_uri_parts_identify_real_classes(self):
        """Every part of a combination identifier belongs to some class."""
        unknown = {}
        for name, c in self.combinations.items():
            uri = str(c.class_uri or "")
            if ":" not in uri:
                unknown[name] = uri
                continue
            parts = uri.split(":", 1)[1].split("_")
            stray = [p for p in parts if p not in self.known_numbers]
            if stray:
                unknown[name] = f"{uri} (no class has {', '.join(stray)})"
        self.assertEqual(
            unknown, {},
            f"{len(unknown)} combination class_uri values contain a number that "
            f"identifies no class: {unknown}")

    def test_combination_uri_matches_what_it_combines(self):
        """The identifier is the mixed-in class's, then the extended class's.

        What a combination mixes in is usually a checklist, but it can be
        another combination: MimsHostAssociatedAncient mixes in
        MimsHostAssociated and extends Ancient, which is why its identifier has
        three parts rather than two.
        """
        def number(class_name):
            c = self.classes.get(class_name)
            if c is None or not c.class_uri:
                return None
            return str(c.class_uri).split(":", 1)[1]

        wrong = {}
        for name, c in self.combinations.items():
            mixed_in = list(c.mixins)[0] if c.mixins else None
            extended_number, mixed_in_number = number(c.is_a), number(mixed_in)
            if extended_number is None or mixed_in_number is None:
                continue
            expected = f"MIXS:{mixed_in_number}_{extended_number}"
            actual = str(c.class_uri)
            if actual != expected:
                wrong[name] = f"{actual}, expected {expected}"
        self.assertEqual(
            wrong, {},
            f"{len(wrong)} combination identifiers do not compose "
            f"<mixed-in class>_<extended class>: {wrong}")


class TestContainerSlots(unittest.TestCase):
    """A class that no container slot points at cannot appear in a MIxS document.

    ``MixsCompliantData`` is the root of a MIxS file, and each checklist,
    extension and combination reaches a document through one ``*_data`` slot
    listed on that class. Declaring ``domain: MixsCompliantData`` on the slot is
    not enough; a slot missing from the class's own list is silently
    unreachable, which is how the nine ancient-DNA slots shipped in v7.0.0
    without anywhere to put ancient data. See issue 1365.
    """

    @classmethod
    def setUpClass(cls):
        view = SchemaView(SCHEMA_PATH)
        cls.view = view
        cls.attached = set(view.class_slots(CONTAINER_DOMAIN))

    def test_every_container_slot_is_attached_to_the_class(self):
        declared = {name for name, slot in self.view.all_slots().items()
                    if slot.domain == CONTAINER_DOMAIN}
        orphaned = sorted(declared - self.attached)
        self.assertEqual(
            orphaned, [],
            f"{len(orphaned)} slots declare domain {CONTAINER_DOMAIN} but are not "
            f"listed on it, so nothing can reach their classes: {orphaned}")

    def test_every_class_is_reachable_from_a_document(self):
        """Every checklist, extension and combination has a way into a file."""
        reachable = {str(self.view.get_slot(s).range)
                     for s in self.attached if self.view.get_slot(s)}
        unreachable = sorted(
            name for name in self.view.all_classes()
            if name not in UNIDENTIFIED_CLASSES and name not in reachable)
        self.assertEqual(
            unreachable, [],
            f"{len(unreachable)} classes cannot appear in a MIxS document because "
            f"no container slot has them as its range: {unreachable}")


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


class TestTitles(unittest.TestCase):
    """The title is the human-readable name a submitter sees.

    Two slots shared the title "host sex" until issue 1223 was settled, so a
    submitter comparing two checklists saw the same label on two different
    terms. Uniqueness is guarded here to keep that from recurring.
    """

    @classmethod
    def setUpClass(cls):
        view = SchemaView(SCHEMA_PATH)
        cls.classes = view.all_classes()
        cls.slots = view.all_slots()

    def test_every_slot_has_a_title(self):
        missing = sorted(name for name, slot in self.slots.items()
                         if not (slot.title or "").strip())
        self.assertEqual(
            missing, [],
            f"{len(missing)} slots have no title: {missing}")

    def test_slot_titles_are_unique(self):
        """No two slots present themselves under the same human-readable name."""
        counts = Counter((slot.title or "").strip()
                         for slot in self.slots.values() if (slot.title or "").strip())
        shared = defaultdict(list)
        for name, slot in self.slots.items():
            title = (slot.title or "").strip()
            if title and counts[title] > 1:
                shared[title].append(name)
        self.assertEqual(
            dict(shared), {},
            f"{len(shared)} titles are used by more than one slot: {dict(shared)}")

    def test_every_identified_class_has_a_title(self):
        """Every class except the structural roots carries a title."""
        missing = sorted(name for name, cls in self.classes.items()
                         if not (cls.title or "").strip()
                         and name not in UNIDENTIFIED_CLASSES)
        self.assertEqual(
            missing, [],
            f"{len(missing)} classes have no title: {missing}")




class TestPatterns(unittest.TestCase):
    """Every ``pattern`` must compile, and must not repeat an anchor.

    A doubled anchor is not a syntax error: ``^^`` is two zero-width assertions at
    the same position, so Python and ECMAScript accept it and behave as if there
    were one. Nothing in the build looks at pattern values, so it reached four
    slots and stayed there until CodeQL reported 80 findings against the generated
    Python.
    """

    @classmethod
    def setUpClass(cls):
        cls.patterns = {name: slot.pattern
                        for name, slot in reporting_terms().items()
                        if slot.pattern}

    def test_every_pattern_compiles(self):
        for name, pattern in self.patterns.items():
            with self.subTest(slot=name):
                try:
                    re.compile(pattern)
                except re.error as error:
                    self.fail(f"{name} has a pattern that does not compile: {error}")

    def test_no_repeated_anchors(self):
        for name, pattern in self.patterns.items():
            with self.subTest(slot=name):
                self.assertFalse(
                    pattern.startswith("^^"),
                    f"{name} starts with a doubled caret. The second asserts the same "
                    f"position as the first, so it does nothing, and CodeQL reports it "
                    f"as an unmatchable caret.",
                )
                self.assertFalse(
                    pattern.endswith("$$"),
                    f"{name} ends with a doubled dollar, which does nothing.",
                )



class TestStructuredPatterns(unittest.TestCase):
    """Every placeholder in a ``structured_pattern`` must resolve to a setting.

    A misspelled or misplaced placeholder is not an error anywhere in the build.
    It survives interpolation as a literal, so ``{[termID]}`` became a regex
    matching a brace, one character, and a closing brace. Nothing complained,
    because the slot carrying it also allowed free text, so every value validated
    through the other branch and the broken one was never exercised.

    Example data cannot catch this: where a slot permits free text, a file with a
    correct ontology term passes whether the term branch works or not.
    """

    @classmethod
    def setUpClass(cls):
        with open(SCHEMA_PATH) as handle:
            cls.schema = yaml.safe_load(handle)
        cls.settings = cls.schema.get("settings") or {}

    def expand(self, syntax):
        for _ in range(5):
            for key, value in self.settings.items():
                syntax = syntax.replace("{" + key + "}", str(value))
        return syntax

    def test_every_placeholder_resolves(self):
        # Any brace group left after interpolation, except a regex quantifier
        # such as {1,2} or {2,9}. Deliberately broad: the real defect was
        # {[termID]}, which a name-shaped pattern would not have caught.
        brace_group = re.compile(r"\{[^{}]*\}")
        quantifier = re.compile(r"^\{\d+(,\d*)?\}$")
        for name, slot in (self.schema.get("slots") or {}).items():
            if not isinstance(slot, dict):
                continue
            structured = slot.get("structured_pattern")
            if not isinstance(structured, dict) or not structured.get("syntax"):
                continue
            with self.subTest(slot=name):
                leftover = [g for g in brace_group.findall(self.expand(structured["syntax"]))
                            if not quantifier.match(g)]
                self.assertEqual(
                    leftover, [],
                    f"{name} has placeholders that no setting resolves: {leftover}. "
                    f"They survive into the generated patterns as literal text, so "
                    f"that branch of the regex matches braces rather than what it "
                    f"was meant to match. Check the spelling against the settings "
                    f"block, and the form: the convention is \\[{{termID}}\\], not "
                    f"{{[termID]}}.",
                )


    def test_anchored_alternations_are_grouped(self):
        """``^A|B$`` anchors only the first and last branch, not the whole thing.

        ``|`` has the lowest precedence, so ``^A|B$`` reads as "starts with A" or
        "ends with B". Values with text either side then validate. 17 slots were
        written that way, and nothing in the build noticed, because a pattern that
        is too permissive never fails anything.
        """
        for name, slot in (self.schema.get("slots") or {}).items():
            if not isinstance(slot, dict):
                continue
            structured = slot.get("structured_pattern")
            if not isinstance(structured, dict):
                continue
            syntax = structured.get("syntax") or ""
            if not (syntax.startswith("^") and syntax.endswith("$")):
                continue
            top_level_pipe = has_top_level_alternation(syntax[1:-1])
            with self.subTest(slot=name):
                self.assertFalse(
                    top_level_pipe,
                    f"{name} has an alternation that is not grouped: {syntax}. The "
                    f"anchors bind to the first and last branch only, so a value with "
                    f"text either side validates. Wrap it: ^(A|B)$ rather than ^A|B$.",
                )



class TestAlternationDetector(unittest.TestCase):
    """The detector used by TestStructuredPatterns, checked against regex semantics.

    Each expectation is cross-checked against Python's own parser: where the pipe
    is inside a character class, ``re`` matches a literal ``|``; where it is an
    alternation, it does not.
    """

    CASES = [
        ("A|B", True, "a plain top-level alternation"),
        ("(A|B)", False, "grouped"),
        ("(?:A|B)", False, "a non-capturing group"),
        (r"A\|B", False, "an escaped pipe is a literal"),
        ("[a|b]", False, "a pipe inside a character class"),
        (r"\(A|B\)", True, "escaped parentheses, so the pipe is top level"),
        (r"[\]|a]", False, "an escaped ] does not close the class"),
        (r"[\]]|B", True, "the escaped ], then the real ], then a top-level pipe"),
        (r"[a\]b|c]d", False, "the pipe stays inside the class"),
        (r"[\\]|B", True, "an escaped backslash ends the class"),
        ("(A)|B", True, "a group closes, then a top-level pipe"),
    ]

    def test_detector_matches_regex_semantics(self):
        for pattern, expected, description in self.CASES:
            with self.subTest(pattern=pattern):
                self.assertEqual(
                    has_top_level_alternation(pattern), expected,
                    f"{pattern!r}: {description}",
                )

    def test_every_case_is_a_valid_regex(self):
        """A case that does not compile would be testing nothing."""
        for pattern, _, _ in self.CASES:
            with self.subTest(pattern=pattern):
                re.compile(pattern)


class TestNumericRanges(unittest.TestCase):
    """A numeric shape must be declared as a range, not as unenforceable text.

    Covers both places a slot can carry one: the top-level ``slots`` block and a
    class's ``slot_usage``. The second was missed at first, which hid host_taxid,
    whose numeric intent lived only in five class usages and so bound nothing.

    ``range: integer`` is checked by every validator. A bare ``{integer}`` written
    into ``string_serialization`` is not checked by anything, so a term carrying
    only that falls back to the schema-level ``default_range: string`` and accepts
    any value. Four terms were in that state and nothing failed, because a term
    that accepts everything cannot.

    Where both were present the text one was redundant, so this asserts the
    absence rather than the agreement: when a working constraint exists, the
    unenforceable duplicate goes.
    """

    NUMERIC_SHAPES = {"{integer}": "integer", "{float}": "float"}

    @classmethod
    def setUpClass(cls):
        with open(SCHEMA_PATH) as handle:
            schema = yaml.safe_load(handle)
        cls.slots = schema.get("slots") or {}
        cls.classes = schema.get("classes") or {}

    def declarations(self):
        """Yield (where, slot name, declared shape) for every place one appears."""
        for name, slot in self.slots.items():
            if isinstance(slot, dict) and isinstance(slot.get("string_serialization"), str):
                yield "slots", name, slot["string_serialization"]
        for class_name, definition in self.classes.items():
            if not isinstance(definition, dict):
                continue
            for name, usage in (definition.get("slot_usage") or {}).items():
                if isinstance(usage, dict) and isinstance(usage.get("string_serialization"), str):
                    yield f"{class_name}.slot_usage", name, usage["string_serialization"]

    def test_no_slot_declares_a_bare_numeric_shape_as_text(self):
        for where, name, declared in self.declarations():
            expected = self.NUMERIC_SHAPES.get(declared.strip())
            if expected is None:
                continue
            with self.subTest(slot=name, where=where):
                self.fail(
                    f"{name} declares its values are {expected} in {where}, a field "
                    f"nothing checks. Use `range: {expected}` on the slot, which "
                    f"validators enforce, and remove the declaration rather than "
                    f"keeping both."
                )

    def test_numeric_terms_kept_their_range(self):
        """The four terms this was found through, plus the one that was already right."""
        for name, expected in [("trnas", "integer"), ("host_of_host_taxid", "integer"),
                               ("host_spec_range", "integer"), ("samp_time_out", "float"),
                               ("num_replicons", "integer")]:
            with self.subTest(slot=name):
                self.assertEqual(
                    self.slots[name].get("range"), expected,
                    f"{name} holds {expected} values and needs `range: {expected}`. "
                    f"Without it the schema default applies and any string is accepted.",
                )

if __name__ == "__main__":
    unittest.main()
