#!/usr/bin/env python3
"""
Configuration Hot-Reloading Example

This example demonstrates the configuration hot-reloading capabilities
of the trading bot. It shows how to:
    pass
1. Enable configuration hot-reloading
2. Monitor configuration file changes
3. Handle automatic reloading with validation
4. Use callbacks to respond to configuration changes
5. Manually trigger configuration reloads

Run this example and then modify configuration files to see hot-reloading in action.
"""

import sys
import signal
import asyncio
from pathlib import Path
from datetime import datetime

# Add src directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config.enhanced_manager import (
    manual_global_reload
)

# Global flag for graceful shutdown
running = True


def signal_handler(signum, frame):
    
        pass
    pass
    """Handle shutdown signals gracefully."""
    global running
    print(f"\nReceived signal {signum}. Shutting down gracefully...")
    running = False


def setup_signal_handlers():
    pass
    """Setup signal handlers for graceful shutdown."""
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    if hasattr(signal, 'SIGHUP'):
    
        pass
    pass
        signal.signal(signal.SIGHUP, signal_handler)


def create_example_config_files():
    pass
    """Create example configuration files for demonstration."""
    config_dir = Path('config')
    config_dir.mkdir(exist_ok=True)
    
    # Create example bot configuration
    bot_config = {
        'app_name': 'HotReloadDemo',
        'version': '1.0.0',
        'debug': False,
        'dry_run': True,
        'base_currency': 'USDT',
        'exchanges': {
            'demo_exchange': {
                'exchange_type': 'demo',
                'api_key': 'demo_key',
                'api_secret': 'demo_secret',
                'enabled': True,
                'sandbox': True
            }
        },
        'strategies': {
            'demo_strategy': {
                'strategy_type': 'moving_average',
                'enabled': True,
                'symbols': ['BTC/USDT', 'ETH/USDT'],
                'timeframe': '1h',
                'parameters': {
                    'fast_period': 10,
                    'slow_period': 20
                }
            }
        },
        'risk': {
            'max_position_size': 0.1,
            'max_daily_loss': 0.05,
            'max_drawdown': 0.15,
            'stop_loss_percentage': 0.02,
            'max_open_positions': 5
        },
        'database': {
            'database_type': 'sqlite',
            'database_url': 'sqlite:///hot_reload_demo.db'
        },
        'logging': {
            'log_level': 'INFO',
            'log_format': 'standard'
        }
    }
    
    # Create example accounts configuration
    accounts_config = {
        'exchanges': {
            'demo_exchange': {
                'exchange_type': 'demo',
                'api_key': 'demo_key',
                'api_secret': 'demo_secret',
                'enabled': True,
                'sandbox': True,
                'rate_limit': 1200,
                'timeout': 30
            }
        }
    }
    
    # Create example environment file
    env_content = """# Configuration Hot-Reload Demo Environment Variables
DEBUG=false
DRY_RUN=true
LOG_LEVEL=INFO
ENABLE_CONFIG_HOT_RELOAD=true

# Demo API credentials (not real)
DEMO_API_KEY=demo_key_from_env
DEMO_API_SECRET=demo_secret_from_env

# Risk management overrides
RISK_MAX_POSITION_SIZE=0.1
RISK_MAX_DAILY_LOSS=0.05
"""
    
    # Write configuration files
    import yaml
    
    bot_config_file = config_dir / 'trading_bot_config.yaml'
        yaml.dump(bot_config, f, default_flow_style=False, indent=2)
    
    accounts_config_file = config_dir / 'accounts.yaml'
    with open(accounts_config_file, 'w') as f:
    pass
        yaml.dump(accounts_config, f, default_flow_style=False, indent=2)
    
    env_file = Path('.env')
    with open(env_file, 'w') as f:
    pass
        f.write(env_content)
    
    print("✓ Created example configuration files:")
    print(f"  • {bot_config_file}")
    print(f"  • {accounts_config_file}")
    print(f"  • {env_file}")
    print()
    
    return bot_config_file, accounts_config_file, env_file


def print_configuration_summary(config):
    pass
    """Print a summary of the current configuration."""
    print("Current Configuration Summary:")
    print("=" * 40)
    print(f"App Name: {config.app_name}")
    print(f"Version: {config.version}")
    print(f"Debug Mode: {config.debug}")
    print(f"Dry Run: {config.dry_run}")
    print(f"Base Currency: {config.base_currency}")
    
    print(f"\nExchanges ({len(config.exchanges)}):")
    for name, exchange in config.exchanges.items():
    pass
        status = "ENABLED" if exchange.enabled else "DISABLED"
        print(f"  • {name}: {exchange.exchange_type} ({status})")
    
    print(f"\nStrategies ({len(config.strategies)}):")
    for name, strategy in config.strategies.items():
    pass
        status = "ENABLED" if strategy.enabled else "DISABLED"
        symbols = ', '.join(strategy.symbols) if strategy.symbols else 'None'
        print(f"  • {name}: {strategy.strategy_type} ({status}) - {symbols}")
    
    print(f"\nRisk Management:")
    print(f"  • Max Position Size: {config.risk.max_position_size}")
    print(f"  • Max Daily Loss: {config.risk.max_daily_loss}")
    print(f"  • Stop Loss: {config.risk.stop_loss_percentage}")
    print(f"  • Max Open Positions: {config.risk.max_open_positions}")
    
    print(f"\nLogging:")
    print(f"  • Level: {config.logging.log_level}")
    print(f"  • Format: {config.logging.log_format}")
    print()


