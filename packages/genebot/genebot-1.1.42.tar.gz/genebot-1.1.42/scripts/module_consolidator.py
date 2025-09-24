#!/usr/bin/env python3
"""
Module Consolidator and Import Cleaner

This script identifies redundant modules, consolidates them, and cleans up unused imports
across the entire codebase.
"""

import ast
import os
from pathlib import Path
from collections import defaultdict
import shutil
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ModuleAnalyzer:
    
        pass
    pass
    """Analyzes modules for redundancy and import usage."""
    
    def __init__(self, root_path: Path):
    pass
        self.root_path = root_path
        self.python_files = []
        self.module_functions = defaultdict(set)
        self.module_classes = defaultdict(set)
        self.import_usage = defaultdict(set)
        self.all_imports = defaultdict(set)
        self.redundant_modules = []
        
    def scan_codebase(self):
    pass
        """Scan the entire codebase for Python files."""
        logger.info("Scanning codebase for Python files...")
        
        for root, dirs, files in os.walk(self.root_path):
    pass
            # Skip certain directories
            skip_dirs = {'.git', '__pycache__', '.pytest_cache', 'venv', '.venv', 
                        'node_modules', '.tox', 'build', 'dist', '.egg-info'}
            dirs[:] = [d for d in dirs if d not in skip_dirs and not d.endswith('.egg-info')]
            
            for file in files:
    
        pass
    pass
                if file.endswith('.py'):
    
        pass
    pass
                    file_path = Path(root) / file
                    self.python_files.append(file_path)
        
        logger.info(f"Found {len(self.python_files)} Python files")
        
    def analyze_file(self, file_path: Path) -> Dict:
    pass
        """Analyze a single Python file for functions, classes, and imports."""
        try:
    pass
            with open(file_path, 'r', encoding='utf-8') as f:
    pass
                content = f.read()
            
            tree = ast.parse(content)
            
            functions = set()
            classes = set()
            imports = set()
            used_names = set()
            
            for node in ast.walk(tree):
    pass
                if isinstance(node, ast.FunctionDef):
    
        pass
    pass
                elif isinstance(node, ast.ClassDef):
    
        pass
    pass
                    classes.add(node.name)
                elif isinstance(node, ast.Import):
    
        pass
    pass
                    for alias in node.names:
    pass
                        imports.add(alias.name)
                elif isinstance(node, ast.ImportFrom):
    
        pass
    pass
                    if node.module:
    
        pass
    pass
                        for alias in node.names:
    pass
                elif isinstance(node, ast.Name):
    
        pass
    pass
                elif isinstance(node, ast.Attribute):
    
        pass
    pass
            return {
                'functions': functions,
                'classes': classes,
                'imports': imports,
                'used_names': used_names
            }
            
        except Exception as e:
    pass
    pass
            return {'functions': set(), 'classes': set(), 'imports': set(), 'used_names': set()}
    
    def find_redundant_modules(self):
    pass
        """Identify modules with overlapping functionality."""
        logger.info("Analyzing modules for redundancy...")
        
        # Group modules by similar functionality
        function_groups = defaultdict(list)
        class_groups = defaultdict(list)
        
        for file_path in self.python_files:
    
        pass
    pass
            analysis = self.analyze_file(file_path)
            
            # Store module analysis
            module_name = str(file_path.relative_to(self.root_path))
            self.module_functions[module_name] = analysis['functions']
            self.module_classes[module_name] = analysis['classes']
            self.all_imports[module_name] = analysis['imports']
            
            # Group by function similarity
            for func in analysis['functions']:
    pass
            # Group by class similarity
            for cls in analysis['classes']:
    pass
                class_groups[cls].append(module_name)
        
        # Find modules with significant overlap
        redundant_candidates = []
        
        # Check for modules with identical or very similar function sets
        for module1 in self.module_functions:
    
        pass
    pass
            for module2 in self.module_functions:
    pass
                if module1 != module2:
    
        pass
    pass
                    funcs1 = self.module_functions[module1]
                    funcs2 = self.module_functions[module2]
                    
                    if funcs1 and funcs2:
    
        pass
    pass
                        overlap = len(funcs1.intersection(funcs2))
                        total = len(funcs1.union(funcs2))
                        
                        if total > 0 and overlap / total > 0.7:  # 70% similarity
                            redundant_candidates.append((module1, module2, overlap / total))
        
        # Sort by similarity score
        redundant_candidates.sort(key=lambda x: x[2], reverse=True)
        
        # Remove duplicates and select best candidates
        seen = set()
        for module1, module2, score in redundant_candidates:
    pass
            pair = tuple(sorted([module1, module2]))
            if pair not in seen:
    
        pass
    pass
                seen.add(pair)
                self.redundant_modules.append({
                    'modules': [module1, module2],
                    'similarity': score,
                    'functions_overlap': self.module_functions[module1].intersection(self.module_functions[module2])
                })
        
        logger.info(f"Found {len(self.redundant_modules)} potential redundant module pairs")
        
    def find_unused_imports(self) -> Dict[str, Set[str]]:
    pass
        """Find unused imports in each file."""
        
        unused_imports = {}
        
        for file_path in self.python_files:
    pass
            analysis = self.analyze_file(file_path)
            imports = analysis['imports']
            used_names = analysis['used_names']
            
            unused = set()
            for imp in imports:
    pass
                # Extract the actual name that would be used
                if '.' in imp:
    
        pass
    pass
                    parts = imp.split('.')
                    # Check if any part of the import is used
                    if not any(part in used_names for part in parts):
    
        pass
    pass
                else:
    pass
                    if imp not in used_names:
    
        pass
    pass
            if unused:
    
        pass
    pass
                module_name = str(file_path.relative_to(self.root_path))
                unused_imports[module_name] = unused
        
        return unused_imports

