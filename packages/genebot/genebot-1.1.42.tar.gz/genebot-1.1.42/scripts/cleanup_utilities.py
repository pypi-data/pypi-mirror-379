#!/usr/bin/env python3
"""
Automated cleanup utilities for the Genebot codebase.
Provides safe file removal, module consolidation, import cleanup, and backup functionality.
"""

import ast
import shutil
import json
import logging
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BackupManager:
    pass
    """Manages backup creation and restoration for safe cleanup operations."""
    
    def __init__(self, backup_dir: str = "backups/cleanup"):
    pass
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        self.backup_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.current_backup_path = self.backup_dir / f"backup_{self.backup_timestamp}"
        
    def create_backup(self, files_to_backup: list[str]) -> str:
    pass
        """Create backup of specified files before cleanup operations."""
        backup_manifest = {
            "timestamp": self.backup_timestamp,
            "files": [],
            "directories": []
        }
        
        self.current_backup_path.mkdir(exist_ok=True)
        
        for file_path in files_to_backup:
    pass
            source_path = Path(file_path)
            if not source_path.exists():
    
        pass
    pass
                continue
                
            # Create relative backup path
            relative_path = source_path.relative_to(Path.cwd()) if source_path.is_absolute() else source_path
            backup_file_path = self.current_backup_path / relative_path
            
            # Create parent directories
            backup_file_path.parent.mkdir(parents=True, exist_ok=True)
            
            if source_path.is_file():
    
        pass
    pass
                shutil.copy2(source_path, backup_file_path)
                backup_manifest["files"].append(str(relative_path))
            elif source_path.is_dir():
    
        pass
    pass
                shutil.copytree(source_path, backup_file_path, dirs_exist_ok=True)
                backup_manifest["directories"].append(str(relative_path))
        
        # Save backup manifest
        manifest_path = self.current_backup_path / "backup_manifest.json"
        with open(manifest_path, 'w') as f:
    
        pass
    pass
            json.dump(backup_manifest, f, indent=2)
            
        logger.info(f"Backup created at: {self.current_backup_path}")
        return str(self.current_backup_path)
    
    def restore_backup(self, backup_path: str) -> bool:
    pass
        """Restore files from a backup."""
        backup_dir = Path(backup_path)
        manifest_path = backup_dir / "backup_manifest.json"
        
        if not manifest_path.exists():
    
        pass
    pass
            return False
            
        try:
    pass
            with open(manifest_path, 'r') as f:
    
        pass
    pass
                manifest = json.load(f)
            
            # Restore files
            for file_path in manifest.get("files", []):
    
        pass
    pass
                backup_file = backup_dir / file_path
                target_file = Path(file_path)
                if backup_file.exists():
    
        pass
    pass
                    target_file.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(backup_file, target_file)
            
            # Restore directories
            for dir_path in manifest.get("directories", []):
    
        pass
    pass
                backup_dir_path = backup_dir / dir_path
                target_dir = Path(dir_path)
                if backup_dir_path.exists():
    
        pass
    pass
                    if target_dir.exists():
    
        pass
    pass
                        shutil.rmtree(target_dir)
                    shutil.copytree(backup_dir_path, target_dir)
            
            logger.info(f"Backup restored from: {backup_path}")
            return True
            
        except Exception as e:
    pass
    pass
            return False


