# ALTERNATIVE to linkml PR #3711 (fix(owlgen): do not cross-reference synthetic
# name-based URIs), done as post-processing so MIxS can build on released linkml.
#
# With --no-use-native-uris, owlgen asserts skos:exactMatch from a class's minted
# (numeric) URI to a synthetic name-based URI, e.g.
#   MIXS:0010003 skos:exactMatch MIXS:MigsBa
# The name-based URI is never declared, so the cross-reference dangles. Delete these:
# any exactMatch whose object is in the MIxS namespace but is not a minted numeric ID
# (i.e. a name-based URI). External-ontology exactMatches (non-MIxS objects) are kept.
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

DELETE { ?s skos:exactMatch ?o }
WHERE {
  ?s skos:exactMatch ?o .
  FILTER(STRSTARTS(STR(?o), "https://w3id.org/mixs/") &&
         !REGEX(STR(?o), "^https://w3id.org/mixs/[0-9]"))
}
