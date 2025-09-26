"""Class inspection utilities for converting class attributes to ArgSpec objects."""

import inspect
from typing import Any, List, Type, get_type_hints, get_origin, get_args
from .models import BaseArgSpec, PositionalArgSpec, OptionArgSpec, FlagArgSpec, Cardinality, PrimitiveType
from .descriptors import PositionalDescriptor, OptionDescriptor, FlagDescriptor

# Support for modern Python union syntax (Python 3.10+)
try:
    from types import UnionType  # Python 3.10+
except ImportError:
    UnionType = type(None)  # Fallback for older versions


def inspect_class(cls: Type) -> List[BaseArgSpec]:
    """Inspect a class and convert its attributes to a list of ArgSpec objects.
    
    This function analyzes class attributes and their type hints to determine
    the appropriate ArgSpec type:
    - Boolean attributes become FlagArgSpec
    - Attributes with default values become OptionArgSpec
    - Attributes with positional() descriptors become PositionalArgSpec
    - Other attributes become OptionArgSpec with inferred types
    
    Args:
        cls: The class to inspect
        
    Returns:
        List of ArgSpec objects representing the class attributes
        
    Example:
        class Args:
            flag: bool
            option: str = "default"
            Name: str = positional(help="foo")
        
        specs = inspect_class(Args)
        # Returns [FlagArgSpec("flag"), OptionArgSpec("option"), PositionalArgSpec("Name")]
    """
    if not inspect.isclass(cls):
        raise TypeError("Expected a class, got {}".format(type(cls).__name__))
    
    specs = []
    type_hints = get_type_hints(cls)
    
    # Get all class attributes (including those from base classes)
    processed_names = set()
    
    # First, process attributes that exist in the class dict
    for name, value in cls.__dict__.items():
        # Skip private attributes and methods
        if name.startswith('_') or callable(value) or isinstance(value, (staticmethod, classmethod)):
            continue
        
        # Skip module-level attributes
        if inspect.ismodule(value):
            continue
        
        spec = _create_argspec_from_attribute(name, value, type_hints.get(name))
        if spec:
            specs.append(spec)
            processed_names.add(name)
    
    # Then, process type hints that don't have corresponding class attributes
    for name, type_hint in type_hints.items():
        if name not in processed_names and not name.startswith('_'):
            spec = _create_argspec_from_attribute(name, None, type_hint)
            if spec:
                specs.append(spec)
    
    return specs


def _create_argspec_from_attribute(name: str, value: Any, type_hint: Any) -> BaseArgSpec:
    """Create an ArgSpec from a class attribute.
    
    Args:
        name: The attribute name
        value: The attribute value (default value or descriptor)
        type_hint: The type hint for the attribute
        
    Returns:
        ArgSpec object or None if the attribute should be skipped
    """
    # Handle descriptors first
    if isinstance(value, PositionalDescriptor):
        return value.to_argspec()
    elif isinstance(value, OptionDescriptor):
        return value.to_argspec()
    elif isinstance(value, FlagDescriptor):
        return value.to_argspec()
    
    # Handle boolean type hints (become flags)
    if type_hint is bool or (type_hint is not None and _is_bool_type(type_hint)):
        return FlagArgSpec(
            name=name,
            help_text=""
        )
    
    # Check if this is a list type to set appropriate cardinality
    cardinality = None
    if type_hint is not None and _is_list_type(type_hint):
        cardinality = Cardinality.zero_or_more()  # Lists can accept multiple values
    
    # Handle attributes with default values (become options)
    if value is not None and not isinstance(value, type):
        # This is a default value, so it's an option
        arg_type = _infer_type_from_hint(type_hint)
        return OptionArgSpec(
            name=name,
            default=value,
            arg_type=arg_type,
            cardinality=cardinality or Cardinality.single(),
            help_text=""
        )
    
    # Handle attributes without default values
    # If they have a type hint, they become options
    if type_hint is not None:
        arg_type = _infer_type_from_hint(type_hint)
        return OptionArgSpec(
            name=name,
            arg_type=arg_type,
            cardinality=cardinality or Cardinality.single(),
            help_text=""
        )
    
    # Skip attributes without type hints and without default values
    return None


def _is_bool_type(type_hint: Any) -> bool:
    """Check if a type hint represents a boolean type."""
    if type_hint is bool:
        return True
    
    # Handle modern Python union syntax (Python 3.10+) - str | None, bool | int, etc.
    if hasattr(type_hint, '__args__') and hasattr(type_hint, '__origin__'):
        # Handle both UnionType (Python 3.10+) and typing.Union
        if get_origin(type_hint) in (UnionType, type(None).__class__) or get_origin(type_hint) is type(None):
            args = get_args(type_hint)
            return bool in args
    
    # Handle Optional[bool] and Union[bool, None]
    try:
        from typing import Union
        if get_origin(type_hint) is Union:
            args = get_args(type_hint)
            return bool in args
    except ImportError:
        pass
    
    return False


def _is_list_type(type_hint: Any) -> bool:
    """Check if a type hint represents a list type."""
    # Handle List types (Python 3.9+)
    origin = get_origin(type_hint)
    if origin is list:
        return True
    
    # Handle List[type] and list[type] syntax
    try:
        from typing import List
        if origin is List:
            return True
    except ImportError:
        pass
    
    return False


def _infer_type_from_hint(type_hint: Any) -> Any:
    """Infer the appropriate argument type from a type hint.
    
    Args:
        type_hint: The type hint to analyze
        
    Returns:
        Type or PrimitiveType instance
    """
    if type_hint is None:
        return str  # Default to string
    
    # Handle direct type hints
    if type_hint in (str, int, float):
        return type_hint
    
    # Handle List types (Python 3.9+)
    origin = get_origin(type_hint)
    if origin is list:
        args = get_args(type_hint)
        if args:
            # For List[str], List[int], etc., return the inner type
            inner_type = args[0]
            if inner_type in (str, int, float):
                return inner_type
        # Default to string for List without type parameter
        return str
    
    # Handle modern Python union syntax (Python 3.10+) - str | None, int | str, etc.
    if hasattr(type_hint, '__args__') and hasattr(type_hint, '__origin__'):
        # Handle both UnionType (Python 3.10+) and typing.Union
        if get_origin(type_hint) in (UnionType, type(None).__class__) or get_origin(type_hint) is type(None):
            args = get_args(type_hint)
            # Take the first non-None type
            for arg in args:
                if arg is not type(None) and arg in (str, int, float):
                    return arg
    
    # Handle Optional types and Union[type, None]
    try:
        from typing import Union
        if get_origin(type_hint) is Union:
            args = get_args(type_hint)
            # Take the first non-None type
            for arg in args:
                if arg is not type(None) and arg in (str, int, float):
                    return arg
    except ImportError:
        pass
    
    # Default to string for unknown types
    return str


def get_argspecs(cls: Type) -> List[BaseArgSpec]:
    """Alias for inspect_class for convenience."""
    return inspect_class(cls)