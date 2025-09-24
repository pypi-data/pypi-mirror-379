#!/usr/bin/env python3
"""
Codebase Analysis Tools for Genebot Trading Bot

This script provides comprehensive analysis tools to:
    pass
1. Scan for duplicate files using file hashing
2. Identify unused imports using AST parsing
3. Detect mock implementations and test stubs
4. Build dependency mapper to understand file relationships

Requirements: 1.1, 1.2, 1.3
"""

import os
import ast
import hashlib
import json
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Optional


class CodebaseAnalyzer:
    pass
    """Main analyzer class that orchestrates all analysis tools."""
    
    def __init__(self, root_path: str = "."):
    pass
        self.root_path = Path(root_path).resolve()
        self.python_files = []
        self.duplicate_detector = DuplicateFileDetector()
        self.import_analyzer = UnusedImportAnalyzer()
        self.mock_detector = MockImplementationDetector()
        self.dependency_mapper = DependencyMapper()
        
    def scan_python_files(self) -> List[Path]:
    pass
        """Scan for all Python files in the codebase."""
        python_files = []
        
        # Skip certain directories
        skip_dirs = {
            '__pycache__', '.git', '.tox', 'venv', 'env', 
            'node_modules', '.pytest_cache', 'build', 'dist',
            '.kiro', 'logs', 'reports', 'backups'
        }
        
        for root, dirs, files in os.walk(self.root_path):
    pass
            # Remove skip directories from dirs list to avoid traversing them
            dirs[:] = [d for d in dirs if d not in skip_dirs]
            
            for file in files:
    
        pass
    pass
                if file.endswith('.py'):
    
        pass
    pass
                    file_path = Path(root) / file
                    python_files.append(file_path)
        
        self.python_files = python_files
        return python_files
    
    def analyze_all(self) -> Dict:
    pass
        """Run all analysis tools and return comprehensive results."""
        print("Starting comprehensive codebase analysis...")
        
        # Scan for Python files
        python_files = self.scan_python_files()
        print(f"Found {len(python_files)} Python files")
        
        results = {
            'total_files': len(python_files),
            'duplicate_files': self.duplicate_detector.find_duplicates(python_files),
            'unused_imports': self.import_analyzer.find_unused_imports(python_files),
        }
        
        return results
    
    def generate_report(self, results: Dict, output_file: str = "codebase_analysis_report.json"):
    pass
        """Generate a detailed analysis report."""
        report_path = self.root_path / output_file
        
        with open(report_path, 'w') as f:
    pass
            json.dump(results, f, indent=2, default=str)
        
        print(f"Analysis report saved to: {report_path}")
        return report_path


class DuplicateFileDetector:
    pass
    """Detects duplicate files using file hashing."""
    
    def __init__(self):
    pass
        self.file_hashes = defaultdict(list)
    
    def calculate_file_hash(self, file_path: Path) -> str:
    pass
        """Calculate SHA-256 hash of file content."""
        try:
    pass
            with open(file_path, 'rb') as f:
    pass
                content = f.read()
                return hashlib.sha256(content).hexdigest()
        except Exception as e:
    pass
    pass
            print(f"Error reading file {file_path}: {e}")
            return None
    
    def find_duplicates(self, files: List[Path]) -> Dict[str, List[str]]:
    pass
        """Find duplicate files based on content hash."""
        print("Scanning for duplicate files...")
        
        hash_to_files = defaultdict(list)
        
        for file_path in files:
    pass
            file_hash = self.calculate_file_hash(file_path)
            if file_hash:
    
        pass
    pass
                hash_to_files[file_hash].append(str(file_path))
        
        # Filter to only include hashes with multiple files
        duplicates = {
            hash_val: file_list 
            for hash_val, file_list in hash_to_files.items() 
            if len(file_list) > 1
        }
        
        print(f"Found {len(duplicates)} sets of duplicate files")
        return duplicates


