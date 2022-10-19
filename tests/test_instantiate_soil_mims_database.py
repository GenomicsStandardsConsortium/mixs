import pprint
import unittest

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.utils.csvutils import get_configmap

import schemasheets.generated.mixs_schemasheets_generated as mixs

import logging
from json_flattener import KeyConfig, GlobalConfig, Serializer
from json_flattener.flattener import CONFIGMAP
from linkml_runtime.linkml_model.meta import SlotDefinitionName, SchemaDefinition, \
    SlotDefinition, ClassDefinition, ClassDefinitionName
from linkml_runtime.utils.schemaview import SchemaView


def _get_key_config(schemaview: SchemaView, tgt_cls: ClassDefinitionName, sn: SlotDefinitionName, sep='_'):
    slot = schemaview.induced_slot(sn, tgt_cls)
    range = slot.range
    all_cls = schemaview.all_classes()
    if range in all_cls and schemaview.is_inlined(slot):
        mappings = {}
        is_complex = False
        for inner_sn in schemaview.class_slots(range):
            denormalized_sn = f'{sn}{sep}{inner_sn}'
            mappings[inner_sn] = denormalized_sn
            inner_slot = schemaview.induced_slot(inner_sn, range)
            inner_slot_range = inner_slot.range
            if (inner_slot_range in all_cls and inner_slot.inlined) or inner_slot.multivalued:
                is_complex = True
        if is_complex:
            serializers = [Serializer.json]
        else:
            serializers = []
        return KeyConfig(is_list=slot.multivalued, delete=True, flatten=True, mappings=mappings,
                         serializers=serializers)
    else:
        return None


class Minimal(unittest.TestCase):
    def test_inst_database(self):
        d = mixs.Database()
        self.assertTrue(type(d) == mixs.Database)

    def test_get_schema_name(self):
        mixs_source = "../schemasheets/yaml_out/mixs_schemasheets.yaml"
        mixs_view = SchemaView(mixs_source)
        assert mixs_view.schema.name == "MIXS"

    def test_report_requireds(self):
        mixs_source = "../schemasheets/yaml_out/mixs_schemasheets.yaml"
        mixs_view = SchemaView(mixs_source)
        ic = mixs_view.induced_class("MimsSoil")
        ic_attribs = ic.attributes
        requireds = []
        for a_name, a_slot_def in ic_attribs.items():
            if a_slot_def.required:
                requireds.append(a_name)
        requireds.sort()
        pprint.pprint(requireds)
        self.assertIn("project_name", requireds)

    # ['collection_date',
    #  'env_broad_scale',
    #  'env_local_scale',
    #  'env_medium',
    #  'geo_loc_name',
    #  'lat_lon',
    #  'project_name',
    #  'samp_name',
    #  'samp_taxon_id',
    #  'seq_meth']

    def test_inst_mims_soil_without_reqd_project_name(self):
        ms = mixs.MimsSoil(
            collection_date="2021-01-01",
            env_broad_scale="ENVO:00000000",
            env_local_scale="ENVO:00000000",
            env_medium="ENVO:00000000",
            geo_loc_name="USA: CA, San Diego",
            lat_lon="77 77",
            samp_taxon_id=12345,
            seq_meth="ENVO:00000000",
        )
        self.assertTrue(type(ms) == mixs.MimsSoil)

    def test_get_configmap(self):
        # mixs_source = "../schemasheets/generated/mixs_schemasheets_generated.yaml"
        mixs_source = "../schemasheets/yaml_out/mixs_schemasheets.yaml"
        mixs_view = SchemaView(mixs_source)
        ic = mixs_view.induced_class("MimsSoil")
        ic_attribs = ic.attributes
        requireds = []
        for a_name, a_slot_def in ic_attribs.items():
            if a_slot_def.required:
                requireds.append(a_name)
        requireds.sort()
        for r in requireds:
            print(r)
            cm = get_configmap(schemaview=mixs_view, index_slot=r)
            print(cm)
