#!/usr/bin/env python3
"""
Command Test Runner
==================

Main CLI script to run comprehensive command testing with various options
for selective testing, progress reporting, and result generation.
"""

import sys
import argparse
import time
import signal
from pathlib import Path
from typing import List, Optional, Dict, Any
from dataclasses import dataclass
from enum import Enum

# Add the project root to the path so we can import genebot modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from genebot.cli.testing.automated_test_suite import (
    AutomatedTestSuite, TestSuiteConfig, TestType, TestPriority, TestSuiteResults
)
from genebot.cli.testing.reporter import TestReporter, ReportConfig, ReportFormat
from genebot.cli.context import CLIContext
from genebot.cli.utils.logger import CLILogger
from genebot.cli.utils.error_handler import CLIErrorHandler
from genebot.cli.discovery.discovery import CommandDiscovery


class ExitCode(Enum):
    """Exit codes for the test runner"""
    SUCCESS = 0
    PARTIAL_FAILURE = 1
    COMPLETE_FAILURE = 2
    INTERRUPTED = 3
    CONFIGURATION_ERROR = 4


@dataclass
class TestRunnerConfig:
    """Configuration for the test runner"""
    test_types: List[TestType]
    command_filter: Optional[List[str]] = None
    exclude_commands: Optional[List[str]] = None
    parallel_execution: bool = True
    max_workers: int = 4
    timeout_per_test: int = 30
    timeout_per_command: int = 300
    stop_on_first_failure: bool = False
    output_directory: Optional[Path] = None
    report_formats: List[ReportFormat] = None
    verbose: bool = False
    quiet: bool = False
    show_progress: bool = True
    generate_detailed_reports: bool = True
    
    def __post_init__(self):
        if self.report_formats is None:
            self.report_formats = [ReportFormat.TEXT, ReportFormat.JSON]
        if self.output_directory is None:
            self.output_directory = Path("test_reports")


class ProgressReporter:
    """Reports progress during test execution"""
    
    def __init__(self, total_commands: int, show_progress: bool = True, verbose: bool = False):
        self.total_commands = total_commands
        self.show_progress = show_progress
        self.verbose = verbose
        self.completed_commands = 0
        self.start_time = time.time()
        self.last_update = 0
    
    def update_progress(self, test_suite: AutomatedTestSuite):
        """Update progress display"""
        if not self.show_progress:
            return
        
        current_time = time.time()
        # Update every 2 seconds or when verbose
        if current_time - self.last_update < 2 and not self.verbose:
            return
        
        progress = test_suite.get_current_progress()
        elapsed = current_time - self.start_time
        
        if progress['total_tests'] > 0:
            completion_rate = progress['completed_tests'] / progress['total_tests']
            eta = (elapsed / completion_rate - elapsed) if completion_rate > 0 else 0
            
            print(f"\rProgress: {progress['completed_tests']}/{progress['total_tests']} tests "
                  f"({progress['success_rate']:.1f}% success) - "
                  f"ETA: {eta:.0f}s", end='', flush=True)
        
        self.last_update = current_time
    
    def finish_progress(self, results: TestSuiteResults):
        """Finish progress reporting"""
        if self.show_progress:
            elapsed = time.time() - self.start_time
            print(f"\nCompleted: {results.passed_tests}/{results.total_tests} tests passed "
                  f"({results.success_rate:.1f}%) in {elapsed:.1f}s")


