"""
Process Manager for Trading Bot Lifecycle Management
==================================================

This module provides comprehensive process management capabilities for the trading bot,
including process launching, monitoring, PID file management, and graceful shutdown.
"""

import os
import sys
import time
import psutil
import subprocess
import threading
from pathlib import Path
from typing import Optional, Dict, Any, List, Callable
from datetime import datetime, timedelta
from dataclasses import dataclass, field
import logging
import json
from enum import Enum
from collections import deque

# Integration manager will be imported when needed to avoid circular imports


class ProcessError(Exception):
    
        pass
    pass
    """Exception raised for process management errors"""
    
    def __init__(self, message: str, suggestions: list[str] = None):
    pass
        super().__init__(message)
        self.message = message
        self.suggestions = suggestions or []


class ProcessState(Enum):
    pass
    """Process state enumeration"""
    STOPPED = "stopped"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
    CRASHED = "crashed"
    RECOVERING = "recovering"


@dataclass
class ProcessInfo:
    pass
    """Information about a running process"""
    pid: int
    name: str
    status: str
    cpu_percent: float
    memory_percent: float
    memory_mb: float
    create_time: datetime
    uptime: timedelta
    command_line: List[str]
    threads: int = 0
    open_files: int = 0
    connections: int = 0


@dataclass
class BotStatus:
    pass
    """Bot process status information"""
    running: bool
    state: ProcessState = ProcessState.STOPPED
    pid: Optional[int] = None
    uptime: Optional[timedelta] = None
    memory_usage: Optional[float] = None
    cpu_usage: Optional[float] = None
    last_activity: Optional[datetime] = None
    process_info: Optional[ProcessInfo] = None
    error_message: Optional[str] = None
    restart_count: int = 0
    last_restart: Optional[datetime] = None


@dataclass
class ProcessMetrics:
    pass
    """Process performance metrics over time"""
    timestamp: datetime
    cpu_percent: float
    memory_mb: float
    memory_percent: float
    threads: int
    open_files: int
    connections: int


@dataclass
class RecoveryConfig:
    pass
    """Configuration for automatic recovery"""
    enabled: bool = True
    max_restarts: int = 5
    restart_delay: int = 30  # seconds
    memory_threshold_mb: float = 1000.0  # MB
    cpu_threshold_percent: float = 90.0  # %
    health_check_interval: int = 60  # seconds
    crash_detection_enabled: bool = True
    auto_restart_on_crash: bool = True


@dataclass
class BotInstance:
    pass
    """Information about a bot instance"""
    name: str
    pid: Optional[int] = None
    config_file: Optional[str] = None
    strategies: List[str] = field(default_factory=list)
    accounts: List[str] = field(default_factory=list)
    status: BotStatus = field(default_factory=lambda: BotStatus(running=False))
    metrics_history: deque = field(default_factory=lambda: deque(maxlen=100))
    log_file: Optional[Path] = None
    pid_file: Optional[Path] = None


