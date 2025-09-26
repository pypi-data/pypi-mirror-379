"""Parser module for command line argument parsing.

This module provides the core parsing functionality for command line arguments,
including context management, argument-specific parsers, and high-level parsing
functions with help system integration.

Classes:
    ParserContext: Manages parsing state and argument consumption
    PositionalArgumentParser: Parses positional arguments
    OptionArgumentParser: Parses option arguments (--option value)
    FlagArgumentParser: Parses flag arguments (--flag)
    HelpRequested: Exception raised when help is requested
    ArgumentParsingError: Exception raised when parsing fails with errors

Functions:
    parse: Main parsing function for classes or argument specifications
    args: Class decorator for immediate argument parsing
    parser: Class decorator that adds a parse() method

Example:
    >>> from argsclass.parser import parse
    >>> from argsclass.models import PositionalArgSpec, OptionArgSpec, FlagArgSpec
    >>> 
    >>> specs = [
    ...     PositionalArgSpec(name="input", help_text="Input file"),
    ...     OptionArgSpec(name="output", help_text="Output file", aliases={"o"}),
    ...     FlagArgSpec(name="verbose", help_text="Verbose output", aliases={"v"})
    ... ]
    >>> 
    >>> try:
    ...     result = parse(specs, ["input.txt", "-o", "output.txt", "-v"])
    ...     print(f"Input: {result['input']}")
    ...     print(f"Output: {result['output']}")
    ...     print(f"Verbose: {result['verbose']}")
    ... except HelpRequested as e:
    ...     print(e.help_message)
    ...     sys.exit(0)
    ... except ArgumentParsingError as e:
    ...     print(e.error_message)
    ...     sys.exit(2)
"""

import inspect
import sys
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, Callable
from .models import BaseArgSpec, PositionalArgSpec, FlagArgSpec, OptionArgSpec
from .help import detect_help_flag, remove_help_flags
from .argparse_parser import parse_with_argparse
from .exceptions import HelpRequested, ArgumentParsingError

T = TypeVar('T')






