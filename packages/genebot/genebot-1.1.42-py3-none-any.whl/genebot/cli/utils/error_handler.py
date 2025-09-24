"""
CLI Error Handling
==================

Comprehensive error handling with user-friendly messages and recovery suggestions.
"""

import sys
import traceback
import logging
import os
import subprocess
from pathlib import Path
from datetime import datetime, timezone
import json
from typing import List, Optional, Dict, Any, Callable

from ..result import CommandResult, ResultStatus


class CLIException(Exception):
    pass
    """Base CLI exception with user-friendly messages"""
    
    def __init__(self, message: str, suggestions: List[str] = None, 
                 error_code: Optional[str] = None, context: Optional[Dict[str, Any]] = None,
                 recovery_actions: Optional[List[Callable]] = None):
    pass
        self.message = message
        self.suggestions = suggestions or []
        self.error_code = error_code
        self.context = context or {}
        self.recovery_actions = recovery_actions or []
        self.timestamp = datetime.now(timezone.utc)
        super().__init__(message)
    
    def to_dict(self) -> Dict[str, Any]:
    pass
        """Convert exception to dictionary for logging/serialization"""
        return {
            'error_type': self.__class__.__name__,
            'error_code': self.error_code,
            'message': self.message,
            'suggestions': self.suggestions,
            'context': self.context,
            'timestamp': self.timestamp.isoformat()
        }


class ConfigurationError(CLIException):
    pass
    """Configuration-related errors"""
    
    def __init__(self, message: str, config_file: Optional[str] = None, 
                 config_key: Optional[str] = None, **kwargs):
    pass
        super().__init__(message, **kwargs)
        self.config_file = config_file
        self.config_key = config_key
        if config_file:
    
        pass
    pass
            self.context['config_file'] = config_file
        if config_key:
    
        pass
    pass
            self.context['config_key'] = config_key


class AccountError(CLIException):
    pass
    """Account management errors"""
    
    def __init__(self, message: str, account_name: Optional[str] = None,
                 account_type: Optional[str] = None, exchange: Optional[str] = None, **kwargs):
    pass
        super().__init__(message, **kwargs)
        self.account_name = account_name
        self.account_type = account_type
        self.exchange = exchange
        if account_name:
    
        pass
    pass
            self.context['account_name'] = account_name
        if account_type:
    
        pass
    pass
            self.context['account_type'] = account_type
        if exchange:
    
        pass
    pass
            self.context['exchange'] = exchange


class ProcessError(CLIException):
    pass
    """Bot process management errors"""
    
    def __init__(self, message: str, pid: Optional[int] = None,
                 process_name: Optional[str] = None, **kwargs):
    pass
        super().__init__(message, **kwargs)
        self.pid = pid
        self.process_name = process_name
        if pid:
    
        pass
    pass
            self.context['pid'] = pid
        if process_name:
    
        pass
    pass
            self.context['process_name'] = process_name


class DataError(CLIException):
    pass
    """Data access and reporting errors"""
    
    def __init__(self, message: str, data_source: Optional[str] = None,
                 operation: Optional[str] = None, **kwargs):
    pass
        super().__init__(message, **kwargs)
        self.data_source = data_source
        self.operation = operation
        if data_source:
    
        pass
    pass
            self.context['data_source'] = data_source
        if operation:
    
        pass
    pass
            self.context['operation'] = operation


class ValidationError(CLIException):
    pass
    """Validation errors"""
    
    def __init__(self, message: str, field_name: Optional[str] = None,
                 field_value: Optional[Any] = None, validation_rule: Optional[str] = None, **kwargs):
    pass
        super().__init__(message, **kwargs)
        self.field_name = field_name
        self.field_value = field_value
        self.validation_rule = validation_rule
        if field_name:
    
        pass
    pass
            self.context['field_name'] = field_name
        if field_value is not None:
    
        pass
    pass
            self.context['field_value'] = str(field_value)
        if validation_rule:
    
        pass
    pass
            self.context['validation_rule'] = validation_rule


