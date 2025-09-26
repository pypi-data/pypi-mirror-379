"""Tests for validation error handling and help flag detection."""

import unittest
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from argsclass.help import ValidationErrorCollector, ValidationError, detect_help_flag, remove_help_flags
from argsclass.parser import HelpRequested, ArgumentParsingError, parse
from argsclass.models import PositionalArgSpec, OptionArgSpec, FlagArgSpec, Cardinality, PrimitiveType


class TestValidationErrorCollector(unittest.TestCase):
    """Test the ValidationErrorCollector class."""
    
    def test_collector_initialization(self):
        """Test collector initialization."""
        collector = ValidationErrorCollector()
        self.assertFalse(collector.has_errors())
        self.assertEqual(len(collector.get_errors()), 0)
    
    def test_add_error(self):
        """Test adding errors to collector."""
        collector = ValidationErrorCollector()
        
        collector.add_error("Test error")
        self.assertTrue(collector.has_errors())
        self.assertEqual(len(collector.get_errors()), 1)
        
        error = collector.get_errors()[0]
        self.assertEqual(error.message, "Test error")
        self.assertIsNone(error.argument)
        self.assertIsNone(error.value)
        self.assertEqual(error.error_type, "error")
    
    def test_add_error_with_context(self):
        """Test adding errors with context."""
        collector = ValidationErrorCollector()
        
        collector.add_error("Invalid value", argument="port", value="abc")
        self.assertTrue(collector.has_errors())
        
        error = collector.get_errors()[0]
        self.assertEqual(error.message, "Invalid value")
        self.assertEqual(error.argument, "port")
        self.assertEqual(error.value, "abc")
    
    def test_add_multiple_errors(self):
        """Test adding multiple errors."""
        collector = ValidationErrorCollector()
        
        collector.add_error("Error 1")
        collector.add_error("Error 2", argument="arg1")
        collector.add_error("Error 3", value="value1")
        
        self.assertTrue(collector.has_errors())
        self.assertEqual(len(collector.get_errors()), 3)
    
    def test_clear_errors(self):
        """Test clearing all errors."""
        collector = ValidationErrorCollector()
        
        collector.add_error("Error 1")
        collector.add_error("Error 2")
        self.assertTrue(collector.has_errors())
        
        collector.clear()
        self.assertFalse(collector.has_errors())
        self.assertEqual(len(collector.get_errors()), 0)
    
    def test_format_errors(self):
        """Test formatting errors into a message."""
        collector = ValidationErrorCollector()
        
        # Test empty collector
        self.assertEqual(collector.format_errors(), "")
        
        # Test with errors
        collector.add_error("Invalid choice", argument="format", value="csv")
        collector.add_error("Missing required argument", argument="input")
        
        error_message = collector.format_errors()
        self.assertIn("error: the following arguments had problems:", error_message)
        self.assertIn("Invalid choice (argument format, value 'csv')", error_message)
        self.assertIn("Missing required argument (argument input)", error_message)
        self.assertIn("use --help for more information", error_message)


class TestValidationError(unittest.TestCase):
    """Test the ValidationError class."""
    
    def test_error_initialization(self):
        """Test error initialization."""
        error = ValidationError("Test error")
        self.assertEqual(error.message, "Test error")
        self.assertIsNone(error.argument)
        self.assertIsNone(error.value)
        self.assertEqual(error.error_type, "error")
    
    def test_error_with_context(self):
        """Test error with context information."""
        error = ValidationError("Invalid value", argument="port", value="abc")
        self.assertEqual(error.message, "Invalid value")
        self.assertEqual(error.argument, "port")
        self.assertEqual(error.value, "abc")
        self.assertEqual(error.error_type, "error")
    
    def test_error_with_custom_type(self):
        """Test error with custom error type."""
        error = ValidationError("Warning message", error_type="warning")
        self.assertEqual(error.message, "Warning message")
        self.assertEqual(error.error_type, "warning")
    
    def test_error_string_representation(self):
        """Test error string representation."""
        # Error with no context
        error = ValidationError("Simple error")
        self.assertEqual(str(error), "Simple error")
        
        # Error with argument only
        error = ValidationError("Argument error", argument="input")
        self.assertEqual(str(error), "Argument error (argument input)")
        
        # Error with value only
        error = ValidationError("Value error", value="invalid")
        self.assertEqual(str(error), "Value error (value 'invalid')")
        
        # Error with both argument and value
        error = ValidationError("Full error", argument="port", value="abc")
        self.assertEqual(str(error), "Full error (argument port, value 'abc')")


