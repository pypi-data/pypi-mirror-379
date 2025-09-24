"""
File Management Utilities
========================

Safe file operations with backup and rollback capabilities.
"""

import shutil
from pathlib import Path
from typing import Optional, Dict, Any, List
from datetime import datetime
import yaml
import json
import os

from .error_handler import CLIException, ConfigurationError


class FileManager:
    pass
    """Safe file operations manager with backup and rollback"""
    
    def __init__(self, backup_dir: Optional[Path] = None):
    pass
        self.backup_dir = backup_dir or Path("backups")
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        self._backup_registry = {}
    
    def create_backup(self, file_path: Path) -> Optional[Path]:
    pass
        """Create a backup of a file before modification"""
        if not file_path.exists():
    
        pass
    pass
            return None
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{file_path.name}.{timestamp}.backup"
        backup_path = self.backup_dir / backup_name
        
        try:
    pass
            shutil.copy2(file_path, backup_path)
            self._backup_registry[str(file_path)] = backup_path
            return backup_path
        except Exception as e:
    pass
    pass
            raise CLIException(
                f"Failed to create backup for {file_path}: {str(e)}",
                suggestions=[
                    "Check file permissions",
                    "Ensure backup directory is writable",
                    "Check available disk space"
                ]
            )
    
    def restore_backup(self, file_path: Path) -> bool:
    pass
        """Restore a file from its most recent backup"""
        backup_path = self._backup_registry.get(str(file_path))
        if not backup_path or not backup_path.exists():
    
        pass
    pass
            return False
        
        try:
    pass
            shutil.copy2(backup_path, file_path)
            return True
        except Exception:
    pass
    pass
            return False
    
    def safe_write_yaml(self, file_path: Path, data: Dict[str, Any], 
                       create_backup: bool = True) -> None:
    pass
        """Safely write YAML data with backup"""
        if create_backup and file_path.exists():
    
        pass
    pass
            self.create_backup(file_path)
        
        # Write to temporary file first
        temp_file = file_path.with_suffix(f"{file_path.suffix}.tmp")
        
        try:
    pass
            with open(temp_file, 'w') as f:
    pass
                yaml.dump(data, f, default_flow_style=False, indent=2)
            
            # Atomic move
            temp_file.replace(file_path)
            
        except Exception as e:
    pass
    pass
            # Clean up temp file
            if temp_file.exists():
    
        pass
    pass
                temp_file.unlink()
            
            raise ConfigurationError(
                f"Failed to write YAML file {file_path}: {str(e)}",
                suggestions=[
                    "Check file permissions",
                    "Verify YAML data structure is valid",
                    "Ensure directory exists and is writable"
                ]
            )
    
    def safe_write_json(self, file_path: Path, data: Dict[str, Any],
                       create_backup: bool = True) -> None:
    pass
        """Safely write JSON data with backup"""
        if create_backup and file_path.exists():
    
        pass
    pass
            self.create_backup(file_path)
        
        # Write to temporary file first
        temp_file = file_path.with_suffix(f"{file_path.suffix}.tmp")
        
        try:
    pass
            with open(temp_file, 'w') as f:
    pass
                json.dump(data, f, indent=2, default=str)
            
            # Atomic move
            temp_file.replace(file_path)
            
        except Exception as e:
    pass
    pass
            # Clean up temp file
            if temp_file.exists():
    
        pass
    pass
                temp_file.unlink()
            
            raise ConfigurationError(
                f"Failed to write JSON file {file_path}: {str(e)}",
                suggestions=[
                    "Check file permissions",
                    "Verify JSON data is serializable",
                    "Ensure directory exists and is writable"
                ]
            )
    
    def safe_write_text(self, file_path: Path, content: str,
                       create_backup: bool = True) -> None:
    pass
        """Safely write text content with backup"""
        if create_backup and file_path.exists():
    
        pass
    pass
            self.create_backup(file_path)
        
        # Write to temporary file first
        temp_file = file_path.with_suffix(f"{file_path.suffix}.tmp")
        
        try:
    pass
            with open(temp_file, 'w') as f:
    pass
                f.write(content)
            
            # Atomic move
            temp_file.replace(file_path)
            
        except Exception as e:
    pass
    pass
            # Clean up temp file
            if temp_file.exists():
    
        pass
    pass
                temp_file.unlink()
            
            raise ConfigurationError(
                f"Failed to write text file {file_path}: {str(e)}",
                suggestions=[
                    "Check file permissions",
                    "Ensure directory exists and is writable"
                ]
            )
    
    def read_yaml(self, file_path: Path) -> Dict[str, Any]:
    pass
        """Read YAML file with error handling"""
        try:
    pass
            with open(file_path, 'r') as f:
    pass
                return yaml.safe_load(f) or {}
        except FileNotFoundError:
    pass
    pass
            raise CLIException(
                f"Configuration file not found: {file_path}",
                suggestions=[
                    f"Create the file with 'touch {file_path}'",
                    "Run 'genebot init-config' to create default configuration",
                    "Check if you are in the correct directory"
                ]
            )
        except yaml.YAMLError as e:
    
        pass
    pass
    pass
            raise ConfigurationError(
                f"Invalid YAML syntax in {file_path}: {str(e)}",
                suggestions=[
                    "Check YAML syntax with an online validator",
                    "Look for indentation or formatting issues",
                    "Restore from backup if available"
                ]
        except Exception as e:
    
        pass
    pass
    pass
            raise CLIException(
                suggestions=[
                    "Check file permissions",
                    "Verify file is not corrupted"
                ]
            )
    
    def read_json(self, file_path: Path) -> Dict[str, Any]:
    pass
        """Read JSON file with error handling"""
        try:
    pass
            with open(file_path, 'r') as f:
    pass
                return json.load(f)
        except FileNotFoundError:
    pass
    pass
            raise CLIException(
                f"Configuration file not found: {file_path}",
                suggestions=[
                    f"Create the file with 'touch {file_path}'",
                    "Check if you are in the correct directory"
                ]
            )
        except json.JSONDecodeError as e:
    
        pass
    pass
    pass
            raise ConfigurationError(
                f"Invalid JSON syntax in {file_path}: {str(e)}",
                suggestions=[
                    "Check JSON syntax with an online validator",
                    "Look for missing commas or brackets",
                    "Restore from backup if available"
                ]
        except Exception as e:
    
        pass
    pass
    pass
            raise CLIException(
                suggestions=[
                    "Check file permissions",
                    "Verify file is not corrupted"
                ]
            )
    
    def ensure_directory(self, dir_path: Path) -> None:
    pass
        """Ensure directory exists with proper permissions"""
        try:
    pass
            dir_path.mkdir(parents=True, exist_ok=True)
        except Exception as e:
    pass
    pass
            raise CLIException(
                f"Failed to create directory {dir_path}: {str(e)}",
                suggestions=[
                    "Check parent directory permissions",
                    "Verify disk space is available",
                    "Check if path conflicts with existing file"
                ]
            )
    
    def check_file_permissions(self, file_path: Path) -> Dict[str, bool]:
    pass
        """Check file permissions and return status"""
        if not file_path.exists():
    
        pass
    pass
            return {"exists": False, "readable": False, "writable": False}
        
        return {
            "exists": True,
            "readable": os.access(file_path, os.R_OK),
            "writable": os.access(file_path, os.W_OK)
        }
    
    def get_file_info(self, file_path: Path) -> Dict[str, Any]:
    pass
        """Get comprehensive file information"""
        if not file_path.exists():
    
        pass
    pass
            return {"exists": False}
        
        stat = file_path.stat()
        return {
            "exists": True,
            "size": stat.st_size,
            "modified": datetime.fromtimestamp(stat.st_mtime),
        }
    
    def list_backups(self, file_path: Optional[Path] = None) -> List[Dict[str, Any]]:
    pass
        """List available backups"""
        backups = []
        
        for backup_file in self.backup_dir.glob("*.backup"):
    pass
            # Parse backup filename to get original file and timestamp
            parts = backup_file.name.split('.')
            if len(parts) >= 3:
    
        pass
    pass
                original_name = '.'.join(parts[:-2])
                timestamp_str = parts[-2]
                
                # Skip if filtering by specific file
                if file_path and original_name != file_path.name:
    
        pass
    pass
                    continue
                
                try:
    pass
                    timestamp = datetime.strptime(timestamp_str, "%Y%m%d_%H%M%S")
                    backups.append({
                        "original_file": original_name,
                        "backup_file": backup_file,
                        "timestamp": timestamp,
                        "size": backup_file.stat().st_size
                    })
                except ValueError:
    pass
    pass
                    continue
        
        return sorted(backups, key=lambda x: x["timestamp"], reverse=True)