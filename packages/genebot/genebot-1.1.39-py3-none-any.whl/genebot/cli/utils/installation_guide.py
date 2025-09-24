"""
Installation Guide Generator
===========================

Generates comprehensive installation guides for missing dependencies
with platform-specific instructions and dependency resolution.
"""

import platform
import subprocess
import sys
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

from .dependency_validator import DependencyInfo, DependencyType, DependencyStatus


class PackageManager(Enum):
    """Available package managers"""
    PIP = "pip"
    CONDA = "conda"
    BREW = "brew"
    APT = "apt"
    YUM = "yum"
    PACMAN = "pacman"
    CHOCOLATEY = "choco"
    WINGET = "winget"


class Platform(Enum):
    """Supported platforms"""
    WINDOWS = "windows"
    MACOS = "macos"
    LINUX = "linux"
    UNKNOWN = "unknown"


@dataclass
class InstallationCommand:
    """Installation command for a specific package manager"""
    package_manager: PackageManager
    command: str
    description: str
    prerequisites: List[str] = None
    post_install_steps: List[str] = None
    
    def __post_init__(self):
        if self.prerequisites is None:
            self.prerequisites = []
        if self.post_install_steps is None:
            self.post_install_steps = []


@dataclass
class PlatformGuide:
    """Installation guide for a specific platform"""
    platform: Platform
    commands: List[InstallationCommand]
    system_requirements: List[str]
    troubleshooting_tips: List[str]
    
    def __post_init__(self):
        if self.system_requirements is None:
            self.system_requirements = []
        if self.troubleshooting_tips is None:
            self.troubleshooting_tips = []


