"""
Market Manager Example - Demonstrates multi-market orchestration.

This example shows how to use the MarketManager to coordinate
trading operations across multiple market types (crypto and forex).
"""

import asyncio
import logging
from typing import Dict, Any

from src.markets.manager import MarketManager, MarketConnectionError


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def get_example_config() -> Dict[str, Any]:
    pass
    """Get example configuration for market manager."""
    return {
        'markets': {
            'crypto': {
                'enabled': True,
                'exchanges': [
                    {
                        'name': 'binance',
                        'type': 'crypto',
                        'api_key': 'your_binance_api_key',
                        'api_secret': 'your_binance_api_secret',
                        'sandbox': True  # Use sandbox for testing
                    }
                ],
                'backup_brokers': [
                    {
                        'name': 'coinbase',
                        'type': 'crypto',
                        'api_key': 'your_coinbase_api_key',
                        'api_secret': 'your_coinbase_api_secret',
                        'sandbox': True
                    }
                ]
            },
            'forex': {
                'enabled': True,
                'brokers': [
                    {
                        'name': 'oanda',
                        'type': 'oanda',
                        'api_key': 'your_oanda_api_key',
                        'account_id': 'your_oanda_account_id',
                        'environment': 'practice'  # Use practice for testing
                    }
                ],
                'backup_brokers': [
                    {
                        'name': 'mt5',
                        'type': 'mt5',
                        'login': 'your_mt5_login',
                        'password': 'your_mt5_password',
                        'server': 'your_mt5_server'
                    }
                ]
            }
        },
        'health_check_interval': 30,  # seconds
        'failover_enabled': True
    }


async def demonstrate_market_manager():
    pass
    """Demonstrate MarketManager functionality."""
    logger.info("Starting Market Manager demonstration...")
    
    # Get configuration
    config = get_example_config()
    
    # Create market manager
    manager = MarketManager(config)
    
    try:
    pass
        # Initialize market connections
        logger.info("Initializing market connections...")
        await manager.initialize()
        
        # Show supported markets
        supported_markets = manager.get_supported_markets()
        logger.info("Supported markets: %s", [m.value for m in supported_markets])
        
        # Show market status
        market_status = manager.get_market_status()
        for market_type, status in market_status.items():
    pass
            logger.info("Market %s: connected=%s, healthy=%s", 
                       market_type.value, status.is_connected, status.is_healthy)
        
        # Show supported symbols
        all_symbols = manager.get_supported_symbols()
        logger.info("Total supported symbols: %d", len(all_symbols))
        
        if MarketType.CRYPTO in supported_markets:
    
        pass
    pass
            crypto_symbols = manager.get_supported_symbols(MarketType.CRYPTO)
            logger.info("Crypto symbols: %d", len(crypto_symbols))
            if crypto_symbols:
    
        pass
    pass
                logger.info("Sample crypto symbols: %s", 
                           [s.to_standard_format() for s in crypto_symbols[:5]])
        
        if MarketType.FOREX in supported_markets:
    
        pass
    pass
            forex_symbols = manager.get_supported_symbols(MarketType.FOREX)
            logger.info("Forex symbols: %d", len(forex_symbols))
            if forex_symbols:
    
        pass
    pass
                logger.info("Sample forex symbols: %s", 
                           [s.to_standard_format() for s in forex_symbols[:5]])
        
        # Demonstrate market data retrieval
        await demonstrate_market_data(manager)
        
        # Demonstrate balance retrieval
        await demonstrate_balance_retrieval(manager)
        
        # Demonstrate order operations
        await demonstrate_order_operations(manager)
        
        # Show health status
        health_status = manager.get_health_status()
        logger.info("Overall health: %s", health_status['overall_healthy'])
        
        # Wait a bit to see health monitoring in action
        logger.info("Monitoring health for 10 seconds...")
        await asyncio.sleep(10)
        
        # Show final health status
        final_health = manager.get_health_status()
        logger.info("Final health status: %s", final_health['overall_healthy'])
        
    except MarketConnectionError as e:
    pass
    pass
        logger.error("Market connection error: %s", e)
    except Exception as e:
    pass
    pass
        logger.error("Unexpected error: %s", e)
    finally:
    pass
        # Cleanup
        logger.info("Shutting down market manager...")
        await manager.shutdown()
        logger.info("Market manager shutdown complete")


