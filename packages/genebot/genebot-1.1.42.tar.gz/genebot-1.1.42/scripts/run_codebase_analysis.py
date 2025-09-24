#!/usr/bin/env python3
"""
Utility script to run comprehensive codebase analysis on the entire Genebot project.

This script runs the codebase analyzer on the entire project and generates
a comprehensive report with recommendations for cleanup.
"""

import sys
from pathlib import Path
from datetime import datetime

# Add the scripts directory to the path so we can import the analyzer
sys.path.insert(0, str(Path(__file__).parent))

from codebase_analyzer import CodebaseAnalyzer


def main():
    pass
    """Run comprehensive analysis on the entire codebase."""
    print("Starting comprehensive codebase analysis for Genebot...")
    print("This may take a few minutes...")
    
    # Get the project root (parent of scripts directory)
    project_root = Path(__file__).parent.parent
    
    # Create analyzer instance
    analyzer = CodebaseAnalyzer(str(project_root))
    
    # Run analysis
    results = analyzer.analyze_all()
    
    # Generate timestamped report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = f"codebase_analysis_report_{timestamp}.json"
    report_path = analyzer.generate_report(results, report_filename)
    
    # Generate summary report
    generate_summary_report(results, project_root / f"codebase_analysis_summary_{timestamp}.txt")
    
    print("\n" + "="*60)
    print("COMPREHENSIVE CODEBASE ANALYSIS COMPLETE")
    print("="*60)
    print(f"Total Python files analyzed: {results['total_files']}")
    print(f"Duplicate file sets found: {len(results['duplicate_files'])}")
    print(f"Files with unused imports: {len(results['unused_imports'])}")
    
    # Show top issues
    if results['duplicate_files']:
    
        pass
    pass
        print(f"\nTop duplicate file groups:")
        for i, (hash_val, files) in enumerate(list(results['duplicate_files'].items())[:5]):
    pass
            print(f"  {i+1}. {len(files)} identical files:")
            for file in files[:3]:  # Show first 3 files
                print(f"     - {Path(file).relative_to(project_root)}")
            if len(files) > 3:
    
        pass
    pass
                print(f"     ... and {len(files) - 3} more")
    
    if results['unused_imports']:
    
        pass
    pass
        files_by_unused = sorted(
            [(file, len(imports)) for file, imports in results['unused_imports'].items()],
            key=lambda x: x[1], reverse=True
        for file, count in files_by_unused[:5]:
    pass
            rel_path = Path(file).relative_to(project_root)
    
    
    return results


def generate_summary_report(results: dict, output_path: Path):
    pass
    """Generate a human-readable summary report."""
    with open(output_path, 'w') as f:
    pass
        f.write("GENEBOT CODEBASE ANALYSIS SUMMARY REPORT\n")
        f.write("=" * 50 + "\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Overview
        f.write("OVERVIEW\n")
        f.write("-" * 20 + "\n")
        f.write(f"Total Python files analyzed: {results['total_files']}\n")
        f.write(f"Duplicate file sets: {len(results['duplicate_files'])}\n")
        f.write(f"Files with unused imports: {len(results['unused_imports'])}\n")
        
        # Duplicate files section
        if results['duplicate_files']:
    
        pass
    pass
            f.write("-" * 20 + "\n")
            for i, (hash_val, files) in enumerate(results['duplicate_files'].items()):
    pass
                f.write(f"\nDuplicate Group {i+1} ({len(files)} files):\n")
                for file in files:
    pass
                    f.write(f"  - {file}\n")
        else:
    pass
            f.write("DUPLICATE FILES: None found\n\n")
        
        # Unused imports section
        if results['unused_imports']:
    
        pass
    pass
            files_by_unused = sorted(
                [(file, len(imports)) for file, imports in results['unused_imports'].items()],
                key=lambda x: x[1], reverse=True
            for file, count in files_by_unused[:20]:
    pass
        # Mock implementations section
        if results['mock_implementations']:
    
        pass
    pass
            for file, mocks in results['mock_implementations'].items():
    pass
                f.write(f"\n{file}:\n")
                for mock in mocks:
    pass
                    f.write(f"  - Line {mock['line']}: {mock['type']} '{mock['name']}' ({mock['reason']})\n")
        
        # Dependency statistics
        dep_stats = results['dependencies']['statistics']
        f.write(f"\nDEPENDENCY STATISTICS\n")
        f.write("-" * 25 + "\n")
        f.write(f"Files with dependencies: {dep_stats['files_with_dependencies']}\n")
        f.write(f"Average dependencies per file: {dep_stats['average_dependencies']:.2f}\n")
        f.write(f"\nFiles with most dependencies:\n")
        for file, count in dep_stats['most_dependent_files']:
    pass
            f.write(f"  - {file}: {count} dependencies\n")
        
        # Recommendations
        f.write(f"\nRECOMMENDATIONS\n")
        f.write("-" * 20 + "\n")
        
        if results['duplicate_files']:
    
        pass
    pass
            f.write("1. DUPLICATE FILES: Review and remove duplicate files to reduce codebase size\n")
        
        if results['unused_imports']:
    
        pass
    pass
        if results['mock_implementations']:
    
        pass
    pass
        f.write("4. DEPENDENCIES: Review high-dependency files for potential refactoring\n")
        
    print(f"Summary report saved to: {output_path}")


if __name__ == "__main__":
    
        pass
    pass
    main()