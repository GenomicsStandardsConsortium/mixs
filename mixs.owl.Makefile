owl-clean:
	rm -rf mixs.testing.*.owl

mixs.testing.0.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format owl \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl.ttl \
		--use-native-uris \
		--useuris $< > $@ && date

mixs.testing.1.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format ttl \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl.ttl \
		--use-native-uris \
		--useuris $< > $@ && date

mixs.testing.2.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format turtle \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl.ttl \
		--use-native-uris \
		--useuris $< > $@ && date

mixs.testing.3.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format xml \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl.ttl \
		--use-native-uris \
		--useuris $< > $@ && date

mixs.testing.4.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format nt \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl \
		--use-native-uris \
		--useuris $< > $@ && date

mixs.testing.5.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format nt11 \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl \
		--use-native-uris \
		--useuris $< > $@ && date

mixs.testing.6.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format ntriples \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl \
		--use-native-uris \
		--useuris $< > $@ && date

mixs.testing.7.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format hext \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl \
		--use-native-uris \
		--useuris $< > $@ && date

mixs.testing.8.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format json-ld \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl \
		--use-native-uris \
		--useuris $< > $@ && date

mixs.testing.9.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format n3 \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl \
		--use-native-uris \
		--useuris $< > $@ && date


mixs.testing.10.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format nquads \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl \
		--use-native-uris \
		--useuris $< > $@ && date


mixs.testing.11.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format trig \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl \
		--use-native-uris \
		--useuris $< > $@ && date


mixs.testing.12.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format trix \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl \
		--use-native-uris \
		--useuris $< > $@ && date


mixs.testing.20.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--no-add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format owl \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl.ttl \
		--use-native-uris \
		--useuris $< > $@ && date

# 20 is default 0 but without ols annotations

mixs.testing.30.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://example.com/its_a_pv/" \
		--enum-iri-separator "#" \
		--format owl \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl.ttl \
		--use-native-uris \
		--useuris $< > $@ && date


mixs.testing.40.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format owl \
		--log_level WARNING \
		--mergeimports \
		--no-metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl.ttl \
		--use-native-uris \
		--useuris $< > $@ && date

# 40 is defualt 0 with no-metadata

mixs.testing.50.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format owl \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile rdfs \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl.ttl \
		--use-native-uris \
		--useuris $< > $@ && date

# only one difference in this case: http://www.w3.org/2004/02/skos/core#definition (linkml) vs rdfs:comment (rdfs)


mixs.testing.51.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format owl \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile ols \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl.ttl \
		--use-native-uris \
		--useuris $< > $@ && date

# ols style inlcudes  http://purl.obolibrary.org/obo/IAO_0000700 "has ontology root term" assertions on the top classes
# uses skos:definition liek linkml style


mixs.testing.60.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format owl \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl.ttl \
		--use-native-uris \
		--useuris $< > $@ && date

# --add-root-classes results in statemetns like SubClassOf(<https://w3id.org/mixs/WindowVertPosEnum> <https://w3id.org/linkml/EnumDefinition>)


mixs.testing.70.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format owl \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl.ttl \
		--use-native-uris \
		--useuris $< > $@ && date

# --assert-equivalent-classes leads to assertiosn like
# AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#exactMatch> <https://w3id.org/mixs/Agriculture> <https://w3id.org/mixs/0016018>)

mixs.testing.80.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format owl \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl.ttl \
		--use-native-uris \
		--useuris $< > $@ && date

# --metaclasses adds
# ClassAssertion(<https://w3id.org/linkml/ClassDefinition> <https://w3id.org/mixs/Agriculture>)

mixs.testing.90.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format owl \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl.ttl \
		--use-native-uris \
		--useuris $< > $@ && date

# mixins-as-expressions adds
# SubClassOf(<https://w3id.org/mixs/MigsBa> DataAllValuesFrom(<https://w3id.org/mixs/adapters> xsd:string))

mixs.testing.100.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format owl \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--type-objects \
		--ontology-uri-suffix .owl.ttl \
		--use-native-uris \
		--useuris $< > $@ && date

# --type-objects causes
# 2025-06-09 12:30:01,165 ERROR org.semanticweb.owlapi.rdf.rdfxml.parser.OWLRDFConsumer - Entity not properly recognized, missing triples in input? http://org.semanticweb.owlapi/error#Error1 for type Datatype
# - DataPropertyRange(<https://w3id.org/mixs/food_prod_char> xsd:string)
#- DataPropertyRange(<https://w3id.org/mixs/food_prod_synonym> xsd:string)
#- DataPropertyRange(<https://w3id.org/mixs/food_product_qual> DataIntersectionOf(xsd:string DatatypeRestriction(xsd:string facetRestriction(pattern "^([^\\s-]{1,2}|[^\\s-]+.+[^\\s-]+) \\[[a-zA-Z]{2,}:[a-zA-Z0-9]\\d+\\]$"^^xsd:string))))

mixs.testing.110.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format owl \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl.ttl \
		--no-use-native-uris \
		--useuris $< > $@ && date

# --no-use-native-uris
# MIXS:MigsEuAir instead MIXS:0010002_0016000

mixs.testing.120.owl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format owl \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile linkml \
		--no-add-root-classes \
		--no-assert-equivalent-classes \
		--no-metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl.ttl \
		--use-native-uris \
		--metauris $< > $@ && date

# metauris instead of useuris
# no difference seen



# robot diff --left mixs.testing.0.owl --right mixs.testing.1.owl
# Ontologies are identical
# but diff or md5sum may be differetnt
# but size in butes may be the same!

# OVERRIDING


# DOES NOT WORK
# --output $@

# NOT USING YET
# -im, --importmap FILENAME       Import mapping file

# --add-ols-annotations / --no-add-ols-annotations [default: add-ols-annotations]
# --add-root-classes / --no-add-root-classes [default: no-add-root-classes]
# --assert-equivalent-classes / --no-assert-equivalent-classes [default: no-assert-equivalent-classes]
# --default-permissible-value-type [default: http://www.w3.org/2002/07/owl#Class]
# --enum-iri-separator [default: #]
# --log_level [CRITICAL|ERROR|WARNING|INFO|DEBUG] [default: WARNING]
# --mergeimports / --no-mergeimports (default=mergeimports)
# --metaclasses / --no-metaclasses [default: no-metaclasses]
# --metadata / --no-metadata [default: metadata]
# --metadata-profile [linkml|rdfs|ols]  [default: linkml]
# --mixins-as-expressions / --no-mixins-as-expressions [default: no-mixins-as-expressions]
# --ontology-uri-suffix [default: .owl.ttl]
# --stacktrace / --no-stacktrace [default: no-stacktrace]
# --type-objects / --no-type-objects [default: no-type-objects]
# --use-native-uris / --no-use-native-uris [default: use-native-uris]
# --useuris / --metauris  [default: useuris]
# -f, --format [owl|ttl|json-ld|xml|n3|turtle|ntriples|nt|nt11|nquads|trix|trig|hext|patch] [default: owl]
# -v, --verbose --log_level (takes precedence over log_level)

# MAM recommends for OLS:
# --metadata-profile ols
  #--add-root-classes
  #--metaclasses
  #--assert-equivalent-classes HELPFUL BUT UGLY

mixs.ols.owl.ttl: src/mixs/schema/mixs.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format owl \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile ols \
		--add-root-classes \
		--no-assert-equivalent-classes \
		--metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl.ttl \
		--use-native-uris \
		--useuris $< > $@ && date