class NetworkError(CLIException):
    pass
    """Network-related errors"""
    
    def __init__(self, message: str, host: Optional[str] = None,
                 port: Optional[int] = None, timeout: Optional[int] = None, **kwargs):
    pass
        super().__init__(message, **kwargs)
        self.host = host
        self.port = port
        self.timeout = timeout
        if host:
    
        pass
    pass
            self.context['host'] = host
        if port:
    
        pass
    pass
            self.context['port'] = port
        if timeout:
    
        pass
    pass
            self.context['timeout'] = timeout


class AuthenticationError(CLIException):
    pass
    """Authentication-related errors"""
    
    def __init__(self, message: str, auth_type: Optional[str] = None,
                 credential_type: Optional[str] = None, **kwargs):
    pass
        super().__init__(message, **kwargs)
        self.auth_type = auth_type
        self.credential_type = credential_type
        if auth_type:
    
        pass
    pass
            self.context['auth_type'] = auth_type
        if credential_type:
    
        pass
    pass
            self.context['credential_type'] = credential_type


class FilePermissionError(CLIException):
    pass
    """File permission-related errors"""
    
    def __init__(self, message: str, file_path: Optional[str] = None,
                 required_permission: Optional[str] = None, **kwargs):
    pass
        super().__init__(message, **kwargs)
        self.file_path = file_path
        self.required_permission = required_permission
        if file_path:
    
        pass
    pass
            self.context['file_path'] = file_path
        if required_permission:
    
        pass
    pass
            self.context['required_permission'] = required_permission


class DependencyError(CLIException):
    pass
    """Dependency-related errors"""
    
    def __init__(self, message: str, dependency_name: Optional[str] = None,
                 required_version: Optional[str] = None, **kwargs):
    pass
        super().__init__(message, **kwargs)
        self.dependency_name = dependency_name
        self.required_version = required_version
        if dependency_name:
    
        pass
    pass
            self.context['dependency_name'] = dependency_name
        if required_version:
    
        pass
    pass
            self.context['required_version'] = required_version


class ErrorRecoveryManager:
    pass
    """Manages error recovery procedures"""
    
    def __init__(self, workspace_path: Path):
    pass
        self.workspace_path = workspace_path
        self.recovery_log = []
    
    def create_config_backup(self, config_file: Path) -> Path:
    pass
        """Create a backup of configuration file"""
        if not config_file.exists():
    
        pass
    pass
            return None
        
        backup_dir = self.workspace_path / "backups" / "config"
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = backup_dir / f"{config_file.name}.backup_{timestamp}"
        
        backup_file.write_text(config_file.read_text())
        self.recovery_log.append(f"Created backup: {backup_file}")
        return backup_file
    
    def restore_config_backup(self, config_file: Path, backup_file: Path) -> bool:
    pass
        """Restore configuration from backup"""
        try:
    pass
            return True
        except Exception as e:
    pass
    pass
            return False
    
    def cleanup_stale_processes(self) -> List[int]:
    pass
        """Clean up stale bot processes"""
        cleaned_pids = []
        pid_files = list(self.workspace_path.glob("*.pid"))
        
        for pid_file in pid_files:
    pass
            try:
    pass
                pid = int(pid_file.read_text().strip())
                # Check if process exists
                try:
    
        pass
    pass
                    os.kill(pid, 0)  # Signal 0 just checks if process exists
                except OSError:
    
        pass
    pass
    pass
                    # Process doesn't exist, remove stale PID file
                    pid_file.unlink()
                    cleaned_pids.append(pid)
                    self.recovery_log.append(f"Removed stale PID file: {pid_file}")
            except (ValueError, FileNotFoundError):
    pass
    pass
                # Invalid PID file, remove it
                pid_file.unlink()
                self.recovery_log.append(f"Removed invalid PID file: {pid_file}")
        
        return cleaned_pids
    
    def repair_directory_structure(self) -> List[str]:
    pass
        """Repair missing directory structure"""
        required_dirs = [
            "config", "logs", "logs/errors", "logs/trades", "logs/metrics",
            "reports", "reports/compliance", "backups", "backups/config"
        ]
        
        created_dirs = []
        for dir_name in required_dirs:
    pass
            dir_path = self.workspace_path / dir_name
            if not dir_path.exists():
    
        pass
    pass
                dir_path.mkdir(parents=True, exist_ok=True)
                created_dirs.append(str(dir_path))
                self.recovery_log.append(f"Created directory: {dir_path}")
        
        return created_dirs
    
    def check_file_permissions(self, file_path: Path) -> Dict[str, bool]:
    pass
        """Check file permissions and suggest fixes"""
        permissions = {
            'readable': False,
            'writable': False,
            'executable': False
        }
        
        if file_path.exists():
    
        pass
    pass
            permissions['readable'] = os.access(file_path, os.R_OK)
            permissions['writable'] = os.access(file_path, os.W_OK)
            permissions['executable'] = os.access(file_path, os.X_OK)
        
        return permissions
    
    def fix_file_permissions(self, file_path: Path, mode: int = 0o644) -> bool:
    pass
        """Fix file permissions"""
        try:
    pass
            file_path.chmod(mode)
            self.recovery_log.append(f"Fixed permissions for: {file_path}")
            return True
        except Exception as e:
    pass
    pass
            self.recovery_log.append(f"Failed to fix permissions for {file_path}: {e}")
            return False


