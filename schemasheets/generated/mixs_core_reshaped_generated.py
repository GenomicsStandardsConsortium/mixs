# Auto generated from mixs_core_reshaped_generated.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-10-11T14:01:50
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
    class_name: ClassVar[str] = "migs_ba"
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
    class_name: ClassVar[str] = "migs_eu"
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
    class_name: ClassVar[str] = "migs_org"
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
    class_name: ClassVar[str] = "migs_pl"
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
    class_name: ClassVar[str] = "migs_vi"
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
    class_name: ClassVar[str] = "mimag"
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
    class_name: ClassVar[str] = "mimarks_c"
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
    class_name: ClassVar[str] = "mimarks_s"
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
class Mims(ChecklistClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS["0010007"]
    class_class_curie: ClassVar[str] = "MIXS:0010007"
    class_name: ClassVar[str] = "mims"
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
class Misag(ChecklistClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS["0010010"]
    class_class_curie: ClassVar[str] = "MIXS:0010010"
    class_name: ClassVar[str] = "misag"
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
    class_name: ClassVar[str] = "miuvig"
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

slots.migs_ba_adapters = Slot(uri=MIXS['0000048'], name="migs_ba_adapters", curie=MIXS.curie('0000048'),
                   model_uri=MIXS.migs_ba_adapters, domain=None, range=Optional[str])

slots.migs_ba_alt = Slot(uri=MIXS['0000094'], name="migs_ba_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.migs_ba_alt, domain=None, range=Optional[str])

slots.migs_ba_annot = Slot(uri=MIXS['0000059'], name="migs_ba_annot", curie=MIXS.curie('0000059'),
                   model_uri=MIXS.migs_ba_annot, domain=None, range=Optional[str])

slots.migs_ba_assembly_name = Slot(uri=MIXS['0000057'], name="migs_ba_assembly_name", curie=MIXS.curie('0000057'),
                   model_uri=MIXS.migs_ba_assembly_name, domain=None, range=Optional[str])

slots.migs_ba_assembly_qual = Slot(uri=MIXS['0000056'], name="migs_ba_assembly_qual", curie=MIXS.curie('0000056'),
                   model_uri=MIXS.migs_ba_assembly_qual, domain=None, range=str)

slots.migs_ba_assembly_software = Slot(uri=MIXS['0000058'], name="migs_ba_assembly_software", curie=MIXS.curie('0000058'),
                   model_uri=MIXS.migs_ba_assembly_software, domain=None, range=str)

slots.migs_ba_associated_resource = Slot(uri=MIXS['0000091'], name="migs_ba_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.migs_ba_associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_ba_biotic_relationship = Slot(uri=MIXS['0000028'], name="migs_ba_biotic_relationship", curie=MIXS.curie('0000028'),
                   model_uri=MIXS.migs_ba_biotic_relationship, domain=None, range=Optional[str])

slots.migs_ba_collection_date = Slot(uri=MIXS['0000011'], name="migs_ba_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.migs_ba_collection_date, domain=None, range=str)

slots.migs_ba_compl_score = Slot(uri=MIXS['0000069'], name="migs_ba_compl_score", curie=MIXS.curie('0000069'),
                   model_uri=MIXS.migs_ba_compl_score, domain=None, range=Optional[str])

slots.migs_ba_compl_software = Slot(uri=MIXS['0000070'], name="migs_ba_compl_software", curie=MIXS.curie('0000070'),
                   model_uri=MIXS.migs_ba_compl_software, domain=None, range=Optional[str])

slots.migs_ba_depth = Slot(uri=MIXS['0000018'], name="migs_ba_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.migs_ba_depth, domain=None, range=Optional[str])

slots.migs_ba_elev = Slot(uri=MIXS['0000093'], name="migs_ba_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.migs_ba_elev, domain=None, range=Optional[str])

slots.migs_ba_encoded_traits = Slot(uri=MIXS['0000034'], name="migs_ba_encoded_traits", curie=MIXS.curie('0000034'),
                   model_uri=MIXS.migs_ba_encoded_traits, domain=None, range=Optional[str])

slots.migs_ba_env_broad_scale = Slot(uri=MIXS['0000012'], name="migs_ba_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.migs_ba_env_broad_scale, domain=None, range=str)

slots.migs_ba_env_local_scale = Slot(uri=MIXS['0000013'], name="migs_ba_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.migs_ba_env_local_scale, domain=None, range=str)

slots.migs_ba_env_medium = Slot(uri=MIXS['0000014'], name="migs_ba_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.migs_ba_env_medium, domain=None, range=str)

slots.migs_ba_estimated_size = Slot(uri=MIXS['0000024'], name="migs_ba_estimated_size", curie=MIXS.curie('0000024'),
                   model_uri=MIXS.migs_ba_estimated_size, domain=None, range=Optional[str])

slots.migs_ba_experimental_factor = Slot(uri=MIXS['0000008'], name="migs_ba_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.migs_ba_experimental_factor, domain=None, range=Optional[str])

slots.migs_ba_extrachrom_elements = Slot(uri=MIXS['0000023'], name="migs_ba_extrachrom_elements", curie=MIXS.curie('0000023'),
                   model_uri=MIXS.migs_ba_extrachrom_elements, domain=None, range=Optional[str])

slots.migs_ba_feat_pred = Slot(uri=MIXS['0000061'], name="migs_ba_feat_pred", curie=MIXS.curie('0000061'),
                   model_uri=MIXS.migs_ba_feat_pred, domain=None, range=Optional[str])

slots.migs_ba_geo_loc_name = Slot(uri=MIXS['0000010'], name="migs_ba_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.migs_ba_geo_loc_name, domain=None, range=str)

slots.migs_ba_host_disease_stat = Slot(uri=MIXS['0000031'], name="migs_ba_host_disease_stat", curie=MIXS.curie('0000031'),
                   model_uri=MIXS.migs_ba_host_disease_stat, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_ba_host_spec_range = Slot(uri=MIXS['0000030'], name="migs_ba_host_spec_range", curie=MIXS.curie('0000030'),
                   model_uri=MIXS.migs_ba_host_spec_range, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_ba_isol_growth_condt = Slot(uri=MIXS['0000003'], name="migs_ba_isol_growth_condt", curie=MIXS.curie('0000003'),
                   model_uri=MIXS.migs_ba_isol_growth_condt, domain=None, range=str)

slots.migs_ba_lat_lon = Slot(uri=MIXS['0000009'], name="migs_ba_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.migs_ba_lat_lon, domain=None, range=str)

slots.migs_ba_lib_layout = Slot(uri=MIXS['0000041'], name="migs_ba_lib_layout", curie=MIXS.curie('0000041'),
                   model_uri=MIXS.migs_ba_lib_layout, domain=None, range=Optional[str])

slots.migs_ba_lib_reads_seqd = Slot(uri=MIXS['0000040'], name="migs_ba_lib_reads_seqd", curie=MIXS.curie('0000040'),
                   model_uri=MIXS.migs_ba_lib_reads_seqd, domain=None, range=Optional[str])

slots.migs_ba_lib_screen = Slot(uri=MIXS['0000043'], name="migs_ba_lib_screen", curie=MIXS.curie('0000043'),
                   model_uri=MIXS.migs_ba_lib_screen, domain=None, range=Optional[str])

slots.migs_ba_lib_size = Slot(uri=MIXS['0000039'], name="migs_ba_lib_size", curie=MIXS.curie('0000039'),
                   model_uri=MIXS.migs_ba_lib_size, domain=None, range=Optional[str])

slots.migs_ba_lib_vector = Slot(uri=MIXS['0000042'], name="migs_ba_lib_vector", curie=MIXS.curie('0000042'),
                   model_uri=MIXS.migs_ba_lib_vector, domain=None, range=Optional[str])

slots.migs_ba_neg_cont_type = Slot(uri=MIXS['0001321'], name="migs_ba_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.migs_ba_neg_cont_type, domain=None, range=Optional[str])

slots.migs_ba_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="migs_ba_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.migs_ba_nucl_acid_amp, domain=None, range=Optional[str])

slots.migs_ba_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="migs_ba_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.migs_ba_nucl_acid_ext, domain=None, range=Optional[str])

slots.migs_ba_num_replicons = Slot(uri=MIXS['0000022'], name="migs_ba_num_replicons", curie=MIXS.curie('0000022'),
                   model_uri=MIXS.migs_ba_num_replicons, domain=None, range=str)

slots.migs_ba_number_contig = Slot(uri=MIXS['0000060'], name="migs_ba_number_contig", curie=MIXS.curie('0000060'),
                   model_uri=MIXS.migs_ba_number_contig, domain=None, range=str)

slots.migs_ba_pathogenicity = Slot(uri=MIXS['0000027'], name="migs_ba_pathogenicity", curie=MIXS.curie('0000027'),
                   model_uri=MIXS.migs_ba_pathogenicity, domain=None, range=Optional[str])

slots.migs_ba_pos_cont_type = Slot(uri=MIXS['0001322'], name="migs_ba_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.migs_ba_pos_cont_type, domain=None, range=Optional[str])

slots.migs_ba_project_name = Slot(uri=MIXS['0000092'], name="migs_ba_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.migs_ba_project_name, domain=None, range=str)

slots.migs_ba_ref_biomaterial = Slot(uri=MIXS['0000025'], name="migs_ba_ref_biomaterial", curie=MIXS.curie('0000025'),
                   model_uri=MIXS.migs_ba_ref_biomaterial, domain=None, range=str)

slots.migs_ba_ref_db = Slot(uri=MIXS['0000062'], name="migs_ba_ref_db", curie=MIXS.curie('0000062'),
                   model_uri=MIXS.migs_ba_ref_db, domain=None, range=Optional[str])

slots.migs_ba_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="migs_ba_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=MIXS.migs_ba_rel_to_oxygen, domain=None, range=Optional[str])

slots.migs_ba_samp_collec_device = Slot(uri=MIXS['0000002'], name="migs_ba_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.migs_ba_samp_collec_device, domain=None, range=Optional[str])

slots.migs_ba_samp_collec_method = Slot(uri=MIXS['0001225'], name="migs_ba_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.migs_ba_samp_collec_method, domain=None, range=Optional[str])

slots.migs_ba_samp_mat_process = Slot(uri=MIXS['0000016'], name="migs_ba_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.migs_ba_samp_mat_process, domain=None, range=Optional[str])

slots.migs_ba_samp_name = Slot(uri=MIXS['0001107'], name="migs_ba_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.migs_ba_samp_name, domain=None, range=str)

slots.migs_ba_samp_size = Slot(uri=MIXS['0000001'], name="migs_ba_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.migs_ba_samp_size, domain=None, range=Optional[str])

slots.migs_ba_samp_taxon_id = Slot(uri=MIXS['0001320'], name="migs_ba_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.migs_ba_samp_taxon_id, domain=None, range=str)

slots.migs_ba_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="migs_ba_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.migs_ba_samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.migs_ba_seq_meth = Slot(uri=MIXS['0000050'], name="migs_ba_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.migs_ba_seq_meth, domain=None, range=str)

slots.migs_ba_sim_search_meth = Slot(uri=MIXS['0000063'], name="migs_ba_sim_search_meth", curie=MIXS.curie('0000063'),
                   model_uri=MIXS.migs_ba_sim_search_meth, domain=None, range=Optional[str])

slots.migs_ba_sop = Slot(uri=MIXS['0000090'], name="migs_ba_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.migs_ba_sop, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_ba_source_mat_id = Slot(uri=MIXS['0000026'], name="migs_ba_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.migs_ba_source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_ba_specific_host = Slot(uri=MIXS['0000029'], name="migs_ba_specific_host", curie=MIXS.curie('0000029'),
                   model_uri=MIXS.migs_ba_specific_host, domain=None, range=Optional[str])

slots.migs_ba_subspecf_gen_lin = Slot(uri=MIXS['0000020'], name="migs_ba_subspecf_gen_lin", curie=MIXS.curie('0000020'),
                   model_uri=MIXS.migs_ba_subspecf_gen_lin, domain=None, range=Optional[str])

slots.migs_ba_tax_class = Slot(uri=MIXS['0000064'], name="migs_ba_tax_class", curie=MIXS.curie('0000064'),
                   model_uri=MIXS.migs_ba_tax_class, domain=None, range=Optional[str])

slots.migs_ba_tax_ident = Slot(uri=MIXS['0000053'], name="migs_ba_tax_ident", curie=MIXS.curie('0000053'),
                   model_uri=MIXS.migs_ba_tax_ident, domain=None, range=Optional[str])

slots.migs_ba_temp = Slot(uri=MIXS['0000113'], name="migs_ba_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.migs_ba_temp, domain=None, range=Optional[str])

slots.migs_ba_trophic_level = Slot(uri=MIXS['0000032'], name="migs_ba_trophic_level", curie=MIXS.curie('0000032'),
                   model_uri=MIXS.migs_ba_trophic_level, domain=None, range=Optional[str])

slots.migs_eu_adapters = Slot(uri=MIXS['0000048'], name="migs_eu_adapters", curie=MIXS.curie('0000048'),
                   model_uri=MIXS.migs_eu_adapters, domain=None, range=Optional[str])

slots.migs_eu_alt = Slot(uri=MIXS['0000094'], name="migs_eu_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.migs_eu_alt, domain=None, range=Optional[str])

slots.migs_eu_annot = Slot(uri=MIXS['0000059'], name="migs_eu_annot", curie=MIXS.curie('0000059'),
                   model_uri=MIXS.migs_eu_annot, domain=None, range=Optional[str])

slots.migs_eu_assembly_name = Slot(uri=MIXS['0000057'], name="migs_eu_assembly_name", curie=MIXS.curie('0000057'),
                   model_uri=MIXS.migs_eu_assembly_name, domain=None, range=Optional[str])

slots.migs_eu_assembly_qual = Slot(uri=MIXS['0000056'], name="migs_eu_assembly_qual", curie=MIXS.curie('0000056'),
                   model_uri=MIXS.migs_eu_assembly_qual, domain=None, range=str)

slots.migs_eu_assembly_software = Slot(uri=MIXS['0000058'], name="migs_eu_assembly_software", curie=MIXS.curie('0000058'),
                   model_uri=MIXS.migs_eu_assembly_software, domain=None, range=str)

slots.migs_eu_associated_resource = Slot(uri=MIXS['0000091'], name="migs_eu_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.migs_eu_associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_eu_biotic_relationship = Slot(uri=MIXS['0000028'], name="migs_eu_biotic_relationship", curie=MIXS.curie('0000028'),
                   model_uri=MIXS.migs_eu_biotic_relationship, domain=None, range=Optional[str])

slots.migs_eu_collection_date = Slot(uri=MIXS['0000011'], name="migs_eu_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.migs_eu_collection_date, domain=None, range=str)

slots.migs_eu_compl_score = Slot(uri=MIXS['0000069'], name="migs_eu_compl_score", curie=MIXS.curie('0000069'),
                   model_uri=MIXS.migs_eu_compl_score, domain=None, range=Optional[str])

slots.migs_eu_compl_software = Slot(uri=MIXS['0000070'], name="migs_eu_compl_software", curie=MIXS.curie('0000070'),
                   model_uri=MIXS.migs_eu_compl_software, domain=None, range=Optional[str])

slots.migs_eu_depth = Slot(uri=MIXS['0000018'], name="migs_eu_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.migs_eu_depth, domain=None, range=Optional[str])

slots.migs_eu_elev = Slot(uri=MIXS['0000093'], name="migs_eu_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.migs_eu_elev, domain=None, range=Optional[str])

slots.migs_eu_env_broad_scale = Slot(uri=MIXS['0000012'], name="migs_eu_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.migs_eu_env_broad_scale, domain=None, range=str)

slots.migs_eu_env_local_scale = Slot(uri=MIXS['0000013'], name="migs_eu_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.migs_eu_env_local_scale, domain=None, range=str)

slots.migs_eu_env_medium = Slot(uri=MIXS['0000014'], name="migs_eu_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.migs_eu_env_medium, domain=None, range=str)

slots.migs_eu_estimated_size = Slot(uri=MIXS['0000024'], name="migs_eu_estimated_size", curie=MIXS.curie('0000024'),
                   model_uri=MIXS.migs_eu_estimated_size, domain=None, range=Optional[str])

slots.migs_eu_experimental_factor = Slot(uri=MIXS['0000008'], name="migs_eu_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.migs_eu_experimental_factor, domain=None, range=Optional[str])

slots.migs_eu_extrachrom_elements = Slot(uri=MIXS['0000023'], name="migs_eu_extrachrom_elements", curie=MIXS.curie('0000023'),
                   model_uri=MIXS.migs_eu_extrachrom_elements, domain=None, range=Optional[str])

slots.migs_eu_feat_pred = Slot(uri=MIXS['0000061'], name="migs_eu_feat_pred", curie=MIXS.curie('0000061'),
                   model_uri=MIXS.migs_eu_feat_pred, domain=None, range=Optional[str])

slots.migs_eu_geo_loc_name = Slot(uri=MIXS['0000010'], name="migs_eu_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.migs_eu_geo_loc_name, domain=None, range=str)

slots.migs_eu_host_disease_stat = Slot(uri=MIXS['0000031'], name="migs_eu_host_disease_stat", curie=MIXS.curie('0000031'),
                   model_uri=MIXS.migs_eu_host_disease_stat, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_eu_host_spec_range = Slot(uri=MIXS['0000030'], name="migs_eu_host_spec_range", curie=MIXS.curie('0000030'),
                   model_uri=MIXS.migs_eu_host_spec_range, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_eu_isol_growth_condt = Slot(uri=MIXS['0000003'], name="migs_eu_isol_growth_condt", curie=MIXS.curie('0000003'),
                   model_uri=MIXS.migs_eu_isol_growth_condt, domain=None, range=str)

slots.migs_eu_lat_lon = Slot(uri=MIXS['0000009'], name="migs_eu_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.migs_eu_lat_lon, domain=None, range=str)

slots.migs_eu_lib_layout = Slot(uri=MIXS['0000041'], name="migs_eu_lib_layout", curie=MIXS.curie('0000041'),
                   model_uri=MIXS.migs_eu_lib_layout, domain=None, range=Optional[str])

slots.migs_eu_lib_reads_seqd = Slot(uri=MIXS['0000040'], name="migs_eu_lib_reads_seqd", curie=MIXS.curie('0000040'),
                   model_uri=MIXS.migs_eu_lib_reads_seqd, domain=None, range=Optional[str])

slots.migs_eu_lib_screen = Slot(uri=MIXS['0000043'], name="migs_eu_lib_screen", curie=MIXS.curie('0000043'),
                   model_uri=MIXS.migs_eu_lib_screen, domain=None, range=Optional[str])

slots.migs_eu_lib_size = Slot(uri=MIXS['0000039'], name="migs_eu_lib_size", curie=MIXS.curie('0000039'),
                   model_uri=MIXS.migs_eu_lib_size, domain=None, range=Optional[str])

slots.migs_eu_lib_vector = Slot(uri=MIXS['0000042'], name="migs_eu_lib_vector", curie=MIXS.curie('0000042'),
                   model_uri=MIXS.migs_eu_lib_vector, domain=None, range=Optional[str])

slots.migs_eu_neg_cont_type = Slot(uri=MIXS['0001321'], name="migs_eu_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.migs_eu_neg_cont_type, domain=None, range=Optional[str])

slots.migs_eu_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="migs_eu_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.migs_eu_nucl_acid_amp, domain=None, range=Optional[str])

slots.migs_eu_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="migs_eu_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.migs_eu_nucl_acid_ext, domain=None, range=Optional[str])

slots.migs_eu_num_replicons = Slot(uri=MIXS['0000022'], name="migs_eu_num_replicons", curie=MIXS.curie('0000022'),
                   model_uri=MIXS.migs_eu_num_replicons, domain=None, range=Optional[str])

slots.migs_eu_number_contig = Slot(uri=MIXS['0000060'], name="migs_eu_number_contig", curie=MIXS.curie('0000060'),
                   model_uri=MIXS.migs_eu_number_contig, domain=None, range=str)

slots.migs_eu_pathogenicity = Slot(uri=MIXS['0000027'], name="migs_eu_pathogenicity", curie=MIXS.curie('0000027'),
                   model_uri=MIXS.migs_eu_pathogenicity, domain=None, range=Optional[str])

slots.migs_eu_ploidy = Slot(uri=MIXS['0000021'], name="migs_eu_ploidy", curie=MIXS.curie('0000021'),
                   model_uri=MIXS.migs_eu_ploidy, domain=None, range=Optional[str])

slots.migs_eu_pos_cont_type = Slot(uri=MIXS['0001322'], name="migs_eu_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.migs_eu_pos_cont_type, domain=None, range=Optional[str])

slots.migs_eu_project_name = Slot(uri=MIXS['0000092'], name="migs_eu_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.migs_eu_project_name, domain=None, range=str)

slots.migs_eu_propagation = Slot(uri=MIXS['0000033'], name="migs_eu_propagation", curie=MIXS.curie('0000033'),
                   model_uri=MIXS.migs_eu_propagation, domain=None, range=Optional[str])

slots.migs_eu_ref_biomaterial = Slot(uri=MIXS['0000025'], name="migs_eu_ref_biomaterial", curie=MIXS.curie('0000025'),
                   model_uri=MIXS.migs_eu_ref_biomaterial, domain=None, range=Optional[str])

slots.migs_eu_ref_db = Slot(uri=MIXS['0000062'], name="migs_eu_ref_db", curie=MIXS.curie('0000062'),
                   model_uri=MIXS.migs_eu_ref_db, domain=None, range=Optional[str])

slots.migs_eu_samp_collec_device = Slot(uri=MIXS['0000002'], name="migs_eu_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.migs_eu_samp_collec_device, domain=None, range=Optional[str])

slots.migs_eu_samp_collec_method = Slot(uri=MIXS['0001225'], name="migs_eu_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.migs_eu_samp_collec_method, domain=None, range=Optional[str])

slots.migs_eu_samp_mat_process = Slot(uri=MIXS['0000016'], name="migs_eu_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.migs_eu_samp_mat_process, domain=None, range=Optional[str])

slots.migs_eu_samp_name = Slot(uri=MIXS['0001107'], name="migs_eu_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.migs_eu_samp_name, domain=None, range=str)

slots.migs_eu_samp_size = Slot(uri=MIXS['0000001'], name="migs_eu_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.migs_eu_samp_size, domain=None, range=Optional[str])

slots.migs_eu_samp_taxon_id = Slot(uri=MIXS['0001320'], name="migs_eu_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.migs_eu_samp_taxon_id, domain=None, range=str)

slots.migs_eu_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="migs_eu_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.migs_eu_samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.migs_eu_seq_meth = Slot(uri=MIXS['0000050'], name="migs_eu_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.migs_eu_seq_meth, domain=None, range=str)

slots.migs_eu_sim_search_meth = Slot(uri=MIXS['0000063'], name="migs_eu_sim_search_meth", curie=MIXS.curie('0000063'),
                   model_uri=MIXS.migs_eu_sim_search_meth, domain=None, range=Optional[str])

slots.migs_eu_sop = Slot(uri=MIXS['0000090'], name="migs_eu_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.migs_eu_sop, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_eu_source_mat_id = Slot(uri=MIXS['0000026'], name="migs_eu_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.migs_eu_source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_eu_specific_host = Slot(uri=MIXS['0000029'], name="migs_eu_specific_host", curie=MIXS.curie('0000029'),
                   model_uri=MIXS.migs_eu_specific_host, domain=None, range=Optional[str])

slots.migs_eu_subspecf_gen_lin = Slot(uri=MIXS['0000020'], name="migs_eu_subspecf_gen_lin", curie=MIXS.curie('0000020'),
                   model_uri=MIXS.migs_eu_subspecf_gen_lin, domain=None, range=Optional[str])

slots.migs_eu_tax_class = Slot(uri=MIXS['0000064'], name="migs_eu_tax_class", curie=MIXS.curie('0000064'),
                   model_uri=MIXS.migs_eu_tax_class, domain=None, range=Optional[str])

slots.migs_eu_tax_ident = Slot(uri=MIXS['0000053'], name="migs_eu_tax_ident", curie=MIXS.curie('0000053'),
                   model_uri=MIXS.migs_eu_tax_ident, domain=None, range=Optional[str])

slots.migs_eu_temp = Slot(uri=MIXS['0000113'], name="migs_eu_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.migs_eu_temp, domain=None, range=Optional[str])

slots.migs_eu_trophic_level = Slot(uri=MIXS['0000032'], name="migs_eu_trophic_level", curie=MIXS.curie('0000032'),
                   model_uri=MIXS.migs_eu_trophic_level, domain=None, range=Optional[str])

slots.migs_org_adapters = Slot(uri=MIXS['0000048'], name="migs_org_adapters", curie=MIXS.curie('0000048'),
                   model_uri=MIXS.migs_org_adapters, domain=None, range=Optional[str])

slots.migs_org_alt = Slot(uri=MIXS['0000094'], name="migs_org_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.migs_org_alt, domain=None, range=Optional[str])

slots.migs_org_annot = Slot(uri=MIXS['0000059'], name="migs_org_annot", curie=MIXS.curie('0000059'),
                   model_uri=MIXS.migs_org_annot, domain=None, range=Optional[str])

slots.migs_org_assembly_name = Slot(uri=MIXS['0000057'], name="migs_org_assembly_name", curie=MIXS.curie('0000057'),
                   model_uri=MIXS.migs_org_assembly_name, domain=None, range=Optional[str])

slots.migs_org_assembly_qual = Slot(uri=MIXS['0000056'], name="migs_org_assembly_qual", curie=MIXS.curie('0000056'),
                   model_uri=MIXS.migs_org_assembly_qual, domain=None, range=Optional[str])

slots.migs_org_assembly_software = Slot(uri=MIXS['0000058'], name="migs_org_assembly_software", curie=MIXS.curie('0000058'),
                   model_uri=MIXS.migs_org_assembly_software, domain=None, range=str)

slots.migs_org_associated_resource = Slot(uri=MIXS['0000091'], name="migs_org_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.migs_org_associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_org_collection_date = Slot(uri=MIXS['0000011'], name="migs_org_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.migs_org_collection_date, domain=None, range=str)

slots.migs_org_compl_score = Slot(uri=MIXS['0000069'], name="migs_org_compl_score", curie=MIXS.curie('0000069'),
                   model_uri=MIXS.migs_org_compl_score, domain=None, range=Optional[str])

slots.migs_org_compl_software = Slot(uri=MIXS['0000070'], name="migs_org_compl_software", curie=MIXS.curie('0000070'),
                   model_uri=MIXS.migs_org_compl_software, domain=None, range=Optional[str])

slots.migs_org_depth = Slot(uri=MIXS['0000018'], name="migs_org_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.migs_org_depth, domain=None, range=Optional[str])

slots.migs_org_elev = Slot(uri=MIXS['0000093'], name="migs_org_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.migs_org_elev, domain=None, range=Optional[str])

slots.migs_org_env_broad_scale = Slot(uri=MIXS['0000012'], name="migs_org_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.migs_org_env_broad_scale, domain=None, range=str)

slots.migs_org_env_local_scale = Slot(uri=MIXS['0000013'], name="migs_org_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.migs_org_env_local_scale, domain=None, range=str)

slots.migs_org_env_medium = Slot(uri=MIXS['0000014'], name="migs_org_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.migs_org_env_medium, domain=None, range=str)

slots.migs_org_estimated_size = Slot(uri=MIXS['0000024'], name="migs_org_estimated_size", curie=MIXS.curie('0000024'),
                   model_uri=MIXS.migs_org_estimated_size, domain=None, range=Optional[str])

slots.migs_org_experimental_factor = Slot(uri=MIXS['0000008'], name="migs_org_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.migs_org_experimental_factor, domain=None, range=Optional[str])

slots.migs_org_extrachrom_elements = Slot(uri=MIXS['0000023'], name="migs_org_extrachrom_elements", curie=MIXS.curie('0000023'),
                   model_uri=MIXS.migs_org_extrachrom_elements, domain=None, range=Optional[str])

slots.migs_org_feat_pred = Slot(uri=MIXS['0000061'], name="migs_org_feat_pred", curie=MIXS.curie('0000061'),
                   model_uri=MIXS.migs_org_feat_pred, domain=None, range=Optional[str])

slots.migs_org_geo_loc_name = Slot(uri=MIXS['0000010'], name="migs_org_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.migs_org_geo_loc_name, domain=None, range=str)

slots.migs_org_isol_growth_condt = Slot(uri=MIXS['0000003'], name="migs_org_isol_growth_condt", curie=MIXS.curie('0000003'),
                   model_uri=MIXS.migs_org_isol_growth_condt, domain=None, range=str)

slots.migs_org_lat_lon = Slot(uri=MIXS['0000009'], name="migs_org_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.migs_org_lat_lon, domain=None, range=str)

slots.migs_org_lib_layout = Slot(uri=MIXS['0000041'], name="migs_org_lib_layout", curie=MIXS.curie('0000041'),
                   model_uri=MIXS.migs_org_lib_layout, domain=None, range=Optional[str])

slots.migs_org_lib_reads_seqd = Slot(uri=MIXS['0000040'], name="migs_org_lib_reads_seqd", curie=MIXS.curie('0000040'),
                   model_uri=MIXS.migs_org_lib_reads_seqd, domain=None, range=Optional[str])

slots.migs_org_lib_screen = Slot(uri=MIXS['0000043'], name="migs_org_lib_screen", curie=MIXS.curie('0000043'),
                   model_uri=MIXS.migs_org_lib_screen, domain=None, range=Optional[str])

slots.migs_org_lib_size = Slot(uri=MIXS['0000039'], name="migs_org_lib_size", curie=MIXS.curie('0000039'),
                   model_uri=MIXS.migs_org_lib_size, domain=None, range=Optional[str])

slots.migs_org_lib_vector = Slot(uri=MIXS['0000042'], name="migs_org_lib_vector", curie=MIXS.curie('0000042'),
                   model_uri=MIXS.migs_org_lib_vector, domain=None, range=Optional[str])

slots.migs_org_neg_cont_type = Slot(uri=MIXS['0001321'], name="migs_org_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.migs_org_neg_cont_type, domain=None, range=Optional[str])

slots.migs_org_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="migs_org_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.migs_org_nucl_acid_amp, domain=None, range=Optional[str])

slots.migs_org_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="migs_org_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.migs_org_nucl_acid_ext, domain=None, range=Optional[str])

slots.migs_org_number_contig = Slot(uri=MIXS['0000060'], name="migs_org_number_contig", curie=MIXS.curie('0000060'),
                   model_uri=MIXS.migs_org_number_contig, domain=None, range=Optional[str])

slots.migs_org_pos_cont_type = Slot(uri=MIXS['0001322'], name="migs_org_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.migs_org_pos_cont_type, domain=None, range=Optional[str])

slots.migs_org_project_name = Slot(uri=MIXS['0000092'], name="migs_org_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.migs_org_project_name, domain=None, range=str)

slots.migs_org_ref_biomaterial = Slot(uri=MIXS['0000025'], name="migs_org_ref_biomaterial", curie=MIXS.curie('0000025'),
                   model_uri=MIXS.migs_org_ref_biomaterial, domain=None, range=Optional[str])

slots.migs_org_ref_db = Slot(uri=MIXS['0000062'], name="migs_org_ref_db", curie=MIXS.curie('0000062'),
                   model_uri=MIXS.migs_org_ref_db, domain=None, range=Optional[str])

slots.migs_org_samp_collec_device = Slot(uri=MIXS['0000002'], name="migs_org_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.migs_org_samp_collec_device, domain=None, range=Optional[str])

slots.migs_org_samp_collec_method = Slot(uri=MIXS['0001225'], name="migs_org_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.migs_org_samp_collec_method, domain=None, range=Optional[str])

slots.migs_org_samp_mat_process = Slot(uri=MIXS['0000016'], name="migs_org_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.migs_org_samp_mat_process, domain=None, range=Optional[str])

slots.migs_org_samp_name = Slot(uri=MIXS['0001107'], name="migs_org_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.migs_org_samp_name, domain=None, range=str)

slots.migs_org_samp_size = Slot(uri=MIXS['0000001'], name="migs_org_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.migs_org_samp_size, domain=None, range=Optional[str])

slots.migs_org_samp_taxon_id = Slot(uri=MIXS['0001320'], name="migs_org_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.migs_org_samp_taxon_id, domain=None, range=str)

slots.migs_org_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="migs_org_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.migs_org_samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.migs_org_seq_meth = Slot(uri=MIXS['0000050'], name="migs_org_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.migs_org_seq_meth, domain=None, range=str)

slots.migs_org_sim_search_meth = Slot(uri=MIXS['0000063'], name="migs_org_sim_search_meth", curie=MIXS.curie('0000063'),
                   model_uri=MIXS.migs_org_sim_search_meth, domain=None, range=Optional[str])

slots.migs_org_sop = Slot(uri=MIXS['0000090'], name="migs_org_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.migs_org_sop, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_org_source_mat_id = Slot(uri=MIXS['0000026'], name="migs_org_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.migs_org_source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_org_subspecf_gen_lin = Slot(uri=MIXS['0000020'], name="migs_org_subspecf_gen_lin", curie=MIXS.curie('0000020'),
                   model_uri=MIXS.migs_org_subspecf_gen_lin, domain=None, range=Optional[str])

slots.migs_org_tax_class = Slot(uri=MIXS['0000064'], name="migs_org_tax_class", curie=MIXS.curie('0000064'),
                   model_uri=MIXS.migs_org_tax_class, domain=None, range=Optional[str])

slots.migs_org_tax_ident = Slot(uri=MIXS['0000053'], name="migs_org_tax_ident", curie=MIXS.curie('0000053'),
                   model_uri=MIXS.migs_org_tax_ident, domain=None, range=Optional[str])

slots.migs_org_temp = Slot(uri=MIXS['0000113'], name="migs_org_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.migs_org_temp, domain=None, range=Optional[str])

slots.migs_pl_adapters = Slot(uri=MIXS['0000048'], name="migs_pl_adapters", curie=MIXS.curie('0000048'),
                   model_uri=MIXS.migs_pl_adapters, domain=None, range=Optional[str])

slots.migs_pl_alt = Slot(uri=MIXS['0000094'], name="migs_pl_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.migs_pl_alt, domain=None, range=Optional[str])

slots.migs_pl_annot = Slot(uri=MIXS['0000059'], name="migs_pl_annot", curie=MIXS.curie('0000059'),
                   model_uri=MIXS.migs_pl_annot, domain=None, range=Optional[str])

slots.migs_pl_assembly_name = Slot(uri=MIXS['0000057'], name="migs_pl_assembly_name", curie=MIXS.curie('0000057'),
                   model_uri=MIXS.migs_pl_assembly_name, domain=None, range=Optional[str])

slots.migs_pl_assembly_qual = Slot(uri=MIXS['0000056'], name="migs_pl_assembly_qual", curie=MIXS.curie('0000056'),
                   model_uri=MIXS.migs_pl_assembly_qual, domain=None, range=Optional[str])

slots.migs_pl_assembly_software = Slot(uri=MIXS['0000058'], name="migs_pl_assembly_software", curie=MIXS.curie('0000058'),
                   model_uri=MIXS.migs_pl_assembly_software, domain=None, range=str)

slots.migs_pl_associated_resource = Slot(uri=MIXS['0000091'], name="migs_pl_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.migs_pl_associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_pl_collection_date = Slot(uri=MIXS['0000011'], name="migs_pl_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.migs_pl_collection_date, domain=None, range=str)

slots.migs_pl_compl_score = Slot(uri=MIXS['0000069'], name="migs_pl_compl_score", curie=MIXS.curie('0000069'),
                   model_uri=MIXS.migs_pl_compl_score, domain=None, range=Optional[str])

slots.migs_pl_compl_software = Slot(uri=MIXS['0000070'], name="migs_pl_compl_software", curie=MIXS.curie('0000070'),
                   model_uri=MIXS.migs_pl_compl_software, domain=None, range=Optional[str])

slots.migs_pl_depth = Slot(uri=MIXS['0000018'], name="migs_pl_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.migs_pl_depth, domain=None, range=Optional[str])

slots.migs_pl_elev = Slot(uri=MIXS['0000093'], name="migs_pl_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.migs_pl_elev, domain=None, range=Optional[str])

slots.migs_pl_encoded_traits = Slot(uri=MIXS['0000034'], name="migs_pl_encoded_traits", curie=MIXS.curie('0000034'),
                   model_uri=MIXS.migs_pl_encoded_traits, domain=None, range=Optional[str])

slots.migs_pl_env_broad_scale = Slot(uri=MIXS['0000012'], name="migs_pl_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.migs_pl_env_broad_scale, domain=None, range=str)

slots.migs_pl_env_local_scale = Slot(uri=MIXS['0000013'], name="migs_pl_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.migs_pl_env_local_scale, domain=None, range=str)

slots.migs_pl_env_medium = Slot(uri=MIXS['0000014'], name="migs_pl_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.migs_pl_env_medium, domain=None, range=str)

slots.migs_pl_estimated_size = Slot(uri=MIXS['0000024'], name="migs_pl_estimated_size", curie=MIXS.curie('0000024'),
                   model_uri=MIXS.migs_pl_estimated_size, domain=None, range=Optional[str])

slots.migs_pl_experimental_factor = Slot(uri=MIXS['0000008'], name="migs_pl_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.migs_pl_experimental_factor, domain=None, range=Optional[str])

slots.migs_pl_feat_pred = Slot(uri=MIXS['0000061'], name="migs_pl_feat_pred", curie=MIXS.curie('0000061'),
                   model_uri=MIXS.migs_pl_feat_pred, domain=None, range=Optional[str])

slots.migs_pl_geo_loc_name = Slot(uri=MIXS['0000010'], name="migs_pl_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.migs_pl_geo_loc_name, domain=None, range=str)

slots.migs_pl_host_spec_range = Slot(uri=MIXS['0000030'], name="migs_pl_host_spec_range", curie=MIXS.curie('0000030'),
                   model_uri=MIXS.migs_pl_host_spec_range, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_pl_isol_growth_condt = Slot(uri=MIXS['0000003'], name="migs_pl_isol_growth_condt", curie=MIXS.curie('0000003'),
                   model_uri=MIXS.migs_pl_isol_growth_condt, domain=None, range=str)

slots.migs_pl_lat_lon = Slot(uri=MIXS['0000009'], name="migs_pl_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.migs_pl_lat_lon, domain=None, range=str)

slots.migs_pl_lib_layout = Slot(uri=MIXS['0000041'], name="migs_pl_lib_layout", curie=MIXS.curie('0000041'),
                   model_uri=MIXS.migs_pl_lib_layout, domain=None, range=Optional[str])

slots.migs_pl_lib_reads_seqd = Slot(uri=MIXS['0000040'], name="migs_pl_lib_reads_seqd", curie=MIXS.curie('0000040'),
                   model_uri=MIXS.migs_pl_lib_reads_seqd, domain=None, range=Optional[str])

slots.migs_pl_lib_screen = Slot(uri=MIXS['0000043'], name="migs_pl_lib_screen", curie=MIXS.curie('0000043'),
                   model_uri=MIXS.migs_pl_lib_screen, domain=None, range=Optional[str])

slots.migs_pl_lib_size = Slot(uri=MIXS['0000039'], name="migs_pl_lib_size", curie=MIXS.curie('0000039'),
                   model_uri=MIXS.migs_pl_lib_size, domain=None, range=Optional[str])

slots.migs_pl_lib_vector = Slot(uri=MIXS['0000042'], name="migs_pl_lib_vector", curie=MIXS.curie('0000042'),
                   model_uri=MIXS.migs_pl_lib_vector, domain=None, range=Optional[str])

slots.migs_pl_neg_cont_type = Slot(uri=MIXS['0001321'], name="migs_pl_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.migs_pl_neg_cont_type, domain=None, range=Optional[str])

slots.migs_pl_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="migs_pl_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.migs_pl_nucl_acid_amp, domain=None, range=Optional[str])

slots.migs_pl_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="migs_pl_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.migs_pl_nucl_acid_ext, domain=None, range=Optional[str])

slots.migs_pl_number_contig = Slot(uri=MIXS['0000060'], name="migs_pl_number_contig", curie=MIXS.curie('0000060'),
                   model_uri=MIXS.migs_pl_number_contig, domain=None, range=Optional[str])

slots.migs_pl_pos_cont_type = Slot(uri=MIXS['0001322'], name="migs_pl_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.migs_pl_pos_cont_type, domain=None, range=Optional[str])

slots.migs_pl_project_name = Slot(uri=MIXS['0000092'], name="migs_pl_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.migs_pl_project_name, domain=None, range=str)

slots.migs_pl_propagation = Slot(uri=MIXS['0000033'], name="migs_pl_propagation", curie=MIXS.curie('0000033'),
                   model_uri=MIXS.migs_pl_propagation, domain=None, range=str)

slots.migs_pl_ref_biomaterial = Slot(uri=MIXS['0000025'], name="migs_pl_ref_biomaterial", curie=MIXS.curie('0000025'),
                   model_uri=MIXS.migs_pl_ref_biomaterial, domain=None, range=Optional[str])

slots.migs_pl_ref_db = Slot(uri=MIXS['0000062'], name="migs_pl_ref_db", curie=MIXS.curie('0000062'),
                   model_uri=MIXS.migs_pl_ref_db, domain=None, range=Optional[str])

slots.migs_pl_samp_collec_device = Slot(uri=MIXS['0000002'], name="migs_pl_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.migs_pl_samp_collec_device, domain=None, range=Optional[str])

slots.migs_pl_samp_collec_method = Slot(uri=MIXS['0001225'], name="migs_pl_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.migs_pl_samp_collec_method, domain=None, range=Optional[str])

slots.migs_pl_samp_mat_process = Slot(uri=MIXS['0000016'], name="migs_pl_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.migs_pl_samp_mat_process, domain=None, range=Optional[str])

slots.migs_pl_samp_name = Slot(uri=MIXS['0001107'], name="migs_pl_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.migs_pl_samp_name, domain=None, range=str)

slots.migs_pl_samp_size = Slot(uri=MIXS['0000001'], name="migs_pl_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.migs_pl_samp_size, domain=None, range=Optional[str])

slots.migs_pl_samp_taxon_id = Slot(uri=MIXS['0001320'], name="migs_pl_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.migs_pl_samp_taxon_id, domain=None, range=str)

slots.migs_pl_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="migs_pl_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.migs_pl_samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.migs_pl_seq_meth = Slot(uri=MIXS['0000050'], name="migs_pl_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.migs_pl_seq_meth, domain=None, range=str)

slots.migs_pl_sim_search_meth = Slot(uri=MIXS['0000063'], name="migs_pl_sim_search_meth", curie=MIXS.curie('0000063'),
                   model_uri=MIXS.migs_pl_sim_search_meth, domain=None, range=Optional[str])

slots.migs_pl_sop = Slot(uri=MIXS['0000090'], name="migs_pl_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.migs_pl_sop, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_pl_source_mat_id = Slot(uri=MIXS['0000026'], name="migs_pl_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.migs_pl_source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_pl_specific_host = Slot(uri=MIXS['0000029'], name="migs_pl_specific_host", curie=MIXS.curie('0000029'),
                   model_uri=MIXS.migs_pl_specific_host, domain=None, range=Optional[str])

slots.migs_pl_subspecf_gen_lin = Slot(uri=MIXS['0000020'], name="migs_pl_subspecf_gen_lin", curie=MIXS.curie('0000020'),
                   model_uri=MIXS.migs_pl_subspecf_gen_lin, domain=None, range=Optional[str])

slots.migs_pl_tax_class = Slot(uri=MIXS['0000064'], name="migs_pl_tax_class", curie=MIXS.curie('0000064'),
                   model_uri=MIXS.migs_pl_tax_class, domain=None, range=Optional[str])

slots.migs_pl_tax_ident = Slot(uri=MIXS['0000053'], name="migs_pl_tax_ident", curie=MIXS.curie('0000053'),
                   model_uri=MIXS.migs_pl_tax_ident, domain=None, range=Optional[str])

slots.migs_pl_temp = Slot(uri=MIXS['0000113'], name="migs_pl_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.migs_pl_temp, domain=None, range=Optional[str])

slots.migs_vi_adapters = Slot(uri=MIXS['0000048'], name="migs_vi_adapters", curie=MIXS.curie('0000048'),
                   model_uri=MIXS.migs_vi_adapters, domain=None, range=Optional[str])

slots.migs_vi_alt = Slot(uri=MIXS['0000094'], name="migs_vi_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.migs_vi_alt, domain=None, range=Optional[str])

slots.migs_vi_annot = Slot(uri=MIXS['0000059'], name="migs_vi_annot", curie=MIXS.curie('0000059'),
                   model_uri=MIXS.migs_vi_annot, domain=None, range=Optional[str])

slots.migs_vi_assembly_name = Slot(uri=MIXS['0000057'], name="migs_vi_assembly_name", curie=MIXS.curie('0000057'),
                   model_uri=MIXS.migs_vi_assembly_name, domain=None, range=Optional[str])

slots.migs_vi_assembly_qual = Slot(uri=MIXS['0000056'], name="migs_vi_assembly_qual", curie=MIXS.curie('0000056'),
                   model_uri=MIXS.migs_vi_assembly_qual, domain=None, range=Optional[str])

slots.migs_vi_assembly_software = Slot(uri=MIXS['0000058'], name="migs_vi_assembly_software", curie=MIXS.curie('0000058'),
                   model_uri=MIXS.migs_vi_assembly_software, domain=None, range=str)

slots.migs_vi_associated_resource = Slot(uri=MIXS['0000091'], name="migs_vi_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.migs_vi_associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_vi_biotic_relationship = Slot(uri=MIXS['0000028'], name="migs_vi_biotic_relationship", curie=MIXS.curie('0000028'),
                   model_uri=MIXS.migs_vi_biotic_relationship, domain=None, range=Optional[str])

slots.migs_vi_collection_date = Slot(uri=MIXS['0000011'], name="migs_vi_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.migs_vi_collection_date, domain=None, range=str)

slots.migs_vi_compl_score = Slot(uri=MIXS['0000069'], name="migs_vi_compl_score", curie=MIXS.curie('0000069'),
                   model_uri=MIXS.migs_vi_compl_score, domain=None, range=Optional[str])

slots.migs_vi_compl_software = Slot(uri=MIXS['0000070'], name="migs_vi_compl_software", curie=MIXS.curie('0000070'),
                   model_uri=MIXS.migs_vi_compl_software, domain=None, range=Optional[str])

slots.migs_vi_depth = Slot(uri=MIXS['0000018'], name="migs_vi_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.migs_vi_depth, domain=None, range=Optional[str])

slots.migs_vi_elev = Slot(uri=MIXS['0000093'], name="migs_vi_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.migs_vi_elev, domain=None, range=Optional[str])

slots.migs_vi_encoded_traits = Slot(uri=MIXS['0000034'], name="migs_vi_encoded_traits", curie=MIXS.curie('0000034'),
                   model_uri=MIXS.migs_vi_encoded_traits, domain=None, range=Optional[str])

slots.migs_vi_env_broad_scale = Slot(uri=MIXS['0000012'], name="migs_vi_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.migs_vi_env_broad_scale, domain=None, range=str)

slots.migs_vi_env_local_scale = Slot(uri=MIXS['0000013'], name="migs_vi_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.migs_vi_env_local_scale, domain=None, range=str)

slots.migs_vi_env_medium = Slot(uri=MIXS['0000014'], name="migs_vi_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.migs_vi_env_medium, domain=None, range=str)

slots.migs_vi_estimated_size = Slot(uri=MIXS['0000024'], name="migs_vi_estimated_size", curie=MIXS.curie('0000024'),
                   model_uri=MIXS.migs_vi_estimated_size, domain=None, range=Optional[str])

slots.migs_vi_experimental_factor = Slot(uri=MIXS['0000008'], name="migs_vi_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.migs_vi_experimental_factor, domain=None, range=Optional[str])

slots.migs_vi_feat_pred = Slot(uri=MIXS['0000061'], name="migs_vi_feat_pred", curie=MIXS.curie('0000061'),
                   model_uri=MIXS.migs_vi_feat_pred, domain=None, range=Optional[str])

slots.migs_vi_geo_loc_name = Slot(uri=MIXS['0000010'], name="migs_vi_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.migs_vi_geo_loc_name, domain=None, range=str)

slots.migs_vi_host_disease_stat = Slot(uri=MIXS['0000031'], name="migs_vi_host_disease_stat", curie=MIXS.curie('0000031'),
                   model_uri=MIXS.migs_vi_host_disease_stat, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_vi_host_spec_range = Slot(uri=MIXS['0000030'], name="migs_vi_host_spec_range", curie=MIXS.curie('0000030'),
                   model_uri=MIXS.migs_vi_host_spec_range, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_vi_isol_growth_condt = Slot(uri=MIXS['0000003'], name="migs_vi_isol_growth_condt", curie=MIXS.curie('0000003'),
                   model_uri=MIXS.migs_vi_isol_growth_condt, domain=None, range=str)

slots.migs_vi_lat_lon = Slot(uri=MIXS['0000009'], name="migs_vi_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.migs_vi_lat_lon, domain=None, range=str)

slots.migs_vi_lib_layout = Slot(uri=MIXS['0000041'], name="migs_vi_lib_layout", curie=MIXS.curie('0000041'),
                   model_uri=MIXS.migs_vi_lib_layout, domain=None, range=Optional[str])

slots.migs_vi_lib_reads_seqd = Slot(uri=MIXS['0000040'], name="migs_vi_lib_reads_seqd", curie=MIXS.curie('0000040'),
                   model_uri=MIXS.migs_vi_lib_reads_seqd, domain=None, range=Optional[str])

slots.migs_vi_lib_screen = Slot(uri=MIXS['0000043'], name="migs_vi_lib_screen", curie=MIXS.curie('0000043'),
                   model_uri=MIXS.migs_vi_lib_screen, domain=None, range=Optional[str])

slots.migs_vi_lib_size = Slot(uri=MIXS['0000039'], name="migs_vi_lib_size", curie=MIXS.curie('0000039'),
                   model_uri=MIXS.migs_vi_lib_size, domain=None, range=Optional[str])

slots.migs_vi_lib_vector = Slot(uri=MIXS['0000042'], name="migs_vi_lib_vector", curie=MIXS.curie('0000042'),
                   model_uri=MIXS.migs_vi_lib_vector, domain=None, range=Optional[str])

slots.migs_vi_neg_cont_type = Slot(uri=MIXS['0001321'], name="migs_vi_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.migs_vi_neg_cont_type, domain=None, range=Optional[str])

slots.migs_vi_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="migs_vi_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.migs_vi_nucl_acid_amp, domain=None, range=Optional[str])

slots.migs_vi_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="migs_vi_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.migs_vi_nucl_acid_ext, domain=None, range=Optional[str])

slots.migs_vi_num_replicons = Slot(uri=MIXS['0000022'], name="migs_vi_num_replicons", curie=MIXS.curie('0000022'),
                   model_uri=MIXS.migs_vi_num_replicons, domain=None, range=Optional[str])

slots.migs_vi_number_contig = Slot(uri=MIXS['0000060'], name="migs_vi_number_contig", curie=MIXS.curie('0000060'),
                   model_uri=MIXS.migs_vi_number_contig, domain=None, range=Optional[str])

slots.migs_vi_pathogenicity = Slot(uri=MIXS['0000027'], name="migs_vi_pathogenicity", curie=MIXS.curie('0000027'),
                   model_uri=MIXS.migs_vi_pathogenicity, domain=None, range=Optional[str])

slots.migs_vi_pos_cont_type = Slot(uri=MIXS['0001322'], name="migs_vi_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.migs_vi_pos_cont_type, domain=None, range=Optional[str])

slots.migs_vi_project_name = Slot(uri=MIXS['0000092'], name="migs_vi_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.migs_vi_project_name, domain=None, range=str)

slots.migs_vi_propagation = Slot(uri=MIXS['0000033'], name="migs_vi_propagation", curie=MIXS.curie('0000033'),
                   model_uri=MIXS.migs_vi_propagation, domain=None, range=str)

slots.migs_vi_ref_biomaterial = Slot(uri=MIXS['0000025'], name="migs_vi_ref_biomaterial", curie=MIXS.curie('0000025'),
                   model_uri=MIXS.migs_vi_ref_biomaterial, domain=None, range=Optional[str])

slots.migs_vi_ref_db = Slot(uri=MIXS['0000062'], name="migs_vi_ref_db", curie=MIXS.curie('0000062'),
                   model_uri=MIXS.migs_vi_ref_db, domain=None, range=Optional[str])

slots.migs_vi_samp_collec_device = Slot(uri=MIXS['0000002'], name="migs_vi_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.migs_vi_samp_collec_device, domain=None, range=Optional[str])

slots.migs_vi_samp_collec_method = Slot(uri=MIXS['0001225'], name="migs_vi_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.migs_vi_samp_collec_method, domain=None, range=Optional[str])

slots.migs_vi_samp_mat_process = Slot(uri=MIXS['0000016'], name="migs_vi_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.migs_vi_samp_mat_process, domain=None, range=Optional[str])

slots.migs_vi_samp_name = Slot(uri=MIXS['0001107'], name="migs_vi_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.migs_vi_samp_name, domain=None, range=str)

slots.migs_vi_samp_size = Slot(uri=MIXS['0000001'], name="migs_vi_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.migs_vi_samp_size, domain=None, range=Optional[str])

slots.migs_vi_samp_taxon_id = Slot(uri=MIXS['0001320'], name="migs_vi_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.migs_vi_samp_taxon_id, domain=None, range=str)

slots.migs_vi_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="migs_vi_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.migs_vi_samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.migs_vi_seq_meth = Slot(uri=MIXS['0000050'], name="migs_vi_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.migs_vi_seq_meth, domain=None, range=str)

slots.migs_vi_sim_search_meth = Slot(uri=MIXS['0000063'], name="migs_vi_sim_search_meth", curie=MIXS.curie('0000063'),
                   model_uri=MIXS.migs_vi_sim_search_meth, domain=None, range=Optional[str])

slots.migs_vi_sop = Slot(uri=MIXS['0000090'], name="migs_vi_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.migs_vi_sop, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_vi_source_mat_id = Slot(uri=MIXS['0000026'], name="migs_vi_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.migs_vi_source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.migs_vi_specific_host = Slot(uri=MIXS['0000029'], name="migs_vi_specific_host", curie=MIXS.curie('0000029'),
                   model_uri=MIXS.migs_vi_specific_host, domain=None, range=Optional[str])

slots.migs_vi_subspecf_gen_lin = Slot(uri=MIXS['0000020'], name="migs_vi_subspecf_gen_lin", curie=MIXS.curie('0000020'),
                   model_uri=MIXS.migs_vi_subspecf_gen_lin, domain=None, range=Optional[str])

slots.migs_vi_tax_class = Slot(uri=MIXS['0000064'], name="migs_vi_tax_class", curie=MIXS.curie('0000064'),
                   model_uri=MIXS.migs_vi_tax_class, domain=None, range=Optional[str])

slots.migs_vi_tax_ident = Slot(uri=MIXS['0000053'], name="migs_vi_tax_ident", curie=MIXS.curie('0000053'),
                   model_uri=MIXS.migs_vi_tax_ident, domain=None, range=Optional[str])

slots.migs_vi_temp = Slot(uri=MIXS['0000113'], name="migs_vi_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.migs_vi_temp, domain=None, range=Optional[str])

slots.migs_vi_virus_enrich_appr = Slot(uri=MIXS['0000036'], name="migs_vi_virus_enrich_appr", curie=MIXS.curie('0000036'),
                   model_uri=MIXS.migs_vi_virus_enrich_appr, domain=None, range=Optional[str])

slots.mimag_x_16s_recover = Slot(uri=MIXS['0000065'], name="mimag_x_16s_recover", curie=MIXS.curie('0000065'),
                   model_uri=MIXS.mimag_x_16s_recover, domain=None, range=Optional[str])

slots.mimag_x_16s_recover_software = Slot(uri=MIXS['0000066'], name="mimag_x_16s_recover_software", curie=MIXS.curie('0000066'),
                   model_uri=MIXS.mimag_x_16s_recover_software, domain=None, range=Optional[str])

slots.mimag_adapters = Slot(uri=MIXS['0000048'], name="mimag_adapters", curie=MIXS.curie('0000048'),
                   model_uri=MIXS.mimag_adapters, domain=None, range=Optional[str])

slots.mimag_alt = Slot(uri=MIXS['0000094'], name="mimag_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.mimag_alt, domain=None, range=Optional[str])

slots.mimag_annot = Slot(uri=MIXS['0000059'], name="mimag_annot", curie=MIXS.curie('0000059'),
                   model_uri=MIXS.mimag_annot, domain=None, range=Optional[str])

slots.mimag_assembly_name = Slot(uri=MIXS['0000057'], name="mimag_assembly_name", curie=MIXS.curie('0000057'),
                   model_uri=MIXS.mimag_assembly_name, domain=None, range=Optional[str])

slots.mimag_assembly_qual = Slot(uri=MIXS['0000056'], name="mimag_assembly_qual", curie=MIXS.curie('0000056'),
                   model_uri=MIXS.mimag_assembly_qual, domain=None, range=str)

slots.mimag_assembly_software = Slot(uri=MIXS['0000058'], name="mimag_assembly_software", curie=MIXS.curie('0000058'),
                   model_uri=MIXS.mimag_assembly_software, domain=None, range=str)

slots.mimag_associated_resource = Slot(uri=MIXS['0000091'], name="mimag_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.mimag_associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.mimag_bin_param = Slot(uri=MIXS['0000077'], name="mimag_bin_param", curie=MIXS.curie('0000077'),
                   model_uri=MIXS.mimag_bin_param, domain=None, range=str)

slots.mimag_bin_software = Slot(uri=MIXS['0000078'], name="mimag_bin_software", curie=MIXS.curie('0000078'),
                   model_uri=MIXS.mimag_bin_software, domain=None, range=str)

slots.mimag_collection_date = Slot(uri=MIXS['0000011'], name="mimag_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.mimag_collection_date, domain=None, range=str)

slots.mimag_compl_appr = Slot(uri=MIXS['0000071'], name="mimag_compl_appr", curie=MIXS.curie('0000071'),
                   model_uri=MIXS.mimag_compl_appr, domain=None, range=Optional[str])

slots.mimag_compl_score = Slot(uri=MIXS['0000069'], name="mimag_compl_score", curie=MIXS.curie('0000069'),
                   model_uri=MIXS.mimag_compl_score, domain=None, range=str)

slots.mimag_compl_software = Slot(uri=MIXS['0000070'], name="mimag_compl_software", curie=MIXS.curie('0000070'),
                   model_uri=MIXS.mimag_compl_software, domain=None, range=str)

slots.mimag_contam_score = Slot(uri=MIXS['0000072'], name="mimag_contam_score", curie=MIXS.curie('0000072'),
                   model_uri=MIXS.mimag_contam_score, domain=None, range=str)

slots.mimag_contam_screen_input = Slot(uri=MIXS['0000005'], name="mimag_contam_screen_input", curie=MIXS.curie('0000005'),
                   model_uri=MIXS.mimag_contam_screen_input, domain=None, range=Optional[str])

slots.mimag_contam_screen_param = Slot(uri=MIXS['0000073'], name="mimag_contam_screen_param", curie=MIXS.curie('0000073'),
                   model_uri=MIXS.mimag_contam_screen_param, domain=None, range=Optional[str])

slots.mimag_decontam_software = Slot(uri=MIXS['0000074'], name="mimag_decontam_software", curie=MIXS.curie('0000074'),
                   model_uri=MIXS.mimag_decontam_software, domain=None, range=Optional[str])

slots.mimag_depth = Slot(uri=MIXS['0000018'], name="mimag_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.mimag_depth, domain=None, range=Optional[str])

slots.mimag_elev = Slot(uri=MIXS['0000093'], name="mimag_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.mimag_elev, domain=None, range=Optional[str])

slots.mimag_env_broad_scale = Slot(uri=MIXS['0000012'], name="mimag_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.mimag_env_broad_scale, domain=None, range=str)

slots.mimag_env_local_scale = Slot(uri=MIXS['0000013'], name="mimag_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.mimag_env_local_scale, domain=None, range=str)

slots.mimag_env_medium = Slot(uri=MIXS['0000014'], name="mimag_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.mimag_env_medium, domain=None, range=str)

slots.mimag_experimental_factor = Slot(uri=MIXS['0000008'], name="mimag_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.mimag_experimental_factor, domain=None, range=Optional[str])

slots.mimag_feat_pred = Slot(uri=MIXS['0000061'], name="mimag_feat_pred", curie=MIXS.curie('0000061'),
                   model_uri=MIXS.mimag_feat_pred, domain=None, range=Optional[str])

slots.mimag_geo_loc_name = Slot(uri=MIXS['0000010'], name="mimag_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.mimag_geo_loc_name, domain=None, range=str)

slots.mimag_lat_lon = Slot(uri=MIXS['0000009'], name="mimag_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.mimag_lat_lon, domain=None, range=str)

slots.mimag_lib_layout = Slot(uri=MIXS['0000041'], name="mimag_lib_layout", curie=MIXS.curie('0000041'),
                   model_uri=MIXS.mimag_lib_layout, domain=None, range=Optional[str])

slots.mimag_lib_reads_seqd = Slot(uri=MIXS['0000040'], name="mimag_lib_reads_seqd", curie=MIXS.curie('0000040'),
                   model_uri=MIXS.mimag_lib_reads_seqd, domain=None, range=Optional[str])

slots.mimag_lib_screen = Slot(uri=MIXS['0000043'], name="mimag_lib_screen", curie=MIXS.curie('0000043'),
                   model_uri=MIXS.mimag_lib_screen, domain=None, range=Optional[str])

slots.mimag_lib_size = Slot(uri=MIXS['0000039'], name="mimag_lib_size", curie=MIXS.curie('0000039'),
                   model_uri=MIXS.mimag_lib_size, domain=None, range=Optional[str])

slots.mimag_lib_vector = Slot(uri=MIXS['0000042'], name="mimag_lib_vector", curie=MIXS.curie('0000042'),
                   model_uri=MIXS.mimag_lib_vector, domain=None, range=Optional[str])

slots.mimag_mag_cov_software = Slot(uri=MIXS['0000080'], name="mimag_mag_cov_software", curie=MIXS.curie('0000080'),
                   model_uri=MIXS.mimag_mag_cov_software, domain=None, range=Optional[str])

slots.mimag_mid = Slot(uri=MIXS['0000047'], name="mimag_mid", curie=MIXS.curie('0000047'),
                   model_uri=MIXS.mimag_mid, domain=None, range=Optional[str])

slots.mimag_neg_cont_type = Slot(uri=MIXS['0001321'], name="mimag_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.mimag_neg_cont_type, domain=None, range=Optional[str])

slots.mimag_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="mimag_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.mimag_nucl_acid_amp, domain=None, range=Optional[str])

slots.mimag_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="mimag_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.mimag_nucl_acid_ext, domain=None, range=Optional[str])

slots.mimag_number_contig = Slot(uri=MIXS['0000060'], name="mimag_number_contig", curie=MIXS.curie('0000060'),
                   model_uri=MIXS.mimag_number_contig, domain=None, range=Optional[str])

slots.mimag_pos_cont_type = Slot(uri=MIXS['0001322'], name="mimag_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.mimag_pos_cont_type, domain=None, range=Optional[str])

slots.mimag_project_name = Slot(uri=MIXS['0000092'], name="mimag_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.mimag_project_name, domain=None, range=str)

slots.mimag_reassembly_bin = Slot(uri=MIXS['0000079'], name="mimag_reassembly_bin", curie=MIXS.curie('0000079'),
                   model_uri=MIXS.mimag_reassembly_bin, domain=None, range=Optional[str])

slots.mimag_ref_biomaterial = Slot(uri=MIXS['0000025'], name="mimag_ref_biomaterial", curie=MIXS.curie('0000025'),
                   model_uri=MIXS.mimag_ref_biomaterial, domain=None, range=Optional[str])

slots.mimag_ref_db = Slot(uri=MIXS['0000062'], name="mimag_ref_db", curie=MIXS.curie('0000062'),
                   model_uri=MIXS.mimag_ref_db, domain=None, range=Optional[str])

slots.mimag_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="mimag_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=MIXS.mimag_rel_to_oxygen, domain=None, range=Optional[str])

slots.mimag_samp_collec_device = Slot(uri=MIXS['0000002'], name="mimag_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.mimag_samp_collec_device, domain=None, range=Optional[str])

slots.mimag_samp_collec_method = Slot(uri=MIXS['0001225'], name="mimag_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.mimag_samp_collec_method, domain=None, range=Optional[str])

slots.mimag_samp_mat_process = Slot(uri=MIXS['0000016'], name="mimag_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.mimag_samp_mat_process, domain=None, range=Optional[str])

slots.mimag_samp_name = Slot(uri=MIXS['0001107'], name="mimag_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.mimag_samp_name, domain=None, range=str)

slots.mimag_samp_size = Slot(uri=MIXS['0000001'], name="mimag_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.mimag_samp_size, domain=None, range=Optional[str])

slots.mimag_samp_taxon_id = Slot(uri=MIXS['0001320'], name="mimag_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.mimag_samp_taxon_id, domain=None, range=str)

slots.mimag_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="mimag_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.mimag_samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.mimag_seq_meth = Slot(uri=MIXS['0000050'], name="mimag_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.mimag_seq_meth, domain=None, range=str)

slots.mimag_sim_search_meth = Slot(uri=MIXS['0000063'], name="mimag_sim_search_meth", curie=MIXS.curie('0000063'),
                   model_uri=MIXS.mimag_sim_search_meth, domain=None, range=Optional[str])

slots.mimag_size_frac = Slot(uri=MIXS['0000017'], name="mimag_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=MIXS.mimag_size_frac, domain=None, range=Optional[str])

slots.mimag_sop = Slot(uri=MIXS['0000090'], name="mimag_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.mimag_sop, domain=None, range=Optional[Union[str, List[str]]])

slots.mimag_source_mat_id = Slot(uri=MIXS['0000026'], name="mimag_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.mimag_source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.mimag_tax_class = Slot(uri=MIXS['0000064'], name="mimag_tax_class", curie=MIXS.curie('0000064'),
                   model_uri=MIXS.mimag_tax_class, domain=None, range=Optional[str])

slots.mimag_tax_ident = Slot(uri=MIXS['0000053'], name="mimag_tax_ident", curie=MIXS.curie('0000053'),
                   model_uri=MIXS.mimag_tax_ident, domain=None, range=str)

slots.mimag_temp = Slot(uri=MIXS['0000113'], name="mimag_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.mimag_temp, domain=None, range=Optional[str])

slots.mimag_trna_ext_software = Slot(uri=MIXS['0000068'], name="mimag_trna_ext_software", curie=MIXS.curie('0000068'),
                   model_uri=MIXS.mimag_trna_ext_software, domain=None, range=Optional[str])

slots.mimag_trnas = Slot(uri=MIXS['0000067'], name="mimag_trnas", curie=MIXS.curie('0000067'),
                   model_uri=MIXS.mimag_trnas, domain=None, range=Optional[str])

slots.mimarks_c_alt = Slot(uri=MIXS['0000094'], name="mimarks_c_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.mimarks_c_alt, domain=None, range=Optional[str])

slots.mimarks_c_associated_resource = Slot(uri=MIXS['0000091'], name="mimarks_c_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.mimarks_c_associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.mimarks_c_biotic_relationship = Slot(uri=MIXS['0000028'], name="mimarks_c_biotic_relationship", curie=MIXS.curie('0000028'),
                   model_uri=MIXS.mimarks_c_biotic_relationship, domain=None, range=Optional[str])

slots.mimarks_c_chimera_check = Slot(uri=MIXS['0000052'], name="mimarks_c_chimera_check", curie=MIXS.curie('0000052'),
                   model_uri=MIXS.mimarks_c_chimera_check, domain=None, range=Optional[str])

slots.mimarks_c_collection_date = Slot(uri=MIXS['0000011'], name="mimarks_c_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.mimarks_c_collection_date, domain=None, range=str)

slots.mimarks_c_depth = Slot(uri=MIXS['0000018'], name="mimarks_c_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.mimarks_c_depth, domain=None, range=Optional[str])

slots.mimarks_c_elev = Slot(uri=MIXS['0000093'], name="mimarks_c_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.mimarks_c_elev, domain=None, range=Optional[str])

slots.mimarks_c_env_broad_scale = Slot(uri=MIXS['0000012'], name="mimarks_c_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.mimarks_c_env_broad_scale, domain=None, range=str)

slots.mimarks_c_env_local_scale = Slot(uri=MIXS['0000013'], name="mimarks_c_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.mimarks_c_env_local_scale, domain=None, range=str)

slots.mimarks_c_env_medium = Slot(uri=MIXS['0000014'], name="mimarks_c_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.mimarks_c_env_medium, domain=None, range=str)

slots.mimarks_c_experimental_factor = Slot(uri=MIXS['0000008'], name="mimarks_c_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.mimarks_c_experimental_factor, domain=None, range=Optional[str])

slots.mimarks_c_extrachrom_elements = Slot(uri=MIXS['0000023'], name="mimarks_c_extrachrom_elements", curie=MIXS.curie('0000023'),
                   model_uri=MIXS.mimarks_c_extrachrom_elements, domain=None, range=Optional[str])

slots.mimarks_c_geo_loc_name = Slot(uri=MIXS['0000010'], name="mimarks_c_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.mimarks_c_geo_loc_name, domain=None, range=str)

slots.mimarks_c_isol_growth_condt = Slot(uri=MIXS['0000003'], name="mimarks_c_isol_growth_condt", curie=MIXS.curie('0000003'),
                   model_uri=MIXS.mimarks_c_isol_growth_condt, domain=None, range=str)

slots.mimarks_c_lat_lon = Slot(uri=MIXS['0000009'], name="mimarks_c_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.mimarks_c_lat_lon, domain=None, range=str)

slots.mimarks_c_neg_cont_type = Slot(uri=MIXS['0001321'], name="mimarks_c_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.mimarks_c_neg_cont_type, domain=None, range=Optional[str])

slots.mimarks_c_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="mimarks_c_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.mimarks_c_nucl_acid_amp, domain=None, range=Optional[str])

slots.mimarks_c_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="mimarks_c_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.mimarks_c_nucl_acid_ext, domain=None, range=Optional[str])

slots.mimarks_c_pcr_cond = Slot(uri=MIXS['0000049'], name="mimarks_c_pcr_cond", curie=MIXS.curie('0000049'),
                   model_uri=MIXS.mimarks_c_pcr_cond, domain=None, range=Optional[str])

slots.mimarks_c_pcr_primers = Slot(uri=MIXS['0000046'], name="mimarks_c_pcr_primers", curie=MIXS.curie('0000046'),
                   model_uri=MIXS.mimarks_c_pcr_primers, domain=None, range=Optional[str])

slots.mimarks_c_pos_cont_type = Slot(uri=MIXS['0001322'], name="mimarks_c_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.mimarks_c_pos_cont_type, domain=None, range=Optional[str])

slots.mimarks_c_project_name = Slot(uri=MIXS['0000092'], name="mimarks_c_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.mimarks_c_project_name, domain=None, range=str)

slots.mimarks_c_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="mimarks_c_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=MIXS.mimarks_c_rel_to_oxygen, domain=None, range=Optional[str])

slots.mimarks_c_samp_collec_device = Slot(uri=MIXS['0000002'], name="mimarks_c_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.mimarks_c_samp_collec_device, domain=None, range=Optional[str])

slots.mimarks_c_samp_collec_method = Slot(uri=MIXS['0001225'], name="mimarks_c_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.mimarks_c_samp_collec_method, domain=None, range=Optional[str])

slots.mimarks_c_samp_mat_process = Slot(uri=MIXS['0000016'], name="mimarks_c_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.mimarks_c_samp_mat_process, domain=None, range=Optional[str])

slots.mimarks_c_samp_name = Slot(uri=MIXS['0001107'], name="mimarks_c_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.mimarks_c_samp_name, domain=None, range=str)

slots.mimarks_c_samp_size = Slot(uri=MIXS['0000001'], name="mimarks_c_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.mimarks_c_samp_size, domain=None, range=Optional[str])

slots.mimarks_c_samp_taxon_id = Slot(uri=MIXS['0001320'], name="mimarks_c_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.mimarks_c_samp_taxon_id, domain=None, range=str)

slots.mimarks_c_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="mimarks_c_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.mimarks_c_samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.mimarks_c_seq_meth = Slot(uri=MIXS['0000050'], name="mimarks_c_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.mimarks_c_seq_meth, domain=None, range=str)

slots.mimarks_c_seq_quality_check = Slot(uri=MIXS['0000051'], name="mimarks_c_seq_quality_check", curie=MIXS.curie('0000051'),
                   model_uri=MIXS.mimarks_c_seq_quality_check, domain=None, range=Optional[str])

slots.mimarks_c_sop = Slot(uri=MIXS['0000090'], name="mimarks_c_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.mimarks_c_sop, domain=None, range=Optional[Union[str, List[str]]])

slots.mimarks_c_source_mat_id = Slot(uri=MIXS['0000026'], name="mimarks_c_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.mimarks_c_source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.mimarks_c_subspecf_gen_lin = Slot(uri=MIXS['0000020'], name="mimarks_c_subspecf_gen_lin", curie=MIXS.curie('0000020'),
                   model_uri=MIXS.mimarks_c_subspecf_gen_lin, domain=None, range=Optional[str])

slots.mimarks_c_target_gene = Slot(uri=MIXS['0000044'], name="mimarks_c_target_gene", curie=MIXS.curie('0000044'),
                   model_uri=MIXS.mimarks_c_target_gene, domain=None, range=str)

slots.mimarks_c_target_subfragment = Slot(uri=MIXS['0000045'], name="mimarks_c_target_subfragment", curie=MIXS.curie('0000045'),
                   model_uri=MIXS.mimarks_c_target_subfragment, domain=None, range=Optional[str])

slots.mimarks_c_temp = Slot(uri=MIXS['0000113'], name="mimarks_c_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.mimarks_c_temp, domain=None, range=Optional[str])

slots.mimarks_c_trophic_level = Slot(uri=MIXS['0000032'], name="mimarks_c_trophic_level", curie=MIXS.curie('0000032'),
                   model_uri=MIXS.mimarks_c_trophic_level, domain=None, range=Optional[str])

slots.mimarks_s_adapters = Slot(uri=MIXS['0000048'], name="mimarks_s_adapters", curie=MIXS.curie('0000048'),
                   model_uri=MIXS.mimarks_s_adapters, domain=None, range=Optional[str])

slots.mimarks_s_alt = Slot(uri=MIXS['0000094'], name="mimarks_s_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.mimarks_s_alt, domain=None, range=Optional[str])

slots.mimarks_s_assembly_software = Slot(uri=MIXS['0000058'], name="mimarks_s_assembly_software", curie=MIXS.curie('0000058'),
                   model_uri=MIXS.mimarks_s_assembly_software, domain=None, range=Optional[str])

slots.mimarks_s_associated_resource = Slot(uri=MIXS['0000091'], name="mimarks_s_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.mimarks_s_associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.mimarks_s_chimera_check = Slot(uri=MIXS['0000052'], name="mimarks_s_chimera_check", curie=MIXS.curie('0000052'),
                   model_uri=MIXS.mimarks_s_chimera_check, domain=None, range=Optional[str])

slots.mimarks_s_collection_date = Slot(uri=MIXS['0000011'], name="mimarks_s_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.mimarks_s_collection_date, domain=None, range=str)

slots.mimarks_s_depth = Slot(uri=MIXS['0000018'], name="mimarks_s_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.mimarks_s_depth, domain=None, range=Optional[str])

slots.mimarks_s_elev = Slot(uri=MIXS['0000093'], name="mimarks_s_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.mimarks_s_elev, domain=None, range=Optional[str])

slots.mimarks_s_env_broad_scale = Slot(uri=MIXS['0000012'], name="mimarks_s_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.mimarks_s_env_broad_scale, domain=None, range=str)

slots.mimarks_s_env_local_scale = Slot(uri=MIXS['0000013'], name="mimarks_s_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.mimarks_s_env_local_scale, domain=None, range=str)

slots.mimarks_s_env_medium = Slot(uri=MIXS['0000014'], name="mimarks_s_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.mimarks_s_env_medium, domain=None, range=str)

slots.mimarks_s_experimental_factor = Slot(uri=MIXS['0000008'], name="mimarks_s_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.mimarks_s_experimental_factor, domain=None, range=Optional[str])

slots.mimarks_s_geo_loc_name = Slot(uri=MIXS['0000010'], name="mimarks_s_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.mimarks_s_geo_loc_name, domain=None, range=str)

slots.mimarks_s_lat_lon = Slot(uri=MIXS['0000009'], name="mimarks_s_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.mimarks_s_lat_lon, domain=None, range=str)

slots.mimarks_s_lib_layout = Slot(uri=MIXS['0000041'], name="mimarks_s_lib_layout", curie=MIXS.curie('0000041'),
                   model_uri=MIXS.mimarks_s_lib_layout, domain=None, range=Optional[str])

slots.mimarks_s_lib_reads_seqd = Slot(uri=MIXS['0000040'], name="mimarks_s_lib_reads_seqd", curie=MIXS.curie('0000040'),
                   model_uri=MIXS.mimarks_s_lib_reads_seqd, domain=None, range=Optional[str])

slots.mimarks_s_lib_screen = Slot(uri=MIXS['0000043'], name="mimarks_s_lib_screen", curie=MIXS.curie('0000043'),
                   model_uri=MIXS.mimarks_s_lib_screen, domain=None, range=Optional[str])

slots.mimarks_s_lib_size = Slot(uri=MIXS['0000039'], name="mimarks_s_lib_size", curie=MIXS.curie('0000039'),
                   model_uri=MIXS.mimarks_s_lib_size, domain=None, range=Optional[str])

slots.mimarks_s_lib_vector = Slot(uri=MIXS['0000042'], name="mimarks_s_lib_vector", curie=MIXS.curie('0000042'),
                   model_uri=MIXS.mimarks_s_lib_vector, domain=None, range=Optional[str])

slots.mimarks_s_mid = Slot(uri=MIXS['0000047'], name="mimarks_s_mid", curie=MIXS.curie('0000047'),
                   model_uri=MIXS.mimarks_s_mid, domain=None, range=Optional[str])

slots.mimarks_s_neg_cont_type = Slot(uri=MIXS['0001321'], name="mimarks_s_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.mimarks_s_neg_cont_type, domain=None, range=Optional[str])

slots.mimarks_s_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="mimarks_s_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.mimarks_s_nucl_acid_amp, domain=None, range=Optional[str])

slots.mimarks_s_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="mimarks_s_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.mimarks_s_nucl_acid_ext, domain=None, range=Optional[str])

slots.mimarks_s_pcr_cond = Slot(uri=MIXS['0000049'], name="mimarks_s_pcr_cond", curie=MIXS.curie('0000049'),
                   model_uri=MIXS.mimarks_s_pcr_cond, domain=None, range=Optional[str])

slots.mimarks_s_pcr_primers = Slot(uri=MIXS['0000046'], name="mimarks_s_pcr_primers", curie=MIXS.curie('0000046'),
                   model_uri=MIXS.mimarks_s_pcr_primers, domain=None, range=Optional[str])

slots.mimarks_s_pos_cont_type = Slot(uri=MIXS['0001322'], name="mimarks_s_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.mimarks_s_pos_cont_type, domain=None, range=Optional[str])

slots.mimarks_s_project_name = Slot(uri=MIXS['0000092'], name="mimarks_s_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.mimarks_s_project_name, domain=None, range=str)

slots.mimarks_s_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="mimarks_s_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=MIXS.mimarks_s_rel_to_oxygen, domain=None, range=Optional[str])

slots.mimarks_s_samp_collec_device = Slot(uri=MIXS['0000002'], name="mimarks_s_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.mimarks_s_samp_collec_device, domain=None, range=Optional[str])

slots.mimarks_s_samp_collec_method = Slot(uri=MIXS['0001225'], name="mimarks_s_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.mimarks_s_samp_collec_method, domain=None, range=Optional[str])

slots.mimarks_s_samp_mat_process = Slot(uri=MIXS['0000016'], name="mimarks_s_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.mimarks_s_samp_mat_process, domain=None, range=Optional[str])

slots.mimarks_s_samp_name = Slot(uri=MIXS['0001107'], name="mimarks_s_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.mimarks_s_samp_name, domain=None, range=str)

slots.mimarks_s_samp_size = Slot(uri=MIXS['0000001'], name="mimarks_s_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.mimarks_s_samp_size, domain=None, range=Optional[str])

slots.mimarks_s_samp_taxon_id = Slot(uri=MIXS['0001320'], name="mimarks_s_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.mimarks_s_samp_taxon_id, domain=None, range=str)

slots.mimarks_s_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="mimarks_s_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.mimarks_s_samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.mimarks_s_seq_meth = Slot(uri=MIXS['0000050'], name="mimarks_s_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.mimarks_s_seq_meth, domain=None, range=str)

slots.mimarks_s_seq_quality_check = Slot(uri=MIXS['0000051'], name="mimarks_s_seq_quality_check", curie=MIXS.curie('0000051'),
                   model_uri=MIXS.mimarks_s_seq_quality_check, domain=None, range=Optional[str])

slots.mimarks_s_size_frac = Slot(uri=MIXS['0000017'], name="mimarks_s_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=MIXS.mimarks_s_size_frac, domain=None, range=Optional[str])

slots.mimarks_s_sop = Slot(uri=MIXS['0000090'], name="mimarks_s_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.mimarks_s_sop, domain=None, range=Optional[Union[str, List[str]]])

slots.mimarks_s_source_mat_id = Slot(uri=MIXS['0000026'], name="mimarks_s_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.mimarks_s_source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.mimarks_s_target_gene = Slot(uri=MIXS['0000044'], name="mimarks_s_target_gene", curie=MIXS.curie('0000044'),
                   model_uri=MIXS.mimarks_s_target_gene, domain=None, range=str)

slots.mimarks_s_target_subfragment = Slot(uri=MIXS['0000045'], name="mimarks_s_target_subfragment", curie=MIXS.curie('0000045'),
                   model_uri=MIXS.mimarks_s_target_subfragment, domain=None, range=Optional[str])

slots.mimarks_s_temp = Slot(uri=MIXS['0000113'], name="mimarks_s_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.mimarks_s_temp, domain=None, range=Optional[str])

slots.mims_adapters = Slot(uri=MIXS['0000048'], name="mims_adapters", curie=MIXS.curie('0000048'),
                   model_uri=MIXS.mims_adapters, domain=None, range=Optional[str])

slots.mims_alt = Slot(uri=MIXS['0000094'], name="mims_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.mims_alt, domain=None, range=Optional[str])

slots.mims_annot = Slot(uri=MIXS['0000059'], name="mims_annot", curie=MIXS.curie('0000059'),
                   model_uri=MIXS.mims_annot, domain=None, range=Optional[str])

slots.mims_assembly_name = Slot(uri=MIXS['0000057'], name="mims_assembly_name", curie=MIXS.curie('0000057'),
                   model_uri=MIXS.mims_assembly_name, domain=None, range=Optional[str])

slots.mims_assembly_qual = Slot(uri=MIXS['0000056'], name="mims_assembly_qual", curie=MIXS.curie('0000056'),
                   model_uri=MIXS.mims_assembly_qual, domain=None, range=Optional[str])

slots.mims_assembly_software = Slot(uri=MIXS['0000058'], name="mims_assembly_software", curie=MIXS.curie('0000058'),
                   model_uri=MIXS.mims_assembly_software, domain=None, range=Optional[str])

slots.mims_associated_resource = Slot(uri=MIXS['0000091'], name="mims_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.mims_associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.mims_collection_date = Slot(uri=MIXS['0000011'], name="mims_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.mims_collection_date, domain=None, range=str)

slots.mims_depth = Slot(uri=MIXS['0000018'], name="mims_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.mims_depth, domain=None, range=Optional[str])

slots.mims_elev = Slot(uri=MIXS['0000093'], name="mims_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.mims_elev, domain=None, range=Optional[str])

slots.mims_env_broad_scale = Slot(uri=MIXS['0000012'], name="mims_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.mims_env_broad_scale, domain=None, range=str)

slots.mims_env_local_scale = Slot(uri=MIXS['0000013'], name="mims_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.mims_env_local_scale, domain=None, range=str)

slots.mims_env_medium = Slot(uri=MIXS['0000014'], name="mims_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.mims_env_medium, domain=None, range=str)

slots.mims_experimental_factor = Slot(uri=MIXS['0000008'], name="mims_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.mims_experimental_factor, domain=None, range=Optional[str])

slots.mims_feat_pred = Slot(uri=MIXS['0000061'], name="mims_feat_pred", curie=MIXS.curie('0000061'),
                   model_uri=MIXS.mims_feat_pred, domain=None, range=Optional[str])

slots.mims_geo_loc_name = Slot(uri=MIXS['0000010'], name="mims_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.mims_geo_loc_name, domain=None, range=str)

slots.mims_lat_lon = Slot(uri=MIXS['0000009'], name="mims_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.mims_lat_lon, domain=None, range=str)

slots.mims_lib_layout = Slot(uri=MIXS['0000041'], name="mims_lib_layout", curie=MIXS.curie('0000041'),
                   model_uri=MIXS.mims_lib_layout, domain=None, range=Optional[str])

slots.mims_lib_reads_seqd = Slot(uri=MIXS['0000040'], name="mims_lib_reads_seqd", curie=MIXS.curie('0000040'),
                   model_uri=MIXS.mims_lib_reads_seqd, domain=None, range=Optional[str])

slots.mims_lib_screen = Slot(uri=MIXS['0000043'], name="mims_lib_screen", curie=MIXS.curie('0000043'),
                   model_uri=MIXS.mims_lib_screen, domain=None, range=Optional[str])

slots.mims_lib_size = Slot(uri=MIXS['0000039'], name="mims_lib_size", curie=MIXS.curie('0000039'),
                   model_uri=MIXS.mims_lib_size, domain=None, range=Optional[str])

slots.mims_lib_vector = Slot(uri=MIXS['0000042'], name="mims_lib_vector", curie=MIXS.curie('0000042'),
                   model_uri=MIXS.mims_lib_vector, domain=None, range=Optional[str])

slots.mims_mid = Slot(uri=MIXS['0000047'], name="mims_mid", curie=MIXS.curie('0000047'),
                   model_uri=MIXS.mims_mid, domain=None, range=Optional[str])

slots.mims_neg_cont_type = Slot(uri=MIXS['0001321'], name="mims_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.mims_neg_cont_type, domain=None, range=Optional[str])

slots.mims_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="mims_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.mims_nucl_acid_amp, domain=None, range=Optional[str])

slots.mims_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="mims_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.mims_nucl_acid_ext, domain=None, range=Optional[str])

slots.mims_number_contig = Slot(uri=MIXS['0000060'], name="mims_number_contig", curie=MIXS.curie('0000060'),
                   model_uri=MIXS.mims_number_contig, domain=None, range=Optional[str])

slots.mims_pos_cont_type = Slot(uri=MIXS['0001322'], name="mims_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.mims_pos_cont_type, domain=None, range=Optional[str])

slots.mims_project_name = Slot(uri=MIXS['0000092'], name="mims_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.mims_project_name, domain=None, range=str)

slots.mims_ref_biomaterial = Slot(uri=MIXS['0000025'], name="mims_ref_biomaterial", curie=MIXS.curie('0000025'),
                   model_uri=MIXS.mims_ref_biomaterial, domain=None, range=Optional[str])

slots.mims_ref_db = Slot(uri=MIXS['0000062'], name="mims_ref_db", curie=MIXS.curie('0000062'),
                   model_uri=MIXS.mims_ref_db, domain=None, range=Optional[str])

slots.mims_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="mims_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=MIXS.mims_rel_to_oxygen, domain=None, range=Optional[str])

slots.mims_samp_collec_device = Slot(uri=MIXS['0000002'], name="mims_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.mims_samp_collec_device, domain=None, range=Optional[str])

slots.mims_samp_collec_method = Slot(uri=MIXS['0001225'], name="mims_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.mims_samp_collec_method, domain=None, range=Optional[str])

slots.mims_samp_mat_process = Slot(uri=MIXS['0000016'], name="mims_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.mims_samp_mat_process, domain=None, range=Optional[str])

slots.mims_samp_name = Slot(uri=MIXS['0001107'], name="mims_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.mims_samp_name, domain=None, range=str)

slots.mims_samp_size = Slot(uri=MIXS['0000001'], name="mims_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.mims_samp_size, domain=None, range=Optional[str])

slots.mims_samp_taxon_id = Slot(uri=MIXS['0001320'], name="mims_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.mims_samp_taxon_id, domain=None, range=str)

slots.mims_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="mims_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.mims_samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.mims_seq_meth = Slot(uri=MIXS['0000050'], name="mims_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.mims_seq_meth, domain=None, range=str)

slots.mims_sim_search_meth = Slot(uri=MIXS['0000063'], name="mims_sim_search_meth", curie=MIXS.curie('0000063'),
                   model_uri=MIXS.mims_sim_search_meth, domain=None, range=Optional[str])

slots.mims_size_frac = Slot(uri=MIXS['0000017'], name="mims_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=MIXS.mims_size_frac, domain=None, range=Optional[str])

slots.mims_sop = Slot(uri=MIXS['0000090'], name="mims_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.mims_sop, domain=None, range=Optional[Union[str, List[str]]])

slots.mims_source_mat_id = Slot(uri=MIXS['0000026'], name="mims_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.mims_source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.mims_tax_class = Slot(uri=MIXS['0000064'], name="mims_tax_class", curie=MIXS.curie('0000064'),
                   model_uri=MIXS.mims_tax_class, domain=None, range=Optional[str])

slots.mims_temp = Slot(uri=MIXS['0000113'], name="mims_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.mims_temp, domain=None, range=Optional[str])

slots.misag_x_16s_recover = Slot(uri=MIXS['0000065'], name="misag_x_16s_recover", curie=MIXS.curie('0000065'),
                   model_uri=MIXS.misag_x_16s_recover, domain=None, range=Optional[str])

slots.misag_x_16s_recover_software = Slot(uri=MIXS['0000066'], name="misag_x_16s_recover_software", curie=MIXS.curie('0000066'),
                   model_uri=MIXS.misag_x_16s_recover_software, domain=None, range=Optional[str])

slots.misag_adapters = Slot(uri=MIXS['0000048'], name="misag_adapters", curie=MIXS.curie('0000048'),
                   model_uri=MIXS.misag_adapters, domain=None, range=Optional[str])

slots.misag_alt = Slot(uri=MIXS['0000094'], name="misag_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.misag_alt, domain=None, range=Optional[str])

slots.misag_annot = Slot(uri=MIXS['0000059'], name="misag_annot", curie=MIXS.curie('0000059'),
                   model_uri=MIXS.misag_annot, domain=None, range=Optional[str])

slots.misag_assembly_name = Slot(uri=MIXS['0000057'], name="misag_assembly_name", curie=MIXS.curie('0000057'),
                   model_uri=MIXS.misag_assembly_name, domain=None, range=Optional[str])

slots.misag_assembly_qual = Slot(uri=MIXS['0000056'], name="misag_assembly_qual", curie=MIXS.curie('0000056'),
                   model_uri=MIXS.misag_assembly_qual, domain=None, range=str)

slots.misag_assembly_software = Slot(uri=MIXS['0000058'], name="misag_assembly_software", curie=MIXS.curie('0000058'),
                   model_uri=MIXS.misag_assembly_software, domain=None, range=str)

slots.misag_associated_resource = Slot(uri=MIXS['0000091'], name="misag_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.misag_associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.misag_collection_date = Slot(uri=MIXS['0000011'], name="misag_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.misag_collection_date, domain=None, range=str)

slots.misag_compl_appr = Slot(uri=MIXS['0000071'], name="misag_compl_appr", curie=MIXS.curie('0000071'),
                   model_uri=MIXS.misag_compl_appr, domain=None, range=Optional[str])

slots.misag_compl_score = Slot(uri=MIXS['0000069'], name="misag_compl_score", curie=MIXS.curie('0000069'),
                   model_uri=MIXS.misag_compl_score, domain=None, range=str)

slots.misag_compl_software = Slot(uri=MIXS['0000070'], name="misag_compl_software", curie=MIXS.curie('0000070'),
                   model_uri=MIXS.misag_compl_software, domain=None, range=str)

slots.misag_contam_score = Slot(uri=MIXS['0000072'], name="misag_contam_score", curie=MIXS.curie('0000072'),
                   model_uri=MIXS.misag_contam_score, domain=None, range=str)

slots.misag_contam_screen_input = Slot(uri=MIXS['0000005'], name="misag_contam_screen_input", curie=MIXS.curie('0000005'),
                   model_uri=MIXS.misag_contam_screen_input, domain=None, range=Optional[str])

slots.misag_contam_screen_param = Slot(uri=MIXS['0000073'], name="misag_contam_screen_param", curie=MIXS.curie('0000073'),
                   model_uri=MIXS.misag_contam_screen_param, domain=None, range=Optional[str])

slots.misag_decontam_software = Slot(uri=MIXS['0000074'], name="misag_decontam_software", curie=MIXS.curie('0000074'),
                   model_uri=MIXS.misag_decontam_software, domain=None, range=Optional[str])

slots.misag_depth = Slot(uri=MIXS['0000018'], name="misag_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.misag_depth, domain=None, range=Optional[str])

slots.misag_elev = Slot(uri=MIXS['0000093'], name="misag_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.misag_elev, domain=None, range=Optional[str])

slots.misag_env_broad_scale = Slot(uri=MIXS['0000012'], name="misag_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.misag_env_broad_scale, domain=None, range=str)

slots.misag_env_local_scale = Slot(uri=MIXS['0000013'], name="misag_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.misag_env_local_scale, domain=None, range=str)

slots.misag_env_medium = Slot(uri=MIXS['0000014'], name="misag_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.misag_env_medium, domain=None, range=str)

slots.misag_experimental_factor = Slot(uri=MIXS['0000008'], name="misag_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.misag_experimental_factor, domain=None, range=Optional[str])

slots.misag_feat_pred = Slot(uri=MIXS['0000061'], name="misag_feat_pred", curie=MIXS.curie('0000061'),
                   model_uri=MIXS.misag_feat_pred, domain=None, range=Optional[str])

slots.misag_geo_loc_name = Slot(uri=MIXS['0000010'], name="misag_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.misag_geo_loc_name, domain=None, range=str)

slots.misag_lat_lon = Slot(uri=MIXS['0000009'], name="misag_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.misag_lat_lon, domain=None, range=str)

slots.misag_lib_layout = Slot(uri=MIXS['0000041'], name="misag_lib_layout", curie=MIXS.curie('0000041'),
                   model_uri=MIXS.misag_lib_layout, domain=None, range=Optional[str])

slots.misag_lib_reads_seqd = Slot(uri=MIXS['0000040'], name="misag_lib_reads_seqd", curie=MIXS.curie('0000040'),
                   model_uri=MIXS.misag_lib_reads_seqd, domain=None, range=Optional[str])

slots.misag_lib_screen = Slot(uri=MIXS['0000043'], name="misag_lib_screen", curie=MIXS.curie('0000043'),
                   model_uri=MIXS.misag_lib_screen, domain=None, range=Optional[str])

slots.misag_lib_size = Slot(uri=MIXS['0000039'], name="misag_lib_size", curie=MIXS.curie('0000039'),
                   model_uri=MIXS.misag_lib_size, domain=None, range=Optional[str])

slots.misag_lib_vector = Slot(uri=MIXS['0000042'], name="misag_lib_vector", curie=MIXS.curie('0000042'),
                   model_uri=MIXS.misag_lib_vector, domain=None, range=Optional[str])

slots.misag_mid = Slot(uri=MIXS['0000047'], name="misag_mid", curie=MIXS.curie('0000047'),
                   model_uri=MIXS.misag_mid, domain=None, range=Optional[str])

slots.misag_neg_cont_type = Slot(uri=MIXS['0001321'], name="misag_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.misag_neg_cont_type, domain=None, range=Optional[str])

slots.misag_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="misag_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.misag_nucl_acid_amp, domain=None, range=Optional[str])

slots.misag_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="misag_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.misag_nucl_acid_ext, domain=None, range=Optional[str])

slots.misag_number_contig = Slot(uri=MIXS['0000060'], name="misag_number_contig", curie=MIXS.curie('0000060'),
                   model_uri=MIXS.misag_number_contig, domain=None, range=Optional[str])

slots.misag_pos_cont_type = Slot(uri=MIXS['0001322'], name="misag_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.misag_pos_cont_type, domain=None, range=Optional[str])

slots.misag_project_name = Slot(uri=MIXS['0000092'], name="misag_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.misag_project_name, domain=None, range=str)

slots.misag_ref_biomaterial = Slot(uri=MIXS['0000025'], name="misag_ref_biomaterial", curie=MIXS.curie('0000025'),
                   model_uri=MIXS.misag_ref_biomaterial, domain=None, range=Optional[str])

slots.misag_ref_db = Slot(uri=MIXS['0000062'], name="misag_ref_db", curie=MIXS.curie('0000062'),
                   model_uri=MIXS.misag_ref_db, domain=None, range=Optional[str])

slots.misag_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="misag_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=MIXS.misag_rel_to_oxygen, domain=None, range=Optional[str])

slots.misag_samp_collec_device = Slot(uri=MIXS['0000002'], name="misag_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.misag_samp_collec_device, domain=None, range=Optional[str])

slots.misag_samp_collec_method = Slot(uri=MIXS['0001225'], name="misag_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.misag_samp_collec_method, domain=None, range=Optional[str])

slots.misag_samp_mat_process = Slot(uri=MIXS['0000016'], name="misag_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.misag_samp_mat_process, domain=None, range=Optional[str])

slots.misag_samp_name = Slot(uri=MIXS['0001107'], name="misag_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.misag_samp_name, domain=None, range=str)

slots.misag_samp_size = Slot(uri=MIXS['0000001'], name="misag_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.misag_samp_size, domain=None, range=Optional[str])

slots.misag_samp_taxon_id = Slot(uri=MIXS['0001320'], name="misag_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.misag_samp_taxon_id, domain=None, range=str)

slots.misag_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="misag_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.misag_samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.misag_seq_meth = Slot(uri=MIXS['0000050'], name="misag_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.misag_seq_meth, domain=None, range=str)

slots.misag_sim_search_meth = Slot(uri=MIXS['0000063'], name="misag_sim_search_meth", curie=MIXS.curie('0000063'),
                   model_uri=MIXS.misag_sim_search_meth, domain=None, range=Optional[str])

slots.misag_single_cell_lysis_appr = Slot(uri=MIXS['0000076'], name="misag_single_cell_lysis_appr", curie=MIXS.curie('0000076'),
                   model_uri=MIXS.misag_single_cell_lysis_appr, domain=None, range=str)

slots.misag_single_cell_lysis_prot = Slot(uri=MIXS['0000054'], name="misag_single_cell_lysis_prot", curie=MIXS.curie('0000054'),
                   model_uri=MIXS.misag_single_cell_lysis_prot, domain=None, range=Optional[str])

slots.misag_size_frac = Slot(uri=MIXS['0000017'], name="misag_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=MIXS.misag_size_frac, domain=None, range=Optional[str])

slots.misag_sop = Slot(uri=MIXS['0000090'], name="misag_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.misag_sop, domain=None, range=Optional[Union[str, List[str]]])

slots.misag_sort_tech = Slot(uri=MIXS['0000075'], name="misag_sort_tech", curie=MIXS.curie('0000075'),
                   model_uri=MIXS.misag_sort_tech, domain=None, range=str)

slots.misag_source_mat_id = Slot(uri=MIXS['0000026'], name="misag_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.misag_source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.misag_tax_class = Slot(uri=MIXS['0000064'], name="misag_tax_class", curie=MIXS.curie('0000064'),
                   model_uri=MIXS.misag_tax_class, domain=None, range=Optional[str])

slots.misag_tax_ident = Slot(uri=MIXS['0000053'], name="misag_tax_ident", curie=MIXS.curie('0000053'),
                   model_uri=MIXS.misag_tax_ident, domain=None, range=str)

slots.misag_temp = Slot(uri=MIXS['0000113'], name="misag_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.misag_temp, domain=None, range=Optional[str])

slots.misag_trna_ext_software = Slot(uri=MIXS['0000068'], name="misag_trna_ext_software", curie=MIXS.curie('0000068'),
                   model_uri=MIXS.misag_trna_ext_software, domain=None, range=Optional[str])

slots.misag_trnas = Slot(uri=MIXS['0000067'], name="misag_trnas", curie=MIXS.curie('0000067'),
                   model_uri=MIXS.misag_trnas, domain=None, range=Optional[str])

slots.misag_wga_amp_appr = Slot(uri=MIXS['0000055'], name="misag_wga_amp_appr", curie=MIXS.curie('0000055'),
                   model_uri=MIXS.misag_wga_amp_appr, domain=None, range=str)

slots.misag_wga_amp_kit = Slot(uri=MIXS['0000006'], name="misag_wga_amp_kit", curie=MIXS.curie('0000006'),
                   model_uri=MIXS.misag_wga_amp_kit, domain=None, range=Optional[str])

slots.miuvig_adapters = Slot(uri=MIXS['0000048'], name="miuvig_adapters", curie=MIXS.curie('0000048'),
                   model_uri=MIXS.miuvig_adapters, domain=None, range=Optional[str])

slots.miuvig_alt = Slot(uri=MIXS['0000094'], name="miuvig_alt", curie=MIXS.curie('0000094'),
                   model_uri=MIXS.miuvig_alt, domain=None, range=Optional[str])

slots.miuvig_annot = Slot(uri=MIXS['0000059'], name="miuvig_annot", curie=MIXS.curie('0000059'),
                   model_uri=MIXS.miuvig_annot, domain=None, range=Optional[str])

slots.miuvig_assembly_name = Slot(uri=MIXS['0000057'], name="miuvig_assembly_name", curie=MIXS.curie('0000057'),
                   model_uri=MIXS.miuvig_assembly_name, domain=None, range=Optional[str])

slots.miuvig_assembly_qual = Slot(uri=MIXS['0000056'], name="miuvig_assembly_qual", curie=MIXS.curie('0000056'),
                   model_uri=MIXS.miuvig_assembly_qual, domain=None, range=str)

slots.miuvig_assembly_software = Slot(uri=MIXS['0000058'], name="miuvig_assembly_software", curie=MIXS.curie('0000058'),
                   model_uri=MIXS.miuvig_assembly_software, domain=None, range=str)

slots.miuvig_associated_resource = Slot(uri=MIXS['0000091'], name="miuvig_associated resource", curie=MIXS.curie('0000091'),
                   model_uri=MIXS.miuvig_associated_resource, domain=None, range=Optional[Union[str, List[str]]])

slots.miuvig_bin_param = Slot(uri=MIXS['0000077'], name="miuvig_bin_param", curie=MIXS.curie('0000077'),
                   model_uri=MIXS.miuvig_bin_param, domain=None, range=Optional[str])

slots.miuvig_bin_software = Slot(uri=MIXS['0000078'], name="miuvig_bin_software", curie=MIXS.curie('0000078'),
                   model_uri=MIXS.miuvig_bin_software, domain=None, range=Optional[str])

slots.miuvig_biotic_relationship = Slot(uri=MIXS['0000028'], name="miuvig_biotic_relationship", curie=MIXS.curie('0000028'),
                   model_uri=MIXS.miuvig_biotic_relationship, domain=None, range=Optional[str])

slots.miuvig_collection_date = Slot(uri=MIXS['0000011'], name="miuvig_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=MIXS.miuvig_collection_date, domain=None, range=str)

slots.miuvig_compl_appr = Slot(uri=MIXS['0000071'], name="miuvig_compl_appr", curie=MIXS.curie('0000071'),
                   model_uri=MIXS.miuvig_compl_appr, domain=None, range=Optional[str])

slots.miuvig_compl_score = Slot(uri=MIXS['0000069'], name="miuvig_compl_score", curie=MIXS.curie('0000069'),
                   model_uri=MIXS.miuvig_compl_score, domain=None, range=Optional[str])

slots.miuvig_compl_software = Slot(uri=MIXS['0000070'], name="miuvig_compl_software", curie=MIXS.curie('0000070'),
                   model_uri=MIXS.miuvig_compl_software, domain=None, range=Optional[str])

slots.miuvig_depth = Slot(uri=MIXS['0000018'], name="miuvig_depth", curie=MIXS.curie('0000018'),
                   model_uri=MIXS.miuvig_depth, domain=None, range=Optional[str])

slots.miuvig_detec_type = Slot(uri=MIXS['0000084'], name="miuvig_detec_type", curie=MIXS.curie('0000084'),
                   model_uri=MIXS.miuvig_detec_type, domain=None, range=str)

slots.miuvig_elev = Slot(uri=MIXS['0000093'], name="miuvig_elev", curie=MIXS.curie('0000093'),
                   model_uri=MIXS.miuvig_elev, domain=None, range=Optional[str])

slots.miuvig_env_broad_scale = Slot(uri=MIXS['0000012'], name="miuvig_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=MIXS.miuvig_env_broad_scale, domain=None, range=str)

slots.miuvig_env_local_scale = Slot(uri=MIXS['0000013'], name="miuvig_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=MIXS.miuvig_env_local_scale, domain=None, range=str)

slots.miuvig_env_medium = Slot(uri=MIXS['0000014'], name="miuvig_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=MIXS.miuvig_env_medium, domain=None, range=str)

slots.miuvig_estimated_size = Slot(uri=MIXS['0000024'], name="miuvig_estimated_size", curie=MIXS.curie('0000024'),
                   model_uri=MIXS.miuvig_estimated_size, domain=None, range=Optional[str])

slots.miuvig_experimental_factor = Slot(uri=MIXS['0000008'], name="miuvig_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=MIXS.miuvig_experimental_factor, domain=None, range=Optional[str])

slots.miuvig_feat_pred = Slot(uri=MIXS['0000061'], name="miuvig_feat_pred", curie=MIXS.curie('0000061'),
                   model_uri=MIXS.miuvig_feat_pred, domain=None, range=Optional[str])

slots.miuvig_geo_loc_name = Slot(uri=MIXS['0000010'], name="miuvig_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=MIXS.miuvig_geo_loc_name, domain=None, range=str)

slots.miuvig_host_disease_stat = Slot(uri=MIXS['0000031'], name="miuvig_host_disease_stat", curie=MIXS.curie('0000031'),
                   model_uri=MIXS.miuvig_host_disease_stat, domain=None, range=Optional[Union[str, List[str]]])

slots.miuvig_host_pred_appr = Slot(uri=MIXS['0000088'], name="miuvig_host_pred_appr", curie=MIXS.curie('0000088'),
                   model_uri=MIXS.miuvig_host_pred_appr, domain=None, range=Optional[str])

slots.miuvig_host_pred_est_acc = Slot(uri=MIXS['0000089'], name="miuvig_host_pred_est_acc", curie=MIXS.curie('0000089'),
                   model_uri=MIXS.miuvig_host_pred_est_acc, domain=None, range=Optional[str])

slots.miuvig_host_spec_range = Slot(uri=MIXS['0000030'], name="miuvig_host_spec_range", curie=MIXS.curie('0000030'),
                   model_uri=MIXS.miuvig_host_spec_range, domain=None, range=Optional[Union[str, List[str]]])

slots.miuvig_lat_lon = Slot(uri=MIXS['0000009'], name="miuvig_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=MIXS.miuvig_lat_lon, domain=None, range=str)

slots.miuvig_lib_layout = Slot(uri=MIXS['0000041'], name="miuvig_lib_layout", curie=MIXS.curie('0000041'),
                   model_uri=MIXS.miuvig_lib_layout, domain=None, range=Optional[str])

slots.miuvig_lib_reads_seqd = Slot(uri=MIXS['0000040'], name="miuvig_lib_reads_seqd", curie=MIXS.curie('0000040'),
                   model_uri=MIXS.miuvig_lib_reads_seqd, domain=None, range=Optional[str])

slots.miuvig_lib_screen = Slot(uri=MIXS['0000043'], name="miuvig_lib_screen", curie=MIXS.curie('0000043'),
                   model_uri=MIXS.miuvig_lib_screen, domain=None, range=Optional[str])

slots.miuvig_lib_size = Slot(uri=MIXS['0000039'], name="miuvig_lib_size", curie=MIXS.curie('0000039'),
                   model_uri=MIXS.miuvig_lib_size, domain=None, range=Optional[str])

slots.miuvig_lib_vector = Slot(uri=MIXS['0000042'], name="miuvig_lib_vector", curie=MIXS.curie('0000042'),
                   model_uri=MIXS.miuvig_lib_vector, domain=None, range=Optional[str])

slots.miuvig_mag_cov_software = Slot(uri=MIXS['0000080'], name="miuvig_mag_cov_software", curie=MIXS.curie('0000080'),
                   model_uri=MIXS.miuvig_mag_cov_software, domain=None, range=Optional[str])

slots.miuvig_mid = Slot(uri=MIXS['0000047'], name="miuvig_mid", curie=MIXS.curie('0000047'),
                   model_uri=MIXS.miuvig_mid, domain=None, range=Optional[str])

slots.miuvig_neg_cont_type = Slot(uri=MIXS['0001321'], name="miuvig_neg_cont_type", curie=MIXS.curie('0001321'),
                   model_uri=MIXS.miuvig_neg_cont_type, domain=None, range=Optional[str])

slots.miuvig_nucl_acid_amp = Slot(uri=MIXS['0000038'], name="miuvig_nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=MIXS.miuvig_nucl_acid_amp, domain=None, range=Optional[str])

slots.miuvig_nucl_acid_ext = Slot(uri=MIXS['0000037'], name="miuvig_nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=MIXS.miuvig_nucl_acid_ext, domain=None, range=Optional[str])

slots.miuvig_number_contig = Slot(uri=MIXS['0000060'], name="miuvig_number_contig", curie=MIXS.curie('0000060'),
                   model_uri=MIXS.miuvig_number_contig, domain=None, range=str)

slots.miuvig_otu_class_appr = Slot(uri=MIXS['0000085'], name="miuvig_otu_class_appr", curie=MIXS.curie('0000085'),
                   model_uri=MIXS.miuvig_otu_class_appr, domain=None, range=Optional[str])

slots.miuvig_otu_db = Slot(uri=MIXS['0000087'], name="miuvig_otu_db", curie=MIXS.curie('0000087'),
                   model_uri=MIXS.miuvig_otu_db, domain=None, range=Optional[str])

slots.miuvig_otu_seq_comp_appr = Slot(uri=MIXS['0000086'], name="miuvig_otu_seq_comp_appr", curie=MIXS.curie('0000086'),
                   model_uri=MIXS.miuvig_otu_seq_comp_appr, domain=None, range=Optional[str])

slots.miuvig_pathogenicity = Slot(uri=MIXS['0000027'], name="miuvig_pathogenicity", curie=MIXS.curie('0000027'),
                   model_uri=MIXS.miuvig_pathogenicity, domain=None, range=Optional[str])

slots.miuvig_pos_cont_type = Slot(uri=MIXS['0001322'], name="miuvig_pos_cont_type", curie=MIXS.curie('0001322'),
                   model_uri=MIXS.miuvig_pos_cont_type, domain=None, range=Optional[str])

slots.miuvig_pred_genome_struc = Slot(uri=MIXS['0000083'], name="miuvig_pred_genome_struc", curie=MIXS.curie('0000083'),
                   model_uri=MIXS.miuvig_pred_genome_struc, domain=None, range=str)

slots.miuvig_pred_genome_type = Slot(uri=MIXS['0000082'], name="miuvig_pred_genome_type", curie=MIXS.curie('0000082'),
                   model_uri=MIXS.miuvig_pred_genome_type, domain=None, range=str)

slots.miuvig_project_name = Slot(uri=MIXS['0000092'], name="miuvig_project_name", curie=MIXS.curie('0000092'),
                   model_uri=MIXS.miuvig_project_name, domain=None, range=str)

slots.miuvig_reassembly_bin = Slot(uri=MIXS['0000079'], name="miuvig_reassembly_bin", curie=MIXS.curie('0000079'),
                   model_uri=MIXS.miuvig_reassembly_bin, domain=None, range=Optional[str])

slots.miuvig_ref_biomaterial = Slot(uri=MIXS['0000025'], name="miuvig_ref_biomaterial", curie=MIXS.curie('0000025'),
                   model_uri=MIXS.miuvig_ref_biomaterial, domain=None, range=Optional[str])

slots.miuvig_ref_db = Slot(uri=MIXS['0000062'], name="miuvig_ref_db", curie=MIXS.curie('0000062'),
                   model_uri=MIXS.miuvig_ref_db, domain=None, range=Optional[str])

slots.miuvig_samp_collec_device = Slot(uri=MIXS['0000002'], name="miuvig_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=MIXS.miuvig_samp_collec_device, domain=None, range=Optional[str])

slots.miuvig_samp_collec_method = Slot(uri=MIXS['0001225'], name="miuvig_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=MIXS.miuvig_samp_collec_method, domain=None, range=Optional[str])

slots.miuvig_samp_mat_process = Slot(uri=MIXS['0000016'], name="miuvig_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=MIXS.miuvig_samp_mat_process, domain=None, range=Optional[str])

slots.miuvig_samp_name = Slot(uri=MIXS['0001107'], name="miuvig_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=MIXS.miuvig_samp_name, domain=None, range=str)

slots.miuvig_samp_size = Slot(uri=MIXS['0000001'], name="miuvig_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=MIXS.miuvig_samp_size, domain=None, range=Optional[str])

slots.miuvig_samp_taxon_id = Slot(uri=MIXS['0001320'], name="miuvig_samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=MIXS.miuvig_samp_taxon_id, domain=None, range=str)

slots.miuvig_samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="miuvig_samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.miuvig_samp_vol_we_dna_ext, domain=None, range=Optional[str])

slots.miuvig_seq_meth = Slot(uri=MIXS['0000050'], name="miuvig_seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=MIXS.miuvig_seq_meth, domain=None, range=str)

slots.miuvig_sim_search_meth = Slot(uri=MIXS['0000063'], name="miuvig_sim_search_meth", curie=MIXS.curie('0000063'),
                   model_uri=MIXS.miuvig_sim_search_meth, domain=None, range=Optional[str])

slots.miuvig_single_cell_lysis_appr = Slot(uri=MIXS['0000076'], name="miuvig_single_cell_lysis_appr", curie=MIXS.curie('0000076'),
                   model_uri=MIXS.miuvig_single_cell_lysis_appr, domain=None, range=Optional[str])

slots.miuvig_single_cell_lysis_prot = Slot(uri=MIXS['0000054'], name="miuvig_single_cell_lysis_prot", curie=MIXS.curie('0000054'),
                   model_uri=MIXS.miuvig_single_cell_lysis_prot, domain=None, range=Optional[str])

slots.miuvig_size_frac = Slot(uri=MIXS['0000017'], name="miuvig_size_frac", curie=MIXS.curie('0000017'),
                   model_uri=MIXS.miuvig_size_frac, domain=None, range=Optional[str])

slots.miuvig_sop = Slot(uri=MIXS['0000090'], name="miuvig_sop", curie=MIXS.curie('0000090'),
                   model_uri=MIXS.miuvig_sop, domain=None, range=Optional[Union[str, List[str]]])

slots.miuvig_sort_tech = Slot(uri=MIXS['0000075'], name="miuvig_sort_tech", curie=MIXS.curie('0000075'),
                   model_uri=MIXS.miuvig_sort_tech, domain=None, range=Optional[str])

slots.miuvig_source_mat_id = Slot(uri=MIXS['0000026'], name="miuvig_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=MIXS.miuvig_source_mat_id, domain=None, range=Optional[Union[str, List[str]]])

slots.miuvig_source_uvig = Slot(uri=MIXS['0000035'], name="miuvig_source_uvig", curie=MIXS.curie('0000035'),
                   model_uri=MIXS.miuvig_source_uvig, domain=None, range=str)

slots.miuvig_specific_host = Slot(uri=MIXS['0000029'], name="miuvig_specific_host", curie=MIXS.curie('0000029'),
                   model_uri=MIXS.miuvig_specific_host, domain=None, range=Optional[str])

slots.miuvig_tax_class = Slot(uri=MIXS['0000064'], name="miuvig_tax_class", curie=MIXS.curie('0000064'),
                   model_uri=MIXS.miuvig_tax_class, domain=None, range=Optional[str])

slots.miuvig_tax_ident = Slot(uri=MIXS['0000053'], name="miuvig_tax_ident", curie=MIXS.curie('0000053'),
                   model_uri=MIXS.miuvig_tax_ident, domain=None, range=Optional[str])

slots.miuvig_temp = Slot(uri=MIXS['0000113'], name="miuvig_temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.miuvig_temp, domain=None, range=Optional[str])

slots.miuvig_trna_ext_software = Slot(uri=MIXS['0000068'], name="miuvig_trna_ext_software", curie=MIXS.curie('0000068'),
                   model_uri=MIXS.miuvig_trna_ext_software, domain=None, range=Optional[str])

slots.miuvig_trnas = Slot(uri=MIXS['0000067'], name="miuvig_trnas", curie=MIXS.curie('0000067'),
                   model_uri=MIXS.miuvig_trnas, domain=None, range=Optional[str])

slots.miuvig_vir_ident_software = Slot(uri=MIXS['0000081'], name="miuvig_vir_ident_software", curie=MIXS.curie('0000081'),
                   model_uri=MIXS.miuvig_vir_ident_software, domain=None, range=str)

slots.miuvig_virus_enrich_appr = Slot(uri=MIXS['0000036'], name="miuvig_virus_enrich_appr", curie=MIXS.curie('0000036'),
                   model_uri=MIXS.miuvig_virus_enrich_appr, domain=None, range=str)

slots.miuvig_wga_amp_appr = Slot(uri=MIXS['0000055'], name="miuvig_wga_amp_appr", curie=MIXS.curie('0000055'),
                   model_uri=MIXS.miuvig_wga_amp_appr, domain=None, range=Optional[str])

slots.miuvig_wga_amp_kit = Slot(uri=MIXS['0000006'], name="miuvig_wga_amp_kit", curie=MIXS.curie('0000006'),
                   model_uri=MIXS.miuvig_wga_amp_kit, domain=None, range=Optional[str])