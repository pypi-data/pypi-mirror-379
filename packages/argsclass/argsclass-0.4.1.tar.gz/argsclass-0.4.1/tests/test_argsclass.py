"""Dummy tests for argsclass package."""

import unittest
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import argsclass


class TestArgsclassPackage(unittest.TestCase):
    """Test argsclass package functionality."""
    
    def test_package_import(self):
        """Test that the package can be imported."""
        assert argsclass is not None

    def test_version(self):
        """Test that the version is defined."""
        assert hasattr(argsclass, '__version__')
        assert argsclass.__version__ == "0.4.1"

    def test_dummy(self):
        """Dummy test to ensure tests run successfully."""
        assert True


if __name__ == "__main__":
    unittest.main()
