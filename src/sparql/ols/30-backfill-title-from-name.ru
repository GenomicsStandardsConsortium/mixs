# Backfill dcterms:title from rdfs:label wherever a title is missing.
#
# OLS uses label_property (dcterms:title) for the header/tree label. MIxS classes
# and slots carry a title, but enums, permissible values, and the grouping classes
# do not, so a title-only label config would fall back to the raw shortform for
# them. Giving every named entity a title (its name where no real title exists)
# makes the labelling consistent (title-primary) without shortform fallbacks.
PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dcterms: <http://purl.org/dc/terms/>

INSERT { ?s dcterms:title ?label }
WHERE {
  ?s rdfs:label ?label .
  FILTER NOT EXISTS { ?s dcterms:title ?anyTitle }
}
