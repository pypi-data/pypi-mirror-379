"""Argparse-based parser for argsclass command line argument parsing.

This module provides the core argparse conversion logic, replacing the custom
parsing implementation with argparse while maintaining the ArgSpec API.
"""

import argparse
from typing import Any, List, Set, Union
from .models import BaseArgSpec, PositionalArgSpec, OptionArgSpec, FlagArgSpec, Cardinality
from .exceptions import HelpRequested, ArgumentParsingError


def _cardinality_to_nargs(cardinality: Cardinality) -> Any:
    """Convert Cardinality to argparse nargs value.
    
    Args:
        cardinality: The Cardinality object to convert
        
    Returns:
        The appropriate nargs value for argparse
    """
    if cardinality.min == 1 and cardinality.max == 1:
        return None  # Single value (default)
    elif cardinality.min == 0 and cardinality.max == 1:
        return "?"
    elif cardinality.min == 0 and cardinality.max is None:
        return "*"
    elif cardinality.min == 1 and cardinality.max is None:
        return "+"
    elif cardinality.min == cardinality.max:
        return cardinality.min
    else:
        # Custom cardinality - argparse doesn't support this directly
        # We'll use the closest approximation
        if cardinality.max is None:
            return "+"  # At least min, no upper limit
        else:
            return "*"  # 0 or more, let validation handle the min requirement


def _aliases_to_option_strings(name: str, aliases: Set[str]) -> List[str]:
    """Convert name and aliases to argparse option strings.
    
    Args:
        name: The main option name (without --)
        aliases: Set of alias names
        
    Returns:
        List of option strings for argparse
    """
    option_strings = [f"--{name}"]
    
    for alias in aliases:
        if len(alias) == 1:
            option_strings.append(f"-{alias}")
        else:
            option_strings.append(f"--{alias}")
    
    return option_strings


def _arg_type_to_argparse_type(arg_type: Any) -> Any:
    """Convert ArgSpec arg_type to argparse type.
    
    Args:
        arg_type: The argument type from ArgSpec
        
    Returns:
        The appropriate type for argparse
    """
    if arg_type is None:
        return str
    
    if hasattr(arg_type, 'convert'):
        return arg_type.convert
    
    if arg_type in (str, int, float, bool):
        return arg_type
    
    return str


def argspec_to_argparse(parser: argparse.ArgumentParser, spec: BaseArgSpec) -> None:
    """Add an ArgSpec to an argparse ArgumentParser.
    
    Args:
        parser: The argparse ArgumentParser to add the argument to
        spec: The ArgSpec to convert and add
    """
    if isinstance(spec, PositionalArgSpec):
        parser.add_argument(
            spec.name,
            help=spec.help_text,
            type=_arg_type_to_argparse_type(spec.arg_type),
            nargs=_cardinality_to_nargs(spec.cardinality),
            choices=spec.choices,
            default=spec.default
        )
    
    elif isinstance(spec, OptionArgSpec):
        option_strings = _aliases_to_option_strings(spec.name, spec.aliases)
        parser.add_argument(
            *option_strings,
            dest=spec.destination,
            help=spec.help_text,
            type=_arg_type_to_argparse_type(spec.arg_type),
            nargs=_cardinality_to_nargs(spec.cardinality),
            choices=spec.choices,
            default=spec.default
        )
    
    elif isinstance(spec, FlagArgSpec):
        option_strings = _aliases_to_option_strings(spec.name, spec.aliases)
        parser.add_argument(
            *option_strings,
            dest=spec.destination,
            help=spec.help_text,
            action="store_true",
            default=False
        )
    
    else:
        raise ValueError(f"Unsupported ArgSpec type: {type(spec)}")


def create_argparse_parser(
    arg_specs: List[BaseArgSpec],
    prog: str = None,
    description: str = None,
    epilog: str = None
) -> argparse.ArgumentParser:
    """Create an argparse ArgumentParser from a list of ArgSpec objects.
    
    Args:
        arg_specs: List of argument specifications
        prog: Program name for help messages
        description: Program description
        epilog: Text to display after argument help
        
    Returns:
        Configured argparse ArgumentParser
    """
    parser = argparse.ArgumentParser(
        prog=prog,
        description=description,
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    for spec in arg_specs:
        argspec_to_argparse(parser, spec)
    
    return parser


def parse_with_argparse(
    arg_specs: List[BaseArgSpec],
    argv: List[str],
    prog: str = None,
    description: str = None,
    epilog: str = None,
    ignore_unknown: bool = False
) -> dict:
    """Parse command line arguments using argparse.
    
    Args:
        arg_specs: List of argument specifications
        argv: Command line arguments to parse
        prog: Program name for help messages
        description: Program description
        epilog: Text to display after argument help
        ignore_unknown: Whether to ignore unknown arguments
        
    Returns:
        Dictionary of parsed argument values
        
    Raises:
        HelpRequested: If help is requested
        ArgumentParsingError: If parsing fails
    """
    # Handle empty argument specifications
    if not arg_specs:
        # If no arguments are defined, return empty dict
        # Check for help flag manually
        if any(arg in ['--help', '-h'] for arg in argv):
            # Create a minimal parser just for help
            parser = create_argparse_parser(arg_specs, prog, description, epilog)
            raise HelpRequested(parser.format_help())
        return {}
    
    parser = create_argparse_parser(arg_specs, prog, description, epilog)
    
    try:
        # Parse arguments
        if ignore_unknown:
            # Use parse_known_args to ignore unknown arguments
            args, unknown = parser.parse_known_args(argv)
        else:
            args = parser.parse_args(argv)
            
    except SystemExit as e:
        if e.code == 0:
            # Help was requested
            raise HelpRequested(parser.format_help())
        else:
            # Parse error - we need to capture the error message
            # Since argparse prints to stderr and exits, we need to catch this differently
            import sys
            from io import StringIO
            
            # Capture stderr to get the error message
            old_stderr = sys.stderr
            sys.stderr = StringIO()
            try:
                parser.parse_args(argv)
            except SystemExit:
                pass
            error_message = sys.stderr.getvalue()
            sys.stderr = old_stderr
            
            # Clean up the error message
            if error_message:
                # Remove the program name and "error:" prefix
                lines = error_message.strip().split('\n')
                if lines and 'error:' in lines[0]:
                    error_message = lines[0].split('error:', 1)[1].strip()
                else:
                    error_message = error_message.strip()
            else:
                error_message = "Parsing failed"
            
            raise ArgumentParsingError(error_message, parser.format_help())
    
    # Convert argparse Namespace to dictionary
    return vars(args)