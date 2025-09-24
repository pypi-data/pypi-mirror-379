#!/usr/bin/env python3
"""
GeneBot Trading Bot Runner
=========================

This module provides the entry point for running the GeneBot trading bot
from the installed package, without requiring main.py in the user's workspace.

This runner is used by the CLI to start trading bot instances and ensures
that the bot runs from the packaged build rather than workspace files.
"""

import asyncio
import os
import sys
import signal
import argparse
import logging
from pathlib import Path
from typing import Optional, List
from datetime import datetime

# Import the trading bot functionality from the installed package
try:
    from ..logging.factory import setup_global_config, get_logger
    from ..logging.config import get_default_config
    from ..logging.context import LogContext, set_context
except ImportError:
    # Fallback to basic logging if genebot logging is not available
    logging.basicConfig(level=logging.INFO)
    get_logger = lambda name: logging.getLogger(name)

# Global bot instance for signal handling
trading_bot = None

def setup_logging():
    """Setup logging for the trading bot runner."""
    try:
        # Use genebot's centralized logging if available
        config = get_default_config()
        
        # Override with environment variables if present
        if os.getenv('LOG_LEVEL'):
            config.level = os.getenv('LOG_LEVEL').upper()
        if os.getenv('LOG_DIRECTORY'):
            config.log_directory = Path(os.getenv('LOG_DIRECTORY'))
        
        setup_global_config(config)
        
        # Set application context
        app_context = LogContext(
            component="runner",
            operation="startup",
            session_id=f"runner_{int(datetime.now().timestamp())}"
        )
        set_context(app_context)
    except ImportError:
        # Fallback to basic logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

def signal_handler(signum, frame):
    """Handle shutdown signals gracefully."""
    logger = get_logger('runner.signal_handler')
    logger.info(f"Received signal {signum}. Shutting down trading bot gracefully...")
    
    global trading_bot
    if trading_bot:
        if hasattr(trading_bot, 'stop'):
            if asyncio.iscoroutinefunction(trading_bot.stop):
                asyncio.create_task(trading_bot.stop())
            else:
                trading_bot.stop()
    sys.exit(0)

def setup_signal_handlers():
    """Setup signal handlers for graceful shutdown."""
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    if hasattr(signal, 'SIGHUP'):
        signal.signal(signal.SIGHUP, signal_handler)

def get_workspace_path() -> Path:
    """Get the workspace path from environment or current directory."""
    workspace_env = os.getenv('GENEBOT_WORKSPACE')
    if workspace_env:
        return Path(workspace_env)
    return Path.cwd()

def find_config_file(workspace_path: Path, config_arg: Optional[str] = None) -> Optional[Path]:
    """Find the configuration file to use."""
    if config_arg:
        config_path = Path(config_arg)
        if config_path.is_absolute():
            return config_path if config_path.exists() else None
        else:
            # Relative to workspace
            config_path = workspace_path / config_arg
            return config_path if config_path.exists() else None
    
    # Auto-discover configuration files in workspace
    config_candidates = [
        'config/multi_market_config.yaml',
        'config/trading_bot_config.yaml',
        'config/bot_config.yaml',
        'trading_bot_config.yaml',
        'config.yaml',
        'config.yml'
    ]
    
    for candidate in config_candidates:
        config_path = workspace_path / candidate
        if config_path.exists():
            return config_path
    
    return None