class CommandTestRunner:
    """Main command test runner"""
    
    def __init__(self, config: TestRunnerConfig):
        self.config = config
        self.context = CLIContext(config_path=Path("config"))
        self.logger = CLILogger()
        self.error_handler = CLIErrorHandler()
        
        # Configure logger based on verbosity
        if config.quiet:
            self.logger = CLILogger(level="ERROR")
        elif config.verbose:
            self.logger = CLILogger(level="DEBUG", verbose=True)
        else:
            self.logger = CLILogger(level="INFO")
        
        # Initialize components
        self.test_suite = AutomatedTestSuite(self.context, self.logger, self.error_handler)
        self.discovery = CommandDiscovery(self.context, self.logger, self.error_handler)
        self.reporter = TestReporter(ReportConfig(
            formats=config.report_formats,
            output_directory=config.output_directory,
            include_execution_details=config.generate_detailed_reports
        ))
        
        # Set up signal handling for graceful shutdown
        self._interrupted = False
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
    
    def _signal_handler(self, signum, frame):
        """Handle interrupt signals"""
        print("\nReceived interrupt signal. Stopping test execution...")
        self._interrupted = True
        self.test_suite.stop_execution()
    
    def run_tests(self) -> ExitCode:
        """Run the test suite with configured options"""
        try:
            # Discover commands first
            if not self.config.quiet:
                print("Discovering commands...")
            
            commands = self.discovery.discover_commands()
            
            # Apply filters
            filtered_commands = self._apply_command_filters(commands)
            
            if not filtered_commands:
                print("No commands to test after applying filters.")
                return ExitCode.CONFIGURATION_ERROR
            
            if not self.config.quiet:
                print(f"Testing {len(filtered_commands)} commands with {len(self.config.test_types)} test types")
                if self.config.verbose:
                    print(f"Commands: {', '.join(filtered_commands.keys())}")
                    print(f"Test types: {', '.join(t.value for t in self.config.test_types)}")
            
            # Create test suite configuration
            suite_config = TestSuiteConfig(
                test_types=self.config.test_types,
                command_filter=list(filtered_commands.keys()) if filtered_commands else None,
                exclude_commands=self.config.exclude_commands,
                parallel_execution=self.config.parallel_execution,
                max_workers=self.config.max_workers,
                timeout_per_test=self.config.timeout_per_test,
                timeout_per_command=self.config.timeout_per_command,
                stop_on_first_failure=self.config.stop_on_first_failure,
                generate_detailed_reports=self.config.generate_detailed_reports
            )
            
            # Set up progress reporting
            progress_reporter = ProgressReporter(
                len(filtered_commands),
                self.config.show_progress and not self.config.quiet,
                self.config.verbose
            )
            
            # Run tests
            if not self.config.quiet:
                print("Starting test execution...")
            
            start_time = time.time()
            
            # Run tests with progress monitoring
            if self.config.show_progress and not self.config.quiet:
                results = self._run_tests_with_progress(suite_config, progress_reporter)
            else:
                results = self.test_suite.run_all_command_tests(suite_config)
            
            execution_time = time.time() - start_time
            
            if self._interrupted:
                print("Test execution was interrupted.")
                return ExitCode.INTERRUPTED
            
            # Generate reports
            if not self.config.quiet:
                print("Generating reports...")
            
            self._generate_reports(results, filtered_commands)
            
            # Print summary
            self._print_summary(results, execution_time)
            
            # Determine exit code
            return self._determine_exit_code(results)
            
        except KeyboardInterrupt:
            print("\nTest execution interrupted by user.")
            return ExitCode.INTERRUPTED
        except Exception as e:
            print(f"Test execution failed: {e}")
            if self.config.verbose:
                import traceback
                traceback.print_exc()
            return ExitCode.COMPLETE_FAILURE
    
    def _apply_command_filters(self, commands: Dict[str, Any]) -> Dict[str, Any]:
        """Apply command filters to the discovered commands"""
        filtered = commands.copy()
        
        # Apply include filter
        if self.config.command_filter:
            filtered = {
                name: info for name, info in filtered.items()
                if name in self.config.command_filter
            }
        
        # Apply exclude filter
        if self.config.exclude_commands:
            filtered = {
                name: info for name, info in filtered.items()
                if name not in self.config.exclude_commands
            }
        
        return filtered
    
    def _run_tests_with_progress(self, suite_config: TestSuiteConfig, 
                                progress_reporter: ProgressReporter) -> TestSuiteResults:
        """Run tests with progress monitoring"""
        import threading
        import time
        
        # Start test execution in a separate thread
        results = [None]  # Use list to allow modification from thread
        exception = [None]
        
        def run_tests():
            try:
                results[0] = self.test_suite.run_all_command_tests(suite_config)
            except Exception as e:
                exception[0] = e
        
        test_thread = threading.Thread(target=run_tests)
        test_thread.daemon = True
        test_thread.start()
        
        # Monitor progress
        while test_thread.is_alive():
            progress_reporter.update_progress(self.test_suite)
            time.sleep(1)
            
            if self._interrupted:
                break
        
        test_thread.join(timeout=5)  # Wait up to 5 seconds for clean shutdown
        
        if exception[0]:
            raise exception[0]
        
        if results[0]:
            progress_reporter.finish_progress(results[0])
            return results[0]
        else:
            # Return empty results if interrupted
            return TestSuiteResults()
    
    def _generate_reports(self, results: TestSuiteResults, commands: Dict[str, Any]):
        """Generate test reports"""
        try:
            # Generate summary report
            self.reporter.generate_summary_report(results)
            
            # Generate detailed report if requested
            if self.config.generate_detailed_reports:
                self.reporter.generate_detailed_report(results)
            
            # Generate dependency report if we have dependency results
            if results.dependency_results:
                self.reporter.generate_dependency_report(results.dependency_results)
            
            # Generate coverage report
            self.reporter.generate_coverage_report(results, commands)
            
            # Generate integration report if we have integration results
            if results.integration_results:
                self.reporter.generate_integration_report(results.integration_results)
            
            if not self.config.quiet:
                print(f"Reports generated in: {self.config.output_directory}")
                
        except Exception as e:
            print(f"Failed to generate reports: {e}")
            if self.config.verbose:
                import traceback
                traceback.print_exc()
    
    def _print_summary(self, results: TestSuiteResults, execution_time: float):
        """Print test execution summary"""
        if self.config.quiet:
            return
        
        print("\n" + "="*60)
        print("TEST EXECUTION SUMMARY")
        print("="*60)
        print(f"Total Tests: {results.total_tests}")
        print(f"Passed: {results.passed_tests}")
        print(f"Failed: {results.failed_tests}")
        print(f"Success Rate: {results.success_rate:.1f}%")
        print(f"Execution Time: {execution_time:.2f} seconds")
        print(f"Commands Tested: {len(results.command_results)}")
        
        if results.failed_commands:
            print(f"Commands with Failures: {len(results.failed_commands)}")
            if self.config.verbose:
                print("Failed Commands:")
                for cmd in results.failed_commands:
                    print(f"  - {cmd}")
        
        if results.integration_results:
            integration_passed = sum(1 for r in results.integration_results if r.success)
            integration_total = len(results.integration_results)
            integration_rate = (integration_passed / integration_total * 100) if integration_total > 0 else 0
            print(f"Integration Tests: {integration_passed}/{integration_total} passed ({integration_rate:.1f}%)")
        
        if results.dependency_results:
            available_deps = sum(1 for info in results.dependency_results.values() 
                               if info.status.value == "available")
            total_deps = len(results.dependency_results)
            print(f"Dependencies: {available_deps}/{total_deps} available")
        
        print("="*60)
    
    def _determine_exit_code(self, results: TestSuiteResults) -> ExitCode:
        """Determine appropriate exit code based on results"""
        if results.total_tests == 0:
            return ExitCode.CONFIGURATION_ERROR
        
        if results.success_rate == 100:
            return ExitCode.SUCCESS
        elif results.success_rate >= 50:
            return ExitCode.PARTIAL_FAILURE
        else:
            return ExitCode.COMPLETE_FAILURE


