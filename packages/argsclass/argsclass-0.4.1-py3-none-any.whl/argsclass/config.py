"""Configuration file support for argsclass.

This module provides utilities for loading configuration from files and merging
them with command-line arguments, allowing users to define default values in
configuration files while still allowing command-line overrides.
"""

import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False

try:
    import tomllib  # Python 3.11+
    TOML_AVAILABLE = True
except ImportError:
    try:
        import tomli as tomllib  # Fallback for older versions
        TOML_AVAILABLE = True
    except ImportError:
        TOML_AVAILABLE = False


class ConfigError(Exception):
    """Exception raised for configuration-related errors."""
    pass


def load_config_file(file_path: Union[str, Path]) -> Dict[str, Any]:
    """Load configuration from a file.
    
    Supports JSON, YAML, and TOML formats based on file extension.
    
    Args:
        file_path: Path to the configuration file
        
    Returns:
        Dictionary containing the configuration data
        
    Raises:
        ConfigError: If the file cannot be read or parsed
        ImportError: If required dependencies are missing
        
    Example:
        >>> config = load_config_file("config.json")
        >>> print(config)
        {'debug': True, 'port': 8080}
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise ConfigError(f"Configuration file not found: {file_path}")
    
    suffix = file_path.suffix.lower()
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            if suffix == '.json':
                return json.load(f)
            elif suffix in ('.yaml', '.yml'):
                if not YAML_AVAILABLE:
                    raise ImportError("PyYAML is required to read YAML files. Install with: pip install PyYAML")
                return yaml.safe_load(f)
            elif suffix == '.toml':
                if not TOML_AVAILABLE:
                    raise ImportError("tomli/tomllib is required to read TOML files. Install with: pip install tomli")
                return tomllib.load(f)
            else:
                raise ConfigError(f"Unsupported configuration file format: {suffix}")
    except Exception as e:
        raise ConfigError(f"Failed to load configuration file {file_path}: {e}")


def find_config_files(
    base_name: str = "config",
    search_paths: Optional[List[Union[str, Path]]] = None
) -> List[Path]:
    """Find configuration files with common names in search paths.
    
    Searches for files with names like config.json, config.yaml, config.toml
    in the specified search paths.
    
    Args:
        base_name: Base name for configuration files (default: "config")
        search_paths: List of directories to search (default: current directory and common locations)
        
    Returns:
        List of found configuration file paths
        
    Example:
        >>> configs = find_config_files("myapp")
        >>> print(configs)
        [Path('/home/user/.config/myapp.json'), Path('./myapp.yaml')]
    """
    if search_paths is None:
        search_paths = [
            Path.cwd(),  # Current directory
            Path.home() / ".config",  # User config directory
            Path("/etc"),  # System config directory
        ]
    
    extensions = ['.json']
    if YAML_AVAILABLE:
        extensions.extend(['.yaml', '.yml'])
    if TOML_AVAILABLE:
        extensions.append('.toml')
    
    found_files = []
    
    for search_path in search_paths:
        search_path = Path(search_path)
        if not search_path.exists():
            continue
            
        for ext in extensions:
            config_file = search_path / f"{base_name}{ext}"
            if config_file.exists():
                found_files.append(config_file)
    
    return found_files


def merge_configs(
    configs: List[Dict[str, Any]],
    merge_strategy: str = "last_wins"
) -> Dict[str, Any]:
    """Merge multiple configuration dictionaries.
    
    Args:
        configs: List of configuration dictionaries to merge
        merge_strategy: How to handle conflicts ("last_wins", "first_wins", "deep")
        
    Returns:
        Merged configuration dictionary
        
    Example:
        >>> config1 = {"debug": True, "port": 8080}
        >>> config2 = {"port": 9000, "host": "localhost"}
        >>> merged = merge_configs([config1, config2])
        >>> print(merged)
        {'debug': True, 'port': 9000, 'host': 'localhost'}
    """
    # Validate merge strategy first
    if merge_strategy not in ("first_wins", "last_wins", "deep"):
        raise ValueError(f"Unknown merge strategy: {merge_strategy}")
    
    if not configs:
        return {}
    
    if len(configs) == 1:
        return configs[0].copy()
    
    if merge_strategy == "first_wins":
        # Reverse the list so first config takes precedence
        configs = configs[::-1]
        merge_strategy = "last_wins"
    
    result = {}
    
    if merge_strategy == "last_wins":
        # Simple merge where later configs override earlier ones
        for config in configs:
            result.update(config)
    
    elif merge_strategy == "deep":
        # Deep merge for nested dictionaries
        for config in configs:
            result = _deep_merge(result, config)
    
    return result


def _deep_merge(base: Dict[str, Any], update: Dict[str, Any]) -> Dict[str, Any]:
    """Deep merge two dictionaries."""
    result = base.copy()
    
    for key, value in update.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = value
    
    return result


def config_to_args(
    config: Dict[str, Any],
    prefix: str = "--"
) -> List[str]:
    """Convert configuration dictionary to command-line arguments.
    
    Args:
        config: Configuration dictionary
        prefix: Prefix for argument names (e.g., "--")
        
    Returns:
        List of command-line arguments
        
    Example:
        >>> config = {"debug": True, "port": 8080, "host": "localhost"}
        >>> args = config_to_args(config)
        >>> print(args)
        ['--debug', '--port', '8080', '--host', 'localhost']
    """
    args = []
    
    for key, value in config.items():
        if isinstance(value, bool):
            if value:  # Only add boolean flags if they're True
                args.append(f"{prefix}{key}")
        elif value is not None:
            args.append(f"{prefix}{key}")
            args.append(str(value))
    
    return args


def load_and_merge_configs(
    config_files: Optional[List[Union[str, Path]]] = None,
    base_name: str = "config",
    auto_discover: bool = True,
    merge_strategy: str = "last_wins"
) -> Dict[str, Any]:
    """Load and merge configuration from multiple sources.
    
    Args:
        config_files: Explicit list of config files to load
        base_name: Base name for auto-discovery
        auto_discover: Whether to auto-discover config files
        merge_strategy: How to merge conflicting values
        
    Returns:
        Merged configuration dictionary
        
    Example:
        >>> config = load_and_merge_configs()
        >>> print(config)
        {'debug': True, 'port': 8080}
    """
    all_configs = []
    
    # Load explicitly specified config files
    if config_files:
        for config_file in config_files:
            try:
                config_data = load_config_file(config_file)
                all_configs.append(config_data)
            except ConfigError as e:
                print(f"Warning: {e}", file=sys.stderr)
    
    # Auto-discover config files
    if auto_discover:
        discovered_files = find_config_files(base_name)
        for config_file in discovered_files:
            try:
                config_data = load_config_file(config_file)
                all_configs.append(config_data)
            except ConfigError as e:
                print(f"Warning: {e}", file=sys.stderr)
    
    return merge_configs(all_configs, merge_strategy)