"""
Integration Manager
==================

Manages integration between CLI and existing trading bot components.
Provides unified access to exchange adapters, configuration system,
database models, and validation utilities.
"""

import asyncio
import logging
from pathlib import Path
from datetime import datetime, timedelta

# Import existing trading bot components
from genebot.config.manager import ConfigManager, get_config_manager
# Import existing trading bot components with fallbacks
try:
    
        pass
    pass
    import sys
    from pathlib import Path
    # Add src to path for imports
    src_path = Path(__file__).parent.parent.parent.parent / 'src'
    if str(src_path) not in sys.path:
    
        pass
    pass
    from src.exchanges.base import ExchangeAdapter
    from src.exchanges.ccxt_adapter import CCXTAdapter
except ImportError:
    pass
    pass
    # Create minimal stubs for CLI functionality
    class ExchangeAdapter:
    pass
        def __init__(self, *args, **kwargs):
    pass
            self.name = args[0] if args else 'unknown'
            self.config = args[1] if len(args) > 1 else kwargs
            self._connected = False
            self._authenticated = False
        
        async def connect(self):
    
        pass
    pass
            self._connected = True
            return True
        
        async def authenticate(self):
    pass
            self._authenticated = True
            return True
        
        async def disconnect(self):
    pass
            self._connected = False
            self._authenticated = False
    
    class CCXTAdapter(ExchangeAdapter):
    pass
        def __init__(self, *args, **kwargs):
    pass
            super().__init__(*args, **kwargs)
        
        async def get_balance(self):
    pass
            """Get account balance - stub implementation"""
            return {
                'USDT': {'free': 1000.0, 'used': 0.0, 'total': 1000.0},
                'BTC': {'free': 0.1, 'used': 0.0, 'total': 0.1}
            }
        
        async def health_check(self):
    pass
            """Perform health check - stub implementation"""
            from datetime import datetime, timezone
            return {
                'status': 'healthy' if self._connected else 'disconnected',
                'latency_ms': 50.0,
                'error': None
            }
        
        def validate_credentials(self):
    pass
            """Validate credentials - stub implementation"""
            return True

try:
    pass
    from src.models.database_models import ()
except ImportError:
    pass
    pass
    # Create minimal stubs
    class OrderModel:
    pass
        def __init__(self, **kwargs):
    pass
            for k, v in kwargs.items():
    pass
                setattr(self, k, v)
    
    class TradeModel:
    pass
        def __init__(self, **kwargs):
    pass
            for k, v in kwargs.items():
    pass
                setattr(self, k, v)
    
    class PositionModel:
    pass
        def __init__(self, **kwargs):
    pass
            for k, v in kwargs.items():
    pass
                setattr(self, k, v)
    
    class MarketDataModel:
    pass
        def __init__(self, **kwargs):
    pass
            for k, v in kwargs.items():
    pass
                setattr(self, k, v)
    
    class StrategyPerformanceModel:
    pass
        def __init__(self, **kwargs):
    pass
            for k, v in kwargs.items():
    pass
                setattr(self, k, v)
    
    class RiskEventModel:
    pass
        def __init__(self, **kwargs):
    pass
            for k, v in kwargs.items():
    pass
                setattr(self, k, v)