class DependencyChecker:
    pass
    """Analyzes file dependencies to ensure safe removal."""
    
    def __init__(self, project_root: str = ".", exclude_dirs: list[str] = None):
    pass
        self.project_root = Path(project_root)
        self.dependency_map = defaultdict(set)
        self.reverse_dependency_map = defaultdict(set)
        self.exclude_dirs = exclude_dirs or [
            'venv', '.venv', 'env', '.env', 'node_modules', '.git', 
            '__pycache__', '.pytest_cache', '.tox', 'build', 'dist',
            '.kiro', 'backups'
        ]
        self._build_dependency_map()
    
    def _build_dependency_map(self):
    pass
        """Build a map of file dependencies across the project."""
        # Get all Python files, excluding specified directories
        python_files = []
        for file_path in self.project_root.rglob("*.py"):
    
        pass
    pass
            # Check if file is in an excluded directory
            should_exclude = False
            for exclude_dir in self.exclude_dirs:
    
        pass
    pass
                if exclude_dir in file_path.parts:
    
        pass
    pass
                    should_exclude = True
                    break
            
            if not should_exclude:
    
        pass
    pass
                python_files.append(file_path)
        
        for file_path in python_files:
    pass
            try:
    pass
                with open(file_path, 'r', encoding='utf-8') as f:
    pass
                    content = f.read()
                
                tree = ast.parse(content)
                imports = self._extract_imports(tree)
                
                for import_module in imports:
    pass
                    # Convert module import to potential file path
                    potential_files = self._module_to_files(import_module)
                    for potential_file in potential_files:
    pass
                        if potential_file.exists():
    
        pass
    pass
            except Exception as e:
    pass
    pass
                logger.warning(f"Could not analyze dependencies for {file_path}: {e}")
    
    def _extract_imports(self, tree: ast.AST) -> set[str]:
    pass
        """Extract import statements from AST."""
        imports = set()
        
        for node in ast.walk(tree):
    pass
            if isinstance(node, ast.Import):
    
        pass
    pass
                for alias in node.names:
    pass
            elif isinstance(node, ast.ImportFrom):
    
        pass
    pass
                if node.module:
    
        pass
    pass
                    # Add the module itself
                    # For 'from module import item', we care about the module dependency
                    # The specific items imported don't create file dependencies
        
        return imports
    
    def _module_to_files(self, module_name: str) -> list[Path]:
    pass
        """Convert module name to potential file paths."""
        potential_files = []
        
        # Handle relative imports within project
        parts = module_name.split('.')
        
        # Try different combinations
        for i in range(len(parts)):
    
        pass
    pass
            path_parts = parts[:i+1]
            
            # Try as .py file
            if len(path_parts) == 1:
    
        pass
    pass
                # Direct module import like 'math_utils1'
                file_path = self.project_root / f"{path_parts[0]}.py"
            else:
    pass
                # Nested module import
                file_path = self.project_root / '/'.join(path_parts[:-1]) / f"{path_parts[-1]}.py"
            
            # Try as __init__.py in directory
            dir_path = self.project_root / '/'.join(path_parts) / "__init__.py"
            potential_files.append(dir_path)
        
        return potential_files
    
    def is_safe_to_remove(self, file_path: str) -> tuple[bool, list[str]]:
    pass
        """Check if a file is safe to remove based on dependencies."""
        # Try both absolute and relative paths
        abs_path = str(Path(file_path).resolve())
        rel_path = str(Path(file_path))
        
        dependents = set()
        dependents.update(self.reverse_dependency_map.get(abs_path, set()))
        dependents.update(self.reverse_dependency_map.get(rel_path, set()))
        
        # Also check if the file path matches any key in the reverse dependency map
        for key, deps in self.reverse_dependency_map.items():
    
        pass
    pass
            if Path(key).name == Path(file_path).name:
    
        pass
    pass
                dependents.update(deps)
        
        dependents_list = list(dependents)
        
        # File is safe to remove if no other files depend on it
        is_safe = len(dependents_list) == 0
        return is_safe, dependents_list


