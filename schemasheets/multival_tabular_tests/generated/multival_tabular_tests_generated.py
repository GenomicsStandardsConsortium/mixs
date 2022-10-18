# Auto generated from multival_tabular_tests_generated.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-10-18T17:30:11
# Schema: multival_tabular_tests
#
# id: http://example.org/multival_tabular_tests
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = CurieNamespace('', 'http://example.org/multival_tabular_tests/')


# Types

# Class references



@dataclass
class Organization(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/multival_tabular_tests/Organization")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/multival_tabular_tests/Organization")

    org_name: Optional[str] = None
    pet_names: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.org_name is not None and not isinstance(self.org_name, str):
            self.org_name = str(self.org_name)

        if not isinstance(self.pet_names, list):
            self.pet_names = [self.pet_names] if self.pet_names is not None else []
        self.pet_names = [v if isinstance(v, str) else str(v) for v in self.pet_names]

        super().__post_init__(**kwargs)


@dataclass
class Person(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/multival_tabular_tests/Person")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/multival_tabular_tests/Person")

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    hobbies: Optional[Union[Union[str, "HobbyEnum"], List[Union[str, "HobbyEnum"]]]] = empty_list()
    pet_names: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.first_name is not None and not isinstance(self.first_name, str):
            self.first_name = str(self.first_name)

        if self.last_name is not None and not isinstance(self.last_name, str):
            self.last_name = str(self.last_name)

        if not isinstance(self.hobbies, list):
            self.hobbies = [self.hobbies] if self.hobbies is not None else []
        self.hobbies = [v if isinstance(v, HobbyEnum) else HobbyEnum(v) for v in self.hobbies]

        if not isinstance(self.pet_names, list):
            self.pet_names = [self.pet_names] if self.pet_names is not None else []
        self.pet_names = [v if isinstance(v, str) else str(v) for v in self.pet_names]

        super().__post_init__(**kwargs)


@dataclass
class Pet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/multival_tabular_tests/Pet")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Pet"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/multival_tabular_tests/Pet")

    pet_name: Optional[str] = None
    species: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.pet_name is not None and not isinstance(self.pet_name, str):
            self.pet_name = str(self.pet_name)

        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

        super().__post_init__(**kwargs)


@dataclass
class Database(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/multival_tabular_tests/Database")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Database"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/multival_tabular_tests/Database")

    person_set: Optional[Union[Union[dict, Person], List[Union[dict, Person]]]] = empty_list()
    pet_set: Optional[Union[Union[dict, Pet], List[Union[dict, Pet]]]] = empty_list()
    org_set: Optional[Union[Union[dict, Organization], List[Union[dict, Organization]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.person_set, list):
            self.person_set = [self.person_set] if self.person_set is not None else []
        self.person_set = [v if isinstance(v, Person) else Person(**as_dict(v)) for v in self.person_set]

        if not isinstance(self.pet_set, list):
            self.pet_set = [self.pet_set] if self.pet_set is not None else []
        self.pet_set = [v if isinstance(v, Pet) else Pet(**as_dict(v)) for v in self.pet_set]

        if not isinstance(self.org_set, list):
            self.org_set = [self.org_set] if self.org_set is not None else []
        self.org_set = [v if isinstance(v, Organization) else Organization(**as_dict(v)) for v in self.org_set]

        super().__post_init__(**kwargs)


# Enumerations
class HobbyEnum(EnumDefinitionImpl):

    tennis = PermissibleValue(text="tennis")
    cooking = PermissibleValue(text="cooking")
    sewing = PermissibleValue(text="sewing")
    fishing = PermissibleValue(text="fishing")

    _defn = EnumDefinition(
        name="HobbyEnum",
    )

# Slots
class slots:
    pass

slots.org_set = Slot(uri=DEFAULT_.org_set, name="org_set", curie=DEFAULT_.curie('org_set'),
                   model_uri=DEFAULT_.org_set, domain=None, range=Optional[Union[Union[dict, Organization], List[Union[dict, Organization]]]])

slots.org_name = Slot(uri=DEFAULT_.org_name, name="org_name", curie=DEFAULT_.curie('org_name'),
                   model_uri=DEFAULT_.org_name, domain=None, range=Optional[str])

slots.pet_name = Slot(uri=DEFAULT_.pet_name, name="pet_name", curie=DEFAULT_.curie('pet_name'),
                   model_uri=DEFAULT_.pet_name, domain=None, range=Optional[str])

slots.species = Slot(uri=DEFAULT_.species, name="species", curie=DEFAULT_.curie('species'),
                   model_uri=DEFAULT_.species, domain=None, range=Optional[str])

slots.pet_names = Slot(uri=DEFAULT_.pet_names, name="pet_names", curie=DEFAULT_.curie('pet_names'),
                   model_uri=DEFAULT_.pet_names, domain=None, range=Optional[Union[str, List[str]]])

slots.person_set = Slot(uri=DEFAULT_.person_set, name="person_set", curie=DEFAULT_.curie('person_set'),
                   model_uri=DEFAULT_.person_set, domain=None, range=Optional[Union[Union[dict, Person], List[Union[dict, Person]]]])

slots.pet_set = Slot(uri=DEFAULT_.pet_set, name="pet_set", curie=DEFAULT_.curie('pet_set'),
                   model_uri=DEFAULT_.pet_set, domain=None, range=Optional[Union[Union[dict, Pet], List[Union[dict, Pet]]]])

slots.first_name = Slot(uri=DEFAULT_.first_name, name="first_name", curie=DEFAULT_.curie('first_name'),
                   model_uri=DEFAULT_.first_name, domain=None, range=Optional[str])

slots.last_name = Slot(uri=DEFAULT_.last_name, name="last_name", curie=DEFAULT_.curie('last_name'),
                   model_uri=DEFAULT_.last_name, domain=None, range=Optional[str])

slots.hobbies = Slot(uri=DEFAULT_.hobbies, name="hobbies", curie=DEFAULT_.curie('hobbies'),
                   model_uri=DEFAULT_.hobbies, domain=None, range=Optional[Union[Union[str, "HobbyEnum"], List[Union[str, "HobbyEnum"]]]])