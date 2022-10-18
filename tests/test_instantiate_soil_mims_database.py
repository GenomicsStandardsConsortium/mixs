import pprint
import unittest

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

import schemasheets.generated.mixs_schemasheets_generated as mixs


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