class SafeFileRemover:
    
        pass
    pass
    """Safely removes files with dependency checking and backup."""
    
    def __init__(self, project_root: str = "."):
    pass
        self.project_root = Path(project_root)
        self.dependency_checker = DependencyChecker(project_root)
        self.backup_manager = BackupManager()
        
    def remove_files_safely(self, files_to_remove: list[str], force: bool = False) -> dict[str, str]:
    pass
        """Remove files safely with dependency checking."""
        results = {}
        files_to_backup = []
        safe_to_remove = []
        
        # Check dependencies for all files
        for file_path in files_to_remove:
    pass
            is_safe, dependents = self.dependency_checker.is_safe_to_remove(file_path)
            
            if is_safe or force:
    
        pass
    pass
                safe_to_remove.append(file_path)
                files_to_backup.append(file_path)
                if not is_safe and force:
    
        pass
    pass
                    results[file_path] = f"FORCED_REMOVAL (dependents: {dependents})"
                else:
    pass
                    results[file_path] = "SAFE_TO_REMOVE"
            else:
    pass
                results[file_path] = f"UNSAFE_TO_REMOVE (dependents: {dependents})"
        
        # Create backup before removal
        if files_to_backup:
    
        pass
    pass
            backup_path = self.backup_manager.create_backup(files_to_backup)
            logger.info(f"Created backup: {backup_path}")
        
        # Remove safe files
        for file_path in safe_to_remove:
    pass
            try:
    pass
                file_obj = Path(file_path)
                if file_obj.exists():
    
        pass
    pass
                    if file_obj.is_file():
    
        pass
    pass
                        file_obj.unlink()
                    elif file_obj.is_dir():
    
        pass
    pass
                        shutil.rmtree(file_obj)
                    logger.info(f"Removed: {file_path}")
                    if results[file_path] == "SAFE_TO_REMOVE":
    
        pass
    pass
                        results[file_path] = "REMOVED"
                    elif "FORCED_REMOVAL" in results[file_path]:
    
        pass
    pass
                        results[file_path] = results[file_path].replace("FORCED_REMOVAL", "FORCE_REMOVED")
            except Exception as e:
    pass
    pass
                results[file_path] = f"REMOVAL_FAILED: {e}"
                logger.error(f"Failed to remove {file_path}: {e}")
        
        return results


