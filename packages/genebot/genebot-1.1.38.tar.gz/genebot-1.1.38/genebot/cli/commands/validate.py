"""
System Validation Commands
=========================

Commands for validating system dependencies and configuration.
"""

from argparse import Namespace
from typing import Dict, Any, List
import json

from ..result import CommandResult
from .base import BaseCommand


class ValidateSystemCommand(BaseCommand):
    """Validate all system dependencies and configuration"""
    
    def execute(self, args: Namespace) -> CommandResult:
        """Execute system validation command"""
        verbose = getattr(args, 'verbose', False)
        output_format = getattr(args, 'format', 'text')
        fix_suggestions = getattr(args, 'fix', False)
        
        self.logger.section("System Validation")
        
        try:
            # Run comprehensive validation
            validation_results = self._run_comprehensive_validation()
            
            # Display results
            if output_format == 'json':
                print(json.dumps(validation_results, indent=2, default=str))
                return CommandResult.success("Validation results displayed in JSON format")
            else:
                return self._display_validation_results(validation_results, verbose, fix_suggestions)
                
        except Exception as e:
            return CommandResult.error(
                f"System validation failed: {str(e)}",
                suggestions=[
                    "Check system permissions",
                    "Ensure genebot package is properly installed",
                    "Try running with --verbose for more details"
                ]
            )
    
    def _run_comprehensive_validation(self) -> Dict[str, Any]:
        """Run comprehensive system validation"""
        results = {
            'timestamp': self._get_timestamp(),
            'system_info': self._get_system_info(),
            'dependencies': {},
            'configuration': {},
            'summary': {}
        }
        
        # Check all dependency categories
        results['dependencies']['database'] = self._validate_database_dependencies()
        results['dependencies']['trade_logger'] = self._validate_trade_logger_dependencies()
        results['dependencies']['ml'] = self._validate_ml_dependencies()
        results['dependencies']['monitoring'] = self._validate_monitoring_dependencies()
        results['dependencies']['exchanges'] = self._validate_exchange_dependencies()
        
        # Check configuration
        results['configuration'] = self._validate_configuration()
        
        # Generate summary
        results['summary'] = self._generate_validation_summary(results)
        
        return results
    
    def _validate_database_dependencies(self) -> Dict[str, Any]:
        """Validate database dependencies"""
        result = self.check_database_dependencies(required=False)
        
        return {
            'status': result.status.value,
            'message': result.message,
            'suggestions': result.suggestions,
            'details': self._get_dependency_details('database')
        }
    
    def _validate_trade_logger_dependencies(self) -> Dict[str, Any]:
        """Validate trade logger dependencies"""
        result = self.check_trade_logger_dependencies(required=False)
        
        return {
            'status': result.status.value,
            'message': result.message,
            'suggestions': result.suggestions,
            'details': self._get_dependency_details('trade_logger')
        }
    
    def _validate_ml_dependencies(self) -> Dict[str, Any]:
        """Validate ML dependencies"""
        result = self.check_ml_dependencies(required=False)
        
        return {
            'status': result.status.value,
            'message': result.message,
            'suggestions': result.suggestions,
            'details': self._get_dependency_details('ml')
        }
    
    def _validate_monitoring_dependencies(self) -> Dict[str, Any]:
        """Validate monitoring dependencies"""
        result = self.check_monitoring_dependencies(required=False)
        
        return {
            'status': result.status.value,
            'message': result.message,
            'suggestions': result.suggestions,
            'details': self._get_dependency_details('monitoring')
        }
    
    def _validate_exchange_dependencies(self) -> Dict[str, Any]:
        """Validate exchange dependencies"""
        exchanges = ['ccxt', 'mt5', 'oanda', 'ib']
        exchange_results = {}
        
        for exchange in exchanges:
            result = self.check_exchange_dependencies(exchange, required=False)
            exchange_results[exchange] = {
                'status': result.status.value,
                'message': result.message,
                'suggestions': result.suggestions
            }
        
        return exchange_results
    
    def _validate_configuration(self) -> Dict[str, Any]:
        """Validate system configuration"""
        config_results = {
            'workspace': self._check_workspace_structure(),
            'config_files': self._check_config_files(),
            'permissions': self._check_permissions()
        }
        
        return config_results
    
    def _check_workspace_structure(self) -> Dict[str, Any]:
        """Check workspace directory structure"""
        required_dirs = ['config', 'logs']
        optional_dirs = ['reports', 'backups']
        
        workspace_path = self.context.workspace_path
        
        structure_status = {
            'workspace_path': str(workspace_path),
            'exists': workspace_path.exists(),
            'required_dirs': {},
            'optional_dirs': {}
        }
        
        for dir_name in required_dirs:
            dir_path = workspace_path / dir_name
            structure_status['required_dirs'][dir_name] = {
                'exists': dir_path.exists(),
                'writable': dir_path.exists() and dir_path.is_dir() and self._is_writable(dir_path)
            }
        
        for dir_name in optional_dirs:
            dir_path = workspace_path / dir_name
            structure_status['optional_dirs'][dir_name] = {
                'exists': dir_path.exists(),
                'writable': dir_path.exists() and dir_path.is_dir() and self._is_writable(dir_path)
            }
        
        return structure_status
    
    def _check_config_files(self) -> Dict[str, Any]:
        """Check configuration files"""
        config_files = [
            'accounts.yaml',
            'trading_bot_config.yaml',
            'logging_config.yaml'
        ]
        
        config_path = self.context.config_path
        file_status = {}
        
        for file_name in config_files:
            file_path = config_path / file_name
            file_status[file_name] = {
                'exists': file_path.exists(),
                'readable': file_path.exists() and self._is_readable(file_path),
                'size': file_path.stat().st_size if file_path.exists() else 0
            }
        
        return file_status
    
    def _check_permissions(self) -> Dict[str, Any]:
        """Check file and directory permissions"""
        workspace_path = self.context.workspace_path
        
        return {
            'workspace_readable': self._is_readable(workspace_path),
            'workspace_writable': self._is_writable(workspace_path),
            'config_readable': self._is_readable(self.context.config_path),
            'logs_writable': self._is_writable(workspace_path / 'logs')
        }
    
    def _get_dependency_details(self, dep_type: str) -> Dict[str, Any]:
        """Get detailed dependency information"""
        try:
            from ..utils.dependency_validator import DependencyValidator
            validator = DependencyValidator()
            
            if dep_type == 'database':
                results = validator.check_database_components()
            elif dep_type == 'trade_logger':
                results = validator.check_trade_logger_components()
            elif dep_type == 'ml':
                results = validator.check_optional_dependencies()
                results = {k: v for k, v in results.items() if v.type.value == 'ml'}
            elif dep_type == 'monitoring':
                results = validator.check_optional_dependencies()
                results = {k: v for k, v in results.items() if v.type.value == 'monitoring'}
            else:
                return {}
            
            details = {}
            for name, dep_info in results.items():
                details[name] = {
                    'name': dep_info.name,
                    'status': dep_info.status.value,
                    'version_installed': dep_info.version_installed,
                    'version_required': dep_info.version_required,
                    'error_message': dep_info.error_message,
                    'installation_command': dep_info.installation_command
                }
            
            return details
            
        except ImportError:
            return {'error': 'Dependency validator not available'}
    
    def _generate_validation_summary(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Generate validation summary"""
        total_checks = 0
        passed_checks = 0
        warnings = 0
        errors = 0
        
        # Count dependency checks
        for category, dep_result in results['dependencies'].items():
            if isinstance(dep_result, dict):
                if 'status' in dep_result:
                    total_checks += 1
                    if dep_result['status'] == 'success':
                        passed_checks += 1
                    elif dep_result['status'] == 'warning':
                        warnings += 1
                    else:
                        errors += 1
                else:
                    # Exchange dependencies have multiple sub-results
                    for exchange, exchange_result in dep_result.items():
                        total_checks += 1
                        if exchange_result['status'] == 'success':
                            passed_checks += 1
                        elif exchange_result['status'] == 'warning':
                            warnings += 1
                        else:
                            errors += 1
        
        # Count configuration checks
        config_results = results['configuration']
        workspace_checks = len(config_results['workspace']['required_dirs'])
        workspace_passed = sum(1 for dir_info in config_results['workspace']['required_dirs'].values() 
                              if dir_info['exists'])
        
        total_checks += workspace_checks
        passed_checks += workspace_passed
        
        health_score = (passed_checks / total_checks * 100) if total_checks > 0 else 0
        
        return {
            'total_checks': total_checks,
            'passed_checks': passed_checks,
            'warnings': warnings,
            'errors': errors,
            'health_score': health_score,
            'overall_status': self._determine_overall_status(health_score, errors)
        }
    
    def _determine_overall_status(self, health_score: float, errors: int) -> str:
        """Determine overall system status"""
        if errors > 0:
            return 'error'
        elif health_score >= 90:
            return 'excellent'
        elif health_score >= 75:
            return 'good'
        elif health_score >= 50:
            return 'fair'
        else:
            return 'poor'
    
    def _display_validation_results(self, results: Dict[str, Any], verbose: bool, fix_suggestions: bool) -> CommandResult:
        """Display validation results in formatted output"""
        summary = results['summary']
        
        # Display summary
        self.logger.subsection("Validation Summary")
        self.logger.list_item(f"Overall Status: {summary['overall_status'].title()}", "info")
        self.logger.list_item(f"Health Score: {summary['health_score']:.1f}%", "info")
        self.logger.list_item(f"Checks Passed: {summary['passed_checks']}/{summary['total_checks']}", "info")
        
        if summary['warnings'] > 0:
            self.logger.list_item(f"Warnings: {summary['warnings']}", "warning")
        
        if summary['errors'] > 0:
            self.logger.list_item(f"Errors: {summary['errors']}", "error")
        
        # Display dependency results
        self.logger.subsection("Dependency Validation")
        for category, dep_result in results['dependencies'].items():
            if isinstance(dep_result, dict) and 'status' in dep_result:
                status_icon = self._get_status_icon(dep_result['status'])
                self.logger.list_item(f"{status_icon} {category.title()}: {dep_result['message']}", "info")
                
                if verbose and dep_result.get('details'):
                    for name, details in dep_result['details'].items():
                        detail_icon = self._get_status_icon(details['status'])
                        self.logger.list_item(f"  {detail_icon} {details['name']}", "info", indent=1)
            else:
                # Exchange dependencies
                self.logger.list_item(f"Exchange Dependencies:", "info")
                for exchange, exchange_result in dep_result.items():
                    status_icon = self._get_status_icon(exchange_result['status'])
                    self.logger.list_item(f"  {status_icon} {exchange.upper()}: {exchange_result['message']}", "info", indent=1)
        
        # Display configuration results
        self.logger.subsection("Configuration Validation")
        config_results = results['configuration']
        
        workspace_status = config_results['workspace']
        workspace_icon = "🟢" if workspace_status['exists'] else "🔴"
        self.logger.list_item(f"{workspace_icon} Workspace: {workspace_status['workspace_path']}", "info")
        
        for dir_name, dir_info in workspace_status['required_dirs'].items():
            dir_icon = "🟢" if dir_info['exists'] and dir_info['writable'] else "🔴"
            self.logger.list_item(f"  {dir_icon} {dir_name}/ directory", "info", indent=1)
        
        # Display fix suggestions if requested
        if fix_suggestions:
            self._display_fix_suggestions(results)
        
        # Determine result status
        if summary['errors'] > 0:
            return CommandResult.error(
                f"System validation failed with {summary['errors']} errors",
                data=results
            )
        elif summary['warnings'] > 0:
            return CommandResult.warning(
                f"System validation completed with {summary['warnings']} warnings",
                data=results
            )
        else:
            return CommandResult.success(
                "System validation passed all checks",
                data=results
            )
    
    def _display_fix_suggestions(self, results: Dict[str, Any]) -> None:
        """Display fix suggestions for identified issues"""
        self.logger.subsection("Fix Suggestions")
        
        suggestions = []
        
        # Collect suggestions from dependency results
        for category, dep_result in results['dependencies'].items():
            if isinstance(dep_result, dict) and dep_result.get('suggestions'):
                suggestions.extend(dep_result['suggestions'])
            elif isinstance(dep_result, dict):
                # Exchange dependencies
                for exchange_result in dep_result.values():
                    if exchange_result.get('suggestions'):
                        suggestions.extend(exchange_result['suggestions'])
        
        # Add configuration suggestions
        config_results = results['configuration']
        workspace_status = config_results['workspace']
        
        if not workspace_status['exists']:
            suggestions.append("Create workspace directory structure")
        
        for dir_name, dir_info in workspace_status['required_dirs'].items():
            if not dir_info['exists']:
                suggestions.append(f"Create {dir_name}/ directory")
            elif not dir_info['writable']:
                suggestions.append(f"Fix permissions for {dir_name}/ directory")
        
        # Display unique suggestions
        unique_suggestions = list(set(suggestions))
        for i, suggestion in enumerate(unique_suggestions, 1):
            self.logger.list_item(f"{i}. {suggestion}", "info")
    
    def _get_status_icon(self, status: str) -> str:
        """Get status icon for display"""
        icons = {
            'success': '🟢',
            'warning': '🟡',
            'error': '🔴',
            'available': '🟢',
            'missing': '🔴',
            'import_error': '🔴'
        }
        return icons.get(status, '⚪')
    
    def _get_timestamp(self) -> str:
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().isoformat()
    
    def _get_system_info(self) -> Dict[str, Any]:
        """Get system information"""
        import platform
        import sys
        
        return {
            'platform': platform.platform(),
            'python_version': sys.version,
            'python_executable': sys.executable,
            'working_directory': str(self.context.workspace_path)
        }
    
    def _is_readable(self, path) -> bool:
        """Check if path is readable"""
        try:
            return path.exists() and path.is_file() and path.stat().st_mode & 0o444
        except:
            return False
    
    def _is_writable(self, path) -> bool:
        """Check if path is writable"""
        try:
            if path.exists():
                return path.stat().st_mode & 0o200
            else:
                # Check parent directory
                return path.parent.exists() and path.parent.stat().st_mode & 0o200
        except:
            return False


class ValidateDependenciesCommand(BaseCommand):
    """Validate specific dependency categories"""
    
    def execute(self, args: Namespace) -> CommandResult:
        """Execute dependency validation command"""
        category = getattr(args, 'category', 'all')
        verbose = getattr(args, 'verbose', False)
        
        self.logger.section(f"Dependency Validation: {category.title()}")
        
        try:
            if category == 'all':
                return self._validate_all_dependencies(verbose)
            elif category == 'database':
                return self._validate_single_category('database', verbose)
            elif category == 'trade_logger':
                return self._validate_single_category('trade_logger', verbose)
            elif category == 'ml':
                return self._validate_single_category('ml', verbose)
            elif category == 'monitoring':
                return self._validate_single_category('monitoring', verbose)
            elif category == 'exchanges':
                return self._validate_exchanges(verbose)
            else:
                return CommandResult.error(
                    f"Unknown dependency category: {category}",
                    suggestions=[
                        "Available categories: all, database, trade_logger, ml, monitoring, exchanges",
                        "Use 'genebot validate-dependencies --help' for more information"
                    ]
                )
                
        except Exception as e:
            return CommandResult.error(
                f"Dependency validation failed: {str(e)}",
                suggestions=[
                    "Check system permissions",
                    "Ensure genebot package is properly installed"
                ]
            )
    
    def _validate_all_dependencies(self, verbose: bool) -> CommandResult:
        """Validate all dependency categories"""
        categories = ['database', 'trade_logger', 'ml', 'monitoring']
        results = {}
        
        for category in categories:
            results[category] = self._get_category_result(category)
        
        # Also validate exchanges
        results['exchanges'] = self._get_exchanges_result()
        
        # Display results
        self._display_dependency_results(results, verbose)
        
        # Determine overall result
        errors = sum(1 for result in results.values() 
                    if isinstance(result, dict) and result.get('status') == 'error')
        warnings = sum(1 for result in results.values() 
                      if isinstance(result, dict) and result.get('status') == 'warning')
        
        if errors > 0:
            return CommandResult.error(
                f"Dependency validation failed with {errors} errors",
                data=results
            )
        elif warnings > 0:
            return CommandResult.warning(
                f"Dependency validation completed with {warnings} warnings",
                data=results
            )
        else:
            return CommandResult.success(
                "All dependencies validated successfully",
                data=results
            )
    
    def _validate_single_category(self, category: str, verbose: bool) -> CommandResult:
        """Validate a single dependency category"""
        if category == 'database':
            result = self.check_database_dependencies(required=False)
        elif category == 'trade_logger':
            result = self.check_trade_logger_dependencies(required=False)
        elif category == 'ml':
            result = self.check_ml_dependencies(required=False)
        elif category == 'monitoring':
            result = self.check_monitoring_dependencies(required=False)
        else:
            return CommandResult.error(f"Unknown category: {category}")
        
        # Display result
        status_icon = self._get_status_icon(result.status.value)
        self.logger.list_item(f"{status_icon} {category.title()}: {result.message}", "info")
        
        if verbose and result.suggestions:
            self.logger.subsection("Suggestions")
            for suggestion in result.suggestions:
                self.logger.list_item(suggestion, "info")
        
        return result
    
    def _validate_exchanges(self, verbose: bool) -> CommandResult:
        """Validate exchange dependencies"""
        exchanges = ['ccxt', 'mt5', 'oanda', 'ib']
        results = {}
        
        for exchange in exchanges:
            results[exchange] = self.check_exchange_dependencies(exchange, required=False)
        
        # Display results
        self.logger.subsection("Exchange Dependencies")
        for exchange, result in results.items():
            status_icon = self._get_status_icon(result.status.value)
            self.logger.list_item(f"{status_icon} {exchange.upper()}: {result.message}", "info")
            
            if verbose and result.suggestions:
                for suggestion in result.suggestions:
                    self.logger.list_item(f"  • {suggestion}", "info", indent=1)
        
        # Determine overall result
        available_count = sum(1 for result in results.values() if result.success)
        
        return CommandResult.success(
            f"Exchange validation completed - {available_count}/{len(exchanges)} exchanges available",
            data=results
        )
    
    def _get_category_result(self, category: str) -> Dict[str, Any]:
        """Get result for a dependency category"""
        if category == 'database':
            result = self.check_database_dependencies(required=False)
        elif category == 'trade_logger':
            result = self.check_trade_logger_dependencies(required=False)
        elif category == 'ml':
            result = self.check_ml_dependencies(required=False)
        elif category == 'monitoring':
            result = self.check_monitoring_dependencies(required=False)
        else:
            return {'status': 'error', 'message': f'Unknown category: {category}'}
        
        return {
            'status': result.status.value,
            'message': result.message,
            'suggestions': result.suggestions
        }
    
    def _get_exchanges_result(self) -> Dict[str, Any]:
        """Get result for exchange dependencies"""
        exchanges = ['ccxt', 'mt5', 'oanda', 'ib']
        exchange_results = {}
        
        for exchange in exchanges:
            result = self.check_exchange_dependencies(exchange, required=False)
            exchange_results[exchange] = {
                'status': result.status.value,
                'message': result.message,
                'suggestions': result.suggestions
            }
        
        return exchange_results
    
    def _display_dependency_results(self, results: Dict[str, Any], verbose: bool) -> None:
        """Display dependency validation results"""
        for category, result in results.items():
            if isinstance(result, dict) and 'status' in result:
                status_icon = self._get_status_icon(result['status'])
                self.logger.list_item(f"{status_icon} {category.title()}: {result['message']}", "info")
                
                if verbose and result.get('suggestions'):
                    for suggestion in result['suggestions']:
                        self.logger.list_item(f"  • {suggestion}", "info", indent=1)
            else:
                # Exchange results
                self.logger.subsection(f"{category.title()} Dependencies")
                for exchange, exchange_result in result.items():
                    status_icon = self._get_status_icon(exchange_result['status'])
                    self.logger.list_item(f"{status_icon} {exchange.upper()}: {exchange_result['message']}", "info")
                    
                    if verbose and exchange_result.get('suggestions'):
                        for suggestion in exchange_result['suggestions']:
                            self.logger.list_item(f"  • {suggestion}", "info", indent=1)