class InstallationGuideGenerator:
    """Generates comprehensive installation guides"""
    
    # Package manager mappings for different dependencies
    PACKAGE_MAPPINGS = {
        # Database dependencies
        'sqlalchemy': {
            PackageManager.PIP: 'sqlalchemy>=1.4.0',
            PackageManager.CONDA: 'sqlalchemy',
        },
        'alembic': {
            PackageManager.PIP: 'alembic',
            PackageManager.CONDA: 'alembic',
        },
        'psycopg2': {
            PackageManager.PIP: 'psycopg2-binary',
            PackageManager.CONDA: 'psycopg2',
            PackageManager.APT: 'python3-psycopg2',
            PackageManager.YUM: 'python3-psycopg2',
        },
        
        # ML dependencies
        'sklearn': {
            PackageManager.PIP: 'scikit-learn>=1.3.0',
            PackageManager.CONDA: 'scikit-learn',
        },
        'tensorflow': {
            PackageManager.PIP: 'tensorflow>=2.13.0',
            PackageManager.CONDA: 'tensorflow',
        },
        'torch': {
            PackageManager.PIP: 'torch>=2.0.0',
            PackageManager.CONDA: 'pytorch',
        },
        
        # Exchange dependencies
        'ccxt': {
            PackageManager.PIP: 'ccxt>=4.0.0',
            PackageManager.CONDA: 'ccxt',
        },
        'mt5': {
            PackageManager.PIP: 'MetaTrader5',
        },
        'oandapyV20': {
            PackageManager.PIP: 'oandapyV20',
        },
        
        # Monitoring dependencies
        'prometheus_client': {
            PackageManager.PIP: 'prometheus-client',
            PackageManager.CONDA: 'prometheus_client',
        },
        'redis': {
            PackageManager.PIP: 'redis>=4.5.0',
            PackageManager.CONDA: 'redis-py',
            PackageManager.APT: 'redis-server',
            PackageManager.YUM: 'redis',
            PackageManager.BREW: 'redis',
        },
        
        # Core dependencies
        'pandas': {
            PackageManager.PIP: 'pandas>=1.5.0',
            PackageManager.CONDA: 'pandas',
        },
        'numpy': {
            PackageManager.PIP: 'numpy>=1.21.0',
            PackageManager.CONDA: 'numpy',
        },
        'pyyaml': {
            PackageManager.PIP: 'PyYAML',
            PackageManager.CONDA: 'pyyaml',
        },
    }
    
    # System package requirements for different platforms
    SYSTEM_REQUIREMENTS = {
        Platform.LINUX: {
            'psycopg2': ['postgresql-dev', 'libpq-dev'],
            'redis': ['redis-server'],
            'mt5': ['wine'],  # For MetaTrader 5 on Linux
        },
        Platform.MACOS: {
            'psycopg2': ['postgresql'],
            'redis': ['redis'],
        },
        Platform.WINDOWS: {
            'psycopg2': [],  # Usually works out of the box with psycopg2-binary
            'redis': [],     # Redis for Windows available as separate download
        }
    }
    
    def __init__(self):
        self.current_platform = self._detect_platform()
        self.available_package_managers = self._detect_package_managers()
    
    def _detect_platform(self) -> Platform:
        """Detect current platform"""
        system = platform.system().lower()
        if system == 'windows':
            return Platform.WINDOWS
        elif system == 'darwin':
            return Platform.MACOS
        elif system == 'linux':
            return Platform.LINUX
        else:
            return Platform.UNKNOWN
    
    def _detect_package_managers(self) -> Set[PackageManager]:
        """Detect available package managers"""
        available = set()
        
        # Always check for pip (should be available with Python)
        try:
            subprocess.run([sys.executable, '-m', 'pip', '--version'], 
                         capture_output=True, check=True)
            available.add(PackageManager.PIP)
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass
        
        # Check for conda
        try:
            subprocess.run(['conda', '--version'], capture_output=True, check=True)
            available.add(PackageManager.CONDA)
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass
        
        # Platform-specific package managers
        if self.current_platform == Platform.MACOS:
            try:
                subprocess.run(['brew', '--version'], capture_output=True, check=True)
                available.add(PackageManager.BREW)
            except (subprocess.CalledProcessError, FileNotFoundError):
                pass
        
        elif self.current_platform == Platform.LINUX:
            # Check for apt
            try:
                subprocess.run(['apt', '--version'], capture_output=True, check=True)
                available.add(PackageManager.APT)
            except (subprocess.CalledProcessError, FileNotFoundError):
                pass
            
            # Check for yum
            try:
                subprocess.run(['yum', '--version'], capture_output=True, check=True)
                available.add(PackageManager.YUM)
            except (subprocess.CalledProcessError, FileNotFoundError):
                pass
            
            # Check for pacman
            try:
                subprocess.run(['pacman', '--version'], capture_output=True, check=True)
                available.add(PackageManager.PACMAN)
            except (subprocess.CalledProcessError, FileNotFoundError):
                pass
        
        elif self.current_platform == Platform.WINDOWS:
            # Check for chocolatey
            try:
                subprocess.run(['choco', '--version'], capture_output=True, check=True)
                available.add(PackageManager.CHOCOLATEY)
            except (subprocess.CalledProcessError, FileNotFoundError):
                pass
            
            # Check for winget
            try:
                subprocess.run(['winget', '--version'], capture_output=True, check=True)
                available.add(PackageManager.WINGET)
            except (subprocess.CalledProcessError, FileNotFoundError):
                pass
        
        return available
    
    def generate_installation_commands(self, missing_deps: List[DependencyInfo]) -> List[InstallationCommand]:
        """Generate installation commands for missing dependencies"""
        commands = []
        
        # Group dependencies by type for better organization
        by_type = {}
        for dep in missing_deps:
            if dep.type not in by_type:
                by_type[dep.type] = []
            by_type[dep.type].append(dep)
        
        # Generate commands for each dependency type
        for dep_type, deps in by_type.items():
            commands.extend(self._generate_type_specific_commands(dep_type, deps))
        
        return commands
    
    def _generate_type_specific_commands(self, dep_type: DependencyType, deps: List[DependencyInfo]) -> List[InstallationCommand]:
        """Generate commands for a specific dependency type"""
        commands = []
        
        if dep_type == DependencyType.DATABASE:
            commands.extend(self._generate_database_commands(deps))
        elif dep_type == DependencyType.ML:
            commands.extend(self._generate_ml_commands(deps))
        elif dep_type == DependencyType.EXCHANGE:
            commands.extend(self._generate_exchange_commands(deps))
        elif dep_type == DependencyType.MONITORING:
            commands.extend(self._generate_monitoring_commands(deps))
        else:
            commands.extend(self._generate_generic_commands(deps))
        
        return commands
    
    def _generate_database_commands(self, deps: List[DependencyInfo]) -> List[InstallationCommand]:
        """Generate database-specific installation commands"""
        commands = []
        
        # System dependencies first
        if self.current_platform == Platform.LINUX and PackageManager.APT in self.available_package_managers:
            commands.append(InstallationCommand(
                package_manager=PackageManager.APT,
                command="sudo apt-get update && sudo apt-get install -y postgresql-dev libpq-dev",
                description="Install PostgreSQL development headers (required for psycopg2)",
                prerequisites=["sudo access"]
            ))
        elif self.current_platform == Platform.MACOS and PackageManager.BREW in self.available_package_managers:
            commands.append(InstallationCommand(
                package_manager=PackageManager.BREW,
                command="brew install postgresql",
                description="Install PostgreSQL (required for psycopg2)",
                prerequisites=["Homebrew installed"]
            ))
        
        # Python packages
        db_packages = []
        for dep in deps:
            dep_key = self._get_dependency_key(dep)
            if dep_key in self.PACKAGE_MAPPINGS:
                if PackageManager.PIP in self.PACKAGE_MAPPINGS[dep_key]:
                    db_packages.append(self.PACKAGE_MAPPINGS[dep_key][PackageManager.PIP])
        
        if db_packages and PackageManager.PIP in self.available_package_managers:
            commands.append(InstallationCommand(
                package_manager=PackageManager.PIP,
                command=f"pip install {' '.join(db_packages)}",
                description="Install database Python packages",
                post_install_steps=[
                    "Run 'genebot validate' to test database connectivity",
                    "Configure database connection in config.yaml"
                ]
            ))
        
        # Alternative: Install genebot with database extras
        if PackageManager.PIP in self.available_package_managers:
            commands.append(InstallationCommand(
                package_manager=PackageManager.PIP,
                command="pip install genebot[database]",
                description="Install genebot with all database dependencies",
                post_install_steps=[
                    "Configure database connection in config.yaml",
                    "Run database migrations if needed"
                ]
            ))
        
        return commands
    
    def _generate_ml_commands(self, deps: List[DependencyInfo]) -> List[InstallationCommand]:
        """Generate ML-specific installation commands"""
        commands = []
        
        # Recommend conda for ML packages
        if PackageManager.CONDA in self.available_package_managers:
            ml_packages = []
            for dep in deps:
                dep_key = self._get_dependency_key(dep)
                if dep_key in self.PACKAGE_MAPPINGS and PackageManager.CONDA in self.PACKAGE_MAPPINGS[dep_key]:
                    ml_packages.append(self.PACKAGE_MAPPINGS[dep_key][PackageManager.CONDA])
            
            if ml_packages:
                commands.append(InstallationCommand(
                    package_manager=PackageManager.CONDA,
                    command=f"conda install -c conda-forge {' '.join(ml_packages)}",
                    description="Install ML packages using conda (recommended for ML dependencies)",
                    prerequisites=["Anaconda or Miniconda installed"],
                    post_install_steps=[
                        "Verify installation with 'python -c \"import sklearn; print(sklearn.__version__)\"'",
                        "Consider creating a dedicated conda environment for ML work"
                    ]
                ))
        
        # Pip alternative
        if PackageManager.PIP in self.available_package_managers:
            ml_packages = []
            for dep in deps:
                dep_key = self._get_dependency_key(dep)
                if dep_key in self.PACKAGE_MAPPINGS and PackageManager.PIP in self.PACKAGE_MAPPINGS[dep_key]:
                    ml_packages.append(self.PACKAGE_MAPPINGS[dep_key][PackageManager.PIP])
            
            if ml_packages:
                commands.append(InstallationCommand(
                    package_manager=PackageManager.PIP,
                    command=f"pip install {' '.join(ml_packages)}",
                    description="Install ML packages using pip",
                    prerequisites=["Sufficient disk space (ML packages can be large)"],
                    post_install_steps=[
                        "Consider using virtual environment to avoid conflicts",
                        "Some packages may require additional system libraries"
                    ]
                ))
        
        # Bundle installation
        if PackageManager.PIP in self.available_package_managers:
            commands.append(InstallationCommand(
                package_manager=PackageManager.PIP,
                command="pip install genebot[ml]",
                description="Install genebot with all ML dependencies",
                post_install_steps=[
                    "Test ML functionality with example strategies",
                    "Check GPU support for TensorFlow/PyTorch if needed"
                ]
            ))
        
        return commands
    
    def _generate_exchange_commands(self, deps: List[DependencyInfo]) -> List[InstallationCommand]:
        """Generate exchange-specific installation commands"""
        commands = []
        
        exchange_packages = []
        for dep in deps:
            dep_key = self._get_dependency_key(dep)
            if dep_key in self.PACKAGE_MAPPINGS and PackageManager.PIP in self.PACKAGE_MAPPINGS[dep_key]:
                exchange_packages.append(self.PACKAGE_MAPPINGS[dep_key][PackageManager.PIP])
        
        if exchange_packages and PackageManager.PIP in self.available_package_managers:
            commands.append(InstallationCommand(
                package_manager=PackageManager.PIP,
                command=f"pip install {' '.join(exchange_packages)}",
                description="Install exchange/broker adapters",
                post_install_steps=[
                    "Configure API credentials for your exchanges",
                    "Test connectivity with 'genebot validate-accounts'",
                    "Review exchange-specific documentation"
                ]
            ))
        
        # Special handling for MetaTrader 5 on Linux
        if any(dep.name == 'MetaTrader 5' for dep in deps) and self.current_platform == Platform.LINUX:
            commands.append(InstallationCommand(
                package_manager=PackageManager.APT,
                command="sudo apt-get install wine",
                description="Install Wine (required for MetaTrader 5 on Linux)",
                prerequisites=["sudo access"],
                post_install_steps=[
                    "Configure Wine for MetaTrader 5",
                    "Install MetaTrader 5 terminal through Wine",
                    "Test connection with demo account first"
                ]
            ))
        
        return commands
    
    def _generate_monitoring_commands(self, deps: List[DependencyInfo]) -> List[InstallationCommand]:
        """Generate monitoring-specific installation commands"""
        commands = []
        
        # System services first (Redis)
        if any(dep.name == 'Redis' for dep in deps):
            if self.current_platform == Platform.LINUX and PackageManager.APT in self.available_package_managers:
                commands.append(InstallationCommand(
                    package_manager=PackageManager.APT,
                    command="sudo apt-get install redis-server",
                    description="Install Redis server",
                    prerequisites=["sudo access"],
                    post_install_steps=[
                        "sudo systemctl start redis-server",
                        "sudo systemctl enable redis-server",
                        "Test with 'redis-cli ping'"
                    ]
                ))
            elif self.current_platform == Platform.MACOS and PackageManager.BREW in self.available_package_managers:
                commands.append(InstallationCommand(
                    package_manager=PackageManager.BREW,
                    command="brew install redis",
                    description="Install Redis server",
                    post_install_steps=[
                        "brew services start redis",
                        "Test with 'redis-cli ping'"
                    ]
                ))
        
        # Python packages
        monitoring_packages = []
        for dep in deps:
            dep_key = self._get_dependency_key(dep)
            if dep_key in self.PACKAGE_MAPPINGS and PackageManager.PIP in self.PACKAGE_MAPPINGS[dep_key]:
                monitoring_packages.append(self.PACKAGE_MAPPINGS[dep_key][PackageManager.PIP])
        
        if monitoring_packages and PackageManager.PIP in self.available_package_managers:
            commands.append(InstallationCommand(
                package_manager=PackageManager.PIP,
                command=f"pip install {' '.join(monitoring_packages)}",
                description="Install monitoring Python packages",
                post_install_steps=[
                    "Configure monitoring endpoints in config.yaml",
                    "Test metrics collection with 'genebot monitor'"
                ]
            ))
        
        return commands
    
    def _generate_generic_commands(self, deps: List[DependencyInfo]) -> List[InstallationCommand]:
        """Generate generic installation commands"""
        commands = []
        
        packages = []
        for dep in deps:
            dep_key = self._get_dependency_key(dep)
            if dep_key in self.PACKAGE_MAPPINGS and PackageManager.PIP in self.PACKAGE_MAPPINGS[dep_key]:
                packages.append(self.PACKAGE_MAPPINGS[dep_key][PackageManager.PIP])
        
        if packages and PackageManager.PIP in self.available_package_managers:
            commands.append(InstallationCommand(
                package_manager=PackageManager.PIP,
                command=f"pip install {' '.join(packages)}",
                description="Install required packages",
                post_install_steps=["Verify installation with 'genebot validate'"]
            ))
        
        return commands
    
    def _get_dependency_key(self, dep: DependencyInfo) -> str:
        """Get dependency key for package mapping lookup"""
        # Map dependency names to package mapping keys
        name_mappings = {
            'SQLAlchemy': 'sqlalchemy',
            'Alembic': 'alembic',
            'PostgreSQL Driver': 'psycopg2',
            'scikit-learn': 'sklearn',
            'TensorFlow': 'tensorflow',
            'PyTorch': 'torch',
            'CCXT': 'ccxt',
            'MetaTrader 5': 'mt5',
            'OANDA API': 'oandapyV20',
            'Prometheus Client': 'prometheus_client',
            'Redis': 'redis',
            'Pandas': 'pandas',
            'NumPy': 'numpy',
            'PyYAML': 'pyyaml',
        }
        
        return name_mappings.get(dep.name, dep.name.lower().replace(' ', '').replace('-', ''))
    
    def generate_platform_guide(self, missing_deps: List[DependencyInfo]) -> PlatformGuide:
        """Generate comprehensive platform-specific installation guide"""
        commands = self.generate_installation_commands(missing_deps)
        
        # Platform-specific system requirements
        system_requirements = []
        if self.current_platform == Platform.LINUX:
            system_requirements.extend([
                "Ubuntu 18.04+ or equivalent Linux distribution",
                "Python 3.8+ with pip installed",
                "sudo access for system package installation",
                "Internet connection for package downloads"
            ])
        elif self.current_platform == Platform.MACOS:
            system_requirements.extend([
                "macOS 10.15+ (Catalina or later)",
                "Python 3.8+ (recommend using Homebrew)",
                "Xcode Command Line Tools",
                "Internet connection for package downloads"
            ])
        elif self.current_platform == Platform.WINDOWS:
            system_requirements.extend([
                "Windows 10 or later",
                "Python 3.8+ from python.org or Microsoft Store",
                "Administrator access may be required",
                "Internet connection for package downloads"
            ])
        
        # Platform-specific troubleshooting tips
        troubleshooting_tips = []
        if self.current_platform == Platform.LINUX:
            troubleshooting_tips.extend([
                "If pip install fails, try: python3 -m pip install --user <package>",
                "For permission errors, use virtual environments instead of sudo pip",
                "Install build-essential if compilation errors occur: sudo apt-get install build-essential",
                "Check Python version with: python3 --version"
            ])
        elif self.current_platform == Platform.MACOS:
            troubleshooting_tips.extend([
                "If pip install fails, ensure Xcode Command Line Tools are installed: xcode-select --install",
                "Use Homebrew Python instead of system Python: brew install python",
                "For M1 Macs, some packages may need Rosetta 2 or native ARM builds",
                "Check Python version with: python3 --version"
            ])
        elif self.current_platform == Platform.WINDOWS:
            troubleshooting_tips.extend([
                "Use Command Prompt or PowerShell as Administrator if needed",
                "If pip is not found, reinstall Python with 'Add to PATH' option",
                "For compilation errors, install Microsoft C++ Build Tools",
                "Use python -m pip instead of pip if command not found"
            ])
        
        return PlatformGuide(
            platform=self.current_platform,
            commands=commands,
            system_requirements=system_requirements,
            troubleshooting_tips=troubleshooting_tips
        )
    
    def generate_dependency_resolution_recommendations(self, missing_deps: List[DependencyInfo]) -> Dict[str, List[str]]:
        """Generate dependency resolution recommendations"""
        recommendations = {
            'installation_order': [],
            'conflict_resolution': [],
            'performance_tips': [],
            'security_considerations': []
        }
        
        # Installation order recommendations
        dep_types = [dep.type for dep in missing_deps]
        
        if DependencyType.REQUIRED in dep_types:
            recommendations['installation_order'].append("1. Install core required dependencies first (pandas, numpy, PyYAML)")
        
        if DependencyType.DATABASE in dep_types:
            recommendations['installation_order'].append("2. Install database dependencies (SQLAlchemy, drivers)")
        
        if DependencyType.EXCHANGE in dep_types:
            recommendations['installation_order'].append("3. Install exchange/broker adapters")
        
        if DependencyType.ML in dep_types:
            recommendations['installation_order'].append("4. Install ML dependencies last (largest packages)")
        
        # Conflict resolution
        if any(dep.name in ['TensorFlow', 'PyTorch'] for dep in missing_deps):
            recommendations['conflict_resolution'].append("TensorFlow and PyTorch may conflict - consider separate environments")
        
        if any(dep.name == 'PostgreSQL Driver' for dep in missing_deps):
            recommendations['conflict_resolution'].append("Use psycopg2-binary for easier installation, psycopg2 for production")
        
        # Performance tips
        if len(missing_deps) > 5:
            recommendations['performance_tips'].append("Consider using conda for complex dependency resolution")
            recommendations['performance_tips'].append("Use virtual environments to avoid system-wide conflicts")
        
        if any(dep.type == DependencyType.ML for dep in missing_deps):
            recommendations['performance_tips'].append("ML packages are large - ensure sufficient disk space and bandwidth")
        
        # Security considerations
        recommendations['security_considerations'].append("Always verify package sources and checksums")
        recommendations['security_considerations'].append("Use virtual environments to isolate dependencies")
        
        if any(dep.type == DependencyType.EXCHANGE for dep in missing_deps):
            recommendations['security_considerations'].append("Exchange adapters handle sensitive API keys - review security practices")
        
        return recommendations