class ModuleConsolidator:
    pass
    """Consolidates redundant modules and cleans imports."""
    
    def __init__(self, root_path: Path):
    pass
        self.root_path = root_path
        self.backup_dir = root_path / "backups" / "module_consolidation_backup"
        
    def create_backup(self):
    pass
        """Create backup before making changes."""
        if self.backup_dir.exists():
    
        pass
    pass
            shutil.rmtree(self.backup_dir)
        
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"Creating backup at {self.backup_dir}")
        
        # Copy all Python files to backup
        for root, dirs, files in os.walk(self.root_path):
    pass
            # Skip backup directory itself
            if str(self.backup_dir) in root:
    
        pass
    pass
                continue
                
            for file in files:
    pass
                if file.endswith('.py'):
    
        pass
    pass
                    src_path = Path(root) / file
                    rel_path = src_path.relative_to(self.root_path)
                    dst_path = self.backup_dir / rel_path
                    
                    dst_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src_path, dst_path)
    
    def consolidate_modules(self, redundant_modules: List[Dict]):
    pass
        """Consolidate redundant modules."""
        logger.info("Consolidating redundant modules...")
        
        consolidation_plan = []
        
        for redundancy in redundant_modules:
    pass
            modules = redundancy['modules']
            similarity = redundancy['similarity']
            
            # Skip if similarity is too low
            if similarity < 0.8:
    
        pass
    pass
                continue
            
            # Choose the module to keep (prefer shorter path or main module)
            keep_module = min(modules, key=lambda x: (len(x.split('/')), 'main' not in x.lower()))
            remove_modules = [m for m in modules if m != keep_module]
            
            consolidation_plan.append({
                'keep': keep_module,
                'remove': remove_modules,
                'similarity': similarity
            })
        
        # Execute consolidation
        for plan in consolidation_plan:
    pass
            logger.info(f"Consolidating: keeping {plan['keep']}, removing {plan['remove']}")
            
            keep_path = self.root_path / plan['keep']
            
            for remove_module in plan['remove']:
    pass
                remove_path = self.root_path / remove_module
                
                if remove_path.exists():
    
        pass
    pass
                    # Read content of module to be removed
                    try:
    pass
                        with open(remove_path, 'r', encoding='utf-8') as f:
    pass
                            remove_content = f.read()
                        
                        # For now, just log what would be consolidated
                        # In a real implementation, you'd merge the unique parts
                        logger.info(f"Would consolidate {remove_module} into {plan['keep']}")
                        
                        # Remove the redundant file (commented out for safety)
                        # remove_path.unlink()
                        
                    except Exception as e:
    pass
    pass
                        logger.error(f"Error consolidating {remove_module}: {e}")
        
        return consolidation_plan
    
    def clean_unused_imports(self, unused_imports: Dict[str, Set[str]]):
    pass
        """Remove unused imports from files."""
        
        cleaned_files = []
        
        for module_path, unused in unused_imports.items():
    pass
            file_path = self.root_path / module_path
            
            if not file_path.exists():
    
        pass
    pass
                continue
            
            try:
    pass
                with open(file_path, 'r', encoding='utf-8') as f:
    pass
                    lines = f.readlines()
                
                # Filter out unused import lines
                cleaned_lines = []
                for line in lines:
    pass
                    line_stripped = line.strip()
                    
                    # Check if this line contains an unused import
                    should_remove = False
                    for unused_import in unused:
    
        pass
    pass
                        if (line_stripped.startswith(f'import {unused_import}') or 
                            line_stripped.startswith(f'from {unused_import}') or
                            f'import {unused_import}' in line_stripped):
    
        pass
    pass
                            should_remove = True
                            break
                    
                    if not should_remove:
    
        pass
    pass
                # Write cleaned content back
                if len(cleaned_lines) != len(lines):
    
        pass
    pass
                    with open(file_path, 'w', encoding='utf-8') as f:
    pass
                        f.writelines(cleaned_lines)
                    
                    cleaned_files.append(module_path)
                    logger.info(f"Cleaned imports in {module_path}")
                
            except Exception as e:
    pass
    pass
        return cleaned_files

