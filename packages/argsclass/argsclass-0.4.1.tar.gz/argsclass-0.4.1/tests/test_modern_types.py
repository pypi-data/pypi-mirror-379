"""Tests for modern Python type hints support."""

import pytest
from typing import List, Optional, Union
from argsclass import inspect_class, parse


class TestModernTypeHints:
    """Test support for modern Python type hints."""
    
    def test_list_type_inference(self):
        """Test inference of List types."""
        class Args:
            files: List[str]
            numbers: List[int]
            mixed: List[str] = ["default"]
        
        specs = inspect_class(Args)
        
        # Should create option specs with zero_or_more cardinality for lists
        files_spec = next(spec for spec in specs if spec.name == "files")
        assert files_spec.cardinality.min == 0
        assert files_spec.cardinality.max is None
        assert files_spec.arg_type.primitive_type == str
        
        numbers_spec = next(spec for spec in specs if spec.name == "numbers")
        assert numbers_spec.cardinality.min == 0
        assert numbers_spec.cardinality.max is None
        assert numbers_spec.arg_type.primitive_type == int
        
        mixed_spec = next(spec for spec in specs if spec.name == "mixed")
        assert mixed_spec.cardinality.min == 0
        assert mixed_spec.cardinality.max is None
        assert mixed_spec.arg_type.primitive_type == str
        assert mixed_spec.default == ["default"]
    
    def test_optional_type_inference(self):
        """Test inference of Optional types."""
        class Args:
            name: Optional[str]
            count: Optional[int] = 42
            flag: Optional[bool]
        
        specs = inspect_class(Args)
        
        name_spec = next(spec for spec in specs if spec.name == "name")
        assert name_spec.arg_type.primitive_type == str
        assert name_spec.default is None
        
        count_spec = next(spec for spec in specs if spec.name == "count")
        assert count_spec.arg_type.primitive_type == int
        assert count_spec.default == 42
        
        # Optional[bool] should still be treated as a flag
        flag_spec = next(spec for spec in specs if spec.name == "flag")
        assert flag_spec.__class__.__name__ == "FlagArgSpec"
    
    def test_union_type_inference(self):
        """Test inference of Union types."""
        class Args:
            value: Union[str, int]
            nullable: Union[str, None]
            mixed: Union[str, int] = "default"
        
        specs = inspect_class(Args)
        
        value_spec = next(spec for spec in specs if spec.name == "value")
        # Should take the first non-None type
        assert value_spec.arg_type.primitive_type == str
        
        nullable_spec = next(spec for spec in specs if spec.name == "nullable")
        assert nullable_spec.arg_type.primitive_type == str
        
        mixed_spec = next(spec for spec in specs if spec.name == "mixed")
        assert mixed_spec.arg_type.primitive_type == str
        assert mixed_spec.default == "default"


class TestPython310UnionSyntax:
    """Test support for Python 3.10+ union syntax (str | int)."""
    
    def test_python310_union_syntax(self):
        """Test the new | union syntax from Python 3.10+."""
        # This test will only work on Python 3.10+
        import sys
        if sys.version_info < (3, 10):
            pytest.skip("Python 3.10+ required for | union syntax")
        
        # Use eval to avoid syntax errors on older Python versions
        class_def = """
class Args:
    value: str | int
    nullable: str | None
    mixed: str | int = "default"
"""
        
        # Create the class dynamically
        namespace = {}
        exec(class_def, namespace)
        Args = namespace['Args']
        
        specs = inspect_class(Args)
        
        value_spec = next(spec for spec in specs if spec.name == "value")
        # Should take the first non-None type
        assert value_spec.arg_type.primitive_type == str
        
        nullable_spec = next(spec for spec in specs if spec.name == "nullable")
        assert nullable_spec.arg_type.primitive_type == str
        
        mixed_spec = next(spec for spec in specs if spec.name == "mixed")
        assert mixed_spec.arg_type.primitive_type == str
        assert mixed_spec.default == "default"


