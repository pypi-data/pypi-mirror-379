"""
CLI Error Handler
================

Handles errors and exceptions in CLI operations.
"""

from typing import Optional, Any
import traceback

from .result import CommandResult


class CLIErrorHandler:
    pass
    pass
    """Handles CLI errors and exceptions"""
    
    def __init__(self, logger=None):
    pass
    pass
        self.logger = logger
        
    def handle_exception(
        self, 
        exception: Exception, 
        context: str = "Command execution",
        return_result: bool = True
    ) -> Optional[CommandResult]:
    pass
        """Handle an exception and optionally return a CommandResult"""
        error_message = f"{context}: {str(exception)}"
        
        if self.logger:
    
        pass
    pass
    pass
            self.logger.error(error_message)
            self.logger.debug(f"Exception traceback: {traceback.format_exc()}")
        else:
    pass
            print(f"ERROR: {error_message}")
        
        if return_result:
    
        pass
    pass
            return CommandResult.error(
                error_message,
                details={"exception_type": type(exception).__name__}
            )
        
        return None
    
    def handle_validation_error(self, message: str) -> CommandResult:
    pass
        """Handle validation errors"""
        if self.logger:
    
        pass
    pass
            self.logger.error(f"Validation error: {message}")
        
        return CommandResult.error(f"Validation failed: {message}")
    
    def handle_configuration_error(self, message: str) -> CommandResult:
    pass
        """Handle configuration errors"""
        if self.logger:
    
        pass
    pass
            self.logger.error(f"Configuration error: {message}")
        
        return CommandResult.error(f"Configuration error: {message}")