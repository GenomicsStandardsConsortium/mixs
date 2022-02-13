
"""
converts mixs6 spreadsheet

spreadsheet:
https://docs.google.com/spreadsheets/d/165AHU4Px4S1fFFIqsvffWFlD1RUFmH609QbuDl4pASk/edit

Note: This file first has to be saved locally as a TSV. This code should also work for mixs5 xlsx files too, once exported to tsv
"""
import click
import yaml
from dataclasses import dataclass, field
from typing import Optional, Set, List, Union, Dict, Any, Tuple
from linkml_runtime.utils.formatutils import underscore
import pandas as pd
import logging
from gsctools.packageutils import new_schema
import os
import re

CORE_PACKAGE_NAME = 'core'

# technology-specific checklists from the MIGS and MIMS standards
CHECKLISTS = {'migs_eu':
                  {'name': 'MIGS eukaryote',
                   'fullname': 'Minimal Information about a Genome Sequence: eukaryote',
                    'abbrev': 'MIGS.eu'},
              'migs_ba':
                  {'name': 'MIGS bacteria',
                   'fullname': 'Minimal Information about a Genome Sequence: cultured bacteria/archaea',
                    'abbrev': 'MIGS.ba'
                   },
              'migs_pl':
                  {'name': 'MIGS plant',
                   'fullname': 'Minimal Information about a Genome Sequence: plant',
                   'abbrev': 'MIGS.pl'},
              'migs_vi':
                  {'name': 'MIGS virus',
                   'fullname': 'Minimal Information about a Genome Sequence: cultured bacteria/archaea',
                   'abbrev': 'MIGS.ba'
                   },
              'migs_org':
                  {'name': 'MIGS org',
                   'fullname': 'Minimal Information about a Genome Sequence: org',
                   'abbrev': 'MIGS.org'},
              'mims':
                  {'name': 'MIMS',
                   'fullname': 'Metagenome or Environmental',
                   'abbrev': 'MIMS'},
              'mimarks_s':
                  {'name': 'MIMARKS specimen',
                   'fullname': 'Minimal Information about a Marker Specimen: specimen',
                   'abbrev': 'MIMARKS.specimen',
                   'see_also': [
                       'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3367316'
                   ]},
              'mimarks_c':  ## TODO check this
                  {'name': 'MIMARKS survey',
                   'fullname': 'Minimal Information about a Marker Specimen: survey',
                   'abbrev': 'MIMARKS.survey',
                   'see_also': [
                        'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3367316'
                   ]},
              'misag': {
                  'name': 'MISAG',
                  'fullname': 'Minimum Information About a Single Amplified Genome',
                  'abbrev': 'MISAG'
              },
              'mimag': {
                  'name': 'MIMAG',
                  'fullname': 'Minimum Information About a Metagenome-Assembled Genome',
                  'abbrev': 'MIMAG'
              },
              'miuvig': {
                  'name': 'MIUVIG',
                  'fullname': 'Minimum Information About an Uncultivated Virus Genome',
                  'abbrev': 'MIUVIG'}
              }


datatype_schema = {
    'classes':
        {'quantity value':
             {'description': 'used to record a measurement',
              'attributes': {
                  'has unit': {
                      'description': 'Example "m"'
                  },
                  'has numeric value': {
                      'range': 'double'
                  },
                  'has raw value': {
                      'string_serialization': '{has numeric value} {has unit}'
                  }
              }
            }
        }
}

def safe(s: str) -> str:
    """
    render a string safe for use as a python variable

    :param s:
    :return:
    """
    if s[0].isdigit():
        s = f"x_{s}"
    if '/' in s:
        s = s.replace("/", "_")
    return s

def parse_value_syntax(s: str, slot_name: str = "") -> Tuple[str,str]:
    """
    Parses the 'value syntax' field from MIxS spreadsheets

    Returns: tuple of (pattern, range)
    """
    pattern = s
    range = 'string'
    if s == '{float} {unit}':
        return None, 'quantity value'
    elif s == '{float}':
        return None, 'double'
    elif s == '{integer}':
        return None, 'integer'
    elif s == '{timestamp}':
        return None, 'date'
    elif slot_name == 'depth':
        return None, 'quantity value'
    return pattern, range