class TestTypeInferenceIntegration:
    """Test type inference integration with parsing."""
    
    def test_parse_with_list_types(self):
        """Test parsing with List type hints."""
        class Args:
            files: List[str]
            numbers: List[int]
            single_file: str = "default.txt"
        
        # Parse with multiple values for list types (disable ambiguity validation for multiple lists)
        result = parse(Args, [
            "--files", "file1.txt", "file2.txt", "file3.txt",
            "--numbers", "1", "2", "3",
            "--single_file", "override.txt"
        ], validate_ambiguities=False)
        
        assert result.files == ["file1.txt", "file2.txt", "file3.txt"]
        assert result.numbers == [1, 2, 3]
        assert result.single_file == "override.txt"
    
    def test_parse_with_optional_types(self):
        """Test parsing with Optional type hints."""
        class Args:
            name: Optional[str]
            count: Optional[int] = 42
            debug: Optional[bool]
        
        # Parse with some values provided
        result = parse(Args, [
            "--name", "test",
            "--debug"  # boolean flag
        ])
        
        assert result.name == "test"
        assert result.count == 42  # default value
        assert result.debug is True
    
    def test_parse_with_union_types(self):
        """Test parsing with Union type hints."""
        class Args:
            value: Union[str, int]
            nullable: Union[str, None]
        
        # Parse with string values
        result = parse(Args, [
            "--value", "hello",
            "--nullable", "world"
        ])
        
        assert result.value == "hello"
        assert result.nullable == "world"
    
    def test_parse_with_complex_type_combinations(self):
        """Test parsing with complex combinations of type hints."""
        class Args:
            # List of optional strings
            tags: List[str]
            # Optional list of integers
            ports: Optional[List[int]] = None
            # Union of string and integer
            id_value: Union[str, int]
            # Boolean flag
            verbose: bool
        
        result = parse(Args, [
            "--tags", "tag1", "tag2", "tag3",
            "--id_value", "123",
            "--verbose"
        ], validate_ambiguities=False)
        
        assert result.tags == ["tag1", "tag2", "tag3"]
        assert result.ports is None  # default value
        assert result.id_value == "123"  # parsed as string
        assert result.verbose is True


class TestBackwardCompatibility:
    """Test that new features don't break backward compatibility."""
    
    def test_old_style_type_hints_still_work(self):
        """Test that old-style type hints still work."""
        class Args:
            name: str
            count: int = 42
            debug: bool
        
        specs = inspect_class(Args)
        
        name_spec = next(spec for spec in specs if spec.name == "name")
        assert name_spec.arg_type.primitive_type == str
        
        count_spec = next(spec for spec in specs if spec.name == "count")
        assert count_spec.arg_type.primitive_type == int
        assert count_spec.default == 42
        
        debug_spec = next(spec for spec in specs if spec.name == "debug")
        assert debug_spec.__class__.__name__ == "FlagArgSpec"
    
    def test_descriptors_still_work(self):
        """Test that descriptors still work with new type inference."""
        from argsclass import positional, option, flag
        
        class Args:
            # Traditional descriptors
            input_file = positional(help_text="Input file")
            output_file = option(help_text="Output file", aliases={"o"})
            verbose = flag(help_text="Verbose output")
            
            # New type hints
            tags: List[str]
            count: Optional[int] = 42
        
        specs = inspect_class(Args)
        
        # Should have all 5 specs
        assert len(specs) == 5
        
        # Descriptors should still work
        input_spec = next(spec for spec in specs if spec.name == "input_file")
        assert input_spec.__class__.__name__ == "PositionalArgSpec"
        
        output_spec = next(spec for spec in specs if spec.name == "output_file")
        assert output_spec.__class__.__name__ == "OptionArgSpec"
        assert "o" in output_spec.aliases
        
        verbose_spec = next(spec for spec in specs if spec.name == "verbose")
        assert verbose_spec.__class__.__name__ == "FlagArgSpec"
        
        # New type hints should work
        tags_spec = next(spec for spec in specs if spec.name == "tags")
        assert tags_spec.cardinality.min == 0
        assert tags_spec.cardinality.max is None
        
        count_spec = next(spec for spec in specs if spec.name == "count")
        assert count_spec.default == 42