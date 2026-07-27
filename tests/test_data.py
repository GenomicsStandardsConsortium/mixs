"""Data test."""
import os
import glob
import unittest

from linkml_runtime.loaders import yaml_loader
from mixs.datamodel.mixs import MixsCompliantData

# this is somewhat redundant with the examples/output Makefile target,
# but it illustrates the use of the MixS python datamodel

ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "examples", "valid")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, 'MixsCompliantData*.yaml'))

class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_data(self):
        """Date test."""
        for path in EXAMPLE_FILES:
            print(path)
            obj = yaml_loader.load(path, target_class=MixsCompliantData)
            assert obj