def parse(arg_specs_or_class, argv: Optional[List[str]] = None, validate_ambiguities: bool = True,
          prog: Optional[str] = None, description: Optional[str] = None, epilog: Optional[str] = None,
          ignore_unknown: bool = False, config_files: Optional[List[str]] = None, 
          config_base_name: str = "config", auto_discover_config: bool = True) -> Any:
    """Parse command line arguments and return a class instance or dictionary.
    
    This is the main parsing function that handles both class-based and specification-based
    argument parsing. It automatically detects help flags, validates arguments, and
    provides comprehensive error reporting. It also supports loading configuration files
    and merging them with command-line arguments.
    
    Args:
        arg_specs_or_class: Either a list of argument specifications (List[BaseArgSpec]) 
                           or a class that can be inspected to generate ArgSpec objects
        argv: Command line arguments to parse (defaults to sys.argv)
        validate_ambiguities: Whether to validate for ambiguous configurations (default: True)
        prog: Program name for help messages (defaults to sys.argv[0])
        description: Program description for help messages
        epilog: Text to display after argument help
        ignore_unknown: Whether to ignore unknown arguments instead of raising errors (default: False)
        config_files: List of configuration files to load (JSON, YAML, TOML)
        config_base_name: Base name for auto-discovering config files (default: "config")
        auto_discover_config: Whether to auto-discover config files (default: True)
        
    Returns:
        If arg_specs_or_class is a class: An instance of that class with parsed argument values
        If arg_specs_or_class is a list: Dictionary of parsed argument values keyed by destination names
        
    Raises:
        HelpRequested: If --help flag is detected (contains help_message attribute)
        ArgumentParsingError: If parsing fails with validation errors (contains error_message and help_message)
        AmbiguityError: If ambiguous argument configurations are detected (when validate_ambiguities=True)
    
    Example:
        >>> # Using with argument specifications
        >>> specs = [
        ...     PositionalArgSpec(name="input", help_text="Input file"),
        ...     OptionArgSpec(name="output", help_text="Output file", aliases={"o"}),
        ...     FlagArgSpec(name="verbose", help_text="Verbose output", aliases={"v"})
        ... ]
        >>> result = parse(specs, ["input.txt", "-o", "output.txt", "-v"])
        >>> print(result["input"], result["output"], result["verbose"])
        input.txt output.txt True
        
        >>> # Using with a class and configuration files
        >>> class Args:
        ...     input_file: str = "input.txt"
        ...     verbose: bool
        >>> args = parse(Args, config_files=["config.json"])
        >>> print(args.input_file, args.verbose)
        input.txt True
    """
    # Default argv to sys.argv if not provided
    if argv is None:
        argv = sys.argv
    
    # Load configuration files if requested
    config_args = []
    if config_files or auto_discover_config:
        try:
            from .config import load_and_merge_configs, config_to_args
            config_data = load_and_merge_configs(
                config_files=config_files,
                base_name=config_base_name,
                auto_discover=auto_discover_config
            )
            if config_data:
                config_args = config_to_args(config_data)
        except ImportError:
            # Configuration support is optional
            pass
    
    # Merge configuration arguments with command line arguments
    # Command line arguments take precedence over config file arguments
    if config_args:
        # Insert config args after the script name but before other arguments
        if argv and argv[0].endswith('.py'):
            # Split script name from other args
            script_name = argv[0]
            other_args = argv[1:] if len(argv) > 1 else []
            argv = [script_name] + config_args + other_args
        else:
            argv = config_args + argv
    
    # Convert class to ArgSpec list if needed
    if isinstance(arg_specs_or_class, list):
        arg_specs = arg_specs_or_class
        is_class = False
    else:
        # Assume it's a class that can be inspected
        from .inspector import inspect_class
        arg_specs = inspect_class(arg_specs_or_class)
        is_class = True
        cls = arg_specs_or_class
    
    # Check for help flag before processing
    if detect_help_flag(argv):
        from .argparse_parser import create_argparse_parser
        parser = create_argparse_parser(arg_specs, prog=prog, description=description, epilog=epilog)
        raise HelpRequested(parser.format_help())
    
    # Validate for ambiguities if requested
    if validate_ambiguities:
        from .ambiguity import validate_no_ambiguities
        validate_no_ambiguities(arg_specs)
    
    # Skip the script name (first argument) if present
    if argv and argv[0].endswith('.py'):
        argv = argv[1:]
    
    # Remove help flags from argv
    argv = remove_help_flags(argv)
    
    # Use argparse-based parsing
    try:
        parsed_values = parse_with_argparse(
            arg_specs, argv, prog=prog, description=description, epilog=epilog, ignore_unknown=ignore_unknown
        )
    except HelpRequested:
        # Re-raise help requests as-is
        raise
    except ArgumentParsingError:
        # Re-raise parsing errors as-is
        raise
    except Exception as e:
        # Convert any other exceptions to ArgumentParsingError
        from .argparse_parser import create_argparse_parser
        parser = create_argparse_parser(arg_specs, prog=prog, description=description, epilog=epilog)
        help_message = parser.format_help()
        error_message = f"Parsing failed: {e}"
        raise ArgumentParsingError(error_message, help_message)
    
    # Return class instance if a class was provided, otherwise return dict
    if is_class:
        # Ensure the class has @dataclass decorator if it doesn't have a custom __init__
        cls = _ensure_dataclass(cls)
        
        # Create an instance of the class with the parsed values
        try:
            # Check if the class is a dataclass with init=False
            if hasattr(cls, '__dataclass_fields__'):
                # Check if it's a dataclass with init=False by looking at the __init__ signature
                init_signature = inspect.signature(cls.__init__)
                # For init=False dataclasses, the signature is (self, /, *args, **kwargs)
                # For init=True dataclasses, the signature has specific field parameters
                if len(init_signature.parameters) == 3 and 'args' in init_signature.parameters and 'kwargs' in init_signature.parameters:
                    # It's a dataclass with init=False, manually set attributes
                    instance = object.__new__(cls)
                    for field_name, value in parsed_values.items():
                        setattr(instance, field_name, value)
                    return instance
            
            # Regular class or dataclass with init=True, use normal instantiation
            return cls(**parsed_values)
        except TypeError as e:
            # Provide more helpful error message
            from .argparse_parser import create_argparse_parser
            parser = create_argparse_parser(arg_specs, prog=prog, description=description, epilog=epilog)
            help_message = parser.format_help()
            error_message = f"Failed to create instance of {cls.__name__} with parsed values: {e}"
            raise ArgumentParsingError(error_message, help_message)
    else:
        # Return dictionary for backward compatibility with ArgSpec lists
        return parsed_values


def _ensure_dataclass(cls: Type[T]) -> Type[T]:
    """Ensure a class has the @dataclass decorator applied.
    
    This function checks if a class already has a custom __init__ method or
    is already a dataclass. If not, it applies the @dataclass decorator with
    init=False to avoid field ordering issues.
    
    Args:
        cls: The class to check and potentially modify
        
    Returns:
        Type[T]: The class with @dataclass decorator applied if needed
        
    Note:
        The function uses init=False to avoid field ordering issues and handles
        initialization manually in the parse function.
    """
    # Check if the class already has __init__ method
    if hasattr(cls, '__init__') and cls.__init__ is not object.__init__:
        # Class already has a custom __init__, don't modify it
        return cls
    
    # Check if the class is already a dataclass
    if hasattr(cls, '__dataclass_fields__'):
        return cls
    
    # Apply @dataclass decorator with init=False to avoid field ordering issues
    # We'll handle initialization manually in the parse function
    return dataclass(init=False)(cls)


