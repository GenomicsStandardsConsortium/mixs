# Append an OBO-Foundry-caveat suffix to the ontology description.
#
# This OWL is offered for convenience in ontology tools (EBI OLS search, API,
# embedding-based similar classes). It does not follow OBO Foundry conventions:
# MIxS reuses external ontology IRIs (SO, NCIT, FOODON, ENVO, ...) as its own
# permissible values, with MIxS labels and placement, so such an IRI does not
# carry that term's definition or hierarchy from its home ontology. The warning
# is added to the OWL only; the canonical schema description is unchanged.
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>

DELETE { ?ont skos:definition ?d }
INSERT { ?ont skos:definition ?withNote }
WHERE {
  ?ont a owl:Ontology ;
       skos:definition ?d .
  BIND(CONCAT(?d,
    " NOTE: this OWL is provided for convenience in ontology tools such as EBI OLS ",
    "(search, API, and embedding-based similar classes). It is generated from the ",
    "MIxS LinkML schema and does not follow OBO Foundry conventions: MIxS reuses ",
    "external ontology IRIs (for example from SO, NCIT, FOODON, and ENVO) as its own ",
    "permissible values, with MIxS labels and placement, so a MIxS reference to an ",
    "external IRI does not carry that term's definition or hierarchy from its home ",
    "ontology."
  ) AS ?withNote)
}
