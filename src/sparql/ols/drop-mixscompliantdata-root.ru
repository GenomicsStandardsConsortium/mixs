# Drop the MixsCompliantData ontology-root marker.
#
# gen-owl --metadata-profile ols marks every parent-less class as an ontology
# root term (IAO:0000700). We only want Checklist and Extension (plus the OLS
# config's preferred_root_term) as entry points, not the internal
# MixsCompliantData domain class. This removes just that one marker; Checklist
# and Extension keep theirs.
PREFIX obo:  <http://purl.obolibrary.org/obo/>
PREFIX mixs: <https://w3id.org/mixs/>

DELETE { ?ont obo:IAO_0000700 mixs:MixsCompliantData }
WHERE  { ?ont obo:IAO_0000700 mixs:MixsCompliantData }
