#!/usr/bin/env python3
"""
Command Discovery Example
========================

Demonstrates the command discovery functionality for analyzing CLI commands.
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def main():
    """Main example function"""
    try:
        from genebot.cli.discovery import CommandDiscovery
        from genebot.cli.context import CLIContext
        from genebot.cli.utils.logger import CLILogger
        from genebot.cli.utils.error_handler import CLIErrorHandler
        
        print("Command Discovery Example")
        print("=" * 50)
        
        # Initialize discovery with minimal dependencies to avoid circular imports
        class SimpleContext:
            def __init__(self):
                self.force = False
                self.verbose = True
        
        class SimpleLogger:
            def debug(self, msg): pass
            def warning(self, msg): print(f"WARNING: {msg}")
            def info(self, msg): print(f"INFO: {msg}")
        
        class SimpleErrorHandler:
            pass
        
        context = SimpleContext()
        logger = SimpleLogger()
        error_handler = SimpleErrorHandler()
        
        discovery = CommandDiscovery(context, logger, error_handler)
        
        # 1. Discover all commands
        print("\n1. Discovering Commands...")
        commands = discovery.discover_commands()
        print(f"Found {len(commands)} commands")
        
        # 2. Show command statistics
        print("\n2. Command Statistics:")
        stats = discovery.get_command_statistics()
        print(f"  Total commands: {stats['total_commands']}")
        print(f"  Commands with aliases: {stats['commands_with_aliases']}")
        print(f"  Total aliases: {stats['total_aliases']}")
        print(f"  Commands with dependencies: {stats['commands_with_dependencies']}")
        print(f"  Total parameters: {stats['parameter_statistics']['total_parameters']}")
        print(f"  Required parameters: {stats['parameter_statistics']['required_parameters']}")
        print(f"  Optional parameters: {stats['parameter_statistics']['optional_parameters']}")
        
        # 3. Show most common dependencies
        print("\n3. Most Common Dependencies:")
        for dep, count in list(stats['most_common_dependencies'].items())[:5]:
            print(f"  {dep}: {count} commands")
        
        # 4. Analyze specific commands
        print("\n4. Analyzing Specific Commands:")
        interesting_commands = ['start', 'status', 'orchestrator-start', 'list-accounts']
        
        for cmd_name in interesting_commands:
            cmd_info = discovery.get_command_info(cmd_name)
            if cmd_info:
                print(f"\n  Command: {cmd_name}")
                print(f"    Class: {cmd_info.class_name}")
                print(f"    Module: {cmd_info.module_path}")
                print(f"    Aliases: {', '.join(cmd_info.aliases) if cmd_info.aliases else 'None'}")
                print(f"    Parameters: {len(cmd_info.all_parameters)} total")
                print(f"      Required: {len(cmd_info.required_params)}")
                print(f"      Optional: {len(cmd_info.optional_params)}")
                
                if cmd_info.metadata.description:
                    print(f"    Description: {cmd_info.metadata.description}")
                
                if cmd_info.metadata.dependencies:
                    print(f"    Dependencies: {', '.join(cmd_info.metadata.dependencies)}")
                
                # Show parameters
                if cmd_info.all_parameters:
                    print("    Parameters:")
                    for param in cmd_info.all_parameters[:3]:  # Show first 3
                        print(f"      - {param.name} ({param.param_type.value})")
                        if param.description:
                            print(f"        {param.description}")
        
        # 5. Find commands with potential issues
        print("\n5. Commands with Potential Issues:")
        issues = discovery.find_commands_with_issues()
        
        for issue_type, commands in issues.items():
            if commands:
                print(f"  {issue_type.replace('_', ' ').title()}: {len(commands)} commands")
                for cmd in commands[:3]:  # Show first 3
                    print(f"    - {cmd}")
                if len(commands) > 3:
                    print(f"    ... and {len(commands) - 3} more")
        
        # 6. Validate command registration
        print("\n6. Command Registration Validation:")
        validation = discovery.validate_command_registration()
        print(f"  Total commands: {validation['total_commands']}")
        print(f"  Valid commands: {validation['valid_commands']}")
        print(f"  Invalid commands: {validation['invalid_commands']}")
        
        if validation['errors']:
            print("  Errors found:")
            for error in validation['errors'][:3]:
                print(f"    - {error}")
        
        # 7. Show commands by dependency
        print("\n7. Commands by Dependency:")
        test_dependencies = ['database', 'orchestrator', 'logging']
        
        for dep in test_dependencies:
            dependent_commands = discovery.get_commands_by_dependency(dep)
            if dependent_commands:
                print(f"  {dep}: {len(dependent_commands)} commands")
                for cmd in dependent_commands[:3]:
                    print(f"    - {cmd}")
        
        print("\n" + "=" * 50)
        print("Command Discovery Example completed successfully!")
        
    except Exception as e:
        print(f"Error running example: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)