"""Tests for configuration file support."""

import json
import tempfile
import pytest
from pathlib import Path
from argsclass.config import (
    load_config_file, find_config_files, merge_configs, 
    config_to_args, load_and_merge_configs, ConfigError
)


class TestLoadConfigFile:
    """Test loading configuration files."""
    
    def test_load_json_config(self):
        """Test loading JSON configuration file."""
        config_data = {"debug": True, "port": 8080, "host": "localhost"}
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(config_data, f)
            temp_file = f.name
        
        try:
            loaded_config = load_config_file(temp_file)
            assert loaded_config == config_data
        finally:
            Path(temp_file).unlink()
    
    def test_load_config_file_not_found(self):
        """Test loading non-existent configuration file."""
        with pytest.raises(ConfigError, match="Configuration file not found"):
            load_config_file("nonexistent.json")
    
    def test_load_config_unsupported_format(self):
        """Test loading unsupported file format."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("some text")
            temp_file = f.name
        
        try:
            with pytest.raises(ConfigError, match="Unsupported configuration file format"):
                load_config_file(temp_file)
        finally:
            Path(temp_file).unlink()
    
    def test_load_invalid_json(self):
        """Test loading invalid JSON file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write("{ invalid json")
            temp_file = f.name
        
        try:
            with pytest.raises(ConfigError, match="Failed to load configuration file"):
                load_config_file(temp_file)
        finally:
            Path(temp_file).unlink()


class TestFindConfigFiles:
    """Test finding configuration files."""
    
    def test_find_config_files(self):
        """Test finding configuration files in current directory."""
        # Create temporary config files
        config_files = []
        try:
            # Create a JSON config file in current directory
            config_file_path = Path("test_config.json")
            with open(config_file_path, 'w') as f:
                json.dump({"test": True}, f)
            config_files.append(config_file_path)
            
            # Find config files
            found_files = find_config_files("test_config")
            
            # Should find at least our test file
            assert len(found_files) >= 1
            assert any("test_config.json" in str(f) for f in found_files)
            
        finally:
            # Clean up
            for file_path in config_files:
                if file_path.exists():
                    file_path.unlink()
    
    def test_find_config_files_empty_search_paths(self):
        """Test finding config files with empty search paths."""
        found_files = find_config_files("nonexistent", search_paths=[])
        assert found_files == []


class TestMergeConfigs:
    """Test merging configuration dictionaries."""
    
    def test_merge_configs_last_wins(self):
        """Test merging configs with last wins strategy."""
        config1 = {"debug": True, "port": 8080}
        config2 = {"port": 9000, "host": "localhost"}
        
        merged = merge_configs([config1, config2], "last_wins")
        
        assert merged == {"debug": True, "port": 9000, "host": "localhost"}
    
    def test_merge_configs_first_wins(self):
        """Test merging configs with first wins strategy."""
        config1 = {"debug": True, "port": 8080}
        config2 = {"port": 9000, "host": "localhost"}
        
        merged = merge_configs([config1, config2], "first_wins")
        
        assert merged == {"debug": True, "port": 8080, "host": "localhost"}
    
    def test_merge_configs_deep(self):
        """Test deep merging of nested configurations."""
        config1 = {"database": {"host": "localhost", "port": 5432}}
        config2 = {"database": {"port": 3306, "name": "testdb"}}
        
        merged = merge_configs([config1, config2], "deep")
        
        expected = {"database": {"host": "localhost", "port": 3306, "name": "testdb"}}
        assert merged == expected
    
    def test_merge_configs_empty_list(self):
        """Test merging empty config list."""
        merged = merge_configs([])
        assert merged == {}
    
    def test_merge_configs_single_config(self):
        """Test merging single config."""
        config = {"debug": True, "port": 8080}
        merged = merge_configs([config])
        assert merged == config
    
    def test_merge_configs_unknown_strategy(self):
        """Test merging with unknown strategy."""
        config = {"debug": True}
        with pytest.raises(ValueError, match="Unknown merge strategy"):
            merge_configs([config], "unknown")


