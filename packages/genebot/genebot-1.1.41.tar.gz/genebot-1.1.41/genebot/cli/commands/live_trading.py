"""
Live Trading Validation CLI Command
===================================

Command for validating live trading functionality including exchange connectivity,
strategy execution, order management, and activity monitoring.
"""

import asyncio
import json
import logging
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any, List, Optional

from ..result import CLIResult
from .base import BaseCommand
from argparse import Namespace
from ...trading.live_validator import LiveTradingValidator
from ...config.manager import ConfigManager


async def run_live_trading_validation(args: Dict[str, Any]) -> CLIResult:
    """
    Run comprehensive live trading validation.
    
    Args:
        args: Command arguments containing validation options
        
    Returns:
        CLIResult: Result of the live trading validation
    """
    try:
        # Set up logging
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        
        # Initialize validator
        validator = LiveTradingValidator()
        
        # Parse arguments
        test_type = args.get('test_type', 'all')
        duration = args.get('duration', 300)  # 5 minutes default
        paper_trading = args.get('paper_trading', True)
        max_position_size = args.get('max_position_size', 0.01)  # 1% default
        output_file = args.get('output_file')
        verbose = args.get('verbose', False)
        
        logger.info(f"Starting live trading validation (duration: {duration}s)")
        if paper_trading:
            logger.info("Running in paper trading mode")
        else:
            logger.warning("Running with REAL MONEY - positions will be live!")
        
        results = {}
        
        # Run specific test types
        if test_type in ['all', 'connectivity']:
            logger.info("Testing live exchange connectivity...")
            results['exchange_connectivity'] = await validator.test_live_exchange_connectivity()
        
        if test_type in ['all', 'market_data']:
            logger.info("Testing real-time market data feeds...")
            results['market_data'] = await validator.test_real_market_data()
        
        if test_type in ['all', 'strategy']:
            logger.info("Testing strategy execution with live data...")
            results['strategy_execution'] = await validator.test_live_strategy_execution(
                duration=min(duration, 180)  # Max 3 minutes for strategy test
            )
        
        if test_type in ['all', 'orders']:
            logger.info("Testing order placement and management...")
            results['order_management'] = await validator.test_live_order_management(
                paper_trading=paper_trading,
                max_position_size=max_position_size
            )
        
        if test_type in ['all', 'monitoring']:
            logger.info("Testing trading activity monitoring...")
            results['activity_monitoring'] = await validator.test_live_activity_monitoring(
                duration=min(duration, 120)  # Max 2 minutes for monitoring test
            )
        
        if test_type == 'full_session':
            logger.info("Running full live trading session...")
            results = await validator.run_full_live_session(
                duration=duration,
                paper_trading=paper_trading,
                max_position_size=max_position_size
            )
        
        # Generate comprehensive report
        summary = validator.generate_live_trading_report(results)
        
        # Display results
        if verbose:
            print("\n" + "="*60)
            print("LIVE TRADING VALIDATION RESULTS")
            print("="*60)
            
            for suite_name, report in results.items():
                if hasattr(report, 'total_count'):  # ValidationReport object
                    print(f"\n{suite_name.upper().replace('_', ' ')} TESTS:")
                    print(f"  Total Tests: {report.total_count}")
                    print(f"  Passed: {report.passed_count}")
                    print(f"  Failed: {report.failed_count}")
                    print(f"  Success Rate: {report.success_rate:.1f}%")
                    print(f"  Duration: {report.duration:.2f}s")
                    
                    if report.failed_count > 0:
                        print("  Failed Tests:")
                        for result in report.results:
                            if result.status.value == "FAILED":
                                print(f"    - {result.test_name}: {result.message}")
                else:  # Dictionary result
                    print(f"\n{suite_name.upper().replace('_', ' ')}:")
                    for key, value in report.items():
                        print(f"  {key}: {value}")
            
            print(f"\nOVERALL SUMMARY:")
            print(f"  Total Tests: {summary.get('total_tests', 0)}")
            print(f"  Passed: {summary.get('passed_tests', 0)}")
            print(f"  Failed: {summary.get('failed_tests', 0)}")
            print(f"  Success Rate: {summary.get('success_rate', 0):.1f}%")
            print(f"  Live Trading Ready: {'YES' if summary.get('live_ready', False) else 'NO'}")
        else:
            # Compact output
            print(f"Live Trading Validation Complete")
            print(f"Tests: {summary.get('total_tests', 0)} | "
                  f"Passed: {summary.get('passed_tests', 0)} | "
                  f"Failed: {summary.get('failed_tests', 0)} | "
                  f"Success Rate: {summary.get('success_rate', 0):.1f}%")
            print(f"Live Trading Ready: {'✅ YES' if summary.get('live_ready', False) else '❌ NO'}")
        
        # Save detailed results if requested
        if output_file:
            output_path = Path(output_file)
            output_data = {
                'summary': summary,
                'detailed_results': results,
                'validation_timestamp': datetime.now().isoformat(),
                'test_parameters': {
                    'test_type': test_type,
                    'duration': duration,
                    'paper_trading': paper_trading,
                    'max_position_size': max_position_size
                }
            }
            
            with open(output_path, 'w') as f:
                json.dump(output_data, f, indent=2, default=str)
            
            print(f"\nDetailed results saved to: {output_path}")
        
        # Determine overall success
        overall_success = summary.get('live_ready', False)
        
        return CLIResult(
            success=overall_success,
            message=f"Live trading validation completed - {'Ready for live trading' if overall_success else 'Issues found, not ready for live trading'}",
            data=summary
        )
        
    except Exception as e:
        logger.error(f"Live trading validation failed: {str(e)}")
        return CLIResult(
            success=False,
            message=f"Live trading validation error: {str(e)}",
            data={"error": str(e)}
        )


