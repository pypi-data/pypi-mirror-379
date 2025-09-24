"""
Minimal config validation utilities for GeneBot CLI
"""

from typing import List, Dict, Any
from pathlib import Path


class ConfigValidationResult:
    pass
    """Config validation result"""
    
    def __init__(self, is_valid: bool = True, errors: List[str] = None):
    pass
        self.is_valid = is_valid
        self.errors = errors or []
        self.warnings = []
        self.info = []
    
    def add_error(self, error: str):
    pass
        """Add validation error"""
        self.errors.append(error)
        self.is_valid = False
    
    def add_warning(self, warning: str):
    pass
        """Add validation warning"""
        self.warnings.append(warning)
    
    def add_info(self, info: str):
    pass
        """Add validation info"""
        self.info.append(info)
    
    def add_info(self, info: str):
    pass
        """Add validation info"""
        self.info.append(info)


class ConfigValidator:
    pass
    """Minimal config validator for CLI"""
    
    @staticmethod
    def validate_config(config: Dict[str, Any]) -> ConfigValidationResult:
    pass
        """Validate configuration dictionary"""
        result = ConfigValidationResult()
        
        # Basic validation - just check if it's a dict
        if not isinstance(config, dict):
    
        pass
    pass
            result.add_error("Configuration must be a dictionary")
        
        return result


def validate_config_file(config_file: str) -> ConfigValidationResult:
    pass
    """Validate configuration file"""
    result = ConfigValidationResult()
    
    config_path = Path(config_file)
    if not config_path.exists():
    
        pass
    pass
        result.add_warning(f"Configuration file {config_file} does not exist")
        return result
    
    try:
    pass
        import yaml
            config = yaml.safe_load(f)
        
        return ConfigValidator.validate_config(config)
    except Exception as e:
    pass
    pass
        result.add_error(f"Failed to load configuration file: {e}")
        return result