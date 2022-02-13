
"""
utils
"""
import click
import yaml
from dataclasses import dataclass, field
from typing import Optional, Set, List, Union, Dict, Any, Tuple
import logging
import re

def new_schema(name: str) -> Dict:
    s = {
        'id': f'http://w3id.org/mixs/{name}',
        'name': f'{name}',
        'imports': [
            'linkml:types'
        ],
        'prefixes': {
            'linkml': 'https://w3id.org/linkml/',
            'mixs.vocab': 'https://w3id.org/mixs/vocab/',
            'MIXS': 'https://w3id.org/mixs/terms/',
        },
        'default_prefix': 'mixs.vocab',
        'slots': {},
        'classes': {},
        'subsets': {},
        'enums': {}
    }
    return s

def write_schema(schema, output) -> None:
    with open(output, 'w') as ostream:
        yaml.safe_dump(schema, ostream, sort_keys=False)

def add_import(schema: dict, mod: str):
    schema['imports'].append(mod)

@click.group()
@click.option('-v', '--verbose', count=True)
def main(verbose):
    if verbose >= 2:
        logging.basicConfig(level=logging.DEBUG)
    elif verbose == 1:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)

@main.command()
@click.option('-i', '--input', help="main schema yaml file")
@click.option('-d', '--directory', default='./src/schema', help="directory to place extracted packages")
@click.option('-o', '--output', help="new schema yaml file")
@click.argument('packages', nargs=-1)
def extract(input: str, output: str, directory: str, packages: List[str]):
    """
    extract a package from the main yaml file
    """
    with open(input, 'r') as stream:
        schema = yaml.safe_load(stream)
        for p in packages:
            pschema = extract_package(schema, p)
            with open(f'{directory}/{p}.yaml', 'w') as ostream:
                yaml.safe_dump(pschema, ostream, sort_keys=False)
        with open(output, 'w') as ostream:
            yaml.safe_dump(schema, ostream, sort_keys=False)

def extract_package(schema: dict, p: str) -> None:
    pschema = new_schema(p)
    add_import(schema, p)
    c = schema['classes'][p]
    del schema['classes'][p]
    pschema['classes'][p] = c
    return pschema

if __name__ == '__main__':
    main()