async def run_live_trading_session(args: Dict[str, Any]) -> CLIResult:
    """
    Run an actual live trading session for validation.
    
    Args:
        args: Command arguments containing session options
        
    Returns:
        CLIResult: Result of the live trading session
    """
    try:
        # Set up logging
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        
        # Parse arguments
        duration = args.get('duration', 1800)  # 30 minutes default
        paper_trading = args.get('paper_trading', True)
        max_position_size = args.get('max_position_size', 0.01)
        strategies = args.get('strategies', [])
        accounts = args.get('accounts', [])
        output_file = args.get('output_file')
        
        if not paper_trading:
            # Require explicit confirmation for live trading
            confirmation = input("⚠️  WARNING: This will trade with REAL MONEY. Type 'CONFIRM' to proceed: ")
            if confirmation != 'CONFIRM':
                return CLIResult(
                    success=False,
                    message="Live trading session cancelled by user"
                )
        
        logger.info(f"Starting live trading session (duration: {duration}s)")
        logger.info(f"Mode: {'Paper Trading' if paper_trading else 'LIVE TRADING'}")
        logger.info(f"Max position size: {max_position_size * 100}%")
        
        # Initialize live validator
        validator = LiveTradingValidator()
        
        # Start the trading session (without orchestrator for now)
        session_results = await validator.run_monitored_trading_session(
            orchestrator=None,  # Skip orchestrator for validation
            duration=duration,
            paper_trading=paper_trading,
            strategies=strategies,
            accounts=accounts
        )
        
        # Generate session report
        report = validator.generate_session_report(session_results)
        
        # Display results
        print("\n" + "="*60)
        print("LIVE TRADING SESSION RESULTS")
        print("="*60)
        
        print(f"\nSession Summary:")
        print(f"  Duration: {report['session_duration']}")
        print(f"  Total Trades: {report['total_trades']}")
        print(f"  Winning Trades: {report['winning_trades']}")
        print(f"  Losing Trades: {report['losing_trades']}")
        print(f"  Win Rate: {report['win_rate']:.1f}%")
        print(f"  Total P&L: ${report['total_pnl']:.2f}")
        print(f"  Max Drawdown: ${report['max_drawdown']:.2f}")
        print(f"  Sharpe Ratio: {report['sharpe_ratio']:.2f}")
        
        print(f"\nSystem Performance:")
        print(f"  Uptime: {report['uptime_percentage']:.1f}%")
        print(f"  Orders Executed: {report['orders_executed']}")
        print(f"  Order Success Rate: {report['order_success_rate']:.1f}%")
        print(f"  Average Latency: {report['avg_latency']:.0f}ms")
        print(f"  Errors Encountered: {report['error_count']}")
        
        # Save detailed results if requested
        if output_file:
            output_path = Path(output_file)
            with open(output_path, 'w') as f:
                json.dump(session_results, f, indent=2, default=str)
            print(f"\nDetailed session data saved to: {output_path}")
        
        # Determine success based on session performance
        success = (
            report['error_count'] == 0 and
            report['order_success_rate'] >= 95.0 and
            report['uptime_percentage'] >= 99.0
        )
        
        return CLIResult(
            success=success,
            message=f"Live trading session completed - {'Successful' if success else 'Issues detected'}",
            data=report
        )
        
    except Exception as e:
        logger.error(f"Live trading session failed: {str(e)}")
        return CLIResult(
            success=False,
            message=f"Live trading session error: {str(e)}",
            data={"error": str(e)}
        )


class LiveTradingCommand(BaseCommand):
    """Live trading validation command."""
    
    def execute(self, args: Namespace) -> CLIResult:
        """Execute the live trading command."""
        # Handle subcommands
        subcommand = getattr(args, 'subcommand', 'validate')
        
        if subcommand == 'validate':
            return asyncio.run(run_live_trading_validation(vars(args)))
        elif subcommand == 'session':
            return asyncio.run(run_live_trading_session(vars(args)))
        else:
            # Default to validation
            return asyncio.run(run_live_trading_validation(vars(args)))