try:
    pass
    from genebot.exceptions.base_exceptions import (
        ValidationException
except ImportError:
    pass
    pass
    # Create minimal exception stubs
    class TradingBotException(Exception):
    pass
    pass
    class ExchangeException(TradingBotException):
    pass
    class ConfigurationException(TradingBotException):
    pass
    class ValidationException(TradingBotException):
    pass
# Import validation utilities with fallback
try:
    pass
    from ...config.validation_utils import ConfigValidator, validate_config_file
except ImportError:
    pass
    pass
    ConfigValidator = None
    validate_config_file = None

# Import database connection with fallback
try:
    pass
    from src.database.connection import DatabaseConnection
except ImportError:
    pass
    pass
    class DatabaseConnection:
    pass
        def __init__(self, *args, **kwargs):
    pass
        def connect(self):
    pass
            return None
        
        def close(self):
    pass
# Forex adapters will be imported dynamically when needed

from ..result import CommandResult
from .error_handler import CLIException, ConfigurationError


class IntegrationManager:
    pass
    """
    Manages integration between CLI and existing trading bot components.
    
    Provides unified access to:
    
        pass
    pass
    - Exchange adapters (crypto and forex)
    - Configuration management system
    - Database models and connections
    - Validation utilities
    - Error handling patterns
    """
    
    def __init__(self, config_path: Path = None, env_file: Path = None):
    pass
        """
        Initialize integration manager.
        
        Args:
    pass
            config_path: Path to configuration directory
            env_file: Path to environment file
        """
        self.config_path = config_path or Path("config")
        self.env_file = env_file or Path(".env")
        self.logger = logging.getLogger(__name__)
        
        # Initialize configuration manager
        self._config_manager = None
        self._db_connection = None
        self._exchange_adapters: Dict[str, ExchangeAdapter] = {}
        
    @property
    def config_manager(self) -> ConfigManager:
    pass
        """Get configuration manager instance."""
        if self._config_manager is None:
    
        pass
    pass
            try:
    pass
                # Try to get existing config manager or create new one
                self._config_manager = get_config_manager()
            except Exception:
    pass
    pass
                # Fallback: create new config manager
                config_file = self.config_path / "trading_bot_config.yaml"
                self._config_manager = ConfigManager(
                    config_path=str(config_file) if config_file.exists() else None,
                    env_file=str(self.env_file) if self.env_file.exists() else None
                )
        return self._config_manager
    
    @property
    def db_connection(self):
    
        pass
    pass
        """Get database connection instance."""
        if DatabaseConnection is None:
    
        pass
    pass
            raise ConfigurationError(
                "Database connection not available",
                suggestions=[
                    "Install database dependencies",
                    "Check database configuration"
                ]
            )
        
        if self._db_connection is None:
    
        pass
    pass
            try:
    pass
                config = self.config_manager.get_config()
                self._db_connection = DatabaseConnection(config.database)
            except Exception as e:
    pass
    pass
                raise ConfigurationError(
                    f"Failed to initialize database connection: {e}",
                    suggestions=[
                        "Check database configuration in trading_bot_config.yaml",
                        "Ensure database is accessible",
                        "Verify database credentials"
                    ]
                )
        return self._db_connection
    
    def get_exchange_adapter(self, exchange_name: str) -> ExchangeAdapter:
    pass
        """
        Get exchange adapter instance.
        
        Args:
    pass
            exchange_name: Name of the exchange/broker
            
        Returns:
    pass
            ExchangeAdapter: Exchange adapter instance
            
        Raises:
    pass
            ConfigurationError: If exchange is not configured
        """
        if exchange_name in self._exchange_adapters:
    
        pass
    pass
            return self._exchange_adapters[exchange_name]
        
        try:
    pass
            config = self.config_manager.get_config()
            
            # Handle both dict and object config formats
            if isinstance(config, dict):
    
        pass
    pass
                exchanges = config.get('exchanges', {})
            else:
    pass
                exchanges = getattr(config, 'exchanges', {})
            
            # Check if it's a crypto exchange
            if exchange_name in exchanges:
    
        pass
    pass
                exchange_config = exchanges[exchange_name]
                if isinstance(exchange_config, dict):
    
        pass
    pass
                    adapter = CCXTAdapter(exchange_name, exchange_config)
                else:
    pass
                    adapter = CCXTAdapter(exchange_name, exchange_config.dict())
                self._exchange_adapters[exchange_name] = adapter
                return adapter
            
            # Check if it's a forex broker (if multi-market config exists)
            try:
    
        pass
    pass
                from config.multi_market_manager import MultiMarketConfigManager
                multi_config_manager = MultiMarketConfigManager(
                    config_file=self.config_path / "multi_market_config.yaml"
                multi_config = multi_config_manager.get_config()
                
                if multi_config.forex.enabled and exchange_name in multi_config.forex.brokers:
    
        pass
    pass
                    broker_config = multi_config.forex.brokers[exchange_name]
                    
                    # Create appropriate forex adapter with dynamic imports
                    if broker_config.broker_type.value == 'oanda':
    
        pass
    pass
                        try:
    pass
                            from src.exchanges.forex.oanda_adapter import OANDAAdapter
                            adapter = OANDAAdapter(exchange_name, broker_config.dict())
                        except ImportError as e:
    pass
    pass
                            raise ConfigurationError(
                                suggestions=["Install forex adapter dependencies", "Check OANDA adapter implementation"]
                            )
                    elif broker_config.broker_type.value == 'ib':
    
        pass
    pass
                        try:
    pass
                            from src.exchanges.forex.ib_adapter import IBAdapter
                            adapter = IBAdapter(exchange_name, broker_config.dict())
                        except ImportError as e:
    pass
    pass
                            raise ConfigurationError(
                                suggestions=["Install IB API dependencies", "Check IB adapter implementation"]
                            )
                    elif broker_config.broker_type.value == 'mt5':
    
        pass
    pass
                        try:
    pass
                            from src.exchanges.forex.mt5_adapter import MT5Adapter
                            adapter = MT5Adapter(exchange_name, broker_config.dict())
                        except ImportError as e:
    pass
    pass
                            raise ConfigurationError(
                                suggestions=["Install MT5 dependencies", "Check MT5 adapter implementation"]
                            )
                    else:
    pass
                        raise ConfigurationError(f"Unsupported broker type: {broker_config.broker_type}")
                    
                    self._exchange_adapters[exchange_name] = adapter
                    return adapter
                    
            except ImportError:
    pass
    pass
                # Multi-market config not available, continue with error
            
            raise ConfigurationError(
                f"Exchange/broker '{exchange_name}' not found in configuration",
                suggestions=[
                    "Check exchange name spelling",
                    "Add exchange configuration to trading_bot_config.yaml",
                    "Use 'genebot list-exchanges' to see available exchanges"
                ]
            )
            
        except Exception as e:
    pass
    pass
            if isinstance(e, CLIException):
    
        pass
    pass
                raise
            raise ConfigurationError(
                f"Failed to create exchange adapter for '{exchange_name}': {e}",
                suggestions=[
                    "Check exchange configuration",
                    "Verify API credentials",
                    "Check network connectivity"
                ]
            )
    
    async def test_exchange_connection(self, exchange_name: str) -> CommandResult:
    pass
        """
        Test connection to an exchange/broker.
        
        Args:
    pass
            exchange_name: Name of the exchange/broker
            
        Returns:
    pass
            CommandResult: Test result
        """
        try:
    pass
            adapter = self.get_exchange_adapter(exchange_name)
            
            # Test connection
            await adapter.connect()
            
            # Test authentication if credentials are provided
            if adapter.validate_credentials():
    
        pass
    pass
                await adapter.authenticate()
            
            # Perform health check
            health_status = await adapter.health_check()
            
            await adapter.disconnect()
            
            return CommandResult.success(
                f"Successfully connected to {exchange_name}",
                data={
                    'exchange': exchange_name,
                    'connected': True,
                    'authenticated': adapter.is_authenticated,
                    'health_status': health_status
                },
                suggestions=[
                    f"Exchange '{exchange_name}' is ready for trading",
                    "Use 'genebot start' to begin trading"
                ]
            )
            
        except Exception as e:
    pass
    pass
            return CommandResult.error(
                f"Failed to connect to {exchange_name}: {e}",
                suggestions=[
                    "Check API credentials in configuration",
                    "Verify network connectivity",
                    "Check exchange status",
                    f"Use 'genebot validate-accounts' to test all accounts"
                ]
            )
    
    def get_available_exchanges(self) -> List[Dict[str, Any]]:
    
        pass
    pass
        """
        Get list of available exchanges and brokers.
        
        Returns:
    pass
            List of exchange/broker information
        """
        exchanges = []
        
        try:
    pass
            config = self.config_manager.get_config()
            
            # Add crypto exchanges
            for name, exchange_config in config.exchanges.items():
    pass
                exchanges.append({
                    'name': name,
                    'type': 'crypto',
                    'exchange_type': exchange_config.exchange_type.value,
                    'enabled': exchange_config.enabled,
                    'sandbox': exchange_config.sandbox
                })
            
            # Add forex brokers if multi-market config exists
            try:
    
        pass
    pass
                from config.multi_market_manager import MultiMarketConfigManager
                multi_config_manager = MultiMarketConfigManager(
                    config_file=self.config_path / "multi_market_config.yaml"
                multi_config = multi_config_manager.get_config()
                
                if multi_config.forex.enabled:
    
        pass
    pass
                    for name, broker_config in multi_config.forex.brokers.items():
    pass
                        exchanges.append({
                            'name': name,
                            'type': 'forex',
                            'broker_type': broker_config.broker_type.value,
                            'enabled': broker_config.enabled,
                            'sandbox': broker_config.sandbox
                        })
                        
            except ImportError:
    pass
    pass
                # Multi-market config not available
            
        except Exception as e:
    pass
    pass
            self.logger.warning(f"Failed to load exchange configurations: {e}")
        
        return exchanges
    
    def validate_configuration(self) -> CommandResult:
    pass
        """
        Validate current configuration using existing validation utilities.
        
        Returns:
    pass
            CommandResult: Validation result
        """
        try:
    pass
            # Validate main configuration
            config = self.config_manager.get_config()
            
            # Use existing validation utilities if available
            config_file = self.config_path / "trading_bot_config.yaml"
            if config_file.exists() and validate_config_file is not None:
    
        pass
    pass
                validation_result = validate_config_file(config_file)
                
                if validation_result.is_valid:
    
        pass
    pass
                    return CommandResult.success(
                        "Configuration is valid",
                        data={
                            'config_file': str(config_file),
                            'warnings': validation_result.warnings,
                            'info': validation_result.info
                        },
                        suggestions=[
                            "Configuration passed all validation checks",
                            "Use 'genebot validate-accounts' to test exchange connections"
                        ]
                    )
                else:
    pass
                    return CommandResult.error(
                        "Configuration validation failed",
                        data={
                            'errors': validation_result.errors,
                            'warnings': validation_result.warnings
                        },
                        suggestions=[
                            "Fix configuration errors before proceeding",
                            "Check configuration file format and values",
                            "Use configuration templates for reference"
                        ]
                    )
            elif config_file.exists():
    
        pass
    pass
                # Basic validation without advanced utilities
                return CommandResult.success(
                    "Configuration loaded successfully",
                    data={'config_file': str(config_file)},
                    suggestions=[
                        "Configuration file loaded",
                        "Advanced validation utilities not available"
                    ]
                )
            else:
    pass
                return CommandResult.error(
                    "Configuration file not found",
                    suggestions=[
                        "Run 'genebot init-config' to create configuration files",
                        "Check configuration file path",
                        "Copy from configuration templates"
                    ]
                
        except Exception as e:
    pass
    pass
            return CommandResult.error(
                f"Configuration validation error: {e}",
                suggestions=[
                    "Check configuration file format",
                    "Verify file permissions",
                    "Check log files for detailed errors"
                ]
            )
    
    def get_database_session(self):
    
        pass
    pass
        """Get database session for data operations."""
        try:
    pass
            return self.db_connection.get_session()
        except Exception as e:
    pass
    pass
            raise ConfigurationError(
                f"Failed to get database session: {e}",
                suggestions=[
                    "Check database configuration",
                    "Ensure database is running",
                    "Verify database permissions"
                ]
            )
    
    def get_recent_trades(self, limit: int = 10, symbol: str = None) -> List[Dict[str, Any]]:
    pass
        """
        Get recent trades from database.
        
        Args:
    pass
            limit: Maximum number of trades to return
            symbol: Optional symbol filter
            
        Returns:
    pass
            List of trade data
        """
        try:
    pass
            session = self.get_database_session()
            
            query = session.query(TradeModel)
            if symbol:
    
        pass
    pass
                query = query.filter(TradeModel.symbol == symbol)
            
            trades = query.order_by(TradeModel.timestamp.desc()).limit(limit).all()
            
            return [
                {
                    'id': trade.id,
                    'symbol': trade.symbol,
                    'side': trade.side,
                    'amount': float(trade.amount),
                    'price': float(trade.price),
                    'fees': float(trade.fees),
                    'timestamp': trade.timestamp.isoformat(),
                    'exchange': trade.exchange
                }
                for trade in trades
            ]
            
        except Exception as e:
    pass
    pass
            self.logger.error(f"Failed to get recent trades: {e}")
            return []
        finally:
    pass
            if 'session' in locals():
    
        pass
    pass
                session.close()
    
    def get_open_orders(self, symbol: str = None) -> List[Dict[str, Any]]:
    pass
        """
        Get open orders from database.
        
        Args:
    pass
            symbol: Optional symbol filter
            
        Returns:
    pass
            List of open orders
        """
        try:
    pass
            session = self.get_database_session()
            
            query = session.query(OrderModel).filter(OrderModel.status == 'OPEN')
            if symbol:
    
        pass
    pass
                query = query.filter(OrderModel.symbol == symbol)
            
            orders = query.order_by(OrderModel.timestamp.desc()).all()
            
            return [
                {
                    'id': order.id,
                    'symbol': order.symbol,
                    'side': order.side,
                    'amount': float(order.amount),
                    'price': float(order.price) if order.price else None,
                    'order_type': order.order_type,
                    'status': order.status,
                    'timestamp': order.timestamp.isoformat(),
                    'exchange': order.exchange,
                    'filled_amount': float(order.filled_amount)
                }
                for order in orders
            ]
            
        except Exception as e:
    pass
    pass
            self.logger.error(f"Failed to get open orders: {e}")
            return []
        finally:
    pass
            if 'session' in locals():
    
        pass
    pass
                session.close()
    
    def get_current_positions(self, symbol: str = None) -> List[Dict[str, Any]]:
    pass
        """
        Get current positions from database.
        
        Args:
    pass
            symbol: Optional symbol filter
            
        Returns:
    pass
            List of current positions
        """
        try:
    pass
            session = self.get_database_session()
            
            query = session.query(PositionModel).filter(PositionModel.is_active == 'true')
            if symbol:
    
        pass
    pass
                query = query.filter(PositionModel.symbol == symbol)
            
            positions = query.all()
            
            return [
                {
                    'id': position.id,
                    'symbol': position.symbol,
                    'size': float(position.size),
                    'entry_price': float(position.entry_price),
                    'current_price': float(position.current_price),
                    'side': position.side,
                    'exchange': position.exchange,
                    'opened_at': position.opened_at.isoformat(),
                    'pnl': float((position.current_price - position.entry_price) * position.size)
                }
                for position in positions
            ]
            
        except Exception as e:
    pass
    pass
            self.logger.error(f"Failed to get current positions: {e}")
            return []
        finally:
    pass
            if 'session' in locals():
    
        pass
    pass
                session.close()
    
    def get_strategy_performance(self, strategy_name: str = None, 
                               days: int = 30) -> List[Dict[str, Any]]:
    pass
        """
        Get strategy performance data.
        
        Args:
    pass
            strategy_name: Optional strategy filter
            days: Number of days to look back
            
        Returns:
    pass
            List of strategy performance data
        """
        try:
    pass
            session = self.get_database_session()
            
            cutoff_date = datetime.utcnow() - timedelta(days=days)
            query = session.query(StrategyPerformanceModel).filter(
                StrategyPerformanceModel.period_start >= cutoff_date
            )
            
            if strategy_name:
    
        pass
    pass
                query = query.filter(StrategyPerformanceModel.strategy_name == strategy_name)
            
            performance_data = query.order_by(StrategyPerformanceModel.period_start.desc()).all()
            
            return [
                {
                    'strategy_name': perf.strategy_name,
                    'symbol': perf.symbol,
                    'period_start': perf.period_start.isoformat(),
                    'period_end': perf.period_end.isoformat(),
                    'total_trades': perf.total_trades,
                    'winning_trades': perf.winning_trades,
                    'losing_trades': perf.losing_trades,
                    'total_pnl': float(perf.total_pnl),
                    'win_rate': float(perf.win_rate),
                    'sharpe_ratio': float(perf.sharpe_ratio) if perf.sharpe_ratio else None,
                    'max_drawdown': float(perf.max_drawdown)
                }
                for perf in performance_data
            ]
            
        except Exception as e:
    pass
    pass
            self.logger.error(f"Failed to get strategy performance: {e}")
            return []
        finally:
    pass
            if 'session' in locals():
    
        pass
    pass
                session.close()
    
    async def close_all_orders(self, symbol: str = None, 
                              exchange: str = None) -> CommandResult:
    pass
        """
        Close all open orders using exchange APIs.
        
        Args:
    pass
            symbol: Optional symbol filter
            exchange: Optional exchange filter
            
        Returns:
    pass
            CommandResult: Operation result
        """
        try:
    pass
            # Get open orders from database
            open_orders = self.get_open_orders(symbol)
            
            if not open_orders:
    
        pass
    pass
                return CommandResult.success(
                    suggestions=["All orders are already closed or filled"]
                )
            
            # Filter by exchange if specified
            if exchange:
    
        pass
    pass
                open_orders = [order for order in open_orders if order['exchange'] == exchange]
            
            closed_orders = []
            failed_orders = []
            
            # Group orders by exchange
            orders_by_exchange = {}
            for order in open_orders:
    
        pass
    pass
                exchange_name = order['exchange']
                if exchange_name not in orders_by_exchange:
    
        pass
    pass
                    orders_by_exchange[exchange_name] = []
                orders_by_exchange[exchange_name].append(order)
            
            # Close orders on each exchange
            for exchange_name, orders in orders_by_exchange.items():
    pass
                try:
    pass
                    adapter = self.get_exchange_adapter(exchange_name)
                    await adapter.connect()
                    
                    for order in orders:
    pass
                        try:
    pass
                            await adapter.cancel_order(order['id'], order['symbol'])
                            closed_orders.append(order)
                        except Exception as e:
    pass
    pass
                            self.logger.error(f"Failed to close order {order['id']}: {e}")
                            failed_orders.append({'order': order, 'error': str(e)})
                    
                    await adapter.disconnect()
                    
                except Exception as e:
    pass
    pass
                    self.logger.error(f"Failed to connect to {exchange_name}: {e}")
                    for order in orders:
    pass
                        failed_orders.append({'order': order, 'error': f"Connection failed: {e}"})
            
            # Prepare result
            if closed_orders and not failed_orders:
    
        pass
    pass
                return CommandResult.success(
                    f"Successfully closed {len(closed_orders)} orders",
                    data={
                        'closed_orders': len(closed_orders),
                        'failed_orders': 0
                    },
                    suggestions=["All orders closed successfully"]
                )
            elif closed_orders and failed_orders:
    
        pass
    pass
                return CommandResult.warning(
                    f"Closed {len(closed_orders)} orders, {len(failed_orders)} failed",
                    data={
                        'closed_orders': len(closed_orders),
                        'failed_orders': len(failed_orders),
                        'failures': failed_orders
                    },
                    suggestions=[
                        "Some orders could not be closed",
                        "Check exchange connectivity",
                        "Retry failed orders manually"
                    ]
                )
            else:
    pass
                return CommandResult.error(
                    f"Failed to close any orders ({len(failed_orders)} failures)",
                    data={'failures': failed_orders},
                    suggestions=[
                        "Check exchange connectivity",
                        "Verify API credentials",
                        "Check order status manually"
                    ]
                )
                
        except Exception as e:
    
        pass
    pass
    pass
            return CommandResult.error(
                f"Failed to close orders: {e}",
                suggestions=[
                    "Check exchange connectivity",
                    "Verify configuration",
                    "Check log files for detailed errors"
                ]
            )
    
    def cleanup(self):
    
        pass
    pass
        """Clean up resources."""
        # Close exchange adapters
        for adapter in self._exchange_adapters.values():
    pass
            try:
    pass
                if hasattr(adapter, 'disconnect'):
    
        pass
    pass
                    asyncio.create_task(adapter.disconnect())
            except Exception as e:
    pass
    pass
                self.logger.warning(f"Error disconnecting adapter: {e}")
        
        # Close database connection
        if self._db_connection:
    
        pass
    pass
            try:
    pass
                self._db_connection.close()
            except Exception as e:
    pass
    pass
                self.logger.warning(f"Error closing database connection: {e}")