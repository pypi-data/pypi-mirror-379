#!/usr/bin/env python3
"""
Logging Configuration Migration Tool

This script provides a command-line interface for migrating legacy logging
configurations to the centralized logging system.
"""

import argparse
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

    ConfigurationMigrator, 
    ConfigurationValidator, 
    LegacyConfigDetector,
    CompatibilityLayer,
    create_migration_script
)
from genebot.logging.config import LoggingConfig


def scan_command(args):
    pass
    """Scan for legacy logging configurations."""
    print(f"Scanning for legacy logging configurations in: {args.path}")
    
    detector = LegacyConfigDetector()
    legacy_configs = detector.find_legacy_configs(Path(args.path))
    
    if not legacy_configs:
    
        pass
    pass
        print("No legacy logging configurations found.")
        return
    
    print(f"\nFound {len(legacy_configs)} legacy configuration files:")
    
    for config_path in legacy_configs:
    pass
        print(f"\n📁 {config_path}")
        
        if config_path.suffix == '.py':
    
        pass
    pass
            info = detector.analyze_python_logging_config(config_path)
        elif config_path.suffix in ['.yaml', '.yml']:
    
        pass
    pass
            info = detector.analyze_yaml_logging_config(config_path)
        else:
    pass
            continue
        
        print(f"   Type: {info['type']}")
        print(f"   Level: {info['level']}")
        
        if info['handlers']:
    
        pass
    pass
            print(f"   Handlers: {', '.join(info['handlers'])}")
        
        if info['formatters']:
    
        pass
    pass
            print(f"   Formatters: {', '.join(info['formatters'])}")
        
        if info['issues']:
    
        pass
    pass
            print(f"   Issues: {', '.join(info['issues'])}")


def migrate_command(args):
    pass
    """Migrate legacy logging configurations."""
    print(f"Migrating logging configurations in: {args.path}")
    
    migrator = ConfigurationMigrator(backup_dir=Path(args.backup_dir))
    
    if args.file:
    
        pass
    pass
        # Migrate single file
        config_path = Path(args.file)
        result = migrator.migrate_config_file(config_path)
        results = [result]
    else:
    pass
        # Migrate all configurations
        results = migrator.migrate_all_configs(Path(args.path))
    
    print(f"\nMigration completed. Processed {len(results)} configurations:")
    
    successful_migrations = []
    
    for result in results:
    pass
        if result.success:
    
        pass
    pass
            print(f"✓ {result.message}")
            if result.backup_path:
    
        pass
    pass
                print(f"  📦 Backup: {result.backup_path}")
            if result.warnings:
    
        pass
    pass
                for warning in result.warnings:
    pass
                    print(f"  ⚠️  Warning: {warning}")
            
            if result.migrated_config:
    
        pass
    pass
                successful_migrations.append(result.migrated_config)
        else:
    pass
            print(f"✗ {result.message}")
    
    # Save migrated configurations if requested
    if args.output and successful_migrations:
    
        pass
    pass
        output_path = Path(args.output)
        
        if len(successful_migrations) == 1:
    
        pass
    pass
            # Save single configuration
            successful_migrations[0].save_to_file(output_path)
            print(f"\n💾 Saved migrated configuration to: {output_path}")
        else:
    pass
            # Save multiple configurations with numbered names
            for i, config in enumerate(successful_migrations):
    pass
                numbered_path = output_path.parent / f"{output_path.stem}_{i+1}{output_path.suffix}"
                config.save_to_file(numbered_path)
                print(f"💾 Saved migrated configuration {i+1} to: {numbered_path}")


def validate_command(args):
    pass
    """Validate logging configuration."""
    print(f"Validating logging configuration: {args.config}")
    
    try:
    pass
        config = LoggingConfig.from_file(args.config)
        
        # Validate configuration
        is_valid, issues = ConfigurationValidator.validate_config(config)
        
        if is_valid:
    
        pass
    pass
            print("✓ Configuration validation passed")
        else:
    pass
            print("✗ Configuration validation failed:")
            for issue in issues:
    pass
                print(f"  - {issue}")
        
        # Test logging functionality if requested
        if args.test_logging:
    
        pass
    pass
            print("\nTesting logging functionality...")
            test_passed, test_issues = ConfigurationValidator.test_logging_functionality(config)
            
            if test_passed:
    
        pass
    pass
                print("✓ Logging functionality test passed")
            else:
    pass
                print("✗ Logging functionality test failed:")
                for issue in test_issues:
    pass
                    print(f"  - {issue}")
        
    except Exception as e:
    pass
    pass
        print(f"✗ Failed to load configuration: {e}")


