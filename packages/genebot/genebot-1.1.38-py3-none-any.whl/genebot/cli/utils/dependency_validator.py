"""
Dependency Validation System
===========================

Comprehensive dependency validation for CLI commands to identify missing
components and provide installation guidance.
"""

import importlib
import logging
import platform
import subprocess
import sys
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from packaging import version

from .error_handler import ValidationError


class DependencyType(Enum):
    """Types of dependencies"""
    REQUIRED = "required"
    OPTIONAL = "optional"
    DATABASE = "database"
    LOGGING = "logging"
    ML = "ml"
    MONITORING = "monitoring"
    EXCHANGE = "exchange"


class DependencyStatus(Enum):
    """Status of dependency availability"""
    AVAILABLE = "available"
    MISSING = "missing"
    VERSION_MISMATCH = "version_mismatch"
    IMPORT_ERROR = "import_error"


@dataclass
class DependencyInfo:
    """Information about a dependency"""
    name: str
    type: DependencyType
    required: bool
    version_required: Optional[str] = None
    version_installed: Optional[str] = None
    status: DependencyStatus = DependencyStatus.MISSING
    import_path: Optional[str] = None
    installation_command: Optional[str] = None
    error_message: Optional[str] = None
    alternatives: List[str] = None
    
    def __post_init__(self):
        if self.alternatives is None:
            self.alternatives = []


@dataclass
class InstallationGuide:
    """Installation guide for missing dependencies"""
    missing_dependencies: List[DependencyInfo]
    platform_specific_commands: Dict[str, List[str]]
    pip_commands: List[str]
    conda_commands: List[str]
    additional_notes: List[str]
    
    def __post_init__(self):
        if self.platform_specific_commands is None:
            self.platform_specific_commands = {}
        if self.pip_commands is None:
            self.pip_commands = []
        if self.conda_commands is None:
            self.conda_commands = []
        if self.additional_notes is None:
            self.additional_notes = []


