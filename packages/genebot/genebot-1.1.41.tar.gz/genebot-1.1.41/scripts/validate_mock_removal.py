#!/usr/bin/env python3
"""
Mock Removal Validation Script

This script validates that all mock implementations and test stubs have been
properly removed from the production codebase.
"""

import ast
from pathlib import Path
import logging
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class MockRemovalValidator:
    """Validates that mock implementations have been properly removed."""
    
    def __init__(self, root_dir: Path):
        self.root_dir = root_dir
        self.production_dirs = ['src', 'genebot']
        self.issues_found: List[Dict] = []
        
    def validate_no_mock_files(self) -> bool:
        """Validate that no mock implementation files remain."""
        logger.info("Validating no mock files remain...")
        
        mock_patterns = ['mock_', 'test_utils', 'test_helpers']
        found_issues = False
        
        for prod_dir in self.production_dirs:
            prod_path = self.root_dir / prod_dir
            if not prod_path.exists():
                continue
                
            for py_file in prod_path.rglob('*.py'):
                filename = py_file.name.lower()
                if any(pattern in filename for pattern in mock_patterns):
                    # Check if it's actually a mock file
                    if self._is_mock_file(py_file):
                        self.issues_found.append({
                            'type': 'mock_file_found',
                            'file': str(py_file),
                            'description': 'Mock implementation file still exists'
                        })
                        found_issues = True
                        
        return not found_issues
        
    def validate_no_mock_imports(self) -> bool:
        """Validate that no mock imports remain in production code."""
        logger.info("Validating no mock imports remain...")
        
        found_issues = False
        mock_import_patterns = [
            'unittest.mock', 'from mock import', 'import mock',
            'mock_strategies', 'register_mock'
        ]
        
        for prod_dir in self.production_dirs:
            prod_path = self.root_dir / prod_dir
            if not prod_path.exists():
                continue
                
            for py_file in prod_path.rglob('*.py'):
                try:
                    with open(py_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    for line_num, line in enumerate(content.split('\n'), 1):
                        line_lower = line.lower().strip()
                        for pattern in mock_import_patterns:
                            if pattern in line_lower:
                                self.issues_found.append({
                                    'type': 'mock_import_found',
                                    'file': str(py_file),
                                    'line': line_num,
                                    'content': line.strip(),
                                    'description': f'Mock import found: {pattern}'
                                })
                                found_issues = True
                                
                except Exception as e:
                    logger.warning(f"Could not read file {py_file}: {e}")
                    
        return not found_issues
        
    def validate_no_mock_classes(self) -> bool:
        """Validate that no mock classes remain in production code."""
        logger.info("Validating no mock classes remain...")
        
        found_issues = False
        
        for prod_dir in self.production_dirs:
            prod_path = self.root_dir / prod_dir
            if not prod_path.exists():
                continue
                
            for py_file in prod_path.rglob('*.py'):
                try:
                    with open(py_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    tree = ast.parse(content)
                    
                    for node in ast.walk(tree):
                        if isinstance(node, ast.ClassDef):
                            if self._is_mock_class_name(node.name):
                                # Check if it's actually a mock class
                                docstring = ast.get_docstring(node)
                                if docstring and any(indicator in docstring.lower() for indicator in [
                                    'mock', 'test', 'stub', 'for testing'
                                ]):
                                    self.issues_found.append({
                                        'type': 'mock_class_found',
                                        'file': str(py_file),
                                        'line': node.lineno,
                                        'class_name': node.name,
                                        'description': 'Mock class found in production code'
                                    })
                                    found_issues = True
                                    
                except Exception as e:
                    logger.warning(f"Could not analyze file {py_file}: {e}")
                    
        return not found_issues
        
    def validate_no_test_functions(self) -> bool:
        """Validate that no test functions remain in production code."""
        logger.info("Validating no test functions remain...")
        
        found_issues = False
        
        for prod_dir in self.production_dirs:
            prod_path = self.root_dir / prod_dir
            if not prod_path.exists():
                continue
                
            for py_file in prod_path.rglob('*.py'):
                try:
                    with open(py_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    tree = ast.parse(content)
                    
                    for node in ast.walk(tree):
                        if isinstance(node, ast.FunctionDef):
                            if node.name.startswith('test_') or 'mock_' in node.name.lower():
                                # Check if it's actually a test function
                                docstring = ast.get_docstring(node)
                                if docstring and any(indicator in docstring.lower() for indicator in [
                                    'test', 'mock', 'stub', 'for testing'
                                ]):
                                    self.issues_found.append({
                                        'type': 'test_function_found',
                                        'file': str(py_file),
                                        'line': node.lineno,
                                        'function_name': node.name,
                                        'description': 'Test function found in production code'
                                    })
                                    found_issues = True
                                    
                except Exception as e:
                    logger.warning(f"Could not analyze file {py_file}: {e}")
                    
        return not found_issues
        
    def _is_mock_file(self, file_path: Path) -> bool:
        """Check if a file is actually a mock implementation."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Check for mock indicators
            mock_indicators = [
                'mock implementation', 'for testing', 'test purposes',
                'Mock strategy for testing', 'test stub'
            ]
            
            return any(indicator.lower() in content.lower() for indicator in mock_indicators)
            
        except Exception:
            return False
            
    def _is_mock_class_name(self, name: str) -> bool:
        """Check if a class name suggests it's a mock."""
        name_lower = name.lower()
        return any(pattern in name_lower for pattern in [
            'mock', 'test', 'stub', 'fake', 'dummy'
        ])
        
    def run_validation(self) -> Dict:
        """Run complete validation and return results."""
        logger.info("Starting mock removal validation...")
        
        # Run all validations
        validations = {
            'no_mock_files': self.validate_no_mock_files(),
            'no_mock_imports': self.validate_no_mock_imports(),
            'no_mock_classes': self.validate_no_mock_classes(),
            'no_test_functions': self.validate_no_test_functions()
        }
        
        # Generate report
        all_passed = all(validations.values())
        
        report = {
            'validation_passed': all_passed,
            'validations': validations,
            'issues_found': self.issues_found,
            'summary': {
                'total_issues': len(self.issues_found),
                'validations_passed': sum(validations.values()),
                'validations_failed': len(validations) - sum(validations.values())
            }
        }
        
        if all_passed:
            logger.info("✅ All validations passed! Mock removal was successful.")
        else:
            logger.warning(f"❌ {len(self.issues_found)} issues found during validation.")
            
        return report


def main():
    """Main function to run mock removal validation."""
    root_dir = Path('.')
    
    # Initialize validator
    validator = MockRemovalValidator(root_dir)
    
    # Run validation
    report = validator.run_validation()
    
    # Save report
    report_file = Path('mock_removal_validation_report.json')
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
        
    print(f"\nMock removal validation completed!")
    print(f"Report saved to: {report_file}")
    print(f"Validation passed: {report['validation_passed']}")
    print(f"Issues found: {report['summary']['total_issues']}")
    
    if report['issues_found']:
        print("\nIssues found:")
        for issue in report['issues_found']:
            print(f"  - {issue['type']}: {issue['description']}")
            print(f"    File: {issue['file']}")
            if 'line' in issue:
                print(f"    Line: {issue['line']}")
            print()


if __name__ == '__main__':
    main()