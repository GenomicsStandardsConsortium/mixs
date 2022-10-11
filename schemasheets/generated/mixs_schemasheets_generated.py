# Auto generated from mixs_schemasheets_generated.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-10-11T19:54:58
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



class ChecklistClass(YAMLRoot):
    """
    A class with slots assigned for the required, recommended, and optional metadata fields for a specific type
    sequence, such as genomes, metagenomes, or marker genes. The migs class, which models genomic sequences, is
    subdivided into checklists for specific taxa: eukaryotes, bacteria, viruses, and plants.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.ChecklistClass
    class_class_curie: ClassVar[str] = "MIXS:ChecklistClass"
    class_name: ClassVar[str] = "ChecklistClass"
    class_model_uri: ClassVar[URIRef] = MIXS.ChecklistClass


@dataclass
class MigsBa(ChecklistClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS["0010003"]
    class_class_curie: ClassVar[str] = "MIXS:0010003"
    class_name: ClassVar[str] = "MigsBa"
    class_model_uri: ClassVar[URIRef] = MIXS.MigsBa

    assembly_qual: str = None
    assembly_software: str = None
    collection_date: str = None
    env_broad_scale: str = None
    env_local_scale: str = None
    env_medium: str = None
    geo_loc_name: str = None
    isol_growth_condt: str = None
    lat_lon: str = None
    num_replicons: str = None
    number_contig: str = None
    project_name: str = None
    ref_biomaterial: str = None
    samp_name: str = None
    samp_taxon_id: str = None
    seq_meth: str = None
    adapters: Optional[str] = None
    alt: Optional[str] = None
    annot: Optional[str] = None
    assembly_name: Optional[str] = None
    associated_resource: Optional[Union[str, List[str]]] = empty_list()
    biotic_relationship: Optional[str] = None
    compl_score: Optional[str] = None
    compl_software: Optional[str] = None
    depth: Optional[str] = None
    elev: Optional[str] = None
    encoded_traits: Optional[str] = None
    estimated_size: Optional[str] = None
    experimental_factor: Optional[str] = None
    extrachrom_elements: Optional[str] = None
    feat_pred: Optional[str] = None
    host_disease_stat: Optional[Union[str, List[str]]] = empty_list()
    host_spec_range: Optional[Union[str, List[str]]] = empty_list()
    lib_layout: Optional[str] = None
    lib_reads_seqd: Optional[str] = None
    lib_screen: Optional[str] = None
    lib_size: Optional[str] = None
    lib_vector: Optional[str] = None
    neg_cont_type: Optional[str] = None
    nucl_acid_amp: Optional[str] = None
    nucl_acid_ext: Optional[str] = None
    pathogenicity: Optional[str] = None
    pos_cont_type: Optional[str] = None
    ref_db: Optional[str] = None
    rel_to_oxygen: Optional[str] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_mat_process: Optional[str] = None
    samp_size: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    sim_search_meth: Optional[str] = None
    sop: Optional[Union[str, List[str]]] = empty_list()
    source_mat_id: Optional[Union[str, List[str]]] = empty_list()
    specific_host: Optional[str] = None
    subspecf_gen_lin: Optional[str] = None
    tax_class: Optional[str] = None
    tax_ident: Optional[str] = None
    temp: Optional[str] = None
    trophic_level: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.assembly_qual):
            self.MissingRequiredField("assembly_qual")
        if not isinstance(self.assembly_qual, str):
            self.assembly_qual = str(self.assembly_qual)

        if self._is_empty(self.assembly_software):
            self.MissingRequiredField("assembly_software")
        if not isinstance(self.assembly_software, str):
            self.assembly_software = str(self.assembly_software)

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

        if self._is_empty(self.isol_growth_condt):
            self.MissingRequiredField("isol_growth_condt")
        if not isinstance(self.isol_growth_condt, str):
            self.isol_growth_condt = str(self.isol_growth_condt)

        if self._is_empty(self.lat_lon):
            self.MissingRequiredField("lat_lon")
        if not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if self._is_empty(self.num_replicons):
            self.MissingRequiredField("num_replicons")
        if not isinstance(self.num_replicons, str):
            self.num_replicons = str(self.num_replicons)

        if self._is_empty(self.number_contig):
            self.MissingRequiredField("number_contig")
        if not isinstance(self.number_contig, str):
            self.number_contig = str(self.number_contig)

        if self._is_empty(self.project_name):
            self.MissingRequiredField("project_name")
        if not isinstance(self.project_name, str):
            self.project_name = str(self.project_name)

        if self._is_empty(self.ref_biomaterial):
            self.MissingRequiredField("ref_biomaterial")
        if not isinstance(self.ref_biomaterial, str):
            self.ref_biomaterial = str(self.ref_biomaterial)

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

        if not isinstance(self.associated_resource, list):
            self.associated_resource = [self.associated_resource] if self.associated_resource is not None else []
        self.associated_resource = [v if isinstance(v, str) else str(v) for v in self.associated_resource]

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, str):
            self.biotic_relationship = str(self.biotic_relationship)

        if self.compl_score is not None and not isinstance(self.compl_score, str):
            self.compl_score = str(self.compl_score)

        if self.compl_software is not None and not isinstance(self.compl_software, str):
            self.compl_software = str(self.compl_software)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.encoded_traits is not None and not isinstance(self.encoded_traits, str):
            self.encoded_traits = str(self.encoded_traits)

        if self.estimated_size is not None and not isinstance(self.estimated_size, str):
            self.estimated_size = str(self.estimated_size)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.extrachrom_elements is not None and not isinstance(self.extrachrom_elements, str):
            self.extrachrom_elements = str(self.extrachrom_elements)

        if self.feat_pred is not None and not isinstance(self.feat_pred, str):
            self.feat_pred = str(self.feat_pred)

        if not isinstance(self.host_disease_stat, list):
            self.host_disease_stat = [self.host_disease_stat] if self.host_disease_stat is not None else []
        self.host_disease_stat = [v if isinstance(v, str) else str(v) for v in self.host_disease_stat]

        if not isinstance(self.host_spec_range, list):
            self.host_spec_range = [self.host_spec_range] if self.host_spec_range is not None else []
        self.host_spec_range = [v if isinstance(v, str) else str(v) for v in self.host_spec_range]

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

        if self.neg_cont_type is not None and not isinstance(self.neg_cont_type, str):
            self.neg_cont_type = str(self.neg_cont_type)

        if self.nucl_acid_amp is not None and not isinstance(self.nucl_acid_amp, str):
            self.nucl_acid_amp = str(self.nucl_acid_amp)

        if self.nucl_acid_ext is not None and not isinstance(self.nucl_acid_ext, str):
            self.nucl_acid_ext = str(self.nucl_acid_ext)

        if self.pathogenicity is not None and not isinstance(self.pathogenicity, str):
            self.pathogenicity = str(self.pathogenicity)

        if self.pos_cont_type is not None and not isinstance(self.pos_cont_type, str):
            self.pos_cont_type = str(self.pos_cont_type)

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

        if not isinstance(self.sop, list):
            self.sop = [self.sop] if self.sop is not None else []
        self.sop = [v if isinstance(v, str) else str(v) for v in self.sop]

        if not isinstance(self.source_mat_id, list):
            self.source_mat_id = [self.source_mat_id] if self.source_mat_id is not None else []
        self.source_mat_id = [v if isinstance(v, str) else str(v) for v in self.source_mat_id]

        if self.specific_host is not None and not isinstance(self.specific_host, str):
            self.specific_host = str(self.specific_host)

        if self.subspecf_gen_lin is not None and not isinstance(self.subspecf_gen_lin, str):
            self.subspecf_gen_lin = str(self.subspecf_gen_lin)

        if self.tax_class is not None and not isinstance(self.tax_class, str):
            self.tax_class = str(self.tax_class)

        if self.tax_ident is not None and not isinstance(self.tax_ident, str):
            self.tax_ident = str(self.tax_ident)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.trophic_level is not None and not isinstance(self.trophic_level, str):
            self.trophic_level = str(self.trophic_level)

        super().__post_init__(**kwargs)


@dataclass
class MigsEu(ChecklistClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS["0010002"]
    class_class_curie: ClassVar[str] = "MIXS:0010002"
    class_name: ClassVar[str] = "MigsEu"
    class_model_uri: ClassVar[URIRef] = MIXS.MigsEu

    assembly_qual: str = None
    assembly_software: str = None
    collection_date: str = None
    env_broad_scale: str = None
    env_local_scale: str = None
    env_medium: str = None
    geo_loc_name: str = None
    isol_growth_condt: str = None
    lat_lon: str = None
    number_contig: str = None
    project_name: str = None
    samp_name: str = None
    samp_taxon_id: str = None
    seq_meth: str = None
    adapters: Optional[str] = None
    alt: Optional[str] = None
    annot: Optional[str] = None
    assembly_name: Optional[str] = None
    associated_resource: Optional[Union[str, List[str]]] = empty_list()
    biotic_relationship: Optional[str] = None
    compl_score: Optional[str] = None
    compl_software: Optional[str] = None
    depth: Optional[str] = None
    elev: Optional[str] = None
    estimated_size: Optional[str] = None
    experimental_factor: Optional[str] = None
    extrachrom_elements: Optional[str] = None
    feat_pred: Optional[str] = None
    host_disease_stat: Optional[Union[str, List[str]]] = empty_list()
    host_spec_range: Optional[Union[str, List[str]]] = empty_list()
    lib_layout: Optional[str] = None
    lib_reads_seqd: Optional[str] = None
    lib_screen: Optional[str] = None
    lib_size: Optional[str] = None
    lib_vector: Optional[str] = None
    neg_cont_type: Optional[str] = None
    nucl_acid_amp: Optional[str] = None
    nucl_acid_ext: Optional[str] = None
    num_replicons: Optional[str] = None
    pathogenicity: Optional[str] = None
    ploidy: Optional[str] = None
    pos_cont_type: Optional[str] = None
    propagation: Optional[str] = None
    ref_biomaterial: Optional[str] = None
    ref_db: Optional[str] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_mat_process: Optional[str] = None
    samp_size: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    sim_search_meth: Optional[str] = None
    sop: Optional[Union[str, List[str]]] = empty_list()
    source_mat_id: Optional[Union[str, List[str]]] = empty_list()
    specific_host: Optional[str] = None
    subspecf_gen_lin: Optional[str] = None
    tax_class: Optional[str] = None
    tax_ident: Optional[str] = None
    temp: Optional[str] = None
    trophic_level: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.assembly_qual):
            self.MissingRequiredField("assembly_qual")
        if not isinstance(self.assembly_qual, str):
            self.assembly_qual = str(self.assembly_qual)

        if self._is_empty(self.assembly_software):
            self.MissingRequiredField("assembly_software")
        if not isinstance(self.assembly_software, str):
            self.assembly_software = str(self.assembly_software)

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

        if self._is_empty(self.isol_growth_condt):
            self.MissingRequiredField("isol_growth_condt")
        if not isinstance(self.isol_growth_condt, str):
            self.isol_growth_condt = str(self.isol_growth_condt)

        if self._is_empty(self.lat_lon):
            self.MissingRequiredField("lat_lon")
        if not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if self._is_empty(self.number_contig):
            self.MissingRequiredField("number_contig")
        if not isinstance(self.number_contig, str):
            self.number_contig = str(self.number_contig)

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

        if not isinstance(self.associated_resource, list):
            self.associated_resource = [self.associated_resource] if self.associated_resource is not None else []
        self.associated_resource = [v if isinstance(v, str) else str(v) for v in self.associated_resource]

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, str):
            self.biotic_relationship = str(self.biotic_relationship)

        if self.compl_score is not None and not isinstance(self.compl_score, str):
            self.compl_score = str(self.compl_score)

        if self.compl_software is not None and not isinstance(self.compl_software, str):
            self.compl_software = str(self.compl_software)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.estimated_size is not None and not isinstance(self.estimated_size, str):
            self.estimated_size = str(self.estimated_size)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.extrachrom_elements is not None and not isinstance(self.extrachrom_elements, str):
            self.extrachrom_elements = str(self.extrachrom_elements)

        if self.feat_pred is not None and not isinstance(self.feat_pred, str):
            self.feat_pred = str(self.feat_pred)

        if not isinstance(self.host_disease_stat, list):
            self.host_disease_stat = [self.host_disease_stat] if self.host_disease_stat is not None else []
        self.host_disease_stat = [v if isinstance(v, str) else str(v) for v in self.host_disease_stat]

        if not isinstance(self.host_spec_range, list):
            self.host_spec_range = [self.host_spec_range] if self.host_spec_range is not None else []
        self.host_spec_range = [v if isinstance(v, str) else str(v) for v in self.host_spec_range]

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

        if self.neg_cont_type is not None and not isinstance(self.neg_cont_type, str):
            self.neg_cont_type = str(self.neg_cont_type)

        if self.nucl_acid_amp is not None and not isinstance(self.nucl_acid_amp, str):
            self.nucl_acid_amp = str(self.nucl_acid_amp)

        if self.nucl_acid_ext is not None and not isinstance(self.nucl_acid_ext, str):
            self.nucl_acid_ext = str(self.nucl_acid_ext)

        if self.num_replicons is not None and not isinstance(self.num_replicons, str):
            self.num_replicons = str(self.num_replicons)

        if self.pathogenicity is not None and not isinstance(self.pathogenicity, str):
            self.pathogenicity = str(self.pathogenicity)

        if self.ploidy is not None and not isinstance(self.ploidy, str):
            self.ploidy = str(self.ploidy)

        if self.pos_cont_type is not None and not isinstance(self.pos_cont_type, str):
            self.pos_cont_type = str(self.pos_cont_type)

        if self.propagation is not None and not isinstance(self.propagation, str):
            self.propagation = str(self.propagation)

        if self.ref_biomaterial is not None and not isinstance(self.ref_biomaterial, str):
            self.ref_biomaterial = str(self.ref_biomaterial)

        if self.ref_db is not None and not isinstance(self.ref_db, str):
            self.ref_db = str(self.ref_db)

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

        if not isinstance(self.sop, list):
            self.sop = [self.sop] if self.sop is not None else []
        self.sop = [v if isinstance(v, str) else str(v) for v in self.sop]

        if not isinstance(self.source_mat_id, list):
            self.source_mat_id = [self.source_mat_id] if self.source_mat_id is not None else []
        self.source_mat_id = [v if isinstance(v, str) else str(v) for v in self.source_mat_id]

        if self.specific_host is not None and not isinstance(self.specific_host, str):
            self.specific_host = str(self.specific_host)

        if self.subspecf_gen_lin is not None and not isinstance(self.subspecf_gen_lin, str):
            self.subspecf_gen_lin = str(self.subspecf_gen_lin)

        if self.tax_class is not None and not isinstance(self.tax_class, str):
            self.tax_class = str(self.tax_class)

        if self.tax_ident is not None and not isinstance(self.tax_ident, str):
            self.tax_ident = str(self.tax_ident)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.trophic_level is not None and not isinstance(self.trophic_level, str):
            self.trophic_level = str(self.trophic_level)

        super().__post_init__(**kwargs)


@dataclass
class MigsOrg(ChecklistClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS["0010006"]
    class_class_curie: ClassVar[str] = "MIXS:0010006"
    class_name: ClassVar[str] = "MigsOrg"
    class_model_uri: ClassVar[URIRef] = MIXS.MigsOrg

    assembly_software: str = None
    collection_date: str = None
    env_broad_scale: str = None
    env_local_scale: str = None
    env_medium: str = None
    geo_loc_name: str = None
    isol_growth_condt: str = None
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
    associated_resource: Optional[Union[str, List[str]]] = empty_list()
    compl_score: Optional[str] = None
    compl_software: Optional[str] = None
    depth: Optional[str] = None
    elev: Optional[str] = None
    estimated_size: Optional[str] = None
    experimental_factor: Optional[str] = None
    extrachrom_elements: Optional[str] = None
    feat_pred: Optional[str] = None
    lib_layout: Optional[str] = None
    lib_reads_seqd: Optional[str] = None
    lib_screen: Optional[str] = None
    lib_size: Optional[str] = None
    lib_vector: Optional[str] = None
    neg_cont_type: Optional[str] = None
    nucl_acid_amp: Optional[str] = None
    nucl_acid_ext: Optional[str] = None
    number_contig: Optional[str] = None
    pos_cont_type: Optional[str] = None
    ref_biomaterial: Optional[str] = None
    ref_db: Optional[str] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_mat_process: Optional[str] = None
    samp_size: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    sim_search_meth: Optional[str] = None
    sop: Optional[Union[str, List[str]]] = empty_list()
    source_mat_id: Optional[Union[str, List[str]]] = empty_list()
    subspecf_gen_lin: Optional[str] = None
    tax_class: Optional[str] = None
    tax_ident: Optional[str] = None
    temp: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.assembly_software):
            self.MissingRequiredField("assembly_software")
        if not isinstance(self.assembly_software, str):
            self.assembly_software = str(self.assembly_software)

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

        if self._is_empty(self.isol_growth_condt):
            self.MissingRequiredField("isol_growth_condt")
        if not isinstance(self.isol_growth_condt, str):
            self.isol_growth_condt = str(self.isol_growth_condt)

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

        if not isinstance(self.associated_resource, list):
            self.associated_resource = [self.associated_resource] if self.associated_resource is not None else []
        self.associated_resource = [v if isinstance(v, str) else str(v) for v in self.associated_resource]

        if self.compl_score is not None and not isinstance(self.compl_score, str):
            self.compl_score = str(self.compl_score)

        if self.compl_software is not None and not isinstance(self.compl_software, str):
            self.compl_software = str(self.compl_software)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.estimated_size is not None and not isinstance(self.estimated_size, str):
            self.estimated_size = str(self.estimated_size)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.extrachrom_elements is not None and not isinstance(self.extrachrom_elements, str):
            self.extrachrom_elements = str(self.extrachrom_elements)

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

        if not isinstance(self.sop, list):
            self.sop = [self.sop] if self.sop is not None else []
        self.sop = [v if isinstance(v, str) else str(v) for v in self.sop]

        if not isinstance(self.source_mat_id, list):
            self.source_mat_id = [self.source_mat_id] if self.source_mat_id is not None else []
        self.source_mat_id = [v if isinstance(v, str) else str(v) for v in self.source_mat_id]

        if self.subspecf_gen_lin is not None and not isinstance(self.subspecf_gen_lin, str):
            self.subspecf_gen_lin = str(self.subspecf_gen_lin)

        if self.tax_class is not None and not isinstance(self.tax_class, str):
            self.tax_class = str(self.tax_class)

        if self.tax_ident is not None and not isinstance(self.tax_ident, str):
            self.tax_ident = str(self.tax_ident)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        super().__post_init__(**kwargs)


@dataclass
class MigsPl(ChecklistClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS["0010004"]
    class_class_curie: ClassVar[str] = "MIXS:0010004"
    class_name: ClassVar[str] = "MigsPl"
    class_model_uri: ClassVar[URIRef] = MIXS.MigsPl

    assembly_software: str = None
    collection_date: str = None
    env_broad_scale: str = None
    env_local_scale: str = None
    env_medium: str = None
    geo_loc_name: str = None
    isol_growth_condt: str = None
    lat_lon: str = None
    project_name: str = None
    propagation: str = None
    samp_name: str = None
    samp_taxon_id: str = None
    seq_meth: str = None
    adapters: Optional[str] = None
    alt: Optional[str] = None
    annot: Optional[str] = None
    assembly_name: Optional[str] = None
    assembly_qual: Optional[str] = None
    associated_resource: Optional[Union[str, List[str]]] = empty_list()
    compl_score: Optional[str] = None
    compl_software: Optional[str] = None
    depth: Optional[str] = None
    elev: Optional[str] = None
    encoded_traits: Optional[str] = None
    estimated_size: Optional[str] = None
    experimental_factor: Optional[str] = None
    feat_pred: Optional[str] = None
    host_spec_range: Optional[Union[str, List[str]]] = empty_list()
    lib_layout: Optional[str] = None
    lib_reads_seqd: Optional[str] = None
    lib_screen: Optional[str] = None
    lib_size: Optional[str] = None
    lib_vector: Optional[str] = None
    neg_cont_type: Optional[str] = None
    nucl_acid_amp: Optional[str] = None
    nucl_acid_ext: Optional[str] = None
    number_contig: Optional[str] = None
    pos_cont_type: Optional[str] = None
    ref_biomaterial: Optional[str] = None
    ref_db: Optional[str] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_mat_process: Optional[str] = None
    samp_size: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    sim_search_meth: Optional[str] = None
    sop: Optional[Union[str, List[str]]] = empty_list()
    source_mat_id: Optional[Union[str, List[str]]] = empty_list()
    specific_host: Optional[str] = None
    subspecf_gen_lin: Optional[str] = None
    tax_class: Optional[str] = None
    tax_ident: Optional[str] = None
    temp: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.assembly_software):
            self.MissingRequiredField("assembly_software")
        if not isinstance(self.assembly_software, str):
            self.assembly_software = str(self.assembly_software)

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

        if self._is_empty(self.isol_growth_condt):
            self.MissingRequiredField("isol_growth_condt")
        if not isinstance(self.isol_growth_condt, str):
            self.isol_growth_condt = str(self.isol_growth_condt)

        if self._is_empty(self.lat_lon):
            self.MissingRequiredField("lat_lon")
        if not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if self._is_empty(self.project_name):
            self.MissingRequiredField("project_name")
        if not isinstance(self.project_name, str):
            self.project_name = str(self.project_name)

        if self._is_empty(self.propagation):
            self.MissingRequiredField("propagation")
        if not isinstance(self.propagation, str):
            self.propagation = str(self.propagation)

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

        if not isinstance(self.associated_resource, list):
            self.associated_resource = [self.associated_resource] if self.associated_resource is not None else []
        self.associated_resource = [v if isinstance(v, str) else str(v) for v in self.associated_resource]

        if self.compl_score is not None and not isinstance(self.compl_score, str):
            self.compl_score = str(self.compl_score)

        if self.compl_software is not None and not isinstance(self.compl_software, str):
            self.compl_software = str(self.compl_software)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.encoded_traits is not None and not isinstance(self.encoded_traits, str):
            self.encoded_traits = str(self.encoded_traits)

        if self.estimated_size is not None and not isinstance(self.estimated_size, str):
            self.estimated_size = str(self.estimated_size)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.feat_pred is not None and not isinstance(self.feat_pred, str):
            self.feat_pred = str(self.feat_pred)

        if not isinstance(self.host_spec_range, list):
            self.host_spec_range = [self.host_spec_range] if self.host_spec_range is not None else []
        self.host_spec_range = [v if isinstance(v, str) else str(v) for v in self.host_spec_range]

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

        if not isinstance(self.sop, list):
            self.sop = [self.sop] if self.sop is not None else []
        self.sop = [v if isinstance(v, str) else str(v) for v in self.sop]

        if not isinstance(self.source_mat_id, list):
            self.source_mat_id = [self.source_mat_id] if self.source_mat_id is not None else []
        self.source_mat_id = [v if isinstance(v, str) else str(v) for v in self.source_mat_id]

        if self.specific_host is not None and not isinstance(self.specific_host, str):
            self.specific_host = str(self.specific_host)

        if self.subspecf_gen_lin is not None and not isinstance(self.subspecf_gen_lin, str):
            self.subspecf_gen_lin = str(self.subspecf_gen_lin)

        if self.tax_class is not None and not isinstance(self.tax_class, str):
            self.tax_class = str(self.tax_class)

        if self.tax_ident is not None and not isinstance(self.tax_ident, str):
            self.tax_ident = str(self.tax_ident)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        super().__post_init__(**kwargs)


@dataclass
class MigsVi(ChecklistClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS["0010005"]
    class_class_curie: ClassVar[str] = "MIXS:0010005"
    class_name: ClassVar[str] = "MigsVi"
    class_model_uri: ClassVar[URIRef] = MIXS.MigsVi

    assembly_software: str = None
    collection_date: str = None
    env_broad_scale: str = None
    env_local_scale: str = None
    env_medium: str = None
    geo_loc_name: str = None
    isol_growth_condt: str = None
    lat_lon: str = None
    project_name: str = None
    propagation: str = None
    samp_name: str = None
    samp_taxon_id: str = None
    seq_meth: str = None
    adapters: Optional[str] = None
    alt: Optional[str] = None
    annot: Optional[str] = None
    assembly_name: Optional[str] = None
    assembly_qual: Optional[str] = None
    associated_resource: Optional[Union[str, List[str]]] = empty_list()
    biotic_relationship: Optional[str] = None
    compl_score: Optional[str] = None
    compl_software: Optional[str] = None
    depth: Optional[str] = None
    elev: Optional[str] = None
    encoded_traits: Optional[str] = None
    estimated_size: Optional[str] = None
    experimental_factor: Optional[str] = None
    feat_pred: Optional[str] = None
    host_disease_stat: Optional[Union[str, List[str]]] = empty_list()
    host_spec_range: Optional[Union[str, List[str]]] = empty_list()
    lib_layout: Optional[str] = None
    lib_reads_seqd: Optional[str] = None
    lib_screen: Optional[str] = None
    lib_size: Optional[str] = None
    lib_vector: Optional[str] = None
    neg_cont_type: Optional[str] = None
    nucl_acid_amp: Optional[str] = None
    nucl_acid_ext: Optional[str] = None
    num_replicons: Optional[str] = None
    number_contig: Optional[str] = None
    pathogenicity: Optional[str] = None
    pos_cont_type: Optional[str] = None
    ref_biomaterial: Optional[str] = None
    ref_db: Optional[str] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_mat_process: Optional[str] = None
    samp_size: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    sim_search_meth: Optional[str] = None
    sop: Optional[Union[str, List[str]]] = empty_list()
    source_mat_id: Optional[Union[str, List[str]]] = empty_list()
    specific_host: Optional[str] = None
    subspecf_gen_lin: Optional[str] = None
    tax_class: Optional[str] = None
    tax_ident: Optional[str] = None
    temp: Optional[str] = None
    virus_enrich_appr: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.assembly_software):
            self.MissingRequiredField("assembly_software")
        if not isinstance(self.assembly_software, str):
            self.assembly_software = str(self.assembly_software)

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

        if self._is_empty(self.isol_growth_condt):
            self.MissingRequiredField("isol_growth_condt")
        if not isinstance(self.isol_growth_condt, str):
            self.isol_growth_condt = str(self.isol_growth_condt)

        if self._is_empty(self.lat_lon):
            self.MissingRequiredField("lat_lon")
        if not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if self._is_empty(self.project_name):
            self.MissingRequiredField("project_name")
        if not isinstance(self.project_name, str):
            self.project_name = str(self.project_name)

        if self._is_empty(self.propagation):
            self.MissingRequiredField("propagation")
        if not isinstance(self.propagation, str):
            self.propagation = str(self.propagation)

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

        if not isinstance(self.associated_resource, list):
            self.associated_resource = [self.associated_resource] if self.associated_resource is not None else []
        self.associated_resource = [v if isinstance(v, str) else str(v) for v in self.associated_resource]

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, str):
            self.biotic_relationship = str(self.biotic_relationship)

        if self.compl_score is not None and not isinstance(self.compl_score, str):
            self.compl_score = str(self.compl_score)

        if self.compl_software is not None and not isinstance(self.compl_software, str):
            self.compl_software = str(self.compl_software)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.encoded_traits is not None and not isinstance(self.encoded_traits, str):
            self.encoded_traits = str(self.encoded_traits)

        if self.estimated_size is not None and not isinstance(self.estimated_size, str):
            self.estimated_size = str(self.estimated_size)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.feat_pred is not None and not isinstance(self.feat_pred, str):
            self.feat_pred = str(self.feat_pred)

        if not isinstance(self.host_disease_stat, list):
            self.host_disease_stat = [self.host_disease_stat] if self.host_disease_stat is not None else []
        self.host_disease_stat = [v if isinstance(v, str) else str(v) for v in self.host_disease_stat]

        if not isinstance(self.host_spec_range, list):
            self.host_spec_range = [self.host_spec_range] if self.host_spec_range is not None else []
        self.host_spec_range = [v if isinstance(v, str) else str(v) for v in self.host_spec_range]

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

        if self.neg_cont_type is not None and not isinstance(self.neg_cont_type, str):
            self.neg_cont_type = str(self.neg_cont_type)

        if self.nucl_acid_amp is not None and not isinstance(self.nucl_acid_amp, str):
            self.nucl_acid_amp = str(self.nucl_acid_amp)

        if self.nucl_acid_ext is not None and not isinstance(self.nucl_acid_ext, str):
            self.nucl_acid_ext = str(self.nucl_acid_ext)

        if self.num_replicons is not None and not isinstance(self.num_replicons, str):
            self.num_replicons = str(self.num_replicons)

        if self.number_contig is not None and not isinstance(self.number_contig, str):
            self.number_contig = str(self.number_contig)

        if self.pathogenicity is not None and not isinstance(self.pathogenicity, str):
            self.pathogenicity = str(self.pathogenicity)

        if self.pos_cont_type is not None and not isinstance(self.pos_cont_type, str):
            self.pos_cont_type = str(self.pos_cont_type)

        if self.ref_biomaterial is not None and not isinstance(self.ref_biomaterial, str):
            self.ref_biomaterial = str(self.ref_biomaterial)

        if self.ref_db is not None and not isinstance(self.ref_db, str):
            self.ref_db = str(self.ref_db)

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

        if not isinstance(self.sop, list):
            self.sop = [self.sop] if self.sop is not None else []
        self.sop = [v if isinstance(v, str) else str(v) for v in self.sop]

        if not isinstance(self.source_mat_id, list):
            self.source_mat_id = [self.source_mat_id] if self.source_mat_id is not None else []
        self.source_mat_id = [v if isinstance(v, str) else str(v) for v in self.source_mat_id]

        if self.specific_host is not None and not isinstance(self.specific_host, str):
            self.specific_host = str(self.specific_host)

        if self.subspecf_gen_lin is not None and not isinstance(self.subspecf_gen_lin, str):
            self.subspecf_gen_lin = str(self.subspecf_gen_lin)

        if self.tax_class is not None and not isinstance(self.tax_class, str):
            self.tax_class = str(self.tax_class)

        if self.tax_ident is not None and not isinstance(self.tax_ident, str):
            self.tax_ident = str(self.tax_ident)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.virus_enrich_appr is not None and not isinstance(self.virus_enrich_appr, str):
            self.virus_enrich_appr = str(self.virus_enrich_appr)

        super().__post_init__(**kwargs)


@dataclass
class Mimag(ChecklistClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS["0010011"]
    class_class_curie: ClassVar[str] = "MIXS:0010011"
    class_name: ClassVar[str] = "Mimag"
    class_model_uri: ClassVar[URIRef] = MIXS.Mimag

    assembly_qual: str = None
    assembly_software: str = None
    bin_param: str = None
    bin_software: str = None
    collection_date: str = None
    compl_score: str = None
    compl_software: str = None
    contam_score: str = None
    env_broad_scale: str = None
    env_local_scale: str = None
    env_medium: str = None
    geo_loc_name: str = None
    lat_lon: str = None
    project_name: str = None
    samp_name: str = None
    samp_taxon_id: str = None
    seq_meth: str = None
    tax_ident: str = None
    x_16s_recover: Optional[str] = None
    x_16s_recover_software: Optional[str] = None
    adapters: Optional[str] = None
    alt: Optional[str] = None
    annot: Optional[str] = None
    assembly_name: Optional[str] = None
    associated_resource: Optional[Union[str, List[str]]] = empty_list()
    compl_appr: Optional[str] = None
    contam_screen_input: Optional[str] = None
    contam_screen_param: Optional[str] = None
    decontam_software: Optional[str] = None
    depth: Optional[str] = None
    elev: Optional[str] = None
    experimental_factor: Optional[str] = None
    feat_pred: Optional[str] = None
    lib_layout: Optional[str] = None
    lib_reads_seqd: Optional[str] = None
    lib_screen: Optional[str] = None
    lib_size: Optional[str] = None
    lib_vector: Optional[str] = None
    mag_cov_software: Optional[str] = None
    mid: Optional[str] = None
    neg_cont_type: Optional[str] = None
    nucl_acid_amp: Optional[str] = None
    nucl_acid_ext: Optional[str] = None
    number_contig: Optional[str] = None
    pos_cont_type: Optional[str] = None
    reassembly_bin: Optional[str] = None
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
    sop: Optional[Union[str, List[str]]] = empty_list()
    source_mat_id: Optional[Union[str, List[str]]] = empty_list()
    tax_class: Optional[str] = None
    temp: Optional[str] = None
    trna_ext_software: Optional[str] = None
    trnas: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.assembly_qual):
            self.MissingRequiredField("assembly_qual")
        if not isinstance(self.assembly_qual, str):
            self.assembly_qual = str(self.assembly_qual)

        if self._is_empty(self.assembly_software):
            self.MissingRequiredField("assembly_software")
        if not isinstance(self.assembly_software, str):
            self.assembly_software = str(self.assembly_software)

        if self._is_empty(self.bin_param):
            self.MissingRequiredField("bin_param")
        if not isinstance(self.bin_param, str):
            self.bin_param = str(self.bin_param)

        if self._is_empty(self.bin_software):
            self.MissingRequiredField("bin_software")
        if not isinstance(self.bin_software, str):
            self.bin_software = str(self.bin_software)

        if self._is_empty(self.collection_date):
            self.MissingRequiredField("collection_date")
        if not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self._is_empty(self.compl_score):
            self.MissingRequiredField("compl_score")
        if not isinstance(self.compl_score, str):
            self.compl_score = str(self.compl_score)

        if self._is_empty(self.compl_software):
            self.MissingRequiredField("compl_software")
        if not isinstance(self.compl_software, str):
            self.compl_software = str(self.compl_software)

        if self._is_empty(self.contam_score):
            self.MissingRequiredField("contam_score")
        if not isinstance(self.contam_score, str):
            self.contam_score = str(self.contam_score)

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

        if self._is_empty(self.tax_ident):
            self.MissingRequiredField("tax_ident")
        if not isinstance(self.tax_ident, str):
            self.tax_ident = str(self.tax_ident)

        if self.x_16s_recover is not None and not isinstance(self.x_16s_recover, str):
            self.x_16s_recover = str(self.x_16s_recover)

        if self.x_16s_recover_software is not None and not isinstance(self.x_16s_recover_software, str):
            self.x_16s_recover_software = str(self.x_16s_recover_software)

        if self.adapters is not None and not isinstance(self.adapters, str):
            self.adapters = str(self.adapters)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.annot is not None and not isinstance(self.annot, str):
            self.annot = str(self.annot)

        if self.assembly_name is not None and not isinstance(self.assembly_name, str):
            self.assembly_name = str(self.assembly_name)

        if not isinstance(self.associated_resource, list):
            self.associated_resource = [self.associated_resource] if self.associated_resource is not None else []
        self.associated_resource = [v if isinstance(v, str) else str(v) for v in self.associated_resource]

        if self.compl_appr is not None and not isinstance(self.compl_appr, str):
            self.compl_appr = str(self.compl_appr)

        if self.contam_screen_input is not None and not isinstance(self.contam_screen_input, str):
            self.contam_screen_input = str(self.contam_screen_input)

        if self.contam_screen_param is not None and not isinstance(self.contam_screen_param, str):
            self.contam_screen_param = str(self.contam_screen_param)

        if self.decontam_software is not None and not isinstance(self.decontam_software, str):
            self.decontam_software = str(self.decontam_software)

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

        if self.mag_cov_software is not None and not isinstance(self.mag_cov_software, str):
            self.mag_cov_software = str(self.mag_cov_software)

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

        if self.reassembly_bin is not None and not isinstance(self.reassembly_bin, str):
            self.reassembly_bin = str(self.reassembly_bin)

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

        if not isinstance(self.sop, list):
            self.sop = [self.sop] if self.sop is not None else []
        self.sop = [v if isinstance(v, str) else str(v) for v in self.sop]

        if not isinstance(self.source_mat_id, list):
            self.source_mat_id = [self.source_mat_id] if self.source_mat_id is not None else []
        self.source_mat_id = [v if isinstance(v, str) else str(v) for v in self.source_mat_id]

        if self.tax_class is not None and not isinstance(self.tax_class, str):
            self.tax_class = str(self.tax_class)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.trna_ext_software is not None and not isinstance(self.trna_ext_software, str):
            self.trna_ext_software = str(self.trna_ext_software)

        if self.trnas is not None and not isinstance(self.trnas, str):
            self.trnas = str(self.trnas)

        super().__post_init__(**kwargs)


@dataclass
class MimarksC(ChecklistClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS["0010009"]
    class_class_curie: ClassVar[str] = "MIXS:0010009"
    class_name: ClassVar[str] = "MimarksC"
    class_model_uri: ClassVar[URIRef] = MIXS.MimarksC

    collection_date: str = None
    env_broad_scale: str = None
    env_local_scale: str = None
    env_medium: str = None
    geo_loc_name: str = None
    isol_growth_condt: str = None
    lat_lon: str = None
    project_name: str = None
    samp_name: str = None
    samp_taxon_id: str = None
    seq_meth: str = None
    target_gene: str = None
    alt: Optional[str] = None
    associated_resource: Optional[Union[str, List[str]]] = empty_list()
    biotic_relationship: Optional[str] = None
    chimera_check: Optional[str] = None
    depth: Optional[str] = None
    elev: Optional[str] = None
    experimental_factor: Optional[str] = None
    extrachrom_elements: Optional[str] = None
    neg_cont_type: Optional[str] = None
    nucl_acid_amp: Optional[str] = None
    nucl_acid_ext: Optional[str] = None
    pcr_cond: Optional[str] = None
    pcr_primers: Optional[str] = None
    pos_cont_type: Optional[str] = None
    rel_to_oxygen: Optional[str] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_mat_process: Optional[str] = None
    samp_size: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    seq_quality_check: Optional[str] = None
    sop: Optional[Union[str, List[str]]] = empty_list()
    source_mat_id: Optional[Union[str, List[str]]] = empty_list()
    subspecf_gen_lin: Optional[str] = None
    target_subfragment: Optional[str] = None
    temp: Optional[str] = None
    trophic_level: Optional[str] = None

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

        if self._is_empty(self.isol_growth_condt):
            self.MissingRequiredField("isol_growth_condt")
        if not isinstance(self.isol_growth_condt, str):
            self.isol_growth_condt = str(self.isol_growth_condt)

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

        if self._is_empty(self.target_gene):
            self.MissingRequiredField("target_gene")
        if not isinstance(self.target_gene, str):
            self.target_gene = str(self.target_gene)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if not isinstance(self.associated_resource, list):
            self.associated_resource = [self.associated_resource] if self.associated_resource is not None else []
        self.associated_resource = [v if isinstance(v, str) else str(v) for v in self.associated_resource]

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, str):
            self.biotic_relationship = str(self.biotic_relationship)

        if self.chimera_check is not None and not isinstance(self.chimera_check, str):
            self.chimera_check = str(self.chimera_check)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.extrachrom_elements is not None and not isinstance(self.extrachrom_elements, str):
            self.extrachrom_elements = str(self.extrachrom_elements)

        if self.neg_cont_type is not None and not isinstance(self.neg_cont_type, str):
            self.neg_cont_type = str(self.neg_cont_type)

        if self.nucl_acid_amp is not None and not isinstance(self.nucl_acid_amp, str):
            self.nucl_acid_amp = str(self.nucl_acid_amp)

        if self.nucl_acid_ext is not None and not isinstance(self.nucl_acid_ext, str):
            self.nucl_acid_ext = str(self.nucl_acid_ext)

        if self.pcr_cond is not None and not isinstance(self.pcr_cond, str):
            self.pcr_cond = str(self.pcr_cond)

        if self.pcr_primers is not None and not isinstance(self.pcr_primers, str):
            self.pcr_primers = str(self.pcr_primers)

        if self.pos_cont_type is not None and not isinstance(self.pos_cont_type, str):
            self.pos_cont_type = str(self.pos_cont_type)

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

        if self.seq_quality_check is not None and not isinstance(self.seq_quality_check, str):
            self.seq_quality_check = str(self.seq_quality_check)

        if not isinstance(self.sop, list):
            self.sop = [self.sop] if self.sop is not None else []
        self.sop = [v if isinstance(v, str) else str(v) for v in self.sop]

        if not isinstance(self.source_mat_id, list):
            self.source_mat_id = [self.source_mat_id] if self.source_mat_id is not None else []
        self.source_mat_id = [v if isinstance(v, str) else str(v) for v in self.source_mat_id]

        if self.subspecf_gen_lin is not None and not isinstance(self.subspecf_gen_lin, str):
            self.subspecf_gen_lin = str(self.subspecf_gen_lin)

        if self.target_subfragment is not None and not isinstance(self.target_subfragment, str):
            self.target_subfragment = str(self.target_subfragment)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.trophic_level is not None and not isinstance(self.trophic_level, str):
            self.trophic_level = str(self.trophic_level)

        super().__post_init__(**kwargs)


@dataclass
class MimarksS(ChecklistClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS["0010008"]
    class_class_curie: ClassVar[str] = "MIXS:0010008"
    class_name: ClassVar[str] = "MimarksS"
    class_model_uri: ClassVar[URIRef] = MIXS.MimarksS

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
    target_gene: str = None
    adapters: Optional[str] = None
    alt: Optional[str] = None
    assembly_software: Optional[str] = None
    associated_resource: Optional[Union[str, List[str]]] = empty_list()
    chimera_check: Optional[str] = None
    depth: Optional[str] = None
    elev: Optional[str] = None
    experimental_factor: Optional[str] = None
    lib_layout: Optional[str] = None
    lib_reads_seqd: Optional[str] = None
    lib_screen: Optional[str] = None
    lib_size: Optional[str] = None
    lib_vector: Optional[str] = None
    mid: Optional[str] = None
    neg_cont_type: Optional[str] = None
    nucl_acid_amp: Optional[str] = None
    nucl_acid_ext: Optional[str] = None
    pcr_cond: Optional[str] = None
    pcr_primers: Optional[str] = None
    pos_cont_type: Optional[str] = None
    rel_to_oxygen: Optional[str] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_mat_process: Optional[str] = None
    samp_size: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    seq_quality_check: Optional[str] = None
    size_frac: Optional[str] = None
    sop: Optional[Union[str, List[str]]] = empty_list()
    source_mat_id: Optional[Union[str, List[str]]] = empty_list()
    target_subfragment: Optional[str] = None
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

        if self._is_empty(self.target_gene):
            self.MissingRequiredField("target_gene")
        if not isinstance(self.target_gene, str):
            self.target_gene = str(self.target_gene)

        if self.adapters is not None and not isinstance(self.adapters, str):
            self.adapters = str(self.adapters)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.assembly_software is not None and not isinstance(self.assembly_software, str):
            self.assembly_software = str(self.assembly_software)

        if not isinstance(self.associated_resource, list):
            self.associated_resource = [self.associated_resource] if self.associated_resource is not None else []
        self.associated_resource = [v if isinstance(v, str) else str(v) for v in self.associated_resource]

        if self.chimera_check is not None and not isinstance(self.chimera_check, str):
            self.chimera_check = str(self.chimera_check)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

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

        if self.pcr_cond is not None and not isinstance(self.pcr_cond, str):
            self.pcr_cond = str(self.pcr_cond)

        if self.pcr_primers is not None and not isinstance(self.pcr_primers, str):
            self.pcr_primers = str(self.pcr_primers)

        if self.pos_cont_type is not None and not isinstance(self.pos_cont_type, str):
            self.pos_cont_type = str(self.pos_cont_type)

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

        if self.seq_quality_check is not None and not isinstance(self.seq_quality_check, str):
            self.seq_quality_check = str(self.seq_quality_check)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if not isinstance(self.sop, list):
            self.sop = [self.sop] if self.sop is not None else []
        self.sop = [v if isinstance(v, str) else str(v) for v in self.sop]

        if not isinstance(self.source_mat_id, list):
            self.source_mat_id = [self.source_mat_id] if self.source_mat_id is not None else []
        self.source_mat_id = [v if isinstance(v, str) else str(v) for v in self.source_mat_id]

        if self.target_subfragment is not None and not isinstance(self.target_subfragment, str):
            self.target_subfragment = str(self.target_subfragment)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        super().__post_init__(**kwargs)


@dataclass
class Misag(ChecklistClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS["0010010"]
    class_class_curie: ClassVar[str] = "MIXS:0010010"
    class_name: ClassVar[str] = "Misag"
    class_model_uri: ClassVar[URIRef] = MIXS.Misag

    assembly_qual: str = None
    assembly_software: str = None
    collection_date: str = None
    compl_score: str = None
    compl_software: str = None
    contam_score: str = None
    env_broad_scale: str = None
    env_local_scale: str = None
    env_medium: str = None
    geo_loc_name: str = None
    lat_lon: str = None
    project_name: str = None
    samp_name: str = None
    samp_taxon_id: str = None
    seq_meth: str = None
    single_cell_lysis_appr: str = None
    sort_tech: str = None
    tax_ident: str = None
    wga_amp_appr: str = None
    x_16s_recover: Optional[str] = None
    x_16s_recover_software: Optional[str] = None
    adapters: Optional[str] = None
    alt: Optional[str] = None
    annot: Optional[str] = None
    assembly_name: Optional[str] = None
    associated_resource: Optional[Union[str, List[str]]] = empty_list()
    compl_appr: Optional[str] = None
    contam_screen_input: Optional[str] = None
    contam_screen_param: Optional[str] = None
    decontam_software: Optional[str] = None
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
    single_cell_lysis_prot: Optional[str] = None
    size_frac: Optional[str] = None
    sop: Optional[Union[str, List[str]]] = empty_list()
    source_mat_id: Optional[Union[str, List[str]]] = empty_list()
    tax_class: Optional[str] = None
    temp: Optional[str] = None
    trna_ext_software: Optional[str] = None
    trnas: Optional[str] = None
    wga_amp_kit: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.assembly_qual):
            self.MissingRequiredField("assembly_qual")
        if not isinstance(self.assembly_qual, str):
            self.assembly_qual = str(self.assembly_qual)

        if self._is_empty(self.assembly_software):
            self.MissingRequiredField("assembly_software")
        if not isinstance(self.assembly_software, str):
            self.assembly_software = str(self.assembly_software)

        if self._is_empty(self.collection_date):
            self.MissingRequiredField("collection_date")
        if not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self._is_empty(self.compl_score):
            self.MissingRequiredField("compl_score")
        if not isinstance(self.compl_score, str):
            self.compl_score = str(self.compl_score)

        if self._is_empty(self.compl_software):
            self.MissingRequiredField("compl_software")
        if not isinstance(self.compl_software, str):
            self.compl_software = str(self.compl_software)

        if self._is_empty(self.contam_score):
            self.MissingRequiredField("contam_score")
        if not isinstance(self.contam_score, str):
            self.contam_score = str(self.contam_score)

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

        if self._is_empty(self.single_cell_lysis_appr):
            self.MissingRequiredField("single_cell_lysis_appr")
        if not isinstance(self.single_cell_lysis_appr, str):
            self.single_cell_lysis_appr = str(self.single_cell_lysis_appr)

        if self._is_empty(self.sort_tech):
            self.MissingRequiredField("sort_tech")
        if not isinstance(self.sort_tech, str):
            self.sort_tech = str(self.sort_tech)

        if self._is_empty(self.tax_ident):
            self.MissingRequiredField("tax_ident")
        if not isinstance(self.tax_ident, str):
            self.tax_ident = str(self.tax_ident)

        if self._is_empty(self.wga_amp_appr):
            self.MissingRequiredField("wga_amp_appr")
        if not isinstance(self.wga_amp_appr, str):
            self.wga_amp_appr = str(self.wga_amp_appr)

        if self.x_16s_recover is not None and not isinstance(self.x_16s_recover, str):
            self.x_16s_recover = str(self.x_16s_recover)

        if self.x_16s_recover_software is not None and not isinstance(self.x_16s_recover_software, str):
            self.x_16s_recover_software = str(self.x_16s_recover_software)

        if self.adapters is not None and not isinstance(self.adapters, str):
            self.adapters = str(self.adapters)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.annot is not None and not isinstance(self.annot, str):
            self.annot = str(self.annot)

        if self.assembly_name is not None and not isinstance(self.assembly_name, str):
            self.assembly_name = str(self.assembly_name)

        if not isinstance(self.associated_resource, list):
            self.associated_resource = [self.associated_resource] if self.associated_resource is not None else []
        self.associated_resource = [v if isinstance(v, str) else str(v) for v in self.associated_resource]

        if self.compl_appr is not None and not isinstance(self.compl_appr, str):
            self.compl_appr = str(self.compl_appr)

        if self.contam_screen_input is not None and not isinstance(self.contam_screen_input, str):
            self.contam_screen_input = str(self.contam_screen_input)

        if self.contam_screen_param is not None and not isinstance(self.contam_screen_param, str):
            self.contam_screen_param = str(self.contam_screen_param)

        if self.decontam_software is not None and not isinstance(self.decontam_software, str):
            self.decontam_software = str(self.decontam_software)

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

        if self.single_cell_lysis_prot is not None and not isinstance(self.single_cell_lysis_prot, str):
            self.single_cell_lysis_prot = str(self.single_cell_lysis_prot)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if not isinstance(self.sop, list):
            self.sop = [self.sop] if self.sop is not None else []
        self.sop = [v if isinstance(v, str) else str(v) for v in self.sop]

        if not isinstance(self.source_mat_id, list):
            self.source_mat_id = [self.source_mat_id] if self.source_mat_id is not None else []
        self.source_mat_id = [v if isinstance(v, str) else str(v) for v in self.source_mat_id]

        if self.tax_class is not None and not isinstance(self.tax_class, str):
            self.tax_class = str(self.tax_class)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.trna_ext_software is not None and not isinstance(self.trna_ext_software, str):
            self.trna_ext_software = str(self.trna_ext_software)

        if self.trnas is not None and not isinstance(self.trnas, str):
            self.trnas = str(self.trnas)

        if self.wga_amp_kit is not None and not isinstance(self.wga_amp_kit, str):
            self.wga_amp_kit = str(self.wga_amp_kit)

        super().__post_init__(**kwargs)


@dataclass
class Miuvig(ChecklistClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS["0010012"]
    class_class_curie: ClassVar[str] = "MIXS:0010012"
    class_name: ClassVar[str] = "Miuvig"
    class_model_uri: ClassVar[URIRef] = MIXS.Miuvig

    assembly_qual: str = None
    assembly_software: str = None
    collection_date: str = None
    detec_type: str = None
    env_broad_scale: str = None
    env_local_scale: str = None
    env_medium: str = None
    geo_loc_name: str = None
    lat_lon: str = None
    number_contig: str = None
    pred_genome_struc: str = None
    pred_genome_type: str = None
    project_name: str = None
    samp_name: str = None
    samp_taxon_id: str = None
    seq_meth: str = None
    source_uvig: str = None
    vir_ident_software: str = None
    virus_enrich_appr: str = None
    adapters: Optional[str] = None
    alt: Optional[str] = None
    annot: Optional[str] = None
    assembly_name: Optional[str] = None
    associated_resource: Optional[Union[str, List[str]]] = empty_list()
    bin_param: Optional[str] = None
    bin_software: Optional[str] = None
    biotic_relationship: Optional[str] = None
    compl_appr: Optional[str] = None
    compl_score: Optional[str] = None
    compl_software: Optional[str] = None
    depth: Optional[str] = None
    elev: Optional[str] = None
    estimated_size: Optional[str] = None
    experimental_factor: Optional[str] = None
    feat_pred: Optional[str] = None
    host_disease_stat: Optional[Union[str, List[str]]] = empty_list()
    host_pred_appr: Optional[str] = None
    host_pred_est_acc: Optional[str] = None
    host_spec_range: Optional[Union[str, List[str]]] = empty_list()
    lib_layout: Optional[str] = None
    lib_reads_seqd: Optional[str] = None
    lib_screen: Optional[str] = None
    lib_size: Optional[str] = None
    lib_vector: Optional[str] = None
    mag_cov_software: Optional[str] = None
    mid: Optional[str] = None
    neg_cont_type: Optional[str] = None
    nucl_acid_amp: Optional[str] = None
    nucl_acid_ext: Optional[str] = None
    otu_class_appr: Optional[str] = None
    otu_db: Optional[str] = None
    otu_seq_comp_appr: Optional[str] = None
    pathogenicity: Optional[str] = None
    pos_cont_type: Optional[str] = None
    reassembly_bin: Optional[str] = None
    ref_biomaterial: Optional[str] = None
    ref_db: Optional[str] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_mat_process: Optional[str] = None
    samp_size: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    sim_search_meth: Optional[str] = None
    single_cell_lysis_appr: Optional[str] = None
    single_cell_lysis_prot: Optional[str] = None
    size_frac: Optional[str] = None
    sop: Optional[Union[str, List[str]]] = empty_list()
    sort_tech: Optional[str] = None
    source_mat_id: Optional[Union[str, List[str]]] = empty_list()
    specific_host: Optional[str] = None
    tax_class: Optional[str] = None
    tax_ident: Optional[str] = None
    temp: Optional[str] = None
    trna_ext_software: Optional[str] = None
    trnas: Optional[str] = None
    wga_amp_appr: Optional[str] = None
    wga_amp_kit: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.assembly_qual):
            self.MissingRequiredField("assembly_qual")
        if not isinstance(self.assembly_qual, str):
            self.assembly_qual = str(self.assembly_qual)

        if self._is_empty(self.assembly_software):
            self.MissingRequiredField("assembly_software")
        if not isinstance(self.assembly_software, str):
            self.assembly_software = str(self.assembly_software)

        if self._is_empty(self.collection_date):
            self.MissingRequiredField("collection_date")
        if not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self._is_empty(self.detec_type):
            self.MissingRequiredField("detec_type")
        if not isinstance(self.detec_type, str):
            self.detec_type = str(self.detec_type)

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

        if self._is_empty(self.number_contig):
            self.MissingRequiredField("number_contig")
        if not isinstance(self.number_contig, str):
            self.number_contig = str(self.number_contig)

        if self._is_empty(self.pred_genome_struc):
            self.MissingRequiredField("pred_genome_struc")
        if not isinstance(self.pred_genome_struc, str):
            self.pred_genome_struc = str(self.pred_genome_struc)

        if self._is_empty(self.pred_genome_type):
            self.MissingRequiredField("pred_genome_type")
        if not isinstance(self.pred_genome_type, str):
            self.pred_genome_type = str(self.pred_genome_type)

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

        if self._is_empty(self.source_uvig):
            self.MissingRequiredField("source_uvig")
        if not isinstance(self.source_uvig, str):
            self.source_uvig = str(self.source_uvig)

        if self._is_empty(self.vir_ident_software):
            self.MissingRequiredField("vir_ident_software")
        if not isinstance(self.vir_ident_software, str):
            self.vir_ident_software = str(self.vir_ident_software)

        if self._is_empty(self.virus_enrich_appr):
            self.MissingRequiredField("virus_enrich_appr")
        if not isinstance(self.virus_enrich_appr, str):
            self.virus_enrich_appr = str(self.virus_enrich_appr)

        if self.adapters is not None and not isinstance(self.adapters, str):
            self.adapters = str(self.adapters)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.annot is not None and not isinstance(self.annot, str):
            self.annot = str(self.annot)

        if self.assembly_name is not None and not isinstance(self.assembly_name, str):
            self.assembly_name = str(self.assembly_name)

        if not isinstance(self.associated_resource, list):
            self.associated_resource = [self.associated_resource] if self.associated_resource is not None else []
        self.associated_resource = [v if isinstance(v, str) else str(v) for v in self.associated_resource]

        if self.bin_param is not None and not isinstance(self.bin_param, str):
            self.bin_param = str(self.bin_param)

        if self.bin_software is not None and not isinstance(self.bin_software, str):
            self.bin_software = str(self.bin_software)

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, str):
            self.biotic_relationship = str(self.biotic_relationship)

        if self.compl_appr is not None and not isinstance(self.compl_appr, str):
            self.compl_appr = str(self.compl_appr)

        if self.compl_score is not None and not isinstance(self.compl_score, str):
            self.compl_score = str(self.compl_score)

        if self.compl_software is not None and not isinstance(self.compl_software, str):
            self.compl_software = str(self.compl_software)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.estimated_size is not None and not isinstance(self.estimated_size, str):
            self.estimated_size = str(self.estimated_size)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.feat_pred is not None and not isinstance(self.feat_pred, str):
            self.feat_pred = str(self.feat_pred)

        if not isinstance(self.host_disease_stat, list):
            self.host_disease_stat = [self.host_disease_stat] if self.host_disease_stat is not None else []
        self.host_disease_stat = [v if isinstance(v, str) else str(v) for v in self.host_disease_stat]

        if self.host_pred_appr is not None and not isinstance(self.host_pred_appr, str):
            self.host_pred_appr = str(self.host_pred_appr)

        if self.host_pred_est_acc is not None and not isinstance(self.host_pred_est_acc, str):
            self.host_pred_est_acc = str(self.host_pred_est_acc)

        if not isinstance(self.host_spec_range, list):
            self.host_spec_range = [self.host_spec_range] if self.host_spec_range is not None else []
        self.host_spec_range = [v if isinstance(v, str) else str(v) for v in self.host_spec_range]

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

        if self.mag_cov_software is not None and not isinstance(self.mag_cov_software, str):
            self.mag_cov_software = str(self.mag_cov_software)

        if self.mid is not None and not isinstance(self.mid, str):
            self.mid = str(self.mid)

        if self.neg_cont_type is not None and not isinstance(self.neg_cont_type, str):
            self.neg_cont_type = str(self.neg_cont_type)

        if self.nucl_acid_amp is not None and not isinstance(self.nucl_acid_amp, str):
            self.nucl_acid_amp = str(self.nucl_acid_amp)

        if self.nucl_acid_ext is not None and not isinstance(self.nucl_acid_ext, str):
            self.nucl_acid_ext = str(self.nucl_acid_ext)

        if self.otu_class_appr is not None and not isinstance(self.otu_class_appr, str):
            self.otu_class_appr = str(self.otu_class_appr)

        if self.otu_db is not None and not isinstance(self.otu_db, str):
            self.otu_db = str(self.otu_db)

        if self.otu_seq_comp_appr is not None and not isinstance(self.otu_seq_comp_appr, str):
            self.otu_seq_comp_appr = str(self.otu_seq_comp_appr)

        if self.pathogenicity is not None and not isinstance(self.pathogenicity, str):
            self.pathogenicity = str(self.pathogenicity)

        if self.pos_cont_type is not None and not isinstance(self.pos_cont_type, str):
            self.pos_cont_type = str(self.pos_cont_type)

        if self.reassembly_bin is not None and not isinstance(self.reassembly_bin, str):
            self.reassembly_bin = str(self.reassembly_bin)

        if self.ref_biomaterial is not None and not isinstance(self.ref_biomaterial, str):
            self.ref_biomaterial = str(self.ref_biomaterial)

        if self.ref_db is not None and not isinstance(self.ref_db, str):
            self.ref_db = str(self.ref_db)

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

        if self.single_cell_lysis_appr is not None and not isinstance(self.single_cell_lysis_appr, str):
            self.single_cell_lysis_appr = str(self.single_cell_lysis_appr)

        if self.single_cell_lysis_prot is not None and not isinstance(self.single_cell_lysis_prot, str):
            self.single_cell_lysis_prot = str(self.single_cell_lysis_prot)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if not isinstance(self.sop, list):
            self.sop = [self.sop] if self.sop is not None else []
        self.sop = [v if isinstance(v, str) else str(v) for v in self.sop]

        if self.sort_tech is not None and not isinstance(self.sort_tech, str):
            self.sort_tech = str(self.sort_tech)

        if not isinstance(self.source_mat_id, list):
            self.source_mat_id = [self.source_mat_id] if self.source_mat_id is not None else []
        self.source_mat_id = [v if isinstance(v, str) else str(v) for v in self.source_mat_id]

        if self.specific_host is not None and not isinstance(self.specific_host, str):
            self.specific_host = str(self.specific_host)

        if self.tax_class is not None and not isinstance(self.tax_class, str):
            self.tax_class = str(self.tax_class)

        if self.tax_ident is not None and not isinstance(self.tax_ident, str):
            self.tax_ident = str(self.tax_ident)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.trna_ext_software is not None and not isinstance(self.trna_ext_software, str):
            self.trna_ext_software = str(self.trna_ext_software)

        if self.trnas is not None and not isinstance(self.trnas, str):
            self.trnas = str(self.trnas)

        if self.wga_amp_appr is not None and not isinstance(self.wga_amp_appr, str):
            self.wga_amp_appr = str(self.wga_amp_appr)

        if self.wga_amp_kit is not None and not isinstance(self.wga_amp_kit, str):
            self.wga_amp_kit = str(self.wga_amp_kit)

        super().__post_init__(**kwargs)


@dataclass
class Mims(ChecklistClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS["0010007"]
    class_class_curie: ClassVar[str] = "MIXS:0010007"
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
    associated_resource: Optional[Union[str, List[str]]] = empty_list()
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
    sop: Optional[Union[str, List[str]]] = empty_list()
    source_mat_id: Optional[Union[str, List[str]]] = empty_list()
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

        if not isinstance(self.associated_resource, list):
            self.associated_resource = [self.associated_resource] if self.associated_resource is not None else []
        self.associated_resource = [v if isinstance(v, str) else str(v) for v in self.associated_resource]

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

        if not isinstance(self.sop, list):
            self.sop = [self.sop] if self.sop is not None else []
        self.sop = [v if isinstance(v, str) else str(v) for v in self.sop]

        if not isinstance(self.source_mat_id, list):
            self.source_mat_id = [self.source_mat_id] if self.source_mat_id is not None else []
        self.source_mat_id = [v if isinstance(v, str) else str(v) for v in self.source_mat_id]

        if self.tax_class is not None and not isinstance(self.tax_class, str):
            self.tax_class = str(self.tax_class)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        super().__post_init__(**kwargs)


@dataclass
class Database(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.Database
    class_class_curie: ClassVar[str] = "MIXS:Database"
    class_name: ClassVar[str] = "Database"
    class_model_uri: ClassVar[URIRef] = MIXS.Database

    mims_set: Optional[Union[Union[dict, Mims], List[Union[dict, Mims]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.mims_set, list):
            self.mims_set = [self.mims_set] if self.mims_set is not None else []
        self.mims_set = [v if isinstance(v, Mims) else Mims(**as_dict(v)) for v in self.mims_set]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.x_16s_recover = Slot(uri=MIXS['0000065'], name="x_16s_recover", curie=MIXS.curie('0000065'),
                   model_uri=MIXS.x_16s_recover, domain=None, range=Optional[str])

slots.x_16s_recover_software = Slot(uri=MIXS['0000066'], name="x_16s_recover_software", curie=MIXS.curie('0000066'),
                   model_uri=MIXS.x_16s_recover_software, domain=None, range=Optional[str])

slots.adapters = Slot(uri=MIXS['0000048'], name="adapters", curie=MIXS.curie('0000048'),
                   model_uri=MIXS.adapters, domain=None, range=Optional[str])

slots.alt = Slot(uri=MIXS['0000094'], name="alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.alt, domain=None, range=Optional[str])

slots.annot = Slot(uri=MIXS['0000059'], name="annot", curie=MIXS.curie('0000059'),
                   model_uri=MIXS.annot, domain=None, range=Optional[str])

slots.assembly_name = Slot(uri=MIXS['0000057'], name="assembly_name", curie=MIXS.curie('0000057'),
                   model_uri=MIXS.assembly_name, domain=None, range=Optional[str])

slots.assembly_qual = Slot(uri=MIXS['0000056'], name="assembly_qual", curie=MIXS.curie('0000056'),
                   model_uri=MIXS.assembly_qual, domain=None, range=Optional[str])

slots.assembly_software = Slot(uri=MIXS['0000058'], name="assembly_software", curie=MIXS.curie('0000058'),
                   model_uri=MIXS.assembly_software, domain=None, range=Optional[str])

slots.associated_resource = Slot(uri=MIXS['0000091'], name="associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.bin_param = Slot(uri=MIXS['0000077'], name="bin_param", curie=MIXS.curie('0000077'),
                   model_uri=MIXS.bin_param, domain=None, range=Optional[str])

slots.bin_software = Slot(uri=MIXS['0000078'], name="bin_software", curie=MIXS.curie('0000078'),
                   model_uri=MIXS.bin_software, domain=None, range=Optional[str])

slots.biotic_relationship = Slot(uri=MIXS['0000028'], name="biotic_relationship", curie=MIXS.curie('0000028'),
                   model_uri=MIXS.biotic_relationship, domain=None, range=Optional[str])

slots.chimera_check = Slot(uri=MIXS['0000052'], name="chimera_check", curie=MIXS.curie('0000052'),
                   model_uri=MIXS.chimera_check, domain=None, range=Optional[str])

slots.collection_date = Slot(uri=MIXS['0000011'], name="collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.collection_date, domain=None, range=Optional[str])

slots.compl_appr = Slot(uri=MIXS['0000071'], name="compl_appr", curie=MIXS.curie('0000071'),
                   model_uri=MIXS.compl_appr, domain=None, range=Optional[str])

slots.compl_score = Slot(uri=MIXS['0000069'], name="compl_score", curie=MIXS.curie('0000069'),
                   model_uri=MIXS.compl_score, domain=None, range=Optional[str])

slots.compl_software = Slot(uri=MIXS['0000070'], name="compl_software", curie=MIXS.curie('0000070'),
                   model_uri=MIXS.compl_software, domain=None, range=Optional[str])

slots.contam_score = Slot(uri=MIXS['0000072'], name="contam_score", curie=MIXS.curie('0000072'),
                   model_uri=MIXS.contam_score, domain=None, range=Optional[str])

slots.contam_screen_input = Slot(uri=MIXS['0000005'], name="contam_screen_input", curie=MIXS.curie('0000005'),
                   model_uri=MIXS.contam_screen_input, domain=None, range=Optional[str])

slots.contam_screen_param = Slot(uri=MIXS['0000073'], name="contam_screen_param", curie=MIXS.curie('0000073'),
                   model_uri=MIXS.contam_screen_param, domain=None, range=Optional[str])

slots.decontam_software = Slot(uri=MIXS['0000074'], name="decontam_software", curie=MIXS.curie('0000074'),
                   model_uri=MIXS.decontam_software, domain=None, range=Optional[str])

slots.depth = Slot(uri=MIXS['0000018'], name="depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.depth, domain=None, range=Optional[str])

slots.detec_type = Slot(uri=MIXS['0000084'], name="detec_type", curie=MIXS.curie('0000084'),
                   model_uri=MIXS.detec_type, domain=None, range=Optional[str])

slots.elev = Slot(uri=MIXS['0000093'], name="elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.elev, domain=None, range=Optional[str])

slots.encoded_traits = Slot(uri=MIXS['0000034'], name="encoded_traits", curie=MIXS.curie('0000034'),
                   model_uri=MIXS.encoded_traits, domain=None, range=Optional[str])

slots.env_broad_scale = Slot(uri=MIXS['0000012'], name="env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.env_broad_scale, domain=None, range=Optional[str])

slots.env_local_scale = Slot(uri=MIXS['0000013'], name="env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.env_local_scale, domain=None, range=Optional[str])

slots.env_medium = Slot(uri=MIXS['0000014'], name="env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.env_medium, domain=None, range=Optional[str])

slots.estimated_size = Slot(uri=MIXS['0000024'], name="estimated_size", curie=MIXS.curie('0000024'),
                   model_uri=MIXS.estimated_size, domain=None, range=Optional[str])

slots.experimental_factor = Slot(uri=MIXS['0000008'], name="experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.experimental_factor, domain=None, range=Optional[str])

slots.extrachrom_elements = Slot(uri=MIXS['0000023'], name="extrachrom_elements", curie=MIXS.curie('0000023'),
                   model_uri=MIXS.extrachrom_elements, domain=None, range=Optional[str])

slots.feat_pred = Slot(uri=MIXS['0000061'], name="feat_pred", curie=MIXS.curie('0000061'),
                   model_uri=MIXS.feat_pred, domain=None, range=Optional[str])

slots.geo_loc_name = Slot(uri=MIXS['0000010'], name="geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.geo_loc_name, domain=None, range=Optional[str])

slots.host_disease_stat = Slot(uri=MIXS['0000031'], name="host_disease_stat", curie=MIXS.curie('0000031'),
                   model_uri=MIXS.host_disease_stat, domain=None, range=Optional[Union[str, List[str]]])

slots.host_pred_appr = Slot(uri=MIXS['0000088'], name="host_pred_appr", curie=MIXS.curie('0000088'),
                   model_uri=MIXS.host_pred_appr, domain=None, range=Optional[str])

slots.host_pred_est_acc = Slot(uri=MIXS['0000089'], name="host_pred_est_acc", curie=MIXS.curie('0000089'),
                   model_uri=MIXS.host_pred_est_acc, domain=None, range=Optional[str])

slots.host_spec_range = Slot(uri=MIXS['0000030'], name="host_spec_range", curie=MIXS.curie('0000030'),
                   model_uri=MIXS.host_spec_range, domain=None, range=Optional[Union[str, List[str]]])

slots.isol_growth_condt = Slot(uri=MIXS['0000003'], name="isol_growth_condt", curie=MIXS.curie('0000003'),
                   model_uri=MIXS.isol_growth_condt, domain=None, range=Optional[str])

slots.lat_lon = Slot(uri=MIXS['0000009'], name="lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.lat_lon, domain=None, range=Optional[str])

slots.lib_layout = Slot(uri=MIXS['0000041'], name="lib_layout", curie=MIXS.curie('0000041'),
                   model_uri=MIXS.lib_layout, domain=None, range=Optional[str])

slots.lib_reads_seqd = Slot(uri=MIXS['0000040'], name="lib_reads_seqd", curie=MIXS.curie('0000040'),
                   model_uri=MIXS.lib_reads_seqd, domain=None, range=Optional[str])

slots.lib_screen = Slot(uri=MIXS['0000043'], name="lib_screen", curie=MIXS.curie('0000043'),
                   model_uri=MIXS.lib_screen, domain=None, range=Optional[str])

slots.lib_size = Slot(uri=MIXS['0000039'], name="lib_size", curie=MIXS.curie('0000039'),
                   model_uri=MIXS.lib_size, domain=None, range=Optional[str])

slots.lib_vector = Slot(uri=MIXS['0000042'], name="lib_vector", curie=MIXS.curie('0000042'),
                   model_uri=MIXS.lib_vector, domain=None, range=Optional[str])

slots.mag_cov_software = Slot(uri=MIXS['0000080'], name="mag_cov_software", curie=MIXS.curie('0000080'),
                   model_uri=MIXS.mag_cov_software, domain=None, range=Optional[str])

slots.mid = Slot(uri=MIXS['0000047'], name="mid", curie=MIXS.curie('0000047'),
                   model_uri=MIXS.mid, domain=None, range=Optional[str])

slots.neg_cont_type = Slot(uri=MIXS['0001321'], name="neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.neg_cont_type, domain=None, range=Optional[str])

slots.nucl_acid_amp = Slot(uri=MIXS['0000038'], name="nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.nucl_acid_amp, domain=None, range=Optional[str])

slots.nucl_acid_ext = Slot(uri=MIXS['0000037'], name="nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.nucl_acid_ext, domain=None, range=Optional[str])

slots.num_replicons = Slot(uri=MIXS['0000022'], name="num_replicons", curie=MIXS.curie('0000022'),
                   model_uri=MIXS.num_replicons, domain=None, range=Optional[str])

slots.number_contig = Slot(uri=MIXS['0000060'], name="number_contig", curie=MIXS.curie('0000060'),
                   model_uri=MIXS.number_contig, domain=None, range=Optional[str])

slots.otu_class_appr = Slot(uri=MIXS['0000085'], name="otu_class_appr", curie=MIXS.curie('0000085'),
                   model_uri=MIXS.otu_class_appr, domain=None, range=Optional[str])

slots.otu_db = Slot(uri=MIXS['0000087'], name="otu_db", curie=MIXS.curie('0000087'),
                   model_uri=MIXS.otu_db, domain=None, range=Optional[str])

slots.otu_seq_comp_appr = Slot(uri=MIXS['0000086'], name="otu_seq_comp_appr", curie=MIXS.curie('0000086'),
                   model_uri=MIXS.otu_seq_comp_appr, domain=None, range=Optional[str])

slots.pathogenicity = Slot(uri=MIXS['0000027'], name="pathogenicity", curie=MIXS.curie('0000027'),
                   model_uri=MIXS.pathogenicity, domain=None, range=Optional[str])

slots.pcr_cond = Slot(uri=MIXS['0000049'], name="pcr_cond", curie=MIXS.curie('0000049'),
                   model_uri=MIXS.pcr_cond, domain=None, range=Optional[str])

slots.pcr_primers = Slot(uri=MIXS['0000046'], name="pcr_primers", curie=MIXS.curie('0000046'),
                   model_uri=MIXS.pcr_primers, domain=None, range=Optional[str])

slots.ploidy = Slot(uri=MIXS['0000021'], name="ploidy", curie=MIXS.curie('0000021'),
                   model_uri=MIXS.ploidy, domain=None, range=Optional[str])

slots.pos_cont_type = Slot(uri=MIXS['0001322'], name="pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.pos_cont_type, domain=None, range=Optional[str])

slots.pred_genome_struc = Slot(uri=MIXS['0000083'], name="pred_genome_struc", curie=MIXS.curie('0000083'),
                   model_uri=MIXS.pred_genome_struc, domain=None, range=Optional[str])

slots.pred_genome_type = Slot(uri=MIXS['0000082'], name="pred_genome_type", curie=MIXS.curie('0000082'),
                   model_uri=MIXS.pred_genome_type, domain=None, range=Optional[str])

slots.project_name = Slot(uri=MIXS['0000092'], name="project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.project_name, domain=None, range=Optional[str])

slots.propagation = Slot(uri=MIXS['0000033'], name="propagation", curie=MIXS.curie('0000033'),
                   model_uri=MIXS.propagation, domain=None, range=Optional[str])

slots.reassembly_bin = Slot(uri=MIXS['0000079'], name="reassembly_bin", curie=MIXS.curie('0000079'),
                   model_uri=MIXS.reassembly_bin, domain=None, range=Optional[str])

slots.ref_biomaterial = Slot(uri=MIXS['0000025'], name="ref_biomaterial", curie=MIXS.curie('0000025'),
                   model_uri=MIXS.ref_biomaterial, domain=None, range=Optional[str])

slots.ref_db = Slot(uri=MIXS['0000062'], name="ref_db", curie=MIXS.curie('0000062'),
                   model_uri=MIXS.ref_db, domain=None, range=Optional[str])

slots.rel_to_oxygen = Slot(uri=MIXS['0000015'], name="rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=MIXS.rel_to_oxygen, domain=None, range=Optional[str])

slots.samp_collec_device = Slot(uri=MIXS['0000002'], name="samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.samp_collec_device, domain=None, range=Optional[str])

slots.samp_collec_method = Slot(uri=MIXS['0001225'], name="samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.samp_collec_method, domain=None, range=Optional[str])

slots.samp_mat_process = Slot(uri=MIXS['0000016'], name="samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.samp_mat_process, domain=None, range=Optional[str])

slots.samp_name = Slot(uri=MIXS['0001107'], name="samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.samp_name, domain=None, range=Optional[str])

slots.samp_size = Slot(uri=MIXS['0000001'], name="samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.samp_size, domain=None, range=Optional[str])

slots.samp_taxon_id = Slot(uri=MIXS['0001320'], name="samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.samp_taxon_id, domain=None, range=Optional[str])

slots.samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.seq_meth = Slot(uri=MIXS['0000050'], name="seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.seq_meth, domain=None, range=Optional[str])

slots.seq_quality_check = Slot(uri=MIXS['0000051'], name="seq_quality_check", curie=MIXS.curie('0000051'),
                   model_uri=MIXS.seq_quality_check, domain=None, range=Optional[str])

slots.sim_search_meth = Slot(uri=MIXS['0000063'], name="sim_search_meth", curie=MIXS.curie('0000063'),
                   model_uri=MIXS.sim_search_meth, domain=None, range=Optional[str])

slots.single_cell_lysis_appr = Slot(uri=MIXS['0000076'], name="single_cell_lysis_appr", curie=MIXS.curie('0000076'),
                   model_uri=MIXS.single_cell_lysis_appr, domain=None, range=Optional[str])

slots.single_cell_lysis_prot = Slot(uri=MIXS['0000054'], name="single_cell_lysis_prot", curie=MIXS.curie('0000054'),
                   model_uri=MIXS.single_cell_lysis_prot, domain=None, range=Optional[str])

slots.size_frac = Slot(uri=MIXS['0000017'], name="size_frac", curie=MIXS.curie('0000017'),
                   model_uri=MIXS.size_frac, domain=None, range=Optional[str])

slots.sop = Slot(uri=MIXS['0000090'], name="sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.sop, domain=None, range=Optional[Union[str, List[str]]])

slots.sort_tech = Slot(uri=MIXS['0000075'], name="sort_tech", curie=MIXS.curie('0000075'),
                   model_uri=MIXS.sort_tech, domain=None, range=Optional[str])

slots.source_mat_id = Slot(uri=MIXS['0000026'], name="source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.source_uvig = Slot(uri=MIXS['0000035'], name="source_uvig", curie=MIXS.curie('0000035'),
                   model_uri=MIXS.source_uvig, domain=None, range=Optional[str])

slots.specific_host = Slot(uri=MIXS['0000029'], name="specific_host", curie=MIXS.curie('0000029'),
                   model_uri=MIXS.specific_host, domain=None, range=Optional[str])

slots.subspecf_gen_lin = Slot(uri=MIXS['0000020'], name="subspecf_gen_lin", curie=MIXS.curie('0000020'),
                   model_uri=MIXS.subspecf_gen_lin, domain=None, range=Optional[str])

slots.target_gene = Slot(uri=MIXS['0000044'], name="target_gene", curie=MIXS.curie('0000044'),
                   model_uri=MIXS.target_gene, domain=None, range=Optional[str])

slots.target_subfragment = Slot(uri=MIXS['0000045'], name="target_subfragment", curie=MIXS.curie('0000045'),
                   model_uri=MIXS.target_subfragment, domain=None, range=Optional[str])

slots.tax_class = Slot(uri=MIXS['0000064'], name="tax_class", curie=MIXS.curie('0000064'),
                   model_uri=MIXS.tax_class, domain=None, range=Optional[str])

slots.tax_ident = Slot(uri=MIXS['0000053'], name="tax_ident", curie=MIXS.curie('0000053'),
                   model_uri=MIXS.tax_ident, domain=None, range=Optional[str])

slots.temp = Slot(uri=MIXS['0000113'], name="temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.temp, domain=None, range=Optional[str])

slots.trna_ext_software = Slot(uri=MIXS['0000068'], name="trna_ext_software", curie=MIXS.curie('0000068'),
                   model_uri=MIXS.trna_ext_software, domain=None, range=Optional[str])

slots.trnas = Slot(uri=MIXS['0000067'], name="trnas", curie=MIXS.curie('0000067'),
                   model_uri=MIXS.trnas, domain=None, range=Optional[str])

slots.trophic_level = Slot(uri=MIXS['0000032'], name="trophic_level", curie=MIXS.curie('0000032'),
                   model_uri=MIXS.trophic_level, domain=None, range=Optional[str])

slots.vir_ident_software = Slot(uri=MIXS['0000081'], name="vir_ident_software", curie=MIXS.curie('0000081'),
                   model_uri=MIXS.vir_ident_software, domain=None, range=Optional[str])

slots.virus_enrich_appr = Slot(uri=MIXS['0000036'], name="virus_enrich_appr", curie=MIXS.curie('0000036'),
                   model_uri=MIXS.virus_enrich_appr, domain=None, range=Optional[str])

slots.wga_amp_appr = Slot(uri=MIXS['0000055'], name="wga_amp_appr", curie=MIXS.curie('0000055'),
                   model_uri=MIXS.wga_amp_appr, domain=None, range=Optional[str])

slots.wga_amp_kit = Slot(uri=MIXS['0000006'], name="wga_amp_kit", curie=MIXS.curie('0000006'),
                   model_uri=MIXS.wga_amp_kit, domain=None, range=Optional[str])

slots.mims_set = Slot(uri=MIXS.mims_set, name="mims_set", curie=MIXS.curie('mims_set'),
                   model_uri=MIXS.mims_set, domain=None, range=Optional[str])

slots.MigsBa_adapters = Slot(uri=MIXS['0000048'], name="MigsBa_adapters", curie=MIXS.curie('0000048'),
                   model_uri=MIXS.MigsBa_adapters, domain=None, range=Optional[str])

slots.MigsBa_alt = Slot(uri=MIXS['0000094'], name="MigsBa_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.MigsBa_alt, domain=None, range=Optional[str])

slots.MigsBa_annot = Slot(uri=MIXS['0000059'], name="MigsBa_annot", curie=MIXS.curie('0000059'),
                   model_uri=MIXS.MigsBa_annot, domain=None, range=Optional[str])

slots.MigsBa_assembly_name = Slot(uri=MIXS['0000057'], name="MigsBa_assembly_name", curie=MIXS.curie('0000057'),
                   model_uri=MIXS.MigsBa_assembly_name, domain=None, range=Optional[str])

slots.MigsBa_assembly_qual = Slot(uri=MIXS['0000056'], name="MigsBa_assembly_qual", curie=MIXS.curie('0000056'),
                   model_uri=MIXS.MigsBa_assembly_qual, domain=None, range=str)

slots.MigsBa_assembly_software = Slot(uri=MIXS['0000058'], name="MigsBa_assembly_software", curie=MIXS.curie('0000058'),
                   model_uri=MIXS.MigsBa_assembly_software, domain=None, range=str)

slots.MigsBa_associated_resource = Slot(uri=MIXS['0000091'], name="MigsBa_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.MigsBa_associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsBa_biotic_relationship = Slot(uri=MIXS['0000028'], name="MigsBa_biotic_relationship", curie=MIXS.curie('0000028'),
                   model_uri=MIXS.MigsBa_biotic_relationship, domain=None, range=Optional[str])

slots.MigsBa_collection_date = Slot(uri=MIXS['0000011'], name="MigsBa_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.MigsBa_collection_date, domain=None, range=str)

slots.MigsBa_compl_score = Slot(uri=MIXS['0000069'], name="MigsBa_compl_score", curie=MIXS.curie('0000069'),
                   model_uri=MIXS.MigsBa_compl_score, domain=None, range=Optional[str])

slots.MigsBa_compl_software = Slot(uri=MIXS['0000070'], name="MigsBa_compl_software", curie=MIXS.curie('0000070'),
                   model_uri=MIXS.MigsBa_compl_software, domain=None, range=Optional[str])

slots.MigsBa_depth = Slot(uri=MIXS['0000018'], name="MigsBa_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.MigsBa_depth, domain=None, range=Optional[str])

slots.MigsBa_elev = Slot(uri=MIXS['0000093'], name="MigsBa_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.MigsBa_elev, domain=None, range=Optional[str])

slots.MigsBa_encoded_traits = Slot(uri=MIXS['0000034'], name="MigsBa_encoded_traits", curie=MIXS.curie('0000034'),
                   model_uri=MIXS.MigsBa_encoded_traits, domain=None, range=Optional[str])

slots.MigsBa_env_broad_scale = Slot(uri=MIXS['0000012'], name="MigsBa_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.MigsBa_env_broad_scale, domain=None, range=str)

slots.MigsBa_env_local_scale = Slot(uri=MIXS['0000013'], name="MigsBa_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.MigsBa_env_local_scale, domain=None, range=str)

slots.MigsBa_env_medium = Slot(uri=MIXS['0000014'], name="MigsBa_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.MigsBa_env_medium, domain=None, range=str)

slots.MigsBa_estimated_size = Slot(uri=MIXS['0000024'], name="MigsBa_estimated_size", curie=MIXS.curie('0000024'),
                   model_uri=MIXS.MigsBa_estimated_size, domain=None, range=Optional[str])

slots.MigsBa_experimental_factor = Slot(uri=MIXS['0000008'], name="MigsBa_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.MigsBa_experimental_factor, domain=None, range=Optional[str])

slots.MigsBa_extrachrom_elements = Slot(uri=MIXS['0000023'], name="MigsBa_extrachrom_elements", curie=MIXS.curie('0000023'),
                   model_uri=MIXS.MigsBa_extrachrom_elements, domain=None, range=Optional[str])

slots.MigsBa_feat_pred = Slot(uri=MIXS['0000061'], name="MigsBa_feat_pred", curie=MIXS.curie('0000061'),
                   model_uri=MIXS.MigsBa_feat_pred, domain=None, range=Optional[str])

slots.MigsBa_geo_loc_name = Slot(uri=MIXS['0000010'], name="MigsBa_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.MigsBa_geo_loc_name, domain=None, range=str)

slots.MigsBa_host_disease_stat = Slot(uri=MIXS['0000031'], name="MigsBa_host_disease_stat", curie=MIXS.curie('0000031'),
                   model_uri=MIXS.MigsBa_host_disease_stat, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsBa_host_spec_range = Slot(uri=MIXS['0000030'], name="MigsBa_host_spec_range", curie=MIXS.curie('0000030'),
                   model_uri=MIXS.MigsBa_host_spec_range, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsBa_isol_growth_condt = Slot(uri=MIXS['0000003'], name="MigsBa_isol_growth_condt", curie=MIXS.curie('0000003'),
                   model_uri=MIXS.MigsBa_isol_growth_condt, domain=None, range=str)

slots.MigsBa_lat_lon = Slot(uri=MIXS['0000009'], name="MigsBa_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.MigsBa_lat_lon, domain=None, range=str)

slots.MigsBa_lib_layout = Slot(uri=MIXS['0000041'], name="MigsBa_lib_layout", curie=MIXS.curie('0000041'),
                   model_uri=MIXS.MigsBa_lib_layout, domain=None, range=Optional[str])

slots.MigsBa_lib_reads_seqd = Slot(uri=MIXS['0000040'], name="MigsBa_lib_reads_seqd", curie=MIXS.curie('0000040'),
                   model_uri=MIXS.MigsBa_lib_reads_seqd, domain=None, range=Optional[str])

slots.MigsBa_lib_screen = Slot(uri=MIXS['0000043'], name="MigsBa_lib_screen", curie=MIXS.curie('0000043'),
                   model_uri=MIXS.MigsBa_lib_screen, domain=None, range=Optional[str])

slots.MigsBa_lib_size = Slot(uri=MIXS['0000039'], name="MigsBa_lib_size", curie=MIXS.curie('0000039'),
                   model_uri=MIXS.MigsBa_lib_size, domain=None, range=Optional[str])

slots.MigsBa_lib_vector = Slot(uri=MIXS['0000042'], name="MigsBa_lib_vector", curie=MIXS.curie('0000042'),
                   model_uri=MIXS.MigsBa_lib_vector, domain=None, range=Optional[str])

slots.MigsBa_neg_cont_type = Slot(uri=MIXS['0001321'], name="MigsBa_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.MigsBa_neg_cont_type, domain=None, range=Optional[str])

slots.MigsBa_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="MigsBa_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.MigsBa_nucl_acid_amp, domain=None, range=Optional[str])

slots.MigsBa_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="MigsBa_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.MigsBa_nucl_acid_ext, domain=None, range=Optional[str])

slots.MigsBa_num_replicons = Slot(uri=MIXS['0000022'], name="MigsBa_num_replicons", curie=MIXS.curie('0000022'),
                   model_uri=MIXS.MigsBa_num_replicons, domain=None, range=str)

slots.MigsBa_number_contig = Slot(uri=MIXS['0000060'], name="MigsBa_number_contig", curie=MIXS.curie('0000060'),
                   model_uri=MIXS.MigsBa_number_contig, domain=None, range=str)

slots.MigsBa_pathogenicity = Slot(uri=MIXS['0000027'], name="MigsBa_pathogenicity", curie=MIXS.curie('0000027'),
                   model_uri=MIXS.MigsBa_pathogenicity, domain=None, range=Optional[str])

slots.MigsBa_pos_cont_type = Slot(uri=MIXS['0001322'], name="MigsBa_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.MigsBa_pos_cont_type, domain=None, range=Optional[str])

slots.MigsBa_project_name = Slot(uri=MIXS['0000092'], name="MigsBa_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.MigsBa_project_name, domain=None, range=str)

slots.MigsBa_ref_biomaterial = Slot(uri=MIXS['0000025'], name="MigsBa_ref_biomaterial", curie=MIXS.curie('0000025'),
                   model_uri=MIXS.MigsBa_ref_biomaterial, domain=None, range=str)

slots.MigsBa_ref_db = Slot(uri=MIXS['0000062'], name="MigsBa_ref_db", curie=MIXS.curie('0000062'),
                   model_uri=MIXS.MigsBa_ref_db, domain=None, range=Optional[str])

slots.MigsBa_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="MigsBa_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=MIXS.MigsBa_rel_to_oxygen, domain=None, range=Optional[str])

slots.MigsBa_samp_collec_device = Slot(uri=MIXS['0000002'], name="MigsBa_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.MigsBa_samp_collec_device, domain=None, range=Optional[str])

slots.MigsBa_samp_collec_method = Slot(uri=MIXS['0001225'], name="MigsBa_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.MigsBa_samp_collec_method, domain=None, range=Optional[str])

slots.MigsBa_samp_mat_process = Slot(uri=MIXS['0000016'], name="MigsBa_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.MigsBa_samp_mat_process, domain=None, range=Optional[str])

slots.MigsBa_samp_name = Slot(uri=MIXS['0001107'], name="MigsBa_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.MigsBa_samp_name, domain=None, range=str)

slots.MigsBa_samp_size = Slot(uri=MIXS['0000001'], name="MigsBa_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.MigsBa_samp_size, domain=None, range=Optional[str])

slots.MigsBa_samp_taxon_id = Slot(uri=MIXS['0001320'], name="MigsBa_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.MigsBa_samp_taxon_id, domain=None, range=str)

slots.MigsBa_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="MigsBa_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.MigsBa_samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.MigsBa_seq_meth = Slot(uri=MIXS['0000050'], name="MigsBa_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.MigsBa_seq_meth, domain=None, range=str)

slots.MigsBa_sim_search_meth = Slot(uri=MIXS['0000063'], name="MigsBa_sim_search_meth", curie=MIXS.curie('0000063'),
                   model_uri=MIXS.MigsBa_sim_search_meth, domain=None, range=Optional[str])

slots.MigsBa_sop = Slot(uri=MIXS['0000090'], name="MigsBa_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.MigsBa_sop, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsBa_source_mat_id = Slot(uri=MIXS['0000026'], name="MigsBa_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.MigsBa_source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsBa_specific_host = Slot(uri=MIXS['0000029'], name="MigsBa_specific_host", curie=MIXS.curie('0000029'),
                   model_uri=MIXS.MigsBa_specific_host, domain=None, range=Optional[str])

slots.MigsBa_subspecf_gen_lin = Slot(uri=MIXS['0000020'], name="MigsBa_subspecf_gen_lin", curie=MIXS.curie('0000020'),
                   model_uri=MIXS.MigsBa_subspecf_gen_lin, domain=None, range=Optional[str])

slots.MigsBa_tax_class = Slot(uri=MIXS['0000064'], name="MigsBa_tax_class", curie=MIXS.curie('0000064'),
                   model_uri=MIXS.MigsBa_tax_class, domain=None, range=Optional[str])

slots.MigsBa_tax_ident = Slot(uri=MIXS['0000053'], name="MigsBa_tax_ident", curie=MIXS.curie('0000053'),
                   model_uri=MIXS.MigsBa_tax_ident, domain=None, range=Optional[str])

slots.MigsBa_temp = Slot(uri=MIXS['0000113'], name="MigsBa_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.MigsBa_temp, domain=None, range=Optional[str])

slots.MigsBa_trophic_level = Slot(uri=MIXS['0000032'], name="MigsBa_trophic_level", curie=MIXS.curie('0000032'),
                   model_uri=MIXS.MigsBa_trophic_level, domain=None, range=Optional[str])

slots.MigsEu_adapters = Slot(uri=MIXS['0000048'], name="MigsEu_adapters", curie=MIXS.curie('0000048'),
                   model_uri=MIXS.MigsEu_adapters, domain=None, range=Optional[str])

slots.MigsEu_alt = Slot(uri=MIXS['0000094'], name="MigsEu_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.MigsEu_alt, domain=None, range=Optional[str])

slots.MigsEu_annot = Slot(uri=MIXS['0000059'], name="MigsEu_annot", curie=MIXS.curie('0000059'),
                   model_uri=MIXS.MigsEu_annot, domain=None, range=Optional[str])

slots.MigsEu_assembly_name = Slot(uri=MIXS['0000057'], name="MigsEu_assembly_name", curie=MIXS.curie('0000057'),
                   model_uri=MIXS.MigsEu_assembly_name, domain=None, range=Optional[str])

slots.MigsEu_assembly_qual = Slot(uri=MIXS['0000056'], name="MigsEu_assembly_qual", curie=MIXS.curie('0000056'),
                   model_uri=MIXS.MigsEu_assembly_qual, domain=None, range=str)

slots.MigsEu_assembly_software = Slot(uri=MIXS['0000058'], name="MigsEu_assembly_software", curie=MIXS.curie('0000058'),
                   model_uri=MIXS.MigsEu_assembly_software, domain=None, range=str)

slots.MigsEu_associated_resource = Slot(uri=MIXS['0000091'], name="MigsEu_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.MigsEu_associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsEu_biotic_relationship = Slot(uri=MIXS['0000028'], name="MigsEu_biotic_relationship", curie=MIXS.curie('0000028'),
                   model_uri=MIXS.MigsEu_biotic_relationship, domain=None, range=Optional[str])

slots.MigsEu_collection_date = Slot(uri=MIXS['0000011'], name="MigsEu_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.MigsEu_collection_date, domain=None, range=str)

slots.MigsEu_compl_score = Slot(uri=MIXS['0000069'], name="MigsEu_compl_score", curie=MIXS.curie('0000069'),
                   model_uri=MIXS.MigsEu_compl_score, domain=None, range=Optional[str])

slots.MigsEu_compl_software = Slot(uri=MIXS['0000070'], name="MigsEu_compl_software", curie=MIXS.curie('0000070'),
                   model_uri=MIXS.MigsEu_compl_software, domain=None, range=Optional[str])

slots.MigsEu_depth = Slot(uri=MIXS['0000018'], name="MigsEu_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.MigsEu_depth, domain=None, range=Optional[str])

slots.MigsEu_elev = Slot(uri=MIXS['0000093'], name="MigsEu_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.MigsEu_elev, domain=None, range=Optional[str])

slots.MigsEu_env_broad_scale = Slot(uri=MIXS['0000012'], name="MigsEu_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.MigsEu_env_broad_scale, domain=None, range=str)

slots.MigsEu_env_local_scale = Slot(uri=MIXS['0000013'], name="MigsEu_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.MigsEu_env_local_scale, domain=None, range=str)

slots.MigsEu_env_medium = Slot(uri=MIXS['0000014'], name="MigsEu_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.MigsEu_env_medium, domain=None, range=str)

slots.MigsEu_estimated_size = Slot(uri=MIXS['0000024'], name="MigsEu_estimated_size", curie=MIXS.curie('0000024'),
                   model_uri=MIXS.MigsEu_estimated_size, domain=None, range=Optional[str])

slots.MigsEu_experimental_factor = Slot(uri=MIXS['0000008'], name="MigsEu_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.MigsEu_experimental_factor, domain=None, range=Optional[str])

slots.MigsEu_extrachrom_elements = Slot(uri=MIXS['0000023'], name="MigsEu_extrachrom_elements", curie=MIXS.curie('0000023'),
                   model_uri=MIXS.MigsEu_extrachrom_elements, domain=None, range=Optional[str])

slots.MigsEu_feat_pred = Slot(uri=MIXS['0000061'], name="MigsEu_feat_pred", curie=MIXS.curie('0000061'),
                   model_uri=MIXS.MigsEu_feat_pred, domain=None, range=Optional[str])

slots.MigsEu_geo_loc_name = Slot(uri=MIXS['0000010'], name="MigsEu_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.MigsEu_geo_loc_name, domain=None, range=str)

slots.MigsEu_host_disease_stat = Slot(uri=MIXS['0000031'], name="MigsEu_host_disease_stat", curie=MIXS.curie('0000031'),
                   model_uri=MIXS.MigsEu_host_disease_stat, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsEu_host_spec_range = Slot(uri=MIXS['0000030'], name="MigsEu_host_spec_range", curie=MIXS.curie('0000030'),
                   model_uri=MIXS.MigsEu_host_spec_range, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsEu_isol_growth_condt = Slot(uri=MIXS['0000003'], name="MigsEu_isol_growth_condt", curie=MIXS.curie('0000003'),
                   model_uri=MIXS.MigsEu_isol_growth_condt, domain=None, range=str)

slots.MigsEu_lat_lon = Slot(uri=MIXS['0000009'], name="MigsEu_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.MigsEu_lat_lon, domain=None, range=str)

slots.MigsEu_lib_layout = Slot(uri=MIXS['0000041'], name="MigsEu_lib_layout", curie=MIXS.curie('0000041'),
                   model_uri=MIXS.MigsEu_lib_layout, domain=None, range=Optional[str])

slots.MigsEu_lib_reads_seqd = Slot(uri=MIXS['0000040'], name="MigsEu_lib_reads_seqd", curie=MIXS.curie('0000040'),
                   model_uri=MIXS.MigsEu_lib_reads_seqd, domain=None, range=Optional[str])

slots.MigsEu_lib_screen = Slot(uri=MIXS['0000043'], name="MigsEu_lib_screen", curie=MIXS.curie('0000043'),
                   model_uri=MIXS.MigsEu_lib_screen, domain=None, range=Optional[str])

slots.MigsEu_lib_size = Slot(uri=MIXS['0000039'], name="MigsEu_lib_size", curie=MIXS.curie('0000039'),
                   model_uri=MIXS.MigsEu_lib_size, domain=None, range=Optional[str])

slots.MigsEu_lib_vector = Slot(uri=MIXS['0000042'], name="MigsEu_lib_vector", curie=MIXS.curie('0000042'),
                   model_uri=MIXS.MigsEu_lib_vector, domain=None, range=Optional[str])

slots.MigsEu_neg_cont_type = Slot(uri=MIXS['0001321'], name="MigsEu_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.MigsEu_neg_cont_type, domain=None, range=Optional[str])

slots.MigsEu_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="MigsEu_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.MigsEu_nucl_acid_amp, domain=None, range=Optional[str])

slots.MigsEu_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="MigsEu_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.MigsEu_nucl_acid_ext, domain=None, range=Optional[str])

slots.MigsEu_num_replicons = Slot(uri=MIXS['0000022'], name="MigsEu_num_replicons", curie=MIXS.curie('0000022'),
                   model_uri=MIXS.MigsEu_num_replicons, domain=None, range=Optional[str])

slots.MigsEu_number_contig = Slot(uri=MIXS['0000060'], name="MigsEu_number_contig", curie=MIXS.curie('0000060'),
                   model_uri=MIXS.MigsEu_number_contig, domain=None, range=str)

slots.MigsEu_pathogenicity = Slot(uri=MIXS['0000027'], name="MigsEu_pathogenicity", curie=MIXS.curie('0000027'),
                   model_uri=MIXS.MigsEu_pathogenicity, domain=None, range=Optional[str])

slots.MigsEu_ploidy = Slot(uri=MIXS['0000021'], name="MigsEu_ploidy", curie=MIXS.curie('0000021'),
                   model_uri=MIXS.MigsEu_ploidy, domain=None, range=Optional[str])

slots.MigsEu_pos_cont_type = Slot(uri=MIXS['0001322'], name="MigsEu_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.MigsEu_pos_cont_type, domain=None, range=Optional[str])

slots.MigsEu_project_name = Slot(uri=MIXS['0000092'], name="MigsEu_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.MigsEu_project_name, domain=None, range=str)

slots.MigsEu_propagation = Slot(uri=MIXS['0000033'], name="MigsEu_propagation", curie=MIXS.curie('0000033'),
                   model_uri=MIXS.MigsEu_propagation, domain=None, range=Optional[str])

slots.MigsEu_ref_biomaterial = Slot(uri=MIXS['0000025'], name="MigsEu_ref_biomaterial", curie=MIXS.curie('0000025'),
                   model_uri=MIXS.MigsEu_ref_biomaterial, domain=None, range=Optional[str])

slots.MigsEu_ref_db = Slot(uri=MIXS['0000062'], name="MigsEu_ref_db", curie=MIXS.curie('0000062'),
                   model_uri=MIXS.MigsEu_ref_db, domain=None, range=Optional[str])

slots.MigsEu_samp_collec_device = Slot(uri=MIXS['0000002'], name="MigsEu_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.MigsEu_samp_collec_device, domain=None, range=Optional[str])

slots.MigsEu_samp_collec_method = Slot(uri=MIXS['0001225'], name="MigsEu_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.MigsEu_samp_collec_method, domain=None, range=Optional[str])

slots.MigsEu_samp_mat_process = Slot(uri=MIXS['0000016'], name="MigsEu_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.MigsEu_samp_mat_process, domain=None, range=Optional[str])

slots.MigsEu_samp_name = Slot(uri=MIXS['0001107'], name="MigsEu_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.MigsEu_samp_name, domain=None, range=str)

slots.MigsEu_samp_size = Slot(uri=MIXS['0000001'], name="MigsEu_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.MigsEu_samp_size, domain=None, range=Optional[str])

slots.MigsEu_samp_taxon_id = Slot(uri=MIXS['0001320'], name="MigsEu_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.MigsEu_samp_taxon_id, domain=None, range=str)

slots.MigsEu_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="MigsEu_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.MigsEu_samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.MigsEu_seq_meth = Slot(uri=MIXS['0000050'], name="MigsEu_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.MigsEu_seq_meth, domain=None, range=str)

slots.MigsEu_sim_search_meth = Slot(uri=MIXS['0000063'], name="MigsEu_sim_search_meth", curie=MIXS.curie('0000063'),
                   model_uri=MIXS.MigsEu_sim_search_meth, domain=None, range=Optional[str])

slots.MigsEu_sop = Slot(uri=MIXS['0000090'], name="MigsEu_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.MigsEu_sop, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsEu_source_mat_id = Slot(uri=MIXS['0000026'], name="MigsEu_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.MigsEu_source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsEu_specific_host = Slot(uri=MIXS['0000029'], name="MigsEu_specific_host", curie=MIXS.curie('0000029'),
                   model_uri=MIXS.MigsEu_specific_host, domain=None, range=Optional[str])

slots.MigsEu_subspecf_gen_lin = Slot(uri=MIXS['0000020'], name="MigsEu_subspecf_gen_lin", curie=MIXS.curie('0000020'),
                   model_uri=MIXS.MigsEu_subspecf_gen_lin, domain=None, range=Optional[str])

slots.MigsEu_tax_class = Slot(uri=MIXS['0000064'], name="MigsEu_tax_class", curie=MIXS.curie('0000064'),
                   model_uri=MIXS.MigsEu_tax_class, domain=None, range=Optional[str])

slots.MigsEu_tax_ident = Slot(uri=MIXS['0000053'], name="MigsEu_tax_ident", curie=MIXS.curie('0000053'),
                   model_uri=MIXS.MigsEu_tax_ident, domain=None, range=Optional[str])

slots.MigsEu_temp = Slot(uri=MIXS['0000113'], name="MigsEu_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.MigsEu_temp, domain=None, range=Optional[str])

slots.MigsEu_trophic_level = Slot(uri=MIXS['0000032'], name="MigsEu_trophic_level", curie=MIXS.curie('0000032'),
                   model_uri=MIXS.MigsEu_trophic_level, domain=None, range=Optional[str])

slots.MigsOrg_adapters = Slot(uri=MIXS['0000048'], name="MigsOrg_adapters", curie=MIXS.curie('0000048'),
                   model_uri=MIXS.MigsOrg_adapters, domain=None, range=Optional[str])

slots.MigsOrg_alt = Slot(uri=MIXS['0000094'], name="MigsOrg_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.MigsOrg_alt, domain=None, range=Optional[str])

slots.MigsOrg_annot = Slot(uri=MIXS['0000059'], name="MigsOrg_annot", curie=MIXS.curie('0000059'),
                   model_uri=MIXS.MigsOrg_annot, domain=None, range=Optional[str])

slots.MigsOrg_assembly_name = Slot(uri=MIXS['0000057'], name="MigsOrg_assembly_name", curie=MIXS.curie('0000057'),
                   model_uri=MIXS.MigsOrg_assembly_name, domain=None, range=Optional[str])

slots.MigsOrg_assembly_qual = Slot(uri=MIXS['0000056'], name="MigsOrg_assembly_qual", curie=MIXS.curie('0000056'),
                   model_uri=MIXS.MigsOrg_assembly_qual, domain=None, range=Optional[str])

slots.MigsOrg_assembly_software = Slot(uri=MIXS['0000058'], name="MigsOrg_assembly_software", curie=MIXS.curie('0000058'),
                   model_uri=MIXS.MigsOrg_assembly_software, domain=None, range=str)

slots.MigsOrg_associated_resource = Slot(uri=MIXS['0000091'], name="MigsOrg_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.MigsOrg_associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsOrg_collection_date = Slot(uri=MIXS['0000011'], name="MigsOrg_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.MigsOrg_collection_date, domain=None, range=str)

slots.MigsOrg_compl_score = Slot(uri=MIXS['0000069'], name="MigsOrg_compl_score", curie=MIXS.curie('0000069'),
                   model_uri=MIXS.MigsOrg_compl_score, domain=None, range=Optional[str])

slots.MigsOrg_compl_software = Slot(uri=MIXS['0000070'], name="MigsOrg_compl_software", curie=MIXS.curie('0000070'),
                   model_uri=MIXS.MigsOrg_compl_software, domain=None, range=Optional[str])

slots.MigsOrg_depth = Slot(uri=MIXS['0000018'], name="MigsOrg_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.MigsOrg_depth, domain=None, range=Optional[str])

slots.MigsOrg_elev = Slot(uri=MIXS['0000093'], name="MigsOrg_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.MigsOrg_elev, domain=None, range=Optional[str])

slots.MigsOrg_env_broad_scale = Slot(uri=MIXS['0000012'], name="MigsOrg_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.MigsOrg_env_broad_scale, domain=None, range=str)

slots.MigsOrg_env_local_scale = Slot(uri=MIXS['0000013'], name="MigsOrg_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.MigsOrg_env_local_scale, domain=None, range=str)

slots.MigsOrg_env_medium = Slot(uri=MIXS['0000014'], name="MigsOrg_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.MigsOrg_env_medium, domain=None, range=str)

slots.MigsOrg_estimated_size = Slot(uri=MIXS['0000024'], name="MigsOrg_estimated_size", curie=MIXS.curie('0000024'),
                   model_uri=MIXS.MigsOrg_estimated_size, domain=None, range=Optional[str])

slots.MigsOrg_experimental_factor = Slot(uri=MIXS['0000008'], name="MigsOrg_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.MigsOrg_experimental_factor, domain=None, range=Optional[str])

slots.MigsOrg_extrachrom_elements = Slot(uri=MIXS['0000023'], name="MigsOrg_extrachrom_elements", curie=MIXS.curie('0000023'),
                   model_uri=MIXS.MigsOrg_extrachrom_elements, domain=None, range=Optional[str])

slots.MigsOrg_feat_pred = Slot(uri=MIXS['0000061'], name="MigsOrg_feat_pred", curie=MIXS.curie('0000061'),
                   model_uri=MIXS.MigsOrg_feat_pred, domain=None, range=Optional[str])

slots.MigsOrg_geo_loc_name = Slot(uri=MIXS['0000010'], name="MigsOrg_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.MigsOrg_geo_loc_name, domain=None, range=str)

slots.MigsOrg_isol_growth_condt = Slot(uri=MIXS['0000003'], name="MigsOrg_isol_growth_condt", curie=MIXS.curie('0000003'),
                   model_uri=MIXS.MigsOrg_isol_growth_condt, domain=None, range=str)

slots.MigsOrg_lat_lon = Slot(uri=MIXS['0000009'], name="MigsOrg_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.MigsOrg_lat_lon, domain=None, range=str)

slots.MigsOrg_lib_layout = Slot(uri=MIXS['0000041'], name="MigsOrg_lib_layout", curie=MIXS.curie('0000041'),
                   model_uri=MIXS.MigsOrg_lib_layout, domain=None, range=Optional[str])

slots.MigsOrg_lib_reads_seqd = Slot(uri=MIXS['0000040'], name="MigsOrg_lib_reads_seqd", curie=MIXS.curie('0000040'),
                   model_uri=MIXS.MigsOrg_lib_reads_seqd, domain=None, range=Optional[str])

slots.MigsOrg_lib_screen = Slot(uri=MIXS['0000043'], name="MigsOrg_lib_screen", curie=MIXS.curie('0000043'),
                   model_uri=MIXS.MigsOrg_lib_screen, domain=None, range=Optional[str])

slots.MigsOrg_lib_size = Slot(uri=MIXS['0000039'], name="MigsOrg_lib_size", curie=MIXS.curie('0000039'),
                   model_uri=MIXS.MigsOrg_lib_size, domain=None, range=Optional[str])

slots.MigsOrg_lib_vector = Slot(uri=MIXS['0000042'], name="MigsOrg_lib_vector", curie=MIXS.curie('0000042'),
                   model_uri=MIXS.MigsOrg_lib_vector, domain=None, range=Optional[str])

slots.MigsOrg_neg_cont_type = Slot(uri=MIXS['0001321'], name="MigsOrg_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.MigsOrg_neg_cont_type, domain=None, range=Optional[str])

slots.MigsOrg_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="MigsOrg_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.MigsOrg_nucl_acid_amp, domain=None, range=Optional[str])

slots.MigsOrg_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="MigsOrg_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.MigsOrg_nucl_acid_ext, domain=None, range=Optional[str])

slots.MigsOrg_number_contig = Slot(uri=MIXS['0000060'], name="MigsOrg_number_contig", curie=MIXS.curie('0000060'),
                   model_uri=MIXS.MigsOrg_number_contig, domain=None, range=Optional[str])

slots.MigsOrg_pos_cont_type = Slot(uri=MIXS['0001322'], name="MigsOrg_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.MigsOrg_pos_cont_type, domain=None, range=Optional[str])

slots.MigsOrg_project_name = Slot(uri=MIXS['0000092'], name="MigsOrg_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.MigsOrg_project_name, domain=None, range=str)

slots.MigsOrg_ref_biomaterial = Slot(uri=MIXS['0000025'], name="MigsOrg_ref_biomaterial", curie=MIXS.curie('0000025'),
                   model_uri=MIXS.MigsOrg_ref_biomaterial, domain=None, range=Optional[str])

slots.MigsOrg_ref_db = Slot(uri=MIXS['0000062'], name="MigsOrg_ref_db", curie=MIXS.curie('0000062'),
                   model_uri=MIXS.MigsOrg_ref_db, domain=None, range=Optional[str])

slots.MigsOrg_samp_collec_device = Slot(uri=MIXS['0000002'], name="MigsOrg_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.MigsOrg_samp_collec_device, domain=None, range=Optional[str])

slots.MigsOrg_samp_collec_method = Slot(uri=MIXS['0001225'], name="MigsOrg_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.MigsOrg_samp_collec_method, domain=None, range=Optional[str])

slots.MigsOrg_samp_mat_process = Slot(uri=MIXS['0000016'], name="MigsOrg_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.MigsOrg_samp_mat_process, domain=None, range=Optional[str])

slots.MigsOrg_samp_name = Slot(uri=MIXS['0001107'], name="MigsOrg_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.MigsOrg_samp_name, domain=None, range=str)

slots.MigsOrg_samp_size = Slot(uri=MIXS['0000001'], name="MigsOrg_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.MigsOrg_samp_size, domain=None, range=Optional[str])

slots.MigsOrg_samp_taxon_id = Slot(uri=MIXS['0001320'], name="MigsOrg_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.MigsOrg_samp_taxon_id, domain=None, range=str)

slots.MigsOrg_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="MigsOrg_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.MigsOrg_samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.MigsOrg_seq_meth = Slot(uri=MIXS['0000050'], name="MigsOrg_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.MigsOrg_seq_meth, domain=None, range=str)

slots.MigsOrg_sim_search_meth = Slot(uri=MIXS['0000063'], name="MigsOrg_sim_search_meth", curie=MIXS.curie('0000063'),
                   model_uri=MIXS.MigsOrg_sim_search_meth, domain=None, range=Optional[str])

slots.MigsOrg_sop = Slot(uri=MIXS['0000090'], name="MigsOrg_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.MigsOrg_sop, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsOrg_source_mat_id = Slot(uri=MIXS['0000026'], name="MigsOrg_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.MigsOrg_source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsOrg_subspecf_gen_lin = Slot(uri=MIXS['0000020'], name="MigsOrg_subspecf_gen_lin", curie=MIXS.curie('0000020'),
                   model_uri=MIXS.MigsOrg_subspecf_gen_lin, domain=None, range=Optional[str])

slots.MigsOrg_tax_class = Slot(uri=MIXS['0000064'], name="MigsOrg_tax_class", curie=MIXS.curie('0000064'),
                   model_uri=MIXS.MigsOrg_tax_class, domain=None, range=Optional[str])

slots.MigsOrg_tax_ident = Slot(uri=MIXS['0000053'], name="MigsOrg_tax_ident", curie=MIXS.curie('0000053'),
                   model_uri=MIXS.MigsOrg_tax_ident, domain=None, range=Optional[str])

slots.MigsOrg_temp = Slot(uri=MIXS['0000113'], name="MigsOrg_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.MigsOrg_temp, domain=None, range=Optional[str])

slots.MigsPl_adapters = Slot(uri=MIXS['0000048'], name="MigsPl_adapters", curie=MIXS.curie('0000048'),
                   model_uri=MIXS.MigsPl_adapters, domain=None, range=Optional[str])

slots.MigsPl_alt = Slot(uri=MIXS['0000094'], name="MigsPl_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.MigsPl_alt, domain=None, range=Optional[str])

slots.MigsPl_annot = Slot(uri=MIXS['0000059'], name="MigsPl_annot", curie=MIXS.curie('0000059'),
                   model_uri=MIXS.MigsPl_annot, domain=None, range=Optional[str])

slots.MigsPl_assembly_name = Slot(uri=MIXS['0000057'], name="MigsPl_assembly_name", curie=MIXS.curie('0000057'),
                   model_uri=MIXS.MigsPl_assembly_name, domain=None, range=Optional[str])

slots.MigsPl_assembly_qual = Slot(uri=MIXS['0000056'], name="MigsPl_assembly_qual", curie=MIXS.curie('0000056'),
                   model_uri=MIXS.MigsPl_assembly_qual, domain=None, range=Optional[str])

slots.MigsPl_assembly_software = Slot(uri=MIXS['0000058'], name="MigsPl_assembly_software", curie=MIXS.curie('0000058'),
                   model_uri=MIXS.MigsPl_assembly_software, domain=None, range=str)

slots.MigsPl_associated_resource = Slot(uri=MIXS['0000091'], name="MigsPl_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.MigsPl_associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsPl_collection_date = Slot(uri=MIXS['0000011'], name="MigsPl_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.MigsPl_collection_date, domain=None, range=str)

slots.MigsPl_compl_score = Slot(uri=MIXS['0000069'], name="MigsPl_compl_score", curie=MIXS.curie('0000069'),
                   model_uri=MIXS.MigsPl_compl_score, domain=None, range=Optional[str])

slots.MigsPl_compl_software = Slot(uri=MIXS['0000070'], name="MigsPl_compl_software", curie=MIXS.curie('0000070'),
                   model_uri=MIXS.MigsPl_compl_software, domain=None, range=Optional[str])

slots.MigsPl_depth = Slot(uri=MIXS['0000018'], name="MigsPl_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.MigsPl_depth, domain=None, range=Optional[str])

slots.MigsPl_elev = Slot(uri=MIXS['0000093'], name="MigsPl_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.MigsPl_elev, domain=None, range=Optional[str])

slots.MigsPl_encoded_traits = Slot(uri=MIXS['0000034'], name="MigsPl_encoded_traits", curie=MIXS.curie('0000034'),
                   model_uri=MIXS.MigsPl_encoded_traits, domain=None, range=Optional[str])

slots.MigsPl_env_broad_scale = Slot(uri=MIXS['0000012'], name="MigsPl_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.MigsPl_env_broad_scale, domain=None, range=str)

slots.MigsPl_env_local_scale = Slot(uri=MIXS['0000013'], name="MigsPl_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.MigsPl_env_local_scale, domain=None, range=str)

slots.MigsPl_env_medium = Slot(uri=MIXS['0000014'], name="MigsPl_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.MigsPl_env_medium, domain=None, range=str)

slots.MigsPl_estimated_size = Slot(uri=MIXS['0000024'], name="MigsPl_estimated_size", curie=MIXS.curie('0000024'),
                   model_uri=MIXS.MigsPl_estimated_size, domain=None, range=Optional[str])

slots.MigsPl_experimental_factor = Slot(uri=MIXS['0000008'], name="MigsPl_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.MigsPl_experimental_factor, domain=None, range=Optional[str])

slots.MigsPl_feat_pred = Slot(uri=MIXS['0000061'], name="MigsPl_feat_pred", curie=MIXS.curie('0000061'),
                   model_uri=MIXS.MigsPl_feat_pred, domain=None, range=Optional[str])

slots.MigsPl_geo_loc_name = Slot(uri=MIXS['0000010'], name="MigsPl_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.MigsPl_geo_loc_name, domain=None, range=str)

slots.MigsPl_host_spec_range = Slot(uri=MIXS['0000030'], name="MigsPl_host_spec_range", curie=MIXS.curie('0000030'),
                   model_uri=MIXS.MigsPl_host_spec_range, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsPl_isol_growth_condt = Slot(uri=MIXS['0000003'], name="MigsPl_isol_growth_condt", curie=MIXS.curie('0000003'),
                   model_uri=MIXS.MigsPl_isol_growth_condt, domain=None, range=str)

slots.MigsPl_lat_lon = Slot(uri=MIXS['0000009'], name="MigsPl_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.MigsPl_lat_lon, domain=None, range=str)

slots.MigsPl_lib_layout = Slot(uri=MIXS['0000041'], name="MigsPl_lib_layout", curie=MIXS.curie('0000041'),
                   model_uri=MIXS.MigsPl_lib_layout, domain=None, range=Optional[str])

slots.MigsPl_lib_reads_seqd = Slot(uri=MIXS['0000040'], name="MigsPl_lib_reads_seqd", curie=MIXS.curie('0000040'),
                   model_uri=MIXS.MigsPl_lib_reads_seqd, domain=None, range=Optional[str])

slots.MigsPl_lib_screen = Slot(uri=MIXS['0000043'], name="MigsPl_lib_screen", curie=MIXS.curie('0000043'),
                   model_uri=MIXS.MigsPl_lib_screen, domain=None, range=Optional[str])

slots.MigsPl_lib_size = Slot(uri=MIXS['0000039'], name="MigsPl_lib_size", curie=MIXS.curie('0000039'),
                   model_uri=MIXS.MigsPl_lib_size, domain=None, range=Optional[str])

slots.MigsPl_lib_vector = Slot(uri=MIXS['0000042'], name="MigsPl_lib_vector", curie=MIXS.curie('0000042'),
                   model_uri=MIXS.MigsPl_lib_vector, domain=None, range=Optional[str])

slots.MigsPl_neg_cont_type = Slot(uri=MIXS['0001321'], name="MigsPl_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.MigsPl_neg_cont_type, domain=None, range=Optional[str])

slots.MigsPl_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="MigsPl_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.MigsPl_nucl_acid_amp, domain=None, range=Optional[str])

slots.MigsPl_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="MigsPl_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.MigsPl_nucl_acid_ext, domain=None, range=Optional[str])

slots.MigsPl_number_contig = Slot(uri=MIXS['0000060'], name="MigsPl_number_contig", curie=MIXS.curie('0000060'),
                   model_uri=MIXS.MigsPl_number_contig, domain=None, range=Optional[str])

slots.MigsPl_pos_cont_type = Slot(uri=MIXS['0001322'], name="MigsPl_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.MigsPl_pos_cont_type, domain=None, range=Optional[str])

slots.MigsPl_project_name = Slot(uri=MIXS['0000092'], name="MigsPl_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.MigsPl_project_name, domain=None, range=str)

slots.MigsPl_propagation = Slot(uri=MIXS['0000033'], name="MigsPl_propagation", curie=MIXS.curie('0000033'),
                   model_uri=MIXS.MigsPl_propagation, domain=None, range=str)

slots.MigsPl_ref_biomaterial = Slot(uri=MIXS['0000025'], name="MigsPl_ref_biomaterial", curie=MIXS.curie('0000025'),
                   model_uri=MIXS.MigsPl_ref_biomaterial, domain=None, range=Optional[str])

slots.MigsPl_ref_db = Slot(uri=MIXS['0000062'], name="MigsPl_ref_db", curie=MIXS.curie('0000062'),
                   model_uri=MIXS.MigsPl_ref_db, domain=None, range=Optional[str])

slots.MigsPl_samp_collec_device = Slot(uri=MIXS['0000002'], name="MigsPl_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.MigsPl_samp_collec_device, domain=None, range=Optional[str])

slots.MigsPl_samp_collec_method = Slot(uri=MIXS['0001225'], name="MigsPl_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.MigsPl_samp_collec_method, domain=None, range=Optional[str])

slots.MigsPl_samp_mat_process = Slot(uri=MIXS['0000016'], name="MigsPl_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.MigsPl_samp_mat_process, domain=None, range=Optional[str])

slots.MigsPl_samp_name = Slot(uri=MIXS['0001107'], name="MigsPl_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.MigsPl_samp_name, domain=None, range=str)

slots.MigsPl_samp_size = Slot(uri=MIXS['0000001'], name="MigsPl_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.MigsPl_samp_size, domain=None, range=Optional[str])

slots.MigsPl_samp_taxon_id = Slot(uri=MIXS['0001320'], name="MigsPl_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.MigsPl_samp_taxon_id, domain=None, range=str)

slots.MigsPl_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="MigsPl_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.MigsPl_samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.MigsPl_seq_meth = Slot(uri=MIXS['0000050'], name="MigsPl_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.MigsPl_seq_meth, domain=None, range=str)

slots.MigsPl_sim_search_meth = Slot(uri=MIXS['0000063'], name="MigsPl_sim_search_meth", curie=MIXS.curie('0000063'),
                   model_uri=MIXS.MigsPl_sim_search_meth, domain=None, range=Optional[str])

slots.MigsPl_sop = Slot(uri=MIXS['0000090'], name="MigsPl_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.MigsPl_sop, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsPl_source_mat_id = Slot(uri=MIXS['0000026'], name="MigsPl_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.MigsPl_source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsPl_specific_host = Slot(uri=MIXS['0000029'], name="MigsPl_specific_host", curie=MIXS.curie('0000029'),
                   model_uri=MIXS.MigsPl_specific_host, domain=None, range=Optional[str])

slots.MigsPl_subspecf_gen_lin = Slot(uri=MIXS['0000020'], name="MigsPl_subspecf_gen_lin", curie=MIXS.curie('0000020'),
                   model_uri=MIXS.MigsPl_subspecf_gen_lin, domain=None, range=Optional[str])

slots.MigsPl_tax_class = Slot(uri=MIXS['0000064'], name="MigsPl_tax_class", curie=MIXS.curie('0000064'),
                   model_uri=MIXS.MigsPl_tax_class, domain=None, range=Optional[str])

slots.MigsPl_tax_ident = Slot(uri=MIXS['0000053'], name="MigsPl_tax_ident", curie=MIXS.curie('0000053'),
                   model_uri=MIXS.MigsPl_tax_ident, domain=None, range=Optional[str])

slots.MigsPl_temp = Slot(uri=MIXS['0000113'], name="MigsPl_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.MigsPl_temp, domain=None, range=Optional[str])

slots.MigsVi_adapters = Slot(uri=MIXS['0000048'], name="MigsVi_adapters", curie=MIXS.curie('0000048'),
                   model_uri=MIXS.MigsVi_adapters, domain=None, range=Optional[str])

slots.MigsVi_alt = Slot(uri=MIXS['0000094'], name="MigsVi_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.MigsVi_alt, domain=None, range=Optional[str])

slots.MigsVi_annot = Slot(uri=MIXS['0000059'], name="MigsVi_annot", curie=MIXS.curie('0000059'),
                   model_uri=MIXS.MigsVi_annot, domain=None, range=Optional[str])

slots.MigsVi_assembly_name = Slot(uri=MIXS['0000057'], name="MigsVi_assembly_name", curie=MIXS.curie('0000057'),
                   model_uri=MIXS.MigsVi_assembly_name, domain=None, range=Optional[str])

slots.MigsVi_assembly_qual = Slot(uri=MIXS['0000056'], name="MigsVi_assembly_qual", curie=MIXS.curie('0000056'),
                   model_uri=MIXS.MigsVi_assembly_qual, domain=None, range=Optional[str])

slots.MigsVi_assembly_software = Slot(uri=MIXS['0000058'], name="MigsVi_assembly_software", curie=MIXS.curie('0000058'),
                   model_uri=MIXS.MigsVi_assembly_software, domain=None, range=str)

slots.MigsVi_associated_resource = Slot(uri=MIXS['0000091'], name="MigsVi_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.MigsVi_associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsVi_biotic_relationship = Slot(uri=MIXS['0000028'], name="MigsVi_biotic_relationship", curie=MIXS.curie('0000028'),
                   model_uri=MIXS.MigsVi_biotic_relationship, domain=None, range=Optional[str])

slots.MigsVi_collection_date = Slot(uri=MIXS['0000011'], name="MigsVi_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.MigsVi_collection_date, domain=None, range=str)

slots.MigsVi_compl_score = Slot(uri=MIXS['0000069'], name="MigsVi_compl_score", curie=MIXS.curie('0000069'),
                   model_uri=MIXS.MigsVi_compl_score, domain=None, range=Optional[str])

slots.MigsVi_compl_software = Slot(uri=MIXS['0000070'], name="MigsVi_compl_software", curie=MIXS.curie('0000070'),
                   model_uri=MIXS.MigsVi_compl_software, domain=None, range=Optional[str])

slots.MigsVi_depth = Slot(uri=MIXS['0000018'], name="MigsVi_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.MigsVi_depth, domain=None, range=Optional[str])

slots.MigsVi_elev = Slot(uri=MIXS['0000093'], name="MigsVi_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.MigsVi_elev, domain=None, range=Optional[str])

slots.MigsVi_encoded_traits = Slot(uri=MIXS['0000034'], name="MigsVi_encoded_traits", curie=MIXS.curie('0000034'),
                   model_uri=MIXS.MigsVi_encoded_traits, domain=None, range=Optional[str])

slots.MigsVi_env_broad_scale = Slot(uri=MIXS['0000012'], name="MigsVi_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.MigsVi_env_broad_scale, domain=None, range=str)

slots.MigsVi_env_local_scale = Slot(uri=MIXS['0000013'], name="MigsVi_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.MigsVi_env_local_scale, domain=None, range=str)

slots.MigsVi_env_medium = Slot(uri=MIXS['0000014'], name="MigsVi_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.MigsVi_env_medium, domain=None, range=str)

slots.MigsVi_estimated_size = Slot(uri=MIXS['0000024'], name="MigsVi_estimated_size", curie=MIXS.curie('0000024'),
                   model_uri=MIXS.MigsVi_estimated_size, domain=None, range=Optional[str])

slots.MigsVi_experimental_factor = Slot(uri=MIXS['0000008'], name="MigsVi_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.MigsVi_experimental_factor, domain=None, range=Optional[str])

slots.MigsVi_feat_pred = Slot(uri=MIXS['0000061'], name="MigsVi_feat_pred", curie=MIXS.curie('0000061'),
                   model_uri=MIXS.MigsVi_feat_pred, domain=None, range=Optional[str])

slots.MigsVi_geo_loc_name = Slot(uri=MIXS['0000010'], name="MigsVi_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.MigsVi_geo_loc_name, domain=None, range=str)

slots.MigsVi_host_disease_stat = Slot(uri=MIXS['0000031'], name="MigsVi_host_disease_stat", curie=MIXS.curie('0000031'),
                   model_uri=MIXS.MigsVi_host_disease_stat, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsVi_host_spec_range = Slot(uri=MIXS['0000030'], name="MigsVi_host_spec_range", curie=MIXS.curie('0000030'),
                   model_uri=MIXS.MigsVi_host_spec_range, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsVi_isol_growth_condt = Slot(uri=MIXS['0000003'], name="MigsVi_isol_growth_condt", curie=MIXS.curie('0000003'),
                   model_uri=MIXS.MigsVi_isol_growth_condt, domain=None, range=str)

slots.MigsVi_lat_lon = Slot(uri=MIXS['0000009'], name="MigsVi_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.MigsVi_lat_lon, domain=None, range=str)

slots.MigsVi_lib_layout = Slot(uri=MIXS['0000041'], name="MigsVi_lib_layout", curie=MIXS.curie('0000041'),
                   model_uri=MIXS.MigsVi_lib_layout, domain=None, range=Optional[str])

slots.MigsVi_lib_reads_seqd = Slot(uri=MIXS['0000040'], name="MigsVi_lib_reads_seqd", curie=MIXS.curie('0000040'),
                   model_uri=MIXS.MigsVi_lib_reads_seqd, domain=None, range=Optional[str])

slots.MigsVi_lib_screen = Slot(uri=MIXS['0000043'], name="MigsVi_lib_screen", curie=MIXS.curie('0000043'),
                   model_uri=MIXS.MigsVi_lib_screen, domain=None, range=Optional[str])

slots.MigsVi_lib_size = Slot(uri=MIXS['0000039'], name="MigsVi_lib_size", curie=MIXS.curie('0000039'),
                   model_uri=MIXS.MigsVi_lib_size, domain=None, range=Optional[str])

slots.MigsVi_lib_vector = Slot(uri=MIXS['0000042'], name="MigsVi_lib_vector", curie=MIXS.curie('0000042'),
                   model_uri=MIXS.MigsVi_lib_vector, domain=None, range=Optional[str])

slots.MigsVi_neg_cont_type = Slot(uri=MIXS['0001321'], name="MigsVi_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.MigsVi_neg_cont_type, domain=None, range=Optional[str])

slots.MigsVi_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="MigsVi_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.MigsVi_nucl_acid_amp, domain=None, range=Optional[str])

slots.MigsVi_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="MigsVi_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.MigsVi_nucl_acid_ext, domain=None, range=Optional[str])

slots.MigsVi_num_replicons = Slot(uri=MIXS['0000022'], name="MigsVi_num_replicons", curie=MIXS.curie('0000022'),
                   model_uri=MIXS.MigsVi_num_replicons, domain=None, range=Optional[str])

slots.MigsVi_number_contig = Slot(uri=MIXS['0000060'], name="MigsVi_number_contig", curie=MIXS.curie('0000060'),
                   model_uri=MIXS.MigsVi_number_contig, domain=None, range=Optional[str])

slots.MigsVi_pathogenicity = Slot(uri=MIXS['0000027'], name="MigsVi_pathogenicity", curie=MIXS.curie('0000027'),
                   model_uri=MIXS.MigsVi_pathogenicity, domain=None, range=Optional[str])

slots.MigsVi_pos_cont_type = Slot(uri=MIXS['0001322'], name="MigsVi_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.MigsVi_pos_cont_type, domain=None, range=Optional[str])

slots.MigsVi_project_name = Slot(uri=MIXS['0000092'], name="MigsVi_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.MigsVi_project_name, domain=None, range=str)

slots.MigsVi_propagation = Slot(uri=MIXS['0000033'], name="MigsVi_propagation", curie=MIXS.curie('0000033'),
                   model_uri=MIXS.MigsVi_propagation, domain=None, range=str)

slots.MigsVi_ref_biomaterial = Slot(uri=MIXS['0000025'], name="MigsVi_ref_biomaterial", curie=MIXS.curie('0000025'),
                   model_uri=MIXS.MigsVi_ref_biomaterial, domain=None, range=Optional[str])

slots.MigsVi_ref_db = Slot(uri=MIXS['0000062'], name="MigsVi_ref_db", curie=MIXS.curie('0000062'),
                   model_uri=MIXS.MigsVi_ref_db, domain=None, range=Optional[str])

slots.MigsVi_samp_collec_device = Slot(uri=MIXS['0000002'], name="MigsVi_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.MigsVi_samp_collec_device, domain=None, range=Optional[str])

slots.MigsVi_samp_collec_method = Slot(uri=MIXS['0001225'], name="MigsVi_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.MigsVi_samp_collec_method, domain=None, range=Optional[str])

slots.MigsVi_samp_mat_process = Slot(uri=MIXS['0000016'], name="MigsVi_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.MigsVi_samp_mat_process, domain=None, range=Optional[str])

slots.MigsVi_samp_name = Slot(uri=MIXS['0001107'], name="MigsVi_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.MigsVi_samp_name, domain=None, range=str)

slots.MigsVi_samp_size = Slot(uri=MIXS['0000001'], name="MigsVi_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.MigsVi_samp_size, domain=None, range=Optional[str])

slots.MigsVi_samp_taxon_id = Slot(uri=MIXS['0001320'], name="MigsVi_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.MigsVi_samp_taxon_id, domain=None, range=str)

slots.MigsVi_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="MigsVi_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.MigsVi_samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.MigsVi_seq_meth = Slot(uri=MIXS['0000050'], name="MigsVi_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.MigsVi_seq_meth, domain=None, range=str)

slots.MigsVi_sim_search_meth = Slot(uri=MIXS['0000063'], name="MigsVi_sim_search_meth", curie=MIXS.curie('0000063'),
                   model_uri=MIXS.MigsVi_sim_search_meth, domain=None, range=Optional[str])

slots.MigsVi_sop = Slot(uri=MIXS['0000090'], name="MigsVi_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.MigsVi_sop, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsVi_source_mat_id = Slot(uri=MIXS['0000026'], name="MigsVi_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.MigsVi_source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.MigsVi_specific_host = Slot(uri=MIXS['0000029'], name="MigsVi_specific_host", curie=MIXS.curie('0000029'),
                   model_uri=MIXS.MigsVi_specific_host, domain=None, range=Optional[str])

slots.MigsVi_subspecf_gen_lin = Slot(uri=MIXS['0000020'], name="MigsVi_subspecf_gen_lin", curie=MIXS.curie('0000020'),
                   model_uri=MIXS.MigsVi_subspecf_gen_lin, domain=None, range=Optional[str])

slots.MigsVi_tax_class = Slot(uri=MIXS['0000064'], name="MigsVi_tax_class", curie=MIXS.curie('0000064'),
                   model_uri=MIXS.MigsVi_tax_class, domain=None, range=Optional[str])

slots.MigsVi_tax_ident = Slot(uri=MIXS['0000053'], name="MigsVi_tax_ident", curie=MIXS.curie('0000053'),
                   model_uri=MIXS.MigsVi_tax_ident, domain=None, range=Optional[str])

slots.MigsVi_temp = Slot(uri=MIXS['0000113'], name="MigsVi_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.MigsVi_temp, domain=None, range=Optional[str])

slots.MigsVi_virus_enrich_appr = Slot(uri=MIXS['0000036'], name="MigsVi_virus_enrich_appr", curie=MIXS.curie('0000036'),
                   model_uri=MIXS.MigsVi_virus_enrich_appr, domain=None, range=Optional[str])

slots.Mimag_x_16s_recover = Slot(uri=MIXS['0000065'], name="Mimag_x_16s_recover", curie=MIXS.curie('0000065'),
                   model_uri=MIXS.Mimag_x_16s_recover, domain=None, range=Optional[str])

slots.Mimag_x_16s_recover_software = Slot(uri=MIXS['0000066'], name="Mimag_x_16s_recover_software", curie=MIXS.curie('0000066'),
                   model_uri=MIXS.Mimag_x_16s_recover_software, domain=None, range=Optional[str])

slots.Mimag_adapters = Slot(uri=MIXS['0000048'], name="Mimag_adapters", curie=MIXS.curie('0000048'),
                   model_uri=MIXS.Mimag_adapters, domain=None, range=Optional[str])

slots.Mimag_alt = Slot(uri=MIXS['0000094'], name="Mimag_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.Mimag_alt, domain=None, range=Optional[str])

slots.Mimag_annot = Slot(uri=MIXS['0000059'], name="Mimag_annot", curie=MIXS.curie('0000059'),
                   model_uri=MIXS.Mimag_annot, domain=None, range=Optional[str])

slots.Mimag_assembly_name = Slot(uri=MIXS['0000057'], name="Mimag_assembly_name", curie=MIXS.curie('0000057'),
                   model_uri=MIXS.Mimag_assembly_name, domain=None, range=Optional[str])

slots.Mimag_assembly_qual = Slot(uri=MIXS['0000056'], name="Mimag_assembly_qual", curie=MIXS.curie('0000056'),
                   model_uri=MIXS.Mimag_assembly_qual, domain=None, range=str)

slots.Mimag_assembly_software = Slot(uri=MIXS['0000058'], name="Mimag_assembly_software", curie=MIXS.curie('0000058'),
                   model_uri=MIXS.Mimag_assembly_software, domain=None, range=str)

slots.Mimag_associated_resource = Slot(uri=MIXS['0000091'], name="Mimag_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.Mimag_associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.Mimag_bin_param = Slot(uri=MIXS['0000077'], name="Mimag_bin_param", curie=MIXS.curie('0000077'),
                   model_uri=MIXS.Mimag_bin_param, domain=None, range=str)

slots.Mimag_bin_software = Slot(uri=MIXS['0000078'], name="Mimag_bin_software", curie=MIXS.curie('0000078'),
                   model_uri=MIXS.Mimag_bin_software, domain=None, range=str)

slots.Mimag_collection_date = Slot(uri=MIXS['0000011'], name="Mimag_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.Mimag_collection_date, domain=None, range=str)

slots.Mimag_compl_appr = Slot(uri=MIXS['0000071'], name="Mimag_compl_appr", curie=MIXS.curie('0000071'),
                   model_uri=MIXS.Mimag_compl_appr, domain=None, range=Optional[str])

slots.Mimag_compl_score = Slot(uri=MIXS['0000069'], name="Mimag_compl_score", curie=MIXS.curie('0000069'),
                   model_uri=MIXS.Mimag_compl_score, domain=None, range=str)

slots.Mimag_compl_software = Slot(uri=MIXS['0000070'], name="Mimag_compl_software", curie=MIXS.curie('0000070'),
                   model_uri=MIXS.Mimag_compl_software, domain=None, range=str)

slots.Mimag_contam_score = Slot(uri=MIXS['0000072'], name="Mimag_contam_score", curie=MIXS.curie('0000072'),
                   model_uri=MIXS.Mimag_contam_score, domain=None, range=str)

slots.Mimag_contam_screen_input = Slot(uri=MIXS['0000005'], name="Mimag_contam_screen_input", curie=MIXS.curie('0000005'),
                   model_uri=MIXS.Mimag_contam_screen_input, domain=None, range=Optional[str])

slots.Mimag_contam_screen_param = Slot(uri=MIXS['0000073'], name="Mimag_contam_screen_param", curie=MIXS.curie('0000073'),
                   model_uri=MIXS.Mimag_contam_screen_param, domain=None, range=Optional[str])

slots.Mimag_decontam_software = Slot(uri=MIXS['0000074'], name="Mimag_decontam_software", curie=MIXS.curie('0000074'),
                   model_uri=MIXS.Mimag_decontam_software, domain=None, range=Optional[str])

slots.Mimag_depth = Slot(uri=MIXS['0000018'], name="Mimag_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.Mimag_depth, domain=None, range=Optional[str])

slots.Mimag_elev = Slot(uri=MIXS['0000093'], name="Mimag_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.Mimag_elev, domain=None, range=Optional[str])

slots.Mimag_env_broad_scale = Slot(uri=MIXS['0000012'], name="Mimag_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.Mimag_env_broad_scale, domain=None, range=str)

slots.Mimag_env_local_scale = Slot(uri=MIXS['0000013'], name="Mimag_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.Mimag_env_local_scale, domain=None, range=str)

slots.Mimag_env_medium = Slot(uri=MIXS['0000014'], name="Mimag_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.Mimag_env_medium, domain=None, range=str)

slots.Mimag_experimental_factor = Slot(uri=MIXS['0000008'], name="Mimag_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.Mimag_experimental_factor, domain=None, range=Optional[str])

slots.Mimag_feat_pred = Slot(uri=MIXS['0000061'], name="Mimag_feat_pred", curie=MIXS.curie('0000061'),
                   model_uri=MIXS.Mimag_feat_pred, domain=None, range=Optional[str])

slots.Mimag_geo_loc_name = Slot(uri=MIXS['0000010'], name="Mimag_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.Mimag_geo_loc_name, domain=None, range=str)

slots.Mimag_lat_lon = Slot(uri=MIXS['0000009'], name="Mimag_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.Mimag_lat_lon, domain=None, range=str)

slots.Mimag_lib_layout = Slot(uri=MIXS['0000041'], name="Mimag_lib_layout", curie=MIXS.curie('0000041'),
                   model_uri=MIXS.Mimag_lib_layout, domain=None, range=Optional[str])

slots.Mimag_lib_reads_seqd = Slot(uri=MIXS['0000040'], name="Mimag_lib_reads_seqd", curie=MIXS.curie('0000040'),
                   model_uri=MIXS.Mimag_lib_reads_seqd, domain=None, range=Optional[str])

slots.Mimag_lib_screen = Slot(uri=MIXS['0000043'], name="Mimag_lib_screen", curie=MIXS.curie('0000043'),
                   model_uri=MIXS.Mimag_lib_screen, domain=None, range=Optional[str])

slots.Mimag_lib_size = Slot(uri=MIXS['0000039'], name="Mimag_lib_size", curie=MIXS.curie('0000039'),
                   model_uri=MIXS.Mimag_lib_size, domain=None, range=Optional[str])

slots.Mimag_lib_vector = Slot(uri=MIXS['0000042'], name="Mimag_lib_vector", curie=MIXS.curie('0000042'),
                   model_uri=MIXS.Mimag_lib_vector, domain=None, range=Optional[str])

slots.Mimag_mag_cov_software = Slot(uri=MIXS['0000080'], name="Mimag_mag_cov_software", curie=MIXS.curie('0000080'),
                   model_uri=MIXS.Mimag_mag_cov_software, domain=None, range=Optional[str])

slots.Mimag_mid = Slot(uri=MIXS['0000047'], name="Mimag_mid", curie=MIXS.curie('0000047'),
                   model_uri=MIXS.Mimag_mid, domain=None, range=Optional[str])

slots.Mimag_neg_cont_type = Slot(uri=MIXS['0001321'], name="Mimag_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.Mimag_neg_cont_type, domain=None, range=Optional[str])

slots.Mimag_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="Mimag_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.Mimag_nucl_acid_amp, domain=None, range=Optional[str])

slots.Mimag_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="Mimag_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.Mimag_nucl_acid_ext, domain=None, range=Optional[str])

slots.Mimag_number_contig = Slot(uri=MIXS['0000060'], name="Mimag_number_contig", curie=MIXS.curie('0000060'),
                   model_uri=MIXS.Mimag_number_contig, domain=None, range=Optional[str])

slots.Mimag_pos_cont_type = Slot(uri=MIXS['0001322'], name="Mimag_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.Mimag_pos_cont_type, domain=None, range=Optional[str])

slots.Mimag_project_name = Slot(uri=MIXS['0000092'], name="Mimag_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.Mimag_project_name, domain=None, range=str)

slots.Mimag_reassembly_bin = Slot(uri=MIXS['0000079'], name="Mimag_reassembly_bin", curie=MIXS.curie('0000079'),
                   model_uri=MIXS.Mimag_reassembly_bin, domain=None, range=Optional[str])

slots.Mimag_ref_biomaterial = Slot(uri=MIXS['0000025'], name="Mimag_ref_biomaterial", curie=MIXS.curie('0000025'),
                   model_uri=MIXS.Mimag_ref_biomaterial, domain=None, range=Optional[str])

slots.Mimag_ref_db = Slot(uri=MIXS['0000062'], name="Mimag_ref_db", curie=MIXS.curie('0000062'),
                   model_uri=MIXS.Mimag_ref_db, domain=None, range=Optional[str])

slots.Mimag_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="Mimag_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=MIXS.Mimag_rel_to_oxygen, domain=None, range=Optional[str])

slots.Mimag_samp_collec_device = Slot(uri=MIXS['0000002'], name="Mimag_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.Mimag_samp_collec_device, domain=None, range=Optional[str])

slots.Mimag_samp_collec_method = Slot(uri=MIXS['0001225'], name="Mimag_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.Mimag_samp_collec_method, domain=None, range=Optional[str])

slots.Mimag_samp_mat_process = Slot(uri=MIXS['0000016'], name="Mimag_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.Mimag_samp_mat_process, domain=None, range=Optional[str])

slots.Mimag_samp_name = Slot(uri=MIXS['0001107'], name="Mimag_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.Mimag_samp_name, domain=None, range=str)

slots.Mimag_samp_size = Slot(uri=MIXS['0000001'], name="Mimag_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.Mimag_samp_size, domain=None, range=Optional[str])

slots.Mimag_samp_taxon_id = Slot(uri=MIXS['0001320'], name="Mimag_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.Mimag_samp_taxon_id, domain=None, range=str)

slots.Mimag_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="Mimag_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.Mimag_samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.Mimag_seq_meth = Slot(uri=MIXS['0000050'], name="Mimag_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.Mimag_seq_meth, domain=None, range=str)

slots.Mimag_sim_search_meth = Slot(uri=MIXS['0000063'], name="Mimag_sim_search_meth", curie=MIXS.curie('0000063'),
                   model_uri=MIXS.Mimag_sim_search_meth, domain=None, range=Optional[str])

slots.Mimag_size_frac = Slot(uri=MIXS['0000017'], name="Mimag_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=MIXS.Mimag_size_frac, domain=None, range=Optional[str])

slots.Mimag_sop = Slot(uri=MIXS['0000090'], name="Mimag_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.Mimag_sop, domain=None, range=Optional[Union[str, List[str]]])

slots.Mimag_source_mat_id = Slot(uri=MIXS['0000026'], name="Mimag_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.Mimag_source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.Mimag_tax_class = Slot(uri=MIXS['0000064'], name="Mimag_tax_class", curie=MIXS.curie('0000064'),
                   model_uri=MIXS.Mimag_tax_class, domain=None, range=Optional[str])

slots.Mimag_tax_ident = Slot(uri=MIXS['0000053'], name="Mimag_tax_ident", curie=MIXS.curie('0000053'),
                   model_uri=MIXS.Mimag_tax_ident, domain=None, range=str)

slots.Mimag_temp = Slot(uri=MIXS['0000113'], name="Mimag_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.Mimag_temp, domain=None, range=Optional[str])

slots.Mimag_trna_ext_software = Slot(uri=MIXS['0000068'], name="Mimag_trna_ext_software", curie=MIXS.curie('0000068'),
                   model_uri=MIXS.Mimag_trna_ext_software, domain=None, range=Optional[str])

slots.Mimag_trnas = Slot(uri=MIXS['0000067'], name="Mimag_trnas", curie=MIXS.curie('0000067'),
                   model_uri=MIXS.Mimag_trnas, domain=None, range=Optional[str])

slots.MimarksC_alt = Slot(uri=MIXS['0000094'], name="MimarksC_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.MimarksC_alt, domain=None, range=Optional[str])

slots.MimarksC_associated_resource = Slot(uri=MIXS['0000091'], name="MimarksC_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.MimarksC_associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.MimarksC_biotic_relationship = Slot(uri=MIXS['0000028'], name="MimarksC_biotic_relationship", curie=MIXS.curie('0000028'),
                   model_uri=MIXS.MimarksC_biotic_relationship, domain=None, range=Optional[str])

slots.MimarksC_chimera_check = Slot(uri=MIXS['0000052'], name="MimarksC_chimera_check", curie=MIXS.curie('0000052'),
                   model_uri=MIXS.MimarksC_chimera_check, domain=None, range=Optional[str])

slots.MimarksC_collection_date = Slot(uri=MIXS['0000011'], name="MimarksC_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.MimarksC_collection_date, domain=None, range=str)

slots.MimarksC_depth = Slot(uri=MIXS['0000018'], name="MimarksC_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.MimarksC_depth, domain=None, range=Optional[str])

slots.MimarksC_elev = Slot(uri=MIXS['0000093'], name="MimarksC_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.MimarksC_elev, domain=None, range=Optional[str])

slots.MimarksC_env_broad_scale = Slot(uri=MIXS['0000012'], name="MimarksC_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.MimarksC_env_broad_scale, domain=None, range=str)

slots.MimarksC_env_local_scale = Slot(uri=MIXS['0000013'], name="MimarksC_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.MimarksC_env_local_scale, domain=None, range=str)

slots.MimarksC_env_medium = Slot(uri=MIXS['0000014'], name="MimarksC_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.MimarksC_env_medium, domain=None, range=str)

slots.MimarksC_experimental_factor = Slot(uri=MIXS['0000008'], name="MimarksC_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.MimarksC_experimental_factor, domain=None, range=Optional[str])

slots.MimarksC_extrachrom_elements = Slot(uri=MIXS['0000023'], name="MimarksC_extrachrom_elements", curie=MIXS.curie('0000023'),
                   model_uri=MIXS.MimarksC_extrachrom_elements, domain=None, range=Optional[str])

slots.MimarksC_geo_loc_name = Slot(uri=MIXS['0000010'], name="MimarksC_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.MimarksC_geo_loc_name, domain=None, range=str)

slots.MimarksC_isol_growth_condt = Slot(uri=MIXS['0000003'], name="MimarksC_isol_growth_condt", curie=MIXS.curie('0000003'),
                   model_uri=MIXS.MimarksC_isol_growth_condt, domain=None, range=str)

slots.MimarksC_lat_lon = Slot(uri=MIXS['0000009'], name="MimarksC_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.MimarksC_lat_lon, domain=None, range=str)

slots.MimarksC_neg_cont_type = Slot(uri=MIXS['0001321'], name="MimarksC_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.MimarksC_neg_cont_type, domain=None, range=Optional[str])

slots.MimarksC_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="MimarksC_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.MimarksC_nucl_acid_amp, domain=None, range=Optional[str])

slots.MimarksC_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="MimarksC_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.MimarksC_nucl_acid_ext, domain=None, range=Optional[str])

slots.MimarksC_pcr_cond = Slot(uri=MIXS['0000049'], name="MimarksC_pcr_cond", curie=MIXS.curie('0000049'),
                   model_uri=MIXS.MimarksC_pcr_cond, domain=None, range=Optional[str])

slots.MimarksC_pcr_primers = Slot(uri=MIXS['0000046'], name="MimarksC_pcr_primers", curie=MIXS.curie('0000046'),
                   model_uri=MIXS.MimarksC_pcr_primers, domain=None, range=Optional[str])

slots.MimarksC_pos_cont_type = Slot(uri=MIXS['0001322'], name="MimarksC_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.MimarksC_pos_cont_type, domain=None, range=Optional[str])

slots.MimarksC_project_name = Slot(uri=MIXS['0000092'], name="MimarksC_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.MimarksC_project_name, domain=None, range=str)

slots.MimarksC_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="MimarksC_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=MIXS.MimarksC_rel_to_oxygen, domain=None, range=Optional[str])

slots.MimarksC_samp_collec_device = Slot(uri=MIXS['0000002'], name="MimarksC_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.MimarksC_samp_collec_device, domain=None, range=Optional[str])

slots.MimarksC_samp_collec_method = Slot(uri=MIXS['0001225'], name="MimarksC_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.MimarksC_samp_collec_method, domain=None, range=Optional[str])

slots.MimarksC_samp_mat_process = Slot(uri=MIXS['0000016'], name="MimarksC_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.MimarksC_samp_mat_process, domain=None, range=Optional[str])

slots.MimarksC_samp_name = Slot(uri=MIXS['0001107'], name="MimarksC_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.MimarksC_samp_name, domain=None, range=str)

slots.MimarksC_samp_size = Slot(uri=MIXS['0000001'], name="MimarksC_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.MimarksC_samp_size, domain=None, range=Optional[str])

slots.MimarksC_samp_taxon_id = Slot(uri=MIXS['0001320'], name="MimarksC_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.MimarksC_samp_taxon_id, domain=None, range=str)

slots.MimarksC_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="MimarksC_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.MimarksC_samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.MimarksC_seq_meth = Slot(uri=MIXS['0000050'], name="MimarksC_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.MimarksC_seq_meth, domain=None, range=str)

slots.MimarksC_seq_quality_check = Slot(uri=MIXS['0000051'], name="MimarksC_seq_quality_check", curie=MIXS.curie('0000051'),
                   model_uri=MIXS.MimarksC_seq_quality_check, domain=None, range=Optional[str])

slots.MimarksC_sop = Slot(uri=MIXS['0000090'], name="MimarksC_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.MimarksC_sop, domain=None, range=Optional[Union[str, List[str]]])

slots.MimarksC_source_mat_id = Slot(uri=MIXS['0000026'], name="MimarksC_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.MimarksC_source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.MimarksC_subspecf_gen_lin = Slot(uri=MIXS['0000020'], name="MimarksC_subspecf_gen_lin", curie=MIXS.curie('0000020'),
                   model_uri=MIXS.MimarksC_subspecf_gen_lin, domain=None, range=Optional[str])

slots.MimarksC_target_gene = Slot(uri=MIXS['0000044'], name="MimarksC_target_gene", curie=MIXS.curie('0000044'),
                   model_uri=MIXS.MimarksC_target_gene, domain=None, range=str)

slots.MimarksC_target_subfragment = Slot(uri=MIXS['0000045'], name="MimarksC_target_subfragment", curie=MIXS.curie('0000045'),
                   model_uri=MIXS.MimarksC_target_subfragment, domain=None, range=Optional[str])

slots.MimarksC_temp = Slot(uri=MIXS['0000113'], name="MimarksC_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.MimarksC_temp, domain=None, range=Optional[str])

slots.MimarksC_trophic_level = Slot(uri=MIXS['0000032'], name="MimarksC_trophic_level", curie=MIXS.curie('0000032'),
                   model_uri=MIXS.MimarksC_trophic_level, domain=None, range=Optional[str])

slots.MimarksS_adapters = Slot(uri=MIXS['0000048'], name="MimarksS_adapters", curie=MIXS.curie('0000048'),
                   model_uri=MIXS.MimarksS_adapters, domain=None, range=Optional[str])

slots.MimarksS_alt = Slot(uri=MIXS['0000094'], name="MimarksS_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.MimarksS_alt, domain=None, range=Optional[str])

slots.MimarksS_assembly_software = Slot(uri=MIXS['0000058'], name="MimarksS_assembly_software", curie=MIXS.curie('0000058'),
                   model_uri=MIXS.MimarksS_assembly_software, domain=None, range=Optional[str])

slots.MimarksS_associated_resource = Slot(uri=MIXS['0000091'], name="MimarksS_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.MimarksS_associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.MimarksS_chimera_check = Slot(uri=MIXS['0000052'], name="MimarksS_chimera_check", curie=MIXS.curie('0000052'),
                   model_uri=MIXS.MimarksS_chimera_check, domain=None, range=Optional[str])

slots.MimarksS_collection_date = Slot(uri=MIXS['0000011'], name="MimarksS_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.MimarksS_collection_date, domain=None, range=str)

slots.MimarksS_depth = Slot(uri=MIXS['0000018'], name="MimarksS_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.MimarksS_depth, domain=None, range=Optional[str])

slots.MimarksS_elev = Slot(uri=MIXS['0000093'], name="MimarksS_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.MimarksS_elev, domain=None, range=Optional[str])

slots.MimarksS_env_broad_scale = Slot(uri=MIXS['0000012'], name="MimarksS_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.MimarksS_env_broad_scale, domain=None, range=str)

slots.MimarksS_env_local_scale = Slot(uri=MIXS['0000013'], name="MimarksS_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.MimarksS_env_local_scale, domain=None, range=str)

slots.MimarksS_env_medium = Slot(uri=MIXS['0000014'], name="MimarksS_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.MimarksS_env_medium, domain=None, range=str)

slots.MimarksS_experimental_factor = Slot(uri=MIXS['0000008'], name="MimarksS_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.MimarksS_experimental_factor, domain=None, range=Optional[str])

slots.MimarksS_geo_loc_name = Slot(uri=MIXS['0000010'], name="MimarksS_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.MimarksS_geo_loc_name, domain=None, range=str)

slots.MimarksS_lat_lon = Slot(uri=MIXS['0000009'], name="MimarksS_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.MimarksS_lat_lon, domain=None, range=str)

slots.MimarksS_lib_layout = Slot(uri=MIXS['0000041'], name="MimarksS_lib_layout", curie=MIXS.curie('0000041'),
                   model_uri=MIXS.MimarksS_lib_layout, domain=None, range=Optional[str])

slots.MimarksS_lib_reads_seqd = Slot(uri=MIXS['0000040'], name="MimarksS_lib_reads_seqd", curie=MIXS.curie('0000040'),
                   model_uri=MIXS.MimarksS_lib_reads_seqd, domain=None, range=Optional[str])

slots.MimarksS_lib_screen = Slot(uri=MIXS['0000043'], name="MimarksS_lib_screen", curie=MIXS.curie('0000043'),
                   model_uri=MIXS.MimarksS_lib_screen, domain=None, range=Optional[str])

slots.MimarksS_lib_size = Slot(uri=MIXS['0000039'], name="MimarksS_lib_size", curie=MIXS.curie('0000039'),
                   model_uri=MIXS.MimarksS_lib_size, domain=None, range=Optional[str])

slots.MimarksS_lib_vector = Slot(uri=MIXS['0000042'], name="MimarksS_lib_vector", curie=MIXS.curie('0000042'),
                   model_uri=MIXS.MimarksS_lib_vector, domain=None, range=Optional[str])

slots.MimarksS_mid = Slot(uri=MIXS['0000047'], name="MimarksS_mid", curie=MIXS.curie('0000047'),
                   model_uri=MIXS.MimarksS_mid, domain=None, range=Optional[str])

slots.MimarksS_neg_cont_type = Slot(uri=MIXS['0001321'], name="MimarksS_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.MimarksS_neg_cont_type, domain=None, range=Optional[str])

slots.MimarksS_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="MimarksS_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.MimarksS_nucl_acid_amp, domain=None, range=Optional[str])

slots.MimarksS_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="MimarksS_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.MimarksS_nucl_acid_ext, domain=None, range=Optional[str])

slots.MimarksS_pcr_cond = Slot(uri=MIXS['0000049'], name="MimarksS_pcr_cond", curie=MIXS.curie('0000049'),
                   model_uri=MIXS.MimarksS_pcr_cond, domain=None, range=Optional[str])

slots.MimarksS_pcr_primers = Slot(uri=MIXS['0000046'], name="MimarksS_pcr_primers", curie=MIXS.curie('0000046'),
                   model_uri=MIXS.MimarksS_pcr_primers, domain=None, range=Optional[str])

slots.MimarksS_pos_cont_type = Slot(uri=MIXS['0001322'], name="MimarksS_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.MimarksS_pos_cont_type, domain=None, range=Optional[str])

slots.MimarksS_project_name = Slot(uri=MIXS['0000092'], name="MimarksS_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.MimarksS_project_name, domain=None, range=str)

slots.MimarksS_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="MimarksS_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=MIXS.MimarksS_rel_to_oxygen, domain=None, range=Optional[str])

slots.MimarksS_samp_collec_device = Slot(uri=MIXS['0000002'], name="MimarksS_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.MimarksS_samp_collec_device, domain=None, range=Optional[str])

slots.MimarksS_samp_collec_method = Slot(uri=MIXS['0001225'], name="MimarksS_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.MimarksS_samp_collec_method, domain=None, range=Optional[str])

slots.MimarksS_samp_mat_process = Slot(uri=MIXS['0000016'], name="MimarksS_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.MimarksS_samp_mat_process, domain=None, range=Optional[str])

slots.MimarksS_samp_name = Slot(uri=MIXS['0001107'], name="MimarksS_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.MimarksS_samp_name, domain=None, range=str)

slots.MimarksS_samp_size = Slot(uri=MIXS['0000001'], name="MimarksS_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.MimarksS_samp_size, domain=None, range=Optional[str])

slots.MimarksS_samp_taxon_id = Slot(uri=MIXS['0001320'], name="MimarksS_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.MimarksS_samp_taxon_id, domain=None, range=str)

slots.MimarksS_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="MimarksS_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.MimarksS_samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.MimarksS_seq_meth = Slot(uri=MIXS['0000050'], name="MimarksS_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.MimarksS_seq_meth, domain=None, range=str)

slots.MimarksS_seq_quality_check = Slot(uri=MIXS['0000051'], name="MimarksS_seq_quality_check", curie=MIXS.curie('0000051'),
                   model_uri=MIXS.MimarksS_seq_quality_check, domain=None, range=Optional[str])

slots.MimarksS_size_frac = Slot(uri=MIXS['0000017'], name="MimarksS_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=MIXS.MimarksS_size_frac, domain=None, range=Optional[str])

slots.MimarksS_sop = Slot(uri=MIXS['0000090'], name="MimarksS_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.MimarksS_sop, domain=None, range=Optional[Union[str, List[str]]])

slots.MimarksS_source_mat_id = Slot(uri=MIXS['0000026'], name="MimarksS_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.MimarksS_source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.MimarksS_target_gene = Slot(uri=MIXS['0000044'], name="MimarksS_target_gene", curie=MIXS.curie('0000044'),
                   model_uri=MIXS.MimarksS_target_gene, domain=None, range=str)

slots.MimarksS_target_subfragment = Slot(uri=MIXS['0000045'], name="MimarksS_target_subfragment", curie=MIXS.curie('0000045'),
                   model_uri=MIXS.MimarksS_target_subfragment, domain=None, range=Optional[str])

slots.MimarksS_temp = Slot(uri=MIXS['0000113'], name="MimarksS_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.MimarksS_temp, domain=None, range=Optional[str])

slots.Misag_x_16s_recover = Slot(uri=MIXS['0000065'], name="Misag_x_16s_recover", curie=MIXS.curie('0000065'),
                   model_uri=MIXS.Misag_x_16s_recover, domain=None, range=Optional[str])

slots.Misag_x_16s_recover_software = Slot(uri=MIXS['0000066'], name="Misag_x_16s_recover_software", curie=MIXS.curie('0000066'),
                   model_uri=MIXS.Misag_x_16s_recover_software, domain=None, range=Optional[str])

slots.Misag_adapters = Slot(uri=MIXS['0000048'], name="Misag_adapters", curie=MIXS.curie('0000048'),
                   model_uri=MIXS.Misag_adapters, domain=None, range=Optional[str])

slots.Misag_alt = Slot(uri=MIXS['0000094'], name="Misag_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.Misag_alt, domain=None, range=Optional[str])

slots.Misag_annot = Slot(uri=MIXS['0000059'], name="Misag_annot", curie=MIXS.curie('0000059'),
                   model_uri=MIXS.Misag_annot, domain=None, range=Optional[str])

slots.Misag_assembly_name = Slot(uri=MIXS['0000057'], name="Misag_assembly_name", curie=MIXS.curie('0000057'),
                   model_uri=MIXS.Misag_assembly_name, domain=None, range=Optional[str])

slots.Misag_assembly_qual = Slot(uri=MIXS['0000056'], name="Misag_assembly_qual", curie=MIXS.curie('0000056'),
                   model_uri=MIXS.Misag_assembly_qual, domain=None, range=str)

slots.Misag_assembly_software = Slot(uri=MIXS['0000058'], name="Misag_assembly_software", curie=MIXS.curie('0000058'),
                   model_uri=MIXS.Misag_assembly_software, domain=None, range=str)

slots.Misag_associated_resource = Slot(uri=MIXS['0000091'], name="Misag_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.Misag_associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.Misag_collection_date = Slot(uri=MIXS['0000011'], name="Misag_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.Misag_collection_date, domain=None, range=str)

slots.Misag_compl_appr = Slot(uri=MIXS['0000071'], name="Misag_compl_appr", curie=MIXS.curie('0000071'),
                   model_uri=MIXS.Misag_compl_appr, domain=None, range=Optional[str])

slots.Misag_compl_score = Slot(uri=MIXS['0000069'], name="Misag_compl_score", curie=MIXS.curie('0000069'),
                   model_uri=MIXS.Misag_compl_score, domain=None, range=str)

slots.Misag_compl_software = Slot(uri=MIXS['0000070'], name="Misag_compl_software", curie=MIXS.curie('0000070'),
                   model_uri=MIXS.Misag_compl_software, domain=None, range=str)

slots.Misag_contam_score = Slot(uri=MIXS['0000072'], name="Misag_contam_score", curie=MIXS.curie('0000072'),
                   model_uri=MIXS.Misag_contam_score, domain=None, range=str)

slots.Misag_contam_screen_input = Slot(uri=MIXS['0000005'], name="Misag_contam_screen_input", curie=MIXS.curie('0000005'),
                   model_uri=MIXS.Misag_contam_screen_input, domain=None, range=Optional[str])

slots.Misag_contam_screen_param = Slot(uri=MIXS['0000073'], name="Misag_contam_screen_param", curie=MIXS.curie('0000073'),
                   model_uri=MIXS.Misag_contam_screen_param, domain=None, range=Optional[str])

slots.Misag_decontam_software = Slot(uri=MIXS['0000074'], name="Misag_decontam_software", curie=MIXS.curie('0000074'),
                   model_uri=MIXS.Misag_decontam_software, domain=None, range=Optional[str])

slots.Misag_depth = Slot(uri=MIXS['0000018'], name="Misag_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.Misag_depth, domain=None, range=Optional[str])

slots.Misag_elev = Slot(uri=MIXS['0000093'], name="Misag_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.Misag_elev, domain=None, range=Optional[str])

slots.Misag_env_broad_scale = Slot(uri=MIXS['0000012'], name="Misag_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.Misag_env_broad_scale, domain=None, range=str)

slots.Misag_env_local_scale = Slot(uri=MIXS['0000013'], name="Misag_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.Misag_env_local_scale, domain=None, range=str)

slots.Misag_env_medium = Slot(uri=MIXS['0000014'], name="Misag_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.Misag_env_medium, domain=None, range=str)

slots.Misag_experimental_factor = Slot(uri=MIXS['0000008'], name="Misag_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.Misag_experimental_factor, domain=None, range=Optional[str])

slots.Misag_feat_pred = Slot(uri=MIXS['0000061'], name="Misag_feat_pred", curie=MIXS.curie('0000061'),
                   model_uri=MIXS.Misag_feat_pred, domain=None, range=Optional[str])

slots.Misag_geo_loc_name = Slot(uri=MIXS['0000010'], name="Misag_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.Misag_geo_loc_name, domain=None, range=str)

slots.Misag_lat_lon = Slot(uri=MIXS['0000009'], name="Misag_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.Misag_lat_lon, domain=None, range=str)

slots.Misag_lib_layout = Slot(uri=MIXS['0000041'], name="Misag_lib_layout", curie=MIXS.curie('0000041'),
                   model_uri=MIXS.Misag_lib_layout, domain=None, range=Optional[str])

slots.Misag_lib_reads_seqd = Slot(uri=MIXS['0000040'], name="Misag_lib_reads_seqd", curie=MIXS.curie('0000040'),
                   model_uri=MIXS.Misag_lib_reads_seqd, domain=None, range=Optional[str])

slots.Misag_lib_screen = Slot(uri=MIXS['0000043'], name="Misag_lib_screen", curie=MIXS.curie('0000043'),
                   model_uri=MIXS.Misag_lib_screen, domain=None, range=Optional[str])

slots.Misag_lib_size = Slot(uri=MIXS['0000039'], name="Misag_lib_size", curie=MIXS.curie('0000039'),
                   model_uri=MIXS.Misag_lib_size, domain=None, range=Optional[str])

slots.Misag_lib_vector = Slot(uri=MIXS['0000042'], name="Misag_lib_vector", curie=MIXS.curie('0000042'),
                   model_uri=MIXS.Misag_lib_vector, domain=None, range=Optional[str])

slots.Misag_mid = Slot(uri=MIXS['0000047'], name="Misag_mid", curie=MIXS.curie('0000047'),
                   model_uri=MIXS.Misag_mid, domain=None, range=Optional[str])

slots.Misag_neg_cont_type = Slot(uri=MIXS['0001321'], name="Misag_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.Misag_neg_cont_type, domain=None, range=Optional[str])

slots.Misag_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="Misag_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.Misag_nucl_acid_amp, domain=None, range=Optional[str])

slots.Misag_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="Misag_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.Misag_nucl_acid_ext, domain=None, range=Optional[str])

slots.Misag_number_contig = Slot(uri=MIXS['0000060'], name="Misag_number_contig", curie=MIXS.curie('0000060'),
                   model_uri=MIXS.Misag_number_contig, domain=None, range=Optional[str])

slots.Misag_pos_cont_type = Slot(uri=MIXS['0001322'], name="Misag_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.Misag_pos_cont_type, domain=None, range=Optional[str])

slots.Misag_project_name = Slot(uri=MIXS['0000092'], name="Misag_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.Misag_project_name, domain=None, range=str)

slots.Misag_ref_biomaterial = Slot(uri=MIXS['0000025'], name="Misag_ref_biomaterial", curie=MIXS.curie('0000025'),
                   model_uri=MIXS.Misag_ref_biomaterial, domain=None, range=Optional[str])

slots.Misag_ref_db = Slot(uri=MIXS['0000062'], name="Misag_ref_db", curie=MIXS.curie('0000062'),
                   model_uri=MIXS.Misag_ref_db, domain=None, range=Optional[str])

slots.Misag_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="Misag_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=MIXS.Misag_rel_to_oxygen, domain=None, range=Optional[str])

slots.Misag_samp_collec_device = Slot(uri=MIXS['0000002'], name="Misag_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.Misag_samp_collec_device, domain=None, range=Optional[str])

slots.Misag_samp_collec_method = Slot(uri=MIXS['0001225'], name="Misag_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.Misag_samp_collec_method, domain=None, range=Optional[str])

slots.Misag_samp_mat_process = Slot(uri=MIXS['0000016'], name="Misag_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.Misag_samp_mat_process, domain=None, range=Optional[str])

slots.Misag_samp_name = Slot(uri=MIXS['0001107'], name="Misag_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.Misag_samp_name, domain=None, range=str)

slots.Misag_samp_size = Slot(uri=MIXS['0000001'], name="Misag_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.Misag_samp_size, domain=None, range=Optional[str])

slots.Misag_samp_taxon_id = Slot(uri=MIXS['0001320'], name="Misag_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.Misag_samp_taxon_id, domain=None, range=str)

slots.Misag_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="Misag_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.Misag_samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.Misag_seq_meth = Slot(uri=MIXS['0000050'], name="Misag_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.Misag_seq_meth, domain=None, range=str)

slots.Misag_sim_search_meth = Slot(uri=MIXS['0000063'], name="Misag_sim_search_meth", curie=MIXS.curie('0000063'),
                   model_uri=MIXS.Misag_sim_search_meth, domain=None, range=Optional[str])

slots.Misag_single_cell_lysis_appr = Slot(uri=MIXS['0000076'], name="Misag_single_cell_lysis_appr", curie=MIXS.curie('0000076'),
                   model_uri=MIXS.Misag_single_cell_lysis_appr, domain=None, range=str)

slots.Misag_single_cell_lysis_prot = Slot(uri=MIXS['0000054'], name="Misag_single_cell_lysis_prot", curie=MIXS.curie('0000054'),
                   model_uri=MIXS.Misag_single_cell_lysis_prot, domain=None, range=Optional[str])

slots.Misag_size_frac = Slot(uri=MIXS['0000017'], name="Misag_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=MIXS.Misag_size_frac, domain=None, range=Optional[str])

slots.Misag_sop = Slot(uri=MIXS['0000090'], name="Misag_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.Misag_sop, domain=None, range=Optional[Union[str, List[str]]])

slots.Misag_sort_tech = Slot(uri=MIXS['0000075'], name="Misag_sort_tech", curie=MIXS.curie('0000075'),
                   model_uri=MIXS.Misag_sort_tech, domain=None, range=str)

slots.Misag_source_mat_id = Slot(uri=MIXS['0000026'], name="Misag_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.Misag_source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.Misag_tax_class = Slot(uri=MIXS['0000064'], name="Misag_tax_class", curie=MIXS.curie('0000064'),
                   model_uri=MIXS.Misag_tax_class, domain=None, range=Optional[str])

slots.Misag_tax_ident = Slot(uri=MIXS['0000053'], name="Misag_tax_ident", curie=MIXS.curie('0000053'),
                   model_uri=MIXS.Misag_tax_ident, domain=None, range=str)

slots.Misag_temp = Slot(uri=MIXS['0000113'], name="Misag_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.Misag_temp, domain=None, range=Optional[str])

slots.Misag_trna_ext_software = Slot(uri=MIXS['0000068'], name="Misag_trna_ext_software", curie=MIXS.curie('0000068'),
                   model_uri=MIXS.Misag_trna_ext_software, domain=None, range=Optional[str])

slots.Misag_trnas = Slot(uri=MIXS['0000067'], name="Misag_trnas", curie=MIXS.curie('0000067'),
                   model_uri=MIXS.Misag_trnas, domain=None, range=Optional[str])

slots.Misag_wga_amp_appr = Slot(uri=MIXS['0000055'], name="Misag_wga_amp_appr", curie=MIXS.curie('0000055'),
                   model_uri=MIXS.Misag_wga_amp_appr, domain=None, range=str)

slots.Misag_wga_amp_kit = Slot(uri=MIXS['0000006'], name="Misag_wga_amp_kit", curie=MIXS.curie('0000006'),
                   model_uri=MIXS.Misag_wga_amp_kit, domain=None, range=Optional[str])

slots.Miuvig_adapters = Slot(uri=MIXS['0000048'], name="Miuvig_adapters", curie=MIXS.curie('0000048'),
                   model_uri=MIXS.Miuvig_adapters, domain=None, range=Optional[str])

slots.Miuvig_alt = Slot(uri=MIXS['0000094'], name="Miuvig_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.Miuvig_alt, domain=None, range=Optional[str])

slots.Miuvig_annot = Slot(uri=MIXS['0000059'], name="Miuvig_annot", curie=MIXS.curie('0000059'),
                   model_uri=MIXS.Miuvig_annot, domain=None, range=Optional[str])

slots.Miuvig_assembly_name = Slot(uri=MIXS['0000057'], name="Miuvig_assembly_name", curie=MIXS.curie('0000057'),
                   model_uri=MIXS.Miuvig_assembly_name, domain=None, range=Optional[str])

slots.Miuvig_assembly_qual = Slot(uri=MIXS['0000056'], name="Miuvig_assembly_qual", curie=MIXS.curie('0000056'),
                   model_uri=MIXS.Miuvig_assembly_qual, domain=None, range=str)

slots.Miuvig_assembly_software = Slot(uri=MIXS['0000058'], name="Miuvig_assembly_software", curie=MIXS.curie('0000058'),
                   model_uri=MIXS.Miuvig_assembly_software, domain=None, range=str)

slots.Miuvig_associated_resource = Slot(uri=MIXS['0000091'], name="Miuvig_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.Miuvig_associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.Miuvig_bin_param = Slot(uri=MIXS['0000077'], name="Miuvig_bin_param", curie=MIXS.curie('0000077'),
                   model_uri=MIXS.Miuvig_bin_param, domain=None, range=Optional[str])

slots.Miuvig_bin_software = Slot(uri=MIXS['0000078'], name="Miuvig_bin_software", curie=MIXS.curie('0000078'),
                   model_uri=MIXS.Miuvig_bin_software, domain=None, range=Optional[str])

slots.Miuvig_biotic_relationship = Slot(uri=MIXS['0000028'], name="Miuvig_biotic_relationship", curie=MIXS.curie('0000028'),
                   model_uri=MIXS.Miuvig_biotic_relationship, domain=None, range=Optional[str])

slots.Miuvig_collection_date = Slot(uri=MIXS['0000011'], name="Miuvig_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.Miuvig_collection_date, domain=None, range=str)

slots.Miuvig_compl_appr = Slot(uri=MIXS['0000071'], name="Miuvig_compl_appr", curie=MIXS.curie('0000071'),
                   model_uri=MIXS.Miuvig_compl_appr, domain=None, range=Optional[str])

slots.Miuvig_compl_score = Slot(uri=MIXS['0000069'], name="Miuvig_compl_score", curie=MIXS.curie('0000069'),
                   model_uri=MIXS.Miuvig_compl_score, domain=None, range=Optional[str])

slots.Miuvig_compl_software = Slot(uri=MIXS['0000070'], name="Miuvig_compl_software", curie=MIXS.curie('0000070'),
                   model_uri=MIXS.Miuvig_compl_software, domain=None, range=Optional[str])

slots.Miuvig_depth = Slot(uri=MIXS['0000018'], name="Miuvig_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.Miuvig_depth, domain=None, range=Optional[str])

slots.Miuvig_detec_type = Slot(uri=MIXS['0000084'], name="Miuvig_detec_type", curie=MIXS.curie('0000084'),
                   model_uri=MIXS.Miuvig_detec_type, domain=None, range=str)

slots.Miuvig_elev = Slot(uri=MIXS['0000093'], name="Miuvig_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.Miuvig_elev, domain=None, range=Optional[str])

slots.Miuvig_env_broad_scale = Slot(uri=MIXS['0000012'], name="Miuvig_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.Miuvig_env_broad_scale, domain=None, range=str)

slots.Miuvig_env_local_scale = Slot(uri=MIXS['0000013'], name="Miuvig_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.Miuvig_env_local_scale, domain=None, range=str)

slots.Miuvig_env_medium = Slot(uri=MIXS['0000014'], name="Miuvig_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.Miuvig_env_medium, domain=None, range=str)

slots.Miuvig_estimated_size = Slot(uri=MIXS['0000024'], name="Miuvig_estimated_size", curie=MIXS.curie('0000024'),
                   model_uri=MIXS.Miuvig_estimated_size, domain=None, range=Optional[str])

slots.Miuvig_experimental_factor = Slot(uri=MIXS['0000008'], name="Miuvig_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.Miuvig_experimental_factor, domain=None, range=Optional[str])

slots.Miuvig_feat_pred = Slot(uri=MIXS['0000061'], name="Miuvig_feat_pred", curie=MIXS.curie('0000061'),
                   model_uri=MIXS.Miuvig_feat_pred, domain=None, range=Optional[str])

slots.Miuvig_geo_loc_name = Slot(uri=MIXS['0000010'], name="Miuvig_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.Miuvig_geo_loc_name, domain=None, range=str)

slots.Miuvig_host_disease_stat = Slot(uri=MIXS['0000031'], name="Miuvig_host_disease_stat", curie=MIXS.curie('0000031'),
                   model_uri=MIXS.Miuvig_host_disease_stat, domain=None, range=Optional[Union[str, List[str]]])

slots.Miuvig_host_pred_appr = Slot(uri=MIXS['0000088'], name="Miuvig_host_pred_appr", curie=MIXS.curie('0000088'),
                   model_uri=MIXS.Miuvig_host_pred_appr, domain=None, range=Optional[str])

slots.Miuvig_host_pred_est_acc = Slot(uri=MIXS['0000089'], name="Miuvig_host_pred_est_acc", curie=MIXS.curie('0000089'),
                   model_uri=MIXS.Miuvig_host_pred_est_acc, domain=None, range=Optional[str])

slots.Miuvig_host_spec_range = Slot(uri=MIXS['0000030'], name="Miuvig_host_spec_range", curie=MIXS.curie('0000030'),
                   model_uri=MIXS.Miuvig_host_spec_range, domain=None, range=Optional[Union[str, List[str]]])

slots.Miuvig_lat_lon = Slot(uri=MIXS['0000009'], name="Miuvig_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.Miuvig_lat_lon, domain=None, range=str)

slots.Miuvig_lib_layout = Slot(uri=MIXS['0000041'], name="Miuvig_lib_layout", curie=MIXS.curie('0000041'),
                   model_uri=MIXS.Miuvig_lib_layout, domain=None, range=Optional[str])

slots.Miuvig_lib_reads_seqd = Slot(uri=MIXS['0000040'], name="Miuvig_lib_reads_seqd", curie=MIXS.curie('0000040'),
                   model_uri=MIXS.Miuvig_lib_reads_seqd, domain=None, range=Optional[str])

slots.Miuvig_lib_screen = Slot(uri=MIXS['0000043'], name="Miuvig_lib_screen", curie=MIXS.curie('0000043'),
                   model_uri=MIXS.Miuvig_lib_screen, domain=None, range=Optional[str])

slots.Miuvig_lib_size = Slot(uri=MIXS['0000039'], name="Miuvig_lib_size", curie=MIXS.curie('0000039'),
                   model_uri=MIXS.Miuvig_lib_size, domain=None, range=Optional[str])

slots.Miuvig_lib_vector = Slot(uri=MIXS['0000042'], name="Miuvig_lib_vector", curie=MIXS.curie('0000042'),
                   model_uri=MIXS.Miuvig_lib_vector, domain=None, range=Optional[str])

slots.Miuvig_mag_cov_software = Slot(uri=MIXS['0000080'], name="Miuvig_mag_cov_software", curie=MIXS.curie('0000080'),
                   model_uri=MIXS.Miuvig_mag_cov_software, domain=None, range=Optional[str])

slots.Miuvig_mid = Slot(uri=MIXS['0000047'], name="Miuvig_mid", curie=MIXS.curie('0000047'),
                   model_uri=MIXS.Miuvig_mid, domain=None, range=Optional[str])

slots.Miuvig_neg_cont_type = Slot(uri=MIXS['0001321'], name="Miuvig_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.Miuvig_neg_cont_type, domain=None, range=Optional[str])

slots.Miuvig_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="Miuvig_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.Miuvig_nucl_acid_amp, domain=None, range=Optional[str])

slots.Miuvig_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="Miuvig_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.Miuvig_nucl_acid_ext, domain=None, range=Optional[str])

slots.Miuvig_number_contig = Slot(uri=MIXS['0000060'], name="Miuvig_number_contig", curie=MIXS.curie('0000060'),
                   model_uri=MIXS.Miuvig_number_contig, domain=None, range=str)

slots.Miuvig_otu_class_appr = Slot(uri=MIXS['0000085'], name="Miuvig_otu_class_appr", curie=MIXS.curie('0000085'),
                   model_uri=MIXS.Miuvig_otu_class_appr, domain=None, range=Optional[str])

slots.Miuvig_otu_db = Slot(uri=MIXS['0000087'], name="Miuvig_otu_db", curie=MIXS.curie('0000087'),
                   model_uri=MIXS.Miuvig_otu_db, domain=None, range=Optional[str])

slots.Miuvig_otu_seq_comp_appr = Slot(uri=MIXS['0000086'], name="Miuvig_otu_seq_comp_appr", curie=MIXS.curie('0000086'),
                   model_uri=MIXS.Miuvig_otu_seq_comp_appr, domain=None, range=Optional[str])

slots.Miuvig_pathogenicity = Slot(uri=MIXS['0000027'], name="Miuvig_pathogenicity", curie=MIXS.curie('0000027'),
                   model_uri=MIXS.Miuvig_pathogenicity, domain=None, range=Optional[str])

slots.Miuvig_pos_cont_type = Slot(uri=MIXS['0001322'], name="Miuvig_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.Miuvig_pos_cont_type, domain=None, range=Optional[str])

slots.Miuvig_pred_genome_struc = Slot(uri=MIXS['0000083'], name="Miuvig_pred_genome_struc", curie=MIXS.curie('0000083'),
                   model_uri=MIXS.Miuvig_pred_genome_struc, domain=None, range=str)

slots.Miuvig_pred_genome_type = Slot(uri=MIXS['0000082'], name="Miuvig_pred_genome_type", curie=MIXS.curie('0000082'),
                   model_uri=MIXS.Miuvig_pred_genome_type, domain=None, range=str)

slots.Miuvig_project_name = Slot(uri=MIXS['0000092'], name="Miuvig_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.Miuvig_project_name, domain=None, range=str)

slots.Miuvig_reassembly_bin = Slot(uri=MIXS['0000079'], name="Miuvig_reassembly_bin", curie=MIXS.curie('0000079'),
                   model_uri=MIXS.Miuvig_reassembly_bin, domain=None, range=Optional[str])

slots.Miuvig_ref_biomaterial = Slot(uri=MIXS['0000025'], name="Miuvig_ref_biomaterial", curie=MIXS.curie('0000025'),
                   model_uri=MIXS.Miuvig_ref_biomaterial, domain=None, range=Optional[str])

slots.Miuvig_ref_db = Slot(uri=MIXS['0000062'], name="Miuvig_ref_db", curie=MIXS.curie('0000062'),
                   model_uri=MIXS.Miuvig_ref_db, domain=None, range=Optional[str])

slots.Miuvig_samp_collec_device = Slot(uri=MIXS['0000002'], name="Miuvig_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.Miuvig_samp_collec_device, domain=None, range=Optional[str])

slots.Miuvig_samp_collec_method = Slot(uri=MIXS['0001225'], name="Miuvig_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.Miuvig_samp_collec_method, domain=None, range=Optional[str])

slots.Miuvig_samp_mat_process = Slot(uri=MIXS['0000016'], name="Miuvig_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.Miuvig_samp_mat_process, domain=None, range=Optional[str])

slots.Miuvig_samp_name = Slot(uri=MIXS['0001107'], name="Miuvig_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.Miuvig_samp_name, domain=None, range=str)

slots.Miuvig_samp_size = Slot(uri=MIXS['0000001'], name="Miuvig_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.Miuvig_samp_size, domain=None, range=Optional[str])

slots.Miuvig_samp_taxon_id = Slot(uri=MIXS['0001320'], name="Miuvig_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.Miuvig_samp_taxon_id, domain=None, range=str)

slots.Miuvig_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="Miuvig_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.Miuvig_samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.Miuvig_seq_meth = Slot(uri=MIXS['0000050'], name="Miuvig_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.Miuvig_seq_meth, domain=None, range=str)

slots.Miuvig_sim_search_meth = Slot(uri=MIXS['0000063'], name="Miuvig_sim_search_meth", curie=MIXS.curie('0000063'),
                   model_uri=MIXS.Miuvig_sim_search_meth, domain=None, range=Optional[str])

slots.Miuvig_single_cell_lysis_appr = Slot(uri=MIXS['0000076'], name="Miuvig_single_cell_lysis_appr", curie=MIXS.curie('0000076'),
                   model_uri=MIXS.Miuvig_single_cell_lysis_appr, domain=None, range=Optional[str])

slots.Miuvig_single_cell_lysis_prot = Slot(uri=MIXS['0000054'], name="Miuvig_single_cell_lysis_prot", curie=MIXS.curie('0000054'),
                   model_uri=MIXS.Miuvig_single_cell_lysis_prot, domain=None, range=Optional[str])

slots.Miuvig_size_frac = Slot(uri=MIXS['0000017'], name="Miuvig_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=MIXS.Miuvig_size_frac, domain=None, range=Optional[str])

slots.Miuvig_sop = Slot(uri=MIXS['0000090'], name="Miuvig_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.Miuvig_sop, domain=None, range=Optional[Union[str, List[str]]])

slots.Miuvig_sort_tech = Slot(uri=MIXS['0000075'], name="Miuvig_sort_tech", curie=MIXS.curie('0000075'),
                   model_uri=MIXS.Miuvig_sort_tech, domain=None, range=Optional[str])

slots.Miuvig_source_mat_id = Slot(uri=MIXS['0000026'], name="Miuvig_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.Miuvig_source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.Miuvig_source_uvig = Slot(uri=MIXS['0000035'], name="Miuvig_source_uvig", curie=MIXS.curie('0000035'),
                   model_uri=MIXS.Miuvig_source_uvig, domain=None, range=str)

slots.Miuvig_specific_host = Slot(uri=MIXS['0000029'], name="Miuvig_specific_host", curie=MIXS.curie('0000029'),
                   model_uri=MIXS.Miuvig_specific_host, domain=None, range=Optional[str])

slots.Miuvig_tax_class = Slot(uri=MIXS['0000064'], name="Miuvig_tax_class", curie=MIXS.curie('0000064'),
                   model_uri=MIXS.Miuvig_tax_class, domain=None, range=Optional[str])

slots.Miuvig_tax_ident = Slot(uri=MIXS['0000053'], name="Miuvig_tax_ident", curie=MIXS.curie('0000053'),
                   model_uri=MIXS.Miuvig_tax_ident, domain=None, range=Optional[str])

slots.Miuvig_temp = Slot(uri=MIXS['0000113'], name="Miuvig_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.Miuvig_temp, domain=None, range=Optional[str])

slots.Miuvig_trna_ext_software = Slot(uri=MIXS['0000068'], name="Miuvig_trna_ext_software", curie=MIXS.curie('0000068'),
                   model_uri=MIXS.Miuvig_trna_ext_software, domain=None, range=Optional[str])

slots.Miuvig_trnas = Slot(uri=MIXS['0000067'], name="Miuvig_trnas", curie=MIXS.curie('0000067'),
                   model_uri=MIXS.Miuvig_trnas, domain=None, range=Optional[str])

slots.Miuvig_vir_ident_software = Slot(uri=MIXS['0000081'], name="Miuvig_vir_ident_software", curie=MIXS.curie('0000081'),
                   model_uri=MIXS.Miuvig_vir_ident_software, domain=None, range=str)

slots.Miuvig_virus_enrich_appr = Slot(uri=MIXS['0000036'], name="Miuvig_virus_enrich_appr", curie=MIXS.curie('0000036'),
                   model_uri=MIXS.Miuvig_virus_enrich_appr, domain=None, range=str)

slots.Miuvig_wga_amp_appr = Slot(uri=MIXS['0000055'], name="Miuvig_wga_amp_appr", curie=MIXS.curie('0000055'),
                   model_uri=MIXS.Miuvig_wga_amp_appr, domain=None, range=Optional[str])

slots.Miuvig_wga_amp_kit = Slot(uri=MIXS['0000006'], name="Miuvig_wga_amp_kit", curie=MIXS.curie('0000006'),
                   model_uri=MIXS.Miuvig_wga_amp_kit, domain=None, range=Optional[str])

slots.Mims_adapters = Slot(uri=MIXS['0000048'], name="Mims_adapters", curie=MIXS.curie('0000048'),
                   model_uri=MIXS.Mims_adapters, domain=Mims, range=Optional[str])

slots.Mims_alt = Slot(uri=MIXS['0000094'], name="Mims_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.Mims_alt, domain=Mims, range=Optional[str])

slots.Mims_annot = Slot(uri=MIXS['0000059'], name="Mims_annot", curie=MIXS.curie('0000059'),
                   model_uri=MIXS.Mims_annot, domain=Mims, range=Optional[str])

slots.Mims_assembly_name = Slot(uri=MIXS['0000057'], name="Mims_assembly_name", curie=MIXS.curie('0000057'),
                   model_uri=MIXS.Mims_assembly_name, domain=Mims, range=Optional[str])

slots.Mims_assembly_qual = Slot(uri=MIXS['0000056'], name="Mims_assembly_qual", curie=MIXS.curie('0000056'),
                   model_uri=MIXS.Mims_assembly_qual, domain=Mims, range=Optional[str])

slots.Mims_assembly_software = Slot(uri=MIXS['0000058'], name="Mims_assembly_software", curie=MIXS.curie('0000058'),
                   model_uri=MIXS.Mims_assembly_software, domain=Mims, range=Optional[str])

slots.Mims_associated_resource = Slot(uri=MIXS['0000091'], name="Mims_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.Mims_associated_resource, domain=Mims, range=Optional[Union[str, List[str]]])

slots.Mims_collection_date = Slot(uri=MIXS['0000011'], name="Mims_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.Mims_collection_date, domain=Mims, range=str)

slots.Mims_depth = Slot(uri=MIXS['0000018'], name="Mims_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.Mims_depth, domain=Mims, range=Optional[str])

slots.Mims_elev = Slot(uri=MIXS['0000093'], name="Mims_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.Mims_elev, domain=Mims, range=Optional[str])

slots.Mims_env_broad_scale = Slot(uri=MIXS['0000012'], name="Mims_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.Mims_env_broad_scale, domain=Mims, range=str)

slots.Mims_env_local_scale = Slot(uri=MIXS['0000013'], name="Mims_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.Mims_env_local_scale, domain=Mims, range=str)

slots.Mims_env_medium = Slot(uri=MIXS['0000014'], name="Mims_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.Mims_env_medium, domain=Mims, range=str)

slots.Mims_experimental_factor = Slot(uri=MIXS['0000008'], name="Mims_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.Mims_experimental_factor, domain=Mims, range=Optional[str])

slots.Mims_feat_pred = Slot(uri=MIXS['0000061'], name="Mims_feat_pred", curie=MIXS.curie('0000061'),
                   model_uri=MIXS.Mims_feat_pred, domain=Mims, range=Optional[str])

slots.Mims_geo_loc_name = Slot(uri=MIXS['0000010'], name="Mims_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.Mims_geo_loc_name, domain=Mims, range=str)

slots.Mims_lat_lon = Slot(uri=MIXS['0000009'], name="Mims_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.Mims_lat_lon, domain=Mims, range=str)

slots.Mims_lib_layout = Slot(uri=MIXS['0000041'], name="Mims_lib_layout", curie=MIXS.curie('0000041'),
                   model_uri=MIXS.Mims_lib_layout, domain=Mims, range=Optional[str])

slots.Mims_lib_reads_seqd = Slot(uri=MIXS['0000040'], name="Mims_lib_reads_seqd", curie=MIXS.curie('0000040'),
                   model_uri=MIXS.Mims_lib_reads_seqd, domain=Mims, range=Optional[str])

slots.Mims_lib_screen = Slot(uri=MIXS['0000043'], name="Mims_lib_screen", curie=MIXS.curie('0000043'),
                   model_uri=MIXS.Mims_lib_screen, domain=Mims, range=Optional[str])

slots.Mims_lib_size = Slot(uri=MIXS['0000039'], name="Mims_lib_size", curie=MIXS.curie('0000039'),
                   model_uri=MIXS.Mims_lib_size, domain=Mims, range=Optional[str])

slots.Mims_lib_vector = Slot(uri=MIXS['0000042'], name="Mims_lib_vector", curie=MIXS.curie('0000042'),
                   model_uri=MIXS.Mims_lib_vector, domain=Mims, range=Optional[str])

slots.Mims_mid = Slot(uri=MIXS['0000047'], name="Mims_mid", curie=MIXS.curie('0000047'),
                   model_uri=MIXS.Mims_mid, domain=Mims, range=Optional[str])

slots.Mims_neg_cont_type = Slot(uri=MIXS['0001321'], name="Mims_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.Mims_neg_cont_type, domain=Mims, range=Optional[str])

slots.Mims_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="Mims_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.Mims_nucl_acid_amp, domain=Mims, range=Optional[str])

slots.Mims_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="Mims_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.Mims_nucl_acid_ext, domain=Mims, range=Optional[str])

slots.Mims_number_contig = Slot(uri=MIXS['0000060'], name="Mims_number_contig", curie=MIXS.curie('0000060'),
                   model_uri=MIXS.Mims_number_contig, domain=Mims, range=Optional[str])

slots.Mims_pos_cont_type = Slot(uri=MIXS['0001322'], name="Mims_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.Mims_pos_cont_type, domain=Mims, range=Optional[str])

slots.Mims_project_name = Slot(uri=MIXS['0000092'], name="Mims_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.Mims_project_name, domain=Mims, range=str)

slots.Mims_ref_biomaterial = Slot(uri=MIXS['0000025'], name="Mims_ref_biomaterial", curie=MIXS.curie('0000025'),
                   model_uri=MIXS.Mims_ref_biomaterial, domain=Mims, range=Optional[str])

slots.Mims_ref_db = Slot(uri=MIXS['0000062'], name="Mims_ref_db", curie=MIXS.curie('0000062'),
                   model_uri=MIXS.Mims_ref_db, domain=Mims, range=Optional[str])

slots.Mims_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="Mims_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=MIXS.Mims_rel_to_oxygen, domain=Mims, range=Optional[str])

slots.Mims_samp_collec_device = Slot(uri=MIXS['0000002'], name="Mims_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.Mims_samp_collec_device, domain=Mims, range=Optional[str])

slots.Mims_samp_collec_method = Slot(uri=MIXS['0001225'], name="Mims_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.Mims_samp_collec_method, domain=Mims, range=Optional[str])

slots.Mims_samp_mat_process = Slot(uri=MIXS['0000016'], name="Mims_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.Mims_samp_mat_process, domain=Mims, range=Optional[str])

slots.Mims_samp_name = Slot(uri=MIXS['0001107'], name="Mims_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.Mims_samp_name, domain=Mims, range=str)

slots.Mims_samp_size = Slot(uri=MIXS['0000001'], name="Mims_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.Mims_samp_size, domain=Mims, range=Optional[str])

slots.Mims_samp_taxon_id = Slot(uri=MIXS['0001320'], name="Mims_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.Mims_samp_taxon_id, domain=Mims, range=str)

slots.Mims_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="Mims_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.Mims_samp_vol_we_dna_ext, domain=Mims, range=Optional[str])

slots.Mims_seq_meth = Slot(uri=MIXS['0000050'], name="Mims_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.Mims_seq_meth, domain=Mims, range=str)

slots.Mims_sim_search_meth = Slot(uri=MIXS['0000063'], name="Mims_sim_search_meth", curie=MIXS.curie('0000063'),
                   model_uri=MIXS.Mims_sim_search_meth, domain=Mims, range=Optional[str])

slots.Mims_size_frac = Slot(uri=MIXS['0000017'], name="Mims_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=MIXS.Mims_size_frac, domain=Mims, range=Optional[str])

slots.Mims_sop = Slot(uri=MIXS['0000090'], name="Mims_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.Mims_sop, domain=Mims, range=Optional[Union[str, List[str]]])

slots.Mims_source_mat_id = Slot(uri=MIXS['0000026'], name="Mims_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.Mims_source_mat_id, domain=Mims, range=Optional[Union[str, List[str]]])

slots.Mims_tax_class = Slot(uri=MIXS['0000064'], name="Mims_tax_class", curie=MIXS.curie('0000064'),
                   model_uri=MIXS.Mims_tax_class, domain=Mims, range=Optional[str])

slots.Mims_temp = Slot(uri=MIXS['0000113'], name="Mims_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.Mims_temp, domain=Mims, range=Optional[str])

slots.Database_mims_set = Slot(uri=MIXS.mims_set, name="Database_mims_set", curie=MIXS.curie('mims_set'),
                   model_uri=MIXS.Database_mims_set, domain=Database, range=Optional[Union[Union[dict, Mims], List[Union[dict, Mims]]]])