class ModuleConsolidator:
    pass
    """Consolidates redundant modules by merging similar functionality."""
    
    def __init__(self, project_root: str = ".", exclude_dirs: list[str] = None):
    pass
        self.project_root = Path(project_root)
        self.backup_manager = BackupManager()
        self.exclude_dirs = exclude_dirs or [
            'venv', '.venv', 'env', '.env', 'node_modules', '.git', 
            '__pycache__', '.pytest_cache', '.tox', 'build', 'dist',
            '.kiro', 'backups'
        ]
    
    def find_similar_modules(self, similarity_threshold: float = 0.7) -> dict[str, list[str]]:
    pass
        """Find modules with similar functionality that could be consolidated."""
        # Get all Python files, excluding specified directories
        python_files = []
        for file_path in self.project_root.rglob("*.py"):
    
        pass
    pass
            # Check if file is in an excluded directory
            should_exclude = False
            for exclude_dir in self.exclude_dirs:
    
        pass
    pass
                if exclude_dir in file_path.parts:
    
        pass
    pass
                    should_exclude = True
                    break
            
            if not should_exclude:
    
        pass
    pass
                python_files.append(file_path)
        
        module_signatures = {}
        
        # Extract signatures from each module
        for file_path in python_files:
    pass
            try:
    pass
                signature = self._extract_module_signature(file_path)
                module_signatures[str(file_path)] = signature
            except Exception as e:
    pass
    pass
                logger.warning(f"Could not analyze {file_path}: {e}")
        
        # Find similar modules
        similar_groups = defaultdict(list)
        processed = set()
        
        for file1, sig1 in module_signatures.items():
    pass
            if file1 in processed:
    
        pass
    pass
                continue
                
            group = [file1]
            processed.add(file1)
            
            for file2, sig2 in module_signatures.items():
    pass
                if file2 in processed:
    
        pass
    pass
                    continue
                    
                similarity = self._calculate_similarity(sig1, sig2)
                if similarity >= similarity_threshold:
    
        pass
    pass
                    group.append(file2)
                    processed.add(file2)
            
            if len(group) > 1:
    
        pass
    pass
                similar_groups[f"group_{len(similar_groups)}"] = group
        
        return dict(similar_groups)
    
    def _extract_module_signature(self, file_path: Path) -> dict[str, set[str]]:
    pass
        """Extract a signature representing the module's functionality."""
        with open(file_path, 'r', encoding='utf-8') as f:
    pass
            content = f.read()
        
        tree = ast.parse(content)
        signature = {
            'functions': set(),
            'classes': set(),
            'imports': set(),
        }
        
        for node in ast.walk(tree):
    pass
            if isinstance(node, ast.FunctionDef):
    
        pass
    pass
                signature['functions'].add(node.name)
            elif isinstance(node, ast.ClassDef):
    
        pass
    pass
                signature['classes'].add(node.name)
            elif isinstance(node, ast.Import):
    
        pass
    pass
                for alias in node.names:
    pass
                    signature['imports'].add(alias.name)
            elif isinstance(node, ast.ImportFrom) and node.module:
    
        pass
    pass
            elif isinstance(node, ast.Assign):
    
        pass
    pass
                for target in node.targets:
    pass
                    if isinstance(target, ast.Name):
    
        pass
    pass
        return signature
    
    def _calculate_similarity(self, sig1: dict[str, set[str]], sig2: dict[str, set[str]]) -> float:
    pass
        """Calculate similarity between two module signatures."""
        total_similarity = 0
        weights = {'functions': 0.4, 'classes': 0.3, 'imports': 0.2, 'constants': 0.1}
        
        for category, weight in weights.items():
    pass
            set1 = sig1.get(category, set())
            set2 = sig2.get(category, set())
            
            if not set1 and not set2:
    
        pass
    pass
                similarity = 1.0
            elif not set1 or not set2:
    
        pass
    pass
                similarity = 0.0
            else:
    pass
                intersection = len(set1.intersection(set2))
                union = len(set1.union(set2))
                similarity = intersection / union if union > 0 else 0.0
            
            total_similarity += similarity * weight
        
        return total_similarity
    
    def consolidate_modules(self, module_groups: dict[str, list[str]], target_dir: str = "consolidated") -> dict[str, str]:
    pass
        """Consolidate similar modules into single files."""
        target_path = self.project_root / target_dir
        target_path.mkdir(exist_ok=True)
        
        results = {}
        all_files_to_backup = []
        
        for group_name, files in module_groups.items():
    pass
            all_files_to_backup.extend(files)
        
        # Create backup
        if all_files_to_backup:
    
        pass
    pass
            backup_path = self.backup_manager.create_backup(all_files_to_backup)
            logger.info(f"Created backup for consolidation: {backup_path}")
        
        for group_name, files in module_groups.items():
    pass
            try:
    pass
                consolidated_content = self._merge_module_contents(files)
                consolidated_file = target_path / f"{group_name}.py"
                
                with open(consolidated_file, 'w', encoding='utf-8') as f:
    pass
                    f.write(consolidated_content)
                
                results[group_name] = {
                    'consolidated_file': str(consolidated_file),
                    'source_files': files,
                    'status': 'SUCCESS'
                }
                
                logger.info(f"Consolidated {len(files)} files into {consolidated_file}")
                
            except Exception as e:
    pass
    pass
                results[group_name] = {
                    'source_files': files,
                    'status': f'FAILED: {e}'
                }
                logger.error(f"Failed to consolidate {group_name}: {e}")
        
        return results
    
    def _merge_module_contents(self, files: list[str]) -> str:
    pass
        """Merge contents of multiple modules into a single module."""
        merged_content = []
        imports = set()
        functions = {}
        classes = {}
        constants = {}
        
        for file_path in files:
    pass
            with open(file_path, 'r', encoding='utf-8') as f:
    pass
                content = f.read()
            
            try:
    pass
                tree = ast.parse(content)
                
                for node in ast.walk(tree):
    pass
                    if isinstance(node, (ast.Import, ast.ImportFrom)):
    
        pass
    pass
                        imports.add(ast.unparse(node))
                    elif isinstance(node, ast.FunctionDef):
    
        pass
    pass
                        if node.name not in functions:
    
        pass
    pass
                            functions[node.name] = ast.unparse(node)
                    elif isinstance(node, ast.ClassDef):
    
        pass
    pass
                        if node.name not in classes:
    
        pass
    pass
                            classes[node.name] = ast.unparse(node)
                    elif isinstance(node, ast.Assign):
    
        pass
    pass
                        for target in node.targets:
    pass
                            if isinstance(target, ast.Name):
    
        pass
    pass
                                if target.id not in constants:
    
        pass
    pass
                                    constants[target.id] = ast.unparse(node)
                                    
            except Exception as e:
    pass
    pass
                logger.warning(f"Could not parse {file_path} for merging: {e}")
                # Fallback: include raw content with comment
                merged_content.append(f"\n# Content from {file_path}\n{content}\n")
        
        # Build merged content
        result = []
        
        # Add header comment
        result.append(f'"""')
        result.append(f'Consolidated module created from:')
        for file_path in files:
    pass
        # Add imports
        if imports:
    
        pass
    pass
        # Add constants
        if constants:
    
        pass
    pass
            result.append('')
        
        # Add classes
        if classes:
    
        pass
    pass
            result.extend(classes.values())
            result.append('')
        
        # Add functions
        if functions:
    
        pass
    pass
            result.extend(functions.values())
            result.append('')
        
        # Add any additional content
        result.extend(merged_content)
        
        return '\n'.join(result)


