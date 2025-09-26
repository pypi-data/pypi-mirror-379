"""Simple class-based argument parsing for python scripts."""

from .models import (
    BaseArgSpec, NamedArgSpec, PositionalArgSpec, OptionArgSpec, FlagArgSpec,
    Cardinality,
    ArgumentType, PrimitiveType
)
from .parser import parse, args, parser
from .exceptions import HelpRequested, ArgumentParsingError
from .descriptors import positional, option, flag
from .inspector import inspect_class, get_argspecs
from .ambiguity import AmbiguityError, detect_ambiguities, validate_no_ambiguities, is_ambiguous, get_ambiguity_resolution_suggestions
from .help import detect_help_flag, remove_help_flags, ValidationErrorCollector, ValidationError

# Configuration support (optional)
try:
    from .config import load_config_file, find_config_files, merge_configs, config_to_args, load_and_merge_configs, ConfigError
    _CONFIG_AVAILABLE = True
except ImportError:
    _CONFIG_AVAILABLE = False

__version__ = "0.4.1"
__all__ = [
    "BaseArgSpec", "NamedArgSpec", "PositionalArgSpec", "OptionArgSpec", "FlagArgSpec",
    "Cardinality",
    "ArgumentType", "PrimitiveType",
    "parse", "args", "parser",
    "HelpRequested", "ArgumentParsingError",
    "positional", "option", "flag",
    "inspect_class", "get_argspecs",
    "AmbiguityError", "detect_ambiguities", "validate_no_ambiguities", "is_ambiguous", "get_ambiguity_resolution_suggestions",
    "detect_help_flag", "remove_help_flags", "ValidationErrorCollector", "ValidationError"
]

# Add configuration functions to __all__ if available
if _CONFIG_AVAILABLE:
    __all__.extend([
        "load_config_file", "find_config_files", "merge_configs", "config_to_args", 
        "load_and_merge_configs", "ConfigError"
    ])