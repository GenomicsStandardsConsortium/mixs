# Remove the internal MixsCompliantData domain class and every combination-relation
# object property it anchors (e.g. migs_ba_soil_data, migs_ba_air_data). These are
# modeling scaffolding: MixsCompliantData is the domain of the per-checklist x
# extension combination relations. They are not user-facing MIxS terms and clutter
# the OLS class and property lists. (This also removes the IAO:0000700 root marker,
# since that is a reference to MixsCompliantData.)
PREFIX mixs: <https://w3id.org/mixs/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

# 1. references TO the properties whose domain is MixsCompliantData
DELETE { ?s ?p ?prop }
WHERE  { ?prop rdfs:domain mixs:MixsCompliantData . ?s ?p ?prop } ;

# 2. those properties' own triples (label, domain, range, definition, ...)
DELETE { ?prop ?p ?o }
WHERE  { ?prop rdfs:domain mixs:MixsCompliantData . ?prop ?p ?o } ;

# 3. references TO MixsCompliantData (root marker, any remaining domain assertions)
DELETE { ?s ?p mixs:MixsCompliantData }
WHERE  { ?s ?p mixs:MixsCompliantData } ;

# 4. MixsCompliantData's own triples
DELETE { mixs:MixsCompliantData ?p ?o }
WHERE  { mixs:MixsCompliantData ?p ?o }
