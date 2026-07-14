# ALTERNATIVE to linkml PR #3713 (feat(owlgen): expose element name as schema:name),
# done as post-processing so MIxS can build on released linkml.
#
# OLS hides rdfs:label (the LinkML name) from term pages and annotation rows. Copy it
# to schema:name, which OLS displays, so the name is visible while dcterms:title stays
# the header. Runs after the grouping-class declarations so they get schema:name too.
PREFIX rdfs:   <http://www.w3.org/2000/01/rdf-schema#>
PREFIX schema: <http://schema.org/>

INSERT { ?s schema:name ?name }
WHERE  {
  ?s rdfs:label ?name .
  FILTER NOT EXISTS { ?s schema:name ?existing }
}