class ImportCleaner:
    pass
    """Cleans up unused imports from Python files."""
    
    def __init__(self, project_root: str = ".", exclude_dirs: list[str] = None):
    pass
        self.project_root = Path(project_root)
        self.backup_manager = BackupManager()
        self.exclude_dirs = exclude_dirs or [
            'venv', '.venv', 'env', '.env', 'node_modules', '.git', 
            '__pycache__', '.pytest_cache', '.tox', 'build', 'dist',
            '.kiro', 'backups'
        ]
    
    def find_unused_imports(self, file_path: str) -> list[str]:
    pass
        """Find unused imports in a Python file."""
        try:
    pass
            with open(file_path, 'r', encoding='utf-8') as f:
    pass
                content = f.read()
            
            tree = ast.parse(content)
            
            # Extract all imports
            imports = {}
            for node in ast.walk(tree):
    pass
                if isinstance(node, ast.Import):
    
        pass
    pass
                    for alias in node.names:
    pass
                        name = alias.asname if alias.asname else alias.name
                        imports[name] = ast.unparse(node)
                elif isinstance(node, ast.ImportFrom):
    
        pass
    pass
                    for alias in node.names:
    pass
                        name = alias.asname if alias.asname else alias.name
                        imports[name] = ast.unparse(node)
            
            # Find which imports are actually used
            used_names = set()
            for node in ast.walk(tree):
    
        pass
    pass
                if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
    
        pass
    pass
                elif isinstance(node, ast.Attribute):
    
        pass
    pass
                    # Handle attribute access like module.function
                    if isinstance(node.value, ast.Name):
    
        pass
    pass
                        used_names.add(node.value.id)
            
            # Find unused imports
            unused_imports = []
            for import_name in imports:
    pass
                if import_name not in used_names:
    
        pass
    pass
                    # Check if it's a module that might be used via attribute access
                    module_used = any(name.startswith(f"{import_name}.") for name in used_names)
                    if not module_used:
    
        pass
    pass
            return unused_imports
            
        except Exception as e:
    pass
    pass
            return []
    
    def clean_imports_in_file(self, file_path: str) -> dict[str, any]:
    pass
        """Remove unused imports from a single file."""
        unused_imports = self.find_unused_imports(file_path)
        
        if not unused_imports:
    
        pass
    pass
            return {
                'status': 'NO_UNUSED_IMPORTS'
            }
        
        try:
    pass
            # Create backup
            self.backup_manager.create_backup([file_path])
            
            # Read original content
            with open(file_path, 'r', encoding='utf-8') as f:
    pass
                content = f.read()
            
            # Remove unused imports
            lines = content.split('\n')
            cleaned_lines = []
            
            for line in lines:
    pass
                line_should_be_kept = True
                for unused_import in unused_imports:
    pass
                    if unused_import.strip() == line.strip():
    
        pass
    pass
                        line_should_be_kept = False
                        break
                
                if line_should_be_kept:
    
        pass
    pass
            # Write cleaned content
            cleaned_content = '\n'.join(cleaned_lines)
            with open(file_path, 'w', encoding='utf-8') as f:
    pass
                f.write(cleaned_content)
            
            return {
                'file': file_path,
                'unused_imports': unused_imports,
                'status': 'CLEANED'
            }
            
        except Exception as e:
    pass
    pass
            return {
                'file': file_path,
                'unused_imports': unused_imports,
                'status': f'FAILED: {e}'
            }
    
    def clean_imports_in_directory(self, directory: str = None) -> list[dict[str, any]]:
    pass
        """Clean unused imports in all Python files in a directory."""
        if directory is None:
    
        pass
    pass
            directory = self.project_root
        else:
    pass
            directory = Path(directory)
        
        # Get all Python files, excluding specified directories
        python_files = []
        for file_path in directory.rglob("*.py"):
    
        pass
    pass
            # Check if file is in an excluded directory
            should_exclude = False
            for exclude_dir in self.exclude_dirs:
    
        pass
    pass
                if exclude_dir in file_path.parts:
    
        pass
    pass
                    should_exclude = True
                    break
            
            if not should_exclude:
    
        pass
    pass
                python_files.append(file_path)
        
        results = []
        
        for file_path in python_files:
    pass
            result = self.clean_imports_in_file(str(file_path))
            
            if result['status'] == 'CLEANED':
    
        pass
    pass
        return results


