"""
Performance optimization utilities for the logging system.

This module provides lazy evaluation, performance monitoring, and optimization
techniques to minimize logging overhead in performance-critical scenarios.
"""

import functools
import logging
import time
import threading
from typing import Callable, Any, Dict, Optional, Union
from collections import defaultdict
from dataclasses import dataclass
import psutil
import os


@dataclass
class LoggingMetrics:
    pass
    """Metrics for logging performance monitoring."""
    total_calls: int = 0
    debug_calls: int = 0
    debug_skipped: int = 0
    total_time_ms: float = 0.0
    avg_time_ms: float = 0.0
    memory_usage_mb: float = 0.0
    cpu_percent: float = 0.0


class LazyString:
    pass
    """
    Lazy string evaluation for expensive log message construction.
    
    This class defers string construction until the message is actually needed,
    which can significantly improve performance when debug logging is disabled.
    """
    
    def __init__(self, func: Callable[[], str], *args, **kwargs):
    pass
        """
        Initialize lazy string with function and arguments.
        
        Args:
    pass
            func: Function that returns the string when called
            *args: Positional arguments for the function
            **kwargs: Keyword arguments for the function
        """
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self._cached_result = None
        self._evaluated = False
    
    def __str__(self) -> str:
    pass
        """Evaluate and return the string."""
        if not self._evaluated:
    
        pass
    pass
            self._cached_result = self.func(*self.args, **self.kwargs)
            self._evaluated = True
        return self._cached_result
    
    def __repr__(self) -> str:
    pass
        """Return representation of lazy string."""
        return f"LazyString({self.func.__name__})"


class LazyFormat:
    pass
    """
    Lazy string formatting for log messages.
    
    This class defers string formatting until the message is actually logged,
    avoiding expensive string operations when logging is disabled.
    """
    
    def __init__(self, template: str, *args, **kwargs):
    pass
        """
        Initialize lazy format with template and arguments.
        
        Args:
    pass
            template: Format string template
            *args: Positional arguments for formatting
            **kwargs: Keyword arguments for formatting
        """
        self.template = template
        self.args = args
        self.kwargs = kwargs
        self._cached_result = None
        self._evaluated = False
    
    def __str__(self) -> str:
    pass
        """Evaluate and return the formatted string."""
        if not self._evaluated:
    
        pass
    pass
            try:
    pass
                if self.args and self.kwargs:
    
        pass
    pass
                    self._cached_result = self.template.format(*self.args, **self.kwargs)
                elif self.args:
    
        pass
    pass
                    self._cached_result = self.template.format(*self.args)
                elif self.kwargs:
    
        pass
    pass
                    self._cached_result = self.template.format(**self.kwargs)
                else:
    pass
                    self._cached_result = self.template
            except (KeyError, IndexError, ValueError) as e:
    pass
    pass
                # Fallback to safe formatting
                self._cached_result = f"[Format Error: {e}] {self.template}"
            self._evaluated = True
        return self._cached_result
    
    def __repr__(self) -> str:
    pass
        """Return representation of lazy format."""
        return f"LazyFormat('{self.template[:50]}...')"


class PerformanceMonitor:
    pass
    """
    Monitor logging performance and collect metrics.
    
    This class tracks logging performance metrics to identify bottlenecks
    and optimize logging configuration.
    """
    
    def __init__(self):
    
        pass
    pass
        self._metrics = defaultdict(LoggingMetrics)
        self._lock = threading.Lock()
        self._start_time = time.time()
        self._process = psutil.Process(os.getpid())
    
    def record_log_call(self, logger_name: str, level: int, duration_ms: float, was_skipped: bool = False):
    pass
        """
        Record a logging call for performance tracking.
        
        Args:
    pass
            logger_name: Name of the logger
            level: Log level
            duration_ms: Time taken for the log call in milliseconds
            was_skipped: Whether the log call was skipped due to level filtering
        """
        with self._lock:
    pass
            metrics = self._metrics[logger_name]
            metrics.total_calls += 1
            
            if level == logging.DEBUG:
    
        pass
    pass
                metrics.debug_calls += 1
                if was_skipped:
    
        pass
    pass
                    metrics.debug_skipped += 1
            
            if not was_skipped:
    
        pass
    pass
                metrics.total_time_ms += duration_ms
                metrics.avg_time_ms = metrics.total_time_ms / (metrics.total_calls - metrics.debug_skipped)
    
    def get_metrics(self, logger_name: str = None) -> Union[LoggingMetrics, Dict[str, LoggingMetrics]]:
    pass
        """
        Get performance metrics for logger(s).
        
        Args:
    pass
            logger_name: Specific logger name, or None for all loggers
            
        Returns:
    
        pass
    pass
            LoggingMetrics for specific logger or dict of all metrics
        """
        with self._lock:
    
        pass
    pass
            if logger_name:
    
        pass
    pass
                return self._metrics.get(logger_name, LoggingMetrics())
            else:
    pass
                return dict(self._metrics)
    
    def get_system_metrics(self) -> Dict[str, float]:
    pass
        """Get current system resource usage."""
        try:
    pass
            memory_info = self._process.memory_info()
            cpu_percent = self._process.cpu_percent()
            
            return {
                'memory_mb': memory_info.rss / 1024 / 1024,
                'cpu_percent': cpu_percent,
                'uptime_seconds': time.time() - self._start_time
            }
        except (psutil.NoSuchProcess, psutil.AccessDenied):
    pass
    pass
            return {
                'memory_mb': 0.0,
                'cpu_percent': 0.0,
                'uptime_seconds': time.time() - self._start_time
            }
    
    def reset_metrics(self, logger_name: str = None):
    pass
        """
        Reset performance metrics.
        
        Args:
    pass
            logger_name: Specific logger to reset, or None for all loggers
        """
        with self._lock:
    
        pass
    pass
            if logger_name:
    
        pass
    pass
                if logger_name in self._metrics:
    
        pass
    pass
                    del self._metrics[logger_name]
            else:
    pass
                self._metrics.clear()


