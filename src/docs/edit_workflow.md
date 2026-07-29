# MIxS Editing Workflows and Good Practices

This document is for members of the GSC Technical Working Group and anyone
cutting a MIxS release. Read [the policies](policy.md) first: that document says
what the rules are, this one says how to carry them out. Where the two disagree,
`policy.md` wins.

# Terms

A term is a LinkML slot.

## Requesting and creating a new term

TBD.

## Requesting and implementing a term update

TBD.

## Requesting and implementing a term deprecation

Terms are deprecated rather than deleted, over two release cycles, so that
existing data and tooling keep working. The procedure is in
[Deprecating schema elements](schema_element_deprecation_guide.md).

# MIxS identifiers

Every term and every checklist, extension and combination carries a permanent
`MIXS:` identifier, in one of these forms:

| element | field | form, as of MIxS 7.0.0 |
|---|---|---|
| terms | `slot_uri` | one number, `MIXS:0000001` to `MIXS:0001399` |
| checklists and extensions | `class_uri` | one number, in blocks between `MIXS:0010002` and `MIXS:0016024` |
| combinations | `class_uri` | the numbers they combine, joined by underscores |
| container slots | `slot_uri` | a name, such as `MIXS:migs_ba_data` |

A combination does not get an identifier of its own. It composes the ones it is
built from: `MigsBaAgriculture` combines `MigsBa` (`MIXS:0010003`) with
`Agriculture` (`MIXS:0016018`), so it is `MIXS:0010003_0016018`. A combination
built on another combination extends the chain, as
`MimsSoilAncient` does with `MIXS:0010007_0016012_0016024`. Each part keeps its
seven digits, because unpadded parts no longer match the identifiers they are
supposed to refer to. So adding a combination needs no request; adding the
checklist or extension it is built from does.

Identifiers are allocated by the CIG from a registry kept outside this
repository, in a spreadsheet only CIG members can edit. That is why you cannot
allocate one yourself: the registry holds numbers already reserved for terms
that have not been merged yet, so a number that looks unused in the schema may
already belong to someone else. Ask on the GitHub issue for the term, and a CIG
member will allocate the identifier and record it in the registry.

Add the identifier after the term is approved and before its pull request is
merged. Placeholder and malformed values must not reach `main`, and both have:
44 terms carrying `MIXS:XXXXXXXXX` were merged in July 2026, and 8 combinations
carried a number identifying no class until this was written. `tests/test_schema_constraints.py`
now checks both, so a pull request introducing one fails rather than being
caught later by a reader.

# Checklists, extensions, and combinations

In MIxS terms, a **checklist** is the set of terms expected for a kind of
sequence data, such as MIGS bacteria or MIMS. An **extension** adds the terms
that matter for a particular sampling environment, such as soil or water.
Extensions were called packages, or environmental packages, before MIxS 6. A
**combination** is a checklist paired with an extension, which is what a
submitter actually fills in. A few combinations carry two extensions.

In LinkML terms, all three are classes. A checklist is a class whose `is_a` is
`Checklist`, and an extension is a class whose `is_a` is `Extension`. A
combination inherits from the extension it applies and mixes in what it applies
it to, and is marked with `in_subset: combination_classes`. `MigsBaSoil` has
`is_a: Soil` and `mixins: [MigsBa]`, so it applies the `Soil` extension to the
`MigsBa` checklist.

What it mixes in is not always a checklist. A combination can be built on
another combination, which is how a sample gets two extensions:
`MimsHostAssociatedAncient` has `is_a: Ancient` and
`mixins: [MimsHostAssociated]`, applying `Ancient` to a class that is itself
`Mims` plus `HostAssociated`.

MIxS 7.0.0 has 13 checklists, 24 extensions and 307 combinations. The
combination classes are written out in `src/mixs/schema/mixs.yaml` like
everything else, so adding one checklist or one extension means adding a
combination for each partner it applies to. 23 of the 24 extensions pair with
all 13 checklists. `Ancient` is the exception and pairs with no checklist at
all: it applies to 8 combinations that are already `Mims` plus an environment,
which is why its own combinations carry three-part identifiers. The
`generate-combinations` script builds the `combinations.md` documentation page
from them; it does not create the classes.

## Requesting and creating a new checklist or extension

TBD, except for one step that is easy to miss.

### Give it a way into a MIxS document

A checklist, extension or combination is not usable until something can hold its
records. `MixsCompliantData` is the root of a MIxS file, and each class reaches a
document through one container slot listed on it. Adding a class means adding
that slot too, in two places:

1. Define the slot in the `slots` section, named after the class with a `_data`
   suffix. Copy an existing one, such as `soil_data`, which sets `domain:
   MixsCompliantData`, `range` to the class, `multivalued: true`, a
   `slot_uri` of `MIXS:<slot name>`, a description and a title.
2. **Add the slot name to the `slots:` list on the `MixsCompliantData` class.**
   This is the step that attaches it. Setting `domain: MixsCompliantData` on the
   slot does not.

Miss the second step and nothing complains: the schema builds, the class is
generated, and it simply cannot appear in a file. That is what happened to the
nine ancient-DNA classes in v7.0.0, found only after release
([issue 1365](https://github.com/GenomicsStandardsConsortium/mixs/issues/1365)).

`tests/test_schema_constraints.py` now checks both directions, that every slot
declaring the container domain is attached, and that every class is reachable
from a document, so the same omission fails the build rather than shipping.

## Updating an existing checklist or extension

TBD.

# Releases

Cutting a release is described in [Releasing MIxS](releasing.md).

# LinkML Updates

MIxS is built with [LinkML](https://linkml.io/), and the technical managers are
expected to keep it current with LinkML releases rather than pinning to an old
version indefinitely. Upgrading regularly keeps each change small enough to
understand.

When a LinkML release cannot be adopted because it breaks something in MIxS,
report it as an issue on [the LinkML repository](https://github.com/linkml/linkml/issues)
rather than working around it here. A workaround in MIxS hides the problem from
the people who can fix it, and from every other LinkML project that will hit it
next.

# Documentation

"Documentation" means several different things in this repository. They are
built and published separately:

- **The published site**, at
  [genomicsstandardsconsortium.github.io/mixs](https://genomicsstandardsconsortium.github.io/mixs/).
  Built from `main` by the "Deploy documentation to GitHub Pages" workflow. This is what to link when
  pointing anyone outside the project at MIxS documentation.
- **Term and class reference pages**, generated from the schema by the `gendoc`
  build step into `docs/`. These are not written by hand and not committed;
  editing a term's `description` in `src/mixs/schema/mixs.yaml` is what changes
  them.
- **Authored pages**, in `src/docs/`. This document, [policy.md](policy.md),
  [SCHEMA_DIFFING.md](SCHEMA_DIFFING.md) and the
  [deprecation guide](schema_element_deprecation_guide.md) are all written by
  hand and appear on the published site through `mkdocs.yml`.
- **Repository-level files**, `README.md` and `CONTRIBUTING.md` at the root.
  These are read on GitHub rather than on the site.
- **The per-pull-request preview**, built by the "Preview documentation build"
  workflow (`.github/workflows/test_pages_build.yaml`) on every pull request
  raised from this repository. Use it to see what the published site will look
  like before merging. It matters most when the documentation tooling changes,
  since that is when a change can build locally and still break the site.

Adding a new authored page means adding it to the `nav:` section of
`mkdocs.yml`; a page in `src/docs/` that is not in the nav is copied to the site
but linked from nowhere.
