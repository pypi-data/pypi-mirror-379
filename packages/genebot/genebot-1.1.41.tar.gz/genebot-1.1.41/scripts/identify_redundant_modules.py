#!/usr/bin/env python3
"""
Identify Redundant Modules

This script identifies modules with overlapping functionality in the main codebase
and suggests consolidation opportunities.
"""

import ast
import os
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict
import logging
import json

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class RedundancyAnalyzer:
    """Analyzes modules for redundancy and overlapping functionality."""
    
    def __init__(self, root_path: Path):
        self.root_path = root_path
        self.module_analysis = {}
        self.redundancy_groups = []
        
    def should_skip_file(self, file_path: Path) -> bool:
        """Check if file should be skipped."""
        path_str = str(file_path)
        
        # Skip backup directories, consolidated files, and other non-essential directories
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
            '.egg-info',
            'migrations/',  # Database migrations
            'tests/',       # Test files
            'test_',        # Test files
        ]
        
        return any(pattern in path_str for pattern in skip_patterns)
    
    def analyze_module(self, file_path: Path) -> Dict:
        """Analyze a single module for its functionality."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if not content.strip():
                return None
            
            tree = ast.parse(content)
            
            functions = []
            classes = []
            imports = []
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    functions.append({
                        'name': node.name,
                        'args': [arg.arg for arg in node.args.args],
                        'line': node.lineno
                    })
                elif isinstance(node, ast.ClassDef):
                    methods = []
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef):
                            methods.append(item.name)
                    
                    classes.append({
                        'name': node.name,
                        'methods': methods,
                        'line': node.lineno
                    })
                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports.append(node.module)
            
            return {
                'path': str(file_path.relative_to(self.root_path)),
                'functions': functions,
                'classes': classes,
                'imports': imports,
                'size': len(content),
                'lines': len(content.splitlines())
            }
            
        except Exception as e:
            logger.warning(f"Error analyzing {file_path}: {e}")
            return None
    
    def find_similar_modules(self) -> List[Dict]:
        """Find modules with similar functionality."""
        logger.info("Analyzing modules for similarity...")
        
        # Group modules by similar characteristics
        function_groups = defaultdict(list)
        class_groups = defaultdict(list)
        import_groups = defaultdict(list)
        
        for module_path, analysis in self.module_analysis.items():
            if not analysis:
                continue
            
            # Group by function names
            func_names = {f['name'] for f in analysis['functions']}
            if func_names:
                func_signature = tuple(sorted(func_names))
                function_groups[func_signature].append(module_path)
            
            # Group by class names
            class_names = {c['name'] for c in analysis['classes']}
            if class_names:
                class_signature = tuple(sorted(class_names))
                class_groups[class_signature].append(module_path)
            
            # Group by import patterns
            import_set = set(analysis['imports'])
            if import_set:
                import_signature = tuple(sorted(import_set))
                import_groups[import_signature].append(module_path)
        
        # Find redundant groups
        redundant_groups = []
        
        # Check function-based similarity
        for func_sig, modules in function_groups.items():
            if len(modules) > 1:
                redundant_groups.append({
                    'type': 'function_similarity',
                    'modules': modules,
                    'similarity_basis': list(func_sig),
                    'count': len(modules)
                })
        
        # Check class-based similarity
        for class_sig, modules in class_groups.items():
            if len(modules) > 1:
                redundant_groups.append({
                    'type': 'class_similarity',
                    'modules': modules,
                    'similarity_basis': list(class_sig),
                    'count': len(modules)
                })
        
        # Check import-based similarity (high import overlap might indicate similar functionality)
        for import_sig, modules in import_groups.items():
            if len(modules) > 1 and len(import_sig) > 3:  # Only consider if significant imports
                redundant_groups.append({
                    'type': 'import_similarity',
                    'modules': modules,
                    'similarity_basis': list(import_sig),
                    'count': len(modules)
                })
        
        return redundant_groups
    
    def find_duplicate_functionality(self) -> List[Dict]:
        """Find modules with duplicate or very similar functionality."""
        logger.info("Looking for duplicate functionality...")
        
        duplicates = []
        
        # Compare modules pairwise for similar function signatures
        modules = list(self.module_analysis.items())
        
        for i, (path1, analysis1) in enumerate(modules):
            if not analysis1:
                continue
                
            for j, (path2, analysis2) in enumerate(modules[i+1:], i+1):
                if not analysis2:
                    continue
                
                # Compare function names
                funcs1 = {f['name'] for f in analysis1['functions']}
                funcs2 = {f['name'] for f in analysis2['functions']}
                
                if funcs1 and funcs2:
                    overlap = funcs1.intersection(funcs2)
                    total = funcs1.union(funcs2)
                    
                    if total and len(overlap) / len(total) > 0.5:  # 50% overlap
                        duplicates.append({
                            'modules': [path1, path2],
                            'function_overlap': list(overlap),
                            'overlap_ratio': len(overlap) / len(total),
                            'type': 'function_duplicate'
                        })
                
                # Compare class names and methods
                classes1 = {c['name']: set(c['methods']) for c in analysis1['classes']}
                classes2 = {c['name']: set(c['methods']) for c in analysis2['classes']}
                
                common_classes = set(classes1.keys()).intersection(set(classes2.keys()))
                if common_classes:
                    method_overlap = 0
                    total_methods = 0
                    
                    for class_name in common_classes:
                        methods1 = classes1[class_name]
                        methods2 = classes2[class_name]
                        method_overlap += len(methods1.intersection(methods2))
                        total_methods += len(methods1.union(methods2))
                    
                    if total_methods > 0 and method_overlap / total_methods > 0.5:
                        duplicates.append({
                            'modules': [path1, path2],
                            'class_overlap': list(common_classes),
                            'overlap_ratio': method_overlap / total_methods,
                            'type': 'class_duplicate'
                        })
        
        return duplicates
    
    def suggest_consolidations(self, duplicates: List[Dict]) -> List[Dict]:
        """Suggest specific consolidation actions."""
        logger.info("Generating consolidation suggestions...")
        
        suggestions = []
        
        for duplicate in duplicates:
            modules = duplicate['modules']
            
            # Analyze which module should be kept
            module_stats = []
            for module_path in modules:
                analysis = self.module_analysis[module_path]
                if analysis:
                    module_stats.append({
                        'path': module_path,
                        'size': analysis['size'],
                        'lines': analysis['lines'],
                        'functions': len(analysis['functions']),
                        'classes': len(analysis['classes'])
                    })
            
            if len(module_stats) >= 2:
                # Prefer the module with more functionality or in a more appropriate location
                primary_module = max(module_stats, key=lambda x: (x['functions'] + x['classes'], x['size']))
                secondary_modules = [m for m in module_stats if m['path'] != primary_module['path']]
                
                suggestions.append({
                    'action': 'consolidate',
                    'keep': primary_module['path'],
                    'merge_from': [m['path'] for m in secondary_modules],
                    'reason': f"{duplicate['type']} with {duplicate['overlap_ratio']:.2%} overlap",
                    'overlap_details': duplicate.get('function_overlap', duplicate.get('class_overlap', []))
                })
        
        return suggestions
    
    def analyze_codebase(self):
        """Analyze the entire codebase for redundancies."""
        logger.info("Starting codebase redundancy analysis...")
        
        # Find all Python files
        python_files = []
        for root, dirs, files in os.walk(self.root_path):
            # Skip certain directories
            dirs[:] = [d for d in dirs if not self.should_skip_file(Path(root) / d)]
            
            for file in files:
                if file.endswith('.py'):
                    file_path = Path(root) / file
                    if not self.should_skip_file(file_path):
                        python_files.append(file_path)
        
        logger.info(f"Found {len(python_files)} Python files to analyze")
        
        # Analyze each module
        for file_path in python_files:
            analysis = self.analyze_module(file_path)
            if analysis:
                self.module_analysis[analysis['path']] = analysis
        
        logger.info(f"Successfully analyzed {len(self.module_analysis)} modules")
        
        # Find similar modules
        similar_groups = self.find_similar_modules()
        
        # Find duplicate functionality
        duplicates = self.find_duplicate_functionality()
        
        # Generate consolidation suggestions
        suggestions = self.suggest_consolidations(duplicates)
        
        return {
            'total_modules_analyzed': len(self.module_analysis),
            'similar_groups': similar_groups,
            'duplicates': duplicates,
            'consolidation_suggestions': suggestions
        }

def main():
    """Main function to run redundancy analysis."""
    root_path = Path(__file__).parent.parent
    
    logger.info("Starting module redundancy analysis...")
    
    analyzer = RedundancyAnalyzer(root_path)
    results = analyzer.analyze_codebase()
    
    # Generate report
    logger.info("\n=== REDUNDANCY ANALYSIS RESULTS ===")
    logger.info(f"Total modules analyzed: {results['total_modules_analyzed']}")
    logger.info(f"Similar module groups found: {len(results['similar_groups'])}")
    logger.info(f"Duplicate functionality pairs: {len(results['duplicates'])}")
    logger.info(f"Consolidation suggestions: {len(results['consolidation_suggestions'])}")
    
    # Show some examples
    if results['consolidation_suggestions']:
        logger.info("\nTop consolidation suggestions:")
        for i, suggestion in enumerate(results['consolidation_suggestions'][:5]):
            logger.info(f"{i+1}. Keep: {suggestion['keep']}")
            logger.info(f"   Merge from: {suggestion['merge_from']}")
            logger.info(f"   Reason: {suggestion['reason']}")
            logger.info("")
    
    # Save detailed report
    report_path = root_path / "redundancy_analysis_report.json"
    with open(report_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    logger.info(f"Detailed report saved to {report_path}")
    
    return results

if __name__ == "__main__":
    main()