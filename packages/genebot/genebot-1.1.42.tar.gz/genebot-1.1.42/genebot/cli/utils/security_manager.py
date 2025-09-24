"""
Security Manager
================

Implements security enhancements and credential management for the CLI.
Provides secure credential validation, file permission checks, credential rotation,
security validation, and audit logging for sensitive operations.
"""

import os
import stat
import logging
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, asdict
from enum import Enum
import yaml
import re

from ..result import CommandResult, ResultStatus


class SecurityLevel(Enum):
    pass
    """Security levels for different operations"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class CredentialType(Enum):
    
        pass
    pass
    """Types of credentials managed by the system"""
    API_KEY = "api_key"
    SECRET_KEY = "secret_key"
    PASSWORD = "password"
    TOKEN = "token"
    CERTIFICATE = "certificate"
    PRIVATE_KEY = "private_key"


@dataclass
class SecurityAuditEntry:
    
        pass
    pass
    """Audit log entry for security-related operations"""
    timestamp: datetime
    operation: str
    user: str
    resource: str
    security_level: SecurityLevel
    success: bool
    details: Dict[str, Any]
    ip_address: Optional[str] = None
    session_id: Optional[str] = None


@dataclass
class CredentialInfo:
    pass
    """Information about a credential without exposing the actual value"""
    name: str
    credential_type: CredentialType
    masked_value: str
    last_used: Optional[datetime]
    expires_at: Optional[datetime]
    strength_score: int  # 0-100
    rotation_due: bool
    source_file: Optional[str]
    permissions_secure: bool


@dataclass
class FileSecurityInfo:
    pass
    """Security information about a file"""
    path: Path
    permissions: int
    owner_readable: bool
    owner_writable: bool
    group_readable: bool
    group_writable: bool
    other_readable: bool
    other_writable: bool
    is_secure: bool
    recommendations: List[str]


class SecurityManager:
    pass
    """
    Manages security enhancements and credential management for the CLI.
    
    Provides secure credential validation without exposing sensitive data,
    file permission checks, credential rotation guidance, and audit logging.
    """
    
    def __init__(self, workspace_path: Path, config_path: Optional[Path] = None):
    pass
        """
        Initialize the security manager.
        
        Args:
    pass
            workspace_path: Path to the workspace root
            config_path: Path to configuration directory (defaults to workspace/config)
        """
        self.workspace_path = workspace_path
        self.config_path = config_path or workspace_path / "config"
        self.logger = logging.getLogger(__name__)
        
        # Security configuration
        self.security_config = self._load_security_config()
        
        # Audit log file
        self.audit_log_file = self.workspace_path / "logs" / "security_audit.log"
        self.audit_log_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Sensitive file patterns
        self.sensitive_patterns = {
            r'\.env$': SecurityLevel.CRITICAL,
            r'\.env\..*': SecurityLevel.CRITICAL,
            r'.*\.key$': SecurityLevel.CRITICAL,
            r'.*\.pem$': SecurityLevel.CRITICAL,
            r'.*\.p12$': SecurityLevel.CRITICAL,
            r'.*\.pfx$': SecurityLevel.CRITICAL,
            r'accounts\.yaml$': SecurityLevel.HIGH,
            r'.*config.*\.yaml$': SecurityLevel.MEDIUM,
            r'.*\.log$': SecurityLevel.LOW
        }
        
        # Credential patterns for detection
        self.credential_patterns = {
            CredentialType.API_KEY: [
                r'api[_-]?key[_-]?=?["\']?([a-zA-Z0-9]{20,})["\']?',
                r'apikey[_-]?=?["\']?([a-zA-Z0-9]{20,})["\']?'
            ],
            CredentialType.SECRET_KEY: [
                r'secret[_-]?key[_-]?=?["\']?([a-zA-Z0-9+/]{20,})["\']?',
                r'secret[_-]?=?["\']?([a-zA-Z0-9+/]{20,})["\']?'
            ],
            CredentialType.PASSWORD: [
                r'password[_-]?=?["\']?([^\s"\']{8,})["\']?',
                r'passwd[_-]?=?["\']?([^\s"\']{8,})["\']?'
            ],
            CredentialType.TOKEN: [
                r'token[_-]?=?["\']?([a-zA-Z0-9._-]{20,})["\']?',
                r'bearer[_-]?=?["\']?([a-zA-Z0-9._-]{20,})["\']?'
            ]
        }
    
    def _load_security_config(self) -> Dict[str, Any]:
    pass
        """Load security configuration with defaults"""
        security_config_file = self.config_path / "security_config.yaml"
        
        default_config = {
            'credential_rotation_days': 90,
            'password_min_length': 12,
            'password_require_special': True,
            'password_require_numbers': True,
            'password_require_uppercase': True,
            'file_permission_checks': True,
            'audit_retention_days': 365,
            'secure_file_permissions': 0o600,
            'secure_dir_permissions': 0o700,
            'allowed_credential_sources': ['.env', 'accounts.yaml'],
            'credential_strength_requirements': {
                'api_key': {'min_length': 20, 'entropy_bits': 128},
                'secret_key': {'min_length': 32, 'entropy_bits': 256},
                'password': {'min_length': 12, 'entropy_bits': 60}
            }
        }
        
        if security_config_file.exists():
    
        pass
    pass
            try:
    pass
                with open(security_config_file, 'r') as f:
    pass
                    user_config = yaml.safe_load(f) or {}
                default_config.update(user_config)
            except Exception as e:
    pass
    pass
                self.logger.warning(f"Failed to load security config: {e}")
        
        return default_config
    
    def _mask_credential(self, value: str, credential_type: CredentialType) -> str:
    pass
        """
        Mask a credential value for safe display.
        
        Args:
    pass
            value: The credential value to mask
            credential_type: Type of credential
            
        Returns:
    pass
            Masked version of the credential
        """
        if not value:
    
        pass
    pass
            return ""
        
        if len(value) <= 8:
    
        pass
    pass
            return "*" * len(value)
        
        # Show first 4 and last 4 characters for longer credentials
        if credential_type in [CredentialType.API_KEY, CredentialType.SECRET_KEY]:
    
        pass
    pass
            return f"{value[:4]}...{value[-4:]}"
        elif credential_type == CredentialType.TOKEN:
    
        pass
    pass
            return f"{value[:6]}...{value[-4:]}"
        else:
    pass
            return "*" * min(len(value), 12)
    
    def _calculate_credential_strength(self, value: str, credential_type: CredentialType) -> int:
    pass
        """
        Calculate the strength score of a credential (0-100).
        
        Args:
    pass
            value: The credential value
            credential_type: Type of credential
            
        Returns:
    pass
            Strength score from 0 to 100
        """
        if not value:
    
        pass
    pass
            return 0
        
        score = 0
        
        # Length score (up to 30 points)
        length_score = min(30, len(value) * 2)
        score += length_score
        
        # Character diversity (up to 40 points)
        has_lower = bool(re.search(r'[a-z]', value))
        has_upper = bool(re.search(r'[A-Z]', value))
        has_digits = bool(re.search(r'[0-9]', value))
        has_special = bool(re.search(r'[^a-zA-Z0-9]', value))
        
        diversity_score = sum([has_lower, has_upper, has_digits, has_special]) * 10
        score += diversity_score
        
        # Entropy estimation (up to 30 points)
        unique_chars = len(set(value))
        entropy_score = min(30, unique_chars * 2)
        score += entropy_score
        
        # Check against requirements
        requirements = self.security_config.get('credential_strength_requirements', {})
        type_requirements = requirements.get(credential_type.value, {})
        
        min_length = type_requirements.get('min_length', 8)
        if len(value) < min_length:
    
        pass
    pass
            score = max(0, score - 20)  # Penalty for not meeting minimum length
        
        return min(100, score)
    
    def _is_credential_rotation_due(self, last_used: Optional[datetime]) -> bool:
    pass
        """
        Check if credential rotation is due based on last usage.
        
        Args:
    
        pass
    pass
            last_used: When the credential was last used
            
        Returns:
    pass
            True if rotation is due
        """
        if not last_used:
    
        pass
    pass
            return True  # No usage history, recommend rotation
        
        rotation_days = self.security_config.get('credential_rotation_days', 90)
        rotation_threshold = datetime.now(timezone.utc) - timedelta(days=rotation_days)
        
        return last_used < rotation_threshold
    
    def validate_credentials_secure(self, env_file: Optional[Path] = None) -> CommandResult:
    pass
        """
        Validate credentials without exposing sensitive data.
        
        Args:
    pass
            env_file: Path to environment file (defaults to .env)
            
        Returns:
    pass
            CommandResult with validation status and recommendations
        """
        try:
    pass
            env_file = env_file or self.workspace_path / ".env"
            
            if not env_file.exists():
    
        pass
    pass
                return CommandResult.warning(
                    message="No .env file found",
                    suggestions=[
                        "Create .env file with your API credentials",
                        "Use .env.example as a template",
                        "Ensure .env file has proper permissions (600)"
                    ]
                )
            
            # Check file permissions first
            file_security = self.check_file_permissions(env_file)
            if not file_security.is_secure:
    
        pass
    pass
                return CommandResult.error(
                    message="Environment file has insecure permissions",
                    suggestions=file_security.recommendations
                )
            
            # Parse credentials without logging values
            credentials = []
            issues = []
            
            try:
    pass
                with open(env_file, 'r') as f:
    pass
                    content = f.read()
                
                # Find credentials using patterns
                for line_num, line in enumerate(content.split('\n'), 1):
    pass
                    line = line.strip()
                    if not line or line.startswith('#'):
    
        pass
    pass
                        continue
                    
                    if '=' in line:
    
        pass
    pass
                        key, value = line.split('=', 1)
                        key = key.strip()
                        value = value.strip().strip('"\'')
                        
                        if value:  # Only process non-empty values
                            # Determine credential type
                            credential_type = self._detect_credential_type(key, value)
                            
                            if credential_type:
    
        pass
    pass
                                strength = self._calculate_credential_strength(value, credential_type)
                                
                                credential_info = CredentialInfo(
                                    name=key,
                                    credential_type=credential_type,
                                    masked_value=self._mask_credential(value, credential_type),
                                    last_used=None,  # Would need to track this separately
                                    expires_at=None,  # Would need to be configured
                                    strength_score=strength,
                                    rotation_due=self._is_credential_rotation_due(None),
                                    source_file=str(env_file),
                                    permissions_secure=file_security.is_secure
                                )
                                
                                credentials.append(credential_info)
                                
                                # Check for issues
                                if strength < 60:
    
        pass
    pass
                                    issues.append(f"Weak credential '{key}' (strength: {strength}/100)")
                                
                                if len(value) < 8:
    
        pass
    pass
                                    issues.append(f"Credential '{key}' is too short")
                                
                                # Check for common weak patterns
                                if value.lower() in ['password', '123456', 'secret', 'test']:
    
        pass
    pass
                                    issues.append(f"Credential '{key}' uses a common weak value")
            
            except Exception as e:
    pass
    pass
                return CommandResult.error(
                    message=f"Failed to parse environment file: {str(e)}",
                    suggestions=[
                        "Check .env file syntax",
                        "Ensure file is readable",
                        "Verify file encoding (should be UTF-8)"
                    ]
                )
            
            # Log audit entry (without credential values)
            self._log_audit_entry(
                operation="credential_validation",
                resource=str(env_file),
                security_level=SecurityLevel.HIGH,
                success=len(issues) == 0,
                details={
                    'credentials_found': len(credentials),
                    'issues_found': len(issues),
                    'file_secure': file_security.is_secure
                }
            )
            
            # Prepare result
            if issues:
    
        pass
    pass
                return CommandResult.warning(
                    message=f"Found {len(issues)} credential security issue(s)",
                    suggestions=[
                        "Review and strengthen weak credentials",
                        "Use credential rotation procedures",
                        "Consider using environment-specific credential management",
                        "Run 'genebot security audit' for detailed analysis"
                    ],
                    data={
                        'credentials': [asdict(c) for c in credentials],
                        'issues': issues,
                        'file_security': asdict(file_security)
                    }
                )
            else:
    pass
                return CommandResult.success(
                    message=f"All {len(credentials)} credential(s) passed security validation",
                    data={
                        'credentials': [asdict(c) for c in credentials],
                        'file_security': asdict(file_security)
                    }
                )
        
        except Exception as e:
    pass
    pass
            self.logger.error(f"Credential validation failed: {e}")
            return CommandResult.error(
                message=f"Credential validation failed: {str(e)}",
                suggestions=[
                    "Check file permissions and accessibility",
                    "Verify .env file format",
                    "Run with --verbose for more details"
                ]
            )
    
    def _detect_credential_type(self, key: str, value: str) -> Optional[CredentialType]:
    pass
        """
        Detect the type of credential based on key name and value pattern.
        
        Args:
    pass
            key: The credential key/name
            value: The credential value
            
        Returns:
    pass
            Detected credential type or None
        """
        key_lower = key.lower()
        
        # Check key patterns
        if 'api' in key_lower and 'key' in key_lower:
    
        pass
    pass
            return CredentialType.API_KEY
        elif 'secret' in key_lower:
    
        pass
    pass
            return CredentialType.SECRET_KEY
        elif 'password' in key_lower or 'passwd' in key_lower:
    
        pass
    pass
            return CredentialType.PASSWORD
        elif 'token' in key_lower:
    
        pass
    pass
            return CredentialType.TOKEN
        elif 'cert' in key_lower or 'certificate' in key_lower:
    
        pass
    pass
            return CredentialType.CERTIFICATE
        elif 'private' in key_lower and 'key' in key_lower:
    
        pass
    pass
            return CredentialType.PRIVATE_KEY
        
        # Check value patterns
        if len(value) >= 20 and re.match(r'^[a-zA-Z0-9]{20,}$', value):
    
        pass
    pass
            return CredentialType.API_KEY
        elif len(value) >= 32 and re.match(r'^[a-zA-Z0-9+/=]{32,}$', value):
    
        pass
    pass
            return CredentialType.SECRET_KEY
        elif value.startswith('-----BEGIN'):
    
        pass
    pass
            if 'PRIVATE KEY' in value:
    
        pass
    pass
                return CredentialType.PRIVATE_KEY
            elif 'CERTIFICATE' in value:
    
        pass
    pass
                return CredentialType.CERTIFICATE
        
        return None
    
    def check_file_permissions(self, file_path: Path) -> FileSecurityInfo:
    pass
        """
        Check file permissions and security status.
        
        Args:
    pass
            file_path: Path to the file to check
            
        Returns:
    pass
            FileSecurityInfo with permission details and recommendations
        """
        try:
    pass
            if not file_path.exists():
    
        pass
    pass
                return FileSecurityInfo(
                    path=file_path,
                    permissions=0,
                    owner_readable=False,
                    owner_writable=False,
                    group_readable=False,
                    group_writable=False,
                    other_readable=False,
                    other_writable=False,
                    is_secure=False,
                    recommendations=["File does not exist"]
                )
            
            # Get file permissions
            file_stat = file_path.stat()
            permissions = file_stat.st_mode
            
            # Parse permission bits
            owner_readable = bool(permissions & stat.S_IRUSR)
            owner_writable = bool(permissions & stat.S_IWUSR)
            group_readable = bool(permissions & stat.S_IRGRP)
            group_writable = bool(permissions & stat.S_IWGRP)
            other_readable = bool(permissions & stat.S_IROTH)
            other_writable = bool(permissions & stat.S_IWOTH)
            
            # Determine security level based on file type
            security_level = self._get_file_security_level(file_path)
            
            # Check if permissions are secure
            is_secure = True
            recommendations = []
            
            if security_level in [SecurityLevel.HIGH, SecurityLevel.CRITICAL]:
    
        pass
    pass
                # Sensitive files should not be readable by group or others
                if group_readable or other_readable:
    
        pass
    pass
                    is_secure = False
                    recommendations.append(f"Remove group/other read permissions: chmod 600 {file_path}")
                
                if group_writable or other_writable:
    
        pass
    pass
                    is_secure = False
                    recommendations.append(f"Remove group/other write permissions: chmod 600 {file_path}")
            
            elif security_level == SecurityLevel.MEDIUM:
    
        pass
    pass
                # Medium security files should not be writable by others
                if other_writable:
    
        pass
    pass
                    is_secure = False
                    recommendations.append(f"Remove other write permissions: chmod o-w {file_path}")
            
            # Check for overly permissive permissions
            if permissions & 0o777 == 0o777:
    
        pass
    pass
                is_secure = False
                recommendations.append(f"File has dangerous permissions (777): chmod 644 {file_path}")
            
            # Add general recommendations if not secure
            if not is_secure and not recommendations:
    
        pass
    pass
                if security_level == SecurityLevel.CRITICAL:
    
        pass
    pass
                    recommendations.append(f"Set secure permissions: chmod 600 {file_path}")
                else:
    pass
                    recommendations.append(f"Review and restrict permissions: chmod 644 {file_path}")
            
            return FileSecurityInfo(
                path=file_path,
                permissions=permissions & 0o777,  # Only permission bits
                owner_readable=owner_readable,
                owner_writable=owner_writable,
                group_readable=group_readable,
                group_writable=group_writable,
                other_readable=other_readable,
                other_writable=other_writable,
                is_secure=is_secure,
                recommendations=recommendations
            )
        
        except Exception as e:
    pass
    pass
            self.logger.error(f"Failed to check file permissions for {file_path}: {e}")
            return FileSecurityInfo(
                path=file_path,
                permissions=0,
                owner_readable=False,
                owner_writable=False,
                group_readable=False,
                group_writable=False,
                other_readable=False,
                other_writable=False,
                is_secure=False,
                recommendations=[f"Error checking permissions: {str(e)}"]
            )
    
    def _get_file_security_level(self, file_path: Path) -> SecurityLevel:
    pass
        """
        Determine the security level required for a file based on its name/path.
        
        Args:
    pass
            file_path: Path to the file
            
        Returns:
    pass
            Required security level
        """
        file_name = file_path.name
        
        for pattern, level in self.sensitive_patterns.items():
    pass
            if re.search(pattern, file_name, re.IGNORECASE):
    
        pass
    pass
                return level
        
        return SecurityLevel.LOW
    
    def audit_workspace_security(self) -> CommandResult:
    pass
        """
        Perform a comprehensive security audit of the workspace.
        
        Returns:
    pass
            CommandResult with audit findings and recommendations
        """
        try:
    pass
            audit_results = {
                'files_checked': 0,
                'secure_files': 0,
                'insecure_files': 0,
                'critical_issues': [],
                'high_issues': [],
                'medium_issues': [],
                'low_issues': [],
                'recommendations': []
            }
            
            # Check important files and directories
            important_paths = [
                self.workspace_path / "config",
                self.workspace_path / "backups"
            ]
            
            # Add any .key, .pem, .p12 files
            for pattern in ['*.key', '*.pem', '*.p12', '*.pfx']:
    pass
                important_paths.extend(self.workspace_path.rglob(pattern))
            
            for path in important_paths:
    pass
                if path.exists():
    
        pass
    pass
                    audit_results['files_checked'] += 1
                    
                    if path.is_file():
    
        pass
    pass
                        file_security = self.check_file_permissions(path)
                        security_level = self._get_file_security_level(path)
                        
                        if file_security.is_secure:
    
        pass
    pass
                            audit_results['secure_files'] += 1
                        else:
    pass
                            audit_results['insecure_files'] += 1
                            
                            issue = {
                                'file': str(path),
                                'security_level': security_level.value,
                                'permissions': oct(file_security.permissions),
                                'recommendations': file_security.recommendations
                            }
                            
                            if security_level == SecurityLevel.CRITICAL:
    
        pass
    pass
                                audit_results['critical_issues'].append(issue)
                            elif security_level == SecurityLevel.HIGH:
    
        pass
    pass
                                audit_results['high_issues'].append(issue)
                            elif security_level == SecurityLevel.MEDIUM:
    
        pass
    pass
                                audit_results['medium_issues'].append(issue)
                            else:
    pass
                                audit_results['low_issues'].append(issue)
                    
                    elif path.is_dir():
    
        pass
    pass
                        # Check directory permissions
                        dir_stat = path.stat()
                        dir_permissions = dir_stat.st_mode & 0o777
                        
                        # Directories should generally not be world-writable
                        if dir_permissions & 0o002:  # World-writable
                            issue = {
                                'directory': str(path),
                                'permissions': oct(dir_permissions),
                                'issue': 'World-writable directory',
                                'recommendation': f'chmod o-w {path}'
                            }
                            audit_results['medium_issues'].append(issue)
            
            # Check for credential files in version control
            gitignore_path = self.workspace_path / ".gitignore"
            if gitignore_path.exists():
    
        pass
    pass
                gitignore_content = gitignore_path.read_text()
                sensitive_files = ['.env', '*.key', '*.pem', '*.p12', '*.pfx']
                
                for sensitive_file in sensitive_files:
    pass
                    if sensitive_file not in gitignore_content:
    
        pass
    pass
                        audit_results['medium_issues'].append({
                            'issue': f'Sensitive file pattern "{sensitive_file}" not in .gitignore',
                            'recommendation': f'Add "{sensitive_file}" to .gitignore'
                        })
            
            # Generate overall recommendations
            total_issues = (len(audit_results['critical_issues']) + 
                          len(audit_results['high_issues']) + 
                          len(audit_results['medium_issues']) + 
                          len(audit_results['low_issues']))
            
            if audit_results['critical_issues']:
    
        pass
    pass
                audit_results['recommendations'].append(
                    "URGENT: Fix critical security issues immediately"
                )
            
            if audit_results['high_issues']:
    
        pass
    pass
                audit_results['recommendations'].append(
                    "Fix high-priority security issues as soon as possible"
                )
            
            if total_issues == 0:
    
        pass
    pass
                audit_results['recommendations'].append(
                    "Security audit passed - no issues found"
                )
            else:
    pass
                audit_results['recommendations'].extend([
                    "Review and fix security issues listed above",
                    "Run 'genebot security fix-permissions' to auto-fix file permissions",
                    "Regularly audit security with 'genebot security audit'"
                ])
            
            # Log audit entry
            self._log_audit_entry(
                operation="security_audit",
                resource="workspace",
                security_level=SecurityLevel.HIGH,
                success=total_issues == 0,
                details={
                    'files_checked': audit_results['files_checked'],
                    'total_issues': total_issues,
                    'critical_issues': len(audit_results['critical_issues']),
                    'high_issues': len(audit_results['high_issues'])
                }
            )
            
            # Determine result status
            if audit_results['critical_issues']:
    
        pass
    pass
                status = ResultStatus.ERROR
                message = f"Security audit failed: {len(audit_results['critical_issues'])} critical issue(s) found"
            elif audit_results['high_issues']:
    
        pass
    pass
                status = ResultStatus.WARNING
                message = f"Security audit warning: {len(audit_results['high_issues'])} high-priority issue(s) found"
            elif total_issues > 0:
    
        pass
    pass
                status = ResultStatus.WARNING
                message = f"Security audit completed: {total_issues} issue(s) found"
            else:
    pass
                status = ResultStatus.SUCCESS
                message = "Security audit passed: no issues found"
            
            if status == ResultStatus.ERROR:
    
        pass
    pass
                result = CommandResult.error(
                    message=message,
                    suggestions=audit_results['recommendations']
                )
                result.data = audit_results  # Add data manually since error() doesn't accept it
                return result
            elif status == ResultStatus.WARNING:
    
        pass
    pass
                return CommandResult.warning(
                    message=message,
                    data=audit_results,
                    suggestions=audit_results['recommendations']
                )
            else:
    pass
                return CommandResult.success(
                    message=message,
                    data=audit_results,
                    suggestions=audit_results['recommendations']
                )
        
        except Exception as e:
    pass
    pass
            self.logger.error(f"Security audit failed: {e}")
            return CommandResult.error(
                message=f"Security audit failed: {str(e)}",
                suggestions=[
                    "Check file permissions and accessibility",
                    "Ensure workspace directory is readable",
                    "Run with --verbose for more details"
                ]
            )
    
    def fix_file_permissions(self, dry_run: bool = False) -> CommandResult:
    pass
        """
        Automatically fix insecure file permissions.
        
        Args:
    pass
            dry_run: If True, only show what would be fixed without making changes
            
        Returns:
    pass
            CommandResult with fix results
        """
        try:
    pass
            fixes_applied = []
            fixes_failed = []
            
            # Get security audit results
            audit_result = self.audit_workspace_security()
            if audit_result.status == ResultStatus.ERROR and not audit_result.data:
    
        pass
    pass
                return audit_result
            
            audit_data = audit_result.data
            
            # Process critical and high issues
            for issue_list, level in [(audit_data['critical_issues'], 'critical'),
                                    (audit_data['high_issues'], 'high')]:
    pass
                for issue in issue_list:
    pass
                    if 'file' in issue:
    
        pass
    pass
                        file_path = Path(issue['file'])
                        recommendations = issue.get('recommendations', [])
                        
                        for recommendation in recommendations:
    pass
                            if recommendation.startswith('chmod'):
    
        pass
    pass
                                # Extract chmod command
                                parts = recommendation.split()
                                if len(parts) >= 3:
    
        pass
    pass
                                    mode_str = parts[1]
                                    target_path = parts[2]
                                    
                                    try:
    pass
                                        # Convert mode string to octal
                                        if mode_str.isdigit():
    
        pass
    pass
                                            mode = int(mode_str, 8)
                                        else:
    pass
                                            # Handle symbolic modes (basic support)
                                            if mode_str == '600':
    
        pass
    pass
                                                mode = 0o600
                                            elif mode_str == '644':
    
        pass
    pass
                                                mode = 0o644
                                            elif mode_str == '700':
    
        pass
    pass
                                                mode = 0o700
                                            else:
    pass
                                                continue
                                        
                                        if not dry_run:
    
        pass
    pass
                                            file_path.chmod(mode)
                                        
                                        fixes_applied.append({
                                            'file': str(file_path),
                                            'old_permissions': issue.get('permissions', 'unknown'),
                                            'new_permissions': oct(mode),
                                            'level': level,
                                            'dry_run': dry_run
                                        })
                                    
                                    except Exception as e:
    pass
    pass
                                        fixes_failed.append({
                                            'file': str(file_path),
                                            'error': str(e),
                                            'recommendation': recommendation
                                        })
            
            # Log audit entry
            self._log_audit_entry(
                operation="fix_permissions",
                resource="workspace",
                security_level=SecurityLevel.HIGH,
                success=len(fixes_failed) == 0,
                details={
                    'fixes_applied': len(fixes_applied),
                    'fixes_failed': len(fixes_failed),
                    'dry_run': dry_run
                }
            )
            
            # Prepare result
            if fixes_failed:
    
        pass
    pass
                return CommandResult.warning(
                    message=f"Fixed {len(fixes_applied)} permission(s), {len(fixes_failed)} failed",
                    suggestions=[
                        "Review failed fixes and apply manually",
                        "Check file ownership and access rights",
                        "Run as appropriate user if permission denied"
                    ],
                    data={
                        'fixes_applied': fixes_applied,
                        'fixes_failed': fixes_failed,
                        'dry_run': dry_run
                    }
                )
            elif fixes_applied:
    
        pass
    pass
                action = "Would fix" if dry_run else "Fixed"
                return CommandResult.success(
                    message=f"{action} {len(fixes_applied)} file permission(s)",
                    data={
                        'fixes_applied': fixes_applied,
                        'dry_run': dry_run
                    }
                )
            else:
    pass
                return CommandResult.success(
                    message="No permission fixes needed",
                    data={'dry_run': dry_run}
                )
        
        except Exception as e:
    pass
    pass
            self.logger.error(f"Permission fix failed: {e}")
            return CommandResult.error(
                message=f"Permission fix failed: {str(e)}",
                suggestions=[
                    "Check file permissions and ownership",
                    "Ensure you have appropriate access rights",
                    "Run with --verbose for more details"
                ]
            )
    
    def generate_credential_rotation_guide(self) -> CommandResult:
    pass
        """
        Generate guidance for credential rotation procedures.
        
        Returns:
    pass
            CommandResult with rotation guidance and procedures
        """
        try:
    pass
            # Analyze current credentials
            credential_result = self.validate_credentials_secure()
            
            rotation_guide = {
                'overview': {
                    'importance': 'Regular credential rotation reduces security risks from compromised keys',
                    'best_practices': [
                        'Keep secure backup of working credentials during transition',
                        'Document rotation dates and procedures'
                    ]
                },
                'procedures': {},
                'current_status': {},
                'next_actions': []
            }
            
            # Add credential-specific procedures
            if credential_result.data and 'credentials' in credential_result.data:
    
        pass
    pass
                credentials = credential_result.data['credentials']
                
                for cred in credentials:
    pass
                    cred_name = cred['name']
                    cred_type = cred['credential_type']
                    
                    # Determine rotation procedure based on credential type
                    if cred_type == 'api_key':
    
        pass
    pass
                        procedure = {
                            'steps': [
                                '1. Log into exchange/broker dashboard',
                                '2. Navigate to API management section',
                                '3. Generate new API key with same permissions',
                                '4. Update .env file with new key',
                                '5. Test connectivity with new key',
                                '6. Delete old API key from dashboard',
                                '7. Verify all systems are using new key'
                            'rollback': 'Keep old key active until new key is confirmed working'
                        }
                    elif cred_type == 'secret_key':
    
        pass
    pass
                        procedure = {
                            'steps': [
                                '1. Generate new secret key in provider dashboard',
                                '2. Update .env file with new secret',
                                '3. Restart any running bot processes',
                                '4. Test all API operations',
                                '5. Revoke old secret key',
                                '6. Update backup configurations'
                            ],
                            'testing': 'Run full validation suite to ensure all operations work',
                            'rollback': 'Maintain old secret until all systems confirmed working'
                        }
                    else:
    pass
                        procedure = {
                            'steps': [
                                '1. Generate new credential in appropriate system',
                                '2. Update configuration files',
                                '3. Test connectivity and functionality',
                                '4. Remove old credential',
                                '5. Update documentation'
                            ],
                            'testing': 'Test all affected functionality',
                            'rollback': 'Keep old credential available during transition'
                        }
                    
                    rotation_guide['procedures'][cred_name] = procedure
                    
                    # Add current status
                    rotation_guide['current_status'][cred_name] = {
                        'type': cred_type,
                        'strength': cred['strength_score'],
                        'rotation_due': cred['rotation_due'],
                        'masked_value': cred['masked_value']
                    }
                    
                    # Add to next actions if rotation is due
                    if cred['rotation_due'] or cred['strength_score'] < 60:
    
        pass
    pass
                        priority = 'HIGH' if cred['strength_score'] < 40 else 'MEDIUM'
                        rotation_guide['next_actions'].append({
                            'credential': cred_name,
                            'priority': priority,
                            'reason': 'Rotation overdue' if cred['rotation_due'] else 'Weak credential',
                            'action': f'Rotate {cred_name} using procedure above'
                        })
            
            # Add general next actions
            if not rotation_guide['next_actions']:
    
        pass
    pass
                rotation_guide['next_actions'].append({
                    'credential': 'all',
                    'priority': 'LOW',
                    'reason': 'Maintenance',
                    'action': 'Schedule next rotation check in 30 days'
                })
            
            # Add automation suggestions
            rotation_guide['automation'] = {
                'monitoring': 'Set up calendar reminders for rotation schedules',
                'testing': 'Create automated tests for credential validation',
                'documentation': 'Maintain rotation log with dates and procedures used',
                'backup': 'Implement secure credential backup and recovery procedures'
            }
            
            # Log audit entry
            self._log_audit_entry(
                operation="rotation_guide_generated",
                resource="credentials",
                security_level=SecurityLevel.MEDIUM,
                success=True,
                details={
                    'credentials_analyzed': len(rotation_guide['current_status']),
                    'rotations_due': len([a for a in rotation_guide['next_actions'] if a['priority'] in ['HIGH', 'MEDIUM']])
                }
            )
            
            return CommandResult.success(
                message="Credential rotation guide generated",
                suggestions=[
                    "Review rotation procedures for each credential type",
                    "Prioritize high-priority rotations",
                    "Set up regular rotation schedule",
                    "Test procedures in development environment first"
                ],
                data=rotation_guide
            )
        
        except Exception as e:
    
        pass
    pass
    pass
            self.logger.error(f"Failed to generate rotation guide: {e}")
            return CommandResult.error(
                message=f"Failed to generate rotation guide: {str(e)}",
                suggestions=[
                    "Check credential validation is working",
                    "Ensure configuration files are accessible",
                    "Run with --verbose for more details"
                ]
            )
    
    def _log_audit_entry(self, operation: str, resource: str, security_level: SecurityLevel,
                        success: bool, details: Dict[str, Any], 
                        user: Optional[str] = None, ip_address: Optional[str] = None) -> None:
    pass
        """
        Log a security audit entry.
        
        Args:
    pass
            operation: The operation being audited
            resource: The resource being accessed
            security_level: Security level of the operation
            success: Whether the operation was successful
            details: Additional details about the operation
            user: User performing the operation (defaults to current user)
            ip_address: IP address of the user (optional)
        """
        try:
    pass
            # Get current user if not provided
            if user is None:
    
        pass
    pass
                user = os.getenv('USER', os.getenv('USERNAME', 'unknown'))
            
            # Create audit entry
            audit_entry = SecurityAuditEntry(
                timestamp=datetime.now(timezone.utc),
                operation=operation,
                user=user,
                resource=resource,
                security_level=security_level,
                success=success,
                details=details,
                ip_address=ip_address,
                session_id=None  # Could be implemented for session tracking
            )
            
            # Format log entry
            log_line = json.dumps({
                'timestamp': audit_entry.timestamp.isoformat(),
                'operation': audit_entry.operation,
                'user': audit_entry.user,
                'resource': audit_entry.resource,
                'security_level': audit_entry.security_level.value,
                'success': audit_entry.success,
                'details': audit_entry.details,
                'ip_address': audit_entry.ip_address,
                'session_id': audit_entry.session_id
            }, separators=(',', ':'))
            
            # Write to audit log
            with open(self.audit_log_file, 'a') as f:
    pass
                f.write(log_line + '\n')
            
            # Also log to application logger for immediate visibility
            log_level = logging.INFO if success else logging.WARNING
            self.logger.log(log_level, f"Security audit: {operation} on {resource} - {'SUCCESS' if success else 'FAILED'}")
        
        except Exception as e:
    
        pass
    pass
    pass
            # Don't fail the operation if audit logging fails, but log the error
            self.logger.error(f"Failed to write security audit log: {e}")
    
    def get_audit_log(self, limit: int = 100, operation_filter: Optional[str] = None,
                     user_filter: Optional[str] = None, days_back: int = 30) -> CommandResult:
    pass
        """
        Retrieve security audit log entries.
        
        Args:
    pass
            limit: Maximum number of entries to return
            operation_filter: Filter by operation type
            user_filter: Filter by user
            days_back: Number of days to look back
            
        Returns:
    pass
            CommandResult with audit log entries
        """
        try:
    pass
            if not self.audit_log_file.exists():
    
        pass
    pass
                return CommandResult.success(
                    message="No audit log found",
                    data={'entries': [], 'total': 0}
                )
            
            # Calculate cutoff date
            cutoff_date = datetime.now(timezone.utc) - timedelta(days=days_back)
            
            entries = []
            total_entries = 0
            
            # Read log file (most recent first)
            with open(self.audit_log_file, 'r') as f:
    pass
                lines = f.readlines()
            
            # Process lines in reverse order (most recent first)
            for line in reversed(lines):
    pass
                line = line.strip()
                if not line:
    
        pass
    pass
                    continue
                
                try:
    pass
                    entry_data = json.loads(line)
                    total_entries += 1
                    
                    # Parse timestamp
                    entry_timestamp = datetime.fromisoformat(entry_data['timestamp'].replace('Z', '+00:00'))
                    
                    # Apply date filter
                    if entry_timestamp < cutoff_date:
    
        pass
    pass
                        continue
                    
                    # Apply operation filter
                    if operation_filter and operation_filter not in entry_data.get('operation', ''):
    
        pass
    pass
                        continue
                    
                    # Apply user filter
                    if user_filter and user_filter != entry_data.get('user', ''):
    
        pass
    pass
                        continue
                    
                    entries.append(entry_data)
                    
                    # Apply limit
                    if len(entries) >= limit:
    
        pass
    pass
                        break
                
                except json.JSONDecodeError:
    pass
    pass
                    # Skip malformed entries
                    continue
            
            return CommandResult.success(
                message=f"Retrieved {len(entries)} audit log entries",
                data={
                    'entries': entries,
                    'total': len(entries),
                    'total_in_file': total_entries,
                    'filters': {
                        'operation': operation_filter,
                        'user': user_filter,
                        'days_back': days_back,
                        'limit': limit
                    }
                }
            )
        
        except Exception as e:
    pass
    pass
            self.logger.error(f"Failed to retrieve audit log: {e}")
            return CommandResult.error(
                message=f"Failed to retrieve audit log: {str(e)}",
                suggestions=[
                    "Check audit log file permissions",
                    "Verify log file is not corrupted",
                    "Run with --verbose for more details"
                ]
            )