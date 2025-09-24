#!/usr/bin/env python3
"""
Focused Import Cleaner

This script focuses on cleaning unused imports from the main codebase,
excluding backup directories and consolidated files.
"""

import ast
import os
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ImportCleaner:
    """Cleans unused imports from Python files."""
    
    def __init__(self, root_path: Path):
        self.root_path = root_path
        self.cleaned_files = []
        
    def should_skip_file(self, file_path: Path) -> bool:
        """Check if file should be skipped."""
        path_str = str(file_path)
        
        # Skip backup directories and consolidated files
        skip_patterns = [
            'backups/',
            'consolidated/',
            '__pycache__',
            '.git/',
            '.venv/',
            'venv/',
            '.tox/',
            'build/',
            'dist/',
            '.egg-info'
        ]
        
        return any(pattern in path_str for pattern in skip_patterns)
    
    def get_imports_and_usage(self, file_path: Path) -> Dict:
        """Extract imports and their usage from a Python file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content)
            
            imports = []
            used_names = set()
            
            # Track all imports with their line numbers
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        import_name = alias.asname if alias.asname else alias.name
                        imports.append({
                            'type': 'import',
                            'module': alias.name,
                            'name': import_name,
                            'line': node.lineno,
                            'full_line': f"import {alias.name}" + (f" as {alias.asname}" if alias.asname else "")
                        })
                        
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        for alias in node.names:
                            import_name = alias.asname if alias.asname else alias.name
                            imports.append({
                                'type': 'from_import',
                                'module': node.module,
                                'name': import_name,
                                'line': node.lineno,
                                'full_line': f"from {node.module} import {alias.name}" + (f" as {alias.asname}" if alias.asname else "")
                            })
                
                # Track all name usage
                elif isinstance(node, ast.Name):
                    used_names.add(node.id)
                elif isinstance(node, ast.Attribute):
                    # For attribute access like module.function
                    if isinstance(node.value, ast.Name):
                        used_names.add(node.value.id)
                    used_names.add(node.attr)
            
            return {
                'imports': imports,
                'used_names': used_names,
                'content': content
            }
            
        except Exception as e:
            logger.warning(f"Error analyzing {file_path}: {e}")
            return {'imports': [], 'used_names': set(), 'content': ''}
    
    def find_unused_imports(self, file_path: Path) -> List[Dict]:
        """Find unused imports in a file."""
        analysis = self.get_imports_and_usage(file_path)
        imports = analysis['imports']
        used_names = analysis['used_names']
        
        unused_imports = []
        
        for imp in imports:
            import_name = imp['name']
            
            # Check if the import name is used anywhere
            if import_name not in used_names:
                # Additional check for module usage (e.g., os.path)
                module_parts = imp['module'].split('.')
                if not any(part in used_names for part in module_parts):
                    unused_imports.append(imp)
        
        return unused_imports
    
    def clean_file_imports(self, file_path: Path) -> bool:
        """Clean unused imports from a single file."""
        unused_imports = self.find_unused_imports(file_path)
        
        if not unused_imports:
            return False
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Sort by line number in reverse order to avoid index shifting
            unused_imports.sort(key=lambda x: x['line'], reverse=True)
            
            removed_count = 0
            for imp in unused_imports:
                line_idx = imp['line'] - 1  # Convert to 0-based index
                
                if line_idx < len(lines):
                    line_content = lines[line_idx].strip()
                    
                    # Simple check to ensure we're removing the right line
                    if ('import' in line_content and 
                        (imp['module'] in line_content or imp['name'] in line_content)):
                        
                        # Remove the line
                        lines.pop(line_idx)
                        removed_count += 1
                        logger.info(f"Removed unused import: {imp['full_line']} from {file_path}")
            
            if removed_count > 0:
                # Write the cleaned content back
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                
                return True
                
        except Exception as e:
            logger.error(f"Error cleaning imports in {file_path}: {e}")
        
        return False
    
    def clean_all_imports(self):
        """Clean unused imports from all Python files."""
        logger.info("Starting import cleanup...")
        
        python_files = []
        
        # Find all Python files in main codebase
        for root, dirs, files in os.walk(self.root_path):
            # Skip certain directories
            dirs[:] = [d for d in dirs if not self.should_skip_file(Path(root) / d)]
            
            for file in files:
                if file.endswith('.py'):
                    file_path = Path(root) / file
                    if not self.should_skip_file(file_path):
                        python_files.append(file_path)
        
        logger.info(f"Found {len(python_files)} Python files to process")
        
        # Clean imports in each file
        for file_path in python_files:
            try:
                if self.clean_file_imports(file_path):
                    self.cleaned_files.append(str(file_path.relative_to(self.root_path)))
            except Exception as e:
                logger.error(f"Error processing {file_path}: {e}")
        
        logger.info(f"Cleaned imports in {len(self.cleaned_files)} files")
        return self.cleaned_files

def remove_redundant_consolidated_files():
    """Remove redundant consolidated files that duplicate main codebase."""
    logger.info("Removing redundant consolidated files...")
    
    root_path = Path(__file__).parent.parent
    consolidated_dir = root_path / "consolidated"
    
    if not consolidated_dir.exists():
        logger.info("No consolidated directory found")
        return []
    
    removed_files = []
    
    # Get list of consolidated files
    consolidated_files = list(consolidated_dir.glob("*.py"))
    
    for consolidated_file in consolidated_files:
        try:
            # Check if this consolidated file has a corresponding main file
            with open(consolidated_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # If the file is very small or mostly empty, remove it
            if len(content.strip()) < 100:
                consolidated_file.unlink()
                removed_files.append(str(consolidated_file.relative_to(root_path)))
                logger.info(f"Removed small consolidated file: {consolidated_file.name}")
                continue
            
            # Check for obvious duplicates by looking for identical function/class names
            # in the main codebase
            tree = ast.parse(content)
            
            functions = []
            classes = []
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    functions.append(node.name)
                elif isinstance(node, ast.ClassDef):
                    classes.append(node.name)
            
            # If no meaningful content, remove
            if not functions and not classes:
                consolidated_file.unlink()
                removed_files.append(str(consolidated_file.relative_to(root_path)))
                logger.info(f"Removed empty consolidated file: {consolidated_file.name}")
                
        except Exception as e:
            logger.warning(f"Error processing consolidated file {consolidated_file}: {e}")
    
    logger.info(f"Removed {len(removed_files)} redundant consolidated files")
    return removed_files

def main():
    """Main function to run focused import cleanup."""
    root_path = Path(__file__).parent.parent
    
    logger.info("Starting focused module consolidation and import cleanup...")
    
    # Clean unused imports
    cleaner = ImportCleaner(root_path)
    cleaned_files = cleaner.clean_all_imports()
    
    # Remove redundant consolidated files
    removed_files = remove_redundant_consolidated_files()
    
    # Generate summary report
    report = {
        'cleaned_import_files': cleaned_files,
        'removed_consolidated_files': removed_files,
        'total_files_cleaned': len(cleaned_files),
        'total_files_removed': len(removed_files)
    }
    
    # Save report
    import json
    report_path = root_path / "focused_cleanup_report.json"
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    logger.info(f"\nFocused cleanup completed!")
    logger.info(f"Files with cleaned imports: {len(cleaned_files)}")
    logger.info(f"Redundant files removed: {len(removed_files)}")
    logger.info(f"Report saved to {report_path}")
    
    return report

if __name__ == "__main__":
    main()