class ProcessManager:
    pass
    """
    Advanced trading bot process lifecycle manager with monitoring,
    recovery, and multi-instance support.
    """
    
    def __init__(self, workspace_path: Optional[Path] = None):
    pass
        """
        Initialize ProcessManager
        
        Args:
    pass
            workspace_path: Path to the workspace directory
        """
        self.workspace_path = workspace_path or Path.cwd()
        self.pid_dir = self.workspace_path / "logs"
        self.pid_file = self.pid_dir / "genebot.pid"
        self.log_dir = self.workspace_path / "logs"
        self.instances_dir = self.pid_dir / "instances"
        
        # Ensure directories exist
        self.pid_dir.mkdir(exist_ok=True)
        self.log_dir.mkdir(exist_ok=True)
        self.instances_dir.mkdir(exist_ok=True)
        
        self.logger = logging.getLogger(__name__)
        
        # Advanced features
        self.recovery_config = RecoveryConfig()
        self.instances: Dict[str, BotInstance] = {}
        self.monitoring_active = False
        self.monitoring_thread: Optional[threading.Thread] = None
        self.recovery_callbacks: List[Callable] = []
        
        # Load existing instances
        self._load_instances()
    
    def start_bot(self, config_file: Optional[str] = None, 
                  strategies: Optional[List[str]] = None,
                  accounts: Optional[List[str]] = None,
                  background: bool = True) -> BotStatus:
    pass
        """
        Start the default trading bot process (legacy method)
        
        Args:
    pass
            config_file: Path to configuration file
            strategies: List of strategies to enable
            accounts: List of accounts to use
            background: Whether to run in background
            
        Returns:
    pass
            BotStatus with process information
            
        Raises:
    pass
            ProcessError: If bot cannot be started
        """
        status = self.start_bot_instance(
            "default",
            config_file=config_file,
            strategies=strategies,
            accounts=accounts,
            background=background
        )
        
        # For legacy compatibility, also create the old PID file
        if status.running and "default" in self.instances:
    
        pass
    pass
            instance = self.instances["default"]
            if instance.pid:
    
        pass
    pass
                try:
    pass
                    # Create legacy PID file
                    cmd = self._build_start_command(config_file, strategies, accounts)
                    log_file = instance.log_file or self.log_dir / f"genebot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
                    self._create_pid_file(instance.pid, cmd, log_file)
                except Exception as e:
    pass
    pass
                    self.logger.warning(f"Failed to create legacy PID file: {e}")
        
        return status
    
    def stop_bot(self, timeout: int = 60, force: bool = False) -> BotStatus:
    pass
        """
        Stop the default trading bot process (legacy method)
        
        Args:
    pass
            timeout: Seconds to wait for graceful shutdown
            force: Whether to force kill if graceful shutdown fails
            
        Returns:
    
        pass
    pass
            BotStatus after shutdown attempt
            
        Raises:
    pass
            ProcessError: If bot cannot be stopped
        """
        if "default" not in self.instances:
    
        pass
    pass
            # Check legacy PID file
            if self.pid_file.exists():
    
        pass
    pass
                pid_info = self._read_pid_file()
                if pid_info and pid_info.get('pid'):
    
        pass
    pass
                    # Migrate to instance system
                    self.instances["default"] = BotInstance(
                        name="default",
                        pid=pid_info['pid'],
                        pid_file=self.pid_file
                    )
                    self.instances["default"].status.running = True
                    self.instances["default"].status.pid = pid_info['pid']
        
        if "default" in self.instances:
    
        pass
    pass
            return self.stop_bot_instance("default", timeout=timeout, force=force)
        else:
    pass
            return BotStatus(running=False)
    
    def restart_bot(self, timeout: int = 60, **start_kwargs) -> BotStatus:
    pass
        """
        Restart the default trading bot (legacy method)
        
        Args:
    pass
            timeout: Timeout for stop operation
            **start_kwargs: Arguments passed to start_bot
            
        Returns:
    pass
            BotStatus after restart
        """
        # Check if default instance exists, if not create it
        if "default" not in self.instances:
    
        pass
    pass
            # Check for legacy PID file
            if self.pid_file.exists():
    
        pass
    pass
                pid_info = self._read_pid_file()
                if pid_info and pid_info.get('pid'):
    
        pass
    pass
                    # Migrate to instance system
                    self.instances["default"] = BotInstance(
                        name="default",
                        pid=pid_info['pid'],
                        pid_file=self.pid_file
                    )
                    self.instances["default"].status.running = True
                    self.instances["default"].status.pid = pid_info['pid']
            else:
    pass
                # No existing bot, just start a new one
                return self.start_bot(**start_kwargs)
        
        return self.restart_bot_instance("default", timeout=timeout, **start_kwargs)
    
    def get_bot_status(self) -> BotStatus:
    pass
        """
        Get current default bot status (legacy method)
        
        Returns:
    pass
            BotStatus with current information
        """
        # Check if default instance exists
        if "default" in self.instances:
    
        pass
    pass
            return self.get_instance_status("default")
        
        # Check legacy PID file
        try:
    pass
            if not self.pid_file.exists():
    
        pass
    pass
                return BotStatus(running=False)
            
            pid_info = self._read_pid_file()
            if not pid_info:
    
        pass
    pass
                return BotStatus(running=False)
            
            pid = pid_info['pid']
            
            # Check if process exists and is running
            try:
    
        pass
    pass
                process_info = self._get_process_info(pid)
                if not process_info:
    
        pass
    pass
                    # Process doesn't exist, cleanup PID file
                    self._cleanup_pid_file()
                    return BotStatus(running=False)
                
                # Migrate to instance system
                self.instances["default"] = BotInstance(
                    name="default",
                    pid=pid,
                    pid_file=self.pid_file
                )
                self.instances["default"].status.running = True
                self.instances["default"].status.pid = pid
                self.instances["default"].status.process_info = process_info
                self.instances["default"].status.memory_usage = process_info.memory_mb
                self.instances["default"].status.cpu_usage = process_info.cpu_percent
                self.instances["default"].status.uptime = process_info.uptime
                self.instances["default"].status.last_activity = datetime.now()
                
                return self.instances["default"].status
                
            except Exception as e:
    pass
    pass
                self.logger.warning(f"Error checking process {pid}: {e}")
                return BotStatus(
                    running=False,
                    error_message=f"Error checking process: {str(e)}"
                )
                
        except Exception as e:
    pass
    pass
            self.logger.error(f"Error getting bot status: {e}")
            return BotStatus(
                running=False,
                error_message=f"Error getting status: {str(e)}"
            )
    
    def monitor_health(self) -> Dict[str, Any]:
    pass
        """
        Monitor bot health and return detailed information
        
        Returns:
    pass
            Dictionary with health information
        """
        status = self.get_bot_status()
        
        health_info = {
            'timestamp': datetime.now().isoformat(),
            'running': status.running,
            'healthy': status.running and not status.error_message,
            'pid': status.pid,
            'uptime_seconds': status.uptime.total_seconds() if status.uptime else None,
            'memory_mb': status.memory_usage,
            'cpu_percent': status.cpu_usage,
            'error_message': status.error_message
        }
        
        if status.process_info:
    
        pass
    pass
            health_info.update({
                'process_name': status.process_info.name,
                'process_status': status.process_info.status,
                'command_line': status.process_info.command_line
            })
        
        return health_info
    
    def _build_start_command(self, config_file: Optional[str] = None,
                           strategies: Optional[List[str]] = None,
                           accounts: Optional[List[str]] = None) -> List[str]:
    pass
        """Build command line for starting the bot"""
        # Use the installed genebot package's trading bot runner instead of main.py
        # This ensures the bot runs from the packaged build, not from workspace files
        cmd = [sys.executable, "-m", "genebot.core.runner"]
        
        # Set workspace path as environment variable so the runner knows where to find config
        if not hasattr(self, '_env_vars'):
    
        pass
    pass
            self._env_vars = {}
        self._env_vars['GENEBOT_WORKSPACE'] = str(self.workspace_path)
        
        if config_file:
    
        pass
    pass
            cmd.extend(["--config", config_file])
        
        if strategies:
    
        pass
    pass
            cmd.extend(["--strategies"] + strategies)
        
        if accounts:
    
        pass
    pass
            cmd.extend(["--accounts"] + accounts)
        
        return cmd
    
    def _create_pid_file(self, pid: int, command: List[str], log_file: Path) -> None:
    pass
        """Create PID file with process information"""
        pid_data = {
            'pid': pid,
            'command': command,
            'log_file': str(log_file),
            'start_time': datetime.now().isoformat(),
            'workspace': str(self.workspace_path)
        }
        
        try:
    pass
            with open(self.pid_file, 'w') as f:
    pass
                json.dump(pid_data, f, indent=2)
            self.logger.debug(f"Created PID file: {self.pid_file}")
        except Exception as e:
    pass
    pass
            self.logger.error(f"Failed to create PID file: {e}")
            raise ProcessError(f"Failed to create PID file: {str(e)}")
    
    def _read_pid_file(self) -> Optional[Dict[str, Any]]:
    pass
        """Read PID file and return process information"""
        try:
    pass
            if not self.pid_file.exists():
    
        pass
    pass
                return None
            
            with open(self.pid_file, 'r') as f:
    pass
                return json.load(f)
        except Exception as e:
    pass
    pass
            self.logger.warning(f"Failed to read PID file: {e}")
            return None
    
    def _cleanup_pid_file(self) -> None:
    pass
        """Remove PID file"""
        try:
    pass
            if self.pid_file.exists():
    
        pass
    pass
                self.pid_file.unlink()
                self.logger.debug(f"Removed PID file: {self.pid_file}")
        except Exception as e:
    pass
    pass
            self.logger.warning(f"Failed to remove PID file: {e}")
    
    def _get_process_info(self, pid: int) -> Optional[ProcessInfo]:
    pass
        """Get detailed process information"""
        try:
    pass
            process = psutil.Process(pid)
            
            # Check if process exists and is running
            if not process.is_running():
    
        pass
    pass
                return None
            
            # Get process information
            create_time = datetime.fromtimestamp(process.create_time())
            uptime = datetime.now() - create_time
            
            # Get resource usage
            try:
    pass
                cpu_percent = process.cpu_percent()
                memory_info = process.memory_info()
                memory_percent = process.memory_percent()
                memory_mb = memory_info.rss / 1024 / 1024  # Convert to MB
            except (psutil.AccessDenied, psutil.NoSuchProcess):
    pass
    pass
                cpu_percent = 0.0
                memory_percent = 0.0
                memory_mb = 0.0
            
            # Get additional metrics
            try:
    pass
                threads = process.num_threads()
            except (psutil.AccessDenied, psutil.NoSuchProcess):
    pass
    pass
                threads = 0
            
            try:
    pass
                open_files_list = process.open_files()
                open_files = len(open_files_list) if open_files_list else 0
            except (psutil.AccessDenied, psutil.NoSuchProcess, TypeError):
    
        pass
    pass
    pass
                open_files = 0
            
            try:
    pass
                connections_list = process.connections()
                connections = len(connections_list) if connections_list else 0
            except (psutil.AccessDenied, psutil.NoSuchProcess, TypeError):
    
        pass
    pass
    pass
                connections = 0
            
            # Get command line
            try:
    pass
                cmdline = process.cmdline()
            except (psutil.AccessDenied, psutil.NoSuchProcess):
    pass
    pass
                cmdline = []
            
            return ProcessInfo(
                pid=pid,
                name=process.name(),
                status=process.status(),
                cpu_percent=cpu_percent,
                memory_percent=memory_percent,
                memory_mb=memory_mb,
                create_time=create_time,
                uptime=uptime,
                command_line=cmdline,
                threads=threads,
                open_files=open_files,
                connections=connections
            )
            
        except psutil.NoSuchProcess:
    pass
    pass
            return None
        except Exception as e:
    pass
    pass
            self.logger.warning(f"Error getting process info for PID {pid}: {e}")
            return None
    
    # Advanced Process Management Features
    
    def configure_recovery(self, config: RecoveryConfig) -> None:
    pass
        """
        Configure automatic recovery settings
        
        Args:
    pass
            config: Recovery configuration
        """
        self.recovery_config = config
        self.logger.info(f"Recovery configuration updated: {config}")
    
    def add_recovery_callback(self, callback: Callable[[str, BotStatus], None]) -> None:
    pass
        """
        Add callback for recovery events
        
        Args:
    pass
            callback: Function called when recovery actions occur
        """
        self.recovery_callbacks.append(callback)
    
    def start_monitoring(self, interval: int = 60) -> None:
    pass
        """
        Start continuous process monitoring
        
        Args:
    pass
            interval: Monitoring interval in seconds
        """
        if self.monitoring_active:
    
        pass
    pass
            self.logger.warning("Monitoring is already active")
            return
        
        self.monitoring_active = True
        self.monitoring_thread = threading.Thread(
            target=self._monitoring_loop,
            args=(interval,),
            daemon=True
        )
        self.monitoring_thread.start()
        self.logger.info(f"Started process monitoring with {interval}s interval")
    
    def stop_monitoring(self) -> None:
    pass
        """Stop continuous process monitoring"""
        if not self.monitoring_active:
    
        pass
    pass
            return
        
        self.monitoring_active = False
        if self.monitoring_thread:
    
        pass
    pass
            self.monitoring_thread.join(timeout=5)
        self.logger.info("Stopped process monitoring")
    
    def _monitoring_loop(self, interval: int) -> None:
    pass
        """Main monitoring loop"""
        while self.monitoring_active:
    pass
            try:
    pass
                self._check_all_instances()
                time.sleep(interval)
            except Exception as e:
    pass
    pass
                self.logger.error(f"Error in monitoring loop: {e}")
                time.sleep(interval)
    
    def _check_all_instances(self) -> None:
    pass
        """Check health of all bot instances"""
        for instance_name, instance in self.instances.items():
    pass
            try:
    pass
                self._check_instance_health(instance_name, instance)
            except Exception as e:
    pass
    pass
                self.logger.error(f"Error checking instance {instance_name}: {e}")
    
    def _check_instance_health(self, instance_name: str, instance: BotInstance) -> None:
    pass
        """
        Check health of a specific instance
        
        Args:
    
        pass
    pass
            instance_name: Name of the instance
            instance: Bot instance to check
        """
        if not instance.pid:
    
        pass
    pass
            return
        
        try:
    pass
            process_info = self._get_process_info(instance.pid)
            
            if not process_info:
    
        pass
    pass
                # Process crashed
                self.logger.warning(f"Instance {instance_name} (PID {instance.pid}) crashed")
                instance.status.state = ProcessState.CRASHED
                instance.status.running = False
                instance.status.error_message = "Process not found"
                
                if self.recovery_config.auto_restart_on_crash:
    
        pass
    pass
                    self._attempt_recovery(instance_name, instance)
                return
            
            # Update metrics
            metrics = ProcessMetrics(
                timestamp=datetime.now(),
                cpu_percent=process_info.cpu_percent,
                memory_mb=process_info.memory_mb,
                memory_percent=process_info.memory_percent,
                threads=process_info.threads,
                open_files=process_info.open_files,
                connections=process_info.connections
            )
            instance.metrics_history.append(metrics)
            
            # Update status
            instance.status.process_info = process_info
            instance.status.memory_usage = process_info.memory_mb
            instance.status.cpu_usage = process_info.cpu_percent
            instance.status.last_activity = datetime.now()
            
            # Check thresholds
            if (process_info.memory_mb > self.recovery_config.memory_threshold_mb or
                process_info.cpu_percent > self.recovery_config.cpu_threshold_percent):
    
        pass
    pass
                self.logger.warning(
                    f"Instance {instance_name} exceeds resource thresholds: "
                    f"Memory: {process_info.memory_mb:.1f}MB, CPU: {process_info.cpu_percent:.1f}%"
                )
                
                # Notify callbacks
                for callback in self.recovery_callbacks:
    
        pass
    pass
                    try:
    pass
                        callback(instance_name, instance.status)
                    except Exception as e:
    pass
    pass
                        self.logger.error(f"Error in recovery callback: {e}")
        
        except Exception as e:
    pass
    pass
            self.logger.error(f"Error checking health of {instance_name}: {e}")
    
    def _attempt_recovery(self, instance_name: str, instance: BotInstance) -> None:
    pass
        """
        Attempt to recover a crashed instance
        
        Args:
    pass
            instance_name: Name of the instance
            instance: Bot instance to recover
        """
        if not self.recovery_config.enabled:
    
        pass
    pass
            return
        
        if instance.status.restart_count >= self.recovery_config.max_restarts:
    
        pass
    pass
            self.logger.error(
                f"Instance {instance_name} exceeded max restart attempts "
                f"({self.recovery_config.max_restarts})"
            )
            return
        
        # Check restart delay
        if (instance.status.last_restart and 
            datetime.now() - instance.status.last_restart < 
            timedelta(seconds=self.recovery_config.restart_delay)):
    
        pass
    pass
            return
        
        self.logger.info(f"Attempting recovery of instance {instance_name}")
        instance.status.state = ProcessState.RECOVERING
        
        try:
    pass
            # Clean up old process
            self._cleanup_instance(instance_name, instance)
            
            # Wait before restart
            time.sleep(self.recovery_config.restart_delay)
            
            # Restart instance
            new_status = self.start_bot_instance(
                instance_name,
                config_file=instance.config_file,
                strategies=instance.strategies,
                accounts=instance.accounts
            )
            
            if new_status.running:
    
        pass
    pass
                instance.status.restart_count += 1
                instance.status.last_restart = datetime.now()
                self.logger.info(f"Successfully recovered instance {instance_name}")
            else:
    pass
                self.logger.error(f"Failed to recover instance {instance_name}")
        
        except Exception as e:
    pass
    pass
            self.logger.error(f"Recovery failed for instance {instance_name}: {e}")
            instance.status.state = ProcessState.CRASHED
    
    def start_bot_instance(self, instance_name: str,
                          config_file: Optional[str] = None,
                          strategies: Optional[List[str]] = None,
                          accounts: Optional[List[str]] = None,
                          background: bool = True) -> BotStatus:
    pass
        """
        Start a named bot instance
        
        Args:
    pass
            instance_name: Unique name for this instance
            config_file: Path to configuration file
            strategies: List of strategies to enable
            accounts: List of accounts to use
            background: Whether to run in background
            
        Returns:
    pass
            BotStatus with process information
        """
        # Check if instance already exists and is running
        if instance_name in self.instances:
    
        pass
    pass
            instance = self.instances[instance_name]
            if instance.status.running:
    
        pass
    pass
                raise ProcessError(
                    f"Instance '{instance_name}' is already running with PID {instance.pid}",
                    suggestions=[
                        f"Use 'genebot stop-instance {instance_name}' to stop it first",
                        f"Use 'genebot restart-instance {instance_name}' to restart it",
                        "Choose a different instance name"
                    ]
                )
        
        # Create instance if it doesn't exist
        if instance_name not in self.instances:
    
        pass
    pass
            self.instances[instance_name] = BotInstance(
                name=instance_name,
                config_file=config_file,
                strategies=strategies or [],
                accounts=accounts or []
            )
        
        instance = self.instances[instance_name]
        instance.pid_file = self.instances_dir / f"{instance_name}.pid"
        instance.log_file = self.log_dir / f"{instance_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        try:
    pass
            instance.status.state = ProcessState.STARTING
            
            # Prepare command
            cmd = self._build_start_command(config_file, strategies, accounts)
            
            # Prepare environment
            env = os.environ.copy()
            env['PYTHONPATH'] = str(self.workspace_path)
            env['GENEBOT_INSTANCE'] = instance_name
            
            # Add any environment variables set by _build_start_command
            if hasattr(self, '_env_vars'):
    
        pass
    pass
                env.update(self._env_vars)
            
            self.logger.info(f"Starting instance '{instance_name}' with command: {' '.join(cmd)}")
            
            # Start process
            if background:
    
        pass
    pass
                with open(instance.log_file, 'w') as log_f:
    pass
                    process = subprocess.Popen(
                        cmd,
                        stdout=log_f,
                        stderr=subprocess.STDOUT,
                        env=env,
                        cwd=self.workspace_path,
                        start_new_session=True
                    )
            else:
    pass
                process = subprocess.Popen(
                    cmd,
                    env=env,
                    cwd=self.workspace_path
                )
            
            # Wait for process to start
            time.sleep(2)
            
            if process.poll() is not None:
    
        pass
    pass
                raise ProcessError(
                    f"Instance '{instance_name}' terminated immediately with exit code {process.returncode}",
                    suggestions=[
                        f"Check log file: {instance.log_file}",
                        "Verify configuration is valid",
                        "Check system resources"
                    ]
                )
            
            # Update instance
            instance.pid = process.pid
            instance.status.pid = process.pid
            instance.status.running = True
            instance.status.state = ProcessState.RUNNING
            instance.status.last_activity = datetime.now()
            
            # Create PID file for instance
            self._create_instance_pid_file(instance_name, instance, cmd)
            
            # Save instances state
            self._save_instances()
            
            self.logger.info(f"Instance '{instance_name}' started with PID {process.pid}")
            return instance.status
        
        except Exception as e:
    
        pass
    pass
    pass
            instance.status.state = ProcessState.STOPPED
            instance.status.error_message = str(e)
            raise
    
    def stop_bot_instance(self, instance_name: str, timeout: int = 60, force: bool = False) -> BotStatus:
    pass
        """
        Stop a specific bot instance
        
        Args:
    
        pass
    pass
            instance_name: Name of the instance to stop
            timeout: Timeout for graceful shutdown
            force: Whether to force kill
            
        Returns:
    pass
            BotStatus after shutdown
        """
        if instance_name not in self.instances:
    
        pass
    pass
            raise ProcessError(
                f"Instance '{instance_name}' not found",
                suggestions=[
                    "Use 'genebot list-instances' to see available instances",
                    "Check the instance name spelling"
                ]
            )
        
        instance = self.instances[instance_name]
        
        if not instance.status.running or not instance.pid:
    
        pass
    pass
            self.logger.info(f"Instance '{instance_name}' is not running")
            instance.status.running = False
            instance.status.state = ProcessState.STOPPED
            self._cleanup_instance(instance_name, instance)
            return instance.status
        
        try:
    pass
            instance.status.state = ProcessState.STOPPING
            
            process = psutil.Process(instance.pid)
            
            if force:
    
        pass
    pass
                self.logger.warning(f"Force killing instance '{instance_name}' (PID {instance.pid})")
                process.kill()
                process.wait(timeout=5)
            else:
    pass
                self.logger.info(f"Gracefully stopping instance '{instance_name}' (PID {instance.pid})")
                process.terminate()
                
                try:
    pass
                    process.wait(timeout=timeout)
                except psutil.TimeoutExpired:
    pass
    pass
                    self.logger.warning(f"Instance '{instance_name}' did not stop gracefully, force killing")
                    process.kill()
                    process.wait(timeout=5)
            
            # Update status
            instance.status.running = False
            instance.status.state = ProcessState.STOPPED
            instance.status.pid = None
            instance.pid = None
            
            # Cleanup
            self._cleanup_instance(instance_name, instance)
            
            self.logger.info(f"Instance '{instance_name}' stopped successfully")
            return instance.status
        
        except psutil.NoSuchProcess:
    pass
    pass
            self.logger.info(f"Instance '{instance_name}' process no longer exists")
            instance.status.running = False
            instance.status.state = ProcessState.STOPPED
            self._cleanup_instance(instance_name, instance)
            return instance.status
        
        except Exception as e:
    pass
    pass
            self.logger.error(f"Failed to stop instance '{instance_name}': {e}")
            raise ProcessError(
                f"Failed to stop instance '{instance_name}': {str(e)}",
                suggestions=[
                    "Try using --force flag",
                    f"Manually kill process {instance.pid} if necessary"
                ]
            )
    
    def restart_bot_instance(self, instance_name: str, timeout: int = 60, **start_kwargs) -> BotStatus:
    pass
        """
        Restart a specific bot instance
        
        Args:
    
        pass
    pass
            instance_name: Name of the instance to restart
            timeout: Timeout for stop operation
            **start_kwargs: Arguments for start operation
            
        Returns:
    pass
            BotStatus after restart
        """
        if instance_name not in self.instances:
    
        pass
    pass
            raise ProcessError(
                f"Instance '{instance_name}' not found",
                suggestions=[
                    "Use 'genebot list-instances' to see available instances"
                ]
            )
        
        instance = self.instances[instance_name]
        
        # Preserve original configuration if not overridden
        config_file = start_kwargs.get('config_file', instance.config_file)
        strategies = start_kwargs.get('strategies', instance.strategies)
        accounts = start_kwargs.get('accounts', instance.accounts)
        
        try:
    
        pass
    pass
            # Stop instance
            self.stop_bot_instance(instance_name, timeout=timeout)
            
            # Wait before restart
            time.sleep(2)
            
            # Start instance
            return self.start_bot_instance(
                instance_name,
                config_file=config_file,
                strategies=strategies,
                accounts=accounts,
                **{k: v for k, v in start_kwargs.items() }
                   if k not in ['config_file', 'strategies', 'accounts']}
            )
        
        except Exception as e:
    
        pass
    pass
    pass
            self.logger.error(f"Failed to restart instance '{instance_name}': {e}")
            raise ProcessError(
                f"Failed to restart instance '{instance_name}': {str(e)}"
            )
    
    def list_instances(self) -> Dict[str, BotInstance]:
    pass
        """
        List all bot instances
        
        Returns:
    pass
            Dictionary of instance name to BotInstance
        """
        # Refresh instance status
        for instance_name, instance in self.instances.items():
    pass
            if instance.pid:
    
        pass
    pass
                process_info = self._get_process_info(instance.pid)
                if not process_info:
    
        pass
    pass
                    instance.status.running = False
                    instance.status.state = ProcessState.STOPPED
                    instance.pid = None
                    instance.status.pid = None
        
        return self.instances.copy()
    
    def get_instance_status(self, instance_name: str) -> BotStatus:
    pass
        """
        Get status of a specific instance
        
        Args:
    
        pass
    pass
            instance_name: Name of the instance
            
        Returns:
    pass
            BotStatus for the instance
        """
        if instance_name not in self.instances:
    
        pass
    pass
            raise ProcessError(f"Instance '{instance_name}' not found")
        
        instance = self.instances[instance_name]
        
        # Refresh status
        if instance.pid:
    
        pass
    pass
            process_info = self._get_process_info(instance.pid)
            if process_info:
    
        pass
    pass
                instance.status.process_info = process_info
                instance.status.memory_usage = process_info.memory_mb
                instance.status.cpu_usage = process_info.cpu_percent
                instance.status.uptime = process_info.uptime
                instance.status.last_activity = datetime.now()
            else:
    pass
                instance.status.running = False
                instance.status.state = ProcessState.STOPPED
                instance.pid = None
                instance.status.pid = None
        
        return instance.status
    
    def get_instance_metrics(self, instance_name: str, limit: int = 50) -> List[ProcessMetrics]:
    pass
        """
        Get performance metrics for an instance
        
        Args:
    pass
            instance_name: Name of the instance
            limit: Maximum number of metrics to return
            
        Returns:
    pass
            List of ProcessMetrics
        """
        if instance_name not in self.instances:
    
        pass
    pass
            raise ProcessError(f"Instance '{instance_name}' not found")
        
        instance = self.instances[instance_name]
        metrics = list(instance.metrics_history)
        return metrics[-limit:] if limit > 0 else metrics
    
    def get_instance_logs(self, instance_name: str, lines: int = 100) -> List[str]:
    pass
        """
        Get recent log lines for an instance
        
        Args:
    pass
            instance_name: Name of the instance
            lines: Number of lines to return
            
        Returns:
    pass
            List of log lines
        """
        if instance_name not in self.instances:
    
        pass
    pass
            raise ProcessError(f"Instance '{instance_name}' not found")
        
        instance = self.instances[instance_name]
        
        if not instance.log_file or not instance.log_file.exists():
    
        pass
    pass
            return []
        
        try:
    pass
            with open(instance.log_file, 'r') as f:
    pass
                all_lines = f.readlines()
                return [line.rstrip() for line in all_lines[-lines:]]
        except Exception as e:
    pass
    pass
            self.logger.error(f"Error reading log file for {instance_name}: {e}")
            return []
    
    def _create_instance_pid_file(self, instance_name: str, instance: BotInstance, command: List[str]) -> None:
    pass
        """Create PID file for an instance"""
        pid_data = {
            'instance_name': instance_name,
            'pid': instance.pid,
            'command': command,
            'log_file': str(instance.log_file),
            'config_file': instance.config_file,
            'strategies': instance.strategies,
            'accounts': instance.accounts,
            'start_time': datetime.now().isoformat(),
            'workspace': str(self.workspace_path)
        }
        
        try:
    pass
            with open(instance.pid_file, 'w') as f:
    pass
                json.dump(pid_data, f, indent=2)
        except Exception as e:
    pass
    pass
            self.logger.error(f"Failed to create PID file for {instance_name}: {e}")
    
    def _cleanup_instance(self, instance_name: str, instance: BotInstance) -> None:
    pass
        """Clean up instance files and state"""
        try:
    pass
            if instance.pid_file and instance.pid_file.exists():
    
        pass
    pass
                instance.pid_file.unlink()
        except Exception as e:
    pass
    pass
            self.logger.warning(f"Failed to remove PID file for {instance_name}: {e}")
        
        # Save updated state
        self._save_instances()
    
    def _load_instances(self) -> None:
    pass
        """Load existing instances from PID files"""
        try:
    pass
            for pid_file in self.instances_dir.glob("*.pid"):
    pass
                try:
    pass
                        pid_data = json.load(f)
                    
                    instance_name = pid_data.get('instance_name')
                    if not instance_name:
    
        pass
    pass
                        continue
                    
                    # Create instance
                    instance = BotInstance(
                        name=instance_name,
                        pid=pid_data.get('pid'),
                        config_file=pid_data.get('config_file'),
                        strategies=pid_data.get('strategies', []),
                        accounts=pid_data.get('accounts', []),
                        pid_file=pid_file,
                        log_file=Path(pid_data.get('log_file', '')) if pid_data.get('log_file') else None
                    )
                    
                    # Check if process is still running
                    if instance.pid:
    
        pass
    pass
                        process_info = self._get_process_info(instance.pid)
                        if process_info:
    
        pass
    pass
                            instance.status.running = True
                            instance.status.state = ProcessState.RUNNING
                            instance.status.pid = instance.pid
                            instance.status.process_info = process_info
                        else:
    pass
                            # Process not running, clean up
                            instance.status.running = False
                            instance.status.state = ProcessState.STOPPED
                            instance.pid = None
                            instance.status.pid = None
                            try:
    pass
                                pid_file.unlink()
                            except Exception:
    pass
    pass
                    self.instances[instance_name] = instance
                
                except Exception as e:
    pass
    pass
                    self.logger.warning(f"Error loading instance from {pid_file}: {e}")
        
        except Exception as e:
    pass
    pass
    def _save_instances(self) -> None:
    pass
        """Save current instances state"""
        # This is handled by individual PID files, no central state file needed