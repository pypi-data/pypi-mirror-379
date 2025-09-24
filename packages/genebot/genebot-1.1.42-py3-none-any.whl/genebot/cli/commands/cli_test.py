"""
CLI Testing Command
==================

Command to run CLI validation tests.
"""

from argparse import Namespace
from pathlib import Path
import json
from datetime import datetime

from .base import BaseCommand
from ..result import CommandResult
from ..testing.test_runner import CLITestRunner
from ..testing.test_cases import CLITestSuite, TestType


class CLITestCommand(BaseCommand):
    pass
    """Run CLI command validation tests"""
    
    def run(self, args: Namespace) -> CommandResult:
    pass
        """Execute CLI testing command"""
        try:
    pass
            test_runner = CLITestRunner()
            
            # Determine what tests to run
            if hasattr(args, 'command') and args.command:
    
        pass
    pass
                return self._run_single_command_tests(test_runner, args.command, args)
            elif hasattr(args, 'test_type') and args.test_type:
    
        pass
    pass
                return self._run_tests_by_type(test_runner, args.test_type, args)
            else:
    pass
                return self._run_comprehensive_tests(test_runner, args)
                
        except Exception as e:
    pass
    pass
            return self.error_handler.handle_exception(
                e, "Failed to run CLI tests"
            )
    
    def _run_comprehensive_tests(self, test_runner: CLITestRunner, args: Namespace) -> CommandResult:
    pass
        """Run comprehensive tests for all commands"""
        self.logger.info("Running comprehensive CLI command validation tests...")
        
        try:
    pass
            results = test_runner.run_comprehensive_tests()
            
            # Save results if output file specified
            if hasattr(args, 'output') and args.output:
    
        pass
    pass
                output_path = Path(args.output)
                test_runner.save_results(results, output_path)
                self.logger.info(f"Test results saved to: {output_path}")
            
            # Generate and display report
            report = test_runner.generate_report(results)
            
            # Determine if tests passed
            summary = results['overall_summary']
            success_rate = summary['success_rate']
            
            if success_rate >= 90:  # 90% success rate threshold
                self.logger.info("CLI validation tests PASSED")
                return CommandResult.success(
                    f"CLI Validation Complete\n\n{report}",
                    data=results
                )
            else:
    pass
                self.logger.warning(f"CLI validation tests had issues (Success rate: {success_rate:.1f}%)")
                return CommandResult.warning(
                    f"CLI Validation Issues Found\n\n{report}",
                    data=results
                )
                
        except Exception as e:
    pass
    pass
            return CommandResult.error(
                f"Failed to run comprehensive tests: {str(e)}"
            )
    
    def _run_single_command_tests(
        self, 
        test_runner: CLITestRunner, 
        command_name: str, 
        args: Namespace
    ) -> CommandResult:
    pass
        """Run tests for a single command"""
        self.logger.info(f"Running tests for command: {command_name}")
        
        try:
    pass
            # Create test suite for single command
            suite = CLITestSuite(f"{command_name}_tests")
            
            # Add all test types for the command
            from ..testing.test_cases import (
                create_output_validation_test
            
            suite.add_test(create_basic_execution_test(command_name))
            
            # Add parameter validation test
            invalid_args = Namespace()
            suite.add_test(create_parameter_validation_test(
                command_name, invalid_args, should_succeed=False
            ))
            
            # Add error handling test
            suite.add_test(create_error_handling_test(
                command_name, Namespace()
            ))
            
            # Add output validation test
            suite.add_test(create_output_validation_test(
                command_name, Namespace(), ["success", "completed"]
            ))
            
            test_runner.add_test_suite(suite)
            results = test_runner.run_all_tests()
            
            # Generate report
            report = test_runner.generate_report(results)
            
            return CommandResult.success(
                f"Tests for '{command_name}' completed\n\n{report}",
                data=results
            )
            
        except Exception as e:
    pass
    pass
            return CommandResult.error(
                f"Failed to run tests for command '{command_name}': {str(e)}"
            )
    
    def _run_tests_by_type(
        self, 
        test_runner: CLITestRunner, 
        test_type: str, 
        args: Namespace
    ) -> CommandResult:
    pass
        """Run tests of a specific type"""
        self.logger.info(f"Running tests of type: {test_type}")
        
        try:
    pass
            # Map string to TestType enum
            type_mapping = {
                'basic': TestType.BASIC_EXECUTION,
                'parameters': TestType.PARAMETER_VALIDATION,
                'errors': TestType.ERROR_HANDLING,
                'output': TestType.OUTPUT_VALIDATION,
                'integration': TestType.INTEGRATION
            }
            
            if test_type not in type_mapping:
    
        pass
    pass
                return CommandResult.error(
                    f"Unknown test type: {test_type}. "
                    f"Available types: {', '.join(type_mapping.keys())}"
                )
            
            target_type = type_mapping[test_type]
            
            # Create comprehensive suite and filter by type
            comprehensive_suite = test_runner.create_comprehensive_test_suite()
            filtered_tests = comprehensive_suite.get_tests_by_type(target_type)
            
            # Create new suite with filtered tests
            filtered_suite = CLITestSuite(f"{test_type}_tests")
            for test in filtered_tests:
    pass
                filtered_suite.add_test(test)
            
            test_runner.add_test_suite(filtered_suite)
            results = test_runner.run_all_tests()
            
            # Generate report
            report = test_runner.generate_report(results)
            
            return CommandResult.success(
                f"Tests of type '{test_type}' completed\n\n{report}",
                data=results
            )
            
        except Exception as e:
    pass
    pass
            return CommandResult.error(
                f"Failed to run tests of type '{test_type}': {str(e)}"
            )
    
    def get_help_text(self) -> str:
    pass
        """Get help text for the command"""
        return """
CLI Test Command - Validate CLI commands

Usage:
    pass
  genebot cli-test                    # Run all tests
  genebot cli-test --command start   # Test specific command
  genebot cli-test --type basic      # Test specific type
  genebot cli-test --output results.json  # Save results

Options:
    
        pass
    pass
  --command COMMAND    Test specific command only
  --type TYPE         Test specific type (basic, parameters, errors, output)
  --output FILE       Save results to JSON file
  --verbose           Show detailed output

Test Types:
    
        pass
    pass
  basic       - Basic command execution
  parameters  - Parameter validation
  errors      - Error handling
  output      - Output format validation
  integration - Integration tests
"""