"""
Centralized logger factory with singleton pattern and specialized logger creation.

This module provides a unified factory for creating and managing loggers throughout
the application, ensuring consistent configuration and eliminating duplicates.
"""

import logging
import threading




class ContextualLogger:
    
        pass
    pass
    """
    Logger wrapper that adds context to log messages and provides enhanced functionality.
    
    This wrapper automatically injects context information into log messages,
    provides convenience methods for different logging scenarios, and includes
    performance optimizations with lazy evaluation support.
    """
    
    def __init__(self, logger: logging.Logger, default_context: Optional[LogContext] = None, enable_optimization: bool = True):
    pass
        self.logger = logger
        self.default_context = default_context
        self.enable_optimization = enable_optimization
        self._optimized_logger = OptimizedLogger(logger, get_performance_monitor()) if enable_optimization else None
    
    def _get_effective_context(self, context: Optional[LogContext] = None) -> Optional[LogContext]:
    pass
        """Get the effective context for logging."""
        if context:
    
        pass
    pass
            return context
        if self.default_context:
    
        pass
    pass
            return self.default_context
        return get_context()
    
    def _log_with_context(self, level: int, message: Union[str, LazyString, LazyFormat], *args, context: Optional[LogContext] = None, **kwargs):
    pass
        """Log message with context information and performance optimization."""
        # Early exit if logging is disabled for this level (performance optimization)
        if self.enable_optimization and not self.logger.isEnabledFor(level):
    
        pass
    pass
            return
        
        effective_context = self._get_effective_context(context)
        
        extra = kwargs.get('extra', {})
        if effective_context:
    
        pass
    pass
            extra['context'] = effective_context
        kwargs['extra'] = extra
        
        # Use optimized logger if available, otherwise fall back to regular logging
        if self._optimized_logger:
    
        pass
    pass
            self._optimized_logger._log_with_timing(level, message, *args, **kwargs)
        else:
    pass
            # Evaluate lazy message if needed for regular logger
            if isinstance(message, (LazyString, LazyFormat)):
    
        pass
    pass
                message = str(message)
            self.logger.log(level, message, *args, **kwargs)
    
    def debug(self, message: Union[str, LazyString, LazyFormat], *args, context: Optional[LogContext] = None, **kwargs):
    pass
        """Log debug message with context and lazy evaluation support."""
        self._log_with_context(logging.DEBUG, message, *args, context=context, **kwargs)
    
    def info(self, message: Union[str, LazyString, LazyFormat], *args, context: Optional[LogContext] = None, **kwargs):
    pass
        """Log info message with context and lazy evaluation support."""
        self._log_with_context(logging.INFO, message, *args, context=context, **kwargs)
    
    def warning(self, message: Union[str, LazyString, LazyFormat], *args, context: Optional[LogContext] = None, **kwargs):
    pass
        """Log warning message with context and lazy evaluation support."""
        self._log_with_context(logging.WARNING, message, *args, context=context, **kwargs)
    
    def error(self, message: Union[str, LazyString, LazyFormat], *args, context: Optional[LogContext] = None, **kwargs):
    pass
        """Log error message with context and lazy evaluation support."""
        self._log_with_context(logging.ERROR, message, *args, context=context, **kwargs)
    
    def critical(self, message: Union[str, LazyString, LazyFormat], *args, context: Optional[LogContext] = None, **kwargs):
    pass
        """Log critical message with context and lazy evaluation support."""
        self._log_with_context(logging.CRITICAL, message, *args, context=context, **kwargs)
    
    def exception(self, message: Union[str, LazyString, LazyFormat], *args, context: Optional[LogContext] = None, **kwargs):
    pass
        """Log exception with full traceback and context."""
        kwargs['exc_info'] = True
        self.error(message, *args, context=context, **kwargs)
    
    def with_context(self, context: LogContext) -> 'ContextualLogger':
    pass
        """Create new logger instance with specific context."""
        return ContextualLogger(self.logger, context, self.enable_optimization)
    
    # Convenience methods for lazy logging
    def lazy_debug(self, template: str, *args, **kwargs):
    pass
        """Log debug message with lazy string formatting."""
        context = kwargs.pop('context', None)
        self.debug(LazyFormat(template, *args, **kwargs), context=context)
    
    def lazy_info(self, template: str, *args, **kwargs):
    pass
        """Log info message with lazy string formatting."""
        context = kwargs.pop('context', None)
        self.info(LazyFormat(template, *args, **kwargs), context=context)
    
    def lazy_warning(self, template: str, *args, **kwargs):
    pass
        """Log warning message with lazy string formatting."""
        context = kwargs.pop('context', None)
        self.warning(LazyFormat(template, *args, **kwargs), context=context)
    
    def lazy_error(self, template: str, *args, **kwargs):
    pass
        """Log error message with lazy string formatting."""
        context = kwargs.pop('context', None)
        self.error(LazyFormat(template, *args, **kwargs), context=context)
    
    def get_performance_metrics(self):
    pass
        """Get performance metrics for this logger."""
        if self._optimized_logger:
    
        pass
    pass
            return self._optimized_logger.monitor.get_metrics(self.logger.name)
        return None
    
    def clear_performance_cache(self):
    pass
        """Clear performance optimization caches."""
        if self._optimized_logger:
    
        pass
    pass
            self._optimized_logger.clear_cache()


