# Auto generated from multival_tabular_tests_generated.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-10-18T10:59:22
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
class Person(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/multival_tabular_tests/Person")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "person"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/multival_tabular_tests/Person")

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    hobbies: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.first_name is not None and not isinstance(self.first_name, str):
            self.first_name = str(self.first_name)

        if self.last_name is not None and not isinstance(self.last_name, str):
            self.last_name = str(self.last_name)

        if not isinstance(self.hobbies, list):
            self.hobbies = [self.hobbies] if self.hobbies is not None else []
        self.hobbies = [v if isinstance(v, str) else str(v) for v in self.hobbies]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.first_name = Slot(uri=DEFAULT_.first_name, name="first_name", curie=DEFAULT_.curie('first_name'),
                   model_uri=DEFAULT_.first_name, domain=None, range=Optional[str])

slots.last_name = Slot(uri=DEFAULT_.last_name, name="last_name", curie=DEFAULT_.curie('last_name'),
                   model_uri=DEFAULT_.last_name, domain=None, range=Optional[str])

slots.hobbies = Slot(uri=DEFAULT_.hobbies, name="hobbies", curie=DEFAULT_.curie('hobbies'),
                   model_uri=DEFAULT_.hobbies, domain=None, range=Optional[Union[str, List[str]]])