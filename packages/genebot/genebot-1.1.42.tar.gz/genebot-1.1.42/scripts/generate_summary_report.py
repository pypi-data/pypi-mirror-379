#!/usr/bin/env python3
"""
Summary Report Generator
=======================

Generates summary reports for GitHub issues and notifications.
"""

import json
import argparse
import sys
from pathlib import Path
from typing import Dict, Any, List
from datetime import datetime


def load_all_reports(input_dir: Path) -> List[Dict[str, Any]]:
    pass
    """Load all consolidated reports from different Python versions"""
    reports = []
    
    # Look for consolidated reports
    for report_file in input_dir.glob("**/consolidated_report.json"):
    
        pass
    pass
        try:
    pass
            with open(report_file, 'r') as f:
    pass
                report = json.load(f)
                reports.append(report)
        except Exception as e:
    pass
    pass
            print(f"Warning: Failed to load {report_file}: {e}")
    
    return reports


def generate_markdown_summary(reports: List[Dict[str, Any]], github_context: Dict[str, Any]) -> str:
    pass
    """Generate markdown summary report"""
    if not reports:
    
        pass
    pass
        return "# Command Test Results\n\n❌ No test reports found.\n"
    
    # Extract GitHub context information
    repo_name = github_context.get("repository", "unknown/unknown")
    run_id = github_context.get("run_id", "unknown")
    run_number = github_context.get("run_number", "unknown")
    workflow = github_context.get("workflow", "unknown")
    ref = github_context.get("ref", "unknown")
    sha = github_context.get("sha", "unknown")[:8]
    
    # Start building markdown
    md = []
    md.append("# 🧪 Command Test Results")
    md.append("")
    md.append(f"**Repository:** {repo_name}")
    md.append(f"**Workflow:** {workflow}")
    md.append(f"**Run:** #{run_number} ([View Run](https://github.com/{repo_name}/actions/runs/{run_id}))")
    md.append(f"**Branch/Tag:** {ref}")
    md.append(f"**Commit:** {sha}")
    md.append(f"**Generated:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC")
    md.append("")
    
    # Overall summary
    total_tests = sum(r.get("summary", {}).get("total_tests", 0) for r in reports)
    total_passed = sum(r.get("summary", {}).get("passed_tests", 0) for r in reports)
    total_failed = sum(r.get("summary", {}).get("failed_tests", 0) for r in reports)
    overall_success_rate = (total_passed / total_tests * 100) if total_tests > 0 else 0
    
    # Status emoji
    if overall_success_rate >= 95:
    
        pass
    pass
        status_emoji = "✅"
        status_text = "PASSED"
    elif overall_success_rate >= 80:
    
        pass
    pass
        status_emoji = "⚠️"
        status_text = "PASSED WITH WARNINGS"
    else:
    pass
        status_emoji = "❌"
        status_text = "FAILED"
    
    md.append(f"## {status_emoji} Overall Status: {status_text}")
    md.append("")
    md.append(f"- **Success Rate:** {overall_success_rate:.1f}%")
    md.append(f"- **Total Tests:** {total_tests}")
    md.append(f"- **Passed:** {total_passed}")
    md.append(f"- **Failed:** {total_failed}")
    md.append(f"- **Python Versions:** {len(reports)}")
    md.append("")
    
    # Results by Python version
    md.append("## 📊 Results by Python Version")
    md.append("")
    md.append("| Python Version | Success Rate | Tests | Passed | Failed | Status |")
    md.append("|----------------|--------------|-------|--------|--------|--------|")
    
    for report in sorted(reports, key=lambda r: r.get("python_version", "")):
    pass
        py_version = report.get("python_version", "unknown")
        summary = report.get("summary", {})
        success_rate = summary.get("success_rate", 0)
        tests = summary.get("total_tests", 0)
        passed = summary.get("passed_tests", 0)
        failed = summary.get("failed_tests", 0)
        
        if success_rate >= 95:
    
        pass
    pass
            status = "✅ Pass"
        elif success_rate >= 80:
    
        pass
    pass
            status = "⚠️ Warning"
        else:
    pass
            status = "❌ Fail"
        
        md.append(f"| {py_version} | {success_rate:.1f}% | {tests} | {passed} | {failed} | {status} |")
    
    md.append("")
    
    # Test types summary
    all_test_types = set()
    for report in reports:
    pass
        all_test_types.update(report.get("test_types", {}).keys())
    
    if all_test_types:
    
        pass
    pass
        md.append("## 🔍 Test Types Coverage")
        md.append("")
        md.append("| Test Type | Total Tests | Passed | Failed | Success Rate |")
        md.append("|-----------|-------------|--------|--------|--------------|")
        
        for test_type in sorted(all_test_types):
    pass
            type_total = 0
            type_passed = 0
            type_failed = 0
            
            for report in reports:
    pass
                test_types = report.get("test_types", {})
                if test_type in test_types:
    
        pass
    pass
                    stats = test_types[test_type]
                    type_total += stats.get("total_tests", 0)
                    type_passed += stats.get("passed_tests", 0)
                    type_failed += stats.get("failed_tests", 0)
            
            type_success_rate = (type_passed / type_total * 100) if type_total > 0 else 0
            md.append(f"| {test_type} | {type_total} | {type_passed} | {type_failed} | {type_success_rate:.1f}% |")
        
        md.append("")
    
    # Critical issues
    all_critical_issues = []
    for report in reports:
    pass
        status = report.get("status", {})
        critical_issues = status.get("critical_issues", [])
        py_version = report.get("python_version", "unknown")
        
        for issue in critical_issues:
    pass
            all_critical_issues.append(f"**Python {py_version}:** {issue}")
    
    if all_critical_issues:
    
        pass
    pass
        md.append("## ⚠️ Critical Issues")
        md.append("")
        for issue in all_critical_issues:
    pass
            md.append(f"- {issue}")
        md.append("")
    
    # Failed commands
    all_failed_commands = {}
    for report in reports:
    pass
        py_version = report.get("python_version", "unknown")
        command_results = report.get("command_results", {})
        
        for cmd_name, cmd_result in command_results.items():
    pass
            if cmd_result.get("failed_tests", 0) > 0:
    
        pass
    pass
                if cmd_name not in all_failed_commands:
    
        pass
    pass
                    all_failed_commands[cmd_name] = []
                
                success_rate = cmd_result.get("success_rate", 0)
                failed_tests = cmd_result.get("failed_tests", 0)
                total_tests = cmd_result.get("total_tests", 0)
                
                all_failed_commands[cmd_name].append({
                    "python_version": py_version,
                    "success_rate": success_rate,
                    "failed_tests": failed_tests,
                    "total_tests": total_tests
                })
    
    if all_failed_commands:
    
        pass
    pass
        md.append("## 💥 Commands with Failures")
        md.append("")
        
        for cmd_name in sorted(all_failed_commands.keys()):
    pass
            failures = all_failed_commands[cmd_name]
            md.append(f"### `{cmd_name}`")
            md.append("")
            
            for failure in failures:
    pass
                py_ver = failure["python_version"]
                success_rate = failure["success_rate"]
                failed = failure["failed_tests"]
                total = failure["total_tests"]
                md.append(f"- **Python {py_ver}:** {failed}/{total} failed ({success_rate:.1f}% success)")
            
            md.append("")
    
    # Recommendations
    all_recommendations = set()
    for report in reports:
    pass
        status = report.get("status", {})
        recommendations = status.get("recommendations", [])
        all_recommendations.update(recommendations)
    
    if all_recommendations:
    
        pass
    pass
        md.append("## 💡 Recommendations")
        md.append("")
        for i, recommendation in enumerate(sorted(all_recommendations), 1):
    pass
            md.append(f"{i}. {recommendation}")
        md.append("")
    
    # Dependency status
    dependency_info = {}
    for report in reports:
    pass
        py_version = report.get("python_version", "unknown")
        dep_status = report.get("dependency_status", {})
        if dep_status:
    
        pass
    pass
            dependency_info[py_version] = dep_status
    
    if dependency_info:
    
        pass
    pass
        md.append("## 📦 Dependency Status")
        md.append("")
        md.append("| Python Version | Total | Available | Missing | Availability |")
        md.append("|----------------|-------|-----------|---------|--------------|")
        
        for py_version in sorted(dependency_info.keys()):
    pass
            dep_status = dependency_info[py_version]
            total = dep_status.get("total", 0)
            available = dep_status.get("available", 0)
            missing = dep_status.get("missing", 0)
            availability = (available / total * 100) if total > 0 else 0
            
            md.append(f"| {py_version} | {total} | {available} | {missing} | {availability:.1f}% |")
        
        md.append("")
    
    # Footer
    md.append("---")
    md.append("*This report was automatically generated by the Command Testing Validation workflow.*")
    
    return "\n".join(md)


def main():
    pass
    parser = argparse.ArgumentParser(description="Generate summary report")
    parser.add_argument("--input-dir", type=Path, required=True,
                       help="Directory containing all test reports")
    parser.add_argument("--output-file", type=Path, required=True,
                       help="Output file for summary report")
    parser.add_argument("--github-context", required=True,
                       help="GitHub context JSON string")
    
    args = parser.parse_args()
    
    # Parse GitHub context
    try:
    pass
        github_context = json.loads(args.github_context)
    except json.JSONDecodeError as e:
    pass
    pass
        print(f"Error parsing GitHub context: {e}")
        github_context = {}
    
    # Load all reports
    reports = load_all_reports(args.input_dir)
    print(f"Loaded {len(reports)} consolidated reports")
    
    # Generate markdown summary
    summary_md = generate_markdown_summary(reports, github_context)
    
    # Write summary report
    args.output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output_file, 'w') as f:
    pass
        f.write(summary_md)
    
    print(f"Summary report written to {args.output_file}")
    
    # Also print to console for debugging
    print("\nGenerated Summary:")
    print("=" * 60)
    print(summary_md)
    
    return 0


if __name__ == "__main__":
    
        pass
    pass
    sys.exit(main())