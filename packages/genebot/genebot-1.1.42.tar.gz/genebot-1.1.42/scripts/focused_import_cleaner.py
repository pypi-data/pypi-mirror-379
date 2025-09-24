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
    pass
    """Cleans unused imports from Python files."""
    
    def __init__(self, root_path: Path):
    pass
        self.root_path = root_path
        self.cleaned_files = []
        
    def should_skip_file(self, file_path: Path) -> bool:
    pass
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
    pass
        """Extract imports and their usage from a Python file."""
        try:
    pass
            with open(file_path, 'r', encoding='utf-8') as f:
    pass
                content = f.read()
            
            tree = ast.parse(content)
            
            imports = []
            used_names = set()
            
            # Track all imports with their line numbers
            for node in ast.walk(tree):
    pass
                if isinstance(node, ast.Import):
    
        pass
    pass
                    for alias in node.names:
    pass
                        import_name = alias.asname if alias.asname else alias.name
                        imports.append({
                            'full_line': f"import {alias.name}" + (f" as {alias.asname}" if alias.asname else "")
                        
                elif isinstance(node, ast.ImportFrom):
    
        pass
    pass
                    if node.module:
    
        pass
    pass
                        for alias in node.names:
    pass
                            import_name = alias.asname if alias.asname else alias.name
                            imports.append({
                                'full_line': f"from {node.module} import {alias.name}" + (f" as {alias.asname}" if alias.asname else "")
                
                # Track all name usage
                elif isinstance(node, ast.Name):
    
        pass
    pass
                elif isinstance(node, ast.Attribute):
    
        pass
    pass
                    # For attribute access like module.function
                    if isinstance(node.value, ast.Name):
    
        pass
    pass
                        used_names.add(node.value.id)
                    used_names.add(node.attr)
            
            return {
                'imports': imports,
                'content': content
            }
            
        except Exception as e:
    pass
    pass
            logger.warning(f"Error analyzing {file_path}: {e}")
            return {'imports': [], 'used_names': set(), 'content': ''}
    
    def find_unused_imports(self, file_path: Path) -> List[Dict]:
    pass
        """Find unused imports in a file."""
        analysis = self.get_imports_and_usage(file_path)
        imports = analysis['imports']
        used_names = analysis['used_names']
        
        unused_imports = []
        
        for imp in imports:
    pass
            import_name = imp['name']
            
            # Check if the import name is used anywhere
            if import_name not in used_names:
    
        pass
    pass
                # Additional check for module usage (e.g., os.path)
                module_parts = imp['module'].split('.')
                if not any(part in used_names for part in module_parts):
    
        pass
    pass
        return unused_imports
    
    def clean_file_imports(self, file_path: Path) -> bool:
    pass
        """Clean unused imports from a single file."""
        unused_imports = self.find_unused_imports(file_path)
        
        if not unused_imports:
    
        pass
    pass
            return False
        
        try:
    pass
            with open(file_path, 'r', encoding='utf-8') as f:
    pass
                lines = f.readlines()
            
            # Sort by line number in reverse order to avoid index shifting
            unused_imports.sort(key=lambda x: x['line'], reverse=True)
            
            removed_count = 0
            for imp in unused_imports:
    pass
                line_idx = imp['line'] - 1  # Convert to 0-based index
                
                if line_idx < len(lines):
    
        pass
    pass
                    line_content = lines[line_idx].strip()
                    
                    # Simple check to ensure we're removing the right line
                    if ('import' in line_content and 
                        (imp['module'] in line_content or imp['name'] in line_content)):
    
        pass
    pass
                        # Remove the line
                        removed_count += 1
                        logger.info(f"Removed unused import: {imp['full_line']} from {file_path}")
            
            if removed_count > 0:
    
        pass
    pass
                # Write the cleaned content back
                with open(file_path, 'w', encoding='utf-8') as f:
    pass
                return True
                
        except Exception as e:
    pass
    pass
            logger.error(f"Error cleaning imports in {file_path}: {e}")
        
        return False
    
    def clean_all_imports(self):
    pass
        """Clean unused imports from all Python files."""
        
        python_files = []
        
        # Find all Python files in main codebase
        for root, dirs, files in os.walk(self.root_path):
    pass
            # Skip certain directories
            dirs[:] = [d for d in dirs if not self.should_skip_file(Path(root) / d)]
            
            for file in files:
    
        pass
    pass
                if file.endswith('.py'):
    
        pass
    pass
                    file_path = Path(root) / file
                    if not self.should_skip_file(file_path):
    
        pass
    pass
                        python_files.append(file_path)
        
        logger.info(f"Found {len(python_files)} Python files to process")
        
        # Clean imports in each file
        for file_path in python_files:
    pass
            try:
    pass
                if self.clean_file_imports(file_path):
    
        pass
    pass
            except Exception as e:
    pass
    pass
        return self.cleaned_files

def remove_redundant_consolidated_files():
    pass
    """Remove redundant consolidated files that duplicate main codebase."""
    
    root_path = Path(__file__).parent.parent
    consolidated_dir = root_path / "consolidated"
    
    if not consolidated_dir.exists():
    
        pass
    pass
        logger.info("No consolidated directory found")
        return []
    
    removed_files = []
    
    # Get list of consolidated files
    consolidated_files = list(consolidated_dir.glob("*.py"))
    
    for consolidated_file in consolidated_files:
    pass
        try:
    pass
            # Check if this consolidated file has a corresponding main file
            with open(consolidated_file, 'r', encoding='utf-8') as f:
    
        pass
    pass
                content = f.read()
            
            # If the file is very small or mostly empty, remove it
            if len(content.strip()) < 100:
    
        pass
    pass
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
    pass
                if isinstance(node, ast.FunctionDef):
    
        pass
    pass
                    functions.append(node.name)
                elif isinstance(node, ast.ClassDef):
    
        pass
    pass
                    classes.append(node.name)
            
            # If no meaningful content, remove
            if not functions and not classes:
    
        pass
    pass
                consolidated_file.unlink()
                removed_files.append(str(consolidated_file.relative_to(root_path)))
                logger.info(f"Removed empty consolidated file: {consolidated_file.name}")
                
        except Exception as e:
    pass
    pass
            logger.warning(f"Error processing consolidated file {consolidated_file}: {e}")
    
    logger.info(f"Removed {len(removed_files)} redundant consolidated files")
    return removed_files

def main():
    pass
    """Main function to run focused import cleanup."""
    root_path = Path(__file__).parent.parent
    
    
    # Clean unused imports
    cleaner = ImportCleaner(root_path)
    cleaned_files = cleaner.clean_all_imports()
    
    # Remove redundant consolidated files
    removed_files = remove_redundant_consolidated_files()
    
    # Generate summary report
    report = {
        'cleaned_import_files': cleaned_files,
    }
    
    # Save report
    import json
    report_path = root_path / "focused_cleanup_report.json"
        json.dump(report, f, indent=2)
    
    logger.info(f"Files with cleaned imports: {len(cleaned_files)}")
    
    return report

if __name__ == "__main__":
    
        pass
    pass
    main()