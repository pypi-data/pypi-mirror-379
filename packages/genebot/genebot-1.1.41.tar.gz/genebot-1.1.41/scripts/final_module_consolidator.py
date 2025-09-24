#!/usr/bin/env python3
"""
Final Module Consolidator

This script performs the actual consolidation of redundant modules based on the analysis.
It focuses on safe consolidations that won't break the system.
"""

import os
import shutil
from pathlib import Path
from typing import List, Dict
import logging
import json

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FinalConsolidator:
    """Performs final consolidation of redundant modules."""
    
    def __init__(self, root_path: Path):
        self.root_path = root_path
        self.backup_dir = root_path / "backups" / "final_consolidation_backup"
        self.consolidated_files = []
        self.removed_files = []
        
    def create_backup(self):
        """Create backup before making changes."""
        if self.backup_dir.exists():
            shutil.rmtree(self.backup_dir)
        
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Creating backup at {self.backup_dir}")
        
        # Copy main codebase files to backup
        for root, dirs, files in os.walk(self.root_path):
            # Skip backup directories themselves
            if 'backups' in root or 'consolidated' in root:
                continue
                
            for file in files:
                if file.endswith('.py'):
                    src_path = Path(root) / file
                    rel_path = src_path.relative_to(self.root_path)
                    dst_path = self.backup_dir / rel_path
                    
                    dst_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src_path, dst_path)
    
    def consolidate_duplicate_orchestrators(self):
        """Consolidate the duplicate orchestrator files."""
        logger.info("Consolidating duplicate orchestrator files...")
        
        genebot_orchestrator = self.root_path / "genebot" / "core" / "orchestrator.py"
        src_orchestrator = self.root_path / "src" / "trading_bot_orchestrator.py"
        
        if genebot_orchestrator.exists() and src_orchestrator.exists():
            # Keep the genebot version as it's in the proper package structure
            logger.info(f"Removing duplicate orchestrator: {src_orchestrator}")
            src_orchestrator.unlink()
            self.removed_files.append(str(src_orchestrator.relative_to(self.root_path)))
    
    def consolidate_strategy_files(self):
        """Consolidate duplicate strategy files between genebot and src."""
        logger.info("Consolidating duplicate strategy files...")
        
        strategy_pairs = [
            ("genebot/strategies/strategy_registry.py", "src/strategies/strategy_registry.py"),
            ("genebot/strategies/market_specific_strategy.py", "src/strategies/market_specific_strategy.py"),
            ("genebot/strategies/market_agnostic_strategy.py", "src/strategies/market_agnostic_strategy.py"),
            ("genebot/strategies/base_strategy.py", "src/strategies/base_strategy.py"),
            ("genebot/strategies/rsi_strategy.py", "src/strategies/rsi_strategy.py"),
            ("genebot/strategies/strategy_engine.py", "src/strategies/strategy_engine.py"),
            ("genebot/strategies/strategy_config.py", "src/strategies/strategy_config.py"),
        ]
        
        for genebot_file, src_file in strategy_pairs:
            genebot_path = self.root_path / genebot_file
            src_path = self.root_path / src_file
            
            if genebot_path.exists() and src_path.exists():
                logger.info(f"Removing duplicate strategy file: {src_file}")
                src_path.unlink()
                self.removed_files.append(src_file)
    
    def consolidate_exception_files(self):
        """Consolidate duplicate exception files between genebot and src."""
        logger.info("Consolidating duplicate exception files...")
        
        exception_pairs = [
            ("genebot/exceptions/regulatory_handler.py", "src/exceptions/regulatory_handler.py"),
            ("genebot/exceptions/broker_failover.py", "src/exceptions/broker_failover.py"),
            ("genebot/exceptions/market_closure_handler.py", "src/exceptions/market_closure_handler.py"),
        ]
        
        for genebot_file, src_file in exception_pairs:
            genebot_path = self.root_path / genebot_file
            src_path = self.root_path / src_file
            
            if genebot_path.exists() and src_path.exists():
                logger.info(f"Removing duplicate exception file: {src_file}")
                src_path.unlink()
                self.removed_files.append(src_file)
    
    def remove_empty_example_files(self):
        """Remove example files that are essentially empty or just contain main()."""
        logger.info("Removing empty or minimal example files...")
        
        examples_dir = self.root_path / "examples"
        if not examples_dir.exists():
            return
        
        for example_file in examples_dir.glob("*.py"):
            try:
                with open(example_file, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                
                # Remove files that are very small or only contain basic structure
                if (len(content) < 200 or 
                    content.count('\n') < 10 or
                    ('def main():' in content and content.count('def ') == 1)):
                    
                    logger.info(f"Removing minimal example file: {example_file.name}")
                    example_file.unlink()
                    self.removed_files.append(str(example_file.relative_to(self.root_path)))
                    
            except Exception as e:
                logger.warning(f"Error processing example file {example_file}: {e}")
    
    def clean_empty_directories(self):
        """Remove empty directories after file removal."""
        logger.info("Cleaning up empty directories...")
        
        # Check src directory structure
        src_dir = self.root_path / "src"
        if src_dir.exists():
            for root, dirs, files in os.walk(src_dir, topdown=False):
                for dir_name in dirs:
                    dir_path = Path(root) / dir_name
                    try:
                        if not any(dir_path.iterdir()):  # Directory is empty
                            logger.info(f"Removing empty directory: {dir_path.relative_to(self.root_path)}")
                            dir_path.rmdir()
                    except OSError:
                        pass  # Directory not empty or other error
    
    def update_import_statements(self):
        """Update import statements to point to consolidated modules."""
        logger.info("Updating import statements...")
        
        # Common import replacements
        import_replacements = {
            'from genebot.strategies.': 'from genebot.strategies.',
            'from genebot.exceptions.': 'from genebot.exceptions.',
            'from genebot.core.orchestrator': 'from genebot.core.orchestrator',
            'import genebot.strategies.': 'import genebot.strategies.',
            'import genebot.exceptions.': 'import genebot.exceptions.',
        }
        
        # Find all Python files to update
        python_files = []
        for root, dirs, files in os.walk(self.root_path):
            # Skip backup and consolidated directories
            if 'backups' in root or 'consolidated' in root:
                continue
                
            for file in files:
                if file.endswith('.py'):
                    python_files.append(Path(root) / file)
        
        updated_files = []
        for file_path in python_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Apply import replacements
                for old_import, new_import in import_replacements.items():
                    content = content.replace(old_import, new_import)
                
                # Write back if changed
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    updated_files.append(str(file_path.relative_to(self.root_path)))
                    
            except Exception as e:
                logger.warning(f"Error updating imports in {file_path}: {e}")
        
        logger.info(f"Updated imports in {len(updated_files)} files")
        return updated_files
    
    def consolidate_all(self):
        """Perform all consolidation steps."""
        logger.info("Starting final module consolidation...")
        
        # Create backup
        self.create_backup()
        
        # Perform consolidations
        self.consolidate_duplicate_orchestrators()
        self.consolidate_strategy_files()
        self.consolidate_exception_files()
        self.remove_empty_example_files()
        
        # Update imports
        updated_imports = self.update_import_statements()
        
        # Clean up empty directories
        self.clean_empty_directories()
        
        # Generate report
        report = {
            'removed_files': self.removed_files,
            'updated_import_files': updated_imports,
            'total_files_removed': len(self.removed_files),
            'total_imports_updated': len(updated_imports),
            'backup_location': str(self.backup_dir)
        }
        
        return report

def main():
    """Main function to run final consolidation."""
    root_path = Path(__file__).parent.parent
    
    logger.info("Starting final module consolidation...")
    
    consolidator = FinalConsolidator(root_path)
    report = consolidator.consolidate_all()
    
    # Save report
    report_path = root_path / "final_consolidation_report.json"
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    logger.info(f"\nFinal consolidation completed!")
    logger.info(f"Files removed: {report['total_files_removed']}")
    logger.info(f"Import statements updated: {report['total_imports_updated']}")
    logger.info(f"Backup created at: {report['backup_location']}")
    logger.info(f"Report saved to: {report_path}")
    
    return report

if __name__ == "__main__":
    main()