#!/usr/bin/env python3
"""
Duplicate File Cleaner for Genebot Trading Bot

This script implements task 3: Analyze and clean duplicate files
- Run duplicate detection across entire codebase
- Identify which duplicates are safe to remove
- Remove duplicate files while preserving functionality
- Update import statements to reference consolidated files

Requirements: 1.1
"""

import os
import ast
import json
import logging
from pathlib import Path
from datetime import datetime

# Import existing utilities
from codebase_analyzer import CodebaseAnalyzer, DuplicateFileDetector
from cleanup_utilities import BackupManager, DependencyChecker, SafeFileRemover

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class DuplicateFileCleaner:
    """Main class for analyzing and cleaning duplicate files."""
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root).resolve()
        self.analyzer = CodebaseAnalyzer(str(self.project_root))
        self.duplicate_detector = DuplicateFileDetector()
        self.dependency_checker = DependencyChecker(str(self.project_root))
        self.backup_manager = BackupManager("backups/duplicate_cleanup")
        self.file_remover = SafeFileRemover(str(self.project_root))
        
        # Track operations for reporting
        self.operations_log = []
        self.import_updates = []
        
    def analyze_duplicates(self) -> Dict:
        """Run duplicate detection across entire codebase."""
        logger.info("Starting duplicate file analysis...")
        
        # Get all Python files
        python_files = self.analyzer.scan_python_files()
        logger.info(f"Scanning {len(python_files)} Python files for duplicates")
        
        # Find duplicates using existing detector
        duplicates = self.duplicate_detector.find_duplicates(python_files)
        
        # Enhance duplicate analysis with additional metadata
        enhanced_duplicates = {}
        
        for file_hash, file_list in duplicates.items():
            if len(file_list) <= 1:
                continue
                
            # Analyze each duplicate group
            group_info = {
                'files': file_list,
                'file_count': len(file_list),
                'file_sizes': [],
                'creation_times': [],
                'safety_analysis': {},
                'recommended_action': 'ANALYZE'
            }
            
            # Get file metadata
            for file_path in file_list:
                try:
                    file_obj = Path(file_path)
                    if file_obj.exists():
                        stat = file_obj.stat()
                        group_info['file_sizes'].append(stat.st_size)
                        group_info['creation_times'].append(stat.st_mtime)
                except Exception as e:
                    logger.warning(f"Could not get metadata for {file_path}: {e}")
            
            # Analyze safety of removing each file
            for file_path in file_list:
                is_safe, dependents = self.dependency_checker.is_safe_to_remove(file_path)
                group_info['safety_analysis'][file_path] = {
                    'safe_to_remove': is_safe,
                    'dependents': dependents,
                    'dependent_count': len(dependents)
                }
            
            # Determine recommended action
            group_info['recommended_action'] = self._determine_recommended_action(group_info)
            
            enhanced_duplicates[file_hash] = group_info
        
        logger.info(f"Found {len(enhanced_duplicates)} groups of duplicate files")
        return enhanced_duplicates
    
    def _determine_recommended_action(self, group_info: Dict) -> str:
        """Determine the recommended action for a duplicate group."""
        files = group_info['files']
        safety_analysis = group_info['safety_analysis']
        
        # Count safe and unsafe files
        safe_files = [f for f in files if safety_analysis[f]['safe_to_remove']]
        unsafe_files = [f for f in files if not safety_analysis[f]['safe_to_remove']]
        
        if len(safe_files) == len(files):
            # All files are safe to remove - keep one, remove others
            return "REMOVE_ALL_BUT_ONE"
        elif len(safe_files) > 0:
            # Some files are safe to remove
            return "REMOVE_SAFE_DUPLICATES"
        else:
            # No files are safe to remove - need manual review
            return "MANUAL_REVIEW_REQUIRED"
    
    def identify_safe_duplicates(self, duplicates: Dict) -> Dict:
        """Identify which duplicates are safe to remove."""
        logger.info("Identifying safe duplicates to remove...")
        
        safe_to_remove = []
        requires_review = []
        removal_plan = {}
        
        for file_hash, group_info in duplicates.items():
            files = group_info['files']
            safety_analysis = group_info['safety_analysis']
            recommended_action = group_info['recommended_action']
            
            if recommended_action == "REMOVE_ALL_BUT_ONE":
                # Keep the file with the most dependencies or the oldest one
                files_with_deps = [(f, len(safety_analysis[f]['dependents'])) for f in files]
                files_with_deps.sort(key=lambda x: (-x[1], Path(x[0]).stat().st_mtime))
                
                keep_file = files_with_deps[0][0]
                remove_files = [f for f in files if f != keep_file]
                
                removal_plan[file_hash] = {
                    'action': 'REMOVE_DUPLICATES',
                    'keep_file': keep_file,
                    'remove_files': remove_files,
                    'reason': 'All duplicates are safe to remove'
                }
                safe_to_remove.extend(remove_files)
                
            elif recommended_action == "REMOVE_SAFE_DUPLICATES":
                # Remove only the safe duplicates
                safe_files = [f for f in files if safety_analysis[f]['safe_to_remove']]
                unsafe_files = [f for f in files if not safety_analysis[f]['safe_to_remove']]
                
                removal_plan[file_hash] = {
                    'action': 'REMOVE_SAFE_ONLY',
                    'keep_files': unsafe_files,
                    'remove_files': safe_files,
                    'reason': 'Remove only safe duplicates, keep files with dependencies'
                }
                safe_to_remove.extend(safe_files)
                
            else:
                # Manual review required
                removal_plan[file_hash] = {
                    'action': 'MANUAL_REVIEW',
                    'files': files,
                    'reason': 'All files have dependencies - manual review required'
                }
                requires_review.extend(files)
        
        result = {
            'safe_to_remove': safe_to_remove,
            'requires_review': requires_review,
            'removal_plan': removal_plan,
            'summary': {
                'total_duplicate_groups': len(duplicates),
                'safe_removal_groups': len([p for p in removal_plan.values() if p['action'] in ['REMOVE_DUPLICATES', 'REMOVE_SAFE_ONLY']]),
                'manual_review_groups': len([p for p in removal_plan.values() if p['action'] == 'MANUAL_REVIEW']),
                'total_files_to_remove': len(safe_to_remove),
                'total_files_requiring_review': len(requires_review)
            }
        }
        
        logger.info(f"Identified {len(safe_to_remove)} files safe to remove")
        logger.info(f"Identified {len(requires_review)} files requiring manual review")
        
        return result
    
    def remove_duplicate_files(self, removal_plan: Dict, dry_run: bool = False) -> Dict:
        """Remove duplicate files while preserving functionality."""
        logger.info(f"{'DRY RUN: ' if dry_run else ''}Starting duplicate file removal...")
        
        results = {
            'timestamp': datetime.now().isoformat(),
            'dry_run': dry_run,
            'operations': [],
            'files_removed': [],
            'files_kept': [],
            'errors': [],
            'backup_path': None
        }
        
        # Collect all files to be removed for backup
        all_files_to_remove = []
        for plan in removal_plan['removal_plan'].values():
            if 'remove_files' in plan:
                all_files_to_remove.extend(plan['remove_files'])
        
        if not all_files_to_remove:
            logger.info("No files to remove")
            return results
        
        # Create backup before removal
        if not dry_run and all_files_to_remove:
            try:
                backup_path = self.backup_manager.create_backup(all_files_to_remove)
                results['backup_path'] = backup_path
                logger.info(f"Created backup at: {backup_path}")
            except Exception as e:
                error_msg = f"Failed to create backup: {e}"
                logger.error(error_msg)
                results['errors'].append(error_msg)
                return results
        
        # Process each duplicate group
        for file_hash, plan in removal_plan['removal_plan'].items():
            if plan['action'] in ['REMOVE_DUPLICATES', 'REMOVE_SAFE_ONLY']:
                operation = {
                    'file_hash': file_hash,
                    'action': plan['action'],
                    'files_to_remove': plan['remove_files'],
                    'files_to_keep': plan.get('keep_file') or plan.get('keep_files', []),
                    'results': {}
                }
                
                # Remove files
                for file_path in plan['remove_files']:
                    try:
                        if dry_run:
                            operation['results'][file_path] = 'DRY_RUN_WOULD_REMOVE'
                            logger.info(f"DRY RUN: Would remove {file_path}")
                        else:
                            file_obj = Path(file_path)
                            if file_obj.exists():
                                file_obj.unlink()
                                operation['results'][file_path] = 'REMOVED'
                                results['files_removed'].append(file_path)
                                logger.info(f"Removed duplicate file: {file_path}")
                            else:
                                operation['results'][file_path] = 'FILE_NOT_FOUND'
                                logger.warning(f"File not found: {file_path}")
                    except Exception as e:
                        error_msg = f"Failed to remove {file_path}: {e}"
                        operation['results'][file_path] = f'ERROR: {e}'
                        results['errors'].append(error_msg)
                        logger.error(error_msg)
                
                # Track kept files
                keep_files = plan.get('keep_file')
                if keep_files:
                    if isinstance(keep_files, str):
                        keep_files = [keep_files]
                    results['files_kept'].extend(keep_files)
                
                keep_files = plan.get('keep_files', [])
                if keep_files:
                    results['files_kept'].extend(keep_files)
                
                results['operations'].append(operation)
        
        logger.info(f"{'DRY RUN: ' if dry_run else ''}Duplicate removal completed")
        logger.info(f"Files removed: {len(results['files_removed'])}")
        logger.info(f"Files kept: {len(results['files_kept'])}")
        logger.info(f"Errors: {len(results['errors'])}")
        
        return results
    
    def update_import_statements(self, removal_results: Dict, dry_run: bool = False) -> Dict:
        """Update import statements to reference consolidated files."""
        logger.info(f"{'DRY RUN: ' if dry_run else ''}Updating import statements...")
        
        if not removal_results['files_removed']:
            logger.info("No files were removed, no import updates needed")
            return {'updates': [], 'errors': []}
        
        # Build mapping of removed files to their replacements
        file_mapping = {}
        
        for operation in removal_results['operations']:
            removed_files = [f for f, result in operation['results'].items() 
                           if result in ['REMOVED', 'DRY_RUN_WOULD_REMOVE']]
            kept_files = operation['files_to_keep']
            
            if isinstance(kept_files, str):
                kept_files = [kept_files]
            
            # Map each removed file to the first kept file
            if kept_files and removed_files:
                replacement_file = kept_files[0]
                for removed_file in removed_files:
                    file_mapping[removed_file] = replacement_file
        
        # Find all Python files that might need import updates
        all_python_files = self.analyzer.scan_python_files()
        
        update_results = {
            'file_mapping': file_mapping,
            'updates': [],
            'errors': [],
            'files_processed': 0,
            'files_updated': 0
        }
        
        for file_path in all_python_files:
            # Skip files that were removed
            if str(file_path) in removal_results['files_removed']:
                continue
            
            try:
                updates_made = self._update_imports_in_file(
                    file_path, file_mapping, dry_run
                )
                
                if updates_made:
                    update_results['updates'].append({
                        'file': str(file_path),
                        'updates': updates_made
                    })
                    update_results['files_updated'] += 1
                
                update_results['files_processed'] += 1
                
            except Exception as e:
                error_msg = f"Failed to update imports in {file_path}: {e}"
                update_results['errors'].append(error_msg)
                logger.error(error_msg)
        
        logger.info(f"Import update completed: {update_results['files_updated']} files updated")
        return update_results
    
    def _update_imports_in_file(self, file_path: Path, file_mapping: Dict[str, str], dry_run: bool = False) -> List[Dict]:
        """Update import statements in a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse the file to find imports
            tree = ast.parse(content)
            updates_made = []
            lines = content.split('\n')
            
            for node in ast.walk(tree):
                if isinstance(node, (ast.Import, ast.ImportFrom)):
                    # Check if this import references a removed file
                    import_line = lines[node.lineno - 1] if node.lineno <= len(lines) else ""
                    
                    for removed_file, replacement_file in file_mapping.items():
                        # Convert file paths to module names for comparison
                        removed_module = self._file_path_to_module(removed_file)
                        replacement_module = self._file_path_to_module(replacement_file)
                        
                        if removed_module and replacement_module:
                            if removed_module in import_line:
                                new_import_line = import_line.replace(removed_module, replacement_module)
                                
                                if new_import_line != import_line:
                                    updates_made.append({
                                        'line_number': node.lineno,
                                        'old_import': import_line.strip(),
                                        'new_import': new_import_line.strip(),
                                        'removed_file': removed_file,
                                        'replacement_file': replacement_file
                                    })
                                    
                                    if not dry_run:
                                        lines[node.lineno - 1] = new_import_line
            
            # Write updated content back to file
            if updates_made and not dry_run:
                updated_content = '\n'.join(lines)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                
                logger.info(f"Updated {len(updates_made)} imports in {file_path}")
            
            return updates_made
            
        except Exception as e:
            logger.error(f"Error updating imports in {file_path}: {e}")
            raise
    
    def _file_path_to_module(self, file_path: str) -> Optional[str]:
        """Convert a file path to a Python module name."""
        try:
            path_obj = Path(file_path)
            
            # Remove .py extension
            if path_obj.suffix == '.py':
                path_obj = path_obj.with_suffix('')
            
            # Convert path separators to dots
            # Remove the project root from the path
            try:
                relative_path = path_obj.relative_to(self.project_root)
                module_name = str(relative_path).replace(os.sep, '.')
                return module_name
            except ValueError:
                # File is not under project root
                return path_obj.name
                
        except Exception:
            return None
    
    def generate_report(self, duplicates: Dict, removal_plan: Dict, removal_results: Dict, 
                       import_updates: Dict, output_file: str = "duplicate_cleanup_report.json") -> str:
        """Generate a comprehensive report of the duplicate cleanup process."""
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_duplicate_groups': len(duplicates),
                'total_duplicate_files': sum(group['file_count'] for group in duplicates.values()),
                'files_removed': len(removal_results.get('files_removed', [])),
                'files_kept': len(removal_results.get('files_kept', [])),
                'import_updates': len(import_updates.get('updates', [])),
                'errors': len(removal_results.get('errors', [])) + len(import_updates.get('errors', []))
            },
            'duplicate_analysis': duplicates,
            'removal_plan': removal_plan,
            'removal_results': removal_results,
            'import_updates': import_updates,
            'backup_location': removal_results.get('backup_path')
        }
        
        # Save report
        report_path = self.project_root / output_file
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        logger.info(f"Comprehensive report saved to: {report_path}")
        
        # Print summary
        print("\n" + "="*60)
        print("DUPLICATE FILE CLEANUP SUMMARY")
        print("="*60)
        print(f"Total duplicate groups found: {report['summary']['total_duplicate_groups']}")
        print(f"Total duplicate files found: {report['summary']['total_duplicate_files']}")
        print(f"Files successfully removed: {report['summary']['files_removed']}")
        print(f"Files kept as references: {report['summary']['files_kept']}")
        print(f"Import statements updated: {report['summary']['import_updates']}")
        print(f"Errors encountered: {report['summary']['errors']}")
        
        if report['summary']['errors'] > 0:
            print("\nERRORS:")
            for error in removal_results.get('errors', []):
                print(f"  - {error}")
            for error in import_updates.get('errors', []):
                print(f"  - {error}")
        
        if removal_results.get('backup_path'):
            print(f"\nBackup created at: {removal_results['backup_path']}")
        
        print(f"\nDetailed report saved to: {report_path}")
        
        return str(report_path)
    
    def run_complete_duplicate_cleanup(self, dry_run: bool = False) -> Dict:
        """Run the complete duplicate file cleanup process."""
        logger.info(f"Starting complete duplicate cleanup process {'(DRY RUN)' if dry_run else ''}")
        
        try:
            # Step 1: Analyze duplicates
            duplicates = self.analyze_duplicates()
            
            if not duplicates:
                logger.info("No duplicate files found")
                return {
                    'status': 'NO_DUPLICATES_FOUND',
                    'duplicates': {},
                    'removal_plan': {},
                    'removal_results': {},
                    'import_updates': {}
                }
            
            # Step 2: Identify safe duplicates
            removal_plan = self.identify_safe_duplicates(duplicates)
            
            # Step 3: Remove duplicate files
            removal_results = self.remove_duplicate_files(removal_plan, dry_run)
            
            # Step 4: Update import statements
            import_updates = self.update_import_statements(removal_results, dry_run)
            
            # Step 5: Generate report
            report_path = self.generate_report(
                duplicates, removal_plan, removal_results, import_updates
            )
            
            result = {
                'status': 'SUCCESS',
                'duplicates': duplicates,
                'removal_plan': removal_plan,
                'removal_results': removal_results,
                'import_updates': import_updates,
                'report_path': report_path
            }
            
            logger.info("Duplicate cleanup process completed successfully")
            return result
            
        except Exception as e:
            logger.error(f"Duplicate cleanup process failed: {e}")
            return {
                'status': f'FAILED: {e}',
                'error': str(e)
            }


def main():
    """Main function to run duplicate file cleanup."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Clean duplicate files from codebase')
    parser.add_argument('--root', default='.', help='Root directory to analyze (default: current directory)')
    parser.add_argument('--dry-run', action='store_true', help='Perform dry run without making changes')
    parser.add_argument('--output', default='duplicate_cleanup_report.json', help='Output report file')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Initialize cleaner
    cleaner = DuplicateFileCleaner(args.root)
    
    # Run complete cleanup
    results = cleaner.run_complete_duplicate_cleanup(dry_run=args.dry_run)
    
    # Print results
    if args.verbose:
        print("\nDETAILED RESULTS:")
        print(json.dumps(results, indent=2, default=str))
    
    return results


if __name__ == "__main__":
    main()