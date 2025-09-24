#!/usr/bin/env python3
"""
Demonstration script for the cleanup utilities.
Shows how to use each component safely.
"""

import sys
from pathlib import Path

# Add the scripts directory to the path
sys.path.insert(0, str(Path(__file__).parent))

    BackupManager, DependencyChecker, SafeFileRemover,
    ModuleConsolidator, ImportCleaner, CleanupOrchestrator
)


def demo_backup_manager():
    """Demonstrate backup functionality."""
    print("=== Backup Manager Demo ===")
    
    backup_manager = BackupManager("demo_backups")
    
    # Create a test file
    test_file = Path("demo_test_file.py")
    test_file.write_text("""
import os
import sys
import unused_module

def hello():
    print("Hello from", os.path.basename(__file__))
""")
    
    # Create backup
    backup_path = backup_manager.create_backup([str(test_file)])
    print(f"Created backup at: {backup_path}")
    
    # Modify the file
    test_file.write_text("# Modified content")
    print("Modified original file")
    
    # Restore backup
    success = backup_manager.restore_backup(backup_path)
    print(f"Backup restoration: {'SUCCESS' if success else 'FAILED'}")
    
    # Check restored content
    restored_content = test_file.read_text()
    print(f"File restored: {'YES' if 'import os' in restored_content else 'NO'}")
    
    # Cleanup
    test_file.unlink()
    print("Demo file cleaned up\n")


def demo_import_cleaner():
    """Demonstrate import cleaning functionality."""
    print("=== Import Cleaner Demo ===")
    
    # Create test files
    test_file = Path("demo_imports.py")
    test_file.write_text("""
import os
import sys
import json
import unused_module1
import unused_module2

def main():
    print("Current directory:", os.getcwd())
    return json.dumps({"status": "ok"})
""")
    
    import_cleaner = ImportCleaner(".", exclude_dirs=['venv', '.venv', 'demo_backups'])
    
    # Find unused imports
    unused_imports = import_cleaner.find_unused_imports(str(test_file))
    print(f"Found {len(unused_imports)} unused imports:")
    for imp in unused_imports:
        print(f"  - {imp}")
    
    # Clean imports
    result = import_cleaner.clean_imports_in_file(str(test_file))
    print(f"Cleanup result: {result['status']}")
    print(f"Removed {len(result['unused_imports'])} imports")
    
    # Show cleaned content
    cleaned_content = test_file.read_text()
    print("Cleaned file still has 'import os':", 'import os' in cleaned_content)
    print("Cleaned file no longer has 'unused_module1':", 'unused_module1' not in cleaned_content)
    
    # Cleanup
    test_file.unlink()
    print("Demo file cleaned up\n")


def demo_dependency_checker():
    """Demonstrate dependency checking."""
    print("=== Dependency Checker Demo ===")
    
    # Create test files
    module1 = Path("demo_module1.py")
    module1.write_text("""
def utility_function():
    return "utility"

class UtilityClass:
    pass
""")
    
    module2 = Path("demo_module2.py")
    module2.write_text("""
from demo_module1 import utility_function

def main():
    return utility_function()
""")
    
    dependency_checker = DependencyChecker(".", exclude_dirs=['venv', '.venv', 'demo_backups'])
    
    # Check if module1 is safe to remove
    is_safe, dependents = dependency_checker.is_safe_to_remove("demo_module1.py")
    print(f"demo_module1.py safe to remove: {is_safe}")
    print(f"Dependents: {dependents}")
    
    # Check if module2 is safe to remove
    is_safe, dependents = dependency_checker.is_safe_to_remove("demo_module2.py")
    print(f"demo_module2.py safe to remove: {is_safe}")
    print(f"Dependents: {dependents}")
    
    # Cleanup
    module1.unlink()
    module2.unlink()
    print("Demo files cleaned up\n")


def demo_safe_file_remover():
    """Demonstrate safe file removal."""
    print("=== Safe File Remover Demo ===")
    
    # Create test files
    safe_file = Path("demo_safe_to_remove.py")
    safe_file.write_text("# This file has no dependencies")
    
    file_remover = SafeFileRemover(".")
    
    # Try to remove the file
    results = file_remover.remove_files_safely([str(safe_file)])
    
    for file_path, status in results.items():
        print(f"{file_path}: {status}")
    
    print("Demo completed\n")


def demo_orchestrator():
    """Demonstrate the full orchestrator."""
    print("=== Cleanup Orchestrator Demo ===")
    
    # Create some test files
    test_files = []
    
    # File with unused imports
    file1 = Path("demo_orchestrator_1.py")
    file1.write_text("""
import os
import sys
import unused_import

def main():
    print(os.getcwd())
""")
    test_files.append(file1)
    
    # Similar file for consolidation
    file2 = Path("demo_orchestrator_2.py")
    file2.write_text("""
import os
import sys

def main():
    print(os.getcwd())
""")
    test_files.append(file2)
    
    orchestrator = CleanupOrchestrator(".")
    
    # Run cleanup with conservative settings
    config = {
        'remove_duplicates': False,  # Skip for demo safety
        'consolidate_modules': False,  # Skip for demo to avoid creating many files
        'clean_imports': True,
        'similarity_threshold': 0.8,
        'force_removal': False
    }
    
    results = orchestrator.run_full_cleanup(config)
    
    print(f"Overall status: {results['overall_status']}")
    
    for operation, details in results.get('operations', {}).items():
        print(f"{operation}: {details.get('status', 'UNKNOWN')}")
    
    # Cleanup test files
    for test_file in test_files:
        if test_file.exists():
            test_file.unlink()
    
    print("Demo files cleaned up\n")


def main():
    """Run all demonstrations."""
    print("Cleanup Utilities Demonstration")
    print("=" * 50)
    print()
    
    try:
        demo_backup_manager()
        demo_import_cleaner()
        demo_dependency_checker()
        demo_safe_file_remover()
        demo_orchestrator()
        
        print("All demonstrations completed successfully!")
        
    except Exception as e:
        print(f"Demo failed: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())