class TestConfigToArgs:
    """Test converting configuration to command-line arguments."""
    
    def test_config_to_args_basic(self):
        """Test basic config to args conversion."""
        config = {"debug": True, "port": 8080, "host": "localhost"}
        args = config_to_args(config)
        
        expected = ["--debug", "--port", "8080", "--host", "localhost"]
        assert args == expected
    
    def test_config_to_args_boolean_false(self):
        """Test config to args with boolean False."""
        config = {"debug": False, "verbose": True, "quiet": False}
        args = config_to_args(config)
        
        expected = ["--verbose"]  # Only True booleans are included
        assert args == expected
    
    def test_config_to_args_none_values(self):
        """Test config to args with None values."""
        config = {"debug": True, "port": None, "host": "localhost"}
        args = config_to_args(config)
        
        expected = ["--debug", "--host", "localhost"]  # None values are skipped
        assert args == expected
    
    def test_config_to_args_custom_prefix(self):
        """Test config to args with custom prefix."""
        config = {"debug": True, "port": 8080}
        args = config_to_args(config, prefix="-")
        
        expected = ["-debug", "-port", "8080"]
        assert args == expected


class TestLoadAndMergeConfigs:
    """Test loading and merging configurations."""
    
    def test_load_and_merge_configs_no_files(self):
        """Test loading and merging with no files."""
        merged = load_and_merge_configs(config_files=[], auto_discover=False)
        assert merged == {}
    
    def test_load_and_merge_configs_with_files(self):
        """Test loading and merging with explicit files."""
        config_data = {"debug": True, "port": 8080}
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(config_data, f)
            temp_file = f.name
        
        try:
            merged = load_and_merge_configs(config_files=[temp_file], auto_discover=False)
            assert merged == config_data
        finally:
            Path(temp_file).unlink()
    
    def test_load_and_merge_configs_multiple_files(self):
        """Test loading and merging multiple files."""
        config1 = {"debug": True, "port": 8080}
        config2 = {"port": 9000, "host": "localhost"}
        
        temp_files = []
        try:
            # Create first config file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
                json.dump(config1, f)
                temp_files.append(f.name)
            
            # Create second config file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
                json.dump(config2, f)
                temp_files.append(f.name)
            
            merged = load_and_merge_configs(config_files=temp_files, auto_discover=False)
            
            # Second file should override first file's values
            expected = {"debug": True, "port": 9000, "host": "localhost"}
            assert merged == expected
            
        finally:
            # Clean up
            for temp_file in temp_files:
                Path(temp_file).unlink()


class TestConfigIntegration:
    """Test configuration integration with argument parsing."""
    
    def test_config_with_parse_function(self):
        """Test using config files with the parse function."""
        from argsclass import parse, PositionalArgSpec, OptionArgSpec, FlagArgSpec
        
        config_data = {"output": "config_output.txt", "verbose": True}
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(config_data, f)
            temp_file = f.name
        
        try:
            from argsclass.models import Cardinality
            specs = [
                PositionalArgSpec(name="input", cardinality=Cardinality.zero_or_one()),  # Make optional
                OptionArgSpec(name="output", aliases={"o"}),
                FlagArgSpec(name="verbose", aliases={"v"})
            ]
            
            # Parse with config file - use empty argv to test config-only parsing
            result = parse(specs, argv=[], config_files=[temp_file])
            
            # Config values should be used as defaults
            assert result["input"] is None  # No input provided
            assert result["output"] == "config_output.txt"
            assert result["verbose"] is True
            
        finally:
            Path(temp_file).unlink()
    
    def test_config_with_class(self):
        """Test using config files with class-based parsing."""
        from argsclass import parse
        
        config_data = {"output_file": "config_output.txt", "debug": True}
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(config_data, f)
            temp_file = f.name
        
        try:
            class Args:
                input_file: str = "default_input.txt"
                output_file: str = "default_output.txt"
                debug: bool = False
            
            # Parse with config file - use empty argv to test config-only parsing
            result = parse(Args, argv=[], config_files=[temp_file])
            
            # Config values should override class defaults
            assert result.input_file == "default_input.txt"  # Not in config, uses class default
            assert result.output_file == "config_output.txt"  # From config
            assert result.debug is True  # From config
            
        finally:
            Path(temp_file).unlink()