class TradeLogger(ContextualLogger):
    pass
    """Specialized logger for trade execution events."""
    
    def trade_opened(self, symbol: str, side: str, quantity: float, price: float, **kwargs):
    pass
        """Log trade opening event."""
        self.info(
            f"Trade opened: {side} {quantity} {symbol} @ {price}",
            extra={'trade_event': 'opened', 'symbol': symbol, 'side': side, 'quantity': quantity, 'price': price, **kwargs}
        )
    
    def trade_closed(self, symbol: str, side: str, quantity: float, price: float, pnl: float = None, **kwargs):
    pass
        """Log trade closing event."""
        pnl_info = f" PnL: {pnl}" if pnl is not None else ""
        self.info(
            f"Trade closed: {side} {quantity} {symbol} @ {price}{pnl_info}",
            extra={'trade_event': 'closed', 'symbol': symbol, 'side': side, 'quantity': quantity, 'price': price, 'pnl': pnl, **kwargs}
        )
    
    def order_placed(self, order_id: str, symbol: str, side: str, quantity: float, order_type: str, **kwargs):
    pass
        """Log order placement event."""
        self.info(
            f"Order placed: {order_id} - {side} {quantity} {symbol} ({order_type})",
            extra={'trade_event': 'order_placed', 'order_id': order_id, 'symbol': symbol, 'side': side, 'quantity': quantity, 'order_type': order_type, **kwargs}
        )
    
    def order_filled(self, order_id: str, symbol: str, filled_quantity: float, avg_price: float, **kwargs):
    pass
        """Log order fill event."""
        self.info(
            f"Order filled: {order_id} - {filled_quantity} {symbol} @ {avg_price}",
            extra={'trade_event': 'order_filled', 'order_id': order_id, 'symbol': symbol, 'filled_quantity': filled_quantity, 'avg_price': avg_price, **kwargs}
        )


class PerformanceLogger(ContextualLogger):
    pass
    """Specialized logger for performance metrics and monitoring."""
    
    def execution_time(self, operation: str, duration_ms: float, **kwargs):
    pass
        """Log execution time metric."""
        self.info(
            f"Performance: {operation} completed in {duration_ms:.2f}ms",
            extra={'metric_type': 'execution_time', 'operation': operation, 'duration_ms': duration_ms, **kwargs}
        )
    
    def memory_usage(self, component: str, memory_mb: float, **kwargs):
    pass
        """Log memory usage metric."""
        self.info(
            f"Memory: {component} using {memory_mb:.2f}MB",
            extra={'metric_type': 'memory_usage', 'component': component, 'memory_mb': memory_mb, **kwargs}
        )
    
    def throughput(self, operation: str, count: int, duration_s: float, **kwargs):
    pass
        """Log throughput metric."""
        rate = count / duration_s if duration_s > 0 else 0
        self.info(
            f"Throughput: {operation} - {count} operations in {duration_s:.2f}s ({rate:.2f}/s)",
            extra={'metric_type': 'throughput', 'operation': operation, 'count': count, 'duration_s': duration_s, 'rate': rate, **kwargs}
        )
    
    def resource_usage(self, cpu_percent: float = None, memory_mb: float = None, **kwargs):
    pass
        """Log system resource usage."""
        metrics = []
        extra_data = {'metric_type': 'resource_usage'}
        
        if cpu_percent is not None:
    
        pass
    pass
            metrics.append(f"CPU: {cpu_percent:.1f}%")
            extra_data['cpu_percent'] = cpu_percent
        
        if memory_mb is not None:
    
        pass
    pass
            metrics.append(f"Memory: {memory_mb:.1f}MB")
            extra_data['memory_mb'] = memory_mb
        
        self.info(f"Resources: {', '.join(metrics)}", extra={**extra_data, **kwargs})


