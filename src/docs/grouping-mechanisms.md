# Grouping mechanisms in MIxS

MIxS uses a small set of LinkML mechanisms to group schema elements. This page
records which mechanisms are in use, what each one is for, where it shows up for
data submitters and ontology users, and what metadata a grouping referent must
carry. A test (`tests/test_grouping_integrity.py`) enforces that every referent
named below has actually been defined.

This page covers three mechanisms: `is_a`, `in_subset`, and `slot_group`. Other
LinkML constructs (`mixins`, `abstract`, `union_of`) are out of scope here:
`mixins` is a composition and reuse mechanism rather than a grouping axis, and the
others are not used as grouping devices in MIxS.

## The three mechanisms

| mechanism | referent (what the value points at) | semantic goal |
|---|---|---|
| `is_a` | a definition of the same kind (a class's parent is a class; a slot's parent is a slot) | Specialization. "X is a more specific kind of Y" and inherits Y's constraints. For slots this is a sub-property relationship. |
| `in_subset` | a subset defined in the `subsets:` block | Flat tagging. Groups elements into named subsets without inheritance or constraint sharing. |
| `slot_group` | a defined slot | Presentation grouping of slots within a class (form groups in tools such as DataHarmonizer). |

The referent type for each comes from the LinkML metamodel: `is_a` has range
`definition`, `in_subset` has range `subset_definition`, and `slot_group` has
range `slot_definition`.

## How MIxS and nmdc-schema use these today

The two schemas have almost opposite centers of gravity, which is worth knowing
before adding a new grouping.

| usage | MIxS (`mixs.yaml`) | nmdc-schema (`src/schema`) |
|---|---|---|
| class `is_a` | 335 of 338 classes (the checklist / extension / combination backbone) | 68 classes |
| slot `is_a` | **0** | 94 slots |
| `in_subset` | 100 slots, 299 classes, across 5 subsets | 9 slots, across 10 subsets (portal / data views) |
| `slot_group` | **0** | 21 slots (form groups such as JGI-Metagenomics, Sample ID) |
| abstract slots / classes | 0 / 0 | 13 / 14 |

So MIxS groups at the class level and tags slots flatly with subsets; it has no
slot `is_a`, no abstract slot, and no `slot_group`. nmdc-schema groups at the
slot level, using slot `is_a`, abstract parent slots, and `slot_group` for form
layout. A consequence for MIxS: introducing a grouping parent slot for the
environmental triad would be the first slot `is_a` and first abstract slot in the
schema, whereas a new subset is the established MIxS idiom. Both can be true at
once, because they group on different axes (a subset is a flat tag; an `is_a`
parent is a hierarchy node that also reaches the OWL).

### The five MIxS subsets

MIxS defines five subsets: `investigation`, `environment`, `sequencing`,
`nucleic acid sequence source`, and `combination_classes`. These carry what GSC
documentation has historically called a term's "section"; going forward the
mechanism is referred to as a `subset`. Whether to keep, describe, or retire
these assertions is under discussion
([#956](https://github.com/GenomicsStandardsConsortium/mixs/issues/956)).

## Where each mechanism is revealed

What a reader sees depends on the artifact. This matters when deciding which
mechanism to use for a given grouping goal.

| mechanism | GitHub Pages (custom doc templates) | OWL (and therefore OLS / BioPortal) |
|---|---|---|
| `is_a` | Shown. Slot and class pages render an inheritance tree. | Shown. Classes emit `subClassOf`; a slot parent emits `subPropertyOf`. Reaches OLS (which renders property hierarchies) and, less richly, BioPortal. |
| `in_subset` | Shown. The dedicated subset page lists its members, and each slot page shows its subsets in its Properties. | Not emitted to OWL at all, so invisible in OLS and BioPortal. |
| `slot_group` | Shown on a slot page when set. MIxS uses it zero times today, so it does not appear yet. | Not emitted to OWL, so invisible in OLS and BioPortal. |

Practical consequence: if a grouping needs to be visible to ontology users in OLS
or BioPortal, only `is_a` (or a real class) carries it there. `in_subset` and
`slot_group` are confined to the documentation site and downstream tooling.

## What metadata a referent must have

The integrity test guarantees a referent exists. These are the additional
expectations for a referent to be useful.

### A subset (referent of `in_subset`)

- Must have a `description`. `linkml lint` flags a subset without one, and an
  undocumented subset is hard to apply consistently (see #956).
- The name should be a stable, human-meaningful category, since it is the public
  label of the subset.

### A parent (referent of `is_a`)

- Must be a defined class (for a class parent) or slot (for a slot parent).
- A parent that exists only to group should be `abstract: true` so it is never
  populated directly.
- It should have a `description` that states what the grouping means.
- For a slot parent, set `range` deliberately. Children inherit the parent's
  `range` unless they override it, so a grouping parent should either omit
  `range` or use a range that is correct for every child. Do not give the parent
  a range that would change the shape of the child slots.

### A slot group (referent of `slot_group`)

- Must be a defined slot (the metamodel range is `slot_definition`).
- Because it groups other slots rather than carrying data, it should be
  `abstract: true` and should have a `description`.
- It should not carry data constraints (`range`, `required`, `pattern`) that
  would suggest it is itself a data field.

## Why LinkML does not catch a missing referent on its own

This was checked empirically against the three mechanisms:

| dangling referent | `linkml lint` | `linkml generate json-schema` | net effect |
|---|---|---|---|
| class `is_a` | crashes with `ValueError: No such class` | exit 1, same crash | caught, but as an ungraceful crash |
| slot `is_a` | crashes with `ValueError: No such slot` | exit 1, same crash | caught, ungracefully |
| `in_subset` | not flagged; exits clean | exit 0, silent | not caught |
| `slot_group` | not flagged; exits clean | exit 0, silent | not caught |

`is_a` participates in inheritance resolution that every generator must perform,
so a dangling parent makes ancestor resolution raise. `in_subset` and
`slot_group` are leaf annotations that no generator needs to dereference
(`slot_group` only affects presentation order; `in_subset` only affects docs and
tooling), so a typo is never looked up and ships silently. `linkml-validate`
checks data against the schema and never inspects the schema's own internal
referential integrity, so antecedents are out of its scope entirely. The test
below is what closes this gap, and it reports cleanly instead of crashing.

## The test

`tests/test_grouping_integrity.py` (run by `make test-python`) reads the schema
through `SchemaView`, so referents defined in imported files are resolved, and
asserts:

- every class `is_a` points at a defined class, and every slot `is_a` at a
  defined slot;
- every `in_subset` value is a defined subset;
- every `slot_group` value, including one set inside a class's `slot_usage`, is a
  defined slot.

LinkML does not enforce any of these on its own, so the test is what keeps a typo
or an unfinished refactor from shipping a grouping that points at nothing.
