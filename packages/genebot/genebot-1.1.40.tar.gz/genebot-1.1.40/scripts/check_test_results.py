#!/usr/bin/env python3
"""
Test Results Checker
===================

Checks test results and sets appropriate exit codes for CI/CD pipelines.
"""

import json
import argparse
import sys
from pathlib import Path
from typing import Dict, Any, List
import glob


def load_consolidated_report(reports_dir: Path) -> Dict[str, Any]:
    """Load the consolidated report"""
    report_file = reports_dir / "consolidated_report.json"
    
    if not report_file.exists():
        print(f"Warning: Consolidated report not found at {report_file}")
        return {}
    
    try:
        with open(report_file, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading consolidated report: {e}")
        return {}


def analyze_test_results(report: Dict[str, Any], fail_threshold: float) -> Dict[str, Any]:
    """Analyze test results and determine status"""
    if not report:
        return {
            "status": "error",
            "exit_code": 2,
            "message": "No test results available",
            "details": []
        }
    
    summary = report.get("summary", {})
    success_rate = summary.get("success_rate", 0.0)
    total_tests = summary.get("total_tests", 0)
    failed_tests = summary.get("failed_tests", 0)
    
    # Determine status based on success rate and thresholds
    if total_tests == 0:
        return {
            "status": "no_tests",
            "exit_code": 1,
            "message": "No tests were executed",
            "details": ["Check test configuration and execution"]
        }
    
    details = []
    
    # Check success rate against threshold
    if success_rate < fail_threshold:
        details.append(f"Success rate {success_rate:.1f}% is below threshold {fail_threshold}%")
    
    # Check for critical command failures
    command_results = report.get("command_results", {})
    critical_commands = []
    for cmd_name, cmd_result in command_results.items():
        if cmd_result.get("success_rate", 0) == 0 and cmd_result.get("total_tests", 0) > 0:
            critical_commands.append(cmd_name)
    
    if critical_commands:
        details.append(f"Commands with 0% success rate: {', '.join(critical_commands)}")
    
    # Check dependency issues
    dep_status = report.get("dependency_status", {})
    missing_deps = dep_status.get("missing", 0)
    if missing_deps > 0:
        details.append(f"{missing_deps} dependencies are missing")
    
    # Check for error patterns
    error_summary = report.get("error_summary", {})
    if error_summary:
        error_count = sum(len(errors) if isinstance(errors, list) else 1 
                         for errors in error_summary.values())
        if error_count > 0:
            details.append(f"{error_count} errors detected across commands")
    
    # Determine final status
    if success_rate >= 95 and not critical_commands:
        status = "success"
        exit_code = 0
        message = f"All tests passed successfully ({success_rate:.1f}% success rate)"
    elif success_rate >= fail_threshold and not critical_commands:
        status = "warning"
        exit_code = 0  # Don't fail CI for warnings
        message = f"Tests passed with warnings ({success_rate:.1f}% success rate)"
    else:
        status = "failure"
        exit_code = 1
        message = f"Tests failed ({success_rate:.1f}% success rate, {failed_tests} failures)"
    
    return {
        "status": status,
        "exit_code": exit_code,
        "message": message,
        "details": details,
        "success_rate": success_rate,
        "total_tests": total_tests,
        "failed_tests": failed_tests
    }


def print_test_summary(analysis: Dict[str, Any], python_version: str):
    """Print test summary to console"""
    status = analysis["status"]
    message = analysis["message"]
    
    # Status emoji
    status_emoji = {
        "success": "✅",
        "warning": "⚠️",
        "failure": "❌",
        "error": "💥",
        "no_tests": "❓"
    }.get(status, "❓")
    
    print(f"\n{status_emoji} Test Results Summary (Python {python_version})")
    print("=" * 60)
    print(f"Status: {status.upper()}")
    print(f"Message: {message}")
    
    if "success_rate" in analysis:
        print(f"Success Rate: {analysis['success_rate']:.1f}%")
        print(f"Total Tests: {analysis['total_tests']}")
        print(f"Failed Tests: {analysis['failed_tests']}")
    
    if analysis.get("details"):
        print("\nDetails:")
        for detail in analysis["details"]:
            print(f"  - {detail}")
    
    print("=" * 60)


def set_github_output(analysis: Dict[str, Any]):
    """Set GitHub Actions output variables"""
    try:
        # Set outputs for GitHub Actions
        github_output = Path(os.environ.get("GITHUB_OUTPUT", "/dev/null"))
        if github_output.exists() or github_output.parent.exists():
            with open(github_output, "a") as f:
                f.write(f"test_status={analysis['status']}\n")
                f.write(f"success_rate={analysis.get('success_rate', 0):.1f}\n")
                f.write(f"total_tests={analysis.get('total_tests', 0)}\n")
                f.write(f"failed_tests={analysis.get('failed_tests', 0)}\n")
                f.write(f"exit_code={analysis['exit_code']}\n")
    except Exception as e:
        print(f"Warning: Could not set GitHub outputs: {e}")


def main():
    parser = argparse.ArgumentParser(description="Check test results and set CI status")
    parser.add_argument("--reports-dir", type=Path, required=True,
                       help="Directory containing test reports")
    parser.add_argument("--fail-threshold", type=float, default=80.0,
                       help="Success rate threshold below which CI fails (default: 80%)")
    parser.add_argument("--python-version", required=True,
                       help="Python version being tested")
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="Verbose output")
    
    args = parser.parse_args()
    
    # Load consolidated report
    report = load_consolidated_report(args.reports_dir)
    
    # Analyze results
    analysis = analyze_test_results(report, args.fail_threshold)
    
    # Print summary
    print_test_summary(analysis, args.python_version)
    
    # Set GitHub Actions outputs if running in CI
    import os
    if os.environ.get("GITHUB_ACTIONS"):
        set_github_output(analysis)
    
    # Additional verbose output
    if args.verbose and report:
        print("\nDetailed Report Information:")
        print(f"Report Version: {report.get('ci_report_version', 'unknown')}")
        print(f"Generated At: {report.get('generated_at', 'unknown')}")
        print(f"Total Reports Processed: {report.get('total_reports', 0)}")
        
        test_types = report.get("test_types", {})
        if test_types:
            print("\nTest Types:")
            for test_type, stats in test_types.items():
                print(f"  {test_type}: {stats.get('passed_tests', 0)}/{stats.get('total_tests', 0)} passed")
        
        command_results = report.get("command_results", {})
        if command_results:
            print(f"\nCommand Results ({len(command_results)} commands):")
            for cmd_name, cmd_result in sorted(command_results.items()):
                success_rate = cmd_result.get("success_rate", 0)
                total_tests = cmd_result.get("total_tests", 0)
                print(f"  {cmd_name}: {success_rate:.1f}% ({total_tests} tests)")
    
    # Exit with appropriate code
    sys.exit(analysis["exit_code"])


if __name__ == "__main__":
    main()