class UnusedImportAnalyzer:
    
        pass
    pass
    """Analyzes Python files to identify unused imports using AST parsing."""
    
    def __init__(self):
    
        pass
    pass
        self.unused_imports = defaultdict(list)
    
    def analyze_file(self, file_path: Path) -> List[str]:
    pass
        """Analyze a single file for unused imports."""
        try:
    pass
            with open(file_path, 'r', encoding='utf-8') as f:
    pass
                content = f.read()
            
            tree = ast.parse(content)
            
            # Extract all imports
            imports = self._extract_imports(tree)
            
            # Extract all names used in the code
            used_names = self._extract_used_names(tree)
            
            # Find unused imports
            unused = []
            for import_info in imports:
    pass
                import_name = import_info['name']
                alias = import_info.get('alias', import_name)
                
                # Check if the import or its alias is used
                if alias not in used_names and import_name not in used_names:
    
        pass
    pass
                    # Special handling for module imports
                    if '.' in import_name:
    
        pass
    pass
                        module_parts = import_name.split('.')
                        if not any(part in used_names for part in module_parts):
    
        pass
    pass
                    else:
    pass
            return unused
            
        except Exception as e:
    pass
    pass
            return []
    
    def _extract_imports(self, tree: ast.AST) -> List[Dict]:
    pass
        """Extract all import statements from AST."""
        imports = []
        
        for node in ast.walk(tree):
    pass
            if isinstance(node, ast.Import):
    
        pass
    pass
                for alias in node.names:
    pass
                    imports.append({
                        'line': node.lineno
            elif isinstance(node, ast.ImportFrom):
    
        pass
    pass
                module = node.module or ''
                for alias in node.names:
    pass
                    imports.append({
                        'line': node.lineno
        
        return imports
    
    def _extract_used_names(self, tree: ast.AST) -> Set[str]:
    pass
        """Extract all names used in the code."""
        used_names = set()
        
        for node in ast.walk(tree):
    pass
            if isinstance(node, ast.Name):
    
        pass
    pass
                used_names.add(node.id)
            elif isinstance(node, ast.Attribute):
    
        pass
    pass
                # Handle attribute access like module.function
                if isinstance(node.value, ast.Name):
    
        pass
    pass
                    used_names.add(node.value.id)
        
        return used_names
    
    def find_unused_imports(self, files: List[Path]) -> Dict[str, List[Dict]]:
    pass
        """Find unused imports across all files."""
        
        unused_by_file = {}
        
        for file_path in files:
    pass
            unused = self.analyze_file(file_path)
            if unused:
    
        pass
    pass
                unused_by_file[str(file_path)] = unused
        
        print(f"Found unused imports in {len(unused_by_file)} files")
        return unused_by_file


class MockImplementationDetector:
    pass
    """Detects mock implementations and test stubs in production code."""
    
    def __init__(self):
    pass
        self.mock_patterns = [
            'mock', 'Mock', 'MagicMock', 'patch', 'stub', 'Stub',
            'fake', 'Fake', 'dummy', 'Dummy', 'test_', 'Test'
        ]
    
    def analyze_file(self, file_path: Path) -> List[Dict]:
    pass
        """Analyze a file for mock implementations."""
        try:
    pass
            with open(file_path, 'r', encoding='utf-8') as f:
    pass
                content = f.read()
            
            tree = ast.parse(content)
            mocks_found = []
            
            for node in ast.walk(tree):
    pass
                # Check class definitions
                if isinstance(node, ast.ClassDef):
    
        pass
    pass
                    if self._is_mock_name(node.name):
    
        pass
    pass
                        mocks_found.append({
                            'type': 'class',
                            'name': node.name,
                            'line': node.lineno,
                            'reason': 'Mock-like class name'
                        })
                
                # Check function definitions
                elif isinstance(node, ast.FunctionDef):
    
        pass
    pass
                    if self._is_mock_name(node.name):
    
        pass
    pass
                        mocks_found.append({
                            'type': 'function',
                            'name': node.name,
                            'line': node.lineno,
                            'reason': 'Mock-like function name'
                        })
                
                # Check for mock imports
                elif isinstance(node, ast.ImportFrom):
    
        pass
    pass
                    if node.module and 'mock' in node.module.lower():
    
        pass
    pass
                        mocks_found.append({
                            'reason': 'Mock library import'
            
            # Check for test-like file patterns
            if self._is_test_file(file_path):
    
        pass
    pass
                mocks_found.append({
                    'type': 'file',
                    'name': str(file_path),
                    'line': 1,
                    'reason': 'Test file in production code'
                })
            
            return mocks_found
            
        except Exception as e:
    pass
    pass
            print(f"Error analyzing file {file_path}: {e}")
            return []
    
    def _is_mock_name(self, name: str) -> bool:
    pass
        """Check if a name suggests it's a mock implementation."""
        name_lower = name.lower()
        return any(pattern.lower() in name_lower for pattern in self.mock_patterns)
    
    def _is_test_file(self, file_path: Path) -> bool:
    pass
        """Check if file appears to be a test file."""
        name = file_path.name.lower()
        return (name.startswith('test_') or 
                name.endswith('_test.py') or 
                'test' in file_path.parts)
    
    def find_mocks(self, files: List[Path]) -> Dict[str, List[Dict]]:
    pass
        """Find mock implementations across all files."""
        print("Detecting mock implementations and test stubs...")
        
        mocks_by_file = {}
        
        for file_path in files:
    pass
            # Skip actual test directories
            if any(part in ['test', 'tests', 'testing'] for part in file_path.parts):
    
        pass
    pass
                continue
                
            mocks = self.analyze_file(file_path)
            if mocks:
    
        pass
    pass
                mocks_by_file[str(file_path)] = mocks
        
        print(f"Found mock implementations in {len(mocks_by_file)} files")
        return mocks_by_file


class DependencyMapper:
    pass
    """Maps file dependencies to understand relationships."""
    
    def __init__(self):
    pass
        self.dependencies = defaultdict(set)
        self.reverse_dependencies = defaultdict(set)
    
    def analyze_file_dependencies(self, file_path: Path, all_files: Set[Path]) -> Set[str]:
    pass
        """Analyze dependencies for a single file."""
        try:
    pass
            with open(file_path, 'r', encoding='utf-8') as f:
    pass
                content = f.read()
            
            tree = ast.parse(content)
            dependencies = set()
            
            for node in ast.walk(tree):
    pass
                if isinstance(node, ast.Import):
    
        pass
    pass
                    for alias in node.names:
    pass
                        dep_path = self._resolve_import_path(alias.name, file_path, all_files)
                        if dep_path:
    
        pass
    pass
                elif isinstance(node, ast.ImportFrom):
    
        pass
    pass
                    if node.module:
    
        pass
    pass
                        dep_path = self._resolve_import_path(node.module, file_path, all_files)
                        if dep_path:
    
        pass
    pass
            return dependencies
            
        except Exception as e:
    pass
    pass
            print(f"Error analyzing dependencies for {file_path}: {e}")
            return set()
    
    def _resolve_import_path(self, import_name: str, current_file: Path, all_files: Set[Path]) -> Optional[str]:
    pass
        """Try to resolve an import to an actual file path."""
        # Handle relative imports
        if import_name.startswith('.'):
    
        pass
    pass
            # This is a relative import, resolve relative to current file
            current_dir = current_file.parent
            parts = import_name.lstrip('.').split('.')
            
            for file_path in all_files:
    pass
                if file_path.parent == current_dir:
    
        pass
    pass
                    if parts and file_path.stem == parts[0]:
    
        pass
    pass
                        return str(file_path)
        
        # Handle absolute imports within the project
        parts = import_name.split('.')
        
        for file_path in all_files:
    pass
            # Check if this file matches the import
            path_parts = file_path.parts
            
            # Try to match the import path to file structure
            if len(parts) <= len(path_parts):
    
        pass
    pass
                if parts[-1] == file_path.stem or parts[-1] in path_parts:
    
        pass
    pass
                    return str(file_path)
        
        return None
    
    def build_dependency_map(self, files: List[Path]) -> Dict:
    pass
        """Build a comprehensive dependency map."""
        print("Building dependency map...")
        
        all_files_set = set(files)
        dependency_map = {}
        reverse_deps = defaultdict(list)
        
        for file_path in files:
    pass
            deps = self.analyze_file_dependencies(file_path, all_files_set)
            file_str = str(file_path)
            dependency_map[file_str] = list(deps)
            
            # Build reverse dependencies
            for dep in deps:
    pass
                reverse_deps[dep].append(file_str)
        
        # Calculate dependency statistics
        stats = {
            'total_files': len(files),
            'files_with_dependencies': len([f for f in dependency_map.values() if f]),
            'average_dependencies': sum(len(deps) for deps in dependency_map.values()) / len(files) if files else 0,
            'most_dependent_files': sorted(
                [(f, len(deps)) for f, deps in dependency_map.items()], 
                key=lambda x: x[1], reverse=True
            )[:10]
        }
        
        result = {
            'dependencies': dependency_map,
            'reverse_dependencies': dict(reverse_deps),
            'statistics': stats
        }
        
        print(f"Mapped dependencies for {len(files)} files")
        return result


def main():
    pass
    """Main function to run the codebase analysis."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Analyze codebase for duplicates, unused imports, mocks, and dependencies')
    parser.add_argument('--root', default='.', help='Root directory to analyze (default: current directory)')
    parser.add_argument('--output', default='codebase_analysis_report.json', help='Output report file')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    analyzer = CodebaseAnalyzer(args.root)
    results = analyzer.analyze_all()
    
    # Generate report
    report_path = analyzer.generate_report(results, args.output)
    
    # Print summary
    print("\n" + "="*50)
    print("CODEBASE ANALYSIS SUMMARY")
    print("="*50)
    print(f"Total Python files analyzed: {results['total_files']}")
    print(f"Duplicate file sets found: {len(results['duplicate_files'])}")
    print(f"Files with unused imports: {len(results['unused_imports'])}")
    print(f"Dependency map created for {results['dependencies']['statistics']['total_files']} files")
    
    if args.verbose:
    
        pass
    pass
        print("\nDETAILED RESULTS:")
        print(json.dumps(results, indent=2, default=str))


if __name__ == "__main__":
    
        pass
    pass
    main()