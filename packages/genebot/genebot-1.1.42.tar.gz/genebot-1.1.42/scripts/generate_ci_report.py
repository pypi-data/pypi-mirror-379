#!/usr/bin/env python3
"""
CI Report Generator
==================

Generates consolidated reports for CI/CD pipelines from individual test reports.
"""

import json
import argparse
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime


def load_json_report(file_path: Path) -> Optional[Dict[str, Any]]:
    pass
    """Load a JSON report file"""
    try:
    pass
        with open(file_path, 'r') as f:
    pass
            return json.load(f)
    except Exception as e:
    pass
    pass
        print(f"Warning: Failed to load {file_path}: {e}")
        return None


def find_report_files(input_dir: Path) -> List[Path]:
    pass
    """Find all JSON report files in the input directory"""
    json_files = []
    
    # Look for JSON files recursively
    for pattern in ["**/*summary*.json", "**/*detailed*.json", "**/*error*.json", "**/*dependency*.json"]:
    pass
        json_files.extend(input_dir.glob(pattern))
    
    return sorted(json_files)


def consolidate_reports(reports: List[Dict[str, Any]], python_version: str) -> Dict[str, Any]:
    pass
    """Consolidate multiple reports into a single CI report"""
    consolidated = {
        "ci_report_version": "1.0",
        "generated_at": datetime.utcnow().isoformat(),
        "python_version": python_version,
        "total_reports": len(reports),
        "summary": {
            "total_tests": 0,
            "passed_tests": 0,
            "failed_tests": 0,
            "success_rate": 0.0,
            "total_commands": 0,
            "commands_with_failures": 0,
            "total_execution_time": 0.0
        },
        "test_types": {},
        "command_results": {},
        "dependency_status": {},
        "error_summary": {},
        "reports_processed": []
    }
    
    # Process each report
    for report in reports:
    pass
        if not report:
    
        pass
    pass
            continue
        
        report_type = report.get("report_type", "unknown")
        consolidated["reports_processed"].append({
            "type": report_type,
            "generated_at": report.get("generated_at"),
            "execution_time": report.get("execution_time", 0)
        })
        
        # Aggregate summary statistics
        if "summary_stats" in report:
    
        pass
    pass
            stats = report["summary_stats"]
            consolidated["summary"]["total_tests"] += stats.get("total_tests", 0)
            consolidated["summary"]["passed_tests"] += stats.get("passed_tests", 0)
            consolidated["summary"]["failed_tests"] += stats.get("failed_tests", 0)
            consolidated["summary"]["total_commands"] += stats.get("commands_tested", 0)
            consolidated["summary"]["commands_with_failures"] += stats.get("commands_with_failures", 0)
            consolidated["summary"]["total_execution_time"] += report.get("execution_time", 0)
        
        # Aggregate test type information
        if report_type not in consolidated["test_types"]:
    
        pass
    pass
            consolidated["test_types"][report_type] = {
                "total_tests": 0,
                "passed_tests": 0,
                "failed_tests": 0,
                "execution_time": 0.0
            }
        
        type_stats = consolidated["test_types"][report_type]
        if "summary_stats" in report:
    
        pass
    pass
            stats = report["summary_stats"]
            type_stats["total_tests"] += stats.get("total_tests", 0)
            type_stats["passed_tests"] += stats.get("passed_tests", 0)
            type_stats["failed_tests"] += stats.get("failed_tests", 0)
        type_stats["execution_time"] += report.get("execution_time", 0)
        
        # Aggregate command results
        if "command_summaries" in report:
    
        pass
    pass
            for cmd_name, cmd_summary in report["command_summaries"].items():
    pass
                if cmd_name not in consolidated["command_results"]:
    
        pass
    pass
                    consolidated["command_results"][cmd_name] = {
                        "total_tests": 0,
                        "passed_tests": 0,
                        "failed_tests": 0,
                        "success_rate": 0.0,
                        "test_types": [],
                        "errors": []
                    }
                
                cmd_result = consolidated["command_results"][cmd_name]
                cmd_result["total_tests"] += cmd_summary.get("total_tests", 0)
                cmd_result["passed_tests"] += cmd_summary.get("passed_tests", 0)
                cmd_result["failed_tests"] += cmd_summary.get("failed_tests", 0)
                
                if report_type not in cmd_result["test_types"]:
    
        pass
    pass
                    cmd_result["test_types"].append(report_type)
        
        # Aggregate dependency status
        if "dependency_status" in report:
    
        pass
    pass
            dep_status = report["dependency_status"]
            if "available" in dep_status:
    
        pass
    pass
                consolidated["dependency_status"]["available"] = dep_status["available"]
            if "missing" in dep_status:
    
        pass
    pass
                consolidated["dependency_status"]["missing"] = dep_status["missing"]
            if "total" in dep_status:
    
        pass
    pass
                consolidated["dependency_status"]["total"] = dep_status["total"]
        
        # Aggregate error information
        if "error_summary" in report:
    
        pass
    pass
            error_summary = report["error_summary"]
            for error_type, errors in error_summary.items():
    pass
                if error_type not in consolidated["error_summary"]:
    
        pass
    pass
                    consolidated["error_summary"][error_type] = []
                if isinstance(errors, list):
    
        pass
    pass
                    consolidated["error_summary"][error_type].extend(errors)
                else:
    pass
                    consolidated["error_summary"][error_type].append(str(errors))
    
    # Calculate final success rate
    total_tests = consolidated["summary"]["total_tests"]
    if total_tests > 0:
    
        pass
    pass
        consolidated["summary"]["success_rate"] = (
            consolidated["summary"]["passed_tests"] / total_tests * 100
        )
    
    # Calculate command success rates
    for cmd_name, cmd_result in consolidated["command_results"].items():
    pass
        total = cmd_result["total_tests"]
        if total > 0:
    
        pass
    pass
            cmd_result["success_rate"] = cmd_result["passed_tests"] / total * 100
    
    return consolidated