class OptimizedLogger:
    pass
    """
    Performance-optimized logger wrapper with lazy evaluation support.
    
    This wrapper adds performance optimizations including:
    pass
    - Lazy message evaluation
    - Level-based filtering before expensive operations
    - Performance monitoring
    - Memory-efficient caching
    """
    
    def __init__(self, logger: logging.Logger, monitor: Optional[PerformanceMonitor] = None):
    pass
        """
        Initialize optimized logger.
        
        Args:
    pass
            logger: Underlying Python logger
            monitor: Optional performance monitor
        """
        self.logger = logger
        self.monitor = monitor or PerformanceMonitor()
        self._level_cache = {}
        self._cache_lock = threading.Lock()
    
    def _is_enabled_for(self, level: int) -> bool:
    pass
        """
        Check if logging is enabled for level with caching.
        
        Args:
    
        pass
    pass
            level: Log level to check
            
        Returns:
    pass
            True if logging is enabled for this level
        """
        # Use cached result if available
        cache_key = (self.logger.name, level)
        if cache_key in self._level_cache:
    
        pass
    pass
            return self._level_cache[cache_key]
        
        # Check and cache result
        with self._cache_lock:
    pass
            enabled = self.logger.isEnabledFor(level)
            self._level_cache[cache_key] = enabled
            return enabled
    
    def _log_with_timing(self, level: int, message: Union[str, LazyString, LazyFormat], *args, **kwargs):
    pass
        """
        Log message with performance timing.
        
        Args:
    pass
            level: Log level
            message: Message to log (can be lazy)
            *args: Additional arguments
            **kwargs: Additional keyword arguments
        """
        start_time = time.perf_counter()
        
        # Check if logging is enabled for this level
        if not self._is_enabled_for(level):
    
        pass
    pass
            duration_ms = (time.perf_counter() - start_time) * 1000
            self.monitor.record_log_call(self.logger.name, level, duration_ms, was_skipped=True)
            return
        
        # Evaluate lazy message if needed
        if isinstance(message, (LazyString, LazyFormat)):
    
        pass
    pass
            message = str(message)
        
        # Perform the actual logging
        self.logger.log(level, message, *args, **kwargs)
        
        # Record performance metrics
        duration_ms = (time.perf_counter() - start_time) * 1000
        self.monitor.record_log_call(self.logger.name, level, duration_ms, was_skipped=False)
    
    def debug(self, message: Union[str, LazyString, LazyFormat], *args, **kwargs):
    pass
        """Log debug message with lazy evaluation."""
        self._log_with_timing(logging.DEBUG, message, *args, **kwargs)
    
    def info(self, message: Union[str, LazyString, LazyFormat], *args, **kwargs):
    pass
        """Log info message with lazy evaluation."""
        self._log_with_timing(logging.INFO, message, *args, **kwargs)
    
    def warning(self, message: Union[str, LazyString, LazyFormat], *args, **kwargs):
    pass
        """Log warning message with lazy evaluation."""
        self._log_with_timing(logging.WARNING, message, *args, **kwargs)
    
    def error(self, message: Union[str, LazyString, LazyFormat], *args, **kwargs):
    pass
        """Log error message with lazy evaluation."""
        self._log_with_timing(logging.ERROR, message, *args, **kwargs)
    
    def critical(self, message: Union[str, LazyString, LazyFormat], *args, **kwargs):
    pass
        """Log critical message with lazy evaluation."""
        self._log_with_timing(logging.CRITICAL, message, *args, **kwargs)
    
    def exception(self, message: Union[str, LazyString, LazyFormat], *args, **kwargs):
    pass
        """Log exception with lazy evaluation."""
        kwargs['exc_info'] = True
        self._log_with_timing(logging.ERROR, message, *args, **kwargs)
    
    def clear_cache(self):
    pass
    pass
        """Clear the level cache (useful when log levels change)."""
        with self._cache_lock:
    pass
            self._level_cache.clear()


