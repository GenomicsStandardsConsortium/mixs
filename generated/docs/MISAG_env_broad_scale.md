
# Slot: env_broad_scale


Report the major environmental system the sample or specimen came from. The system(s) identified should have a coarse spatial grain, to provide the general environmental context of where the sampling was done (e.g. in the desert or a rainforest). We recommend using subclasses of EnvO’s biome class:  http://purl.obolibrary.org/obo/ENVO_00000428. EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS

URI: [mixs.vocab:MISAG_env_broad_scale](https://w3id.org/mixs/vocab/MISAG_env_broad_scale)


## Domain and Range

[MISAG](MISAG.md) &#8594;  <sub>1..1</sub> [String](types/String.md)

## Parents

 *  is_a: [env_broad_scale](env_broad_scale.md)

## Children


## Used by

 * [MISAG](MISAG.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | broad-scale environmental context |
| **Mappings:** | | MIXS:0000012 |
| **Comments:** | | Expected value: The major environment type(s) where the sample was collected. Recommend subclasses of biome [ENVO:00000428]. Multiple terms can be separated by one or more pipes. |
| **Examples:** | | Example(value='oceanic epipelagic zone biome [ENVO:01000033] for annotating a water sample from the photic zone in middle of the Atlantic Ocean', description=None) |

