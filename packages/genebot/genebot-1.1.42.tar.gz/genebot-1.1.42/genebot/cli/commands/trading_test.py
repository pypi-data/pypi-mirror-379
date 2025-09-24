"""
Trading System Testing CLI Command
=================================

Command for running comprehensive trading system validation tests.
"""

import asyncio
import json
import logging
from pathlib import Path
from typing import Dict, Any

from ..result import CLIResult
from .base import BaseCommand
from argparse import Namespace
from ...trading.validation import TradingSystemValidator


async def run_trading_tests(args: Dict[str, Any]) -> CLIResult:
    pass
    """
    Run comprehensive trading system validation tests.
    
    Args:
    pass
        args: Command arguments containing test options
        
    Returns:
    pass
        CLIResult: Result of the trading tests
    """
    try:
    pass
        # Set up logging
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        
        # Initialize validator
        validator = TradingSystemValidator()
        
        # Determine which tests to run
        test_type = args.get('test_type', 'all')
        verbose = args.get('verbose', False)
        output_file = args.get('output_file')
        
        results = {}
        
        if test_type in ['all', 'connectivity']:
    
        pass
    pass
            logger.info("Running exchange connectivity tests...")
            results['exchange_connectivity'] = await validator.validate_exchange_connectivity()
        
        if test_type in ['all', 'strategy']:
    
        pass
    pass
            logger.info("Running strategy execution tests...")
            results['strategy_execution'] = await validator.validate_strategy_execution()
        
        if test_type in ['all', 'orders']:
    
        pass
    pass
            logger.info("Running order management tests...")
            results['order_management'] = await validator.validate_order_management()
        
        if test_type in ['all', 'monitoring']:
    
        pass
    pass
            logger.info("Running trading activity monitoring tests...")
            results['trading_monitoring'] = await validator.validate_trading_activity_monitoring()
        
        if test_type == 'all':
    
        pass
    pass
            logger.info("Running comprehensive validation...")
            results = await validator.run_comprehensive_validation()
        
        # Generate summary
        summary = validator.generate_summary_report(results)
        
        # Output results
        if verbose:
    
        pass
    pass
            print("\n" + "="*60)
            print("TRADING SYSTEM VALIDATION RESULTS")
            print("="*60)
            
            for suite_name, report in results.items():
    pass
                print(f"\n{suite_name.upper().replace('_', ' ')} TESTS:")
                print(f"  Total Tests: {report.total_count}")
                print(f"  Passed: {report.passed_count}")
                print(f"  Failed: {report.failed_count}")
                print(f"  Success Rate: {report.success_rate:.1f}%")
                print(f"  Duration: {report.duration:.2f}s")
                
                if report.failed_count > 0:
    
        pass
    pass
                    print("  Failed Tests:")
                    for result in report.results:
    pass
                        if result.status.value == "FAILED":
    
        pass
    pass
                            print(f"    - {result.test_name}: {result.message}")
            
            print(f"\nOVERALL SUMMARY:")
            print(f"  Total Tests: {summary['overall_summary']['total_tests']}")
            print(f"  Passed: {summary['overall_summary']['passed']}")
            print(f"  Failed: {summary['overall_summary']['failed']}")
            print(f"  Success Rate: {summary['overall_summary']['success_rate']:.1f}%")
        else:
    pass
            # Compact output
            print(f"Trading System Validation Complete")
            print(f"Tests: {summary['overall_summary']['total_tests']} | "
                  f"Passed: {summary['overall_summary']['passed']} | "
                  f"Failed: {summary['overall_summary']['failed']} | "
                  f"Success Rate: {summary['overall_summary']['success_rate']:.1f}%")
        
        # Save to file if requested
        if output_file:
    
        pass
    pass
            output_path = Path(output_file)
            output_data = {
                'summary': summary,
                'detailed_results': {name: report.to_dict() for name, report in results.items()}
            }
            
            with open(output_path, 'w') as f:
    pass
                json.dump(output_data, f, indent=2, default=str)
            
            print(f"\nDetailed results saved to: {output_path}")
        
        # Determine overall success
        overall_success = summary['overall_summary']['failed'] == 0
        
        return CLIResult(
            success=overall_success,
            message=f"Trading system validation completed with {summary['overall_summary']['success_rate']:.1f}% success rate",
            data=summary
        )
        
    except Exception as e:
    pass
    pass
        logger.error(f"Trading system validation failed: {str(e)}")
        return CLIResult(
            success=False,
            message=f"Trading system validation error: {str(e)}",
            data={"error": str(e)}
        )


class TradingTestCommand(BaseCommand):
    pass
    """Trading system validation test command."""
    
    def execute(self, args: Namespace) -> CLIResult:
    pass
        """Execute the trading test command."""
        return asyncio.run(run_trading_tests(vars(args)))