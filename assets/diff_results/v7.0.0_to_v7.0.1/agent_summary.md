# MIxS v7.0.0 (2026-07-29) to v7.0.1 (2026-07-31)

*Written by the `mixs-diff-summary` skill from `schema_comparison_results.yaml`,
then corrected by hand before publication.*

A patch release with no vocabulary change at all. No slot, class, enum or
permissible value was added, removed or renamed; 347 classes and 1178 slots are
present in both, with the same names. No title, description, `range`, `required`
or `multivalued` changed, so there are no cosmetic mass-edits to group and
nothing for a consumer keyed on `MIXS:` identifiers or on titles to react to.

Everything in the release sits in two entries the counts flatten to almost
nothing: one class definition change and 17 slot definition changes.

## The ancient DNA extension becomes reachable

`MixsCompliantData` gained nine slots, going from 335 to 344:

`ancient_data`, `mims_hostassociated_ancient_data`,
`mims_humanassociated_ancient_data`, `mims_humangut_ancient_data`,
`mims_humanoral_ancient_data`, `mims_humanskin_ancient_data`,
`mims_plantassociated_ancient_data`, `mims_sediment_ancient_data`,
`mims_soil_ancient_data`.

The reason this shows as zero added slots is worth stating precisely, because it
is the whole shape of the fix. All nine slots were already **defined** in v7.0.0,
each with `domain: MixsCompliantData`, the matching ancient class as its `range`,
`multivalued: true` and `inlined_as_list: true`. The nine ancient classes were
also already there. The single thing missing was the slots' membership in
`MixsCompliantData.slots`, and in LinkML `domain` on a slot does not by itself
put that slot on the class. So v7.0.0 shipped every component of MInAS and no
place in a document to put an ancient DNA record.

Added by
https://github.com/GenomicsStandardsConsortium/mixs/pull/1367 — Give the ancient
DNA classes a way into a MIxS document.

## Pattern changes: 17 slots, one bug, five families

Every one of the 17 slot changes is a `pattern` change and nothing else. All 17
have the same cause: alternation binds looser than the anchors, so in `^A|B$`
only the first branch is anchored at the start and only the last at the end. Each
fix wraps the alternation in a group.

Grouped by the `structured_pattern` syntax they share, rather than one line per
slot:

| n | old syntax | new syntax | slots |
|---|---|---|---|
| 6 | `^{PMID}\|{DOI}\|{URL}$` | `^({PMID}\|{DOI}\|{URL})$` | `internal_standard`, `prev_pubs`, `samp_decont_pretreat`, `sip_method`, `sop_experimental`, `sop_lib_preparation` |
| 5 | `^({termLabel} \[{termID}\])\|{integer}$` | `^(({termLabel} \[{termID}\])\|{integer})$` | `animal_intrusion`, `cult_result_org`, `microb_start_taxID`, `serovar_or_serotype`, `spikein_org` |
| 4 | `^{text}\|({termLabel} \[{termID}\])$` | `^({text}\|({termLabel} \[{termID}\]))$` | `microb_cult_med`, `samp_stor_media`, `seq_meth`, `spikein_growth_med` |
| 1 | `^{termLabel} {[termID]}\|{text}$` | `^({termLabel} \[{termID}\]\|{text})$` | `isotopolog_atom_pos` |
| 1 | `^{float}-{float} {unit}\|{float} {unit}$` | `^({float}-{float} {unit}\|{float} {unit})$` | `gradient_pos_density` |

Fixed by
https://github.com/GenomicsStandardsConsortium/mixs/pull/1386 — Group the
alternations so the anchors apply to the whole pattern, with example data and
tests added in
https://github.com/GenomicsStandardsConsortium/mixs/pull/1385 — Example data and
tests for the reference patterns.

### What the count of 17 overstates

Only 12 of the 17 change what validates. For the 4 free-text-or-ontology-term
slots and for `isotopolog_atom_pos`, one branch is `{text}`, which accepts
anything, so the grouping does not narrow them. The one difference is that a
value containing a newline matched the old pattern and does not match the new
one, since `.` does not cross a line break.

