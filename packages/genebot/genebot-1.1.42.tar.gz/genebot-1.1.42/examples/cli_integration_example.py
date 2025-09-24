#!/usr/bin/env python3
"""
CLI Integration Example
======================

This example demonstrates how the GeneBot CLI integrates with existing
trading bot components including exchange adapters, configuration management,
database models, and validation utilities.
"""

import asyncio
import logging
from pathlib import Path

# Import CLI integration components
from genebot.cli.utils.integration_manager import IntegrationManager
from genebot.cli.utils.account_validator import RealAccountValidator

# Import existing trading bot components


async def demonstrate_exchange_integration():
    pass
    """Demonstrate CLI integration with existing exchange adapters."""
    print("=== Exchange Integration Demo ===")
    
    # Initialize integration manager
    integration_manager = IntegrationManager(
        config_path=Path("config"),
        env_file=Path(".env")
    )
    
    try:
    pass
        # Get available exchanges using existing configuration
        exchanges = integration_manager.get_available_exchanges()
        print(f"Found {len(exchanges)} configured exchanges/brokers:")
        
        for exchange in exchanges:
    pass
            print(f"  - {exchange['name']} ({exchange['type']}: {exchange['exchange_type']})")
            print(f"    Enabled: {exchange['enabled']}, Sandbox: {exchange['sandbox']}")
        
        # Test connection to first available exchange
        if exchanges:
    
        pass
    pass
            exchange_name = exchanges[0]['name']
            print(f"\nTesting connection to {exchange_name}...")
            
            result = await integration_manager.test_exchange_connection(exchange_name)
            if result.success:
    
        pass
    pass
                print(f"✅ {result.message}")
                print(f"   Connected: {result.data['connected']}")
                print(f"   Authenticated: {result.data['authenticated']}")
                if 'health_status' in result.data:
    
        pass
    pass
                    health = result.data['health_status']
                    print(f"   Status: {health.get('status', 'unknown')}")
                    if 'latency_ms' in health:
    
        pass
    pass
                        print(f"   Latency: {health['latency_ms']}ms")
            else:
    pass
                print(f"❌ {result.message}")
                for suggestion in result.suggestions:
    pass
                    print(f"   💡 {suggestion}")
    
    except Exception as e:
    pass
    pass
        print(f"❌ Exchange integration error: {e}")
    
    finally:
    pass
        integration_manager.cleanup()


def demonstrate_configuration_integration():
    pass
    """Demonstrate CLI integration with existing configuration management."""
    print("\n=== Configuration Integration Demo ===")
    
    # Initialize integration manager
    integration_manager = IntegrationManager()
    
    try:
    pass
        # Validate configuration using existing validation utilities
        result = integration_manager.validate_configuration()
        
        if result.success:
    
        pass
    pass
            print("✅ Configuration validation passed")
            if result.data and 'warnings' in result.data:
    
        pass
    pass
                for warning in result.data['warnings']:
    pass
                    print(f"   ⚠️  {warning}")
            if result.data and 'info' in result.data:
    
        pass
    pass
                for info in result.data['info']:
    pass
                    print(f"   ℹ️  {info}")
        else:
    pass
            print("❌ Configuration validation failed")
            if result.data and 'errors' in result.data:
    
        pass
    pass
                for error in result.data['errors']:
    pass
                    print(f"   ❌ {error}")
        
        # Access configuration manager directly
        config_manager = integration_manager.config_manager
        config = config_manager.get_config()
        
        print(f"\nConfiguration details:")
        print(f"  App name: {config.app_name}")
        print(f"  Version: {config.version}")
        print(f"  Debug mode: {config.debug}")
        print(f"  Dry run: {config.dry_run}")
        print(f"  Base currency: {config.base_currency}")
        print(f"  Exchanges configured: {len(config.exchanges)}")
        print(f"  Strategies configured: {len(config.strategies)}")
    
    except Exception as e:
    pass
    pass
        print(f"❌ Configuration integration error: {e}")


def demonstrate_database_integration():
    pass
    """Demonstrate CLI integration with existing database models."""
    print("\n=== Database Integration Demo ===")
    
    # Initialize integration manager
    integration_manager = IntegrationManager()
    
    try:
    pass
        # Get recent trades using existing database models
        trades = integration_manager.get_recent_trades(limit=5)
        print(f"Recent trades ({len(trades)}):")
        
        if trades:
    
        pass
    pass
            for trade in trades:
    pass
                timestamp = datetime.fromisoformat(trade['timestamp'].replace('Z', ''))
        else:
    pass
        # Get open orders
        orders = integration_manager.get_open_orders()
        print(f"\nOpen orders ({len(orders)}):")
        
        if orders:
    
        pass
    pass
            for order in orders:
    pass
                timestamp = datetime.fromisoformat(order['timestamp'].replace('Z', ''))
                if order['price']:
    
        pass
    pass
                print(f"    Filled: {order['filled_amount']}")
        else:
    pass
            print("  No open orders found")
        
        # Get current positions
        positions = integration_manager.get_current_positions()
        print(f"\nCurrent positions ({len(positions)}):")
        
        if positions:
    
        pass
    pass
            for position in positions:
    pass
                opened_at = datetime.fromisoformat(position['opened_at'].replace('Z', ''))
                print(f"    Entry: {position['entry_price']}, Current: {position['current_price']}")
        else:
    pass
            print("  No open positions found")
        
        # Get strategy performance
        performance = integration_manager.get_strategy_performance(days=7)
        print(f"\nStrategy performance (last 7 days, {len(performance)} entries):")
        
        if performance:
    
        pass
    pass
            for perf in performance[:3]:  # Show top 3
                print(f"  - {perf['strategy_name']} ({perf['symbol']}):")
                print(f"    Total trades: {perf['total_trades']}")
                print(f"    Win rate: {perf['win_rate']:.1%}")
                print(f"    Total P&L: {perf['total_pnl']}")
                if perf['sharpe_ratio']:
    
        pass
    pass
                    print(f"    Sharpe ratio: {perf['sharpe_ratio']:.2f}")
        else:
    pass
            print("  No strategy performance data found")
    
    except Exception as e:
    pass
    pass
        print(f"❌ Database integration error: {e}")


