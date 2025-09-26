"""Tests for the argument parser functionality."""

import unittest
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from argsclass.parser import parse, ArgumentParsingError
from argsclass.models import BaseArgSpec, PositionalArgSpec, OptionArgSpec, FlagArgSpec, Cardinality, PrimitiveType


class TestParseFunction(unittest.TestCase):
    """Test the root parse function."""
    
    def test_parse_single_positional(self):
        """Test parsing a single positional argument."""
        specs = [PositionalArgSpec(name="filename")]
        argv = ["script.py", "test.txt"]
        
        result = parse(specs, argv)
        
        assert result == {"filename": "test.txt"}
    
    def test_parse_multiple_positionals(self):
        """Test parsing multiple positional arguments."""
        specs = [
            PositionalArgSpec(name="input"),
            PositionalArgSpec(name="output")
        ]
        argv = ["script.py", "input.txt", "output.txt"]
        
        result = parse(specs, argv)
        
        assert result == {"input": "input.txt", "output": "output.txt"}
    
    def test_parse_mixed_cardinality(self):
        """Test parsing arguments with mixed cardinality."""
        specs = [
            PositionalArgSpec(name="required_file"),
            PositionalArgSpec(
                name="optional_files",
                cardinality=Cardinality.zero_or_more()
            )
        ]
        argv = ["script.py", "required.txt", "opt1.txt", "opt2.txt"]
        
        result = parse(specs, argv)
        
        assert result == {
            "required_file": "required.txt",
            "optional_files": ["opt1.txt", "opt2.txt"]
        }
    
    def test_parse_with_types_and_choices(self):
        """Test parsing with type conversion and choices."""
        specs = [
            PositionalArgSpec(
                name="count",
                arg_type=PrimitiveType(int)
            ),
            PositionalArgSpec(
                name="format",
                choices=["json", "xml", "csv"]
            )
        ]
        argv = ["script.py", "42", "json"]
        
        result = parse(specs, argv)
        
        assert result == {"count": 42, "format": "json"}
    
    def test_parse_with_defaults(self):
        """Test parsing with default values."""
        specs = [
            PositionalArgSpec(name="required"),
            PositionalArgSpec(
                name="optional",
                cardinality=Cardinality.zero_or_one(),
                default="default_value"
            )
        ]
        argv = ["script.py", "required_value"]
        
        result = parse(specs, argv)
        
        assert result == {
            "required": "required_value",
            "optional": "default_value"
        }
    
    def test_parse_options(self):
        """Test parsing option arguments."""
        specs = [
            OptionArgSpec(
                name="output",
                aliases={"o"},
                help_text="Output file"
            ),
            OptionArgSpec(
                name="port",
                arg_type=PrimitiveType(int),
                default=8080
            )
        ]
        argv = ["script.py", "--output", "file.txt", "--port", "9000"]
        
        result = parse(specs, argv)
        
        assert result == {"output": "file.txt", "port": 9000}
    
    def test_parse_flags(self):
        """Test parsing flag arguments."""
        specs = [
            FlagArgSpec(
                name="verbose",
                aliases={"v"},
                help_text="Verbose output"
            ),
            FlagArgSpec(
                name="debug",
                help_text="Debug mode"
            )
        ]
        argv = ["script.py", "--verbose", "--debug"]
        
        result = parse(specs, argv)
        
        assert result == {"verbose": True, "debug": True}
    
    def test_parse_mixed_arguments(self):
        """Test parsing mixed argument types."""
        specs = [
            PositionalArgSpec(name="input"),
            OptionArgSpec(name="output", aliases={"o"}),
            FlagArgSpec(name="verbose", aliases={"v"})
        ]
        argv = ["script.py", "input.txt", "-o", "output.txt", "-v"]
        
        result = parse(specs, argv)
        
        assert result == {
            "input": "input.txt",
            "output": "output.txt",
            "verbose": True
        }
    
    def test_parse_help_flag(self):
        """Test that help flag raises HelpRequested."""
        specs = [PositionalArgSpec(name="input")]
        argv = ["script.py", "--help"]
        
        from argsclass.parser import HelpRequested
        
        with self.assertRaises(HelpRequested) as cm:
            parse(specs, argv)
        
        # Check that help message is provided
        assert "usage:" in cm.exception.help_message
        assert "input" in cm.exception.help_message
    
    def test_parse_unknown_argument(self):
        """Test that unknown arguments raise ArgumentParsingError."""
        specs = [PositionalArgSpec(name="input")]
        argv = ["script.py", "--unknown", "value"]
        
        with self.assertRaises(ArgumentParsingError) as cm:
            parse(specs, argv)
        
        # Check that error message mentions unknown argument
        assert "unrecognized" in cm.exception.error_message.lower()
    
    def test_parse_invalid_choice(self):
        """Test that invalid choices raise ArgumentParsingError."""
        specs = [
            PositionalArgSpec(
                name="format",
                choices=["json", "xml"]
            )
        ]
        argv = ["script.py", "csv"]  # csv is not in choices
        
        with self.assertRaises(ArgumentParsingError) as cm:
            parse(specs, argv)
        
        # Check that error message mentions invalid choice
        assert "invalid choice" in cm.exception.error_message.lower()
    
    def test_parse_type_conversion_error(self):
        """Test that type conversion errors raise ArgumentParsingError."""
        specs = [
            PositionalArgSpec(
                name="count",
                arg_type=PrimitiveType(int)
            )
        ]
        argv = ["script.py", "not_a_number"]
        
        with self.assertRaises(ArgumentParsingError) as cm:
            parse(specs, argv)
        
        # Check that error message mentions type conversion
        assert "invalid" in cm.exception.error_message.lower()
    
    def test_parse_missing_required(self):
        """Test that missing required arguments raise ArgumentParsingError."""
        specs = [PositionalArgSpec(name="input")]  # Required by default
        argv = ["script.py"]  # No arguments provided
        
        with self.assertRaises(ArgumentParsingError) as cm:
            parse(specs, argv)
        
        # Check that error message mentions missing argument
        assert "required" in cm.exception.error_message.lower() or "expected" in cm.exception.error_message.lower()
    
    def test_parse_with_class(self):
        """Test parsing with a class instead of specs."""
        class Args:
            input_file: str
            verbose: bool = False
        
        argv = ["script.py", "--input_file", "test.txt", "--verbose"]
        
        result = parse(Args, argv)
        
        assert result.input_file == "test.txt"
        assert result.verbose is True
        assert isinstance(result, Args)
    
    def test_parse_with_dataclass(self):
        """Test parsing with a dataclass."""
        from dataclasses import dataclass
        
        @dataclass
        class Args:
            input_file: str
            verbose: bool = False
        
        argv = ["script.py", "--input_file", "test.txt", "--verbose"]
        
        result = parse(Args, argv)
        
        assert result.input_file == "test.txt"
        assert result.verbose is True
        assert isinstance(result, Args)
    
    def test_parse_ignore_unknown(self):
        """Test parsing with ignore_unknown=True."""
        specs = [PositionalArgSpec(name="input")]
        argv = ["script.py", "input.txt", "--unknown", "value"]
        
        result = parse(specs, argv, ignore_unknown=True)
        
        assert result == {"input": "input.txt"}
    
    def test_parse_with_program_info(self):
        """Test parsing with custom program info."""
        specs = [PositionalArgSpec(name="input")]
        argv = ["script.py", "--help"]
        
        from argsclass.parser import HelpRequested
        
        with self.assertRaises(HelpRequested) as cm:
            parse(specs, argv, prog="myapp", description="My application")
        
        # Check that custom program name and description appear in help
        assert "myapp" in cm.exception.help_message
        assert "My application" in cm.exception.help_message


if __name__ == "__main__":
    unittest.main()