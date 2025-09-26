"""Exception classes for argsclass command line argument parsing."""

from typing import Optional


class HelpRequested(Exception):
    """Exception raised when help is requested via --help flag.
    
    This exception is raised when the --help or -h flag is detected during
    argument parsing. It contains the formatted help message that should be
    displayed to the user.
    
    Attributes:
        help_message (str): The formatted help message to display
        
    Example:
        >>> try:
        ...     parse(specs, ["--help"])
        ... except HelpRequested as e:
        ...     print(e.help_message)
        ...     sys.exit(0)
    """
    
    def __init__(self, help_message: str):
        """Initialize help request exception.
        
        Args:
            help_message: The formatted help message to display
        """
        self.help_message = help_message
        super().__init__(help_message)


class ArgumentParsingError(Exception):
    """Exception raised when argument parsing fails with validation errors.
    
    This exception is raised when argument parsing encounters validation errors
    such as invalid values, missing required arguments, or unknown arguments.
    It contains both the error message describing the problems and an optional
    help message that can be displayed to guide the user.
    
    Attributes:
        error_message (str): The error message describing the problems
        help_message (Optional[str]): Optional help message to display
        
    Example:
        >>> try:
        ...     parse(specs, ["--unknown", "--port", "not_a_number"])
        ... except ArgumentParsingError as e:
        ...     print(e.error_message)
        ...     if e.help_message:
        ...         print()
        ...         print(e.help_message)
        ...     sys.exit(2)
    """
    
    def __init__(self, error_message: str, help_message: Optional[str] = None):
        """Initialize argument parsing error.
        
        Args:
            error_message: The error message describing the problems
            help_message: Optional help message to display
        """
        self.error_message = error_message
        self.help_message = help_message
        super().__init__(error_message)