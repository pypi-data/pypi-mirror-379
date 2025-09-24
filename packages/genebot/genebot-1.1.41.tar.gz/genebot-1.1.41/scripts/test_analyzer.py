#!/usr/bin/env python3
"""
Test script to verify the codebase analyzer components work correctly.
"""

import tempfile
from pathlib import Path
import sys

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from codebase_analyzer import (
    DuplicateFileDetector, 
    UnusedImportAnalyzer, 
    MockImplementationDetector, 
    DependencyMapper
)


def create_test_files():
    """Create temporary test files for analysis."""
    temp_dir = Path(tempfile.mkdtemp())
    
    # Create duplicate files
    file1 = temp_dir / "duplicate1.py"
    file2 = temp_dir / "duplicate2.py"
    content = "print('Hello World')\n"
    
    file1.write_text(content)
    file2.write_text(content)
    
    # Create file with unused imports
    unused_imports_file = temp_dir / "unused_imports.py"
    unused_imports_file.write_text("""
import sys
import json  # unused
from typing import Dict, List  # Dict is unused

def main():
    print(os.getcwd())
    return sys.version
""")
    
    # Create file with mock implementations
    mock_file = temp_dir / "mock_impl.py"
    mock_file.write_text("""
from unittest.mock import Mock

class MockDatabase:
    def get_data(self):
        return "mock data"

def test_function():
    return "test"

class FakeService:
    pass
""")
    
    return temp_dir, [file1, file2, unused_imports_file, mock_file]


def test_duplicate_detector():
    """Test the duplicate file detector."""
    print("Testing DuplicateFileDetector...")
    
    temp_dir, files = create_test_files()
    detector = DuplicateFileDetector()
    
    duplicates = detector.find_duplicates(files)
    
    assert len(duplicates) == 1, f"Expected 1 duplicate set, got {len(duplicates)}"
    
    # Get the duplicate set
    duplicate_set = list(duplicates.values())[0]
    assert len(duplicate_set) == 2, f"Expected 2 duplicate files, got {len(duplicate_set)}"
    
    print("✓ DuplicateFileDetector working correctly")
    return True


def test_unused_import_analyzer():
    """Test the unused import analyzer."""
    print("Testing UnusedImportAnalyzer...")
    
    temp_dir, files = create_test_files()
    analyzer = UnusedImportAnalyzer()
    
    unused_imports_file = temp_dir / "unused_imports.py"
    unused = analyzer.analyze_file(unused_imports_file)
    
    # Should find json and Dict as unused
    assert len(unused) >= 1, f"Expected at least 1 unused import, got {len(unused)}"
    
    unused_names = [imp['name'] for imp in unused]
    assert 'json' in unused_names, "Should detect 'json' as unused"
    
    print("✓ UnusedImportAnalyzer working correctly")
    return True


def test_mock_detector():
    """Test the mock implementation detector."""
    print("Testing MockImplementationDetector...")
    
    temp_dir, files = create_test_files()
    detector = MockImplementationDetector()
    
    mock_file = temp_dir / "mock_impl.py"
    mocks = detector.analyze_file(mock_file)
    
    assert len(mocks) >= 2, f"Expected at least 2 mock implementations, got {len(mocks)}"
    
    mock_names = [mock['name'] for mock in mocks]
    assert 'MockDatabase' in mock_names, "Should detect MockDatabase class"
    
    print("✓ MockImplementationDetector working correctly")
    return True


def test_dependency_mapper():
    """Test the dependency mapper."""
    print("Testing DependencyMapper...")
    
    temp_dir, files = create_test_files()
    mapper = DependencyMapper()
    
    # Create a file with dependencies
    dep_file = temp_dir / "with_deps.py"
    dep_file.write_text("""
from pathlib import Path
from .unused_imports import main
""")
    files.append(dep_file)
    
    dep_map = mapper.build_dependency_map(files)
    
    assert 'dependencies' in dep_map, "Should have dependencies key"
    assert 'statistics' in dep_map, "Should have statistics key"
    
    print("✓ DependencyMapper working correctly")
    return True


def main():
    """Run all tests."""
    print("Running codebase analyzer tests...\n")
    
    tests = [
        test_duplicate_detector,
        test_unused_import_analyzer,
        test_mock_detector,
        test_dependency_mapper
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
    
    print(f"\nTest Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed! The codebase analyzer is working correctly.")
        return True
    else:
        print("❌ Some tests failed. Please check the implementation.")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)