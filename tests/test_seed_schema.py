import unittest
from gsctools.mixs_converter import MIxS6Converter
from linkml.generators.pythongen import PythonGenerator
from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml.generators.owlgen import OwlSchemaGenerator
import os
import sys

INPUTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'inputs')
OUTPUTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'outputs')

class MIxS6TestCase(unittest.TestCase):
    def test_convert(self):
        cv = MIxS6Converter()
        cv.core_filename = f'{INPUTS_DIR}/mixs6_core.tsv'
        cv.packages_filename = f'{INPUTS_DIR}/mixs6.tsv'
        cv.output_directory = OUTPUTS_DIR
        self.assertTrue(True)
        fn = cv.convert_and_save()
        g = PythonGenerator(fn)
        print(g.serialize()[0:1000])
        g = JsonSchemaGenerator(fn)
        print(g.serialize()[0:1000])
        g = OwlSchemaGenerator(fn)
        print(g.serialize()[0:1000])





if __name__ == '__main__':
    unittest.main()