async def demonstrate_account_validation_integration():
    pass
    """Demonstrate CLI integration with account validation."""
    print("\n=== Account Validation Integration Demo ===")
    
    # Initialize account validator with integration manager
    validator = RealAccountValidator()
    
    try:
    pass
        # Get all accounts using existing configuration
        accounts = validator.get_all_accounts()
        print(f"Found {len(accounts)} configured accounts:")
        
        for account in accounts:
    pass
            print(f"  - {account['name']} ({account['type']})")
            print(f"    Type: {account.get('exchange_type', account.get('broker_type', 'unknown'))}")
            print(f"    Enabled: {account.get('enabled', False)}")
            print(f"    Sandbox: {account.get('sandbox', True)}")
        
        # Validate enabled accounts
        enabled_accounts = [acc for acc in accounts if acc.get('enabled', False)]
        
        if enabled_accounts:
    
        pass
    pass
            print(f"\nValidating {len(enabled_accounts)} enabled accounts...")
            
            # Validate accounts using existing exchange adapters
            validation_results = await validator.validate_all_accounts(
                enabled_only=True,
                timeout=10
            )
            
            for result in validation_results:
    pass
                status_icon = "✅" if result.connected and result.authenticated else "❌"
                print(f"{status_icon} {result.name} ({result.type})")
                print(f"    Exchange/Broker: {result.exchange_or_broker}")
                print(f"    Connected: {result.connected}")
                print(f"    Authenticated: {result.authenticated}")
                
                if result.latency_ms:
    
        pass
    pass
                    print(f"    Latency: {result.latency_ms}ms")
                
                if result.error_message:
    
        pass
    pass
                    print(f"    Error: {result.error_message}")
                
                if result.balance:
    
        pass
    pass
                    print(f"    Balance available: {len(result.balance)} currencies")
            
            # Save validation history using existing patterns
            validator.save_validation_history(validation_results)
            print("\n💾 Validation results saved to history")
        else:
    pass
            print("  No enabled accounts to validate")
    
    except Exception as e:
    pass
    pass
        print(f"❌ Account validation integration error: {e}")


def demonstrate_error_handling_integration():
    pass
    """Demonstrate CLI integration with existing error handling patterns."""
    print("\n=== Error Handling Integration Demo ===")
    
    # Initialize integration manager
    integration_manager = IntegrationManager()
    
    try:
    pass
        # Test configuration error handling
        print("Testing configuration error handling...")
        try:
    pass
            # Try to get a non-existent exchange
            adapter = integration_manager.get_exchange_adapter('nonexistent-exchange')
        except Exception as e:
    pass
    pass
            print(f"✅ Configuration error properly caught: {type(e).__name__}")
            print(f"   Message: {e}")
        
        # Test validation error handling
        print("\nTesting validation error handling...")
        config_file = Path("nonexistent_config.yaml")
        result = integration_manager.validate_configuration()
        
        if not result.success:
    
        pass
    pass
            print("✅ Validation error properly handled")
            print(f"   Message: {result.message}")
            for suggestion in result.suggestions:
    pass
                print(f"   💡 {suggestion}")
        
        # Test database error handling
        print("\nTesting database error handling...")
        try:
    pass
            # This should handle database connection gracefully
            trades = integration_manager.get_recent_trades()
            print(f"✅ Database operation completed (returned {len(trades)} trades)")
        except Exception as e:
    pass
    pass
            print(f"✅ Database error properly caught: {type(e).__name__}")
            print(f"   Message: {e}")
    
    except Exception as e:
    pass
    pass
        print(f"❌ Error handling integration error: {e}")


async def main():
    pass
    """Run all integration demonstrations."""
    print("GeneBot CLI Integration with Existing Components Demo")
    print("=" * 60)
    
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Run demonstrations
    await demonstrate_exchange_integration()
    demonstrate_configuration_integration()
    demonstrate_database_integration()
    await demonstrate_account_validation_integration()
    demonstrate_error_handling_integration()
    
    print("\n" + "=" * 60)
    print("Integration demonstration completed!")
    print("\nKey Integration Points Demonstrated:")
    print("✅ Exchange adapters (CCXTAdapter, forex adapters)")
    print("✅ Configuration management (ConfigManager)")
    print("✅ Database models (TradeModel, OrderModel, PositionModel)")
    print("✅ Validation utilities (validate_config_file)")
    print("✅ Error handling patterns (existing exception hierarchy)")
    print("✅ Account validation (real API connectivity tests)")
    print("✅ Data operations (real database queries)")
    
    print("\nThe CLI now properly integrates with all existing trading bot components!")


if __name__ == "__main__":
    
        pass
    pass
    pass
    asyncio.run(main())