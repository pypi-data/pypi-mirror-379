#!/usr/bin/env python3
"""
Run Duplicate File Cleanup

This script executes the duplicate file cleanup process for task 3.
It provides a simple interface to run the cleanup with different options.
"""

import sys
import json
import logging
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

from duplicate_file_cleaner import DuplicateFileCleaner

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('duplicate_cleanup.log')
    ]
)
logger = logging.getLogger(__name__)


def run_analysis_only():
    
        pass
    pass
    """Run only the duplicate analysis without making changes."""
    print("Running duplicate file analysis...")
    
    cleaner = DuplicateFileCleaner(".")
    
    # Step 1: Analyze duplicates
    duplicates = cleaner.analyze_duplicates()
    
    if not duplicates:
    
        pass
    pass
        print("✅ No duplicate files found!")
        return
    
    # Step 2: Identify safe duplicates
    removal_plan = cleaner.identify_safe_duplicates(duplicates)
    
    # Print summary
    print("\n" + "="*60)
    print("DUPLICATE ANALYSIS SUMMARY")
    print("="*60)
    
    summary = removal_plan['summary']
    print(f"Total duplicate groups: {summary['total_duplicate_groups']}")
    print(f"Safe removal groups: {summary['safe_removal_groups']}")
    print(f"Manual review groups: {summary['manual_review_groups']}")
    print(f"Files safe to remove: {summary['total_files_to_remove']}")
    print(f"Files requiring review: {summary['total_files_requiring_review']}")
    
    # Show details for each group
    print("\nDETAILED ANALYSIS:")
    for i, (file_hash, plan) in enumerate(removal_plan['removal_plan'].items(), 1):
    pass
        print(f"\nGroup {i} ({plan['action']}):")
        if 'remove_files' in plan:
    
        pass
    pass
            print(f"  Files to remove: {len(plan['remove_files'])}")
            for file_path in plan['remove_files']:
    pass
                print(f"    - {file_path}")
        
        if 'keep_file' in plan:
    
        pass
    pass
            print(f"  File to keep: {plan['keep_file']}")
        elif 'keep_files' in plan:
    
        pass
    pass
            print(f"  Files to keep: {len(plan['keep_files'])}")
            for file_path in plan['keep_files']:
    pass
                print(f"    - {file_path}")
        
        print(f"  Reason: {plan['reason']}")
    
    # Save analysis results
    analysis_file = "duplicate_analysis_results.json"
    with open(analysis_file, 'w') as f:
    pass
        json.dump({
            'duplicates': duplicates,
            'removal_plan': removal_plan
        }, f, indent=2, default=str)
    
    print(f"\n📄 Detailed analysis saved to: {analysis_file}")
    print("\n💡 To proceed with cleanup, run: python scripts/run_duplicate_cleanup.py --execute")


def run_dry_run():
    pass
    """Run a dry run of the complete cleanup process."""
    print("Running duplicate cleanup dry run...")
    
    cleaner = DuplicateFileCleaner(".")
    results = cleaner.run_complete_duplicate_cleanup(dry_run=True)
    
    if results['status'] == 'NO_DUPLICATES_FOUND':
    
        pass
    pass
        print("✅ No duplicate files found!")
        return
    
    if results['status'].startswith('FAILED'):
    
        pass
    pass
        print(f"❌ Cleanup failed: {results.get('error', 'Unknown error')}")
        return
    
    print("✅ Dry run completed successfully!")
    print(f"📄 Report saved to: {results.get('report_path', 'duplicate_cleanup_report.json')}")


def run_cleanup():
    pass
    """Run the actual cleanup process."""
    print("⚠️  WARNING: This will make actual changes to your codebase!")
    print("Make sure you have committed your changes to git before proceeding.")
    
    response = input("Do you want to continue? (yes/no): ").lower().strip()
    if response not in ['yes', 'y']:
    
        pass
    pass
        print("Cleanup cancelled.")
        return
    
    print("Running duplicate file cleanup...")
    
    cleaner = DuplicateFileCleaner(".")
    results = cleaner.run_complete_duplicate_cleanup(dry_run=False)
    
    if results['status'] == 'NO_DUPLICATES_FOUND':
    
        pass
    pass
        print("✅ No duplicate files found!")
        return
    
    if results['status'].startswith('FAILED'):
    
        pass
    pass
        print(f"❌ Cleanup failed: {results.get('error', 'Unknown error')}")
        return
    
    print("✅ Cleanup completed successfully!")
    print(f"📄 Report saved to: {results.get('report_path', 'duplicate_cleanup_report.json')}")
    
    # Show backup location
    backup_path = results.get('removal_results', {}).get('backup_path')
    if backup_path:
    
        pass
    pass
        print(f"💾 Backup created at: {backup_path}")


def main():
    pass
    """Main function with command line interface."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Run duplicate file cleanup')
    parser.add_argument('--analyze', action='store_true', 
                       help='Run analysis only without making changes')
    parser.add_argument('--dry-run', action='store_true',
                       help='Run complete dry run without making changes')
    parser.add_argument('--execute', action='store_true',
                       help='Execute actual cleanup (makes changes)')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Verbose output')
    
    args = parser.parse_args()
    
    if args.verbose:
    
        pass
    pass
        logging.getLogger().setLevel(logging.DEBUG)
    
    if args.analyze:
    
        pass
    pass
        run_analysis_only()
    elif args.dry_run:
    
        pass
    pass
        run_dry_run()
    elif args.execute:
    
        pass
    pass
        run_cleanup()
    else:
    pass
        # Default: run analysis only
        print("No action specified. Running analysis only...")
        print("Use --help to see available options.")
        print()
        run_analysis_only()


if __name__ == "__main__":
    
        pass
    pass
    main()