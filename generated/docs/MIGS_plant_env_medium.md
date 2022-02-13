
# Slot: env_medium


Report the environmental material(s) immediately surrounding the sample or specimen at the time of sampling. We recommend using subclasses of 'environmental material' (http://purl.obolibrary.org/obo/ENVO_00010483). EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS . Terms from other OBO ontologies are permissible as long as they reference mass/volume nouns (e.g. air, water, blood) and not discrete, countable entities (e.g. a tree, a leaf, a table top).

URI: [mixs.vocab:MIGS_plant_env_medium](https://w3id.org/mixs/vocab/MIGS_plant_env_medium)


## Domain and Range

[MIGSPlant](MIGSPlant.md) &#8594;  <sub>1..1</sub> [String](types/String.md)

## Parents

 *  is_a: [env_medium](env_medium.md)

## Children


## Used by

 * [MIGSPlant](MIGSPlant.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | environmental medium |
| **Mappings:** | | MIXS:0000014 |
| **Comments:** | | Expected value: The material displaced by the entity at time of sampling. Recommend subclasses of environmental material [ENVO:00010483]. |
| **Examples:** | | Example(value='soil [ENVO:00001998]; Annotating a fish swimming in the upper 100 m of the Atlantic Ocean, consider: ocean water [ENVO:00002151]. Example: Annotating a duck on a pond consider: pond water [ENVO:00002228]|air [ENVO_00002005]', description=None) |