# Global performance monitor instance
_global_monitor = PerformanceMonitor()


def get_performance_monitor() -> PerformanceMonitor:
    pass
    """Get the global performance monitor instance."""
    return _global_monitor


def lazy_string(func: Callable[[], str]) -> Callable[..., LazyString]:
    pass
    """
    Decorator to create lazy string functions.
    
    Args:
    pass
        func: Function that returns a string
        
    Returns:
    pass
        Decorated function that returns LazyString
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
    pass
        return LazyString(func, *args, **kwargs)
    return wrapper


def lazy_format(template: str) -> Callable[..., LazyFormat]:
    pass
    """
    Create a lazy format function for a template.
    
    Args:
    pass
        template: Format string template
        
    Returns:
    pass
        Function that creates LazyFormat instances
    """
    def formatter(*args, **kwargs):
    pass
        return LazyFormat(template, *args, **kwargs)
    return formatter


def optimize_logger(logger: logging.Logger, monitor: Optional[PerformanceMonitor] = None) -> OptimizedLogger:
    pass
    """
    Wrap a logger with performance optimizations.
    
    Args:
    pass
        logger: Logger to optimize
        monitor: Optional performance monitor
        
    Returns:
    pass
        OptimizedLogger instance
    """
    return OptimizedLogger(logger, monitor or _global_monitor)


# Convenience functions for common lazy logging patterns
def lazy_debug_format(template: str):
    pass
    """Create lazy format function optimized for debug logging."""
    return lazy_format(template)


def lazy_json_dump(obj: Any) -> LazyString:
    pass
    """Create lazy JSON serialization for logging."""
    import json
    return LazyString(lambda: json.dumps(obj, default=str, separators=(',', ':')))


def lazy_repr(obj: Any) -> LazyString:
    pass
    """Create lazy repr() for logging."""
    return LazyString(lambda: repr(obj))


def lazy_str_join(separator: str, items) -> LazyString:
    pass
    """Create lazy string join for logging."""
    return LazyString(lambda: separator.join(str(item) for item in items))


# Performance benchmarking utilities
class LoggingBenchmark:
    pass
    """Benchmark logging performance under different scenarios."""
    
    def __init__(self, logger: logging.Logger):
    pass
        self.logger = logger
        self.optimized_logger = optimize_logger(logger)
    
    def benchmark_regular_logging(self, iterations: int = 10000) -> Dict[str, float]:
    pass
        """Benchmark regular logging performance."""
        start_time = time.perf_counter()
        
        for i in range(iterations):
    pass
            self.logger.debug(f"Debug message {i} with data: {{'key': 'value', 'number': {i}}}")
        
        duration = time.perf_counter() - start_time
        return {
            'total_time_s': duration,
            'avg_time_ms': (duration / iterations) * 1000,
            'messages_per_second': iterations / duration
        }
    
    def benchmark_lazy_logging(self, iterations: int = 10000) -> Dict[str, float]:
    pass
        """Benchmark lazy logging performance."""
        start_time = time.perf_counter()
        
        for i in range(iterations):
    pass
            self.optimized_logger.debug(
                LazyFormat("Debug message {} with data: {}", i, {'key': 'value', 'number': i})
            )
        
        duration = time.perf_counter() - start_time
        return {
            'total_time_s': duration,
            'avg_time_ms': (duration / iterations) * 1000,
            'messages_per_second': iterations / duration
        }
    
    def benchmark_disabled_logging(self, iterations: int = 10000) -> Dict[str, float]:
    pass
        """Benchmark performance when logging is disabled."""
        # Temporarily disable debug logging
        original_level = self.logger.level
        self.logger.setLevel(logging.INFO)
        
        try:
    pass
            start_time = time.perf_counter()
            
            for i in range(iterations):
    pass
                self.optimized_logger.debug(
                    LazyFormat("Debug message {} with data: {}", i, {'key': 'value', 'number': i})
                )
            
            duration = time.perf_counter() - start_time
            return {
                'total_time_s': duration,
                'avg_time_ms': (duration / iterations) * 1000,
                'messages_per_second': iterations / duration
            }
        finally:
    pass
            self.logger.setLevel(original_level)
    
    def run_full_benchmark(self) -> Dict[str, Dict[str, float]]:
    pass
        """Run complete benchmark suite."""
        return {
            'regular_logging': self.benchmark_regular_logging(),
            'lazy_logging': self.benchmark_lazy_logging(),
            'disabled_logging': self.benchmark_disabled_logging()
        }