class ErrorLogger(ContextualLogger):
    pass
    """Specialized logger for centralized error tracking."""
    
    def error_occurred(self, error_type: str, error_message: str, component: str = None, **kwargs):
    pass
        """Log error occurrence with categorization."""
        self.error(
            f"Error in {component or 'unknown'}: {error_type} - {error_message}",
            extra={'error_type': error_type, 'error_message': error_message, 'component': component, **kwargs}
        )
    
    def exception_caught(self, exception: Exception, component: str = None, operation: str = None, **kwargs):
    pass
        """Log caught exception with full context."""
        self.exception(
            f"Exception in {component or 'unknown'}.{operation or 'unknown'}: {type(exception).__name__}: {str(exception)}",
            extra={'exception_type': type(exception).__name__, 'exception_message': str(exception), 'component': component, 'operation': operation, **kwargs}
        )
    
    def validation_error(self, field: str, value: str, reason: str, **kwargs):
    pass
        """Log validation error."""
        self.error(
            f"Validation error: {field}='{value}' - {reason}",
            extra={'error_type': 'validation', 'field': field, 'value': value, 'reason': reason, **kwargs}
        )


class CLILogger(ContextualLogger):
    pass
    """Specialized logger for CLI operations with user-friendly output."""
    
    def __init__(self, logger: logging.Logger, verbose: bool = False, default_context: Optional[LogContext] = None):
    pass
        super().__init__(logger, default_context)
        self.verbose = verbose
    
    def command_start(self, command: str, command_args: Dict = None, **kwargs):
    pass
        """Log command execution start."""
        args_str = f" with args: {command_args}" if command_args else ""
        
        # Extract custom parameters and put them in extra
        custom_params = ['session_id', 'execution_time_s', 'context']
        extra = kwargs.get('extra', {})
        extra.update({'command': command, 'command_args': command_args})
        
        # Move custom parameters to extra and remove from kwargs
        for param in custom_params:
    pass
            if param in kwargs:
    
        pass
    pass
                extra[param] = kwargs.pop(param)
        
        kwargs['extra'] = extra
        self.info(f"Executing command: {command}{args_str}", **kwargs)
    
    def command_success(self, command: str, result: str = None, **kwargs):
    pass
        """Log successful command completion."""
        result_str = f" - {result}" if result else ""
        
        # Extract custom parameters and put them in extra
        custom_params = ['session_id', 'execution_time_s', 'context']
        extra = kwargs.get('extra', {})
        extra.update({'command': command, 'result': result})
        
        # Move custom parameters to extra and remove from kwargs
        for param in custom_params:
    pass
            if param in kwargs:
    
        pass
    pass
                extra[param] = kwargs.pop(param)
        
        kwargs['extra'] = extra
        self.info(f"Command completed successfully: {command}{result_str}", **kwargs)
    
    def command_error(self, command: str, error: str, **kwargs):
    pass
        """Log command execution error."""
        # Extract custom parameters and put them in extra
        custom_params = ['session_id', 'execution_time_s', 'context']
        extra = kwargs.get('extra', {})
        extra.update({'command': command, 'error': error})
        
        # Move custom parameters to extra and remove from kwargs
        for param in custom_params:
    pass
            if param in kwargs:
    
        pass
    pass
                extra[param] = kwargs.pop(param)
        
        kwargs['extra'] = extra
        self.error(f"Command failed: {command} - {error}", **kwargs)
    
    def progress(self, message: str, current: int = None, total: int = None, **kwargs):
    pass
        """Log progress information."""
        if current is not None and total is not None:
    
        pass
    pass
            percentage = (current / total) * 100 if total > 0 else 0
            progress_str = f" ({current}/{total} - {percentage:.1f}%)"
        else:
    pass
            progress_str = ""
        
        # Extract custom parameters and put them in extra
        custom_params = ['session_id', 'execution_time_s', 'context']
        extra = kwargs.get('extra', {})
        extra.update({'progress_message': message, 'current': current, 'total': total})
        
        # Move custom parameters to extra and remove from kwargs
        for param in custom_params:
    pass
            if param in kwargs:
    
        pass
    pass
                extra[param] = kwargs.pop(param)
        
        kwargs['extra'] = extra
        self.info(f"Progress: {message}{progress_str}", **kwargs)
    
    def user_info(self, message: str, **kwargs):
    pass
        """Log user-facing information."""
        if self.verbose or kwargs.get('force', False):
    
        pass
    pass
            # Extract custom parameters and put them in extra
            custom_params = ['session_id', 'execution_time_s', 'context']
            extra = kwargs.get('extra', {})
            extra.update({'user_message': message})
            
            # Move custom parameters to extra and remove from kwargs
            for param in custom_params:
    pass
                if param in kwargs:
    
        pass
    pass
                    extra[param] = kwargs.pop(param)
            
            kwargs['extra'] = extra
            self.info(f"Info: {message}", **kwargs)


