# Remove skos:inScheme. It comes from the metamodel from_schema slot and points every
# element back at the schema id; OLS shows it (skos namespace) and adds no value for a
# browser user. Config cannot hide it and linkml has no supported way to suppress it,
# so delete it from the OLS OWL here.
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

DELETE { ?s skos:inScheme ?o }
WHERE  { ?s skos:inScheme ?o }