def args(
    cls_or_argv: Union[Type[T], Optional[List[str]]] = None,
    validate_ambiguities: bool = True,
    program_name: Optional[str] = None,
    argv: Optional[List[str]] = None,
    description: Optional[str] = None,
    epilog: Optional[str] = None,
    ignore_unknown: bool = False
) -> Union[T, Callable[[Type[T]], T]]:
    """Class decorator that automatically parses command line arguments and returns an instance.
    
    This decorator transforms a class into an instance with parsed command line arguments.
    The class name becomes a reference to the parsed instance. It automatically handles
    help requests and validation errors by printing messages and exiting with appropriate codes.
    
    Supports both @args and @args() syntax:
    - @args: Uses default options (sys.argv, validate_ambiguities=True)
    - @args(): Same as @args
    - @args(program_name="myapp"): Custom options
    
    Args:
        cls_or_argv: Either a class (when used as @args) or argv list (when used as @args(...))
        validate_ambiguities: Whether to validate for ambiguous configurations (default: True)
        program_name: Override program name for help text (defaults to script name)
        argv: Command line arguments to parse (defaults to sys.argv)
        description: Program description for help messages
        epilog: Text to display after argument help
        ignore_unknown: Whether to ignore unknown arguments instead of raising errors (default: False)
        
    Returns:
        Either a parsed instance (when used as @args) or a decorator function (when used as @args(...))
        
    Note:
        This decorator automatically handles help requests (--help) and validation errors
        by printing appropriate messages and exiting with codes 0 (help) or 2 (error).
        
    Example:
        @args
        class Args:
            input_file: str = "input.txt"
            output_file: str = "output.txt"
            verbose: bool
        
        # Args is now an instance with parsed values
        print(Args.input_file)  # Access parsed values directly
        print(Args.verbose)
        
    Example with options:
        @args(program_name="myapp", validate_ambiguities=False)
        class Config:
            port: int = 8080
            debug: bool
    """
    # Check if the first argument is a class (no brackets usage)
    if cls_or_argv is not None and inspect.isclass(cls_or_argv):
        # @args usage (no brackets) - cls_or_argv is actually the class
        cls = cls_or_argv
        method_argv = argv  # Use provided argv or None (which will default to sys.argv)
        
        # Store the original class before any modifications
        original_class = cls
        
        try:
            # Parse the arguments and create an instance
            instance = parse(cls, method_argv, validate_ambiguities, 
                           prog=program_name, description=description, epilog=epilog, ignore_unknown=ignore_unknown)
        except HelpRequested as e:
            print(e.help_message)
            sys.exit(0)
        except ArgumentParsingError as e:
            print(e.error_message)
            if e.help_message:
                print()
                print(e.help_message)
            sys.exit(2)
        
        # Store the original class for introspection
        instance._original_class = original_class
        
        # Add some useful attributes
        instance._program_name = program_name or (sys.argv[0] if sys.argv else "program")
        instance._validate_ambiguities = validate_ambiguities
        
        return instance
    
    # @args(...) usage (with brackets) - cls_or_argv is actually argv
    decorator_argv = cls_or_argv
    
    def decorator(cls: Type[T]) -> T:
        """The actual decorator that transforms the class into an instance."""
        # Use provided argv or decorator argv or None (which will default to sys.argv)
        method_argv = argv if argv is not None else decorator_argv
        
        # Store the original class before any modifications
        original_class = cls
        
        try:
            # Parse the arguments and create an instance
            instance = parse(original_class, method_argv, validate_ambiguities,
                           prog=program_name, description=description, epilog=epilog, ignore_unknown=ignore_unknown)
        except HelpRequested as e:
            print(e.help_message)
            sys.exit(0)
        except ArgumentParsingError as e:
            print(e.error_message)
            if e.help_message:
                print()
                print(e.help_message)
            sys.exit(2)
        
        # Store the original class for introspection
        instance._original_class = original_class
        
        # Add some useful attributes
        instance._program_name = program_name or (method_argv[0] if method_argv else sys.argv[0]) if (method_argv or sys.argv) else "program"
        instance._validate_ambiguities = validate_ambiguities
        
        return instance
    
    return decorator


