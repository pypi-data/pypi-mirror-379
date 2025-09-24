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
    pass
    from ..logging.factory import setup_global_config, get_logger
    from ..logging.config import get_default_config
    from ..logging.context import LogContext, set_context
except ImportError:
    pass
    pass
    # Fallback to basic logging if genebot logging is not available
    logging.basicConfig(level=logging.INFO)
    get_logger = lambda name: logging.getLogger(name)

# Global bot instance for signal handling
trading_bot = None

def setup_logging():
    pass
    """Setup logging for the trading bot runner."""
    try:
    pass
        # Use genebot's centralized logging if available
        config = get_default_config()
        
        # Override with environment variables if present
        if os.getenv('LOG_LEVEL'):
    
        pass
    pass
            config.level = os.getenv('LOG_LEVEL').upper()
        if os.getenv('LOG_DIRECTORY'):
    
        pass
    pass
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
    pass
    pass
        # Fallback to basic logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

def signal_handler(signum, frame):
    pass
    """Handle shutdown signals gracefully."""
    logger = get_logger('runner.signal_handler')
    logger.info(f"Received signal {signum}. Shutting down trading bot gracefully...")
    
    global trading_bot
    if trading_bot:
    
        pass
    pass
        if hasattr(trading_bot, 'stop'):
    
        pass
    pass
            if asyncio.iscoroutinefunction(trading_bot.stop):
    
        pass
    pass
                asyncio.create_task(trading_bot.stop())
            else:
    pass
                trading_bot.stop()
    sys.exit(0)

def setup_signal_handlers():
    pass
    """Setup signal handlers for graceful shutdown."""
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    if hasattr(signal, 'SIGHUP'):
    
        pass
    pass
        signal.signal(signal.SIGHUP, signal_handler)

def get_workspace_path() -> Path:
    pass
    """Get the workspace path from environment or current directory."""
    workspace_env = os.getenv('GENEBOT_WORKSPACE')
    if workspace_env:
    
        pass
    pass
        return Path(workspace_env)
    return Path.cwd()

def find_config_file(workspace_path: Path, config_arg: Optional[str] = None) -> Optional[Path]:
    pass
    """Find the configuration file to use."""
    if config_arg:
    
        pass
    pass
        config_path = Path(config_arg)
        if config_path.is_absolute():
    
        pass
    pass
            return config_path if config_path.exists() else None
        else:
    
        pass
    pass
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
    
        pass
    pass
        config_path = workspace_path / candidate
        if config_path.exists():
    
        pass
    pass
            return config_path
    
    return None

async def run_trading_bot(workspace_path: Path, config_file: Optional[str] = None, 
                         strategies: Optional[List[str]] = None, 
                         accounts: Optional[List[str]] = None):
    pass
    """Run the trading bot with the specified configuration."""
    global trading_bot
    logger = get_logger('runner.trading_bot')
    
    try:
    
        pass
    pass
        # Try to import the full trading bot implementation
        trading_bot_class = None
        MarketAwareTradingBot = None
        
        try:
    pass
            # First try to import from the workspace src directory
            from market_aware_trading_bot import MarketAwareTradingBot
            trading_bot_class = MarketAwareTradingBot
        except ImportError:
    pass
    pass
            try:
    pass
                # Try to import from installed package
                from ..core.trading_bot import TradingBot
                trading_bot_class = TradingBot
            except ImportError:
    pass
    pass
                return False
        
        # Find configuration file
        config_path = find_config_file(workspace_path, config_file)
        env_file = workspace_path / '.env' if (workspace_path / '.env').exists() else None
        
        if config_path:
    
        pass
    pass
            logger.info(f"Using configuration: {config_path}")
        else:
    pass
            logger.warning("No configuration file found, using defaults")
        
        if env_file:
    
        pass
    pass
            logger.info(f"Using environment file: {env_file}")
        
        # Initialize trading bot
        logger.info("Initializing trading bot...")
        
        if MarketAwareTradingBot and trading_bot_class == MarketAwareTradingBot:
    
        pass
    pass
            # Full implementation with config file support
            trading_bot = trading_bot_class(
                config_file=str(config_path) if config_path else None,
                env_file=str(env_file) if env_file else None
            )
        else:
    
        pass
    pass
            # Basic implementation
            config_dict = {}
            if strategies:
    
        pass
    pass
                config_dict['strategies'] = strategies
            if accounts:
    
        pass
    pass
                config_dict['accounts'] = accounts
            trading_bot = trading_bot_class(config=config_dict)
        
        logger.info("Trading bot initialized successfully")
        
        # Start the trading bot
        logger.info("Starting trading bot...")
        
        if hasattr(trading_bot, 'start'):
    
        pass
    pass
            if asyncio.iscoroutinefunction(trading_bot.start):
    
        pass
    pass
                success = await trading_bot.start()
            else:
    pass
                success = trading_bot.start()
        else:
    pass
            logger.warning("Trading bot does not have a start method")
            success = True
        
        if success:
    
        pass
    pass
            logger.info("Trading bot started successfully!")
            
            # Keep the bot running
            if hasattr(trading_bot, 'is_running'):
    
        pass
    pass
                while getattr(trading_bot, 'is_running', True):
    pass
                    await asyncio.sleep(1)
            else:
    pass
                # For basic implementations, just keep running
                logger.info("Trading bot is running. Press Ctrl+C to stop.")
                try:
    pass
                    while True:
    pass
                        await asyncio.sleep(1)
                except KeyboardInterrupt:
    pass
    pass
                    logger.info("Received keyboard interrupt")
        else:
    pass
            logger.error("Failed to start trading bot")
            return False
        
    except Exception as e:
    pass
    pass
        logger.exception(f"Error running trading bot: {e}")
        return False
    finally:
    pass
        if trading_bot and hasattr(trading_bot, 'stop'):
    
        pass
    pass
            logger.info("Stopping trading bot...")
            if asyncio.iscoroutinefunction(trading_bot.stop):
    
        pass
    pass
                await trading_bot.stop()
            else:
    pass
                trading_bot.stop()
            logger.info("Trading bot stopped")
    
    return True

def main():
    pass
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
    
        pass
    pass
        workspace_path = Path(args.workspace)
    else:
    pass
        workspace_path = get_workspace_path()
    
    logger.info(f"Using workspace: {workspace_path}")
    
    # Ensure workspace exists
    if not workspace_path.exists():
    
        pass
    pass
        logger.error(f"Workspace directory does not exist: {workspace_path}")
        sys.exit(1)
    
    # Change to workspace directory
    os.chdir(workspace_path)
    
    # Run the trading bot
    try:
    pass
        success = asyncio.run(run_trading_bot(
            workspace_path=workspace_path,
            config_file=args.config,
            strategies=args.strategies,
            accounts=args.accounts
        ))
        
        if not success:
    
        pass
    pass
            logger.error("Trading bot failed to run successfully")
            sys.exit(1)
        
    except KeyboardInterrupt:
    pass
    pass
        logger.info("Received keyboard interrupt, shutting down...")
    except Exception as e:
    pass
    pass
        logger.exception(f"Unexpected error: {e}")
        sys.exit(1)
    
    logger.info("GeneBot Trading Bot Runner finished")

if __name__ == "__main__":
    
        pass
    pass
    main()