def create_argument_parser() -> argparse.ArgumentParser:
    """Create command line argument parser"""
    parser = argparse.ArgumentParser(
        description="Run comprehensive CLI command tests",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                                    # Run all tests
  %(prog)s --smoke                           # Run only smoke tests
  %(prog)s --commands bot-start bot-stop     # Test specific commands
  %(prog)s --exclude orchestrator-start      # Exclude specific commands
  %(prog)s --parallel --workers 8            # Use 8 parallel workers
  %(prog)s --output-dir ./my-reports         # Custom output directory
  %(prog)s --formats json markdown           # Generate JSON and Markdown reports
  %(prog)s --verbose --no-progress           # Verbose output without progress
        """
    )
    
    # Test type selection
    test_group = parser.add_argument_group("Test Types")
    test_group.add_argument(
        "--smoke", action="store_true",
        help="Run smoke tests only"
    )
    test_group.add_argument(
        "--parameter-validation", action="store_true",
        help="Run parameter validation tests only"
    )
    test_group.add_argument(
        "--dependency", action="store_true",
        help="Run dependency tests only"
    )
    test_group.add_argument(
        "--error-handling", action="store_true",
        help="Run error handling tests only"
    )
    test_group.add_argument(
        "--integration", action="store_true",
        help="Run integration tests only"
    )
    test_group.add_argument(
        "--all-tests", action="store_true",
        help="Run all test types (default)"
    )
    
    # Command selection
    cmd_group = parser.add_argument_group("Command Selection")
    cmd_group.add_argument(
        "--commands", nargs="+", metavar="COMMAND",
        help="Specific commands to test"
    )
    cmd_group.add_argument(
        "--exclude", nargs="+", metavar="COMMAND",
        help="Commands to exclude from testing"
    )
    cmd_group.add_argument(
        "--list-commands", action="store_true",
        help="List all available commands and exit"
    )
    
    # Execution options
    exec_group = parser.add_argument_group("Execution Options")
    exec_group.add_argument(
        "--parallel", action="store_true", default=True,
        help="Run tests in parallel (default)"
    )
    exec_group.add_argument(
        "--sequential", action="store_true",
        help="Run tests sequentially"
    )
    exec_group.add_argument(
        "--workers", type=int, default=4, metavar="N",
        help="Number of parallel workers (default: 4)"
    )
    exec_group.add_argument(
        "--timeout-test", type=int, default=30, metavar="SECONDS",
        help="Timeout per test in seconds (default: 30)"
    )
    exec_group.add_argument(
        "--timeout-command", type=int, default=300, metavar="SECONDS",
        help="Timeout per command in seconds (default: 300)"
    )
    exec_group.add_argument(
        "--stop-on-failure", action="store_true",
        help="Stop execution on first failure"
    )
    
    # Output options
    output_group = parser.add_argument_group("Output Options")
    output_group.add_argument(
        "--output-dir", type=Path, metavar="DIR",
        help="Output directory for reports (default: test_reports)"
    )
    output_group.add_argument(
        "--formats", nargs="+", 
        choices=["json", "text", "markdown", "csv", "html"],
        default=["text", "json"],
        help="Report formats to generate (default: text json)"
    )
    output_group.add_argument(
        "--no-detailed-reports", action="store_true",
        help="Skip detailed report generation"
    )
    output_group.add_argument(
        "--verbose", "-v", action="store_true",
        help="Verbose output"
    )
    output_group.add_argument(
        "--quiet", "-q", action="store_true",
        help="Quiet output (errors only)"
    )
    output_group.add_argument(
        "--no-progress", action="store_true",
        help="Disable progress reporting"
    )
    
    return parser


def main():
    """Main entry point"""
    parser = create_argument_parser()
    args = parser.parse_args()
    
    # Handle list commands option
    if args.list_commands:
        try:
            context = CLIContext(config_path=Path("config"))
            logger = CLILogger()
            error_handler = CLIErrorHandler()
            discovery = CommandDiscovery(context, logger, error_handler)
            commands = discovery.discover_commands()
            print("Available commands:")
            for name in sorted(commands.keys()):
                print(f"  {name}")
            return ExitCode.SUCCESS.value
        except Exception as e:
            print(f"Failed to list commands: {e}")
            if args.verbose:
                import traceback
                traceback.print_exc()
            return ExitCode.CONFIGURATION_ERROR.value
    
    # Determine test types
    test_types = []
    if args.smoke:
        test_types.append(TestType.SMOKE)
    if args.parameter_validation:
        test_types.append(TestType.PARAMETER_VALIDATION)
    if args.dependency:
        test_types.append(TestType.DEPENDENCY)
    if args.error_handling:
        test_types.append(TestType.ERROR_HANDLING)
    if args.integration:
        test_types.append(TestType.INTEGRATION)
    
    # Default to all tests if none specified
    if not test_types or args.all_tests:
        test_types = list(TestType)
    
    # Convert format strings to enums
    report_formats = []
    for fmt in args.formats:
        try:
            report_formats.append(ReportFormat(fmt))
        except ValueError:
            print(f"Invalid report format: {fmt}")
            return ExitCode.CONFIGURATION_ERROR.value
    
    # Create configuration
    config = TestRunnerConfig(
        test_types=test_types,
        command_filter=args.commands,
        exclude_commands=args.exclude,
        parallel_execution=not args.sequential,
        max_workers=args.workers,
        timeout_per_test=args.timeout_test,
        timeout_per_command=args.timeout_command,
        stop_on_first_failure=args.stop_on_failure,
        output_directory=args.output_dir,
        report_formats=report_formats,
        verbose=args.verbose,
        quiet=args.quiet,
        show_progress=not args.no_progress,
        generate_detailed_reports=not args.no_detailed_reports
    )
    
    # Validate configuration
    if config.quiet and config.verbose:
        print("Cannot use both --quiet and --verbose options")
        return ExitCode.CONFIGURATION_ERROR.value
    
    if config.max_workers < 1:
        print("Number of workers must be at least 1")
        return ExitCode.CONFIGURATION_ERROR.value
    
    # Create and run test runner
    runner = CommandTestRunner(config)
    exit_code = runner.run_tests()
    
    return exit_code.value


if __name__ == "__main__":
    sys.exit(main())