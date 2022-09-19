from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

schema_file = "../model/schema/mixs.yaml"
view = SchemaView(schema_file)
schema = view.schema

del schema.classes
del schema.slots

print(yaml_dumper.dumps(schema))

# todo make a new name that indicates the intended version?
# todo check prefixes expansions, default prefix assertion, and w3id rules
#   for redirecting docs home, per-term docs, and artifacts esp yaml
# todo see linkml
#   https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/meta.yaml
#   id: https://w3id.org/linkml/meta
#   -> https://linkml.io/linkml-model/docs/meta/ (documentation)
#   w3id implementation?

# no subsets?

# DONE
# description: Minimal Information about any Sequence Standard
# id: http://w3id.org/mixs

# PARTIAL
# name: MIxS
# default_prefix: mixs.vocab

# TDOD
# imports:
# - linkml:types
# - checklists
# - core
# - agriculture
# - food_animal_and_animal_feed
# - food_farm_environment
# - food_food_production_facility
# - food_human_foods
# - symbiont_associated
# - host_associated
# - microbial_mat_biofilm
# - miscellaneous_natural_or_artificial_environment
# - plant_associated
# - sediment
# - soil
# - wastewater_sludge
# - water
# - human_associated
# - human_gut
# - human_oral
# - human_skin
# - human_vaginal
# - air
# - built_environment
# - hydrocarbon_resources_cores
# - hydrocarbon_resources_fluids_swabs

# prefixes:
#   linkml:
#     prefix_prefix: linkml
#     prefix_reference: https://w3id.org/linkml/
#   mixs.vocab:
#     prefix_prefix: mixs.vocab
#     prefix_reference: https://w3id.org/mixs/vocab/
#   MIXS:
#     prefix_prefix: MIXS
#     prefix_reference: https://w3id.org/mixs/terms/
#   MIGS:
#     prefix_prefix: MIGS
#     prefix_reference: https://w3id.org/mixs/migs/

