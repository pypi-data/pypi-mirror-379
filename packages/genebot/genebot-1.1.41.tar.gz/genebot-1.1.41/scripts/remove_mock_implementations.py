#!/usr/bin/env python3
"""
Mock Implementation and Test Stub Remover

This script identifies and removes mock implementations and test stubs from the production codebase
while preserving real functionality.
"""

import ast
import shutil
from pathlib import Path
import logging
import json
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class MockImplementationRemover:
    """Removes mock implementations and test stubs from production code."""
    
    def __init__(self, root_dir: Path):
        self.root_dir = root_dir
        self.removed_files: List[str] = []
        self.modified_files: List[str] = []
        self.mock_patterns = [
            'mock_', 'Mock', 'test_', 'Test', 'stub_', 'Stub',
            'fake_', 'Fake', 'dummy_', 'Dummy'
        ]
        self.production_dirs = ['src', 'genebot']
        self.backup_dir = Path('backups/mock_removal_backup')
        
    def create_backup(self) -> None:
        """Create backup before removing mocks."""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.backup_dir = Path(f'backups/mock_removal_backup_{timestamp}')
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Created backup directory: {self.backup_dir}")
        
    def is_production_file(self, file_path: Path) -> bool:
        """Check if file is in production directories."""
        return any(prod_dir in file_path.parts for prod_dir in self.production_dirs)
        
    def is_mock_file(self, file_path: Path) -> bool:
        """Check if entire file is a mock implementation."""
        filename = file_path.name
        
        # Check for mock patterns in filename
        if any(pattern in filename for pattern in self.mock_patterns):
            return True
            
        # Check file content for mock indicators
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Check for mock-related imports and classes
            mock_indicators = [
                'unittest.mock', 'from mock import', 'import mock',
                'class Mock', 'def mock_', 'Mock strategy for testing',
                'Mock implementation', 'for testing purposes only'
            ]
            
            return any(indicator in content for indicator in mock_indicators)
            
        except Exception as e:
            logger.warning(f"Could not read file {file_path}: {e}")
            return False
            
    def analyze_file_for_mocks(self, file_path: Path) -> Dict[str, List[Dict]]:
        """Analyze a Python file for mock implementations."""
        mocks_found = {
            'classes': [],
            'functions': [],
            'imports': []
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            tree = ast.parse(content)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    if self._is_mock_class(node):
                        mocks_found['classes'].append({
                            'name': node.name,
                            'line': node.lineno,
                            'type': 'class'
                        })
                        
                elif isinstance(node, ast.FunctionDef):
                    if self._is_mock_function(node):
                        mocks_found['functions'].append({
                            'name': node.name,
                            'line': node.lineno,
                            'type': 'function'
                        })
                        
                elif isinstance(node, (ast.Import, ast.ImportFrom)):
                    if self._is_mock_import(node):
                        mocks_found['imports'].append({
                            'line': node.lineno,
                            'type': 'import',
                            'module': getattr(node, 'module', None) or 
                                     (node.names[0].name if node.names else 'unknown')
                        })
                        
        except Exception as e:
            logger.warning(f"Could not analyze file {file_path}: {e}")
            
        return mocks_found
        
    def _is_mock_class(self, node: ast.ClassDef) -> bool:
        """Check if a class is a mock implementation."""
        name_lower = node.name.lower()
        
        # Check class name patterns
        if any(pattern.lower() in name_lower for pattern in self.mock_patterns):
            return True
            
        # Check docstring for mock indicators
        docstring = ast.get_docstring(node)
        if docstring:
            doc_lower = docstring.lower()
            if any(indicator in doc_lower for indicator in [
                'mock', 'test', 'stub', 'fake', 'dummy', 'for testing'
            ]):
                return True
                
        return False
        
    def _is_mock_function(self, node: ast.FunctionDef) -> bool:
        """Check if a function is a mock implementation."""
        name_lower = node.name.lower()
        
        # Check function name patterns
        if any(pattern.lower() in name_lower for pattern in self.mock_patterns):
            return True
            
        # Check docstring for mock indicators
        docstring = ast.get_docstring(node)
        if docstring:
            doc_lower = docstring.lower()
            if any(indicator in doc_lower for indicator in [
                'mock', 'test', 'stub', 'fake', 'dummy', 'for testing'
            ]):
                return True
                
        return False
        
    def _is_mock_import(self, node) -> bool:
        """Check if an import is mock-related."""
        if isinstance(node, ast.ImportFrom):
            if node.module and any(mock_mod in node.module for mock_mod in [
                'mock', 'unittest.mock', 'test', 'testing'
            ]):
                return True
                
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if any(mock_mod in alias.name for mock_mod in [
                    'mock', 'unittest.mock', 'test', 'testing'
                ]):
                    return True
                    
        return False
        
    def remove_mock_files(self) -> None:
        """Remove entire files that are mock implementations."""
        logger.info("Scanning for mock files to remove...")
        
        for prod_dir in self.production_dirs:
            prod_path = self.root_dir / prod_dir
            if not prod_path.exists():
                continue
                
            for py_file in prod_path.rglob('*.py'):
                if self.is_mock_file(py_file):
                    # Create backup
                    backup_path = self.backup_dir / py_file.relative_to(self.root_dir)
                    backup_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(py_file, backup_path)
                    
                    # Remove the file
                    py_file.unlink()
                    self.removed_files.append(str(py_file))
                    logger.info(f"Removed mock file: {py_file}")
                    
    def clean_mock_imports_from_files(self) -> None:
        """Remove mock-related imports and references from production files."""
        logger.info("Cleaning mock imports from production files...")
        
        for prod_dir in self.production_dirs:
            prod_path = self.root_dir / prod_dir
            if not prod_path.exists():
                continue
                
            for py_file in prod_path.rglob('*.py'):
                if py_file.exists() and not self.is_mock_file(py_file):
                    self._clean_file_mock_content(py_file)
                    
    def _clean_file_mock_content(self, file_path: Path) -> None:
        """Clean mock content from a specific file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
                
            lines = original_content.split('\n')
            cleaned_lines = []
            modified = False
            
            for line in lines:
                line_lower = line.lower().strip()
                
                # Skip mock-related imports
                if any(mock_import in line_lower for mock_import in [
                    'from unittest.mock import', 'import unittest.mock',
                    'from mock import', 'import mock',
                    'from ..strategies.mock_strategies import',
                    'from .mock_strategies import'
                ]):
                    modified = True
                    logger.debug(f"Removed mock import: {line.strip()}")
                    continue
                    
                # Skip mock strategy registration
                if any(mock_ref in line_lower for mock_ref in [
                    'register_mock_strategies', 'mock_strategies',
                    'mock_registry'
                ]):
                    modified = True
                    logger.debug(f"Removed mock reference: {line.strip()}")
                    continue
                    
                cleaned_lines.append(line)
                
            if modified:
                # Create backup
                backup_path = self.backup_dir / file_path.relative_to(self.root_dir)
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file_path, backup_path)
                
                # Write cleaned content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(cleaned_lines))
                    
                self.modified_files.append(str(file_path))
                logger.info(f"Cleaned mock content from: {file_path}")
                
        except Exception as e:
            logger.error(f"Error cleaning file {file_path}: {e}")
            
    def remove_test_utilities_from_production(self) -> None:
        """Remove test utility functions and classes from production code."""
        logger.info("Removing test utilities from production code...")
        
        test_utility_files = [
            'src/orchestration/test_utils.py'
        ]
        
        for util_file in test_utility_files:
            file_path = self.root_dir / util_file
            if file_path.exists():
                # Create backup
                backup_path = self.backup_dir / file_path.relative_to(self.root_dir)
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file_path, backup_path)
                
                # Remove the file
                file_path.unlink()
                self.removed_files.append(str(file_path))
                logger.info(f"Removed test utility file: {file_path}")
                
    def generate_report(self) -> Dict:
        """Generate a report of all changes made."""
        report = {
            'timestamp': datetime.now().isoformat(),
            'removed_files': self.removed_files,
            'modified_files': self.modified_files,
            'backup_location': str(self.backup_dir),
            'summary': {
                'files_removed': len(self.removed_files),
                'files_modified': len(self.modified_files),
                'total_changes': len(self.removed_files) + len(self.modified_files)
            }
        }
        
        return report
        
    def run_cleanup(self) -> Dict:
        """Run the complete mock cleanup process."""
        logger.info("Starting mock implementation cleanup...")
        
        # Create backup
        self.create_backup()
        
        # Remove mock files
        self.remove_mock_files()
        
        # Clean mock imports from remaining files
        self.clean_mock_imports_from_files()
        
        # Remove test utilities from production
        self.remove_test_utilities_from_production()
        
        # Generate report
        report = self.generate_report()
        
        logger.info("Mock cleanup completed successfully!")
        logger.info(f"Files removed: {len(self.removed_files)}")
        logger.info(f"Files modified: {len(self.modified_files)}")
        
        return report


def main():
    """Main function to run mock implementation removal."""
    root_dir = Path('.')
    
    # Initialize remover
    remover = MockImplementationRemover(root_dir)
    
    # Run cleanup
    report = remover.run_cleanup()
    
    # Save report
    report_file = Path('mock_removal_report.json')
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
        
    print(f"\nMock removal completed!")
    print(f"Report saved to: {report_file}")
    print(f"Backup created at: {report['backup_location']}")
    print(f"Files removed: {report['summary']['files_removed']}")
    print(f"Files modified: {report['summary']['files_modified']}")


if __name__ == '__main__':
    main()