def print_hot_reload_status():
    pass
    """Print the current hot-reload status."""
    status = get_global_hot_reload_status()
    
    print("Hot-Reload Status:")
    print("-" * 20)
    print(f"Enabled: {status.get('enabled', False)}")
    print(f"Available: {status.get('available', False)}")
    print(f"Running: {status.get('is_running', False)}")
    
    if status.get('enabled'):
    
        pass
    pass
        print(f"Auto-reload: {status.get('auto_reload_enabled', False)}")
        print(f"Validation Required: {status.get('validation_required', False)}")
        print(f"Monitored Files: {len(status.get('monitored_files', []))}")
        
        if status.get('monitored_files'):
    
        pass
    pass
            print("  Files being monitored:")
            for file_path in status['monitored_files']:
    pass
                print(f"    • {file_path}")
        
        print(f"Total Reloads: {status.get('reload_count', 0)}")
        print(f"Successful: {status.get('successful_reloads', 0)}")
        print(f"Failed: {status.get('failed_reloads', 0)}")
        
        if status.get('last_reload_time'):
    
        pass
    pass
            print(f"Last Reload: {status['last_reload_time']}")
    else:
    pass
        reason = status.get('reason', 'Unknown')
        print(f"Reason: {reason}")
    
    print()


def setup_hot_reload_callbacks(config_manager):
    pass
    """Setup callbacks to monitor configuration changes."""
    
    def on_config_reloaded(result):
    pass
        """Handle configuration reload events."""
        timestamp = datetime.now().strftime('%H:%M:%S')
        
        if result.success:
    
        pass
    pass
            print(f"\n🔄 [{timestamp}] Configuration automatically reloaded!")
            
            if result.changes:
    
        pass
    pass
                print("Changes detected:")
                for change in result.changes:
    pass
                    print(f"  • {change.file_path}: {change.change_type}")
            
            if result.warnings:
    
        pass
    pass
                print("Warnings:")
                for warning in result.warnings:
    pass
                    print(f"  ⚠️  {warning}")
            
            # Print updated configuration summary
            try:
    pass
                updated_config = config_manager.get_config()
                print_configuration_summary(updated_config)
            except Exception as e:
    pass
    pass
                print(f"Error getting updated configuration: {e}")
        else:
    pass
            print(f"\n❌ [{timestamp}] Configuration reload failed!")
            
            if result.errors:
    
        pass
    pass
                print("Errors:")
                for error in result.errors:
    pass
                    print(f"  • {error}")
            
            if result.rollback_performed:
    
        pass
    pass
                print("🔄 Configuration rollback was performed")
        
        print("=" * 60)
        print("Monitoring for changes... (Ctrl+C to exit)")
        print("Try modifying configuration files to see hot-reloading in action!")
        print()
    
    def on_config_changed(change):
    
        pass
    pass
        """Handle configuration file change events."""
        timestamp = datetime.now().strftime('%H:%M:%S')
        print(f"\n📁 [{timestamp}] File {change.change_type}: {change.file_path}")
    
    # Add callbacks
    config_manager.add_reload_callback(on_config_reloaded)
    config_manager.add_change_callback(on_config_changed)
    
    return on_config_reloaded, on_config_changed


