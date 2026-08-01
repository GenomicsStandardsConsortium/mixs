# MIxS v7.0.0 to v7.0.1

A patch release. No term was added, removed, renamed or redefined, and no
permissible value changed. Anything valid under v7.0.0 stays valid, with one
class of exception noted at the end.

## Ancient DNA data can now be submitted

This is the reason the release exists, and the counts do not show it.

MIxS v7.0.0 shipped the MInAS ancient DNA extension: the `Ancient` class, its
eight combinations with MIMS environment packages, and 44 terms. But a MIxS file
holds records in a labelled place per checklist-and-extension pairing, and those
nine classes had no such place. The classes existed and could not be used.

v7.0.1 attaches them. `MixsCompliantData` now carries `ancient_data` and the
eight `mims_*_ancient_data` labels, taking it from 335 to 344.

In the comparison this appears as a single line, "1 class definition change",
which is why this summary leads with it.

## Seventeen patterns now match what they were written to match

Each of these had a value-format rule whose anchors did not bind to the whole
rule, so text on either side of an otherwise-correct value was accepted.

`^A|B$` reads as "starts with A" or "ends with B", because alternation binds
loosest. Only the first branch was anchored at the start and only the last at the
end. Wrapping the alternation fixes it.

Twelve terms were accepting values they should have rejected:

| term | previously accepted |
|---|---|
| `animal_intrusion`, `cult_result_org`, `microb_start_taxID`, `serovar_or_serotype`, `spikein_org` | `junk text 123` |
| `gradient_pos_density` | `prefix 1.5 g/mL` |
| `internal_standard`, `prev_pubs`, `samp_decont_pretreat`, `sip_method`, `sop_experimental`, `sop_lib_preparation` | `garbage doi:10.1038/nbt.1823 garbage` |

Five more were repaired for consistency but are unchanged in effect, because one
branch of each accepts free text: `isotopolog_atom_pos`, `microb_cult_med`,
`samp_stor_media`, `seq_meth`, `spikein_growth_med`.

`isotopolog_atom_pos` also had a placeholder that never resolved,
`{[termID]}` where every other term uses `\[{termID}\]`. It matched a brace
rather than an ontology identifier. No data was affected, because the free-text
branch accepted everything regardless.

Four reference terms carried a duplicated anchor, `^^…$$`. Removing it changes
nothing: repeated anchors assert the same position.

## What this means if you submit data

Nothing to change, unless you were relying on the twelve terms above accepting
surrounding text. A value such as `see doi:10.1038/nbt.1823 for details` in
`prev_pubs` validated before and does not now. The bare reference,
`doi:10.1038/nbt.1823`, was always correct and still is.

## What this means if you consume MIxS

The published JSON Schema and OWL now describe the nine ancient DNA containers,
so a tool generated from v7.0.0 cannot round-trip an ancient DNA record and one
generated from v7.0.1 can.

Term identifiers, titles and definitions are untouched, so anything keyed on
`MIXS:` identifiers or on titles needs no change.
