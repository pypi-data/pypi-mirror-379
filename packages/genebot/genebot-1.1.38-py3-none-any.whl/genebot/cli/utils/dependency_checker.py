"""
Dependency Checker Utility
==========================

Utility script for checking dependencies and generating installation guides.
This can be used by CLI commands to validate their dependencies.
"""

import logging
from typing import Dict, List, Optional, Tuple

from .dependency_validator import DependencyValidator, DependencyInfo, DependencyStatus
from .installation_guide import InstallationGuideGenerator, PlatformGuide


class DependencyChecker:
    """High-level dependency checker for CLI commands"""
    
    def __init__(self):
        self.validator = DependencyValidator()
        self.guide_generator = InstallationGuideGenerator()
        self.logger = logging.getLogger(__name__)
    
    def check_command_dependencies(self, command_name: str, required_components: List[str]) -> Tuple[bool, Dict[str, str]]:
        """
        Check dependencies for a specific command
        
        Args:
            command_name: Name of the command being checked
            required_components: List of required components (e.g., ['database', 'trade_logger'])
        
        Returns:
            Tuple of (all_available, error_messages)
        """
        error_messages = {}
        all_available = True
        
        for component in required_components:
            if component == 'database':
                db_results = self.validator.check_database_components()
                missing_db = self.validator.get_missing_dependencies(db_results)
                if missing_db:
                    all_available = False
                    error_messages['database'] = f"Database components not available: {', '.join([dep.name for dep in missing_db])}"
            
            elif component == 'trade_logger':
                logger_results = self.validator.check_trade_logger_components()
                missing_logger = self.validator.get_missing_dependencies(logger_results)
                if missing_logger:
                    all_available = False
                    error_messages['trade_logger'] = f"Trade logger not available: {', '.join([dep.name for dep in missing_logger])}"
            
            elif component == 'ml':
                ml_results = self.validator.check_optional_dependencies()
                ml_deps = {k: v for k, v in ml_results.items() if v.type.value == 'ml'}
                missing_ml = self.validator.get_missing_dependencies(ml_deps)
                if missing_ml:
                    all_available = False
                    error_messages['ml'] = f"ML components not available: {', '.join([dep.name for dep in missing_ml])}"
        
        return all_available, error_messages
    
    def get_installation_suggestions(self, missing_components: List[str]) -> List[str]:
        """Get installation suggestions for missing components"""
        suggestions = []
        
        if 'database' in missing_components:
            suggestions.extend([
                "Install database dependencies: pip install genebot[database]",
                "Or install individual packages: pip install sqlalchemy psycopg2-binary",
                "Configure database connection in config.yaml",
                "Run 'genebot validate' to test connectivity"
            ])
        
        if 'trade_logger' in missing_components:
            suggestions.extend([
                "Trade logger is part of genebot package",
                "Ensure genebot is properly installed: pip install --upgrade genebot",
                "Check if src/monitoring/trade_logger.py exists in your installation"
            ])
        
        if 'ml' in missing_components:
            suggestions.extend([
                "Install ML dependencies: pip install genebot[ml]",
                "Or install individual packages: pip install scikit-learn tensorflow",
                "Consider using conda for ML packages: conda install scikit-learn tensorflow",
                "ML components are optional - strategies will work without them"
            ])
        
        return suggestions
    
    def generate_comprehensive_report(self) -> Dict[str, any]:
        """Generate comprehensive dependency report"""
        # Check all dependencies
        all_results = self.validator.check_all_dependencies()
        missing_deps = self.validator.get_missing_dependencies(all_results)
        summary = self.validator.get_dependency_summary(all_results)
        
        # Generate installation guide
        installation_guide = None
        platform_guide = None
        if missing_deps:
            installation_guide = self.validator.generate_installation_guide(missing_deps)
            platform_guide = self.guide_generator.generate_platform_guide(missing_deps)
        
        return {
            'summary': summary,
            'all_dependencies': {name: {
                'name': dep.name,
                'type': dep.type.value,
                'status': dep.status.value,
                'required': dep.required,
                'version_installed': dep.version_installed,
                'version_required': dep.version_required,
                'error_message': dep.error_message
            } for name, dep in all_results.items()},
            'missing_dependencies': [{
                'name': dep.name,
                'type': dep.type.value,
                'installation_command': dep.installation_command,
                'error_message': dep.error_message
            } for dep in missing_deps],
            'installation_guide': {
                'pip_commands': installation_guide.pip_commands if installation_guide else [],
                'conda_commands': installation_guide.conda_commands if installation_guide else [],
                'additional_notes': installation_guide.additional_notes if installation_guide else []
            } if installation_guide else None,
            'platform_guide': {
                'platform': platform_guide.platform.value if platform_guide else None,
                'system_requirements': platform_guide.system_requirements if platform_guide else [],
                'troubleshooting_tips': platform_guide.troubleshooting_tips if platform_guide else []
            } if platform_guide else None
        }
    
    def validate_database_availability(self) -> Tuple[bool, List[str]]:
        """Validate database components availability"""
        db_results = self.validator.check_database_components()
        missing_db = self.validator.get_missing_dependencies(db_results)
        
        if not missing_db:
            return True, []
        
        suggestions = self.get_installation_suggestions(['database'])
        return False, suggestions
    
    def validate_trade_logger_availability(self) -> Tuple[bool, List[str]]:
        """Validate trade logger availability"""
        logger_results = self.validator.check_trade_logger_components()
        missing_logger = self.validator.get_missing_dependencies(logger_results)
        
        if not missing_logger:
            return True, []
        
        suggestions = self.get_installation_suggestions(['trade_logger'])
        return False, suggestions
    
    def validate_ml_availability(self) -> Tuple[bool, List[str]]:
        """Validate ML components availability"""
        all_results = self.validator.check_optional_dependencies()
        ml_deps = {k: v for k, v in all_results.items() if v.type.value == 'ml'}
        missing_ml = self.validator.get_missing_dependencies(ml_deps)
        
        if not missing_ml:
            return True, []
        
        suggestions = self.get_installation_suggestions(['ml'])
        return False, suggestions
    
    def get_dependency_status_message(self, component: str) -> str:
        """Get user-friendly status message for a component"""
        if component == 'database':
            available, suggestions = self.validate_database_availability()
            if available:
                return "Database components are available"
            else:
                return f"Database components not available. {suggestions[0] if suggestions else 'Install database dependencies.'}"
        
        elif component == 'trade_logger':
            available, suggestions = self.validate_trade_logger_availability()
            if available:
                return "Trade logger is available"
            else:
                return f"Trade logger not available. {suggestions[0] if suggestions else 'Ensure genebot is properly installed.'}"
        
        elif component == 'ml':
            available, suggestions = self.validate_ml_availability()
            if available:
                return "ML components are available"
            else:
                return f"ML components not available. {suggestions[0] if suggestions else 'Install ML dependencies.'}"
        
        else:
            return f"Unknown component: {component}"


# Convenience functions for common use cases
def check_database_components() -> Tuple[bool, List[str]]:
    """Quick check for database components"""
    checker = DependencyChecker()
    return checker.validate_database_availability()


def check_trade_logger_components() -> Tuple[bool, List[str]]:
    """Quick check for trade logger components"""
    checker = DependencyChecker()
    return checker.validate_trade_logger_availability()


def check_ml_components() -> Tuple[bool, List[str]]:
    """Quick check for ML components"""
    checker = DependencyChecker()
    return checker.validate_ml_availability()


def get_missing_dependency_suggestions(missing_components: List[str]) -> List[str]:
    """Get installation suggestions for missing components"""
    checker = DependencyChecker()
    return checker.get_installation_suggestions(missing_components)