async def interactive_demo():
    pass
    """Run an interactive demonstration of hot-reloading."""
    print("Configuration Hot-Reload Interactive Demo")
    print("=" * 50)
    print()
    
    while running:
    pass
        print("Available commands:")
        print("  1. Show current configuration")
        print("  2. Show hot-reload status")
        print("  3. Manually trigger reload")
        print("  4. Modify configuration (guided)")
        print("  5. Exit")
        print()
        
        try:
    
        pass
    pass
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '1':
    
        pass
    pass
                print("\n" + "=" * 60)
                try:
    pass
                    config_manager = get_enhanced_config_manager()
                    config = config_manager.get_config()
                    print_configuration_summary(config)
                except Exception as e:
    pass
    pass
                    print(f"Error getting configuration: {e}")
                print("=" * 60)
            
            elif choice == '2':
    
        pass
    pass
                print("\n" + "=" * 60)
                print_hot_reload_status()
                print("=" * 60)
            
            elif choice == '3':
    
        pass
    pass
                print("\nTriggering manual configuration reload...")
                result = manual_global_reload()
                if result:
    
        pass
    pass
                    if result.success:
    
        pass
    pass
                        print("✓ Configuration reloaded successfully")
                        if result.warnings:
    
        pass
    pass
                            for warning in result.warnings:
    pass
                                print(f"⚠️  Warning: {warning}")
                    else:
    pass
                        print("❌ Configuration reload failed")
                        for error in result.errors:
    pass
                            print(f"Error: {error}")
                else:
    pass
                    print("Hot-reloader not available")
            
            elif choice == '4':
    
        pass
    pass
                print("\nGuided Configuration Modification")
                print("-" * 35)
                print("This will help you modify configuration files to see hot-reloading.")
                print()
                
                modify_choice = input("What would you like to modify?\n"
                                    "  a) App name and version\n"
                                    "  b) Debug mode\n"
                                    "  c) Risk settings\n"
                                    "  d) Add a new strategy\n"
                                    "Enter choice (a-d): ").strip().lower()
                
                if modify_choice == 'a':
    
        pass
    pass
                    await modify_app_info()
                elif modify_choice == 'b':
    
        pass
    pass
                    await modify_debug_mode()
                elif modify_choice == 'c':
    
        pass
    pass
                    await modify_risk_settings()
                elif modify_choice == 'd':
    
        pass
    pass
                    await add_new_strategy()
                else:
    pass
                    print("Invalid choice")
            
            elif choice == '5':
    
        pass
    pass
                print("Exiting demo...")
                break
            
            else:
    pass
                print("Invalid choice. Please enter 1-5.")
            
            print()
            
        except KeyboardInterrupt:
    pass
    pass
            print("\nExiting demo...")
            break
        except EOFError:
    pass
    pass
            print("\nExiting demo...")
            break
        except Exception as e:
    pass
    pass
            print(f"Error: {e}")


async def modify_app_info():
    
        pass
    pass
    """Modify app name and version."""
    import yaml
    
    config_file = Path('config/trading_bot_config.yaml')
    if not config_file.exists():
    
        pass
    pass
        return
    
    try:
    pass
        with open(config_file, 'r') as f:
    pass
            config = yaml.safe_load(f)
        
        print(f"Current app name: {config.get('app_name', 'Unknown')}")
        print(f"Current version: {config.get('version', 'Unknown')}")
        
        new_name = input("Enter new app name (or press Enter to keep current): ").strip()
        new_version = input("Enter new version (or press Enter to keep current): ").strip()
        
        if new_name:
    
        pass
    pass
            config['app_name'] = new_name
        if new_version:
    
        pass
    pass
            config['version'] = new_version
        
        with open(config_file, 'w') as f:
    pass
            yaml.dump(config, f, default_flow_style=False, indent=2)
        
        print(f"✓ Updated {config_file}")
        print("Watch for automatic reload...")
        
    except Exception as e:
    pass
    pass
        print(f"Error modifying configuration: {e}")


async def modify_debug_mode():
    
        pass
    pass
    """Toggle debug mode."""
    import yaml
    
    config_file = Path('config/trading_bot_config.yaml')
    if not config_file.exists():
    
        pass
    pass
        return
    
    try:
    pass
        with open(config_file, 'r') as f:
    pass
            config = yaml.safe_load(f)
        
        current_debug = config.get('debug', False)
        new_debug = not current_debug
        
        config['debug'] = new_debug
        
        with open(config_file, 'w') as f:
    pass
            yaml.dump(config, f, default_flow_style=False, indent=2)
        
        print(f"✓ Debug mode changed from {current_debug} to {new_debug}")
        print("Watch for automatic reload...")
        
    except Exception as e:
    pass
    pass
