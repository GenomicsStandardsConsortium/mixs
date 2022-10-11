# Auto generated from database_test_generated.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-10-11T18:10:12
# Schema: MIXS
#
# id: https://example.com/mixs
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
MIXS = CurieNamespace('MIXS', 'https://example.com/mixs')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = MIXS


# Types

# Class references



@dataclass
class Database(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.Database
    class_class_curie: ClassVar[str] = "MIXS:Database"
    class_name: ClassVar[str] = "Database"
    class_model_uri: ClassVar[URIRef] = MIXS.Database

    mims_set: Optional[Union[Union[dict, "Mims"], List[Union[dict, "Mims"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.mims_set, list):
            self.mims_set = [self.mims_set] if self.mims_set is not None else []
        self.mims_set = [v if isinstance(v, Mims) else Mims(**as_dict(v)) for v in self.mims_set]

        super().__post_init__(**kwargs)


@dataclass
class Mims(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.Mims
    class_class_curie: ClassVar[str] = "MIXS:Mims"
    class_name: ClassVar[str] = "Mims"
    class_model_uri: ClassVar[URIRef] = MIXS.Mims

    collection_date: str = None
    env_broad_scale: str = None
    env_local_scale: str = None
    env_medium: str = None
    geo_loc_name: str = None
    lat_lon: str = None
    project_name: str = None
    samp_name: str = None
    samp_taxon_id: str = None
    seq_meth: str = None
    adapters: Optional[str] = None
    alt: Optional[str] = None
    annot: Optional[str] = None
    assembly_name: Optional[str] = None
    assembly_qual: Optional[str] = None
    assembly_software: Optional[str] = None
    associated_resource: Optional[str] = None
    depth: Optional[str] = None
    elev: Optional[str] = None
    experimental_factor: Optional[str] = None
    feat_pred: Optional[str] = None
    lib_layout: Optional[str] = None
    lib_reads_seqd: Optional[str] = None
    lib_screen: Optional[str] = None
    lib_size: Optional[str] = None
    lib_vector: Optional[str] = None
    mid: Optional[str] = None
    neg_cont_type: Optional[str] = None
    nucl_acid_amp: Optional[str] = None
    nucl_acid_ext: Optional[str] = None
    number_contig: Optional[str] = None
    pos_cont_type: Optional[str] = None
    ref_biomaterial: Optional[str] = None
    ref_db: Optional[str] = None
    rel_to_oxygen: Optional[str] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_mat_process: Optional[str] = None
    samp_size: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    sim_search_meth: Optional[str] = None
    size_frac: Optional[str] = None
    sop: Optional[str] = None
    source_mat_id: Optional[str] = None
    tax_class: Optional[str] = None
    temp: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_date):
            self.MissingRequiredField("collection_date")
        if not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self._is_empty(self.env_broad_scale):
            self.MissingRequiredField("env_broad_scale")
        if not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self._is_empty(self.env_local_scale):
            self.MissingRequiredField("env_local_scale")
        if not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self._is_empty(self.env_medium):
            self.MissingRequiredField("env_medium")
        if not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self._is_empty(self.geo_loc_name):
            self.MissingRequiredField("geo_loc_name")
        if not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self._is_empty(self.lat_lon):
            self.MissingRequiredField("lat_lon")
        if not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if self._is_empty(self.project_name):
            self.MissingRequiredField("project_name")
        if not isinstance(self.project_name, str):
            self.project_name = str(self.project_name)

        if self._is_empty(self.samp_name):
            self.MissingRequiredField("samp_name")
        if not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if self._is_empty(self.samp_taxon_id):
            self.MissingRequiredField("samp_taxon_id")
        if not isinstance(self.samp_taxon_id, str):
            self.samp_taxon_id = str(self.samp_taxon_id)

        if self._is_empty(self.seq_meth):
            self.MissingRequiredField("seq_meth")
        if not isinstance(self.seq_meth, str):
            self.seq_meth = str(self.seq_meth)

        if self.adapters is not None and not isinstance(self.adapters, str):
            self.adapters = str(self.adapters)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.annot is not None and not isinstance(self.annot, str):
            self.annot = str(self.annot)

        if self.assembly_name is not None and not isinstance(self.assembly_name, str):
            self.assembly_name = str(self.assembly_name)

        if self.assembly_qual is not None and not isinstance(self.assembly_qual, str):
            self.assembly_qual = str(self.assembly_qual)

        if self.assembly_software is not None and not isinstance(self.assembly_software, str):
            self.assembly_software = str(self.assembly_software)

        if self.associated_resource is not None and not isinstance(self.associated_resource, str):
            self.associated_resource = str(self.associated_resource)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.feat_pred is not None and not isinstance(self.feat_pred, str):
            self.feat_pred = str(self.feat_pred)

        if self.lib_layout is not None and not isinstance(self.lib_layout, str):
            self.lib_layout = str(self.lib_layout)

        if self.lib_reads_seqd is not None and not isinstance(self.lib_reads_seqd, str):
            self.lib_reads_seqd = str(self.lib_reads_seqd)

        if self.lib_screen is not None and not isinstance(self.lib_screen, str):
            self.lib_screen = str(self.lib_screen)

        if self.lib_size is not None and not isinstance(self.lib_size, str):
            self.lib_size = str(self.lib_size)

        if self.lib_vector is not None and not isinstance(self.lib_vector, str):
            self.lib_vector = str(self.lib_vector)

        if self.mid is not None and not isinstance(self.mid, str):
            self.mid = str(self.mid)

        if self.neg_cont_type is not None and not isinstance(self.neg_cont_type, str):
            self.neg_cont_type = str(self.neg_cont_type)

        if self.nucl_acid_amp is not None and not isinstance(self.nucl_acid_amp, str):
            self.nucl_acid_amp = str(self.nucl_acid_amp)

        if self.nucl_acid_ext is not None and not isinstance(self.nucl_acid_ext, str):
            self.nucl_acid_ext = str(self.nucl_acid_ext)

        if self.number_contig is not None and not isinstance(self.number_contig, str):
            self.number_contig = str(self.number_contig)

        if self.pos_cont_type is not None and not isinstance(self.pos_cont_type, str):
            self.pos_cont_type = str(self.pos_cont_type)

        if self.ref_biomaterial is not None and not isinstance(self.ref_biomaterial, str):
            self.ref_biomaterial = str(self.ref_biomaterial)

        if self.ref_db is not None and not isinstance(self.ref_db, str):
            self.ref_db = str(self.ref_db)

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, str):
            self.rel_to_oxygen = str(self.rel_to_oxygen)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.samp_vol_we_dna_ext is not None and not isinstance(self.samp_vol_we_dna_ext, str):
            self.samp_vol_we_dna_ext = str(self.samp_vol_we_dna_ext)

        if self.sim_search_meth is not None and not isinstance(self.sim_search_meth, str):
            self.sim_search_meth = str(self.sim_search_meth)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.sop is not None and not isinstance(self.sop, str):
            self.sop = str(self.sop)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        if self.tax_class is not None and not isinstance(self.tax_class, str):
            self.tax_class = str(self.tax_class)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.mims_set = Slot(uri=MIXS.mims_set, name="mims_set", curie=MIXS.curie('mims_set'),
                   model_uri=MIXS.mims_set, domain=None, range=Optional[str])

slots.samp_name = Slot(uri=MIXS.samp_name, name="samp_name", curie=MIXS.curie('samp_name'),
                   model_uri=MIXS.samp_name, domain=None, range=str)

slots.adapters = Slot(uri=MIXS.adapters, name="adapters", curie=MIXS.curie('adapters'),
                   model_uri=MIXS.adapters, domain=None, range=Optional[str])

slots.alt = Slot(uri=MIXS.alt, name="alt", curie=MIXS.curie('alt'),
                   model_uri=MIXS.alt, domain=None, range=Optional[str])

slots.annot = Slot(uri=MIXS.annot, name="annot", curie=MIXS.curie('annot'),
                   model_uri=MIXS.annot, domain=None, range=Optional[str])

slots.assembly_name = Slot(uri=MIXS.assembly_name, name="assembly_name", curie=MIXS.curie('assembly_name'),
                   model_uri=MIXS.assembly_name, domain=None, range=Optional[str])

slots.assembly_qual = Slot(uri=MIXS.assembly_qual, name="assembly_qual", curie=MIXS.curie('assembly_qual'),
                   model_uri=MIXS.assembly_qual, domain=None, range=Optional[str])

slots.assembly_software = Slot(uri=MIXS.assembly_software, name="assembly_software", curie=MIXS.curie('assembly_software'),
                   model_uri=MIXS.assembly_software, domain=None, range=Optional[str])

slots.associated_resource = Slot(uri=MIXS.associated_resource, name="associated resource", curie=MIXS.curie('associated_resource'),
                   model_uri=MIXS.associated_resource, domain=None, range=Optional[str])

slots.bin_param = Slot(uri=MIXS.bin_param, name="bin_param", curie=MIXS.curie('bin_param'),
                   model_uri=MIXS.bin_param, domain=None, range=Optional[str])

slots.bin_software = Slot(uri=MIXS.bin_software, name="bin_software", curie=MIXS.curie('bin_software'),
                   model_uri=MIXS.bin_software, domain=None, range=Optional[str])

slots.biotic_relationship = Slot(uri=MIXS.biotic_relationship, name="biotic_relationship", curie=MIXS.curie('biotic_relationship'),
                   model_uri=MIXS.biotic_relationship, domain=None, range=Optional[str])

slots.chimera_check = Slot(uri=MIXS.chimera_check, name="chimera_check", curie=MIXS.curie('chimera_check'),
                   model_uri=MIXS.chimera_check, domain=None, range=Optional[str])

slots.collection_date = Slot(uri=MIXS.collection_date, name="collection_date", curie=MIXS.curie('collection_date'),
                   model_uri=MIXS.collection_date, domain=None, range=Optional[str])

slots.compl_appr = Slot(uri=MIXS.compl_appr, name="compl_appr", curie=MIXS.curie('compl_appr'),
                   model_uri=MIXS.compl_appr, domain=None, range=Optional[str])

slots.compl_score = Slot(uri=MIXS.compl_score, name="compl_score", curie=MIXS.curie('compl_score'),
                   model_uri=MIXS.compl_score, domain=None, range=Optional[str])

slots.compl_software = Slot(uri=MIXS.compl_software, name="compl_software", curie=MIXS.curie('compl_software'),
                   model_uri=MIXS.compl_software, domain=None, range=Optional[str])

slots.contam_score = Slot(uri=MIXS.contam_score, name="contam_score", curie=MIXS.curie('contam_score'),
                   model_uri=MIXS.contam_score, domain=None, range=Optional[str])

slots.contam_screen_input = Slot(uri=MIXS.contam_screen_input, name="contam_screen_input", curie=MIXS.curie('contam_screen_input'),
                   model_uri=MIXS.contam_screen_input, domain=None, range=Optional[str])

slots.contam_screen_param = Slot(uri=MIXS.contam_screen_param, name="contam_screen_param", curie=MIXS.curie('contam_screen_param'),
                   model_uri=MIXS.contam_screen_param, domain=None, range=Optional[str])

slots.decontam_software = Slot(uri=MIXS.decontam_software, name="decontam_software", curie=MIXS.curie('decontam_software'),
                   model_uri=MIXS.decontam_software, domain=None, range=Optional[str])

slots.depth = Slot(uri=MIXS.depth, name="depth", curie=MIXS.curie('depth'),
                   model_uri=MIXS.depth, domain=None, range=Optional[str])

slots.detec_type = Slot(uri=MIXS.detec_type, name="detec_type", curie=MIXS.curie('detec_type'),
                   model_uri=MIXS.detec_type, domain=None, range=Optional[str])

slots.elev = Slot(uri=MIXS.elev, name="elev", curie=MIXS.curie('elev'),
                   model_uri=MIXS.elev, domain=None, range=Optional[str])

slots.encoded_traits = Slot(uri=MIXS.encoded_traits, name="encoded_traits", curie=MIXS.curie('encoded_traits'),
                   model_uri=MIXS.encoded_traits, domain=None, range=Optional[str])

slots.env_broad_scale = Slot(uri=MIXS.env_broad_scale, name="env_broad_scale", curie=MIXS.curie('env_broad_scale'),
                   model_uri=MIXS.env_broad_scale, domain=None, range=Optional[str])

slots.env_local_scale = Slot(uri=MIXS.env_local_scale, name="env_local_scale", curie=MIXS.curie('env_local_scale'),
                   model_uri=MIXS.env_local_scale, domain=None, range=Optional[str])

slots.env_medium = Slot(uri=MIXS.env_medium, name="env_medium", curie=MIXS.curie('env_medium'),
                   model_uri=MIXS.env_medium, domain=None, range=Optional[str])

slots.estimated_size = Slot(uri=MIXS.estimated_size, name="estimated_size", curie=MIXS.curie('estimated_size'),
                   model_uri=MIXS.estimated_size, domain=None, range=Optional[str])

slots.experimental_factor = Slot(uri=MIXS.experimental_factor, name="experimental_factor", curie=MIXS.curie('experimental_factor'),
                   model_uri=MIXS.experimental_factor, domain=None, range=Optional[str])

slots.extrachrom_elements = Slot(uri=MIXS.extrachrom_elements, name="extrachrom_elements", curie=MIXS.curie('extrachrom_elements'),
                   model_uri=MIXS.extrachrom_elements, domain=None, range=Optional[str])

slots.feat_pred = Slot(uri=MIXS.feat_pred, name="feat_pred", curie=MIXS.curie('feat_pred'),
                   model_uri=MIXS.feat_pred, domain=None, range=Optional[str])

slots.geo_loc_name = Slot(uri=MIXS.geo_loc_name, name="geo_loc_name", curie=MIXS.curie('geo_loc_name'),
                   model_uri=MIXS.geo_loc_name, domain=None, range=Optional[str])

slots.host_disease_stat = Slot(uri=MIXS.host_disease_stat, name="host_disease_stat", curie=MIXS.curie('host_disease_stat'),
                   model_uri=MIXS.host_disease_stat, domain=None, range=Optional[str])

slots.host_pred_appr = Slot(uri=MIXS.host_pred_appr, name="host_pred_appr", curie=MIXS.curie('host_pred_appr'),
                   model_uri=MIXS.host_pred_appr, domain=None, range=Optional[str])

slots.host_pred_est_acc = Slot(uri=MIXS.host_pred_est_acc, name="host_pred_est_acc", curie=MIXS.curie('host_pred_est_acc'),
                   model_uri=MIXS.host_pred_est_acc, domain=None, range=Optional[str])

slots.host_spec_range = Slot(uri=MIXS.host_spec_range, name="host_spec_range", curie=MIXS.curie('host_spec_range'),
                   model_uri=MIXS.host_spec_range, domain=None, range=Optional[str])

slots.isol_growth_condt = Slot(uri=MIXS.isol_growth_condt, name="isol_growth_condt", curie=MIXS.curie('isol_growth_condt'),
                   model_uri=MIXS.isol_growth_condt, domain=None, range=Optional[str])

slots.lat_lon = Slot(uri=MIXS.lat_lon, name="lat_lon", curie=MIXS.curie('lat_lon'),
                   model_uri=MIXS.lat_lon, domain=None, range=Optional[str])

slots.lib_layout = Slot(uri=MIXS.lib_layout, name="lib_layout", curie=MIXS.curie('lib_layout'),
                   model_uri=MIXS.lib_layout, domain=None, range=Optional[str])

slots.lib_reads_seqd = Slot(uri=MIXS.lib_reads_seqd, name="lib_reads_seqd", curie=MIXS.curie('lib_reads_seqd'),
                   model_uri=MIXS.lib_reads_seqd, domain=None, range=Optional[str])

slots.lib_screen = Slot(uri=MIXS.lib_screen, name="lib_screen", curie=MIXS.curie('lib_screen'),
                   model_uri=MIXS.lib_screen, domain=None, range=Optional[str])

slots.lib_size = Slot(uri=MIXS.lib_size, name="lib_size", curie=MIXS.curie('lib_size'),
                   model_uri=MIXS.lib_size, domain=None, range=Optional[str])

slots.lib_vector = Slot(uri=MIXS.lib_vector, name="lib_vector", curie=MIXS.curie('lib_vector'),
                   model_uri=MIXS.lib_vector, domain=None, range=Optional[str])

slots.mag_cov_software = Slot(uri=MIXS.mag_cov_software, name="mag_cov_software", curie=MIXS.curie('mag_cov_software'),
                   model_uri=MIXS.mag_cov_software, domain=None, range=Optional[str])

slots.mid = Slot(uri=MIXS.mid, name="mid", curie=MIXS.curie('mid'),
                   model_uri=MIXS.mid, domain=None, range=Optional[str])

slots.neg_cont_type = Slot(uri=MIXS.neg_cont_type, name="neg_cont_type", curie=MIXS.curie('neg_cont_type'),
                   model_uri=MIXS.neg_cont_type, domain=None, range=Optional[str])

slots.nucl_acid_amp = Slot(uri=MIXS.nucl_acid_amp, name="nucl_acid_amp", curie=MIXS.curie('nucl_acid_amp'),
                   model_uri=MIXS.nucl_acid_amp, domain=None, range=Optional[str])

slots.nucl_acid_ext = Slot(uri=MIXS.nucl_acid_ext, name="nucl_acid_ext", curie=MIXS.curie('nucl_acid_ext'),
                   model_uri=MIXS.nucl_acid_ext, domain=None, range=Optional[str])

slots.num_replicons = Slot(uri=MIXS.num_replicons, name="num_replicons", curie=MIXS.curie('num_replicons'),
                   model_uri=MIXS.num_replicons, domain=None, range=Optional[str])

slots.number_contig = Slot(uri=MIXS.number_contig, name="number_contig", curie=MIXS.curie('number_contig'),
                   model_uri=MIXS.number_contig, domain=None, range=Optional[str])

slots.otu_class_appr = Slot(uri=MIXS.otu_class_appr, name="otu_class_appr", curie=MIXS.curie('otu_class_appr'),
                   model_uri=MIXS.otu_class_appr, domain=None, range=Optional[str])

slots.otu_db = Slot(uri=MIXS.otu_db, name="otu_db", curie=MIXS.curie('otu_db'),
                   model_uri=MIXS.otu_db, domain=None, range=Optional[str])

slots.otu_seq_comp_appr = Slot(uri=MIXS.otu_seq_comp_appr, name="otu_seq_comp_appr", curie=MIXS.curie('otu_seq_comp_appr'),
                   model_uri=MIXS.otu_seq_comp_appr, domain=None, range=Optional[str])

slots.pathogenicity = Slot(uri=MIXS.pathogenicity, name="pathogenicity", curie=MIXS.curie('pathogenicity'),
                   model_uri=MIXS.pathogenicity, domain=None, range=Optional[str])

slots.pcr_cond = Slot(uri=MIXS.pcr_cond, name="pcr_cond", curie=MIXS.curie('pcr_cond'),
                   model_uri=MIXS.pcr_cond, domain=None, range=Optional[str])

slots.pcr_primers = Slot(uri=MIXS.pcr_primers, name="pcr_primers", curie=MIXS.curie('pcr_primers'),
                   model_uri=MIXS.pcr_primers, domain=None, range=Optional[str])

slots.ploidy = Slot(uri=MIXS.ploidy, name="ploidy", curie=MIXS.curie('ploidy'),
                   model_uri=MIXS.ploidy, domain=None, range=Optional[str])

slots.pos_cont_type = Slot(uri=MIXS.pos_cont_type, name="pos_cont_type", curie=MIXS.curie('pos_cont_type'),
                   model_uri=MIXS.pos_cont_type, domain=None, range=Optional[str])

slots.pred_genome_struc = Slot(uri=MIXS.pred_genome_struc, name="pred_genome_struc", curie=MIXS.curie('pred_genome_struc'),
                   model_uri=MIXS.pred_genome_struc, domain=None, range=Optional[str])

slots.pred_genome_type = Slot(uri=MIXS.pred_genome_type, name="pred_genome_type", curie=MIXS.curie('pred_genome_type'),
                   model_uri=MIXS.pred_genome_type, domain=None, range=Optional[str])

slots.project_name = Slot(uri=MIXS.project_name, name="project_name", curie=MIXS.curie('project_name'),
                   model_uri=MIXS.project_name, domain=None, range=Optional[str])

slots.propagation = Slot(uri=MIXS.propagation, name="propagation", curie=MIXS.curie('propagation'),
                   model_uri=MIXS.propagation, domain=None, range=Optional[str])

slots.reassembly_bin = Slot(uri=MIXS.reassembly_bin, name="reassembly_bin", curie=MIXS.curie('reassembly_bin'),
                   model_uri=MIXS.reassembly_bin, domain=None, range=Optional[str])

slots.ref_biomaterial = Slot(uri=MIXS.ref_biomaterial, name="ref_biomaterial", curie=MIXS.curie('ref_biomaterial'),
                   model_uri=MIXS.ref_biomaterial, domain=None, range=Optional[str])

slots.ref_db = Slot(uri=MIXS.ref_db, name="ref_db", curie=MIXS.curie('ref_db'),
                   model_uri=MIXS.ref_db, domain=None, range=Optional[str])

slots.rel_to_oxygen = Slot(uri=MIXS.rel_to_oxygen, name="rel_to_oxygen", curie=MIXS.curie('rel_to_oxygen'),
                   model_uri=MIXS.rel_to_oxygen, domain=None, range=Optional[str])

slots.samp_collec_device = Slot(uri=MIXS.samp_collec_device, name="samp_collec_device", curie=MIXS.curie('samp_collec_device'),
                   model_uri=MIXS.samp_collec_device, domain=None, range=Optional[str])

slots.samp_collec_method = Slot(uri=MIXS.samp_collec_method, name="samp_collec_method", curie=MIXS.curie('samp_collec_method'),
                   model_uri=MIXS.samp_collec_method, domain=None, range=Optional[str])

slots.samp_mat_process = Slot(uri=MIXS.samp_mat_process, name="samp_mat_process", curie=MIXS.curie('samp_mat_process'),
                   model_uri=MIXS.samp_mat_process, domain=None, range=Optional[str])

slots.samp_size = Slot(uri=MIXS.samp_size, name="samp_size", curie=MIXS.curie('samp_size'),
                   model_uri=MIXS.samp_size, domain=None, range=Optional[str])

slots.samp_taxon_id = Slot(uri=MIXS.samp_taxon_id, name="samp_taxon_id", curie=MIXS.curie('samp_taxon_id'),
                   model_uri=MIXS.samp_taxon_id, domain=None, range=Optional[str])

slots.samp_vol_we_dna_ext = Slot(uri=MIXS.samp_vol_we_dna_ext, name="samp_vol_we_dna_ext", curie=MIXS.curie('samp_vol_we_dna_ext'),
                   model_uri=MIXS.samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.seq_meth = Slot(uri=MIXS.seq_meth, name="seq_meth", curie=MIXS.curie('seq_meth'),
                   model_uri=MIXS.seq_meth, domain=None, range=Optional[str])

slots.seq_quality_check = Slot(uri=MIXS.seq_quality_check, name="seq_quality_check", curie=MIXS.curie('seq_quality_check'),
                   model_uri=MIXS.seq_quality_check, domain=None, range=Optional[str])

slots.sim_search_meth = Slot(uri=MIXS.sim_search_meth, name="sim_search_meth", curie=MIXS.curie('sim_search_meth'),
                   model_uri=MIXS.sim_search_meth, domain=None, range=Optional[str])

slots.single_cell_lysis_appr = Slot(uri=MIXS.single_cell_lysis_appr, name="single_cell_lysis_appr", curie=MIXS.curie('single_cell_lysis_appr'),
                   model_uri=MIXS.single_cell_lysis_appr, domain=None, range=Optional[str])

slots.single_cell_lysis_prot = Slot(uri=MIXS.single_cell_lysis_prot, name="single_cell_lysis_prot", curie=MIXS.curie('single_cell_lysis_prot'),
                   model_uri=MIXS.single_cell_lysis_prot, domain=None, range=Optional[str])

slots.size_frac = Slot(uri=MIXS.size_frac, name="size_frac", curie=MIXS.curie('size_frac'),
                   model_uri=MIXS.size_frac, domain=None, range=Optional[str])

slots.sop = Slot(uri=MIXS.sop, name="sop", curie=MIXS.curie('sop'),
                   model_uri=MIXS.sop, domain=None, range=Optional[str])

slots.sort_tech = Slot(uri=MIXS.sort_tech, name="sort_tech", curie=MIXS.curie('sort_tech'),
                   model_uri=MIXS.sort_tech, domain=None, range=Optional[str])

slots.source_mat_id = Slot(uri=MIXS.source_mat_id, name="source_mat_id", curie=MIXS.curie('source_mat_id'),
                   model_uri=MIXS.source_mat_id, domain=None, range=Optional[str])

slots.source_uvig = Slot(uri=MIXS.source_uvig, name="source_uvig", curie=MIXS.curie('source_uvig'),
                   model_uri=MIXS.source_uvig, domain=None, range=Optional[str])

slots.specific_host = Slot(uri=MIXS.specific_host, name="specific_host", curie=MIXS.curie('specific_host'),
                   model_uri=MIXS.specific_host, domain=None, range=Optional[str])

slots.subspecf_gen_lin = Slot(uri=MIXS.subspecf_gen_lin, name="subspecf_gen_lin", curie=MIXS.curie('subspecf_gen_lin'),
                   model_uri=MIXS.subspecf_gen_lin, domain=None, range=Optional[str])

slots.target_gene = Slot(uri=MIXS.target_gene, name="target_gene", curie=MIXS.curie('target_gene'),
                   model_uri=MIXS.target_gene, domain=None, range=Optional[str])

slots.target_subfragment = Slot(uri=MIXS.target_subfragment, name="target_subfragment", curie=MIXS.curie('target_subfragment'),
                   model_uri=MIXS.target_subfragment, domain=None, range=Optional[str])

slots.tax_class = Slot(uri=MIXS.tax_class, name="tax_class", curie=MIXS.curie('tax_class'),
                   model_uri=MIXS.tax_class, domain=None, range=Optional[str])

slots.tax_ident = Slot(uri=MIXS.tax_ident, name="tax_ident", curie=MIXS.curie('tax_ident'),
                   model_uri=MIXS.tax_ident, domain=None, range=Optional[str])

slots.temp = Slot(uri=MIXS.temp, name="temp", curie=MIXS.curie('temp'),
                   model_uri=MIXS.temp, domain=None, range=Optional[str])

slots.trna_ext_software = Slot(uri=MIXS.trna_ext_software, name="trna_ext_software", curie=MIXS.curie('trna_ext_software'),
                   model_uri=MIXS.trna_ext_software, domain=None, range=Optional[str])

slots.trnas = Slot(uri=MIXS.trnas, name="trnas", curie=MIXS.curie('trnas'),
                   model_uri=MIXS.trnas, domain=None, range=Optional[str])

slots.trophic_level = Slot(uri=MIXS.trophic_level, name="trophic_level", curie=MIXS.curie('trophic_level'),
                   model_uri=MIXS.trophic_level, domain=None, range=Optional[str])

slots.vir_ident_software = Slot(uri=MIXS.vir_ident_software, name="vir_ident_software", curie=MIXS.curie('vir_ident_software'),
                   model_uri=MIXS.vir_ident_software, domain=None, range=Optional[str])

slots.virus_enrich_appr = Slot(uri=MIXS.virus_enrich_appr, name="virus_enrich_appr", curie=MIXS.curie('virus_enrich_appr'),
                   model_uri=MIXS.virus_enrich_appr, domain=None, range=Optional[str])

slots.wga_amp_appr = Slot(uri=MIXS.wga_amp_appr, name="wga_amp_appr", curie=MIXS.curie('wga_amp_appr'),
                   model_uri=MIXS.wga_amp_appr, domain=None, range=Optional[str])

slots.wga_amp_kit = Slot(uri=MIXS.wga_amp_kit, name="wga_amp_kit", curie=MIXS.curie('wga_amp_kit'),
                   model_uri=MIXS.wga_amp_kit, domain=None, range=Optional[str])

slots.x_16s_recover = Slot(uri=MIXS.x_16s_recover, name="x_16s_recover", curie=MIXS.curie('x_16s_recover'),
                   model_uri=MIXS.x_16s_recover, domain=None, range=Optional[str])

slots.x_16s_recover_software = Slot(uri=MIXS.x_16s_recover_software, name="x_16s_recover_software", curie=MIXS.curie('x_16s_recover_software'),
                   model_uri=MIXS.x_16s_recover_software, domain=None, range=Optional[str])

slots.Database_mims_set = Slot(uri=MIXS.mims_set, name="Database_mims_set", curie=MIXS.curie('mims_set'),
                   model_uri=MIXS.Database_mims_set, domain=Database, range=Optional[Union[Union[dict, "Mims"], List[Union[dict, "Mims"]]]])

slots.Mims_adapters = Slot(uri=MIXS.adapters, name="Mims_adapters", curie=MIXS.curie('adapters'),
                   model_uri=MIXS.Mims_adapters, domain=Mims, range=Optional[str])

slots.Mims_alt = Slot(uri=MIXS.alt, name="Mims_alt", curie=MIXS.curie('alt'),
                   model_uri=MIXS.Mims_alt, domain=Mims, range=Optional[str])

slots.Mims_annot = Slot(uri=MIXS.annot, name="Mims_annot", curie=MIXS.curie('annot'),
                   model_uri=MIXS.Mims_annot, domain=Mims, range=Optional[str])

slots.Mims_assembly_name = Slot(uri=MIXS.assembly_name, name="Mims_assembly_name", curie=MIXS.curie('assembly_name'),
                   model_uri=MIXS.Mims_assembly_name, domain=Mims, range=Optional[str])

slots.Mims_assembly_qual = Slot(uri=MIXS.assembly_qual, name="Mims_assembly_qual", curie=MIXS.curie('assembly_qual'),
                   model_uri=MIXS.Mims_assembly_qual, domain=Mims, range=Optional[str])

slots.Mims_assembly_software = Slot(uri=MIXS.assembly_software, name="Mims_assembly_software", curie=MIXS.curie('assembly_software'),
                   model_uri=MIXS.Mims_assembly_software, domain=Mims, range=Optional[str])

slots.Mims_associated_resource = Slot(uri=MIXS.associated_resource, name="Mims_associated resource", curie=MIXS.curie('associated_resource'),
                   model_uri=MIXS.Mims_associated_resource, domain=Mims, range=Optional[str])

slots.Mims_collection_date = Slot(uri=MIXS.collection_date, name="Mims_collection_date", curie=MIXS.curie('collection_date'),
                   model_uri=MIXS.Mims_collection_date, domain=Mims, range=str)

slots.Mims_depth = Slot(uri=MIXS.depth, name="Mims_depth", curie=MIXS.curie('depth'),
                   model_uri=MIXS.Mims_depth, domain=Mims, range=Optional[str])

slots.Mims_elev = Slot(uri=MIXS.elev, name="Mims_elev", curie=MIXS.curie('elev'),
                   model_uri=MIXS.Mims_elev, domain=Mims, range=Optional[str])

slots.Mims_env_broad_scale = Slot(uri=MIXS.env_broad_scale, name="Mims_env_broad_scale", curie=MIXS.curie('env_broad_scale'),
                   model_uri=MIXS.Mims_env_broad_scale, domain=Mims, range=str)

slots.Mims_env_local_scale = Slot(uri=MIXS.env_local_scale, name="Mims_env_local_scale", curie=MIXS.curie('env_local_scale'),
                   model_uri=MIXS.Mims_env_local_scale, domain=Mims, range=str)

slots.Mims_env_medium = Slot(uri=MIXS.env_medium, name="Mims_env_medium", curie=MIXS.curie('env_medium'),
                   model_uri=MIXS.Mims_env_medium, domain=Mims, range=str)

slots.Mims_experimental_factor = Slot(uri=MIXS.experimental_factor, name="Mims_experimental_factor", curie=MIXS.curie('experimental_factor'),
                   model_uri=MIXS.Mims_experimental_factor, domain=Mims, range=Optional[str])

slots.Mims_feat_pred = Slot(uri=MIXS.feat_pred, name="Mims_feat_pred", curie=MIXS.curie('feat_pred'),
                   model_uri=MIXS.Mims_feat_pred, domain=Mims, range=Optional[str])

slots.Mims_geo_loc_name = Slot(uri=MIXS.geo_loc_name, name="Mims_geo_loc_name", curie=MIXS.curie('geo_loc_name'),
                   model_uri=MIXS.Mims_geo_loc_name, domain=Mims, range=str)

slots.Mims_lat_lon = Slot(uri=MIXS.lat_lon, name="Mims_lat_lon", curie=MIXS.curie('lat_lon'),
                   model_uri=MIXS.Mims_lat_lon, domain=Mims, range=str)

slots.Mims_lib_layout = Slot(uri=MIXS.lib_layout, name="Mims_lib_layout", curie=MIXS.curie('lib_layout'),
                   model_uri=MIXS.Mims_lib_layout, domain=Mims, range=Optional[str])

slots.Mims_lib_reads_seqd = Slot(uri=MIXS.lib_reads_seqd, name="Mims_lib_reads_seqd", curie=MIXS.curie('lib_reads_seqd'),
                   model_uri=MIXS.Mims_lib_reads_seqd, domain=Mims, range=Optional[str])

slots.Mims_lib_screen = Slot(uri=MIXS.lib_screen, name="Mims_lib_screen", curie=MIXS.curie('lib_screen'),
                   model_uri=MIXS.Mims_lib_screen, domain=Mims, range=Optional[str])

slots.Mims_lib_size = Slot(uri=MIXS.lib_size, name="Mims_lib_size", curie=MIXS.curie('lib_size'),
                   model_uri=MIXS.Mims_lib_size, domain=Mims, range=Optional[str])

slots.Mims_lib_vector = Slot(uri=MIXS.lib_vector, name="Mims_lib_vector", curie=MIXS.curie('lib_vector'),
                   model_uri=MIXS.Mims_lib_vector, domain=Mims, range=Optional[str])

slots.Mims_mid = Slot(uri=MIXS.mid, name="Mims_mid", curie=MIXS.curie('mid'),
                   model_uri=MIXS.Mims_mid, domain=Mims, range=Optional[str])

slots.Mims_neg_cont_type = Slot(uri=MIXS.neg_cont_type, name="Mims_neg_cont_type", curie=MIXS.curie('neg_cont_type'),
                   model_uri=MIXS.Mims_neg_cont_type, domain=Mims, range=Optional[str])

slots.Mims_nucl_acid_amp = Slot(uri=MIXS.nucl_acid_amp, name="Mims_nucl_acid_amp", curie=MIXS.curie('nucl_acid_amp'),
                   model_uri=MIXS.Mims_nucl_acid_amp, domain=Mims, range=Optional[str])

slots.Mims_nucl_acid_ext = Slot(uri=MIXS.nucl_acid_ext, name="Mims_nucl_acid_ext", curie=MIXS.curie('nucl_acid_ext'),
                   model_uri=MIXS.Mims_nucl_acid_ext, domain=Mims, range=Optional[str])

slots.Mims_number_contig = Slot(uri=MIXS.number_contig, name="Mims_number_contig", curie=MIXS.curie('number_contig'),
                   model_uri=MIXS.Mims_number_contig, domain=Mims, range=Optional[str])

slots.Mims_pos_cont_type = Slot(uri=MIXS.pos_cont_type, name="Mims_pos_cont_type", curie=MIXS.curie('pos_cont_type'),
                   model_uri=MIXS.Mims_pos_cont_type, domain=Mims, range=Optional[str])

slots.Mims_project_name = Slot(uri=MIXS.project_name, name="Mims_project_name", curie=MIXS.curie('project_name'),
                   model_uri=MIXS.Mims_project_name, domain=Mims, range=str)

slots.Mims_ref_biomaterial = Slot(uri=MIXS.ref_biomaterial, name="Mims_ref_biomaterial", curie=MIXS.curie('ref_biomaterial'),
                   model_uri=MIXS.Mims_ref_biomaterial, domain=Mims, range=Optional[str])

slots.Mims_ref_db = Slot(uri=MIXS.ref_db, name="Mims_ref_db", curie=MIXS.curie('ref_db'),
                   model_uri=MIXS.Mims_ref_db, domain=Mims, range=Optional[str])

slots.Mims_rel_to_oxygen = Slot(uri=MIXS.rel_to_oxygen, name="Mims_rel_to_oxygen", curie=MIXS.curie('rel_to_oxygen'),
                   model_uri=MIXS.Mims_rel_to_oxygen, domain=Mims, range=Optional[str])

slots.Mims_samp_collec_device = Slot(uri=MIXS.samp_collec_device, name="Mims_samp_collec_device", curie=MIXS.curie('samp_collec_device'),
                   model_uri=MIXS.Mims_samp_collec_device, domain=Mims, range=Optional[str])

slots.Mims_samp_collec_method = Slot(uri=MIXS.samp_collec_method, name="Mims_samp_collec_method", curie=MIXS.curie('samp_collec_method'),
                   model_uri=MIXS.Mims_samp_collec_method, domain=Mims, range=Optional[str])

slots.Mims_samp_mat_process = Slot(uri=MIXS.samp_mat_process, name="Mims_samp_mat_process", curie=MIXS.curie('samp_mat_process'),
                   model_uri=MIXS.Mims_samp_mat_process, domain=Mims, range=Optional[str])

slots.Mims_samp_name = Slot(uri=MIXS.samp_name, name="Mims_samp_name", curie=MIXS.curie('samp_name'),
                   model_uri=MIXS.Mims_samp_name, domain=Mims, range=str)

slots.Mims_samp_size = Slot(uri=MIXS.samp_size, name="Mims_samp_size", curie=MIXS.curie('samp_size'),
                   model_uri=MIXS.Mims_samp_size, domain=Mims, range=Optional[str])

slots.Mims_samp_taxon_id = Slot(uri=MIXS.samp_taxon_id, name="Mims_samp_taxon_id", curie=MIXS.curie('samp_taxon_id'),
                   model_uri=MIXS.Mims_samp_taxon_id, domain=Mims, range=str)

slots.Mims_samp_vol_we_dna_ext = Slot(uri=MIXS.samp_vol_we_dna_ext, name="Mims_samp_vol_we_dna_ext", curie=MIXS.curie('samp_vol_we_dna_ext'),
                   model_uri=MIXS.Mims_samp_vol_we_dna_ext, domain=Mims, range=Optional[str])

slots.Mims_seq_meth = Slot(uri=MIXS.seq_meth, name="Mims_seq_meth", curie=MIXS.curie('seq_meth'),
                   model_uri=MIXS.Mims_seq_meth, domain=Mims, range=str)

slots.Mims_sim_search_meth = Slot(uri=MIXS.sim_search_meth, name="Mims_sim_search_meth", curie=MIXS.curie('sim_search_meth'),
                   model_uri=MIXS.Mims_sim_search_meth, domain=Mims, range=Optional[str])

slots.Mims_size_frac = Slot(uri=MIXS.size_frac, name="Mims_size_frac", curie=MIXS.curie('size_frac'),
                   model_uri=MIXS.Mims_size_frac, domain=Mims, range=Optional[str])

slots.Mims_sop = Slot(uri=MIXS.sop, name="Mims_sop", curie=MIXS.curie('sop'),
                   model_uri=MIXS.Mims_sop, domain=Mims, range=Optional[str])

slots.Mims_source_mat_id = Slot(uri=MIXS.source_mat_id, name="Mims_source_mat_id", curie=MIXS.curie('source_mat_id'),
                   model_uri=MIXS.Mims_source_mat_id, domain=Mims, range=Optional[str])

slots.Mims_tax_class = Slot(uri=MIXS.tax_class, name="Mims_tax_class", curie=MIXS.curie('tax_class'),
                   model_uri=MIXS.Mims_tax_class, domain=Mims, range=Optional[str])

slots.Mims_temp = Slot(uri=MIXS.temp, name="Mims_temp", curie=MIXS.curie('temp'),
                   model_uri=MIXS.Mims_temp, domain=Mims, range=Optional[str])