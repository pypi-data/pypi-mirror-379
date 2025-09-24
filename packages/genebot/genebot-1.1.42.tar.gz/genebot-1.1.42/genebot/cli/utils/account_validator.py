"""
Real Account Validator
=====================

Validates trading accounts by testing actual API connectivity with exchanges and brokers.
Replaces mock validation with real API connection tests.
"""

import asyncio
import logging
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from decimal import Decimal
import yaml
from pathlib import Path

from .integration_manager import IntegrationManager

# Import existing exceptions through integration manager
try:
    pass
    pass
    from ..exceptions import ()
except ImportError:
    pass
    pass
    # Create minimal exception stubs
    class ConnectionException(Exception):
    pass
    pass
    class AuthenticationException(Exception):
    pass
    class ExchangeException(Exception):
    pass
@dataclass
class AccountStatus:
    pass
    """Account status information from real API validation"""
    name: str
    type: str  # 'crypto' or 'forex'
    exchange_or_broker: str
    enabled: bool
    connected: bool
    authenticated: bool
    last_check: datetime
    error_message: Optional[str] = None
    balance: Optional[Dict[str, Decimal]] = None
    latency_ms: Optional[float] = None
    additional_info: Optional[Dict[str, Any]] = None


class RealAccountValidator:
    pass
    """
    Real account validator that uses existing exchange adapters to test API connectivity.
    
    This class replaces mock account validation with actual API connection tests
    for both crypto exchanges and forex brokers.
    """
    
    def __init__(self, config_path: Optional[Path] = None):
    pass
        """
        Initialize the real account validator.
        
        Args:
    pass
            config_path: Path to configuration directory (defaults to config/)
        """
        self.logger = logging.getLogger(__name__)
        self.config_path = config_path or Path("config")
        self.accounts_file = self.config_path / "accounts.yaml"
        
        # Initialize integration manager for accessing existing components
        self.integration_manager = IntegrationManager(
            config_path=self.config_path,
            env_file=Path(".env")
        )
        
        # Cache for loaded accounts
        self._accounts_cache = None
        self._cache_timestamp = None
    
    def _load_accounts_config(self) -> Dict[str, Any]:
    pass
        """
        Load accounts configuration from YAML file.
        
        Returns:
    pass
            Dictionary containing crypto_exchanges and forex_brokers configurations
            
        Raises:
    pass
            FileNotFoundError: If accounts.yaml doesn't exist
            yaml.YAMLError: If YAML parsing fails
        """
        try:
    pass
            if not self.accounts_file.exists():
    
        pass
    pass
                raise FileNotFoundError(f"Accounts configuration not found: {self.accounts_file}")
            
            # Check if we need to reload cache
            file_mtime = self.accounts_file.stat().st_mtime
            if (self._accounts_cache is None or 
                self._cache_timestamp is None or 
                file_mtime > self._cache_timestamp):
    
        pass
    pass
                with open(self.accounts_file, 'r') as f:
    pass
                    self._accounts_cache = yaml.safe_load(f) or {}
                self._cache_timestamp = file_mtime
                self.logger.debug(f"Loaded accounts configuration from {self.accounts_file}")
            
            return self._accounts_cache
            
        except yaml.YAMLError as e:
    pass
    pass
            raise
        except Exception as e:
    pass
    pass
            self.logger.error(f"Failed to load accounts configuration: {e}")
            raise
    
    def get_all_accounts(self) -> List[Dict[str, Any]]:
    pass
        """
        Get all configured accounts (both crypto and forex).
        
        Returns:
    pass
            List of account configurations with type information
        """
        try:
    pass
            config = self._load_accounts_config()
            accounts = []
            
            # Add crypto exchanges
            crypto_exchanges = config.get('crypto_exchanges', {})
            for name, account_config in crypto_exchanges.items():
    pass
                account_config = dict(account_config)  # Make a copy
                account_config['name'] = name
                account_config['type'] = 'crypto'
                accounts.append(account_config)
            
            # Add forex brokers
            forex_brokers = config.get('forex_brokers', {})
            for name, account_config in forex_brokers.items():
    pass
                account_config = dict(account_config)  # Make a copy
                account_config['name'] = name
                account_config['type'] = 'forex'
                accounts.append(account_config)
            
            return accounts
            
        except Exception as e:
    pass
    pass
            self.logger.error(f"Failed to get all accounts: {e}")
            return []
    
    def get_account_by_name(self, name: str) -> Optional[Dict[str, Any]]:
    pass
        """
        Get specific account configuration by name.
        
        Args:
    
        pass
    pass
            name: Account name to search for
            
        Returns:
    pass
            Account configuration dictionary or None if not found
        """
        accounts = self.get_all_accounts()
        for account in accounts:
    
        pass
    pass
            if account.get('name') == name:
    
        pass
    pass
                return account
        return None
    
    def filter_accounts(self, accounts: List[Dict[str, Any]], 
                       account_type: Optional[str] = None,
                       enabled_only: bool = False) -> List[Dict[str, Any]]:
    pass
        """
        Filter accounts by type and enabled status.
        
        Args:
    pass
            accounts: List of account configurations
            account_type: Filter by type ('crypto' or 'forex'), None for all
            enabled_only: If True, only return enabled accounts
            
        Returns:
    pass
            Filtered list of accounts
        """
        filtered = accounts
        
        if account_type:
    
        pass
    pass
            filtered = [acc for acc in filtered if acc.get('type') == account_type]
        
        if enabled_only:
    
        pass
    pass
            filtered = [acc for acc in filtered if acc.get('enabled', False)]
        
        return filtered
    
    async def _create_crypto_adapter(self, account_config: Dict[str, Any]):
    pass
        """
        Create a crypto exchange adapter from account configuration using integration manager.
        
        Args:
    pass
            account_config: Account configuration dictionary
            
        Returns:
    pass
            Initialized exchange adapter
            
        Raises:
    pass
            ValueError: If exchange type is not supported
            ImportError: If required modules are not available
        """
        exchange_name = account_config.get('name')
        if not exchange_name:
    
        pass
    pass
            raise ValueError("Missing account name in configuration")
        
        # Use integration manager to get exchange adapter
        return self.integration_manager.get_exchange_adapter(exchange_name)
    
    async def _create_forex_adapter(self, account_config: Dict[str, Any]):
    pass
        """
        Create a forex broker adapter from account configuration using integration manager.
        
        Args:
    pass
            account_config: Account configuration dictionary
            
        Returns:
    pass
            Initialized broker adapter
            
        Raises:
    pass
            ValueError: If broker type is not supported
            ImportError: If required modules are not available
        """
        broker_name = account_config.get('name')
        if not broker_name:
    
        pass
    pass
            raise ValueError("Missing account name in configuration")
        
        # Use integration manager to get broker adapter
        return self.integration_manager.get_exchange_adapter(broker_name)
    
    async def validate_single_account(self, account_config: Dict[str, Any], 
                                    timeout: int = 30) -> AccountStatus:
    pass
        """
        Validate a single account by testing API connectivity.
        
        Args:
    pass
            account_config: Account configuration dictionary
            timeout: Connection timeout in seconds
            
        Returns:
    pass
            AccountStatus with validation results
        """
        account_name = account_config.get('name', 'unknown')
        account_type = account_config.get('type', 'unknown')
        
        start_time = datetime.now()
        
        try:
    pass
            # Create appropriate adapter based on account type
            if account_type == 'crypto':
    
        pass
    pass
                adapter = await self._create_crypto_adapter(account_config)
                exchange_or_broker = account_config.get('exchange_type', 'unknown')
            elif account_type == 'forex':
    
        pass
    pass
                adapter = await self._create_forex_adapter(account_config)
                exchange_or_broker = account_config.get('broker_type', 'unknown')
            else:
    pass
                return AccountStatus(
                    name=account_name,
                    type=account_type,
                    exchange_or_broker='unknown',
                    enabled=account_config.get('enabled', False),
                    connected=False,
                    authenticated=False,
                    last_check=datetime.now(timezone.utc),
                    error_message=f"Unknown account type: {account_type}"
                )
            
            # Test connection
            connected = False
            authenticated = False
            balance = None
            error_message = None
            additional_info = None
            
            try:
    pass
                # Test basic connection
                connected = await asyncio.wait_for(adapter.connect(), timeout=timeout)
                
                if connected:
    
        pass
    pass
                    # Test authentication
                    authenticated = await asyncio.wait_for(adapter.authenticate(), timeout=timeout)
                    
                    if authenticated:
    
        pass
    pass
                        # Get additional account information
                        try:
    pass
                            balance = await asyncio.wait_for(adapter.get_balance(), timeout=timeout)
                        except Exception as e:
    pass
    pass
                            self.logger.warning(f"Failed to get balance for {account_name}: {e}")
                        
                        try:
    pass
                            health_info = await asyncio.wait_for(adapter.health_check(), timeout=timeout)
                            additional_info = health_info
                        except Exception as e:
    pass
    pass
                            self.logger.warning(f"Failed to get health info for {account_name}: {e}")
                
            except asyncio.TimeoutError:
    pass
    pass
                error_message = f"Connection timeout after {timeout} seconds - check network connectivity"
            except ConnectionException as e:
    pass
    pass
                error_message = f"Connection failed: {str(e)} - verify network settings and exchange status"
            except AuthenticationException as e:
    
        pass
    pass
    pass
                error_message = f"Authentication failed: {str(e)} - check API credentials and permissions"
                connected = True  # Connection worked, but auth failed
            except ImportError as e:
    pass
    pass
                error_message = f"Missing dependencies: {str(e)} - install required packages"
            except ValueError as e:
    pass
    pass
                error_message = f"Configuration error: {str(e)} - check account configuration"
            except Exception as e:
    pass
    pass
                # Categorize common error types
                error_str = str(e).lower()
                if 'network' in error_str or 'connection' in error_str:
    
        pass
    pass
                    error_message = f"Network error: {str(e)} - check internet connection and firewall"
                elif 'api' in error_str or 'key' in error_str or 'auth' in error_str:
    
        pass
    pass
                    error_message = f"API error: {str(e)} - verify API credentials and permissions"
                elif 'timeout' in error_str:
    
        pass
    pass
                    error_message = f"Request timeout: {str(e)} - try increasing timeout or check server status"
                elif 'rate' in error_str or 'limit' in error_str:
    
        pass
    pass
                    error_message = f"Rate limit error: {str(e)} - reduce request frequency"
                else:
    pass
                    error_message = f"Validation failed: {str(e)}"
            
            finally:
    pass
                # Always disconnect
                try:
    pass
                    await adapter.disconnect()
                except Exception as e:
    pass
    pass
                    self.logger.warning(f"Error disconnecting from {account_name}: {e}")
            
            # Calculate latency
            end_time = datetime.now()
            latency_ms = (end_time - start_time).total_seconds() * 1000
            
            return AccountStatus(
                name=account_name,
                type=account_type,
                exchange_or_broker=exchange_or_broker,
                enabled=account_config.get('enabled', False),
                connected=connected,
                authenticated=authenticated,
                last_check=datetime.now(timezone.utc),
                error_message=error_message,
                balance=balance,
                latency_ms=round(latency_ms, 2),
                additional_info=additional_info
            )
            
        except Exception as e:
    pass
    pass
            self.logger.error(f"Failed to validate account {account_name}: {e}")
            return AccountStatus(
                name=account_name,
                type=account_type,
                exchange_or_broker=account_config.get('exchange_type', 
                                                   account_config.get('broker_type', 'unknown')),
                enabled=account_config.get('enabled', False),
                connected=False,
                authenticated=False,
                last_check=datetime.now(timezone.utc),
                error_message=f"Validation error: {str(e)}"
            )
    
    async def validate_all_accounts(self, account_filter: Optional[str] = None,
                                  account_type: Optional[str] = None,
                                  enabled_only: bool = False,
                                  timeout: int = 30) -> List[AccountStatus]:
    pass
        """
        Validate all configured accounts or a filtered subset.
        
        Args:
    pass
            account_filter: Specific account name to validate (None for all)
            account_type: Filter by account type ('crypto' or 'forex')
            enabled_only: Only validate enabled accounts
            timeout: Connection timeout per account in seconds
            
        Returns:
    pass
            List of AccountStatus objects with validation results
        """
        try:
    pass
            # Get all accounts
            all_accounts = self.get_all_accounts()
            
            # Apply filters
            if account_filter:
    
        pass
    pass
                all_accounts = [acc for acc in all_accounts if acc.get('name') == account_filter]
            
            accounts_to_validate = self.filter_accounts(
                all_accounts, 
                account_type=account_type, 
                enabled_only=enabled_only
            )
            
            if not accounts_to_validate:
    
        pass
    pass
                self.logger.warning("No accounts found matching the specified criteria")
                return []
            
            self.logger.info(f"Validating {len(accounts_to_validate)} account(s)")
            
            # Validate accounts concurrently (but with some limit to avoid overwhelming APIs)
            semaphore = asyncio.Semaphore(3)  # Max 3 concurrent validations
            
            async def validate_with_semaphore(account_config):
    
        pass
    pass
                async with semaphore:
    pass
                    return await self.validate_single_account(account_config, timeout)
            
            # Run validations
            validation_tasks = [
                validate_with_semaphore(account_config) 
                for account_config in accounts_to_validate
            ]
            
            results = await asyncio.gather(*validation_tasks, return_exceptions=True)
            
            # Process results and handle any exceptions
            account_statuses = []
            for i, result in enumerate(results):
    pass
    pass
                if isinstance(result, Exception):
    
        pass
    pass
                    account_config = accounts_to_validate[i]
                    self.logger.error(f"Validation failed for {account_config.get('name')}: {result}")
                    
                    # Create error status
                    account_statuses.append(AccountStatus(
                        name=account_config.get('name', 'unknown'),
                        type=account_config.get('type', 'unknown'),
                        exchange_or_broker=account_config.get('exchange_type', 
                                                           account_config.get('broker_type', 'unknown')),
                        enabled=account_config.get('enabled', False),
                        connected=False,
                        authenticated=False,
                        last_check=datetime.now(timezone.utc),
                        error_message=f"Validation exception: {str(result)}"
                    ))
                else:
    pass
                    account_statuses.append(result)
            
            return account_statuses
            
        except Exception as e:
    pass
    pass
            self.logger.error(f"Failed to validate accounts: {e}")
            return []
    
    def save_validation_history(self, statuses: List[AccountStatus]) -> None:
    pass
        """
        Save validation results to history file for tracking.
        
        Args:
    pass
            statuses: List of AccountStatus objects to save
        """
        try:
    pass
            history_file = self.config_path / "validation_history.yaml"
            
            # Load existing history
            history = []
            if history_file.exists():
    
        pass
    pass
                try:
    pass
                    with open(history_file, 'r') as f:
    pass
                        history = yaml.safe_load(f) or []
                except Exception as e:
    pass
    pass
                    self.logger.warning(f"Failed to load validation history: {e}")
            
            # Add new validation entry
            validation_entry = {
                'timestamp': datetime.now(timezone.utc).isoformat(),
                'accounts': []
            }
            
            for status in statuses:
    pass
                account_entry = {
                    'name': status.name,
                    'type': status.type,
                    'exchange_or_broker': status.exchange_or_broker,
                    'enabled': status.enabled,
                    'connected': status.connected,
                    'authenticated': status.authenticated,
                    'last_check': status.last_check.isoformat(),
                    'error_message': status.error_message,
                    'latency_ms': status.latency_ms
                }
                validation_entry['accounts'].append(account_entry)
            
            history.append(validation_entry)
            
            # Keep only last 50 validation runs
            if len(history) > 50:
    
        pass
    pass
                history = history[-50:]
            
            # Save updated history
            with open(history_file, 'w') as f:
    pass
                yaml.dump(history, f, default_flow_style=False)
            
            self.logger.debug(f"Saved validation history to {history_file}")
            
        except Exception as e:
    pass
    pass
            self.logger.warning(f"Failed to save validation history: {e}")
    
    def get_validation_history(self, account_name: Optional[str] = None, 
                             limit: int = 10) -> List[Dict[str, Any]]:
    pass
        """
        Get validation history for tracking account status over time.
        
        Args:
    pass
            account_name: Filter by specific account name (None for all)
            limit: Maximum number of history entries to return
            
        Returns:
    pass
            List of validation history entries
        """
        try:
    pass
            history_file = self.config_path / "validation_history.yaml"
            
            if not history_file.exists():
    
        pass
    pass
                return []
            
            with open(history_file, 'r') as f:
    pass
                history = yaml.safe_load(f) or []
            
            # Filter by account name if specified
            if account_name:
    
        pass
    pass
                filtered_history = []
                for entry in history:
    pass
                    filtered_accounts = [
                        acc for acc in entry.get('accounts', [])
                        if acc.get('name') == account_name
                    ]
                    if filtered_accounts:
    
        pass
    pass
                        filtered_entry = dict(entry)
                        filtered_entry['accounts'] = filtered_accounts
                        filtered_history.append(filtered_entry)
                history = filtered_history
            
            # Return most recent entries up to limit
            return history[-limit:] if len(history) > limit else history
            
        except Exception as e:
    
        pass
    pass
    pass
            self.logger.warning(f"Failed to load validation history: {e}")
            return []
    
    def get_account_status_trend(self, account_name: str, 
                               days: int = 7) -> Dict[str, Any]:
    pass
        """
        Get status trend for a specific account over time.
        
        Args:
    
        pass
    pass
            account_name: Name of account to analyze
            days: Number of days to look back
            
        Returns:
    pass
            Dictionary containing trend analysis
        """
        try:
    pass
            history = self.get_validation_history(account_name=account_name, limit=100)
            
            if not history:
    
        pass
    pass
                return {'account': account_name, 'trend': 'no_data', 'entries': 0}
            
            # Filter by date range
            cutoff_date = datetime.now(timezone.utc) - timedelta(days=days)
            recent_history = []
            
            for entry in history:
    pass
                try:
    pass
                    entry_date = datetime.fromisoformat(entry['timestamp'].replace('Z', '+00:00'))
                    if entry_date >= cutoff_date:
    
        pass
    pass
                except Exception:
    pass
    pass
                    continue
            
            if not recent_history:
    
        pass
    pass
                return {'account': account_name, 'trend': 'no_recent_data', 'entries': 0}
            
            # Analyze trend
            success_count = 0
            total_count = len(recent_history)
            
            for entry in recent_history:
    pass
                for account in entry.get('accounts', []):
    pass
                    if (account.get('name') == account_name and 
                        account.get('connected') and account.get('authenticated')):
    
        pass
    pass
                        success_count += 1
                        break
            
            success_rate = (success_count / total_count * 100) if total_count > 0 else 0
            
            # Determine trend
            if success_rate >= 90:
    
        pass
    pass
                trend = 'excellent'
            elif success_rate >= 75:
    
        pass
    pass
                trend = 'good'
            elif success_rate >= 50:
    
        pass
    pass
                trend = 'fair'
            elif success_rate >= 25:
    
        pass
    pass
                trend = 'poor'
            else:
    pass
                trend = 'critical'
            
            return {
                'account': account_name,
                'trend': trend,
                'success_rate': round(success_rate, 1),
                'entries': total_count,
                'successful_validations': success_count,
                'period_days': days
            }
            
        except Exception as e:
    pass
    pass
            self.logger.warning(f"Failed to analyze account trend: {e}")
            return {'account': account_name, 'trend': 'error', 'entries': 0}

    def get_validation_summary(self, statuses: List[AccountStatus]) -> Dict[str, Any]:
    pass
        """
        Generate a summary of validation results.
        
        Args:
    pass
            statuses: List of AccountStatus objects
            
        Returns:
    pass
            Dictionary containing validation summary statistics
        """
        if not statuses:
    
        pass
    pass
            return {
                'total_accounts': 0,
                'valid_accounts': 0,
                'invalid_accounts': 0,
                'enabled_accounts': 0,
                'disabled_accounts': 0,
                'crypto_accounts': 0,
                'forex_accounts': 0,
                'success_rate': 0.0,
                'average_latency_ms': 0.0
            }
        
        total = len(statuses)
        valid = sum(1 for s in statuses if s.connected and s.authenticated)
        invalid = total - valid
        enabled = sum(1 for s in statuses if s.enabled)
        disabled = total - enabled
        crypto = sum(1 for s in statuses if s.type == 'crypto')
        forex = sum(1 for s in statuses if s.type == 'forex')
        
        success_rate = (valid / total * 100) if total > 0 else 0.0
        
        # Calculate average latency for successful connections
        successful_latencies = [s.latency_ms for s in statuses ]
                              if s.latency_ms is not None and s.connected]
        avg_latency = (sum(successful_latencies) / len(successful_latencies) )
                      if successful_latencies else 0.0)
        
        return {
            'total_accounts': total,
            'valid_accounts': valid,
            'invalid_accounts': invalid,
            'enabled_accounts': enabled,
            'disabled_accounts': disabled,
            'crypto_accounts': crypto,
            'forex_accounts': forex,
            'success_rate': round(success_rate, 1),
            'average_latency_ms': round(avg_latency, 2)
        }