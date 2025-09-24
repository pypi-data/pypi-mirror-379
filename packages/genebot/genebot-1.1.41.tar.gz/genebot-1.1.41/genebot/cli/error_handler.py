"""
CLI Error Handler
================

Handles errors and exceptions in CLI operations.
"""

from typing import Optional, Any
import traceback

from .result import CommandResult


class CLIErrorHandler:
    """Handles CLI errors and exceptions"""
    
    def __init__(self, logger=None):
        self.logger = logger
        
    def handle_exception(
        self, 
        exception: Exception, 
        context: str = "Command execution",
        return_result: bool = True
    ) -> Optional[CommandResult]:
        """Handle an exception and optionally return a CommandResult"""
        error_message = f"{context}: {str(exception)}"
        
        if self.logger:
            self.logger.error(error_message)
            self.logger.debug(f"Exception traceback: {traceback.format_exc()}")
        else:
            print(f"ERROR: {error_message}")
        
        if return_result:
            return CommandResult.error(
                error_message,
                details={"exception_type": type(exception).__name__}
            )
        
        return None
    
    def handle_validation_error(self, message: str) -> CommandResult:
        """Handle validation errors"""
        if self.logger:
            self.logger.error(f"Validation error: {message}")
        
        return CommandResult.error(f"Validation failed: {message}")
    
    def handle_configuration_error(self, message: str) -> CommandResult:
        """Handle configuration errors"""
        if self.logger:
            self.logger.error(f"Configuration error: {message}")
        
        return CommandResult.error(f"Configuration error: {message}")