async def demonstrate_market_data(manager: MarketManager):
    pass
    """Demonstrate market data retrieval."""
    logger.info("\n--- Market Data Demonstration ---")
    
    try:
    pass
        # Try to get crypto market data
        if manager.is_market_supported(MarketType.CRYPTO):
    
        pass
    pass
            crypto_symbols = manager.get_supported_symbols(MarketType.CRYPTO)
            if crypto_symbols:
    
        pass
    pass
                symbol = crypto_symbols[0]  # Use first available symbol
                logger.info("Getting market data for %s...", symbol.to_standard_format())
                
                data = await manager.get_market_data(symbol, timeframe='1h', limit=10)
                logger.info("Retrieved %d data points", len(data))
                
                if data:
    
        pass
    pass
                    latest = data[-1]
                    logger.info("Latest data: O=%.4f H=%.4f L=%.4f C=%.4f V=%.2f", 
                               latest.open, latest.high, latest.low, latest.close, latest.volume)
                
                # Get current price
                current_price = await manager.get_current_price(symbol)
                logger.info("Current price for %s: %.4f", symbol.to_standard_format(), current_price)
        
        # Try to get forex market data
        if manager.is_market_supported(MarketType.FOREX):
    
        pass
    pass
            forex_symbols = manager.get_supported_symbols(MarketType.FOREX)
            if forex_symbols:
    
        pass
    pass
                symbol = forex_symbols[0]  # Use first available symbol
                logger.info("Getting market data for %s...", symbol.to_standard_format())
                
                data = await manager.get_market_data(symbol, timeframe='1h', limit=10)
                logger.info("Retrieved %d data points", len(data))
                
                if data:
    
        pass
    pass
                    latest = data[-1]
                    logger.info("Latest data: O=%.5f H=%.5f L=%.5f C=%.5f V=%.2f", 
                               latest.open, latest.high, latest.low, latest.close, latest.volume)
                
                # Get current price
                current_price = await manager.get_current_price(symbol)
                logger.info("Current price for %s: %.5f", symbol.to_standard_format(), current_price)
                
    except Exception as e:
    pass
    pass
        logger.error("Error getting market data: %s", e)


async def demonstrate_balance_retrieval(manager: MarketManager):
    pass
    """Demonstrate balance retrieval."""
    logger.info("\n--- Balance Demonstration ---")
    
    try:
    pass
        # Get balance from all markets
        all_balance = await manager.get_balance()
        for asset, amount in all_balance.items():
    pass
            if amount > 0:  # Only show non-zero balances
        
        # Get balance from specific markets
        if manager.is_market_supported(MarketType.CRYPTO):
    
        pass
    pass
            crypto_balance = await manager.get_balance(MarketType.CRYPTO)
            for asset, amount in crypto_balance.items():
    pass
                if amount > 0:
    
        pass
    pass
                    logger.info("  %s: %.8f", asset, amount)
        
        if manager.is_market_supported(MarketType.FOREX):
    
        pass
    pass
            forex_balance = await manager.get_balance(MarketType.FOREX)
            logger.info("Forex balance:")
            for asset, amount in forex_balance.items():
    pass
                if amount > 0:
    
        pass
    pass
                    logger.info("  %s: %.2f", asset, amount)
                    
    except Exception as e:
    pass
    pass
        logger.error("Error getting balance: %s", e)


async def demonstrate_order_operations(manager: MarketManager):
    pass
    """Demonstrate order operations."""
    logger.info("\n--- Order Operations Demonstration ---")
    
    try:
    pass
        # Note: This is just a demonstration - in a real scenario,
        # you would want to be more careful about order placement
        
        # Try crypto order (small amount for safety)
        if manager.is_market_supported(MarketType.CRYPTO):
    
        pass
    pass
            crypto_symbols = manager.get_supported_symbols(MarketType.CRYPTO)
            if crypto_symbols:
    
        pass
    pass
                symbol = crypto_symbols[0]
                
                # Check if market is open
                if manager._handlers[MarketType.CRYPTO].is_market_open(symbol):
    
        pass
    pass
                    logger.info("Crypto market is open for %s", symbol.to_standard_format())
                    
                    # In a real scenario, you would place actual orders here
                    logger.info("Would place crypto order for %s", symbol.to_standard_format())
                else:
    pass
                    logger.info("Crypto market is closed for %s", symbol.to_standard_format())
        
        # Try forex order
        if manager.is_market_supported(MarketType.FOREX):
    
        pass
    pass
            forex_symbols = manager.get_supported_symbols(MarketType.FOREX)
            if forex_symbols:
    
        pass
    pass
                symbol = forex_symbols[0]
                
                # Check if market is open
                if manager._handlers[MarketType.FOREX].is_market_open(symbol):
    
        pass
    pass
                    logger.info("Forex market is open for %s", symbol.to_standard_format())
                    
                    # In a real scenario, you would place actual orders here
                    logger.info("Would place forex order for %s", symbol.to_standard_format())
                else:
    pass
                    logger.info("Forex market is closed for %s", symbol.to_standard_format())
                    
                    # Show market hours
                    market_hours = manager._handlers[MarketType.FOREX].get_market_hours(symbol)
                    logger.info("Market hours info: %s", market_hours)
                    
    except Exception as e:
    pass
    pass
        logger.error("Error with order operations: %s", e)


async def demonstrate_failover():
    pass
    """Demonstrate failover functionality."""
    logger.info("\n--- Failover Demonstration ---")
    
    # This would require a more complex setup with actual failing connections
    # For now, we'll just log what would happen
    logger.info("Failover would be triggered when primary connections fail")
    logger.info("Backup handlers would automatically take over")
    logger.info("Trading operations would continue seamlessly")


def main():
    pass
    """Main function to run the demonstration."""
    try:
    pass
        asyncio.run(demonstrate_market_manager())
    except KeyboardInterrupt:
    pass
    pass
        logger.info("Demonstration interrupted by user")
    except Exception as e:
    pass
    pass
        logger.error("Demonstration failed: %s", e)


if __name__ == "__main__":
    
        pass
    pass
    main()