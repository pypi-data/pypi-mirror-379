"""Validation error handling and help flag detection for command line arguments.

This module provides validation error collection and reporting, and utility functions 
for help flag detection and processing. Help message generation is now handled by 
argparse through the argparse_parser module.

Classes:
    ValidationError: Represents a single validation error with context
    ValidationErrorCollector: Collects and manages multiple validation errors

Functions:
    detect_help_flag: Check if help flags are present in argv
    remove_help_flags: Remove help flags from argv list

Example:
    >>> from argsclass.help import detect_help_flag
    >>> from argsclass.models import PositionalArgSpec, OptionArgSpec, FlagArgSpec
    >>> 
    >>> specs = [
    ...     PositionalArgSpec(name="input", help_text="Input file"),
    ...     OptionArgSpec(name="output", help_text="Output file", aliases={"o"}),
    ...     FlagArgSpec(name="verbose", help_text="Verbose output", aliases={"v"})
    ... ]
    >>> 
    >>> # Check for help flag
    >>> if detect_help_flag(sys.argv):
    ...     from argsclass.argparse_parser import create_argparse_parser
    ...     parser = create_argparse_parser(specs, prog="myapp", description="My application")
    ...     print(parser.format_help())
    ...     sys.exit(0)
"""

import sys
from typing import List, Optional




class ValidationError:
    """Represents a validation error with context.
    
    This class encapsulates a single validation error with all relevant context
    information including the error message, argument name, value that caused
    the error, and error type.
    
    Attributes:
        message (str): The error message describing what went wrong
        argument (Optional[str]): Name of the argument that caused the error
        value (Optional[str]): The value that caused the error
        error_type (str): Type of error (default: "error")
    
    Example:
        >>> error = ValidationError("Invalid choice", argument="format", value="csv")
        >>> print(error)
        Invalid choice (argument format, value 'csv')
    """
    
    def __init__(self, message: str, argument: Optional[str] = None, 
                 value: Optional[str] = None, error_type: str = "error"):
        """Initialize validation error.
        
        Args:
            message: Error message describing what went wrong
            argument: Name of the argument that caused the error (optional)
            value: The value that caused the error (optional)
            error_type: Type of error - "error", "warning", etc. (default: "error")
        """
        self.message = message
        self.argument = argument
        self.value = value
        self.error_type = error_type
    
    def __str__(self) -> str:
        """String representation of the error.
        
        Returns:
            str: Formatted error message with context information
        """
        parts = []
        if self.argument:
            parts.append(f"argument {self.argument}")
        if self.value:
            parts.append(f"value '{self.value}'")
        if parts:
            return f"{self.message} ({', '.join(parts)})"
        else:
            return self.message


class ValidationErrorCollector:
    """Collects and manages validation errors.
    
    This class provides a centralized way to collect multiple validation errors
    during argument parsing, allowing all errors to be reported together rather
    than stopping at the first error encountered.
    
    Attributes:
        errors (List[ValidationError]): List of collected validation errors
    
    Example:
        >>> collector = ValidationErrorCollector()
        >>> collector.add_error("Invalid choice", argument="format", value="csv")
        >>> collector.add_error("Missing required argument", argument="input")
        >>> if collector.has_errors():
        ...     print(collector.format_errors())
    """
    
    def __init__(self):
        """Initialize error collector."""
        self.errors: List[ValidationError] = []
    
    def add_error(self, message: str, argument: Optional[str] = None, 
                  value: Optional[str] = None, error_type: str = "error"):
        """Add a validation error.
        
        Creates a new ValidationError and adds it to the collection.
        
        Args:
            message: Error message describing what went wrong
            argument: Name of the argument that caused the error (optional)
            value: The value that caused the error (optional)
            error_type: Type of error - "error", "warning", etc. (default: "error")
        """
        self.errors.append(ValidationError(message, argument, value, error_type))
    
    def has_errors(self) -> bool:
        """Check if there are any errors.
        
        Returns:
            bool: True if any errors have been collected, False otherwise
        """
        return len(self.errors) > 0
    
    def get_errors(self) -> List[ValidationError]:
        """Get all errors.
        
        Returns:
            List[ValidationError]: Copy of the errors list
        """
        return self.errors.copy()
    
    def clear(self):
        """Clear all errors.
        
        Removes all collected errors from the collector.
        """
        self.errors.clear()
    
    def format_errors(self) -> str:
        """Format all errors into a help message.
        
        Creates a formatted error message that includes all collected errors
        and a suggestion to use --help for more information.
        
        Returns:
            str: Formatted error message, or empty string if no errors
            
        Example:
            >>> collector = ValidationErrorCollector()
            >>> collector.add_error("Invalid choice", argument="format", value="csv")
            >>> print(collector.format_errors())
            error: the following arguments had problems:
            <BLANKLINE>
              Invalid choice (argument format, value 'csv')
            <BLANKLINE>
            use --help for more information
        """
        if not self.errors:
            return ""
        
        lines = []
        lines.append("error: the following arguments had problems:")
        lines.append("")
        
        for error in self.errors:
            lines.append(f"  {error}")
        
        lines.append("")
        lines.append("use --help for more information")
        
        return "\n".join(lines)




def detect_help_flag(argv: List[str]) -> bool:
    """Detect if --help or -h flag is present in argv.
    
    Checks if any of the standard help flags (--help or -h) are present
    in the provided argument list.
    
    Args:
        argv: List of command line arguments to check
        
    Returns:
        bool: True if --help or -h is found, False otherwise
        
    Example:
        >>> detect_help_flag(["--help"])
        True
        >>> detect_help_flag(["-h"])
        True
        >>> detect_help_flag(["script.py", "--help"])
        True
        >>> detect_help_flag(["script.py", "--verbose"])
        False
    """
    help_flags = {'--help', '-h'}
    return any(arg in help_flags for arg in argv)


def remove_help_flags(argv: List[str]) -> List[str]:
    """Remove help flags from argv.
    
    Creates a new list with all help flags (--help and -h) removed from
    the original argument list.
    
    Args:
        argv: List of command line arguments
        
    Returns:
        List[str]: New list with help flags removed
        
    Example:
        >>> remove_help_flags(["--help"])
        []
        >>> remove_help_flags(["-h"])
        []
        >>> remove_help_flags(["script.py", "--help", "--verbose"])
        ["script.py", "--verbose"]
        >>> remove_help_flags(["script.py", "--verbose"])
        ["script.py", "--verbose"]
    """
    help_flags = {'--help', '-h'}
    return [arg for arg in argv if arg not in help_flags]