async def modify_risk_settings():
    
        pass
    pass
    """Modify risk management settings."""
    import yaml
    
    config_file = Path('config/trading_bot_config.yaml')
    if not config_file.exists():
    
        pass
    pass
        return
    
    try:
    pass
        with open(config_file, 'r') as f:
    pass
            config = yaml.safe_load(f)
        
        risk = config.get('risk', {})
        
        print("Current risk settings:")
        print(f"  Max Position Size: {risk.get('max_position_size', 'Unknown')}")
        print(f"  Max Daily Loss: {risk.get('max_daily_loss', 'Unknown')}")
        print(f"  Stop Loss %: {risk.get('stop_loss_percentage', 'Unknown')}")
        
        new_pos_size = input("Enter new max position size (0.01-1.0, or Enter to skip): ").strip()
        new_daily_loss = input("Enter new max daily loss (0.01-1.0, or Enter to skip): ").strip()
        new_stop_loss = input("Enter new stop loss % (0.01-0.1, or Enter to skip): ").strip()
        
        if new_pos_size:
    
        pass
    pass
            try:
    pass
                risk['max_position_size'] = float(new_pos_size)
            except ValueError:
    pass
    pass
                print("Invalid position size value")
                return
        
        if new_daily_loss:
    
        pass
    pass
            try:
    pass
                risk['max_daily_loss'] = float(new_daily_loss)
            except ValueError:
    pass
    pass
                print("Invalid daily loss value")
                return
        
        if new_stop_loss:
    
        pass
    pass
            try:
    pass
                risk['stop_loss_percentage'] = float(new_stop_loss)
            except ValueError:
    pass
    pass
                print("Invalid stop loss value")
                return
        
        config['risk'] = risk
        
        with open(config_file, 'w') as f:
    pass
            yaml.dump(config, f, default_flow_style=False, indent=2)
        
        print(f"✓ Updated risk settings in {config_file}")
        print("Watch for automatic reload...")
        
    except Exception as e:
    pass
    pass
        print(f"Error modifying configuration: {e}")


async def add_new_strategy():
    pass
    """Add a new strategy to the configuration."""
    import yaml
    
    config_file = Path('config/trading_bot_config.yaml')
    if not config_file.exists():
    
        pass
    pass
        return
    
    try:
    pass
        with open(config_file, 'r') as f:
    pass
            config = yaml.safe_load(f)
        
        strategies = config.get('strategies', {})
        
        strategy_name = input("Enter strategy name: ").strip()
        if not strategy_name:
    
        pass
    pass
            print("Strategy name is required")
            return
        
        strategy_type = input("Enter strategy type (moving_average, rsi, momentum): ").strip()
        if not strategy_type:
    
        pass
    pass
            strategy_type = 'moving_average'
        
        symbols = input("Enter symbols (comma-separated, e.g., BTC/USDT,ETH/USDT): ").strip()
        symbol_list = [s.strip() for s in symbols.split(',')] if symbols else ['BTC/USDT']
        
        new_strategy = {
            'strategy_type': strategy_type,
            'enabled': True,
            'symbols': symbol_list,
            'timeframe': '1h',
            'parameters': {
                'period': 14
            }
        }
        
        strategies[strategy_name] = new_strategy
        config['strategies'] = strategies
        
        with open(config_file, 'w') as f:
    pass
            yaml.dump(config, f, default_flow_style=False, indent=2)
        
        print(f"✓ Added new strategy '{strategy_name}' to {config_file}")
        print("Watch for automatic reload...")
        
    except Exception as e:
    pass
    pass
        print(f"Error adding strategy: {e}")


async def main():
    pass
    """Main function."""
    setup_signal_handlers()
    
    print("Configuration Hot-Reloading Example")
    print("=" * 50)
    print()
    
    # Check if configuration files exist, create them if not
    config_dir = Path('config')
    bot_config_file = config_dir / 'trading_bot_config.yaml'
    
    if not bot_config_file.exists():
    
        pass
    pass
        print("Creating example configuration files...")
        create_example_config_files()
    else:
    pass
        print("Using existing configuration files")
        print()
    
    try:
    pass
        # Initialize configuration manager with hot-reloading enabled
        print("Initializing configuration manager with hot-reloading...")
        config_manager = get_enhanced_config_manager(
            use_unified_loading=True,
            enable_hot_reload=True,
            auto_reload=True,
            validation_required=True
        )
        
        # Load initial configuration
        print("Loading initial configuration...")
        config = config_manager.get_config()
        print_configuration_summary(config)
        
        # Start hot-reloader
        print("Starting configuration hot-reloader...")
        success = start_global_hot_reloader(
            enable_hot_reload=True,
            auto_reload=True,
            validation_required=True
        )
        
        if success:
    
        pass
    pass
            print("✓ Hot-reloader started successfully")
            print_hot_reload_status()
            
            # Setup callbacks
            print("Setting up hot-reload callbacks...")
            reload_callback, change_callback = setup_hot_reload_callbacks(config_manager)
            
            print("=" * 60)
            print("Configuration hot-reloading is now active!")
            print("=" * 60)
            print()
            
            # Run interactive demo
            await interactive_demo()
            
        else:
    pass
            print("❌ Failed to start hot-reloader")
            print("This might be due to missing dependencies (watchdog)")
            print("Install with: pip install watchdog")
    
    except KeyboardInterrupt:
    pass
    pass
        print("\nShutdown requested...")
    except Exception as e:
    pass
    pass
        print(f"Error: {e}")
        import traceback
    finally:
    pass
        # Cleanup
        print("✓ Hot-reloader stopped")
        print("Example completed.")


if __name__ == "__main__":
    
        pass
    pass
    asyncio.run(main())