For the other 12, values that were accepted are now rejected. This applies to
the materialized schema, where `structured_pattern` is expanded into `pattern`.
It is not what the published JSON Schema enforces today; see the section below.
Witnesses were checked by running both regexes, using search semantics, the way
JSON Schema applies `pattern`:

| slots | accepted under v7.0.0, rejected under v7.0.1, materialized schema |
|---|---|
| the 6 reference slots | `see doi:10.1038/nbt.1823 for details`, `PMID:12345 and more` |
| the 5 organism slots | `junk text 123`, `trailing 999`, and also bare `PMID:12345` or `doi:10.1038/nbt.1823`, which are not organisms at all |
| `gradient_pos_density` | `prefix 1.5 g/mL` |

The bare correct forms (`doi:10.1038/nbt.1823`, `Escherichia coli
[NCBITaxon:562]`, `562`, `1.5 g/mL`) validated before and still do. Nothing
previously rejected is now accepted.

### Which of these reach a consumer

All 17 changes are to `structured_pattern`, which becomes a `pattern` only in a
materialized build. The artifacts published at w3id.org are generated from the
un-materialized schema, so `project/jsonschema/mixs.schema.json` carries 4
distinct patterns, all from the 5 slots that also assert a literal `pattern`.
The other 306 structured patterns reach no consumer, which has been true since
v6.2.2 in December 2025.

For a slot carrying both, the literal `pattern` is what ships, and it was
already anchored per branch. `prev_pubs` publishes
`^PMID:\d+$|^doi:10.\d{2,9}/.*$|^https?:...$`, and
`see doi:10.1038/nbt.1823 for details` was rejected under v7.0.0 and is
rejected under v7.0.1. So on the published path these 12 are unchanged.

The tightening above is what the schema now means, and what the example data
under `src/data/examples/` is validated against. Closing the gap between that
and what is published is
https://github.com/GenomicsStandardsConsortium/mixs/issues/1021.

### What the count of 17 understates

This is a consistency repair, not a new rule. v7.0.0 already had 22 slots
carrying the correctly grouped `^({PMID}|{DOI}|{URL})$`; the 6 changed here were
the stragglers still on the ungrouped form, and v7.0.1 brings the total to 28.
The same holds for the organism and free-text families. The convention was
already the majority; these slots were the exceptions.

### `isotopolog_atom_pos` also had a placeholder that never resolved

Its syntax was `^{termLabel} {[termID]}|{text}$`, using `{[termID]}` where every
other term uses `\[{termID}\]`. As a regex that reads as a literal brace, a
character class of the letters in `termID`, and a closing brace, so it never
matched an ontology identifier. No data was affected, because the `{text}`
branch accepted everything anyway. v7.0.1 replaces it with the standard form.

## Doubled anchors: fixed in this window, invisible in this diff

https://github.com/GenomicsStandardsConsortium/mixs/pull/1382 — Remove the
doubled regex anchors, and test that they cannot come back merged in this window
and removed `^^...$$` from the literal `pattern` field of four slots, including
`prev_pubs`. It does not appear anywhere in this comparison, and that is correct:
the comparison records the materialized pattern, which comes from
`structured_pattern` and replaces whatever the literal `pattern` field said. The
doubled anchors were dead text that never reached a consumer. (An earlier
revision of this summary listed them as a change in the release; they are not
one.)

## What this comparison covers

The new side is `main` at 574e69e, one commit before the release commit. The only
later change to `src/mixs/schema/mixs.yaml` is `version: 7.0.0` to `version:
7.0.1`, so no term is affected, but the release's own version bump falls outside
the comparison. The only scalar difference recorded is the `source_file` path.

There are no rename candidates. The tool gained rename detection in
https://github.com/GenomicsStandardsConsortium/mixs/pull/1368 — Detect renames in
the comparison instead of leaving them to the summarizer, but with no names added
and none removed there is nothing to pair up, so nothing here needs a maintainer
to confirm.

The comparison emitted only `classes` and `slots`. Enums, prefixes and settings
are absent from the output rather than present and empty, so this summary makes
no claim about them.
