"""
CLI Validation Utilities
========================

Input validation and configuration validation for CLI operations.
"""

import re
from pathlib import Path
from typing import Any, Dict, Union
from urllib.parse import urlparse

from .error_handler import ValidationError


class CLIValidator:
    pass
    """Comprehensive validation utilities for CLI operations"""
    
    # Common validation patterns
    PATTERNS = {
        'email': re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'),
        'api_key': re.compile(r'^[a-zA-Z0-9_-]{16,}$'),
        'account_name': re.compile(r'^[a-zA-Z0-9_-]{3,50}$'),
        'exchange_name': re.compile(r'^[a-zA-Z0-9_-]{2,20}$'),
        'symbol': re.compile(r'^[A-Z]{3,10}[/_-]?[A-Z]{3,10}$'),
        'percentage': re.compile(r'^\d+(\.\d+)?%?$'),
        'positive_number': re.compile(r'^\d+(\.\d+)?$'),
        'port': re.compile(r'^([1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$')
    }
    
    # Supported exchanges and brokers
    SUPPORTED_EXCHANGES = {
        'crypto': ['binance', 'coinbase', 'kraken', 'bitfinex', 'huobi', 'okx', 'bybit', 'kucoin'],
        'forex': ['oanda', 'ib', 'mt5', 'fxcm', 'pepperstone']
    }
    
    def __init__(self):
    pass
        self.errors = []
    
    def reset_errors(self) -> None:
    pass
        """Reset validation errors"""
        self.errors = []
    
    def add_error(self, error: str) -> None:
    pass
        """Add validation error"""
        self.errors.append(error)
    
    def has_errors(self) -> bool:
    pass
        """Check if there are validation errors"""
        return len(self.errors) > 0
    
    def get_errors(self) -> list[str]:
    
        pass
    pass
        """Get all validation errors"""
        return self.errors.copy()
    
    def validate_required_field(self, value: Any, field_name: str) -> bool:
    pass
        """Validate required field is present and not empty"""
        if value is None or (isinstance(value, str) and not value.strip()):
    
        pass
    pass
            self.add_error(f"Required field '{field_name}' is missing or empty")
            return False
        return True
    
    def validate_pattern(self, value: str, pattern_name: str, field_name: str) -> bool:
    pass
        """Validate value against a pattern"""
        if pattern_name not in self.PATTERNS:
    
        pass
    pass
            self.add_error(f"Unknown validation pattern: {pattern_name}")
            return False
        
        pattern = self.PATTERNS[pattern_name]
        if not pattern.match(value):
    
        pass
    pass
            self.add_error(f"Invalid format for '{field_name}': {value}")
            return False
        return True
    
    def validate_email(self, email: str, field_name: str = "email") -> bool:
    pass
        """Validate email address"""
        return self.validate_pattern(email, 'email', field_name)
    
    def validate_api_key(self, api_key: str, field_name: str = "API key") -> bool:
    pass
        """Validate API key format"""
        if not api_key or len(api_key) < 16:
    
        pass
    pass
            self.add_error(f"Invalid {field_name}: must be at least 16 characters")
            return False
        return True
    
    def validate_account_name(self, name: str) -> bool:
    pass
        """Validate account name"""
        return self.validate_pattern(name, 'account_name', 'account name')
    
    def validate_exchange_name(self, exchange: str, account_type: str = 'crypto') -> bool:
    pass
        """Validate exchange/broker name"""
        if account_type not in self.SUPPORTED_EXCHANGES:
    
        pass
    pass
            self.add_error(f"Unsupported account type: {account_type}")
            return False
        
        supported = self.SUPPORTED_EXCHANGES[account_type]
        if exchange.lower() not in supported:
    
        pass
    pass
            self.add_error(f"Unsupported {account_type} exchange: {exchange}")
            self.add_error(f"Supported exchanges: {', '.join(supported)}")
            return False
        return True
    
    def validate_percentage(self, value: Union[str, float], field_name: str, 
                          min_val: float = 0, max_val: float = 100) -> bool:
    pass
        """Validate percentage value"""
        try:
    pass
            # Convert string percentage to float
            if isinstance(value, str):
    
        pass
    pass
                if value.endswith('%'):
    
        pass
    pass
                    value = float(value[:-1])
                else:
    pass
                    value = float(value)
            
            if not min_val <= value <= max_val:
    
        pass
    pass
                self.add_error(f"{field_name} must be between {min_val}% and {max_val}%")
                return False
            return True
        except (ValueError, TypeError):
    pass
    pass
            self.add_error(f"Invalid percentage format for {field_name}: {value}")
            return False
    
    def validate_positive_number(self, value: Union[str, float], field_name: str) -> bool:
    pass
        """Validate positive number"""
        try:
    pass
            num_value = float(value)
            if num_value <= 0:
    
        pass
    pass
                self.add_error(f"{field_name} must be a positive number")
                return False
            return True
        except (ValueError, TypeError):
    pass
    pass
            self.add_error(f"Invalid number format for {field_name}: {value}")
            return False
    
    def validate_port(self, port: Union[str, int], field_name: str = "port") -> bool:
    pass
        """Validate port number"""
        try:
    pass
            port_num = int(port)
            if not 1 <= port_num <= 65535:
    
        pass
    pass
                self.add_error(f"{field_name} must be between 1 and 65535")
                return False
            return True
        except (ValueError, TypeError):
    pass
    pass
            self.add_error(f"Invalid port number: {port}")
            return False
    
    def validate_url(self, url: str, field_name: str = "URL") -> bool:
    pass
        """Validate URL format"""
        try:
    pass
            result = urlparse(url)
            if not all([result.scheme, result.netloc]):
    
        pass
    pass
                self.add_error(f"Invalid {field_name} format: {url}")
                return False
            return True
        except Exception:
    pass
    pass
            self.add_error(f"Invalid {field_name} format: {url}")
            return False
    
    def validate_file_path(self, path: Union[str, Path], field_name: str, 
                          must_exist: bool = False, must_be_writable: bool = False) -> bool:
    pass
        """Validate file path"""
        try:
    pass
            path_obj = Path(path)
            
            if must_exist and not path_obj.exists():
    
        pass
    pass
                self.add_error(f"{field_name} does not exist: {path}")
                return False
            
            if must_be_writable:
    
        pass
    pass
                # Check if parent directory is writable
                parent = path_obj.parent
                if not parent.exists():
    
        pass
    pass
                    self.add_error(f"Parent directory does not exist for {field_name}: {parent}")
                    return False
                if not parent.is_dir():
    
        pass
    pass
                    self.add_error(f"Parent path is not a directory for {field_name}: {parent}")
                    return False
            
            return True
        except Exception as e:
    pass
    pass
            self.add_error(f"Invalid path for {field_name}: {str(e)}")
            return False
    
    def validate_choice(self, value: str, choices: list[str], field_name: str) -> bool:
    pass
        """Validate value is in allowed choices"""
        if value not in choices:
    
        pass
    pass
            self.add_error(f"Invalid {field_name}: '{value}'. Must be one of: {', '.join(choices)}")
            return False
        return True
    
    def validate_account_config(self, config: Dict[str, Any], account_type: str) -> bool:
    pass
        """Validate account configuration"""
        valid = True
        
        # Common validations
        if not self.validate_required_field(config.get('name'), 'name'):
    
        pass
    pass
            valid = False
        
        if not self.validate_required_field(config.get('enabled'), 'enabled'):
    
        pass
    pass
            valid = False
        elif not isinstance(config['enabled'], bool):
    
        pass
    pass
            self.add_error("Field 'enabled' must be a boolean")
            valid = False
        
        # Type-specific validations
        if account_type == 'crypto':
    
        pass
    pass
            valid &= self._validate_crypto_config(config)
        elif account_type == 'forex':
    
        pass
    pass
            valid &= self._validate_forex_config(config)
        else:
    pass
            self.add_error(f"Unknown account type: {account_type}")
            valid = False
        
        return valid
    
    def _validate_crypto_config(self, config: Dict[str, Any]) -> bool:
    pass
        """Validate crypto account configuration"""
        valid = True
        
        exchange = config.get('exchange_type')
        if not self.validate_required_field(exchange, 'exchange_type'):
    
        pass
    pass
            valid = False
        elif not self.validate_exchange_name(exchange, 'crypto'):
    
        pass
    pass
            valid = False
        
        if not self.validate_required_field(config.get('api_key'), 'api_key'):
    
        pass
    pass
            valid = False
        
        if not self.validate_required_field(config.get('api_secret'), 'api_secret'):
    
        pass
    pass
            valid = False
        
        # Validate sandbox setting
        sandbox = config.get('sandbox')
        if sandbox is not None and not isinstance(sandbox, bool):
    
        pass
    pass
            self.add_error("Field 'sandbox' must be a boolean")
            valid = False
        
        return valid
    
    def _validate_forex_config(self, config: Dict[str, Any]) -> bool:
    pass
        """Validate forex account configuration"""
        valid = True
        
        broker = config.get('broker_type')
        if not self.validate_required_field(broker, 'broker_type'):
    
        pass
    pass
            valid = False
        elif not self.validate_exchange_name(broker, 'forex'):
    
        pass
    pass
            valid = False
        
        # Broker-specific validations
        if broker == 'oanda':
    
        pass
    pass
            valid &= self._validate_oanda_config(config)
        elif broker == 'ib':
    
        pass
    pass
            valid &= self._validate_ib_config(config)
        elif broker == 'mt5':
    
        pass
    pass
            valid &= self._validate_mt5_config(config)
        
        return valid
    
    def _validate_oanda_config(self, config: Dict[str, Any]) -> bool:
    pass
        """Validate OANDA configuration"""
        valid = True
        
        if not self.validate_required_field(config.get('api_key'), 'api_key'):
    
        pass
    pass
            valid = False
        
        if not self.validate_required_field(config.get('account_id'), 'account_id'):
    
        pass
    pass
            valid = False
        
        return valid
    
    def _validate_ib_config(self, config: Dict[str, Any]) -> bool:
    pass
        """Validate Interactive Brokers configuration"""
        valid = True
        
        host = config.get('host', 'localhost')
        if not self.validate_required_field(host, 'host'):
    
        pass
    pass
            valid = False
        
        port = config.get('port')
        if not self.validate_required_field(port, 'port'):
    
        pass
    pass
            valid = False
        elif not self.validate_port(port):
    
        pass
    pass
            valid = False
        
        client_id = config.get('client_id')
        if client_id is not None:
    
        pass
    pass
            try:
    pass
                int(client_id)
            except (ValueError, TypeError):
    pass
    pass
                self.add_error("Field 'client_id' must be an integer")
                valid = False
        
        return valid
    
    def _validate_mt5_config(self, config: Dict[str, Any]) -> bool:
    pass
        """Validate MetaTrader 5 configuration"""
        valid = True
        
        if not self.validate_required_field(config.get('login'), 'login'):
    
        pass
    pass
            valid = False
        
        if not self.validate_required_field(config.get('password'), 'password'):
    
        pass
    pass
            valid = False
        
        if not self.validate_required_field(config.get('server'), 'server'):
    
        pass
    pass
            valid = False
        
        return valid
    
    def validate_and_raise(self, context: str = "") -> None:
    pass
        """Validate and raise exception if errors found"""
        if self.has_errors():
    
        pass
    pass
    pass
            message = f"Validation failed"
            if context:
    
        pass
    pass
                message = f"{context}: {message}"
            
            raise ValidationError(
                message,
                suggestions=self.get_errors()
            )