class DependencyValidator:
    """Comprehensive dependency validation system"""
    
    # Core dependency definitions
    DEPENDENCIES = {
        # Database components
        'sqlalchemy': DependencyInfo(
            name='SQLAlchemy',
            type=DependencyType.DATABASE,
            required=False,
            version_required='>=1.4.0',
            import_path='sqlalchemy',
            installation_command='pip install sqlalchemy>=1.4.0'
        ),
        'alembic': DependencyInfo(
            name='Alembic',
            type=DependencyType.DATABASE,
            required=False,
            import_path='alembic',
            installation_command='pip install alembic'
        ),
        'psycopg2': DependencyInfo(
            name='PostgreSQL Driver',
            type=DependencyType.DATABASE,
            required=False,
            import_path='psycopg2',
            installation_command='pip install psycopg2-binary',
            alternatives=['psycopg2-binary']
        ),
        'sqlite3': DependencyInfo(
            name='SQLite3',
            type=DependencyType.DATABASE,
            required=False,
            import_path='sqlite3',
            installation_command='Built-in Python module'
        ),
        
        # Trade logging components
        'trade_logger': DependencyInfo(
            name='Trade Logger',
            type=DependencyType.LOGGING,
            required=False,
            import_path='src.monitoring.trade_logger',
            installation_command='Part of genebot package'
        ),
        'monitoring_trade_logger': DependencyInfo(
            name='Monitoring Trade Logger',
            type=DependencyType.LOGGING,
            required=False,
            import_path='src.monitoring.trade_logger.TradeLogger',
            installation_command='Part of genebot package'
        ),
        
        # Machine Learning components
        'sklearn': DependencyInfo(
            name='scikit-learn',
            type=DependencyType.ML,
            required=False,
            version_required='>=1.3.0',
            import_path='sklearn',
            installation_command='pip install scikit-learn>=1.3.0'
        ),
        'tensorflow': DependencyInfo(
            name='TensorFlow',
            type=DependencyType.ML,
            required=False,
            version_required='>=2.13.0',
            import_path='tensorflow',
            installation_command='pip install tensorflow>=2.13.0'
        ),
        'torch': DependencyInfo(
            name='PyTorch',
            type=DependencyType.ML,
            required=False,
            version_required='>=2.0.0',
            import_path='torch',
            installation_command='pip install torch>=2.0.0'
        ),
        
        # Monitoring components
        'prometheus_client': DependencyInfo(
            name='Prometheus Client',
            type=DependencyType.MONITORING,
            required=False,
            import_path='prometheus_client',
            installation_command='pip install prometheus-client'
        ),
        'redis': DependencyInfo(
            name='Redis',
            type=DependencyType.MONITORING,
            required=False,
            version_required='>=4.5.0',
            import_path='redis',
            installation_command='pip install redis>=4.5.0'
        ),
        
        # Exchange/Trading components
        'ccxt': DependencyInfo(
            name='CCXT',
            type=DependencyType.EXCHANGE,
            required=False,
            version_required='>=4.0.0',
            import_path='ccxt',
            installation_command='pip install ccxt>=4.0.0'
        ),
        'mt5': DependencyInfo(
            name='MetaTrader 5',
            type=DependencyType.EXCHANGE,
            required=False,
            import_path='MetaTrader5',
            installation_command='pip install MetaTrader5'
        ),
        'oandapyV20': DependencyInfo(
            name='OANDA API',
            type=DependencyType.EXCHANGE,
            required=False,
            import_path='oandapyV20',
            installation_command='pip install oandapyV20'
        ),
        
        # Core required components
        'pandas': DependencyInfo(
            name='Pandas',
            type=DependencyType.REQUIRED,
            required=True,
            version_required='>=1.5.0',
            import_path='pandas',
            installation_command='pip install pandas>=1.5.0'
        ),
        'numpy': DependencyInfo(
            name='NumPy',
            type=DependencyType.REQUIRED,
            required=True,
            version_required='>=1.21.0',
            import_path='numpy',
            installation_command='pip install numpy>=1.21.0'
        ),
        'pyyaml': DependencyInfo(
            name='PyYAML',
            type=DependencyType.REQUIRED,
            required=True,
            import_path='yaml',
            installation_command='pip install PyYAML'
        ),
    }
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._dependency_cache: Dict[str, DependencyInfo] = {}
        self._platform = platform.system().lower()
    
    def check_database_components(self) -> Dict[str, DependencyInfo]:
        """Check availability of database components"""
        database_deps = {
            name: dep for name, dep in self.DEPENDENCIES.items()
            if dep.type == DependencyType.DATABASE
        }
        
        results = {}
        for name, dep_info in database_deps.items():
            results[name] = self._check_single_dependency(dep_info)
        
        # Check for database manager specifically
        db_manager_info = DependencyInfo(
            name='Database Manager',
            type=DependencyType.DATABASE,
            required=False,
            import_path='src.database.connection.DatabaseManager',
            installation_command='Part of genebot package'
        )
        results['database_manager'] = self._check_single_dependency(db_manager_info)
        
        # Check for database models
        db_models_info = DependencyInfo(
            name='Database Models',
            type=DependencyType.DATABASE,
            required=False,
            import_path='src.models.database_models',
            installation_command='Part of genebot package'
        )
        results['database_models'] = self._check_single_dependency(db_models_info)
        
        return results
    
    def check_trade_logger_components(self) -> Dict[str, DependencyInfo]:
        """Check availability of trade logger components"""
        trade_logger_deps = {
            name: dep for name, dep in self.DEPENDENCIES.items()
            if dep.type == DependencyType.LOGGING
        }
        
        results = {}
        for name, dep_info in trade_logger_deps.items():
            results[name] = self._check_single_dependency(dep_info)
        
        # Check specific trade logger class
        trade_logger_class_info = DependencyInfo(
            name='TradeLogger Class',
            type=DependencyType.LOGGING,
            required=False,
            import_path='src.monitoring.trade_logger.TradeLogger',
            installation_command='Part of genebot package'
        )
        results['trade_logger_class'] = self._check_single_dependency(trade_logger_class_info)
        
        return results
    
    def check_optional_dependencies(self) -> Dict[str, DependencyInfo]:
        """Check availability of optional dependencies (ML, monitoring, etc.)"""
        optional_deps = {
            name: dep for name, dep in self.DEPENDENCIES.items()
            if dep.type in [DependencyType.ML, DependencyType.MONITORING, DependencyType.EXCHANGE]
        }
        
        results = {}
        for name, dep_info in optional_deps.items():
            results[name] = self._check_single_dependency(dep_info)
        
        return results
    
    def check_all_dependencies(self) -> Dict[str, DependencyInfo]:
        """Check all dependencies"""
        results = {}
        
        # Check all defined dependencies
        for name, dep_info in self.DEPENDENCIES.items():
            results[name] = self._check_single_dependency(dep_info)
        
        # Add specific component checks
        db_results = self.check_database_components()
        trade_logger_results = self.check_trade_logger_components()
        
        # Merge results, avoiding duplicates
        for key, value in db_results.items():
            if key not in results:
                results[key] = value
        
        for key, value in trade_logger_results.items():
            if key not in results:
                results[key] = value
        
        return results
    
    def _check_single_dependency(self, dep_info: DependencyInfo) -> DependencyInfo:
        """Check a single dependency"""
        # Use cache if available
        cache_key = f"{dep_info.name}_{dep_info.import_path}"
        if cache_key in self._dependency_cache:
            return self._dependency_cache[cache_key]
        
        result = DependencyInfo(
            name=dep_info.name,
            type=dep_info.type,
            required=dep_info.required,
            version_required=dep_info.version_required,
            import_path=dep_info.import_path,
            installation_command=dep_info.installation_command,
            alternatives=dep_info.alternatives.copy() if dep_info.alternatives else []
        )
        
        try:
            if dep_info.import_path:
                # Try to import the module
                module = importlib.import_module(dep_info.import_path)
                result.status = DependencyStatus.AVAILABLE
                
                # Check version if required
                if dep_info.version_required and hasattr(module, '__version__'):
                    installed_version = module.__version__
                    result.version_installed = installed_version
                    
                    # Parse version requirement
                    if self._check_version_requirement(installed_version, dep_info.version_required):
                        result.status = DependencyStatus.AVAILABLE
                    else:
                        result.status = DependencyStatus.VERSION_MISMATCH
                        result.error_message = f"Version {installed_version} does not meet requirement {dep_info.version_required}"
                
        except ImportError as e:
            result.status = DependencyStatus.IMPORT_ERROR
            result.error_message = str(e)
            
            # Try alternatives if available
            if dep_info.alternatives:
                for alt in dep_info.alternatives:
                    try:
                        importlib.import_module(alt)
                        result.status = DependencyStatus.AVAILABLE
                        result.error_message = None
                        break
                    except ImportError:
                        continue
        
        except Exception as e:
            result.status = DependencyStatus.IMPORT_ERROR
            result.error_message = f"Unexpected error: {str(e)}"
        
        # Cache the result
        self._dependency_cache[cache_key] = result
        return result
    
    def _check_version_requirement(self, installed: str, required: str) -> bool:
        """Check if installed version meets requirement"""
        try:
            # Parse requirement (e.g., ">=1.4.0")
            if required.startswith('>='):
                min_version = required[2:].strip()
                return version.parse(installed) >= version.parse(min_version)
            elif required.startswith('>'):
                min_version = required[1:].strip()
                return version.parse(installed) > version.parse(min_version)
            elif required.startswith('<='):
                max_version = required[2:].strip()
                return version.parse(installed) <= version.parse(max_version)
            elif required.startswith('<'):
                max_version = required[1:].strip()
                return version.parse(installed) < version.parse(max_version)
            elif required.startswith('=='):
                exact_version = required[2:].strip()
                return version.parse(installed) == version.parse(exact_version)
            else:
                # Assume exact match
                return version.parse(installed) == version.parse(required)
        except Exception:
            # If version parsing fails, assume it's okay
            return True
    
    def generate_installation_guide(self, missing_deps: List[DependencyInfo]) -> InstallationGuide:
        """Generate installation guide for missing dependencies"""
        if not missing_deps:
            return InstallationGuide([], {}, [], [], [])
        
        pip_commands = []
        conda_commands = []
        platform_commands = {}
        notes = []
        
        # Group dependencies by type
        by_type = {}
        for dep in missing_deps:
            if dep.type not in by_type:
                by_type[dep.type] = []
            by_type[dep.type].append(dep)
        
        # Generate pip commands
        for dep in missing_deps:
            if dep.installation_command and dep.installation_command.startswith('pip install'):
                pip_commands.append(dep.installation_command)
            elif dep.installation_command and 'Part of genebot package' in dep.installation_command:
                notes.append(f"{dep.name} is part of the genebot package - ensure proper installation")
        
        # Generate conda commands (convert pip to conda where possible)
        conda_map = {
            'sqlalchemy': 'conda install sqlalchemy',
            'pandas': 'conda install pandas',
            'numpy': 'conda install numpy',
            'scikit-learn': 'conda install scikit-learn',
            'tensorflow': 'conda install tensorflow',
            'pytorch': 'conda install pytorch',
        }
        
        for dep in missing_deps:
            dep_name_lower = dep.name.lower().replace('-', '').replace(' ', '')
            if dep_name_lower in conda_map:
                conda_commands.append(conda_map[dep_name_lower])
        
        # Platform-specific commands
        if self._platform == 'darwin':  # macOS
            platform_commands['macOS'] = [
                'brew install postgresql',  # For psycopg2
                'brew install redis',       # For Redis
            ]
        elif self._platform == 'linux':
            platform_commands['Linux'] = [
                'sudo apt-get install postgresql-dev',  # For psycopg2
                'sudo apt-get install redis-server',    # For Redis
            ]
        elif self._platform == 'windows':
            platform_commands['Windows'] = [
                'Download PostgreSQL from https://www.postgresql.org/download/windows/',
                'Download Redis from https://github.com/microsoftarchive/redis/releases',
            ]
        
        # Add type-specific notes
        if DependencyType.DATABASE in by_type:
            notes.append("Database components are optional but required for persistent data storage")
            notes.append("Use 'genebot validate' to check database connectivity after installation")
        
        if DependencyType.ML in by_type:
            notes.append("Machine Learning components are optional and only needed for ML-based strategies")
            notes.append("Consider using conda for ML packages as they often have complex dependencies")
        
        if DependencyType.EXCHANGE in by_type:
            notes.append("Exchange adapters are optional and only needed for specific brokers/exchanges")
        
        # Add installation bundle suggestions
        if len(missing_deps) > 3:
            pip_commands.insert(0, "# Install all optional dependencies:")
            pip_commands.insert(1, "pip install genebot[all]")
            pip_commands.insert(2, "")
            pip_commands.insert(3, "# Or install specific feature sets:")
            
            if DependencyType.DATABASE in by_type:
                pip_commands.insert(4, "pip install genebot[database]")
            if DependencyType.ML in by_type:
                pip_commands.insert(5, "pip install genebot[ml]")
            if DependencyType.MONITORING in by_type:
                pip_commands.insert(6, "pip install genebot[monitoring]")
        
        return InstallationGuide(
            missing_dependencies=missing_deps,
            platform_specific_commands=platform_commands,
            pip_commands=pip_commands,
            conda_commands=conda_commands,
            additional_notes=notes
        )
    
    def get_missing_dependencies(self, dependency_results: Dict[str, DependencyInfo]) -> List[DependencyInfo]:
        """Get list of missing dependencies from results"""
        missing = []
        for dep_info in dependency_results.values():
            if dep_info.status in [DependencyStatus.MISSING, DependencyStatus.IMPORT_ERROR, DependencyStatus.VERSION_MISMATCH]:
                missing.append(dep_info)
        return missing
    
    def get_dependency_summary(self, dependency_results: Dict[str, DependencyInfo]) -> Dict[str, Any]:
        """Get summary of dependency check results"""
        total = len(dependency_results)
        available = sum(1 for dep in dependency_results.values() if dep.status == DependencyStatus.AVAILABLE)
        missing = sum(1 for dep in dependency_results.values() if dep.status == DependencyStatus.MISSING)
        version_issues = sum(1 for dep in dependency_results.values() if dep.status == DependencyStatus.VERSION_MISMATCH)
        import_errors = sum(1 for dep in dependency_results.values() if dep.status == DependencyStatus.IMPORT_ERROR)
        
        by_type = {}
        for dep in dependency_results.values():
            dep_type = dep.type.value
            if dep_type not in by_type:
                by_type[dep_type] = {'total': 0, 'available': 0, 'missing': 0}
            
            by_type[dep_type]['total'] += 1
            if dep.status == DependencyStatus.AVAILABLE:
                by_type[dep_type]['available'] += 1
            else:
                by_type[dep_type]['missing'] += 1
        
        return {
            'total_dependencies': total,
            'available': available,
            'missing': missing,
            'version_issues': version_issues,
            'import_errors': import_errors,
            'by_type': by_type,
            'health_score': (available / total * 100) if total > 0 else 0
        }
    
    def validate_command_dependencies(self, command_name: str, required_deps: List[str]) -> Tuple[bool, List[str]]:
        """Validate dependencies for a specific command"""
        missing_deps = []
        
        for dep_name in required_deps:
            if dep_name in self.DEPENDENCIES:
                dep_info = self._check_single_dependency(self.DEPENDENCIES[dep_name])
                if dep_info.status != DependencyStatus.AVAILABLE:
                    missing_deps.append(f"{dep_info.name}: {dep_info.error_message or 'Not available'}")
        
        return len(missing_deps) == 0, missing_deps
    
    def clear_cache(self):
        """Clear dependency check cache"""
        self._dependency_cache.clear()