class TestHelpUtilityFunctions(unittest.TestCase):
    """Test help utility functions."""
    
    def test_detect_help_flag(self):
        """Test help flag detection."""
        # Test with --help
        self.assertTrue(detect_help_flag(["--help"]))
        self.assertTrue(detect_help_flag(["script.py", "--help"]))
        self.assertTrue(detect_help_flag(["--help", "other", "args"]))
        
        # Test with -h
        self.assertTrue(detect_help_flag(["-h"]))
        self.assertTrue(detect_help_flag(["script.py", "-h"]))
        self.assertTrue(detect_help_flag(["-h", "other", "args"]))
        
        # Test without help flags
        self.assertFalse(detect_help_flag([]))
        self.assertFalse(detect_help_flag(["script.py"]))
        self.assertFalse(detect_help_flag(["--verbose"]))
        self.assertFalse(detect_help_flag(["-v"]))
        self.assertFalse(detect_help_flag(["script.py", "--verbose", "-v"]))
    
    def test_remove_help_flags(self):
        """Test help flag removal."""
        # Test removing --help
        self.assertEqual(remove_help_flags(["--help"]), [])
        self.assertEqual(remove_help_flags(["script.py", "--help"]), ["script.py"])
        self.assertEqual(remove_help_flags(["--help", "other", "args"]), ["other", "args"])
        
        # Test removing -h
        self.assertEqual(remove_help_flags(["-h"]), [])
        self.assertEqual(remove_help_flags(["script.py", "-h"]), ["script.py"])
        self.assertEqual(remove_help_flags(["-h", "other", "args"]), ["other", "args"])
        
        # Test removing both
        self.assertEqual(remove_help_flags(["--help", "-h"]), [])
        self.assertEqual(remove_help_flags(["script.py", "--help", "-h"]), ["script.py"])
        
        # Test with no help flags
        self.assertEqual(remove_help_flags([]), [])
        self.assertEqual(remove_help_flags(["script.py"]), ["script.py"])
        self.assertEqual(remove_help_flags(["--verbose"]), ["--verbose"])
        self.assertEqual(remove_help_flags(["script.py", "--verbose", "-v"]), ["script.py", "--verbose", "-v"])
        
        # Test with mixed flags
        self.assertEqual(remove_help_flags(["script.py", "--help", "--verbose", "-h"]), ["script.py", "--verbose"])


class TestHelpIntegration(unittest.TestCase):
    """Test help integration with parsing."""
    
    def test_help_requested_exception(self):
        """Test that help flag raises HelpRequested exception."""
        specs = [PositionalArgSpec(name="input")]
        argv = ["script.py", "--help"]
        
        with self.assertRaises(HelpRequested) as cm:
            parse(specs, argv)
        
        # Check that help message is provided
        self.assertIn("usage:", cm.exception.help_message)
        self.assertIn("input", cm.exception.help_message)
    
    def test_help_with_custom_program_info(self):
        """Test help with custom program information."""
        specs = [PositionalArgSpec(name="input")]
        argv = ["script.py", "--help"]
        
        with self.assertRaises(HelpRequested) as cm:
            parse(specs, argv, prog="myapp", description="My application")
        
        # Check that custom program name and description appear in help
        self.assertIn("myapp", cm.exception.help_message)
        self.assertIn("My application", cm.exception.help_message)
    
    def test_help_with_epilog(self):
        """Test help with epilog."""
        specs = [PositionalArgSpec(name="input")]
        argv = ["script.py", "--help"]
        
        with self.assertRaises(HelpRequested) as cm:
            parse(specs, argv, epilog="Additional information")
        
        # Check that epilog appears in help
        self.assertIn("Additional information", cm.exception.help_message)


class TestArgumentParsingError(unittest.TestCase):
    """Test ArgumentParsingError exception."""
    
    def test_error_initialization(self):
        """Test error initialization."""
        error = ArgumentParsingError("Test error")
        self.assertEqual(error.error_message, "Test error")
        self.assertIsNone(error.help_message)
    
    def test_error_with_help(self):
        """Test error with help message."""
        error = ArgumentParsingError("Test error", "Help message")
        self.assertEqual(error.error_message, "Test error")
        self.assertEqual(error.help_message, "Help message")
    
    def test_error_inheritance(self):
        """Test that error inherits from Exception."""
        error = ArgumentParsingError("Test error")
        self.assertIsInstance(error, Exception)
        self.assertEqual(str(error), "Test error")


if __name__ == "__main__":
    unittest.main()