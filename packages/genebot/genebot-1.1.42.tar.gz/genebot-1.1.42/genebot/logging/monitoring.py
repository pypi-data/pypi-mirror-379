"""
Logging monitoring and alerting integration.

This module provides hooks for external monitoring systems, log aggregation
preparation, and log-based alerting capabilities.
"""

import json
import time
import threading
from abc import ABC, abstractmethod
from collections import defaultdict, deque
from dataclasses import dataclass, asdict
from enum import Enum
import logging

from .context import LogContext


class AlertSeverity(Enum):
    pass
    """Alert severity levels."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class AlertType(Enum):
    pass
    """Types of alerts that can be generated."""
    ERROR_RATE = "error_rate"
    PERFORMANCE_DEGRADATION = "performance_degradation"
    LOG_VOLUME = "log_volume"
    DISK_SPACE = "disk_space"
    HANDLER_FAILURE = "handler_failure"
    CONFIGURATION_ERROR = "configuration_error"
    SECURITY_VIOLATION = "security_violation"


@dataclass
class LogMetric:
    pass
    """Represents a log-based metric."""
    name: str
    value: float
    timestamp: datetime
    labels: Dict[str, str]
    unit: str = ""
    
    def to_dict(self) -> Dict[str, Any]:
    pass
        """Convert to dictionary for serialization."""
        return {
            'name': self.name,
            'value': self.value,
            'timestamp': self.timestamp.isoformat(),
            'labels': self.labels,
            'unit': self.unit
        }


@dataclass
class LogAlert:
    pass
    """Represents a log-based alert."""
    alert_type: AlertType
    severity: AlertSeverity
    message: str
    timestamp: datetime
    context: Optional[LogContext] = None
    metrics: Optional[Dict[str, float]] = None
    suggested_actions: Optional[List[str]] = None
    
    def to_dict(self) -> Dict[str, Any]:
    pass
        """Convert to dictionary for serialization."""
        return {
            'alert_type': self.alert_type.value,
            'severity': self.severity.value,
            'message': self.message,
            'timestamp': self.timestamp.isoformat(),
            'context': asdict(self.context) if self.context else None,
            'metrics': self.metrics or {},
            'suggested_actions': self.suggested_actions or []
        }


class MonitoringHook(ABC):
    pass
    """Abstract base class for monitoring system hooks."""
    
    @abstractmethod
    def send_metric(self, metric: LogMetric) -> None:
    pass
        """Send a metric to the monitoring system."""
    
    @abstractmethod
    def send_alert(self, alert: LogAlert) -> None:
    pass
        """Send an alert to the monitoring system."""
    
    @abstractmethod
    def is_healthy(self) -> bool:
    pass
        """Check if the monitoring system is healthy."""


class PrometheusHook(MonitoringHook):
    
        pass
    pass
    """Prometheus monitoring integration."""
    
    def __init__(self, gateway_url: str = "http://localhost:9091", job_name: str = "trading_bot"):
    pass
        """
        Initialize Prometheus hook.
        
        Args:
    pass
            gateway_url: Prometheus pushgateway URL
            job_name: Job name for metrics
        """
        self.gateway_url = gateway_url
        self.job_name = job_name
        self.metrics_buffer = []
        self.buffer_lock = threading.Lock()
        
    def send_metric(self, metric: LogMetric) -> None:
    pass
        """Send metric to Prometheus."""
        try:
    pass
            # Convert to Prometheus format
            prometheus_metric = self._convert_to_prometheus_format(metric)
            
            with self.buffer_lock:
    pass
                self.metrics_buffer.append(prometheus_metric)
                
            # Send buffered metrics periodically
            if len(self.metrics_buffer) >= 100:
    
        pass
    pass
                self._flush_metrics()
                
        except Exception as e:
    pass
    pass
            logging.getLogger(__name__).error(f"Failed to send metric to Prometheus: {e}")
    
    def send_alert(self, alert: LogAlert) -> None:
    pass
        """Send alert as Prometheus metric."""
        try:
    pass
            # Convert alert to metric
            alert_metric = LogMetric(
                name="log_alert",
                value=1.0,
                timestamp=alert.timestamp,
                labels={
                    "alert_type": alert.alert_type.value,
                    "severity": alert.severity.value,
                    "job": self.job_name
                }
            )
            
            self.send_metric(alert_metric)
            
        except Exception as e:
    pass
    pass
            logging.getLogger(__name__).error(f"Failed to send alert to Prometheus: {e}")
    
    def is_healthy(self) -> bool:
    pass
        """Check Prometheus gateway health."""
        try:
    pass
            import requests
            response = requests.get(f"{self.gateway_url}/metrics", timeout=5)
            return response.status_code == 200
        except Exception:
    pass
    pass
            return False
    
    def _convert_to_prometheus_format(self, metric: LogMetric) -> str:
    pass
        """Convert LogMetric to Prometheus format."""
        labels_str = ",".join([f'{k}="{v}"' for k, v in metric.labels.items()])
        if labels_str:
    
        pass
    pass
            labels_str = "{" + labels_str + "}"
        
        return f"{metric.name}{labels_str} {metric.value} {int(metric.timestamp.timestamp() * 1000)}"
    
    def _flush_metrics(self) -> None:
    pass
        """Flush buffered metrics to Prometheus."""
        try:
    pass
            import requests
            
            with self.buffer_lock:
    pass
                if not self.metrics_buffer:
    
        pass
    pass
                    return
                
                metrics_data = "\n".join(self.metrics_buffer)
                self.metrics_buffer.clear()
            
            # Send to pushgateway
            url = f"{self.gateway_url}/metrics/job/{self.job_name}"
            response = requests.post(
                url,
                data=metrics_data,
                headers={'Content-Type': 'text/plain'},
                timeout=10
            )
            
            if response.status_code != 200:
    
        pass
    pass
                logging.getLogger(__name__).warning(
                    f"Failed to push metrics to Prometheus: {response.status_code}"
                )
                
        except Exception as e:
    pass
    pass
            logging.getLogger(__name__).error(f"Failed to flush metrics to Prometheus: {e}")


class DatadogHook(MonitoringHook):
    pass
    """Datadog monitoring integration."""
    
    def __init__(self, api_key: str, app_key: str = None):
    pass
        """
        Initialize Datadog hook.
        
        Args:
    pass
            api_key: Datadog API key
            app_key: Datadog application key (optional)
        """
        self.api_key = api_key
        self.app_key = app_key
        self.metrics_buffer = []
        self.buffer_lock = threading.Lock()
    
    def send_metric(self, metric: LogMetric) -> None:
    pass
        """Send metric to Datadog."""
        try:
    pass
            datadog_metric = {
                'metric': metric.name,
                'points': [[int(metric.timestamp.timestamp()), metric.value]],
                'tags': [f"{k}:{v}" for k, v in metric.labels.items()],
                'type': 'gauge'
            }
            
            with self.buffer_lock:
    pass
                self.metrics_buffer.append(datadog_metric)
            
            if len(self.metrics_buffer) >= 100:
    
        pass
    pass
                self._flush_metrics()
                
        except Exception as e:
    pass
    pass
            logging.getLogger(__name__).error(f"Failed to send metric to Datadog: {e}")
    
    def send_alert(self, alert: LogAlert) -> None:
    pass
        """Send alert to Datadog."""
        try:
    pass
            # Send as event
            event_data = {
                'title': f"Log Alert: {alert.alert_type.value}",
                'text': alert.message,
                'alert_type': alert.severity.value,
                'tags': [
                    f"alert_type:{alert.alert_type.value}",
                    f"severity:{alert.severity.value}"
                ],
                'date_happened': int(alert.timestamp.timestamp())
            }
            
            self._send_event(event_data)
            
        except Exception as e:
    pass
    pass
            logging.getLogger(__name__).error(f"Failed to send alert to Datadog: {e}")
    
    def is_healthy(self) -> bool:
    pass
        """Check Datadog API health."""
        try:
    pass
            import requests
            
            headers = {
                'Content-Type': 'application/json'
            }
            
            response = requests.get(
                'https://api.datadoghq.com/api/v1/validate',
                headers=headers,
                timeout=5
            )
            
            return response.status_code == 200
            
        except Exception:
    pass
    pass
            return False
    
    def _flush_metrics(self) -> None:
    pass
        """Flush buffered metrics to Datadog."""
        try:
    pass
            import requests
            
            with self.buffer_lock:
    pass
                if not self.metrics_buffer:
    
        pass
    pass
                    return
                
                metrics_data = {'series': self.metrics_buffer.copy()}
                self.metrics_buffer.clear()
            
            headers = {
                'DD-API-KEY': self.api_key,
                'Content-Type': 'application/json'
            }
            
            response = requests.post(
                'https://api.datadoghq.com/api/v1/series',
                json=metrics_data,
                headers=headers,
                timeout=10
            )
            
            if response.status_code != 202:
    
        pass
    pass
                logging.getLogger(__name__).warning(
                    f"Failed to send metrics to Datadog: {response.status_code}"
                )
                
        except Exception as e:
    pass
    pass
            logging.getLogger(__name__).error(f"Failed to flush metrics to Datadog: {e}")
    
    def _send_event(self, event_data: Dict[str, Any]) -> None:
    pass
        """Send event to Datadog."""
        try:
    pass
            import requests
            
            headers = {
                'Content-Type': 'application/json'
            }
            
            response = requests.post(
                'https://api.datadoghq.com/api/v1/events',
                json=event_data,
                headers=headers,
                timeout=10
            )
            
            if response.status_code not in [200, 202]:
    
        pass
    pass
                logging.getLogger(__name__).warning(
                    f"Failed to send event to Datadog: {response.status_code}"
                )
                
        except Exception as e:
    pass
    pass
            logging.getLogger(__name__).error(f"Failed to send event to Datadog: {e}")


class SlackHook(MonitoringHook):
    pass
    """Slack alerting integration."""
    
    def __init__(self, webhook_url: str, channel: str = None):
    pass
        """
        Initialize Slack hook.
        
        Args:
    pass
            webhook_url: Slack webhook URL
            channel: Slack channel (optional)
        """
        self.webhook_url = webhook_url
        self.channel = channel
    
    def send_metric(self, metric: LogMetric) -> None:
    pass
        """Metrics are not sent to Slack (use for alerts only)."""
    
    def send_alert(self, alert: LogAlert) -> None:
    pass
        """Send alert to Slack."""
        try:
    pass
            color_map = {
                AlertSeverity.LOW: "good",
                AlertSeverity.MEDIUM: "warning",
                AlertSeverity.HIGH: "danger",
                AlertSeverity.CRITICAL: "danger"
            }
            
            attachment = {
                "color": color_map.get(alert.severity, "warning"),
                "title": f"🚨 {alert.alert_type.value.replace('_', ' ').title()}",
                "text": alert.message,
                "fields": [
                    {
                        "title": "Severity",
                        "value": alert.severity.value.upper(),
                        "short": True
                    },
                    {
                        "title": "Time",
                        "value": alert.timestamp.strftime("%Y-%m-%d %H:%M:%S UTC"),
                        "short": True
                    }
                ],
                "footer": "Trading Bot Logging System",
                "ts": int(alert.timestamp.timestamp())
            }
            
            if alert.context:
    
        pass
    pass
                attachment["fields"].extend([
                    {
                        "title": "Component",
                        "value": alert.context.component,
                        "short": True
                    },
                    {
                        "title": "Operation",
                        "value": alert.context.operation,
                        "short": True
                    }
                ])
            
            if alert.suggested_actions:
    
        pass
    pass
                attachment["fields"].append({
                    "title": "Suggested Actions",
                    "value": "\n".join([f"• {action}" for action in alert.suggested_actions]),
                    "short": False
                })
            
            payload = {
                "attachments": [attachment]
            }
            
            if self.channel:
    
        pass
    pass
                payload["channel"] = self.channel
            
            self._send_to_slack(payload)
            
        except Exception as e:
    pass
    pass
            logging.getLogger(__name__).error(f"Failed to send alert to Slack: {e}")
    
    def is_healthy(self) -> bool:
    pass
        """Check Slack webhook health."""
        try:
    pass
            import requests
            
            # Send a test payload
            test_payload = {"text": "Health check"}
            response = requests.post(
                json=test_payload,
                timeout=5
            )
            
            return response.status_code == 200
            
        except Exception:
    pass
    pass
            return False
    
    def _send_to_slack(self, payload: Dict[str, Any]) -> None:
    pass
        """Send payload to Slack."""
        try:
    pass
            import requests
            
            response = requests.post(
                json=payload,
                timeout=10
            )
            
            if response.status_code != 200:
    
        pass
    pass
                logging.getLogger(__name__).warning(
                    f"Failed to send message to Slack: {response.status_code}"
                )
                
        except Exception as e:
    pass
    pass
            logging.getLogger(__name__).error(f"Failed to send to Slack: {e}")


class LogAggregationHook(MonitoringHook):
    pass
    """Hook for log aggregation systems (ELK, Fluentd, etc.)."""
    
    def __init__(self, endpoint_url: str, index_name: str = "trading-bot-logs"):
    pass
        """
        Initialize log aggregation hook.
        
        Args:
    pass
            endpoint_url: Aggregation system endpoint
            index_name: Index/collection name
        """
        self.endpoint_url = endpoint_url
        self.index_name = index_name
        self.log_buffer = []
        self.buffer_lock = threading.Lock()
    
    def send_metric(self, metric: LogMetric) -> None:
    pass
        """Send metric to aggregation system."""
        try:
    pass
            log_entry = {
                'type': 'metric',
                'data': metric.to_dict(),
                'index': self.index_name,
                'timestamp': metric.timestamp.isoformat()
            }
            
            with self.buffer_lock:
    pass
                self.log_buffer.append(log_entry)
            
            if len(self.log_buffer) >= 100:
    
        pass
    pass
                self._flush_logs()
                
        except Exception as e:
    pass
    pass
            logging.getLogger(__name__).error(f"Failed to send metric to aggregation system: {e}")
    
    def send_alert(self, alert: LogAlert) -> None:
    pass
        """Send alert to aggregation system."""
        try:
    pass
            log_entry = {
                'type': 'alert',
                'data': alert.to_dict(),
                'index': self.index_name,
                'timestamp': alert.timestamp.isoformat()
            }
            
            with self.buffer_lock:
    pass
                self.log_buffer.append(log_entry)
            
            # Flush immediately for alerts
            self._flush_logs()
            
        except Exception as e:
    pass
    pass
            logging.getLogger(__name__).error(f"Failed to send alert to aggregation system: {e}")
    
    def is_healthy(self) -> bool:
    pass
        """Check aggregation system health."""
        try:
    pass
            import requests
            
            response = requests.get(
                timeout=5
            
            return response.status_code == 200
            
        except Exception:
    pass
    pass
            return False
    
    def _flush_logs(self) -> None:
    pass
        """Flush buffered logs to aggregation system."""
        try:
    pass
            import requests
            
            with self.buffer_lock:
    pass
                if not self.log_buffer:
    
        pass
    pass
                    return
                
                logs_data = self.log_buffer.copy()
                self.log_buffer.clear()
            
            # Send bulk data
            bulk_data = []
            for log_entry in logs_data:
    pass
                # Elasticsearch bulk format
                action = {"index": {"_index": log_entry['index']}}
                bulk_data.append(json.dumps(action))
                bulk_data.append(json.dumps(log_entry))
            
            bulk_payload = "\n".join(bulk_data) + "\n"
            
            response = requests.post(
                f"{self.endpoint_url}/_bulk",
                data=bulk_payload,
                headers={'Content-Type': 'application/x-ndjson'},
                timeout=30
            )
            
            if response.status_code not in [200, 201]:
    
        pass
    pass
                logging.getLogger(__name__).warning(
                    f"Failed to send logs to aggregation system: {response.status_code}"
                )
                
        except Exception as e:
    pass
    pass
            logging.getLogger(__name__).error(f"Failed to flush logs to aggregation system: {e}")


class LogMonitor:
    pass
    """Main log monitoring and alerting coordinator."""
    
    def __init__(self):
    pass
        """Initialize log monitor."""
        self.hooks: List[MonitoringHook] = []
        self.alert_rules: List[Callable[[Dict[str, Any]], Optional[LogAlert]]] = []
        self.metrics_collectors: List[Callable[[], List[LogMetric]]] = []
        
        # Statistics tracking
        self.log_stats = defaultdict(lambda: defaultdict(int))
        self.error_rates = defaultdict(lambda: deque(maxlen=100))
        self.performance_metrics = defaultdict(lambda: deque(maxlen=100))
        
        # Monitoring thread
        self.monitoring_thread = None
        self.monitoring_active = False
        self.stats_lock = threading.Lock()
    
    def add_hook(self, hook: MonitoringHook) -> None:
    pass
        """Add a monitoring hook."""
        self.hooks.append(hook)
    
    def add_alert_rule(self, rule: Callable[[Dict[str, Any]], Optional[LogAlert]]) -> None:
    pass
        """Add an alert rule."""
        self.alert_rules.append(rule)
    
    def add_metrics_collector(self, collector: Callable[[], List[LogMetric]]) -> None:
    pass
        """Add a metrics collector."""
        self.metrics_collectors.append(collector)
    
    def start_monitoring(self, interval: float = 60.0) -> None:
    pass
        """Start the monitoring thread."""
        if self.monitoring_active:
    
        pass
    pass
            return
        
        self.monitoring_active = True
        self.monitoring_thread = threading.Thread(
            target=self._monitoring_loop,
            args=(interval,),
            daemon=True,
            name="LogMonitor"
        )
        self.monitoring_thread.start()
    
    def stop_monitoring(self) -> None:
    pass
        """Stop the monitoring thread."""
        self.monitoring_active = False
        if self.monitoring_thread:
    
        pass
    pass
            self.monitoring_thread.join(timeout=5.0)
    
    def record_log_event(self, level: str, logger_name: str, context: Optional[LogContext] = None) -> None:
    pass
        """Record a log event for monitoring."""
        with self.stats_lock:
    pass
            self.log_stats[logger_name][level] += 1
            self.log_stats['_total'][level] += 1
            
            # Track error rates
            if level in ['ERROR', 'CRITICAL']:
    
        pass
    pass
                self.error_rates[logger_name].append(time.time())
    
    def record_performance_metric(self, operation: str, duration: float, context: Optional[LogContext] = None) -> None:
    pass
        """Record a performance metric."""
        with self.stats_lock:
    pass
            self.performance_metrics[operation].append({
                'duration': duration,
                'timestamp': time.time(),
                'context': context
            })
    
    def send_metric(self, metric: LogMetric) -> None:
    pass
        """Send metric to all hooks."""
        for hook in self.hooks:
    pass
            try:
    pass
                hook.send_metric(metric)
            except Exception as e:
    pass
    pass
                logging.getLogger(__name__).error(f"Hook {type(hook).__name__} failed to send metric: {e}")
    
    def send_alert(self, alert: LogAlert) -> None:
    pass
        """Send alert to all hooks."""
        for hook in self.hooks:
    pass
            try:
    pass
                hook.send_alert(alert)
            except Exception as e:
    pass
    pass
                logging.getLogger(__name__).error(f"Hook {type(hook).__name__} failed to send alert: {e}")
    
    def _monitoring_loop(self, interval: float) -> None:
    pass
        """Main monitoring loop."""
        while self.monitoring_active:
    pass
            try:
    pass
                # Collect metrics
                self._collect_metrics()
                
                # Check alert rules
                self._check_alert_rules()
                
                # Sleep until next iteration
                time.sleep(interval)
                
            except Exception as e:
    pass
    pass
                logging.getLogger(__name__).error(f"Error in monitoring loop: {e}")
                time.sleep(interval)
    
    def _collect_metrics(self) -> None:
    pass
        """Collect and send metrics."""
        try:
    pass
            # Collect built-in metrics
            metrics = self._get_builtin_metrics()
            
            # Collect custom metrics
            for collector in self.metrics_collectors:
    pass
                try:
    pass
                    custom_metrics = collector()
                    metrics.extend(custom_metrics)
                except Exception as e:
    pass
    pass
                    logging.getLogger(__name__).error(f"Metrics collector failed: {e}")
            
            # Send all metrics
            for metric in metrics:
    pass
                self.send_metric(metric)
                
        except Exception as e:
    pass
    pass
            logging.getLogger(__name__).error(f"Failed to collect metrics: {e}")
    
    def _get_builtin_metrics(self) -> List[LogMetric]:
    pass
        """Get built-in log metrics."""
        metrics = []
        now = datetime.now()
        
        with self.stats_lock:
    pass
            # Log level metrics
            for logger_name, level_stats in self.log_stats.items():
    pass
                for level, count in level_stats.items():
    pass
                    metrics.append(LogMetric(
                        name="log_messages_total",
                        value=float(count),
                        timestamp=now,
                        labels={
                            "logger": logger_name,
                            "level": level
                        },
                        unit="count"
                    ))
            
            # Error rate metrics
            for logger_name, error_times in self.error_rates.items():
    pass
                if error_times:
    
        pass
    pass
                    # Calculate error rate per minute
                    recent_errors = [t for t in error_times if time.time() - t < 60]
                    error_rate = len(recent_errors)
                    
                    metrics.append(LogMetric(
                        name="log_error_rate",
                        value=float(error_rate),
                        timestamp=now,
                        labels={"logger": logger_name},
                        unit="errors_per_minute"
                    ))
            
            # Performance metrics
            for operation, perf_data in self.performance_metrics.items():
    pass
                if perf_data:
    
        pass
    pass
                    recent_data = [d for d in perf_data if time.time() - d['timestamp'] < 300]  # 5 minutes
                    if recent_data:
    
        pass
    pass
                        durations = [d['duration'] for d in recent_data]
                        avg_duration = sum(durations) / len(durations)
                        max_duration = max(durations)
                        
                        metrics.append(LogMetric(
                            name="log_operation_duration_avg",
                            value=avg_duration,
                            timestamp=now,
                            labels={"operation": operation},
                            unit="seconds"
                        ))
                        
                        metrics.append(LogMetric(
                            name="log_operation_duration_max",
                            value=max_duration,
                            timestamp=now,
                            labels={"operation": operation},
                            unit="seconds"
                        ))
        
        return metrics
    
    def _check_alert_rules(self) -> None:
    pass
        """Check all alert rules and send alerts if triggered."""
        try:
    
        pass
    pass
            # Prepare statistics for alert rules
            with self.stats_lock:
    pass
                stats = {
                    'log_stats': dict(self.log_stats),
                    'error_rates': dict(self.error_rates),
                    'performance_metrics': dict(self.performance_metrics),
                    'timestamp': time.time()
                }
            
            # Check each alert rule
            for rule in self.alert_rules:
    pass
                try:
    pass
                    alert = rule(stats)
                    if alert:
    
        pass
    pass
                        self.send_alert(alert)
                except Exception as e:
    pass
    pass
                    logging.getLogger(__name__).error(f"Alert rule failed: {e}")
                    
        except Exception as e:
    pass
    pass
            logging.getLogger(__name__).error(f"Failed to check alert rules: {e}")


# Built-in alert rules
def high_error_rate_rule(stats: Dict[str, Any]) -> Optional[LogAlert]:
    pass
    """Alert rule for high error rates."""
    error_rates = stats.get('error_rates', {})
    current_time = stats.get('timestamp', time.time())
    
    for logger_name, error_times in error_rates.items():
    pass
        if not error_times:
    
        pass
    pass
            continue
        
        # Check error rate in last 5 minutes
        recent_errors = [t for t in error_times if current_time - t < 300]
        error_rate = len(recent_errors) / 5.0  # errors per minute
        
        if error_rate > 10:  # More than 10 errors per minute
            return LogAlert(
                alert_type=AlertType.ERROR_RATE,
                severity=AlertSeverity.HIGH if error_rate > 20 else AlertSeverity.MEDIUM,
                message=f"High error rate detected: {error_rate:.1f} errors/min in {logger_name}",
                timestamp=datetime.now(),
                metrics={"error_rate": error_rate},
                suggested_actions=[
                    "Check application logs for error details",
                    "Verify system resources and dependencies",
                    "Consider reducing log level temporarily"
                ]
            )
    
    return None


def performance_degradation_rule(stats: Dict[str, Any]) -> Optional[LogAlert]:
    pass
    """Alert rule for performance degradation."""
    performance_metrics = stats.get('performance_metrics', {})
    current_time = stats.get('timestamp', time.time())
    
    for operation, perf_data in performance_metrics.items():
    pass
        if not perf_data:
    
        pass
    pass
            continue
        
        # Check recent performance
        recent_data = [d for d in perf_data if current_time - d['timestamp'] < 300]
        if len(recent_data) < 10:  # Need enough samples
            continue
        
        durations = [d['duration'] for d in recent_data]
        avg_duration = sum(durations) / len(durations)
        max_duration = max(durations)
        
        # Alert if average duration > 1 second or max > 5 seconds
        if avg_duration > 1.0 or max_duration > 5.0:
    
        pass
    pass
            severity = AlertSeverity.CRITICAL if max_duration > 10.0 else AlertSeverity.HIGH
            
            return LogAlert(
                alert_type=AlertType.PERFORMANCE_DEGRADATION,
                severity=severity,
                message=f"Performance degradation in {operation}: avg={avg_duration:.2f}s, max={max_duration:.2f}s",
                timestamp=datetime.now(),
                metrics={
                    "avg_duration": avg_duration,
                    "max_duration": max_duration,
                    "sample_count": len(recent_data)
                },
                suggested_actions=[
                    "Check system resources (CPU, memory, disk)",
                    "Review recent code changes",
                    "Consider enabling async logging",
                    "Reduce log verbosity temporarily"
                ]
            )
    
    return None


def log_volume_rule(stats: Dict[str, Any]) -> Optional[LogAlert]:
    pass
    """Alert rule for excessive log volume."""
    log_stats = stats.get('log_stats', {})
    
    total_logs = sum(sum(level_stats.values()) for level_stats in log_stats.values())
    
    # Alert if more than 100,000 log messages in monitoring period
    if total_logs > 100000:
    
        pass
    pass
        return LogAlert(
            alert_type=AlertType.LOG_VOLUME,
            severity=AlertSeverity.MEDIUM,
            message=f"High log volume detected: {total_logs} messages",
            timestamp=datetime.now(),
            metrics={"total_messages": total_logs},
            suggested_actions=[
                "Review log levels and reduce verbosity",
                "Check for log loops or excessive debug logging",
                "Consider log sampling for high-frequency events",
                "Verify log rotation is working properly"
            ]
        )
    
    return None


# Global monitor instance
_global_monitor: Optional[LogMonitor] = None


def get_global_monitor() -> LogMonitor:
    pass
    """Get the global log monitor instance."""
    global _global_monitor
    if _global_monitor is None:
    
        pass
    pass
        _global_monitor = LogMonitor()
        
        # Add default alert rules
        _global_monitor.add_alert_rule(high_error_rate_rule)
        _global_monitor.add_alert_rule(performance_degradation_rule)
        _global_monitor.add_alert_rule(log_volume_rule)
    
    return _global_monitor


def setup_monitoring_hooks(config: Dict[str, Any]) -> None:
    pass
    """Set up monitoring hooks based on configuration."""
    monitor = get_global_monitor()
    
    # Prometheus hook
    if config.get('prometheus', {}).get('enabled', False):
    
        pass
    pass
        prometheus_config = config['prometheus']
        hook = PrometheusHook(
            gateway_url=prometheus_config.get('gateway_url', 'http://localhost:9091'),
            job_name=prometheus_config.get('job_name', 'trading_bot')
        )
        monitor.add_hook(hook)
    
    # Datadog hook
    if config.get('datadog', {}).get('enabled', False):
    
        pass
    pass
        datadog_config = config['datadog']
        hook = DatadogHook(
            api_key=datadog_config['api_key'],
            app_key=datadog_config.get('app_key')
        )
        monitor.add_hook(hook)
    
    # Slack hook
    if config.get('slack', {}).get('enabled', False):
    
        pass
    pass
        slack_config = config['slack']
        hook = SlackHook(
            webhook_url=slack_config['webhook_url'],
            channel=slack_config.get('channel')
        )
        monitor.add_hook(hook)
    
    # Log aggregation hook
    if config.get('log_aggregation', {}).get('enabled', False):
    
        pass
    pass
        aggregation_config = config['log_aggregation']
        hook = LogAggregationHook(
            endpoint_url=aggregation_config['endpoint_url'],
            index_name=aggregation_config.get('index_name', 'trading-bot-logs')
        )
        monitor.add_hook(hook)
    
    # Start monitoring
    monitor.start_monitoring(interval=config.get('monitoring_interval', 60.0))