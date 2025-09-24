"""
Dependency Checking Mixin
=========================

Standardized dependency checking patterns for CLI commands.
"""

from typing import List, Dict, Any, Optional
from ..result import CommandResult


class DependencyCheckMixin:
    """Mixin class providing standardized dependency checking methods"""
    
    def check_database_dependencies(self, required: bool = False) -> CommandResult:
        """Check database component dependencies"""
        try:
            from .dependency_validator import DependencyValidator
            validator = DependencyValidator()
            db_results = validator.check_database_components()
            
            missing_deps = validator.get_missing_dependencies(db_results)
            
            if missing_deps:
                if required:
                    # Database is required for this command
                    suggestions = [
                        "Install database support: pip install genebot[database]",
                        "Install SQLAlchemy: pip install sqlalchemy>=1.4.0",
                        "For PostgreSQL: pip install psycopg2-binary",
                        "Use 'genebot validate' to check all dependencies"
                    ]
                    
                    return CommandResult.error(
                        "Database components not available",
                        suggestions=suggestions
                    )
                else:
                    # Database is optional - provide warning
                    suggestions = [
                        "Database components not available - some features may be limited",
                        "Install database support: pip install genebot[database]",
                        "Data will not be persisted without database"
                    ]
                    
                    return CommandResult.warning(
                        "Database components not available - proceeding with limited functionality",
                        suggestions=suggestions
                    )
            
            return CommandResult.success("Database components available")
            
        except ImportError:
            # Dependency validator not available
            if required:
                return CommandResult.error(
                    "Database components not available",
                    suggestions=[
                        "Install database support: pip install genebot[database]",
                        "Ensure dependency validator is available"
                    ]
                )
            else:
                return CommandResult.warning(
                    "Cannot validate database dependencies - proceeding",
                    suggestions=["Install full genebot package for dependency validation"]
                )
    
    def check_trade_logger_dependencies(self, required: bool = False) -> CommandResult:
        """Check trade logger component dependencies"""
        try:
            from .dependency_validator import DependencyValidator
            validator = DependencyValidator()
            logger_results = validator.check_trade_logger_components()
            
            missing_deps = validator.get_missing_dependencies(logger_results)
            
            if missing_deps:
                if required:
                    suggestions = [
                        "Trade logger components not available",
                        "Ensure src.monitoring.trade_logger module is accessible",
                        "Install full genebot package: pip install genebot[all]",
                        "Check Python path includes src directory"
                    ]
                    
                    return CommandResult.error(
                        "Trade logger not available",
                        suggestions=suggestions
                    )
                else:
                    suggestions = [
                        "Trade logger not available - trade logging disabled",
                        "Install logging support for trade persistence",
                        "Some monitoring features may be limited"
                    ]
                    
                    return CommandResult.warning(
                        "Trade logger not available - proceeding without trade logging",
                        suggestions=suggestions
                    )
            
            return CommandResult.success("Trade logger components available")
            
        except ImportError:
            if required:
                return CommandResult.error(
                    "Trade logger not available",
                    suggestions=[
                        "Install full genebot package",
                        "Ensure monitoring modules are available"
                    ]
                )
            else:
                return CommandResult.warning(
                    "Cannot validate trade logger - proceeding",
                    suggestions=["Trade logging may not be available"]
                )
    
    def check_ml_dependencies(self, required: bool = False) -> CommandResult:
        """Check machine learning component dependencies"""
        try:
            from .dependency_validator import DependencyValidator
            validator = DependencyValidator()
            ml_results = validator.check_optional_dependencies()
            
            # Filter for ML dependencies
            ml_deps = {k: v for k, v in ml_results.items() 
                      if v.type.value == 'ml'}
            
            missing_deps = validator.get_missing_dependencies(ml_deps)
            
            if missing_deps:
                if required:
                    suggestions = [
                        "Install ML dependencies: pip install genebot[ml]",
                        "Install scikit-learn: pip install scikit-learn>=1.3.0",
                        "For deep learning: pip install tensorflow>=2.13.0",
                        "Or PyTorch: pip install torch>=2.0.0"
                    ]
                    
                    return CommandResult.error(
                        "Machine learning components not available",
                        suggestions=suggestions
                    )
                else:
                    suggestions = [
                        "ML components not available - ML strategies disabled",
                        "Install ML support: pip install genebot[ml]",
                        "Basic strategies will still work"
                    ]
                    
                    return CommandResult.warning(
                        "ML components not available - ML features disabled",
                        suggestions=suggestions
                    )
            
            return CommandResult.success("ML components available")
            
        except ImportError:
            if required:
                return CommandResult.error(
                    "ML components not available",
                    suggestions=["Install ML dependencies: pip install genebot[ml]"]
                )
            else:
                return CommandResult.warning(
                    "Cannot validate ML dependencies",
                    suggestions=["ML features may not be available"]
                )
    
    def check_monitoring_dependencies(self, required: bool = False) -> CommandResult:
        """Check monitoring component dependencies"""
        try:
            from .dependency_validator import DependencyValidator
            validator = DependencyValidator()
            monitoring_results = validator.check_optional_dependencies()
            
            # Filter for monitoring dependencies
            monitoring_deps = {k: v for k, v in monitoring_results.items() 
                             if v.type.value == 'monitoring'}
            
            missing_deps = validator.get_missing_dependencies(monitoring_deps)
            
            if missing_deps:
                if required:
                    suggestions = [
                        "Install monitoring dependencies: pip install genebot[monitoring]",
                        "Install Prometheus client: pip install prometheus-client",
                        "Install Redis: pip install redis>=4.5.0"
                    ]
                    
                    return CommandResult.error(
                        "Monitoring components not available",
                        suggestions=suggestions
                    )
                else:
                    suggestions = [
                        "Monitoring components not available - advanced monitoring disabled",
                        "Install monitoring support: pip install genebot[monitoring]",
                        "Basic monitoring will still work"
                    ]
                    
                    return CommandResult.warning(
                        "Monitoring components not available - limited monitoring",
                        suggestions=suggestions
                    )
            
            return CommandResult.success("Monitoring components available")
            
        except ImportError:
            if required:
                return CommandResult.error(
                    "Monitoring components not available",
                    suggestions=["Install monitoring dependencies: pip install genebot[monitoring]"]
                )
            else:
                return CommandResult.warning(
                    "Cannot validate monitoring dependencies",
                    suggestions=["Advanced monitoring may not be available"]
                )
    
    def check_exchange_dependencies(self, exchange_name: str, required: bool = False) -> CommandResult:
        """Check exchange-specific dependencies"""
        exchange_deps = {
            'ccxt': ['ccxt'],
            'mt5': ['MetaTrader5'],
            'oanda': ['oandapyV20'],
            'ib': ['ibapi']
        }
        
        if exchange_name.lower() not in exchange_deps:
            return CommandResult.warning(
                f"Unknown exchange: {exchange_name}",
                suggestions=["Supported exchanges: " + ", ".join(exchange_deps.keys())]
            )
        
        missing_modules = []
        for module_name in exchange_deps[exchange_name.lower()]:
            try:
                __import__(module_name)
            except ImportError:
                missing_modules.append(module_name)
        
        if missing_modules:
            if required:
                suggestions = [
                    f"Install {exchange_name} dependencies: pip install {' '.join(missing_modules)}",
                    f"Or install exchange support: pip install genebot[exchanges]"
                ]
                
                return CommandResult.error(
                    f"{exchange_name} exchange dependencies not available",
                    suggestions=suggestions
                )
            else:
                suggestions = [
                    f"{exchange_name} not available - exchange features disabled",
                    f"Install {exchange_name} support: pip install {' '.join(missing_modules)}"
                ]
                
                return CommandResult.warning(
                    f"{exchange_name} exchange not available",
                    suggestions=suggestions
                )
        
        return CommandResult.success(f"{exchange_name} exchange dependencies available")
    
    def validate_command_dependencies(self, dependencies: Dict[str, bool]) -> CommandResult:
        """Validate multiple dependencies for a command
        
        Args:
            dependencies: Dict mapping dependency type to required flag
                         e.g., {'database': True, 'trade_logger': False, 'ml': False}
        """
        errors = []
        warnings = []
        
        for dep_type, required in dependencies.items():
            if dep_type == 'database':
                result = self.check_database_dependencies(required)
            elif dep_type == 'trade_logger':
                result = self.check_trade_logger_dependencies(required)
            elif dep_type == 'ml':
                result = self.check_ml_dependencies(required)
            elif dep_type == 'monitoring':
                result = self.check_monitoring_dependencies(required)
            else:
                continue
            
            if not result.success and required:
                errors.append(result.message)
                if result.suggestions:
                    errors.extend(result.suggestions)
            elif result.status.value == 'warning':
                warnings.append(result.message)
                if result.suggestions:
                    warnings.extend(result.suggestions)
        
        if errors:
            return CommandResult.error(
                "Required dependencies not available",
                suggestions=errors
            )
        elif warnings:
            return CommandResult.warning(
                "Some optional dependencies not available",
                suggestions=warnings
            )
        else:
            return CommandResult.success("All dependencies available")