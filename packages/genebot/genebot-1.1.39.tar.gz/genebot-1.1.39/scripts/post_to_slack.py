#!/usr/bin/env python3
"""
Slack Notification Script
=========================

Posts test results to Slack webhook.
"""

import json
import argparse
import sys
import requests
from pathlib import Path
from typing import Dict, Any


def create_slack_message(report_content: str, status: str) -> Dict[str, Any]:
    """Create Slack message payload"""
    
    # Determine color based on status
    color_map = {
        "success": "good",
        "warning": "#warning",
        "failure": "danger",
        "error": "danger"
    }
    color = color_map.get(status, "#808080")
    
    # Status emoji
    emoji_map = {
        "success": "✅",
        "warning": "⚠️",
        "failure": "❌",
        "error": "💥"
    }
    emoji = emoji_map.get(status, "❓")
    
    # Extract key information from report
    lines = report_content.split('\n')
    title = "Command Test Results"
    
    # Find the overall status line
    status_line = ""
    for line in lines:
        if "Overall Status:" in line:
            status_line = line.strip()
            break
    
    # Create message
    message = {
        "text": f"{emoji} {title}",
        "attachments": [
            {
                "color": color,
                "title": f"{emoji} {title}",
                "text": status_line,
                "fields": [],
                "footer": "Command Testing Validation",
                "ts": int(time.time()) if 'time' in globals() else None
            }
        ]
    }
    
    # Extract key metrics
    for line in lines:
        line = line.strip()
        if line.startswith("- **Success Rate:**"):
            success_rate = line.replace("- **Success Rate:**", "").strip()
            message["attachments"][0]["fields"].append({
                "title": "Success Rate",
                "value": success_rate,
                "short": True
            })
        elif line.startswith("- **Total Tests:**"):
            total_tests = line.replace("- **Total Tests:**", "").strip()
            message["attachments"][0]["fields"].append({
                "title": "Total Tests",
                "value": total_tests,
                "short": True
            })
        elif line.startswith("- **Failed:**"):
            failed_tests = line.replace("- **Failed:**", "").strip()
            message["attachments"][0]["fields"].append({
                "title": "Failed Tests",
                "value": failed_tests,
                "short": True
            })
        elif line.startswith("- **Python Versions:**"):
            python_versions = line.replace("- **Python Versions:**", "").strip()
            message["attachments"][0]["fields"].append({
                "title": "Python Versions",
                "value": python_versions,
                "short": True
            })
    
    # Add critical issues if any
    in_critical_section = False
    critical_issues = []
    for line in lines:
        if "## ⚠️ Critical Issues" in line:
            in_critical_section = True
            continue
        elif line.startswith("##") and in_critical_section:
            break
        elif in_critical_section and line.startswith("- "):
            critical_issues.append(line[2:])  # Remove "- "
    
    if critical_issues:
        issues_text = "\n".join(f"• {issue}" for issue in critical_issues[:5])  # Limit to 5
        if len(critical_issues) > 5:
            issues_text += f"\n... and {len(critical_issues) - 5} more"
        
        message["attachments"][0]["fields"].append({
            "title": "Critical Issues",
            "value": issues_text,
            "short": False
        })
    
    return message


def post_to_slack(webhook_url: str, message: Dict[str, Any]) -> bool:
    """Post message to Slack webhook"""
    try:
        response = requests.post(
            webhook_url,
            json=message,
            headers={'Content-Type': 'application/json'},
            timeout=30
        )
        response.raise_for_status()
        print("Successfully posted to Slack")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Failed to post to Slack: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Post test results to Slack")
    parser.add_argument("--webhook-url", required=True,
                       help="Slack webhook URL")
    parser.add_argument("--report-file", type=Path, required=True,
                       help="Path to the summary report file")
    parser.add_argument("--status", required=True,
                       choices=["success", "warning", "failure", "error"],
                       help="Overall test status")
    
    args = parser.parse_args()
    
    # Read report content
    if not args.report_file.exists():
        print(f"Error: Report file {args.report_file} does not exist")
        return 1
    
    try:
        with open(args.report_file, 'r') as f:
            report_content = f.read()
    except Exception as e:
        print(f"Error reading report file: {e}")
        return 1
    
    # Create Slack message
    message = create_slack_message(report_content, args.status)
    
    # Post to Slack
    success = post_to_slack(args.webhook_url, message)
    
    return 0 if success else 1


if __name__ == "__main__":
    import time
    sys.exit(main())