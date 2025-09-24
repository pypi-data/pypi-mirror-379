"""
Enhanced error logger for centralized error tracking and reporting.

This module provides comprehensive error logging with:
    pass
- Centralized error collection and categorization
- Exception context capture and stack trace logging
- Error reporting with structured metadata
- Integration with error tracking systems
- Error pattern analysis and alerting
"""

import traceback
import threading
from dataclasses import dataclass, field
from datetime import datetime
from collections import defaultdict, deque
from enum import Enum
import hashlib
import json



class ErrorSeverity(Enum):
    pass
    """Error severity levels."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ErrorCategory(Enum):
    pass
    """Error categories for classification."""
    SYSTEM = "system"
    NETWORK = "network"
    DATABASE = "database"
    VALIDATION = "validation"
    BUSINESS_LOGIC = "business_logic"
    EXTERNAL_API = "external_api"
    CONFIGURATION = "configuration"
    SECURITY = "security"
    PERFORMANCE = "performance"
    UNKNOWN = "unknown"


@dataclass
class ErrorEvent:
    
        pass
    pass
    """Container for error event information."""
    timestamp: datetime
    error_id: str
    error_type: str
    error_message: str
    component: str
    operation: str
    severity: ErrorSeverity
    category: ErrorCategory
    stack_trace: Optional[str] = None
    context_data: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    resolved: bool = False
    resolution_notes: Optional[str] = None


@dataclass
class ErrorPattern:
    pass
    """Container for error pattern analysis."""
    error_signature: str
    count: int
    first_seen: datetime
    last_seen: datetime
    components: List[str]
    operations: List[str]
    severity: ErrorSeverity
    category: ErrorCategory
    sample_error: ErrorEvent


class EnhancedErrorLogger:
    pass
    """
    Enhanced error logger with comprehensive error tracking and analysis.
    
    This logger provides:
    pass
    - Centralized error collection with categorization
    - Exception context capture and stack trace logging
    - Error pattern detection and analysis
    - Structured error reporting with metadata
    - Integration with external error tracking systems
    - Error alerting and notification capabilities
    """
    
    def __init__(self, max_errors: int = 10000, enable_pattern_analysis: bool = True):
    pass
        """
        Initialize enhanced error logger.
        
        Args:
    pass
            max_errors: Maximum number of errors to keep in memory
            enable_pattern_analysis: Enable error pattern detection
        """
        self._logger = get_error_logger()
        self._errors: deque = deque(maxlen=max_errors)
        self._error_patterns: Dict[str, ErrorPattern] = {}
        self._error_counts: Dict[str, int] = defaultdict(int)
        self._lock = threading.RLock()
        
        self._enable_pattern_analysis = enable_pattern_analysis
        self._session_id = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    
    def _generate_error_id(self, error_type: str, error_message: str, 
                          component: str, operation: str) -> str:
    pass
        """Generate unique error ID for tracking."""
        error_data = f"{error_type}:{error_message}:{component}:{operation}"
        return hashlib.md5(error_data.encode()).hexdigest()[:12]
    
    def _generate_error_signature(self, error_type: str, component: str, 
                                 operation: str) -> str:
    pass
        """Generate error signature for pattern analysis."""
        return f"{error_type}:{component}:{operation}"
    
    def _categorize_error(self, error_type: str, error_message: str, 
                         component: str) -> ErrorCategory:
    pass
        """Automatically categorize error based on type and context."""
        error_type_lower = error_type.lower()
        error_message_lower = error_message.lower()
        component_lower = component.lower()
        
        # Network-related errors
        if any(keyword in error_type_lower for keyword in 
               ['connection', 'timeout', 'network', 'socket', 'http']):
    
        pass
    pass
            return ErrorCategory.NETWORK
        
        # Database-related errors
        if any(keyword in component_lower for keyword in 
               ['database', 'db', 'sql', 'mongo', 'redis']):
    
        pass
    pass
            return ErrorCategory.DATABASE
        
        # Validation errors
        if any(keyword in error_type_lower for keyword in 
               ['validation', 'invalid', 'format', 'parse']):
    
        pass
    pass
            return ErrorCategory.VALIDATION
        
        # Configuration errors
        if any(keyword in error_message_lower for keyword in 
               ['config', 'setting', 'parameter', 'environment']):
    
        pass
    pass
            return ErrorCategory.CONFIGURATION
        
        # Security errors
        if any(keyword in error_type_lower for keyword in 
               ['permission', 'auth', 'security', 'access', 'forbidden']):
    
        pass
    pass
            return ErrorCategory.SECURITY
        
        # Performance errors
        if any(keyword in error_message_lower for keyword in 
               ['memory', 'timeout', 'slow', 'performance']):
    
        pass
    pass
            return ErrorCategory.PERFORMANCE
        
        # External API errors
        if any(keyword in component_lower for keyword in 
               ['api', 'external', 'service', 'client']):
    
        pass
    pass
            return ErrorCategory.EXTERNAL_API
        
        # System errors
        if any(keyword in error_type_lower for keyword in 
               ['system', 'os', 'file', 'disk', 'memory']):
    
        pass
    pass
            return ErrorCategory.SYSTEM
        
        return ErrorCategory.UNKNOWN
    
    def _determine_severity(self, error_type: str, error_message: str, 
                           category: ErrorCategory) -> ErrorSeverity:
    pass
        """Determine error severity based on type and category."""
        error_type_lower = error_type.lower()
        error_message_lower = error_message.lower()
        
        # Critical errors
        if any(keyword in error_type_lower for keyword in 
               ['critical', 'fatal', 'crash', 'abort']):
    
        pass
    pass
            return ErrorSeverity.CRITICAL
        
        if category == ErrorCategory.SECURITY:
    
        pass
    pass
            return ErrorSeverity.HIGH
        
        # High severity errors
        if any(keyword in error_message_lower for keyword in 
               ['failed to start', 'cannot connect', 'out of memory']):
    
        pass
    pass
            return ErrorSeverity.HIGH
        
        # Medium severity errors
        if category in [ErrorCategory.DATABASE, ErrorCategory.EXTERNAL_API]:
    
        pass
    pass
            return ErrorSeverity.MEDIUM
        
        if any(keyword in error_type_lower for keyword in 
               ['warning', 'deprecated']):
    
        pass
    pass
            return ErrorSeverity.LOW
        
        return ErrorSeverity.MEDIUM
    
    def log_error(self, error_type: str, error_message: str, 
                  component: str = "unknown", operation: str = "unknown",
                  severity: Optional[ErrorSeverity] = None,
                  category: Optional[ErrorCategory] = None,
                  **metadata) -> str:
    pass
        """
        Log an error with comprehensive tracking.
        
        Args:
    pass
            error_type: Type of error
            error_message: Error message
            component: Component where error occurred
            operation: Operation being performed
            severity: Error severity (auto-determined if not provided)
            category: Error category (auto-determined if not provided)
            **metadata: Additional metadata
            
        Returns:
    pass
            Error ID for tracking
        """
        # Auto-categorize if not provided
        if category is None:
    
        pass
    pass
            category = self._categorize_error(error_type, error_message, component)
        
        if severity is None:
    
        pass
    pass
            severity = self._determine_severity(error_type, error_message, category)
        
        # Generate error ID
        error_id = self._generate_error_id(error_type, error_message, component, operation)
        
        # Create error event
        error_event = ErrorEvent(
            timestamp=datetime.utcnow(),
            error_id=error_id,
            error_type=error_type,
            error_message=error_message,
            component=component,
            operation=operation,
            severity=severity,
            category=category,
            context_data=metadata.get('context_data', {}),
            metadata=metadata
        )
        
        # Store error
        with self._lock:
    pass
            self._errors.append(error_event)
            self._error_counts[error_id] += 1
        
        # Pattern analysis
        if self._enable_pattern_analysis:
    
        pass
    pass
            self._analyze_error_pattern(error_event)
        
        # Create logging context
        context = error_context(error_type, component)
        
        # Log using centralized logger
        self._logger.error_occurred(
            error_type=error_type,
            error_message=error_message,
            component=component,
            context=context,
            operation=operation,
            error_id=error_id,
            severity=severity.value,
            category=category.value,
            session_id=self._session_id,
            **metadata
        )
        
        return error_id
    
    def log_exception(self, exception: Exception, component: str = "unknown", 
                     operation: str = "unknown", 
                     severity: Optional[ErrorSeverity] = None,
                     category: Optional[ErrorCategory] = None,
                     **metadata) -> str:
    pass
        """
        Log an exception with full context and stack trace.
        
        Args:
    pass
    pass
            exception: Exception instance
            component: Component where exception occurred
            operation: Operation being performed
            severity: Error severity (auto-determined if not provided)
            category: Error category (auto-determined if not provided)
            **metadata: Additional metadata
            
        Returns:
    pass
            Error ID for tracking
        """
        error_type = type(exception).__name__
        error_message = str(exception)
        
        # Capture stack trace
        stack_trace = ''.join(traceback.format_exception(
            type(exception), exception, exception.__traceback__
        ))
        
        # Auto-categorize if not provided
        if category is None:
    
        pass
    pass
    pass
            category = self._categorize_error(error_type, error_message, component)
        
        if severity is None:
    
        pass
    pass
            severity = self._determine_severity(error_type, error_message, category)
        
        # Generate error ID
        error_id = self._generate_error_id(error_type, error_message, component, operation)
        
        # Create error event
        error_event = ErrorEvent(
            timestamp=datetime.utcnow(),
            error_id=error_id,
            error_type=error_type,
            error_message=error_message,
            component=component,
            operation=operation,
            severity=severity,
            category=category,
            stack_trace=stack_trace,
            context_data=metadata.get('context_data', {}),
            metadata=metadata
        )
        
        # Store error
        with self._lock:
    pass
            self._errors.append(error_event)
            self._error_counts[error_id] += 1
        
        # Pattern analysis
        if self._enable_pattern_analysis:
    
        pass
    pass
            self._analyze_error_pattern(error_event)
        
        # Create logging context
        context = error_context(error_type, component)
        
        # Log using centralized logger
        self._logger.exception_caught()
            exception=exception,
            component=component,
            operation=operation,
            context=context,
            error_id=error_id,
            severity=severity.value,
            category=category.value,
            session_id=self._session_id,
            stack_trace=stack_trace,
            **metadata
        )
        
        return error_id
    
    def log_validation_error(self, field: str, value: str, reason: str,
                           component: str = "validation", **metadata) -> str:
    pass
        """
        Log a validation error with structured information.
        
        Args:
    pass
            field: Field that failed validation
            value: Value that was invalid
            reason: Reason for validation failure
            component: Component performing validation
            **metadata: Additional metadata
            
        Returns:
    pass
            Error ID for tracking
        """
        error_type = "ValidationError"
        error_message = f"Field '{field}' validation failed: {reason}"
        
        # Create logging context
        context = error_context("validation", component)
        
        # Log using centralized logger
        self._logger.validation_error(
            field=field,
            value=value,
            reason=reason,
            context=context,
            component=component,
            session_id=self._session_id,
            **metadata
        )
        
        # Also log as regular error for tracking
        return self.log_error(
            error_type=error_type,
            error_message=error_message,
            component=component,
            operation="validation",
            category=ErrorCategory.VALIDATION,
            severity=ErrorSeverity.MEDIUM,
            field=field,
            value=value,
            reason=reason,
            **metadata
        )
    
    def _analyze_error_pattern(self, error_event: ErrorEvent) -> None:
    pass
        """Analyze error patterns for trend detection."""
        signature = self._generate_error_signature(
            error_event.error_type, 
            error_event.component, 
            error_event.operation
        )
        
        with self._lock:
    pass
            if signature in self._error_patterns:
    
        pass
    pass
                pattern = self._error_patterns[signature]
                pattern.count += 1
                pattern.last_seen = error_event.timestamp
                
                # Update components and operations lists
                if error_event.component not in pattern.components:
    
        pass
    pass
                    pattern.components.append(error_event.component)
                if error_event.operation not in pattern.operations:
    
        pass
    pass
                    pattern.operations.append(error_event.operation)
                
                # Update severity if current error is more severe
                if error_event.severity.value > pattern.severity.value:
    
        pass
    pass
                    pattern.severity = error_event.severity
            else:
    pass
                # Create new pattern
                self._error_patterns[signature] = ErrorPattern(
                    error_signature=signature,
                    count=1,
                    first_seen=error_event.timestamp,
                    last_seen=error_event.timestamp,
                    components=[error_event.component],
                    operations=[error_event.operation],
                    severity=error_event.severity,
                    category=error_event.category,
                    sample_error=error_event
                )
    
    def get_error_summary(self, hours: int = 24) -> Dict[str, Any]:
    pass
        """
        Get error summary for the specified time period.
        
        Args:
    
        pass
    pass
            hours: Number of hours to analyze
            
        Returns:
    pass
            Dictionary containing error summary
        """
        from datetime import timedelta
        cutoff = datetime.utcnow() - timedelta(hours=hours)
        
        with self._lock:
    pass
            recent_errors = [e for e in self._errors if e.timestamp >= cutoff]
        
        if not recent_errors:
    
        pass
    pass
            return {'message': 'No errors in the specified period'}
        
        # Count by severity
        severity_counts = defaultdict(int)
        for error in recent_errors:
    
        pass
    pass
            severity_counts[error.severity.value] += 1
        
        # Count by category
        category_counts = defaultdict(int)
        for error in recent_errors:
    pass
            category_counts[error.category.value] += 1
        
        # Count by component
        component_counts = defaultdict(int)
        for error in recent_errors:
    pass
            component_counts[error.component] += 1
        
        # Top error types
        error_type_counts = defaultdict(int)
        for error in recent_errors:
    pass
            error_type_counts[error.error_type] += 1
        
        return {
            'period_hours': hours,
            'total_errors': len(recent_errors),
            'severity_distribution': dict(severity_counts),
            'category_distribution': dict(category_counts),
            'top_components': dict(sorted(component_counts.items(), 
                                        key=lambda x: x[1], reverse=True)[:10]),
            'top_error_types': dict(sorted(error_type_counts.items(), 
                                         key=lambda x: x[1], reverse=True)[:10]),
            'session_id': self._session_id
        }
    
    def get_error_patterns(self, min_count: int = 2) -> List[Dict[str, Any]]:
    pass
        """
        Get detected error patterns.
        
        Args:
    pass
            min_count: Minimum occurrence count to include pattern
            
        Returns:
    pass
            List of error patterns
        """
        with self._lock:
    pass
            patterns = []
            for signature, pattern in self._error_patterns.items():
    pass
                if pattern.count >= min_count:
    
        pass
    pass
                    patterns.append({
                        'signature': signature,
                        'count': pattern.count,
                        'first_seen': pattern.first_seen.isoformat(),
                        'last_seen': pattern.last_seen.isoformat(),
                        'components': pattern.components,
                        'operations': pattern.operations,
                        'severity': pattern.severity.value,
                        'category': pattern.category.value,
                        'sample_error_id': pattern.sample_error.error_id
                    })
            
            return sorted(patterns, key=lambda x: x['count'], reverse=True)
    
    def get_critical_errors(self, hours: int = 24) -> List[Dict[str, Any]]:
    pass
        """
        Get critical errors from the specified time period.
        
        Args:
    
        pass
    pass
            hours: Number of hours to analyze
            
        Returns:
    pass
            List of critical errors
        """
        from datetime import timedelta
        cutoff = datetime.utcnow() - timedelta(hours=hours)
        
        with self._lock:
    pass
            critical_errors = [
                e for e in self._errors 
                if (e.timestamp >= cutoff and 
                    e.severity in [ErrorSeverity.CRITICAL, ErrorSeverity.HIGH])
            ]
        
        return [
            {
                'error_id': error.error_id,
                'timestamp': error.timestamp.isoformat(),
                'error_type': error.error_type,
                'error_message': error.error_message,
                'component': error.component,
                'operation': error.operation,
                'severity': error.severity.value,
                'category': error.category.value,
                'metadata': error.metadata
            }
            for error in critical_errors
        ]
    
    def resolve_error(self, error_id: str, resolution_notes: str) -> bool:
    pass
        """
        Mark an error as resolved.
        
        Args:
    pass
            error_id: Error ID to resolve
            resolution_notes: Notes about the resolution
            
        Returns:
    pass
            True if error was found and resolved, False otherwise
        """
        with self._lock:
    
        pass
    pass
            for error in self._errors:
    pass
                if error.error_id == error_id:
    
        pass
    pass
                    error.resolved = True
                    error.resolution_notes = resolution_notes
                    
                    # Log resolution
                    self._logger.info(
                        f"Error resolved: {error_id} - {resolution_notes}",
                        extra={
                            'error_resolution': True,
                            'error_id': error_id,
                            'resolution_notes': resolution_notes,
                            'session_id': self._session_id
                        }
                    )
                    return True
        
        return False
    
    def export_errors(self, hours: int = 24, include_resolved: bool = False) -> str:
    pass
        """
        Export errors to JSON format for external analysis.
        
        Args:
    pass
            hours: Number of hours to export
            include_resolved: Include resolved errors
            
        Returns:
    pass
            JSON string containing error data
        """
        from datetime import timedelta
        cutoff = datetime.utcnow() - timedelta(hours=hours)
        
        with self._lock:
    pass
            errors_to_export = []
            for error in self._errors:
    pass
                if error.timestamp >= cutoff:
    
        pass
    pass
                    if include_resolved or not error.resolved:
    
        pass
    pass
                        error_data = {
                            'error_id': error.error_id,
                            'timestamp': error.timestamp.isoformat(),
                            'error_type': error.error_type,
                            'error_message': error.error_message,
                            'component': error.component,
                            'operation': error.operation,
                            'severity': error.severity.value,
                            'category': error.category.value,
                            'stack_trace': error.stack_trace,
                            'context_data': error.context_data,
                            'metadata': error.metadata,
                            'resolved': error.resolved,
                            'resolution_notes': error.resolution_notes
                        }
                        errors_to_export.append(error_data)
        
        export_data = {
            'export_timestamp': datetime.utcnow().isoformat(),
            'period_hours': hours,
            'session_id': self._session_id,
            'total_errors': len(errors_to_export),
            'errors': errors_to_export
        }
        
        return json.dumps(export_data, indent=2)
    
    def clear_errors(self) -> None:
    pass
        """Clear stored errors (useful for testing or memory management)."""
        with self._lock:
    pass
            self._errors.clear()
            self._error_patterns.clear()
            self._error_counts.clear()


# Global error logger instance
_error_logger = None


def get_enhanced_error_logger() -> EnhancedErrorLogger:
    pass
    """Get global enhanced error logger instance."""
    global _error_logger
    if _error_logger is None:
    
        pass
    pass
        _error_logger = EnhancedErrorLogger()
    return _error_logger