def backup_command(args):
    pass
    """Create backup of current logging configuration."""
    print(f"Creating backup of logging configurations in: {args.path}")
    
    migrator = ConfigurationMigrator(backup_dir=Path(args.backup_dir))
    detector = LegacyConfigDetector()
    
    legacy_configs = detector.find_legacy_configs(Path(args.path))
    
    if not legacy_configs:
    
        pass
    pass
        print("No logging configurations found to backup.")
        return
    
    backup_paths = []
    for config_path in legacy_configs:
    pass
        try:
    pass
            backup_path = migrator.create_backup(config_path)
            backup_paths.append(backup_path)
            print(f"✓ Backed up {config_path} to {backup_path}")
        except Exception as e:
    pass
    pass
            print(f"✗ Failed to backup {config_path}: {e}")
    
    print(f"\nCreated {len(backup_paths)} backups in: {migrator.backup_dir}")


def restore_command(args):
    pass
    """Restore logging configuration from backup."""
    backup_path = Path(args.backup)
    
    if not backup_path.exists():
    
        pass
    pass
        return
    
    # Determine original path from backup name
    if '.backup' in backup_path.name:
    
        pass
    pass
        original_name = backup_path.name.split('.backup')[0]
        original_path = backup_path.parent.parent / original_name
    else:
    pass
        return
    
    if args.target:
    
        pass
    pass
        original_path = Path(args.target)
    
    try:
    pass
        import shutil
    except Exception as e:
    pass
    pass
def generate_script_command(args):
    pass
    """Generate standalone migration script."""
    output_path = Path(args.output)
    root_path = Path(args.path)
    
    try:
    pass
        create_migration_script(output_path, root_path)
        print(f"✓ Generated migration script: {output_path}")
        print(f"  Run with: python {output_path}")
    except Exception as e:
    pass
    pass
        print(f"✗ Failed to generate migration script: {e}")


def main():
    pass
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Logging Configuration Migration Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    pass
  # Scan for legacy configurations
  python logging_migration_tool.py scan /path/to/project

  # Migrate all configurations
  python logging_migration_tool.py migrate /path/to/project --output new_config.yaml

  # Migrate single file
  python logging_migration_tool.py migrate /path/to/project --file config/logging.py

  # Validate configuration
  python logging_migration_tool.py validate config/logging_config.yaml --test-logging

  # Create backup
  python logging_migration_tool.py backup /path/to/project

  # Restore from backup
  python logging_migration_tool.py restore config/backups/logging.py.20250920_120000.backup

  # Generate migration script
  python logging_migration_tool.py generate-script /path/to/project --output migrate_logging.py
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Scan command
    scan_parser = subparsers.add_parser('scan', help='Scan for legacy logging configurations')
    scan_parser.add_argument('path', help='Path to scan for configurations')
    scan_parser.set_defaults(func=scan_command)
    
    # Migrate command
    migrate_parser = subparsers.add_parser('migrate', help='Migrate legacy logging configurations')
    migrate_parser.add_argument('path', help='Path containing configurations to migrate')
    migrate_parser.add_argument('--file', help='Migrate specific file instead of scanning directory')
    migrate_parser.add_argument('--output', help='Output path for migrated configuration')
    migrate_parser.add_argument('--backup-dir', default='config/backups', help='Backup directory')
    migrate_parser.set_defaults(func=migrate_command)
    
    # Validate command
    validate_parser = subparsers.add_parser('validate', help='Validate logging configuration')
    validate_parser.add_argument('config', help='Path to configuration file to validate')
    validate_parser.add_argument('--test-logging', action='store_true', help='Test actual logging functionality')
    validate_parser.set_defaults(func=validate_command)
    
    # Backup command
    backup_parser = subparsers.add_parser('backup', help='Create backup of logging configurations')
    backup_parser.add_argument('path', help='Path containing configurations to backup')
    backup_parser.add_argument('--backup-dir', default='config/backups', help='Backup directory')
    backup_parser.set_defaults(func=backup_command)
    
    # Restore command
    restore_parser = subparsers.add_parser('restore', help='Restore configuration from backup')
    restore_parser.add_argument('backup', help='Path to backup file')
    restore_parser.add_argument('--target', help='Target path for restored file (auto-detected if not specified)')
    restore_parser.set_defaults(func=restore_command)
    
    # Generate script command
    generate_parser = subparsers.add_parser('generate-script', help='Generate standalone migration script')
    generate_parser.add_argument('path', help='Project root path')
    generate_parser.add_argument('--output', default='migrate_logging.py', help='Output script path')
    generate_parser.set_defaults(func=generate_script_command)
    
    args = parser.parse_args()
    
    if not args.command:
    
        pass
    pass
        parser.print_help()
        return
    
    try:
    pass
        args.func(args)
    except KeyboardInterrupt:
    pass
    pass
        print("\n\nOperation cancelled by user.")
    except Exception as e:
    pass
    pass
        print(f"\n✗ Unexpected error: {e}")
        if '--debug' in sys.argv:
    
        pass
    pass
            import traceback


if __name__ == "__main__":
    
        pass
    pass