def parser(
    cls_or_argv: Union[Type[T], Optional[List[str]]] = None,
    validate_ambiguities: bool = True,
    program_name: Optional[str] = None,
    argv: Optional[List[str]] = None,
    description: Optional[str] = None,
    epilog: Optional[str] = None,
    ignore_unknown: bool = False
) -> Union[Type[T], Callable[[Type[T]], Type[T]]]:
    """Class decorator that adds a static parse() method to the class.
    
    This decorator transforms a class by adding a static parse() method that
    returns an instance with parsed command line arguments. Unlike @args,
    this doesn't parse immediately - it adds the parse() method for later use.
    The parse() method automatically handles help requests and validation errors.
    
    Supports both @parser and @parser() syntax:
    - @parser: Adds parse() method with default options
    - @parser(): Same as @parser
    - @parser(program_name="myapp"): Custom options for the parse() method
    
    Args:
        cls_or_argv: Either a class (when used as @parser) or argv list (when used as @parser(...))
        validate_ambiguities: Whether to validate for ambiguous configurations (default: True)
        program_name: Override program name for help text (defaults to script name)
        argv: Command line arguments to parse (defaults to sys.argv)
        description: Program description for help messages
        epilog: Text to display after argument help
        ignore_unknown: Whether to ignore unknown arguments instead of raising errors (default: False)
        
    Returns:
        Either the modified class (when used as @parser) or a decorator function (when used as @parser(...))
        
    Note:
        The added parse() method automatically handles help requests (--help) and validation errors
        by printing appropriate messages and exiting with codes 0 (help) or 2 (error).
        
    Example:
        @parser
        class Args:
            input_file: str = "input.txt"
            output_file: str = "output.txt"
            verbose: bool
        
        # Parse when you want to
        args = Args.parse()
        print(args.input_file)  # Access parsed values
        
    Example with options:
        @parser(program_name="myapp", validate_ambiguities=False)
        class Config:
            port: int = 8080
            debug: bool
        
        # Parse with custom options
        config = Config.parse()
    """
    # Check if the first argument is a class (no brackets usage)
    if cls_or_argv is not None and inspect.isclass(cls_or_argv):
        # @parser usage (no brackets) - cls_or_argv is actually the class
        cls = cls_or_argv
        decorator_argv = argv  # Use provided argv or None (which will default to sys.argv)
        
        # Store the original class before any modifications
        original_class = cls
        
        # Add the parse method to the class
        @staticmethod
        def parse_method(custom_argv: Optional[List[str]] = None) -> T:
            """Static method that parses command line arguments and returns an instance."""
            # Use custom_argv if provided, otherwise use the decorator's argv, otherwise use sys.argv
            method_argv = custom_argv if custom_argv is not None else decorator_argv
            
            try:
                # Parse the arguments and create an instance
                instance = parse(original_class, method_argv, validate_ambiguities,
                               prog=program_name, description=description, epilog=epilog)
            except HelpRequested as e:
                print(e.help_message)
                sys.exit(0)
            except ArgumentParsingError as e:
                print(e.error_message)
                if e.help_message:
                    print()
                    print(e.help_message)
                sys.exit(2)
            
            # Store the original class for introspection
            instance._original_class = original_class
            
            # Add some useful attributes
            instance._program_name = program_name or (method_argv[0] if method_argv else sys.argv[0]) if (method_argv or sys.argv) else "program"
            instance._validate_ambiguities = validate_ambiguities
            
            return instance
        
        # Add the static method to the class
        cls.parse = parse_method
        
        return cls
    
    # @parser(...) usage (with brackets) - cls_or_argv is actually argv
    decorator_argv = cls_or_argv
    
    def decorator(cls: Type[T]) -> Type[T]:
        """The actual decorator that adds the parse method to the class."""
        # Store the original class before any modifications
        original_class = cls
        
        # Add the parse method to the class
        @staticmethod
        def parse_method(custom_argv: Optional[List[str]] = None) -> T:
            """Static method that parses command line arguments and returns an instance."""
            # Use custom_argv if provided, otherwise use the decorator's argv, otherwise use sys.argv
            method_argv = custom_argv if custom_argv is not None else (argv if argv is not None else decorator_argv)
            
            try:
                # Parse the arguments and create an instance
                instance = parse(original_class, method_argv, validate_ambiguities,
                               prog=program_name, description=description, epilog=epilog)
            except HelpRequested as e:
                print(e.help_message)
                sys.exit(0)
            except ArgumentParsingError as e:
                print(e.error_message)
                if e.help_message:
                    print()
                    print(e.help_message)
                sys.exit(2)
            
            # Store the original class for introspection
            instance._original_class = original_class
            
            # Add some useful attributes
            instance._program_name = program_name or (method_argv[0] if method_argv else sys.argv[0]) if (method_argv or sys.argv) else "program"
            instance._validate_ambiguities = validate_ambiguities
            
            return instance
        
        # Add the static method to the class
        cls.parse = parse_method
        
        return cls
    
    return decorator