@dataclass
class MIxS6Converter:
    """
    converts TSV from MIxS spreadsheet into LinkML yaml
    """

    core_filename: Optional[str] = None
    packages_filename: Optional[str] = None
    output_directory: str = './model/schema'

    def convert_and_save(self, fn: str = None) -> str:
        obj = self.convert()
        if fn is None:
            fn = os.path.join(self.output_directory, "mixs.yaml")
        with open(fn, 'w') as stream:
            yaml.safe_dump(obj, stream, sort_keys=False)
        return fn

    def save_schema(self, schema, output) -> None:
        f = f'{self.output_directory}/{output}'
        with open(f, 'w') as ostream:
            yaml.safe_dump(schema, ostream, sort_keys=False)

    def create_slot(self, row, enums: dict = {}) -> (str, Dict):
        """
        turn a row from EITHER core tab OR packages tab into a slot definition

        :param row:
        :return: tuple of id and definition dictionary
        """
        action_column = next(k for k in row.keys() if k.startswith('Action'))
        s_id = row['Structured comment name']
        if s_id is None or s_id == '-':
            logging.error(f"Bad row: {row}")
            return None, None
        if ';' in s_id:
            logging.error(f'Bad ID / SCN: {s_id} in {row}')
            return None, None
        if 'Item' in row:
            s_name = row['Item']
        elif 'Package item' in row:
            s_name = row['Package item']
        else:
            s_name = row['Item (rdfs:label)']
        if s_name == '':
            logging.error(f'No name: {s_id}')
            return None, None
        if ';' in s_name:
            logging.error(f'Bad name: {s_name} in {row}')
            return None, None
        comments = []
        annotations = {}
       # for k in ('Expected value', 'Preferred unit', 'Occurrence', 'Position'): position was in editors's sheet but is not being used in MIxS 6. We may want to add it back at some point.
       #  for k in ('Expected value', 'Preferred unit', 'Occurrence'):
        for k in ('Expected value', 'Preferred unit'):
            if k in row and row[k] != '':
                comments.append(f'{k}: {row[k]}')
        multivalued = row.get('Occurrence', '') == 'm'
        annotations['Occurrence'] = row.get('Occurrence', '')

        # the column header is not consistent between sheets here
        # column headers are now unique as MIXS ID, but this still works
        slot_uri = None
        if 'Unique MIXS ID' in row and row['Unique MIXS ID'] is not None:
            slot_uri = row['Unique MIXS ID']
        elif 'unique MIXS ID' in row and row['unique MIXS ID'] is not None:
            slot_uri = row['unique MIXS ID']
        elif 'MIXS ID' in row and row['MIXS ID'] is not None:
            slot_uri = row['MIXS ID']
        else:
            None
            #logging.error(f'No ID: {slot_uri}')
        # workaround for https://github.com/GenomicsStandardsConsortium/mixs/issues/216
        # this issue has been fixed
        #if slot_uri.startswith('Measure'):
        #    logging.error(f'Bad format for MIXS ID in {row} -- value given is {slot_uri}')
        #    slot_uri = 'MIXS:TODO1234'
        
        # The GOLD mappings have been removed. If we want to add them back in, uncomment this section and readd the column.
        # exact_mappings = []
        # if 'MIGS ID (mapping to GOLD)' in row:
        #    exact_mappings.append(f'MIGS:{row["MIGS ID (mapping to GOLD)"]}')

        section = row['Section'] if 'Section' in row else 'environment'
        if section == '':
            logging.warning(f'No section: {s_id}')
            section = 'core'
        is_a = f'{section} field'
        pattern, range = parse_value_syntax(row['Value syntax'], s_name)
        slot = {
            'is_a': is_a,
            'title': s_name,
            'description': row['Definition'],
            'range': range,
            'multivalued': multivalued,
            'examples': [
                {'value': row['Example']}
            ],
            'comments': comments,
            "aliases": []
        }
        slot["aliases"].append(s_name)
        # 'aliases': [s_name]
        # 'annotations': annotations

        if (action_column and row[action_column] == 'deprecated term') or\
                ('Discussion' in row and row['Discussion'] == 'remove'):
            slot['deprecated'] = 'Deprecated in mixs6'

        #if len(exact_mappings) > 0:
        #    slot['exact_mappings'] = exact_mappings
        if pattern is not None:
            # slot['pattern'] = pattern
            slot['string_serialization'] = pattern
       # the link to GH issues were removed. We may want to add them back in.
       # LINK = 'Link to GH issue'
       # if LINK in row:
       #     url = row[LINK]
       #     if url is not None and url.startswith("http"):
       #         slot['see_also'] = url

        s_id = safe(s_id)
        if pattern is not None and '|' in pattern:
            vals = pattern.replace('[', '').replace(']','').split('|')
            vals = [v.strip() for v in vals]
            # remove entries like '[{PMID}|{DOI}|...]'
            vals = [v for v in vals if not v.startswith('{')]
            if len(vals) > 2:
                enum_name = f'{s_id}_enum'
                slot['range'] = enum_name
                # slot['string_serialization'] = ''
                del slot['string_serialization']
                enums[enum_name] = {
                    'permissible_values': {v: {} for v in vals}
                }
        if slot_uri is not None and slot_uri != '':
            slot['slot_uri'] = slot_uri
        else:
            logging.error(f'No slot_uri for {row}')
        if 'Expected value' in row:
            range = row['Expected value']

        if 'Section' in row:
            row['in_subset'] = [row['Section']]

        return (s_id, slot)

    def convert(self) -> Dict[str, Any]:
        """
        Converts set of inputs to a schema

        :return: link schema as a python Dictionary
        """
        trim_strings = lambda x: x.strip() if isinstance(x, str) else x
        core_df = pd.read_csv(self.core_filename, sep="\t").fillna("").applymap(trim_strings)
        pkg_df  = pd.read_csv(self.packages_filename, sep="\t").fillna("").applymap(trim_strings)
        slots = {
            'core field': {
                'abstract': True,
                'description': "basic fields"
            },
            'investigation field': {
                'abstract': True,
                'description': "field describing aspect of the investigation/study to which the sample belongs"
            },
            'nucleic acid sequence source field': {
                'abstract': True
            },
            'sequencing field': {
                'abstract': True
            },
            'mixs extension field': {
                'abstract': True
            },
            'environment field': {
                'abstract': True,
                'description': "field describing environmental aspect of a sample"
            }
        }
        classes = {}
        subsets = {}
        enums = {}
        obj = {
            'id': f'http://w3id.org/mixs',
            'name': 'MIxS',
            'description': 'Minimal Information about any Sequence Standard',
            'imports': [
                'linkml:types',
                'checklists',
                'core'
            ],
            'prefixes': {
                'linkml': 'https://w3id.org/linkml/',
                'mixs.vocab': 'https://w3id.org/mixs/vocab/',
                'MIXS': 'https://w3id.org/mixs/terms/',
                'MIGS': 'https://w3id.org/mixs/migs/',
            },
            'default_prefix': 'mixs.vocab',
            'slots': {},
            'classes': classes,
            'subsets': subsets
        }


        # TODO: make configurable whether this is in main schema or import
        rschema = new_schema('ranges')
        for k,v in datatype_schema.items():
            rschema[k] = v
        self.save_schema(rschema, 'ranges.yaml')
        
        cls_slot_req = {}
        slot_cls_req = {}

        core_slots = []
        core_env_slots = []

        core_slot_dict = {}
        # PARSE CORE
        for _, row in core_df.iterrows():
            s_id, slot = self.create_slot(row, enums=enums)
            if s_id is None:
                continue
            slots[s_id] = slot
            core_slot_dict[s_id] = row
            core_slots.append(s_id)
            if row['Section'] == 'environment':
                core_env_slots.append(s_id)

        for checklist, info in CHECKLISTS.items():
            checklist_slot_usage = {}
            checklist_name = info['name']
            for s_id, s_row in core_slot_dict.items():
                cardinality = s_row[checklist]
                # information about whether an item is:
                # - mandatory (M)
                # - conditional mandatory (C)
                # - optional (X)
                # - environment-dependent (E)
                # - or not applicable (-)
                if cardinality != 'E':
                    usage = {}
                    if cardinality == 'M':
                        usage['required'] = True
                    elif cardinality == 'X':
                        usage['required'] = False
                    elif cardinality == 'C':
                        usage['recommended'] = True
                    #elif cardinality == '-':
                    #    usage['comments'] = ['not applicable']
                    if usage != {}:
                        checklist_slot_usage[s_id] = usage
            classes[checklist_name] = {
                'mixin': True,
                'description': info['fullname'],
                'aliases': [
                    info['abbrev']
                ],
                'see_also': info.get('see_also', []),
                #'todos': ['add details here'],
                'slots': list(checklist_slot_usage.keys()),
                'slot_usage': checklist_slot_usage
            }
        classes[CORE_PACKAGE_NAME] = {
            'description': 'Core package. Do not use this directly, this is used to build other packages',
            'slots': core_slots
        }
        env_packages = []
        # PARSE PACKAGES
        for _, row in pkg_df.iterrows():
            in_core_and_package = False
            p = row['Environmental package']
            req = row['Requirement']
            is_required = req == 'M'
            cn = safe(p.lower())
            if cn not in classes:
                env_packages.append(cn)
                cls_slot_req[cn] = {}
                classes[cn] = {
                    #'is_a': CORE_PACKAGE_NAME,
                    'description': p,
                    'mappings': [],
                    'slots': list(core_env_slots),
                    'slot_usage': {}
                }
            c = classes[cn]

            s_id, slot = self.create_slot(row, enums=enums)

            if s_id is not None:
                c['slot_usage'][s_id] = {'required': is_required}
                cls_slot_req[cn][s_id] = req

                if s_id not in slots:
                    slots[s_id] = slot
                else:
                    in_core_and_package = True
                    slot['todos'] = ['this is in both core and packages']

                if s_id not in slot_cls_req:
                    slot_cls_req[s_id] = {}
                slot_cls_req[s_id][cn] = req
                if s_id not in core_slots:
                    c['slots'].append(s_id)


        # n_cls = len(cls_slot_req.keys())
        # inf_core_slots = []
        # for s_id, s in slot_cls_req.items():
        #     packages_str = ', '.join(list(s.keys()))
        #     if len(s.keys()) == n_cls:
        #         inf_core_slots.append(s_id)
        #         cmt = "This field is used in all packages"
        #     elif len(s.keys()) == 1:
        #         cmt = f"This field is used uniquely in: {packages_str}"
        #     else:
        #         cmt = f"This field is used in: {len(s.keys())} packages: {packages_str}"
        #     slots[s_id]['comments'].append(cmt)



        for p in env_packages:
            for checklist, info in CHECKLISTS.items():
                name = info['name']
                fullname = info['fullname']
                combo = f'{p} {name}'
                classes[combo] = {
                    'is_a': p,
                    'mixins': [name],
                    'description': f'Combinatorial checklist {fullname} with environmental package {p}'
                }
            pname = underscore(p).replace("-", "_")
            obj['imports'].append(pname)
            pschema = new_schema(pname)
            pschema['imports'].append('terms')
            pschema['classes'] = {p: classes[p]}
            del classes[p]
            self.save_schema(pschema, f'{pname}.yaml')


        slot_schema = new_schema('terms')
        slot_schema['imports'].append('ranges')
        slot_schema['slots'] = slots
        slot_schema['enums'] = enums
        slot_schema['subsets'] = {
            'checklist': {
                'description': 'A MIxS checklist. These can be combined with packages'
            },
            'package': {
                'description': 'A MIxS package. These can be combined with checklists'
            },
            'checklist_package_combination': {
                'description': 'A combination of a checklist and a package'
            }
        }
        self.save_schema(slot_schema, 'terms.yaml')

        core_schema = new_schema('core')
        core_schema['imports'].append('terms')
        core_schema['classes'] = {'core': obj['classes']['core'] }
        del obj['classes']['core']
        self.save_schema(core_schema, 'core.yaml')

        checklist_schema = new_schema('checklists')
        checklist_schema['imports'].append('terms')
        checklist_schema['classes'] = obj['classes']
        obj['classes'] = {}
        self.save_schema(checklist_schema, 'checklists.yaml')

        return obj

@click.command()
def cli(**kwargs):
    """ Generate JSON Schema representation of a biolink model """
    cv = MIxS6Converter()
    cv.core_filename = f'downloads/mixs6_core.tsv'
    cv.packages_filename = f'downloads/mixs6.tsv'
    cv.convert_and_save('model/schema/mixs.yaml')


if __name__ == '__main__':
    cli()