class CLIErrorHandler:
    pass
    """Centralized error handling for CLI operations"""
    
    def __init__(self, verbose: bool = False, workspace_path: Optional[Path] = None):
    pass
        self.verbose = verbose
        self.workspace_path = workspace_path or Path.cwd()
        self.recovery_manager = ErrorRecoveryManager(self.workspace_path)
        self.error_mappings = self._setup_error_mappings()
        self.error_history = []
        self.logger = logging.getLogger(__name__)
    
    def _setup_error_mappings(self) -> Dict[type, Dict[str, Any]]:
    pass
        """Setup comprehensive error type to user message mappings"""
        import builtins
        return {
            FileNotFoundError: {
                'suggestions': [
                    'Check if you are in the correct directory',
                    'Verify file permissions and path spelling'
                ],
                'recovery_actions': ['repair_directory_structure', 'create_default_config']
            },
            builtins.PermissionError: {
                'message': 'Permission denied accessing file or directory',
                'suggestions': [
                    'Check file permissions with "ls -la"',
                    'Run with appropriate user permissions',
                    'Ensure the directory is writable',
                    'Try running with sudo if necessary (use with caution)'
                ],
                'recovery_actions': ['fix_file_permissions', 'check_directory_ownership']
            },
            ConnectionError: {
                'message': 'Network connection failed',
                'suggestions': [
                    'Check your internet connection',
                    'Verify API endpoints are accessible',
                    'Check firewall and proxy settings',
                    'Try again in a few moments',
                    'Check if the service is experiencing downtime'
                ],
                'recovery_actions': ['test_network_connectivity', 'check_dns_resolution']
            },
            TimeoutError: {
                'message': 'Operation timed out',
                'suggestions': [
                    'Increase timeout value with --timeout parameter',
                    'Check network connectivity',
                    'Verify server responsiveness',
                    'Try during off-peak hours'
                ],
                'recovery_actions': ['retry_with_backoff']
            },
            subprocess.CalledProcessError: {
                'message': 'External command failed',
                'suggestions': [
                    'Check if required dependencies are installed',
                    'Verify command syntax and parameters',
                    'Check system PATH environment variable',
                    'Review error output for specific issues'
                ],
                'recovery_actions': ['check_dependencies', 'validate_environment']
            },
            ImportError: {
                'message': 'Required module not found',
                'suggestions': [
                    'Install missing dependencies with pip install -r requirements.txt',
                    'Check Python environment and virtual environment activation',
                    'Verify module installation with pip list',
                    'Check Python version compatibility'
                ],
                'recovery_actions': ['check_python_environment', 'install_dependencies']
            },
            json.JSONDecodeError: {
                'message': 'Invalid JSON format in configuration file',
                'suggestions': [
                    'Check JSON syntax in configuration files',
                    'Use a JSON validator to identify syntax errors',
                    'Restore from backup if available',
                    'Regenerate configuration with init-config command'
            KeyError: {
                'message': 'Required configuration key missing',
                'suggestions': [
                    'Check configuration file completeness',
                    'Compare with configuration template',
                    'Run configuration validation',
                    'Regenerate configuration if corrupted'
                ],
                'recovery_actions': ['validate_config_schema', 'merge_default_config']
            },
            ValueError: {
                'message': 'Invalid value provided',
                'suggestions': [
                    'Check input format and data types',
                    'Verify numeric values are within valid ranges',
                    'Check date/time format if applicable',
                    'Review command documentation for valid values'
                ],
                'recovery_actions': ['validate_input_format']
            },
            OSError: {
                'message': 'Operating system error',
                'suggestions': [
                    'Check available disk space',
                    'Verify file system permissions',
                    'Check if files are locked by other processes',
                    'Restart the application if necessary'
                ],
                'recovery_actions': ['check_disk_space', 'check_file_locks']
            },
            # CLI-specific exceptions
            ConfigurationError: {
                'message': 'Configuration error detected',
                'suggestions': [
                    'Check configuration file syntax and format',
                    'Validate required fields are present and correct',
                    'Run "genebot validate" to check all configurations',
                    'Compare with working configuration examples'
                ],
                'recovery_actions': ['validate_config_schema', 'restore_config_backup']
            },
            AccountError: {
                'message': 'Account management error',
                'suggestions': [
                    'Verify account credentials in .env file',
                    'Check account configuration in config/accounts.yaml',
                    'Run "genebot validate-accounts" to test connectivity',
                    'Ensure API keys have required permissions'
                ],
                'recovery_actions': ['validate_credentials', 'test_api_connectivity']
            },
            ProcessError: {
                'message': 'Process management error',
                'suggestions': [
                    'Check if bot is already running with "genebot status"',
                    'Verify system resources are available',
                    'Check process permissions and user access',
                    'Clean up stale processes if necessary'
                ],
                'recovery_actions': ['cleanup_stale_processes', 'check_system_resources']
            },
            DataError: {
                'message': 'Data access error',
                'suggestions': [
                    'Check database connectivity and credentials',
                    'Verify data files exist and are readable',
                    'Check log files for detailed error information',
                    'Ensure database schema is up to date'
                ],
                'recovery_actions': ['test_database_connection', 'check_data_integrity']
            },
            NetworkError: {
                'message': 'Network communication error',
                'suggestions': [
                    'Check internet connectivity',
                    'Verify API endpoint URLs and ports',
                    'Check firewall and proxy settings',
                    'Verify SSL/TLS certificate validity'
                ],
                'recovery_actions': ['test_network_connectivity', 'check_ssl_certificates']
            },
            AuthenticationError: {
                'message': 'Authentication failed',
                'suggestions': [
                    'Verify API credentials are correct and current',
                    'Check if API keys have expired',
                    'Ensure API keys have required permissions',
                    'Check for IP address restrictions'
                ],
                'recovery_actions': ['validate_credentials', 'check_api_permissions']
            },
            ValidationError: {
                'message': 'Validation error',
                'suggestions': [
                    'Check input data format and values',
                    'Verify all required fields are provided',
                    'Check data type constraints',
                    'Review validation rules and requirements'
                ],
                'recovery_actions': ['validate_input_schema']
            }
        }
    
    def handle_exception(self, exc: Exception, context: str = "", 
                        auto_recover: bool = False) -> CommandResult:
    pass
        """Handle an exception and return a user-friendly result"""
        exc_type = type(exc)
        
        # Log the error for debugging
        self._log_error(exc, context)
        
        # Check if it's a CLI exception with custom handling
        if isinstance(exc, CLIException):
    
        pass
    pass
    pass
            result = CommandResult.error(
                message=f"{context}: {exc.message}" if context else exc.message,
                error_code=exc.error_code,
                suggestions=exc.suggestions
            )
            
            # Add context information
            if exc.context:
    
        pass
    pass
                result.add_data('error_context', exc.context)
            
            # Attempt automatic recovery if enabled
            if auto_recover and exc.recovery_actions:
    
        pass
    pass
                recovery_results = self._attempt_recovery(exc.recovery_actions, exc.context)
                if recovery_results:
    
        pass
    pass
                    result.add_data('recovery_attempts', recovery_results)
                    if any(r['success'] for r in recovery_results):
    
        pass
    pass
                        result.add_suggestion("Some automatic recovery actions were successful. Try the command again.")
            
            return result
        
        # Check for mapped error types
        if exc_type in self.error_mappings:
    
        pass
    pass
            mapping = self.error_mappings[exc_type]
            message = f"{context}: {mapping['message']}" if context else mapping['message']
            
            # Add specific error details if available
            if str(exc):
    
        pass
    pass
                message += f" - {str(exc)}"
            
            result = CommandResult.error(
                message=message,
                suggestions=mapping['suggestions']
            )
            
            # Attempt automatic recovery if enabled
            if auto_recover and 'recovery_actions' in mapping:
    
        pass
    pass
                recovery_results = self._attempt_recovery(mapping['recovery_actions'])
                if recovery_results:
    
        pass
    pass
                    result.add_data('recovery_attempts', recovery_results)
                    if any(r['success'] for r in recovery_results):
    
        pass
    pass
                        result.add_suggestion("Some automatic recovery actions were successful. Try the command again.")
            
            return result
        
        # Generic error handling
        error_msg = f"Unexpected error: {str(exc)}"
        if context:
    
        pass
    pass
            error_msg = f"{context}: {error_msg}"
        
        suggestions = [
            'Check the logs for more details',
            'Try running the command with --verbose for more information',
            'Report this issue if it persists with steps to reproduce'
        ]
        
        # Add traceback in verbose mode
        if self.verbose:
    
        pass
    pass
            tb = traceback.format_exc()
            error_msg += f"\n\nTraceback:\n{tb}"
        
        return CommandResult.error(
            message=error_msg,
            suggestions=suggestions
        )
    
    def _log_error(self, exc: Exception, context: str = "") -> None:
    pass
        """Log error details for debugging"""
        error_entry = {
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'error_type': type(exc).__name__,
            'message': str(exc),
            'context': context,
            'traceback': traceback.format_exc()
        }
        
        self.error_history.append(error_entry)
        
        # Log to file if logger is configured
        if self.logger:
    
        pass
    pass
            self.logger.error(f"CLI Error [{context}]: {exc}", exc_info=True)
    
    def _attempt_recovery(self, recovery_actions: List[str], 
                         context: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    pass
        """Attempt automatic recovery actions"""
        results = []
        
        for action in recovery_actions:
    pass
            try:
    pass
                if hasattr(self, f'_recovery_{action}'):
    
        pass
    pass
                    recovery_method = getattr(self, f'_recovery_{action}')
                    success = recovery_method(context or {})
                    results.append({
                        'action': action,
                        'success': success,
                        'message': f"Recovery action '{action}' {'succeeded' if success else 'failed'}"
                    })
                elif hasattr(self.recovery_manager, action):
    
        pass
    pass
                    recovery_method = getattr(self.recovery_manager, action)
                    result = recovery_method()
                    success = bool(result)
                    results.append({
                        'action': action,
                        'success': success,
                        'message': f"Recovery action '{action}' {'succeeded' if success else 'failed'}",
                        'details': result
                    })
            except Exception as e:
    pass
    pass
                results.append({
                    'action': action,
                    'success': False,
                    'message': f"Recovery action '{action}' failed: {str(e)}"
                })
        
        return results
    
    def _recovery_test_network_connectivity(self, context: Dict[str, Any]) -> bool:
    pass
        """Test basic network connectivity"""
        try:
    pass
            import socket
            socket.create_connection(("8.8.8.8", 53), timeout=5)
            return True
        except Exception:
    pass
    pass
            return False
    
    def _recovery_check_dependencies(self, context: Dict[str, Any]) -> bool:
    pass
        """Check if required dependencies are available"""
        try:
    
        pass
    pass
            import pkg_resources
            requirements_file = self.workspace_path / "requirements.txt"
            if requirements_file.exists():
    
        pass
    pass
                requirements = requirements_file.read_text().strip().split('\n')
                for req in requirements:
    pass
                    if req.strip() and not req.strip().startswith('#'):
    
        pass
    pass
                        pkg_resources.require(req.strip())
            return True
        except Exception:
    pass
    pass
            return False
    
    def _recovery_validate_config_schema(self, context: Dict[str, Any]) -> bool:
    pass
        """Validate configuration schema"""
        try:
    pass
            # This would integrate with existing config validation
            from ..utils.config_manager import ConfigurationManager
            config_manager = ConfigurationManager()
            return config_manager.validate_all_configs()
        except Exception:
    pass
    pass
            return False
    
    def handle_validation_errors(self, errors: List[str], context: str = "", 
                               auto_recover: bool = False) -> CommandResult:
    pass
        """Handle multiple validation errors"""
        if not errors:
    
        pass
    pass
            return CommandResult.success("Validation passed")
        
        message = f"{context}: Found {len(errors)} validation error(s)" if context else f"Found {len(errors)} validation error(s)"
        
        # Add first few errors to message
        if len(errors) <= 3:
    
        pass
    pass
            message += ":\n" + "\n".join(f"  • {error}" for error in errors)
        else:
    pass
            message += ":\n" + "\n".join(f"  • {error}" for error in errors[:3])
            message += f"\n  • ... and {len(errors) - 3} more errors"
        
        suggestions = [
            'Fix the validation errors listed above',
            'Run "genebot validate" to check all configurations',
            'Check the documentation for configuration examples',
            'Use "genebot init-config" to regenerate configuration templates'
        ]
        
        result = CommandResult.error(
            message=message,
            suggestions=suggestions,
            error_code="VALIDATION_FAILED"
        )
        
        # Add detailed error information
        result.add_data('validation_errors', errors)
        result.add_data('error_count', len(errors))
        
        # Attempt automatic recovery if enabled
        if auto_recover:
    
        pass
    pass
            recovery_results = self._attempt_recovery(['validate_config_schema', 'repair_directory_structure'])
            if recovery_results:
    
        pass
    pass
                result.add_data('recovery_attempts', recovery_results)
                if any(r['success'] for r in recovery_results):
    
        pass
    pass
                    result.add_suggestion("Some automatic recovery actions were successful. Try validation again.")
        
        return result
    
    def create_error_report(self, include_history: bool = True) -> Dict[str, Any]:
    pass
        """Create a comprehensive error report"""
        report = {
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'workspace_path': str(self.workspace_path),
            'system_info': self._get_system_info(),
            'recovery_log': self.recovery_manager.recovery_log.copy()
        }
        
        if include_history:
    
        pass
    pass
            report['error_history'] = self.error_history.copy()
        
        return report
    
    def _get_system_info(self) -> Dict[str, Any]:
    pass
        """Get system information for error reporting"""
        import platform
        import sys
        
        return {
            'working_directory': str(Path.cwd()),
            'environment_variables': {
                k: v for k, v in os.environ.items() 
                if k.startswith(('GENEBOT_', 'PYTHONPATH', 'PATH'))
            }
        }
    
    def save_error_report(self, report_path: Optional[Path] = None) -> Path:
    pass
        """Save error report to file"""
        if report_path is None:
    
        pass
    pass
            logs_dir = self.workspace_path / "logs" / "errors"
            logs_dir.mkdir(parents=True, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            report_path = logs_dir / f"error_report_{timestamp}.json"
        
        report = self.create_error_report()
        report_path.write_text(json.dumps(report, indent=2, default=str))
        return report_path
    
    def format_result(self, result: CommandResult) -> str:
    pass
        """Format a command result for display"""
        lines = []
        
        # Status icon and message
        if result.status == ResultStatus.SUCCESS:
    
        pass
    pass
            lines.append(f"✅ {result.message}")
        elif result.status == ResultStatus.ERROR:
    
        pass
    pass
            lines.append(f"❌ {result.message}")
        elif result.status == ResultStatus.WARNING:
    
        pass
    pass
            lines.append(f"⚠️  {result.message}")
        elif result.status == ResultStatus.INFO:
    
        pass
    pass
            lines.append(f"ℹ️  {result.message}")
        
        # Add suggestions if available
        if result.suggestions:
    
        pass
    pass
            lines.append("")
            lines.append("💡 Suggestions:")
            for i, suggestion in enumerate(result.suggestions, 1):
    pass
                lines.append(f"  {i}. {suggestion}")
        
        # Add recovery information if available
        if result.data and 'recovery_attempts' in result.data:
    
        pass
    pass
            recovery_attempts = result.data['recovery_attempts']
            successful_recoveries = [r for r in recovery_attempts if r['success']]
            failed_recoveries = [r for r in recovery_attempts if not r['success']]
            
            if successful_recoveries:
    
        pass
    pass
                lines.append("")
                lines.append("🔧 Successful Recovery Actions:")
                for recovery in successful_recoveries:
    pass
                    lines.append(f"  ✅ {recovery['message']}")
            
            if failed_recoveries:
    
        pass
    pass
                lines.append("")
                lines.append("❌ Failed Recovery Actions:")
                for recovery in failed_recoveries:
    pass
                    lines.append(f"  ❌ {recovery['message']}")
        
        # Add error code if available
        if result.error_code:
    
        pass
    pass
            lines.append(f"\nError Code: {result.error_code}")
        
        # Add context information if available
        if result.data and 'error_context' in result.data:
    
        pass
    pass
            context = result.data['error_context']
            if context:
    
        pass
    pass
                lines.append(f"\nContext: {json.dumps(context, indent=2)}")
        
        return "\n".join(lines)
    
    def format_troubleshooting_guide(self, exc: Exception) -> str:
    pass
        """Generate a troubleshooting guide for specific error types"""
        exc_type = type(exc)
        
        guide_lines = [
            f"🔍 Troubleshooting Guide for {exc_type.__name__}",
            "=" * 50
        ]
        
        if exc_type in self.error_mappings:
    
        pass
    pass
            mapping = self.error_mappings[exc_type]
            
            guide_lines.extend([
                "",
                "📋 Quick Diagnosis Steps:",
            ])
            
            # Add diagnostic steps based on error type
            if exc_type == FileNotFoundError:
    
        pass
    pass
                guide_lines.extend([
                    "1. Check if you're in the correct directory",
                    "2. Verify the file path is spelled correctly",
                    "3. Check file permissions with 'ls -la'",
                    "4. Ensure the file hasn't been moved or deleted"
                ])
            elif exc_type == ConnectionError:
    
        pass
    pass
                guide_lines.extend([
                    "1. Test internet connectivity: ping google.com",
                    "2. Check if the service is online",
                    "3. Verify firewall settings",
                    "4. Check proxy configuration if applicable"
                ])
            elif exc_type == PermissionError:
    
        pass
    pass
                guide_lines.extend([
                    "1. Check file ownership: ls -la <file>",
                    "2. Verify user permissions",
                    "3. Check if file is locked by another process",
                    "4. Consider running with appropriate privileges"
                ])
            
            guide_lines.extend([
                "",
                "🛠️  Suggested Solutions:",
            ])
            
            for i, suggestion in enumerate(mapping['suggestions'], 1):
    pass
                guide_lines.append(f"{i}. {suggestion}")
            
            if 'recovery_actions' in mapping:
    
        pass
    pass
                guide_lines.extend([
                    "",
                    "🔄 Automatic Recovery Options:",
                    "Run the command with --auto-recover flag to attempt automatic fixes"
                ])
        
        guide_lines.extend([
            "",
            "📞 Need More Help?",
            "- Check the logs in logs/errors/ directory",
            "- Run with --verbose for detailed output",
            "- Create an error report with 'genebot error-report'",
            "- Consult the documentation or support channels"
        ])
        
        return "\n".join(guide_lines)
    
    def exit_with_error(self, result: CommandResult, show_troubleshooting: bool = False) -> None:
    pass
        """Print error and exit with appropriate code"""
        output = self.format_result(result)
        
        if show_troubleshooting and result.data and 'original_exception' in result.data:
    
        pass
    pass
    pass
            exc = result.data['original_exception']
            output += "\n\n" + self.format_troubleshooting_guide(exc)
        
        print(output, file=sys.stderr)
        
        # Save error report for debugging
        try:
    pass
    pass
            report_path = self.save_error_report()
            print(f"\n📄 Error report saved to: {report_path}", file=sys.stderr)
        except Exception:
    pass
    pass
            pass  # Don't fail on error report saving
        
        sys.exit(1 if not result.success else 0)
    
    def wrap_command_execution(self, command_func: Callable, *args, **kwargs) -> CommandResult:
    pass
        """Wrap command execution with comprehensive error handling"""
        try:
    pass
            return command_func(*args, **kwargs)
        except Exception as exc:
    pass
    pass
            # Add original exception to context for troubleshooting
            result = self.handle_exception(exc, context=f"Command: {command_func.__name__}")
            if result.data is None:
    
        pass
    pass
                result.data = {}
            result.data['original_exception'] = exc
            return result