class LoggerFactory:
    pass
    """
    Centralized factory for creating and managing loggers with singleton pattern.
    
    This factory ensures consistent logger configuration across the application
    and provides caching to prevent duplicate logger creation.
    """
    
    _instance: Optional['LoggerFactory'] = None
    _lock = threading.Lock()
    
    def __init__(self):
    pass
        self._config: Optional[LoggingConfig] = None
        self._logger_cache: Dict[str, ContextualLogger] = {}
        self._configured = False
    
    def __new__(cls) -> 'LoggerFactory':
    pass
        """Implement singleton pattern."""
        if cls._instance is None:
    
        pass
    pass
            with cls._lock:
    pass
                if cls._instance is None:
    
        pass
    pass
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def setup_global_config(self, config: LoggingConfig) -> None:
    pass
        """
        Set up global logging configuration.
        
        Args:
    pass
            config: LoggingConfig instance with all settings
        """
        self._config = config
        self._configure_logging()
        self._configured = True
    
    def _get_base_handlers(self) -> list:
    pass
        """Get base handlers based on configuration."""
        handlers = []
        if self._config.console_output:
    
        pass
    pass
            handlers.append('console')
        if self._config.file_output:
    
        pass
    pass
            handlers.append('file')
        return handlers or []  # Can be empty for testing
    
    def _get_specialized_handlers(self, specialized_handler: str, is_enabled: bool) -> list:
    pass
        """Get handlers for specialized loggers."""
        handlers = []
        if is_enabled:
    
        pass
    pass
            handlers.append(specialized_handler)
        if self._config.console_output:
    
        pass
    pass
            handlers.append('console')
        return handlers or []  # Can be empty for testing
    
    def _configure_logging(self) -> None:
    pass
        """Configure the Python logging system based on current config."""
        if not self._config:
    
        pass
    pass
            return
        
        # Create log directory
        self._config.log_directory.mkdir(parents=True, exist_ok=True)
        
        # Define formatters
        formatters = {}
        if self._config.format_type == "structured":
    
        pass
    pass
            formatters['structured'] = {
                '()': StructuredJSONFormatter
            }
            formatters['simple'] = {
                '()': SimpleFormatter
            }
        else:
    pass
            formatters['simple'] = {
                'format': '%(asctime)s - %(name)s - %(levelname)s - [%(module)s:%(funcName)s:%(lineno)d] - %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            }
        
        # Define handlers
        handlers = {}
        
        if self._config.console_output:
    
        pass
    pass
            handlers['console'] = {
                'class': 'logging.StreamHandler',
                'level': self._config.level,
                'formatter': 'simple',
                'stream': 'ext://sys.stdout'
            }
        
        if self._config.file_output:
    
        pass
    pass
            if self._config.enable_async_logging:
    
        pass
    pass
                handlers['file'] = {
                    '()': AsyncRotatingFileHandler,
                    'filename': str(self._config.log_directory / 'genebot.log'),
                    'max_bytes': self._config.max_file_size,
                    'backup_count': self._config.backup_count,
                    'queue_size': self._config.async_queue_size,
                    'batch_size': self._config.async_batch_size,
                    'flush_interval': self._config.async_flush_interval,
                    'formatter': self._config.format_type,
                    'level': self._config.level
                }
            elif self._config.optimized_file_io:
    
        pass
    pass
                # Create rotation policy
                rotation_policy = setup_log_rotation_policy(
                    self._config.log_directory,
                    max_file_size_mb=self._config.max_file_size // (1024*1024),
                    max_files=self._config.backup_count,
                    max_age_days=self._config.max_log_age_days,
                    compress_rotated=self._config.compress_rotated_files,
                    min_free_space_mb=self._config.min_free_space_mb
                )
                
                handlers['file'] = {
                    '()': CompressedRotatingFileHandler,
                    'filename': str(self._config.log_directory / 'genebot.log'),
                    'maxBytes': self._config.max_file_size,
                    'backupCount': self._config.backup_count,
                    'rotation_policy': rotation_policy,
                    'formatter': self._config.format_type,
                    'level': self._config.level
                }
            else:
    pass
                handlers['file'] = {
                    'class': 'logging.handlers.RotatingFileHandler',
                    'level': self._config.level,
                    'formatter': self._config.format_type,
                    'filename': str(self._config.log_directory / 'genebot.log'),
                    'maxBytes': self._config.max_file_size,
                    'backupCount': self._config.backup_count
                }
        
        if self._config.enable_error_logging:
    
        pass
    pass
            if self._config.enable_async_logging:
    
        pass
    pass
                handlers['error_file'] = {
                    '()': AsyncRotatingFileHandler,
                    'filename': str(self._config.log_directory / 'errors.log'),
                    'max_bytes': self._config.max_file_size,
                    'backup_count': self._config.backup_count,
                    'queue_size': self._config.async_queue_size,
                    'batch_size': self._config.async_batch_size,
                    'flush_interval': self._config.async_flush_interval,
                    'formatter': self._config.format_type,
                    'level': 'ERROR'
                }
            else:
    pass
                handlers['error_file'] = {
                    'class': 'logging.handlers.RotatingFileHandler',
                    'level': 'ERROR',
                    'formatter': self._config.format_type,
                    'filename': str(self._config.log_directory / 'errors.log'),
                    'maxBytes': self._config.max_file_size,
                    'backupCount': self._config.backup_count
                }
        
        if self._config.enable_trade_logging:
    
        pass
    pass
            if self._config.enable_async_logging:
    
        pass
    pass
                handlers['trade_file'] = {
                    '()': AsyncRotatingFileHandler,
                    'filename': str(self._config.log_directory / 'trades.log'),
                    'max_bytes': self._config.max_file_size,
                    'backup_count': self._config.backup_count * 2,  # Keep more trade history
                    'queue_size': self._config.async_queue_size,
                    'batch_size': self._config.async_batch_size,
                    'flush_interval': self._config.async_flush_interval,
                    'formatter': self._config.format_type,
                    'level': 'INFO'
                }
            elif self._config.optimized_file_io:
    
        pass
    pass
                rotation_policy = setup_log_rotation_policy(
                    self._config.log_directory,
                    max_file_size_mb=self._config.max_file_size // (1024*1024),
                    max_files=self._config.backup_count * 2,  # Keep more trade history
                    max_age_days=self._config.max_log_age_days * 2,  # Keep trade logs longer
                    compress_rotated=self._config.compress_rotated_files,
                    min_free_space_mb=self._config.min_free_space_mb
                )
                
                handlers['trade_file'] = {
                    '()': CompressedRotatingFileHandler,
                    'filename': str(self._config.log_directory / 'trades.log'),
                    'maxBytes': self._config.max_file_size,
                    'backupCount': self._config.backup_count * 2,
                    'rotation_policy': rotation_policy,
                    'formatter': self._config.format_type,
                    'level': 'INFO'
                }
            else:
    pass
                handlers['trade_file'] = {
                    'class': 'logging.handlers.RotatingFileHandler',
                    'level': 'INFO',
                    'formatter': self._config.format_type,
                    'filename': str(self._config.log_directory / 'trades.log'),
                    'maxBytes': self._config.max_file_size,
                    'backupCount': self._config.backup_count * 2  # Keep more trade history
                }
        
        if self._config.enable_performance_logging:
    
        pass
    pass
            if self._config.enable_async_logging:
    
        pass
    pass
                handlers['performance_file'] = {
                    '()': AsyncRotatingFileHandler,
                    'filename': str(self._config.log_directory / 'performance.log'),
                    'max_bytes': self._config.max_file_size,
                    'backup_count': self._config.backup_count,
                    'queue_size': self._config.async_queue_size,
                    'batch_size': self._config.async_batch_size,
                    'flush_interval': self._config.async_flush_interval,
                    'formatter': self._config.format_type,
                    'level': 'INFO'
                }
            else:
    pass
                handlers['performance_file'] = {
                    'class': 'logging.handlers.RotatingFileHandler',
                    'level': 'INFO',
                    'formatter': self._config.format_type,
                    'filename': str(self._config.log_directory / 'performance.log'),
                    'maxBytes': self._config.max_file_size,
                    'backupCount': self._config.backup_count
                }
        
        if self._config.enable_cli_logging:
    
        pass
    pass
            if self._config.enable_async_logging:
    
        pass
    pass
                handlers['cli_file'] = {
                    '()': AsyncRotatingFileHandler,
                    'filename': str(self._config.log_directory / 'cli.log'),
                    'max_bytes': self._config.max_file_size,
                    'backup_count': self._config.backup_count,
                    'queue_size': self._config.async_queue_size,
                    'batch_size': self._config.async_batch_size,
                    'flush_interval': self._config.async_flush_interval,
                    'formatter': self._config.format_type,
                    'level': 'INFO'
                }
            else:
    pass
                handlers['cli_file'] = {
                    'class': 'logging.handlers.RotatingFileHandler',
                    'level': 'INFO',
                    'formatter': self._config.format_type,
                    'filename': str(self._config.log_directory / 'cli.log'),
                    'maxBytes': self._config.max_file_size,
                    'backupCount': self._config.backup_count
                }
        
        # Define loggers with proper hierarchy and propagation
        loggers = {
            '': {  # root logger - minimal handlers to prevent duplicates
                'level': 'WARNING',  # Only show warnings and above from root
                'handlers': []  # No handlers on root to prevent duplicates
            'genebot': {
                'propagate': False  # Don't propagate to root to prevent duplicates
            },
            'genebot.trades': {
                'level': 'INFO',
                'handlers': self._get_specialized_handlers('trade_file', self._config.enable_trade_logging),
                'propagate': False  # Don't propagate to parent genebot logger
            },
            'genebot.performance': {
                'level': 'INFO',
                'handlers': self._get_specialized_handlers('performance_file', self._config.enable_performance_logging),
                'propagate': False  # Don't propagate to parent genebot logger
            },
            'genebot.errors': {
                'level': 'ERROR',
                'handlers': self._get_specialized_handlers('error_file', self._config.enable_error_logging),
                'propagate': False  # Don't propagate to parent genebot logger
            },
            'genebot.cli': {
                'level': self._config.level,
                'handlers': self._get_specialized_handlers('cli_file', self._config.enable_cli_logging),
                'propagate': False  # Don't propagate to parent genebot logger
            },
            'genebot.monitoring': {
                'level': self._config.level,
                'handlers': self._get_base_handlers(),
                'propagate': False  # Don't propagate to parent genebot logger
            },
            'genebot.logging': {
                'level': self._config.level,
                'handlers': self._get_base_handlers(),
                'propagate': False  # Don't propagate to parent genebot logger
            },
            # External library loggers - controlled noise level
            'ccxt': {
                'level': self._config.external_lib_level,
                'handlers': ['file'] if self._config.file_output else [],
                'propagate': False  # Don't propagate to root
            },
            'urllib3': {
                'level': self._config.external_lib_level,
                'handlers': ['file'] if self._config.file_output else [],
                'propagate': False  # Don't propagate to root
            },
            'requests': {
                'level': self._config.external_lib_level,
                'handlers': ['file'] if self._config.file_output else [],
                'propagate': False  # Don't propagate to root
            },
            'aiohttp': {
                'level': self._config.external_lib_level,
                'handlers': ['file'] if self._config.file_output else [],
                'propagate': False  # Don't propagate to root
            },
            'websockets': {
                'level': self._config.external_lib_level,
                'handlers': ['file'] if self._config.file_output else [],
                'propagate': False  # Don't propagate to root
            },
            'asyncio': {
                'level': self._config.external_lib_level,
                'handlers': ['file'] if self._config.file_output else [],
                'propagate': False  # Don't propagate to root
            },
            'sqlalchemy': {
                'level': self._config.external_lib_level,
                'handlers': ['file'] if self._config.file_output else [],
                'propagate': False  # Don't propagate to root
            }
        }
        
        # Create logging configuration
        config_dict = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': formatters,
            'handlers': handlers,
            'loggers': loggers
        }
        
        # Apply configuration
        logging.config.dictConfig(config_dict)
        
        # Enable global async logging if configured
        if self._config.enable_async_logging:
    
        pass
    pass
            enable_async_logging()
    
    def get_logger(self, name: str, context: Optional[LogContext] = None, enable_optimization: bool = True) -> ContextualLogger:
    pass
        """
        Get a contextual logger instance.
        
        Args:
    pass
            name: Logger name
            context: Optional default context for the logger
            enable_optimization: Whether to enable performance optimizations
            
        Returns:
    pass
            ContextualLogger instance
        """
        if not self._configured:
    
        pass
    pass
            self.setup_global_config(get_default_config())
        
        cache_key = f"{name}:{id(context) if context else 'none'}:{enable_optimization}"
        
        if cache_key not in self._logger_cache:
    
        pass
    pass
            logger = logging.getLogger(name)
            self._logger_cache[cache_key] = ContextualLogger(logger, context, enable_optimization)
        
        return self._logger_cache[cache_key]
    
    def get_trade_logger(self, context: Optional[LogContext] = None) -> TradeLogger:
    pass
        """Get specialized logger for trade execution."""
        logger = logging.getLogger('genebot.trades')
        return TradeLogger(logger, context)
    
    def get_cli_logger(self, verbose: bool = False, context: Optional[LogContext] = None) -> CLILogger:
    pass
        """Get specialized logger for CLI operations."""
        logger = logging.getLogger('genebot.cli')
        return CLILogger(logger, verbose, context)
    
    def get_performance_logger(self, context: Optional[LogContext] = None) -> PerformanceLogger:
    pass
        """Get specialized logger for performance metrics."""
        logger = logging.getLogger('genebot.performance')
        return PerformanceLogger(logger, context)
    
    def get_error_logger(self, context: Optional[LogContext] = None) -> ErrorLogger:
    pass
        """Get specialized logger for error tracking."""
        logger = logging.getLogger('genebot.errors')
        return ErrorLogger(logger, context)
    
    def clear_cache(self) -> None:
    pass
        """Clear the logger cache (useful for testing)."""
        self._logger_cache.clear()
    
    def is_configured(self) -> bool:
    pass
        """Check if the factory has been configured."""
        return self._configured
    
    def get_performance_metrics(self) -> Dict[str, Dict]:
    
        pass
    pass
        """Get performance metrics for all loggers."""
        monitor = get_performance_monitor()
        metrics = monitor.get_metrics()
        system_metrics = monitor.get_system_metrics()
        
        return {
            'logger_metrics': metrics,
            'system_metrics': system_metrics
        }
    
    def reset_performance_metrics(self):
    pass
        """Reset all performance metrics."""
        monitor = get_performance_monitor()
        monitor.reset_metrics()
        
        # Clear caches in all cached loggers
        for logger in self._logger_cache.values():
    pass
            if hasattr(logger, 'clear_performance_cache'):
    
        pass
    pass
                logger.clear_performance_cache()
    
    def get_log_directory_status(self) -> Dict[str, Any]:
    pass
        """Get status information about the log directory."""
        if self._config and self._config.log_directory:
    
        pass
    pass
            return monitor_log_directory(self._config.log_directory)
        return {}
    
    def cleanup_old_logs(self, max_age_days: Optional[int] = None) -> list[Path]:
    pass
        """
        Clean up old log files.
        
        Args:
    pass
            max_age_days: Maximum age in days, uses config default if None
            
        Returns:
    
        pass
    pass
            List of deleted files
        """
        if not self._config:
    
        pass
    pass
            return []
        
        from .rotation import DiskSpaceMonitor
        monitor = DiskSpaceMonitor(self._config.log_directory, self._config.min_free_space_mb)
        age_days = max_age_days or self._config.max_log_age_days
        return monitor.cleanup_old_files(age_days)


# Global factory instance
_factory = LoggerFactory()


def setup_global_config(config: LoggingConfig) -> None:
    pass
    """Set up global logging configuration."""
    _factory.setup_global_config(config)


def get_logger(name: str, context: Optional[LogContext] = None, enable_optimization: bool = True) -> ContextualLogger:
    pass
    """Get a contextual logger instance."""
    return _factory.get_logger(name, context, enable_optimization)


def get_trade_logger(context: Optional[LogContext] = None) -> TradeLogger:
    pass
    """Get specialized logger for trade execution."""
    return _factory.get_trade_logger(context)


def get_cli_logger(verbose: bool = False, context: Optional[LogContext] = None) -> CLILogger:
    pass
    """Get specialized logger for CLI operations."""
    return _factory.get_cli_logger(verbose, context)


def get_performance_logger(context: Optional[LogContext] = None) -> PerformanceLogger:
    pass
    """Get specialized logger for performance metrics."""
    return _factory.get_performance_logger(context)


def get_error_logger(context: Optional[LogContext] = None) -> ErrorLogger:
    pass
    """Get specialized logger for error tracking."""
    return _factory.get_error_logger(context)


# Import and expose enhanced loggers
def get_enhanced_trade_logger():
    pass
    """Get enhanced trade logger with audit trail support."""
    from ..monitoring.trade_logger import get_enhanced_trade_logger
    return get_enhanced_trade_logger()


def get_enhanced_performance_logger():
    pass
    """Get enhanced performance logger with system monitoring."""
    from .performance_logger import get_enhanced_performance_logger
    return get_enhanced_performance_logger()


def get_enhanced_error_logger():
    pass
    """Get enhanced error logger with pattern analysis."""
    from .error_logger import get_enhanced_error_logger
    return get_enhanced_error_logger()


def get_enhanced_cli_logger(verbose: bool = False):
    pass
    """Get enhanced CLI logger with command tracking."""
    from ..cli.utils.logger import EnhancedCLILogger
    return EnhancedCLILogger.create_cli_logger(verbose=verbose)


# Performance monitoring functions
def get_logging_performance_metrics() -> Dict[str, Dict]:
    pass
    """Get performance metrics for the logging system."""
    return _factory.get_performance_metrics()


def reset_logging_performance_metrics():
    pass
    """Reset all logging performance metrics."""
    _factory.reset_performance_metrics()


def create_lazy_string(func, *args, **kwargs) -> LazyString:
    pass
    """Create a lazy string for deferred evaluation."""
    return LazyString(func, *args, **kwargs)


def create_lazy_format(template: str, *args, **kwargs) -> LazyFormat:
    pass
    """Create a lazy format string for deferred formatting."""
    return LazyFormat(template, *args, **kwargs)


def get_log_directory_status() -> Dict[str, Any]:
    pass
    """Get status information about the log directory."""
    return _factory.get_log_directory_status()


def cleanup_old_log_files(max_age_days: Optional[int] = None) -> list[Path]:
    pass
    """Clean up old log files."""
    return _factory.cleanup_old_logs(max_age_days)