class CleanupOrchestrator:
    pass
    """Orchestrates all cleanup operations with proper sequencing and safety checks."""
    
    def __init__(self, project_root: str = "."):
    pass
        self.project_root = Path(project_root)
        self.backup_manager = BackupManager()
        self.file_remover = SafeFileRemover(project_root)
        self.module_consolidator = ModuleConsolidator(project_root)
        self.import_cleaner = ImportCleaner(project_root)
    
    def run_full_cleanup(self, config: dict[str, any] = None) -> dict[str, any]:
    pass
        """Run complete cleanup process with all utilities."""
        if config is None:
    
        pass
    pass
            config = {
                'remove_duplicates': True,
                'consolidate_modules': True,
                'clean_imports': True,
                'force_removal': False
            }
        
        results = {
            'timestamp': datetime.now().isoformat(),
            'config': config,
            'operations': {}
        }
        
        try:
    pass
            # Step 1: Clean imports first (safest operation)
            if config.get('clean_imports', True):
    
        pass
    pass
                import_results = self.import_cleaner.clean_imports_in_directory()
                results['operations']['import_cleanup'] = {
                    'summary': {
                        'files_cleaned': len([r for r in import_results if r['status'] == 'CLEANED'])
                    }
                }
            
            # Step 2: Module consolidation
            if config.get('consolidate_modules', True):
    
        pass
    pass
                logger.info("Starting module consolidation...")
                similar_modules = self.module_consolidator.find_similar_modules(
                    config.get('similarity_threshold', 0.7)
                )
                if similar_modules:
    
        pass
    pass
                    consolidation_results = self.module_consolidator.consolidate_modules(similar_modules)
                    results['operations']['module_consolidation'] = {
                        'status': 'COMPLETED',
                        'similar_groups': similar_modules,
                        'consolidation_results': consolidation_results
                    }
                else:
    pass
                    results['operations']['module_consolidation'] = {
                        'status': 'NO_SIMILAR_MODULES_FOUND'
                    }
            
            # Step 3: File removal (most risky, done last)
            if config.get('remove_duplicates', True):
    
        pass
    pass
                logger.info("File removal would be handled by duplicate detection from task 1...")
                results['operations']['file_removal'] = {
                    'note': 'File removal should be done after duplicate detection from task 1'
                }
            
            results['overall_status'] = 'SUCCESS'
            
        except Exception as e:
    pass
    pass
            results['overall_status'] = f'FAILED: {e}'
            logger.error(f"Cleanup process failed: {e}")
        
        return results


if __name__ == "__main__":
    
        pass
    pass
    # Example usage
    orchestrator = CleanupOrchestrator()
    
    # Run with default configuration
    results = orchestrator.run_full_cleanup()
    
    # Print summary
    print(json.dumps(results, indent=2))