async def run_trading_bot(workspace_path: Path, config_file: Optional[str] = None, 
                         strategies: Optional[List[str]] = None, 
                         accounts: Optional[List[str]] = None):
    """Run the trading bot with the specified configuration."""
    global trading_bot
    logger = get_logger('runner.trading_bot')
    
    try:
        # Try to import the full trading bot implementation
        trading_bot_class = None
        MarketAwareTradingBot = None
        
        try:
            # First try to import from the workspace src directory
            sys.path.insert(0, str(workspace_path / 'src'))
            from market_aware_trading_bot import MarketAwareTradingBot
            logger.info("Using workspace trading bot implementation")
            trading_bot_class = MarketAwareTradingBot
        except ImportError:
            try:
                # Try to import from installed package
                from ..core.trading_bot import TradingBot
                logger.info("Using packaged trading bot implementation")
                trading_bot_class = TradingBot
            except ImportError:
                logger.error("No trading bot implementation found")
                return False
        
        # Find configuration file
        config_path = find_config_file(workspace_path, config_file)
        env_file = workspace_path / '.env' if (workspace_path / '.env').exists() else None
        
        if config_path:
            logger.info(f"Using configuration: {config_path}")
        else:
            logger.warning("No configuration file found, using defaults")
        
        if env_file:
            logger.info(f"Using environment file: {env_file}")
        
        # Initialize trading bot
        logger.info("Initializing trading bot...")
        
        if MarketAwareTradingBot and trading_bot_class == MarketAwareTradingBot:
            # Full implementation with config file support
            trading_bot = trading_bot_class(
                config_file=str(config_path) if config_path else None,
                env_file=str(env_file) if env_file else None
            )
        else:
            # Basic implementation
            config_dict = {}
            if strategies:
                config_dict['strategies'] = strategies
            if accounts:
                config_dict['accounts'] = accounts
            trading_bot = trading_bot_class(config=config_dict)
        
        logger.info("Trading bot initialized successfully")
        
        # Start the trading bot
        logger.info("Starting trading bot...")
        
        if hasattr(trading_bot, 'start'):
            if asyncio.iscoroutinefunction(trading_bot.start):
                success = await trading_bot.start()
            else:
                success = trading_bot.start()
        else:
            logger.warning("Trading bot does not have a start method")
            success = True
        
        if success:
            logger.info("Trading bot started successfully!")
            
            # Keep the bot running
            if hasattr(trading_bot, 'is_running'):
                while getattr(trading_bot, 'is_running', True):
                    await asyncio.sleep(1)
            else:
                # For basic implementations, just keep running
                logger.info("Trading bot is running. Press Ctrl+C to stop.")
                try:
                    while True:
                        await asyncio.sleep(1)
                except KeyboardInterrupt:
                    logger.info("Received keyboard interrupt")
        else:
            logger.error("Failed to start trading bot")
            return False
        
    except Exception as e:
        logger.exception(f"Error running trading bot: {e}")
        return False
    finally:
        if trading_bot and hasattr(trading_bot, 'stop'):
            logger.info("Stopping trading bot...")
            if asyncio.iscoroutinefunction(trading_bot.stop):
                await trading_bot.stop()
            else:
                trading_bot.stop()
            logger.info("Trading bot stopped")
    
    return True

def main():
    """Main entry point for the trading bot runner."""
    parser = argparse.ArgumentParser(description='GeneBot Trading Bot Runner')
    parser.add_argument('--config', help='Configuration file path')
    parser.add_argument('--strategies', nargs='+', help='Strategies to enable')
    parser.add_argument('--accounts', nargs='+', help='Accounts to use')
    parser.add_argument('--workspace', help='Workspace directory path')
    
    args = parser.parse_args()
    
    # Setup logging and signal handlers
    setup_logging()
    setup_signal_handlers()
    
    logger = get_logger('runner.main')
    logger.info("GeneBot Trading Bot Runner starting...")
    
    # Determine workspace path
    if args.workspace:
        workspace_path = Path(args.workspace)
    else:
        workspace_path = get_workspace_path()
    
    logger.info(f"Using workspace: {workspace_path}")
    
    # Ensure workspace exists
    if not workspace_path.exists():
        logger.error(f"Workspace directory does not exist: {workspace_path}")
        sys.exit(1)
    
    # Change to workspace directory
    os.chdir(workspace_path)
    
    # Run the trading bot
    try:
        success = asyncio.run(run_trading_bot(
            workspace_path=workspace_path,
            config_file=args.config,
            strategies=args.strategies,
            accounts=args.accounts
        ))
        
        if not success:
            logger.error("Trading bot failed to run successfully")
            sys.exit(1)
        
    except KeyboardInterrupt:
        logger.info("Received keyboard interrupt, shutting down...")
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        sys.exit(1)
    
    logger.info("GeneBot Trading Bot Runner finished")

if __name__ == '__main__':
    main()