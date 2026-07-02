# Append a caveat to the ontology description (OWL only; the canonical schema
# description is unchanged). MIxS is offered in OLS for browser conveniences, not
# as an ontology.
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>

DELETE { ?ont skos:definition ?d }
INSERT { ?ont skos:definition ?withNote }
WHERE {
  ?ont a owl:Ontology ;
       skos:definition ?d .
  BIND(CONCAT(?d,
    " NOTE: MIxS is offered in OLS to take advantage of the search, hierarchical browsing, ",
    "API access and pre-computed, embeddings-based identification of similar classes ",
    "and similar properties. It is not an ontology and users should anticipate some ",
    "pragmatic reuse of ontology-browser features."
  ) AS ?withNote)
}