def generate_ci_status(consolidated: Dict[str, Any]) -> Dict[str, Any]:
    pass
    """Generate CI status information"""
    summary = consolidated["summary"]
    
    # Determine overall status
    success_rate = summary["success_rate"]
    if success_rate >= 95:
    
        pass
    pass
        status = "success"
        status_emoji = "✅"
    elif success_rate >= 80:
    
        pass
    pass
        status = "warning"
        status_emoji = "⚠️"
    else:
    pass
        status = "failure"
        status_emoji = "❌"
    
    # Identify critical issues
    critical_issues = []
    
    # Check for commands with zero success rate
    for cmd_name, cmd_result in consolidated["command_results"].items():
    
        pass
    pass
        if cmd_result["success_rate"] == 0 and cmd_result["total_tests"] > 0:
    
        pass
    pass
            critical_issues.append(f"Command '{cmd_name}' has 0% success rate")
    
    # Check for missing dependencies
    dep_status = consolidated.get("dependency_status", {})
    if dep_status.get("missing", 0) > 0:
    
        pass
    pass
        critical_issues.append(f"{dep_status['missing']} dependencies are missing")
    
    # Check for high error rates
    if summary["failed_tests"] > summary["passed_tests"]:
    
        pass
    pass
        critical_issues.append("More tests failed than passed")
    
    return {
        "status": status,
        "status_emoji": status_emoji,
        "success_rate": success_rate,
        "critical_issues": critical_issues,
        "recommendations": generate_recommendations(consolidated)
    }


