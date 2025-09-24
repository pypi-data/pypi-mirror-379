#!/usr/bin/env python3
"""
Test Configuration Runner
=========================

Runs predefined test configurations from test-config.json.
"""

import json
import argparse
import sys
import subprocess
from pathlib import Path
from typing import Dict, Any, List


def load_test_config(config_file: Path) -> Dict[str, Any]:
    """Load test configuration from JSON file"""
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading test configuration: {e}")
        return {}


def build_command_args(config: Dict[str, Any], commands: List[str] = None) -> List[str]:
    """Build command line arguments from configuration"""
    args = ["python", "scripts/run_command_tests.py"]
    
    # Add test types
    test_types = config.get("test_types", [])
    for test_type in test_types:
        if test_type == "smoke":
            args.append("--smoke")
        elif test_type == "parameter-validation":
            args.append("--parameter-validation")
        elif test_type == "dependency":
            args.append("--dependency")
        elif test_type == "error-handling":
            args.append("--error-handling")
        elif test_type == "integration":
            args.append("--integration")
    
    # Add commands if specified
    if commands:
        args.extend(["--commands"] + commands)
    
    # Add execution mode
    if config.get("parallel", True):
        args.append("--parallel")
    else:
        args.append("--sequential")
    
    # Add timeouts
    if "timeout_per_test" in config:
        args.extend(["--timeout-test", str(config["timeout_per_test"])])
    
    if "timeout_per_command" in config:
        args.extend(["--timeout-command", str(config["timeout_per_command"])])
    
    # Add output formats
    formats = config.get("formats", ["text", "json"])
    args.extend(["--formats"] + formats)
    
    # Add verbosity
    if config.get("verbose", False):
        args.append("--verbose")
    
    if config.get("quiet", False):
        args.append("--quiet")
    
    # Add output directory
    output_dir = config.get("output_dir", "test_reports")
    args.extend(["--output-dir", output_dir])
    
    return args


def run_test_configuration(config_name: str, config: Dict[str, Any], 
                          commands: List[str] = None) -> int:
    """Run a test configuration"""
    print(f"Running test configuration: {config_name}")
    print(f"Description: {config.get('description', 'No description')}")
    
    # Build command arguments
    cmd_args = build_command_args(config, commands)
    
    print(f"Command: {' '.join(cmd_args)}")
    print("-" * 60)
    
    # Run the command
    try:
        result = subprocess.run(cmd_args, check=False)
        return result.returncode
    except Exception as e:
        print(f"Error running test configuration: {e}")
        return 1


def list_configurations(test_config: Dict[str, Any]):
    """List available test configurations"""
    configurations = test_config.get("test_configurations", {})
    command_groups = test_config.get("command_groups", {})
    
    print("Available Test Configurations:")
    print("=" * 40)
    
    for name, config in configurations.items():
        description = config.get("description", "No description")
        test_types = ", ".join(config.get("test_types", []))
        parallel = "parallel" if config.get("parallel", True) else "sequential"
        
        print(f"\n{name}:")
        print(f"  Description: {description}")
        print(f"  Test Types: {test_types}")
        print(f"  Execution: {parallel}")
        print(f"  Timeout per test: {config.get('timeout_per_test', 30)}s")
        print(f"  Timeout per command: {config.get('timeout_per_command', 300)}s")
    
    if command_groups:
        print("\n\nAvailable Command Groups:")
        print("=" * 30)
        
        for group_name, commands in command_groups.items():
            print(f"\n{group_name}: {', '.join(commands)}")


def main():
    parser = argparse.ArgumentParser(description="Run predefined test configurations")
    parser.add_argument("--config", type=Path, default="test-config.json",
                       help="Test configuration file (default: test-config.json)")
    parser.add_argument("--list", action="store_true",
                       help="List available configurations and exit")
    parser.add_argument("configuration", nargs="?",
                       help="Configuration name to run")
    parser.add_argument("--commands", nargs="+",
                       help="Specific commands to test")
    parser.add_argument("--command-group",
                       help="Command group to test")
    
    args = parser.parse_args()
    
    # Load test configuration
    if not args.config.exists():
        print(f"Error: Configuration file {args.config} not found")
        return 1
    
    test_config = load_test_config(args.config)
    if not test_config:
        return 1
    
    # List configurations if requested
    if args.list:
        list_configurations(test_config)
        return 0
    
    # Check if configuration name is provided
    if not args.configuration:
        print("Error: Configuration name is required")
        print("\nUse --list to see available configurations")
        return 1
    
    # Get configuration
    configurations = test_config.get("test_configurations", {})
    if args.configuration not in configurations:
        print(f"Error: Configuration '{args.configuration}' not found")
        print(f"Available configurations: {', '.join(configurations.keys())}")
        return 1
    
    config = configurations[args.configuration]
    
    # Determine commands to test
    commands = args.commands
    
    # Use command group if specified
    if args.command_group:
        command_groups = test_config.get("command_groups", {})
        if args.command_group not in command_groups:
            print(f"Error: Command group '{args.command_group}' not found")
            print(f"Available groups: {', '.join(command_groups.keys())}")
            return 1
        
        group_commands = command_groups[args.command_group]
        if commands:
            # Combine group commands with specified commands
            commands.extend(group_commands)
        else:
            commands = group_commands
    
    # Run the configuration
    return run_test_configuration(args.configuration, config, commands)


if __name__ == "__main__":
    sys.exit(main())