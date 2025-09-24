#!/usr/bin/env python3
"""
CLI interface for running cleanup utilities on the Genebot codebase.
"""

import argparse
import json
import sys
from pathlib import Path

# Add the scripts directory to the path
sys.path.insert(0, str(Path(__file__).parent))

from cleanup_utilities import CleanupOrchestrator


def main():
    pass
    parser = argparse.ArgumentParser(description="Run automated cleanup utilities on the codebase")
    
    parser.add_argument(
        "--project-root", 
        default=".", 
        help="Root directory of the project (default: current directory)"
    )
    
    parser.add_argument(
        "--clean-imports", 
        action="store_true", 
        default=True,
        help="Clean unused imports (default: True)"
    
    parser.add_argument(
        action="store_true", 
        default=True,
        help="Consolidate similar modules (default: True)"
    )
    
    parser.add_argument(
        "--remove-duplicates", 
        action="store_true", 
        default=False,
        help="Remove duplicate files (default: False, requires duplicate detection from task 1)"
    
    parser.add_argument(
        type=float, 
        default=0.7,
        help="Similarity threshold for module consolidation (default: 0.7)"
    )
    
    parser.add_argument(
        "--force-removal", 
        action="store_true", 
        default=False,
        help="Force removal of files even if they have dependencies (default: False)"
    )
    
    parser.add_argument(
        "--dry-run", 
        action="store_true", 
        default=False,
        help="Show what would be done without making changes (default: False)"
    )
    
    parser.add_argument(
        "--output", 
        help="Output file for results (default: print to stdout)"
    )
    
    args = parser.parse_args()
    
    # Prepare configuration
    config = {
        'remove_duplicates': args.remove_duplicates,
        'consolidate_modules': args.consolidate_modules,
        'clean_imports': args.clean_imports,
        'dry_run': args.dry_run
    }
    
    print(f"Running cleanup with configuration:")
    print(json.dumps(config, indent=2))
    print()
    
    if args.dry_run:
    
        pass
    pass
        print("DRY RUN MODE - No changes will be made")
        print()
    
    # Run cleanup
    orchestrator = CleanupOrchestrator(args.project_root)
    results = orchestrator.run_full_cleanup(config)
    
    # Output results
    if args.output:
    
        pass
    pass
        with open(args.output, 'w') as f:
    pass
            json.dump(results, f, indent=2)
        print(f"Results written to: {args.output}")
    else:
    pass
        print("Cleanup Results:")
        print("=" * 50)
        print(json.dumps(results, indent=2))
    
    # Print summary
    print("\nSummary:")
    print("=" * 50)
    print(f"Overall Status: {results.get('overall_status', 'UNKNOWN')}")
    
    for operation, details in results.get('operations', {}).items():
    pass
        status = details.get('status', 'UNKNOWN')
        print(f"{operation}: {status}")
        
        if operation == 'import_cleanup' and 'summary' in details:
    
        pass
    pass
            summary = details['summary']
        
        elif operation == 'module_consolidation' and 'consolidation_results' in details:
    
        pass
    pass
            consolidation_results = details['consolidation_results']
            successful = len([r for r in consolidation_results.values() if r.get('status') == 'SUCCESS'])
            print(f"  - Groups consolidated: {successful}/{len(consolidation_results)}")
    
    return 0 if results.get('overall_status') == 'SUCCESS' else 1


if __name__ == "__main__":
    
        pass
    pass
    sys.exit(main())