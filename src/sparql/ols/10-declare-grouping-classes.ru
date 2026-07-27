# ALTERNATIVE to linkml PR #3681 (declare metamodel grouping classes referenced by
# add_root_classes), done as post-processing so MIxS can build on released linkml.
#
# With --add-root-classes, owlgen makes enums/permissible-values/classes subclasses
# of the LinkML metamodel grouping classes but (in released linkml) does not declare
# or label them, so OLS shows bare, unlabeled roots. Declare and label them
# (UpperCamel). Runs first so the title backfill and schema:name steps see their
# rdfs:label.
PREFIX linkml: <https://w3id.org/linkml/>
PREFIX rdfs:   <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:    <http://www.w3.org/2002/07/owl#>
PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>

INSERT DATA {
  linkml:EnumDefinition a owl:Class ;
    rdfs:label "EnumDefinition" ;
    skos:definition "an element whose instances must be drawn from a specified set of permissible values" .
  linkml:PermissibleValue a owl:Class ;
    rdfs:label "PermissibleValue" ;
    skos:definition "a permissible value, accompanied by intended text and an optional mapping to a concept URI" .
  linkml:ClassDefinition a owl:Class ;
    rdfs:label "ClassDefinition" ;
    skos:definition "an element whose instances are complex objects that may have slot-value assignments" .
}
