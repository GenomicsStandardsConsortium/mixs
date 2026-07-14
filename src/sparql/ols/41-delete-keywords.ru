# Remove schema:keywords. OLS always displays schema.org properties, so the config
# cannot hide them, and suppressing them in linkml would mean editing every slot's
# keywords in the YAML (cross-cutting, affects all outputs) or an owlgen option the
# maintainers declined (linkml #3665). Delete them from the OLS OWL here.
PREFIX schema: <http://schema.org/>

DELETE { ?s schema:keywords ?k }
WHERE  { ?s schema:keywords ?k }
