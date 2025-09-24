#!/usr/bin/env python3
"""
Refined Mock Implementation Remover

This script specifically targets actual mock implementations and test stubs
while preserving real functionality that may have "mock" in the name but serves
a real purpose (like database adapters).
"""

import shutil
from pathlib import Path
import logging
import json
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class RefinedMockRemover:
    """Removes only actual mock implementations and test stubs."""
    
    def __init__(self, root_dir: Path):
        self.root_dir = root_dir
        self.removed_files: List[str] = []
        self.modified_files: List[str] = []
        self.backup_dir = Path('backups/refined_mock_removal_backup')
        
        # Files that are definitely mock implementations for testing
        self.definite_mock_files = [
            'src/strategies/mock_strategies.py',
            'src/orchestration/test_utils.py'
        ]
        
        # Patterns that indicate test/mock code
        self.test_indicators = [
            'for testing', 'test purposes', 'mock implementation',
            'test stub', 'testing only', 'demo purposes'
        ]
        
    def create_backup(self) -> None:
        """Create backup before removing mocks."""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.backup_dir = Path(f'backups/refined_mock_removal_backup_{timestamp}')
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Created backup directory: {self.backup_dir}")
        
    def is_actual_mock_file(self, file_path: Path) -> bool:
        """Check if file is an actual mock implementation (not real functionality)."""
        # Check if it's in our definite mock files list
        relative_path = str(file_path.relative_to(self.root_dir))
        if relative_path in self.definite_mock_files:
            return True
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Check for explicit test/mock indicators in docstrings and comments
            lines = content.split('\n')
            for line in lines[:20]:  # Check first 20 lines
                line_lower = line.lower()
                if any(indicator in line_lower for indicator in self.test_indicators):
                    return True
                    
            # Check for mock strategy patterns
            if 'mock_strategies.py' in file_path.name:
                return True
                
            # Check for test utility patterns
            if 'test_utils.py' in file_path.name and 'src/' in str(file_path):
                return True
                
        except Exception as e:
            logger.warning(f"Could not read file {file_path}: {e}")
            
        return False
        
    def remove_actual_mock_files(self) -> None:
        """Remove only actual mock implementation files."""
        logger.info("Scanning for actual mock files to remove...")
        
        for mock_file in self.definite_mock_files:
            file_path = self.root_dir / mock_file
            if file_path.exists():
                # Create backup
                backup_path = self.backup_dir / file_path.relative_to(self.root_dir)
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file_path, backup_path)
                
                # Remove the file
                file_path.unlink()
                self.removed_files.append(str(file_path))
                logger.info(f"Removed mock file: {file_path}")
                
    def clean_mock_imports_from_files(self) -> None:
        """Remove mock-related imports and references from production files."""
        logger.info("Cleaning mock imports from production files...")
        
        production_dirs = ['src', 'genebot']
        for prod_dir in production_dirs:
            prod_path = self.root_dir / prod_dir
            if not prod_path.exists():
                continue
                
            for py_file in prod_path.rglob('*.py'):
                if py_file.exists():
                    self._clean_file_mock_imports(py_file)
                    
    def _clean_file_mock_imports(self, file_path: Path) -> None:
        """Clean mock imports from a specific file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
                
            lines = original_content.split('\n')
            cleaned_lines = []
            modified = False
            skip_next = False
            
            for i, line in enumerate(lines):
                if skip_next:
                    skip_next = False
                    continue
                    
                line_lower = line.lower().strip()
                
                # Skip mock strategy imports
                if any(mock_import in line_lower for mock_import in [
                    'from ..strategies.mock_strategies import',
                    'from .mock_strategies import',
                    'from genebot.strategies.mock_strategies import'
                ]):
                    modified = True
                    logger.debug(f"Removed mock import: {line.strip()}")
                    continue
                    
                # Skip mock strategy registration code
                if any(mock_ref in line_lower for mock_ref in [
                    'register_mock_strategies', 'mock_registry'
                ]):
                    modified = True
                    logger.debug(f"Removed mock reference: {line.strip()}")
                    # Also skip the next few lines if they're part of the same block
                    if 'try:' in line_lower or 'if' in line_lower:
                        # Skip the entire try/except or if block
                        indent_level = len(line) - len(line.lstrip())
                        j = i + 1
                        while j < len(lines) and (
                            lines[j].strip() == '' or 
                            len(lines[j]) - len(lines[j].lstrip()) > indent_level or
                            lines[j].strip().startswith('except') or
                            lines[j].strip().startswith('finally')
                        ):
                            j += 1
                        # Skip all these lines
                        for k in range(i + 1, min(j, len(lines))):
                            if k < len(lines):
                                logger.debug(f"Skipped mock block line: {lines[k].strip()}")
                        i = j - 1  # Will be incremented by the loop
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
                logger.info(f"Cleaned mock imports from: {file_path}")
                
        except Exception as e:
            logger.error(f"Error cleaning file {file_path}: {e}")
            
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
        """Run the refined mock cleanup process."""
        logger.info("Starting refined mock implementation cleanup...")
        
        # Create backup
        self.create_backup()
        
        # Remove actual mock files
        self.remove_actual_mock_files()
        
        # Clean mock imports from remaining files
        self.clean_mock_imports_from_files()
        
        # Generate report
        report = self.generate_report()
        
        logger.info("Refined mock cleanup completed successfully!")
        logger.info(f"Files removed: {len(self.removed_files)}")
        logger.info(f"Files modified: {len(self.modified_files)}")
        
        return report


def main():
    """Main function to run refined mock implementation removal."""
    root_dir = Path('.')
    
    # Initialize remover
    remover = RefinedMockRemover(root_dir)
    
    # Run cleanup
    report = remover.run_cleanup()
    
    # Save report
    report_file = Path('refined_mock_removal_report.json')
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
        
    print(f"\nRefined mock removal completed!")
    print(f"Report saved to: {report_file}")
    print(f"Backup created at: {report['backup_location']}")
    print(f"Files removed: {report['summary']['files_removed']}")
    print(f"Files modified: {report['summary']['files_modified']}")


if __name__ == '__main__':
    main()