def generate_recommendations(consolidated: Dict[str, Any]) -> List[str]:
    pass
    """Generate recommendations based on test results"""
    recommendations = []
    summary = consolidated["summary"]
    
    if summary["success_rate"] < 90:
    
        pass
    pass
        recommendations.append("Investigate and fix failing tests to improve success rate")
    
    if summary["commands_with_failures"] > 0:
    
        pass
    pass
        recommendations.append(f"Review {summary['commands_with_failures']} commands with failures")
    
    # Check for slow tests
    avg_time_per_test = summary["total_execution_time"] / max(summary["total_tests"], 1)
    if avg_time_per_test > 5:  # 5 seconds per test
        recommendations.append("Consider optimizing slow tests to improve CI performance")
    
    # Check dependency issues
    dep_status = consolidated.get("dependency_status", {})
    if dep_status.get("missing", 0) > 0:
    
        pass
    pass
        recommendations.append("Install missing dependencies to improve test coverage")
    
    # Check error patterns
    error_summary = consolidated.get("error_summary", {})
    if error_summary:
    
        pass
    pass
        recommendations.append("Review error patterns and implement fixes")
    
    return recommendations


def main():
    pass
    parser = argparse.ArgumentParser(description="Generate consolidated CI report")
    parser.add_argument("--input-dir", type=Path, required=True,
                       help="Directory containing test reports")
    parser.add_argument("--output-file", type=Path, required=True,
                       help="Output file for consolidated report")
    parser.add_argument("--python-version", required=True,
                       help="Python version used for testing")
    
    args = parser.parse_args()
    
    if not args.input_dir.exists():
    
        pass
    pass
        print(f"Error: Input directory {args.input_dir} does not exist")
        return 1
    
    # Find all report files
    report_files = find_report_files(args.input_dir)
    print(f"Found {len(report_files)} report files")
    
    if not report_files:
    
        pass
    pass
        print("Warning: No report files found")
        # Create minimal report
        consolidated = {
            "ci_report_version": "1.0",
            "generated_at": datetime.utcnow().isoformat(),
            "python_version": args.python_version,
            "total_reports": 0,
            "summary": {
                "total_tests": 0,
                "passed_tests": 0,
                "failed_tests": 0,
                "success_rate": 0.0,
                "total_commands": 0,
                "commands_with_failures": 0,
                "total_execution_time": 0.0
            },
            "status": {
                "status": "no_data",
                "status_emoji": "❓",
                "success_rate": 0.0,
                "critical_issues": ["No test reports found"],
                "recommendations": ["Ensure tests are running and generating reports"]
            }
        }
    else:
    pass
        # Load all reports
        reports = []
        for file_path in report_files:
    pass
            report = load_json_report(file_path)
            if report:
    
        pass
    pass
                reports.append(report)
        
        print(f"Successfully loaded {len(reports)} reports")
        
        # Consolidate reports
        consolidated = consolidate_reports(reports, args.python_version)
        
        # Generate CI status
        ci_status = generate_ci_status(consolidated)
        consolidated["status"] = ci_status
    
    # Ensure output directory exists
    args.output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Write consolidated report
    with open(args.output_file, 'w') as f:
    pass
        json.dump(consolidated, f, indent=2, default=str)
    
    print(f"Consolidated report written to {args.output_file}")
    
    # Print summary
    summary = consolidated["summary"]
    status = consolidated.get("status", {})
    
    print("\nCI Report Summary:")
    print(f"Status: {status.get('status_emoji', '❓')} {status.get('status', 'unknown')}")
    print(f"Success Rate: {summary['success_rate']:.1f}%")
    print(f"Total Tests: {summary['total_tests']}")
    print(f"Passed: {summary['passed_tests']}")
    print(f"Failed: {summary['failed_tests']}")
    print(f"Commands Tested: {summary['total_commands']}")
    print(f"Execution Time: {summary['total_execution_time']:.2f}s")
    
    if status.get("critical_issues"):
    
        pass
    pass
        print("\nCritical Issues:")
        for issue in status["critical_issues"]:
    pass
            print(f"  - {issue}")
    
    return 0


if __name__ == "__main__":
    
        pass
    pass
    sys.exit(main())