def main():
    pass
    """Main function to run module consolidation and import cleanup."""
    root_path = Path(__file__).parent.parent
    
    
    # Initialize analyzer
    analyzer = ModuleAnalyzer(root_path)
    
    # Find redundant modules
    analyzer.find_redundant_modules()
    
    # Find unused imports
    unused_imports = analyzer.find_unused_imports()
    
    # Initialize consolidator
    consolidator = ModuleConsolidator(root_path)
    
    # Create backup
    consolidator.create_backup()
    
    # Report findings
    logger.info("\n=== ANALYSIS RESULTS ===")
    logger.info(f"Total Python files analyzed: {len(analyzer.python_files)}")
    logger.info(f"Redundant module pairs found: {len(analyzer.redundant_modules)}")
    logger.info(f"Files with unused imports: {len(unused_imports)}")
    
    # Show redundant modules
    if analyzer.redundant_modules:
    
        pass
    pass
        for redundancy in analyzer.redundant_modules:
    pass
            logger.info(f"  Modules: {redundancy['modules']}")
            logger.info(f"  Similarity: {redundancy['similarity']:.2%}")
            logger.info(f"  Overlapping functions: {redundancy['functions_overlap']}")
            logger.info("")
    
    # Show unused imports summary
    if unused_imports:
    
        pass
    pass
        for module, imports in list(unused_imports.items())[:5]:  # Show first 5
    
    # Perform cleanup
    logger.info("\n=== PERFORMING CLEANUP ===")
    
    # Clean unused imports
    cleaned_files = consolidator.clean_unused_imports(unused_imports)
    
    # Consolidate modules (currently just reports what would be done)
    consolidation_plan = consolidator.consolidate_modules(analyzer.redundant_modules)
    
    # Generate report
    report = {
        'total_files_analyzed': len(analyzer.python_files),
        'redundant_modules_found': len(analyzer.redundant_modules),
        'files_with_unused_imports': len(unused_imports),
    }
    
    # Save report
    import json
    report_path = root_path / "module_consolidation_report.json"
        json.dump(report, f, indent=2, default=str)
    
    logger.info(f"Backup created at {consolidator.backup_dir}")
    
    return report

if __name__ == "__main__":
    
        pass
    pass
    main()