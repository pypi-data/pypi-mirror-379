"""
Final Validation CLI Command

Provides CLI access to the final validation and reporting system.
"""

import json
from argparse import Namespace
from pathlib import Path

from .base import BaseCommand
from ..result import CommandResult
from ...reporting.report_generator import ReportGenerator
from ...reporting.health_dashboard import HealthDashboard
from ...reporting.system_monitor import SystemMonitor
from ...reporting.cleanup_reporter import CleanupReporter


class FinalValidationCommand(BaseCommand):
    """Final validation and reporting command."""
    
    def execute(self, args: Namespace) -> CommandResult:
        """Execute final validation command."""
        
        # Determine subcommand
        subcommand = getattr(args, 'subcommand', 'generate_final_report')
        
        if subcommand == 'generate_final_report':
            return self._generate_final_report(args)
        elif subcommand == 'generate_changes_doc':
            return self._generate_changes_doc(args)
        elif subcommand == 'generate_cleanup_report':
            return self._generate_cleanup_report(args)
        elif subcommand == 'show_dashboard':
            return self._show_dashboard(args)
        elif subcommand == 'monitor':
            return self._monitor(args)
        elif subcommand == 'system_status':
            return self._system_status(args)
        else:
            return self._generate_final_report(args)  # Default action
    
    def _generate_final_report(self, args: Namespace) -> CommandResult:
        """Generate comprehensive final validation report."""
        try:
            output_dir = getattr(args, 'output_dir', 'reports')
            
            self.logger.info("Generating final validation report...")
            
            report_generator = ReportGenerator(output_dir)
            
            # Generate final validation report
            report = report_generator.generate_final_validation_report()
            
            # Display summary
            summary_lines = [
                "📊 Final Validation Report Generated Successfully",
                f"📁 Report saved to: {output_dir}/",
                "",
                "📊 Report Summary:",
                f"   Overall Health Score: {report.get('system_health_report', {}).get('health_score', 'N/A')}",
                f"   Validation Success: {'✅ PASSED' if report.get('validation_results', {}).get('overall_success', False) else '❌ ISSUES FOUND'}",
                f"   Files Cleaned: {report.get('executive_summary', {}).get('metrics', {}).get('files_cleaned', 'N/A')}",
                f"   System Status: {report.get('system_health_report', {}).get('system_overview', {}).get('status', 'Unknown')}"
            ]
            
            return CommandResult.success("\n".join(summary_lines))
            
        except Exception as e:
            return CommandResult.error(f"Error generating final report: {str(e)}")
    
    def _generate_changes_doc(self, args: Namespace) -> CommandResult:
        """Generate comprehensive changes documentation."""
        try:
            output_dir = getattr(args, 'output_dir', 'reports')
            
            self.logger.info("Generating changes documentation...")
            
            report_generator = ReportGenerator(output_dir)
            
            # Generate changes documentation
            changes_doc = report_generator.generate_changes_documentation()
            
            # Display summary
            overview = changes_doc.get('overview', {})
            summary_lines = [
                "📋 Changes Documentation Generated Successfully",
                f"📁 Documentation saved to: {output_dir}/",
                "",
                "📋 Changes Summary:",
                f"   Total Changes: {overview.get('total_changes', 'N/A')}",
                f"   Files Modified: {overview.get('files_modified', 'N/A')}",
                f"   Files Removed: {overview.get('files_removed', 'N/A')}",
                f"   Code Reduction: {overview.get('complexity_reduction', 'N/A')}"
            ]
            
            return CommandResult.success("\n".join(summary_lines))
            
        except Exception as e:
            return CommandResult.error(f"Error generating changes documentation: {str(e)}")
    
    def _generate_cleanup_report(self, args: Namespace) -> CommandResult:
        """Generate comprehensive cleanup report."""
        try:
            output_dir = getattr(args, 'output_dir', 'reports')
            
            self.logger.info("Generating cleanup report...")
            
            cleanup_reporter = CleanupReporter(output_dir)
            
            # Generate cleanup report
            report = cleanup_reporter.generate_cleanup_report()
            
            # Display summary
            summary = report.get('cleanup_summary', {})
            summary_lines = [
                "🧹 Cleanup Report Generated Successfully",
                f"📁 Report saved to: {output_dir}/",
                "",
                "🧹 Cleanup Summary:",
                f"   Files Processed: {summary.get('total_files_processed', 'N/A')}",
                f"   Duplicates Removed: {summary.get('duplicate_files_removed', 'N/A')}",
                f"   Mocks Removed: {summary.get('mock_implementations_removed', 'N/A')}",
                f"   Modules Consolidated: {summary.get('modules_consolidated', 'N/A')}",
                f"   Completion: {summary.get('cleanup_completion_percentage', 'N/A')}%"
            ]
            
            return CommandResult.success("\n".join(summary_lines))
            
        except Exception as e:
            return CommandResult.error(f"Error generating cleanup report: {str(e)}")
    
    def _show_dashboard(self, args: Namespace) -> CommandResult:
        """Show system health dashboard."""
        try:
            refresh = getattr(args, 'refresh', False)
            
            self.logger.info("Loading system health dashboard...")
            
            dashboard = HealthDashboard()
            
            # Get dashboard data
            data = dashboard.get_dashboard_data(force_refresh=refresh)
            
            # Format dashboard output
            dashboard_lines = [
                "🎛️  System Health Dashboard",
                "=" * 50,
                "",
                "📊 System Overview:",
                f"   Status: {data.get('system_overview', {}).get('status', 'Unknown')}",
                f"   Health Score: {data.get('health_score', 'N/A')}",
                f"   Uptime: {data.get('system_overview', {}).get('uptime', 'Unknown')}",
                f"   Version: {data.get('system_overview', {}).get('version', 'Unknown')}",
                "",
                "💾 Database Status:",
                f"   Connection: {data.get('database_status', {}).get('connection_status', 'Unknown')}",
                f"   Schema: {data.get('database_status', {}).get('schema_status', 'Unknown')}",
                f"   CRUD Operations: {data.get('database_status', {}).get('crud_operations', 'Unknown')}",
                f"   Performance: {data.get('database_status', {}).get('performance', 'N/A')}ms",
                "",
                "⌨️  CLI Commands Status:",
                f"   Total Commands: {data.get('cli_commands_status', {}).get('total_commands', 'N/A')}",
                f"   Working: {data.get('cli_commands_status', {}).get('working_commands', 'N/A')}",
                f"   Success Rate: {data.get('cli_commands_status', {}).get('success_rate', 'N/A')}%",
                "",
                "📈 Trading System Status:",
                f"   Exchange Connectivity: {data.get('trading_system_status', {}).get('exchange_connectivity', 'Unknown')}",
                f"   Strategy Validation: {data.get('trading_system_status', {}).get('strategy_validation', 'Unknown')}",
                f"   Order Management: {data.get('trading_system_status', {}).get('order_management', 'Unknown')}",
                f"   Active Strategies: {data.get('trading_system_status', {}).get('active_strategies', 'N/A')}"
            ]
            
            # Add alerts if any
            alerts = data.get('alerts', [])
            if alerts:
                dashboard_lines.extend([
                    "",
                    f"⚠️  Active Alerts ({len(alerts)}):"
                ])
                for alert in alerts[:5]:  # Show first 5 alerts
                    level_icon = "🔴" if alert.get('level') == 'critical' else "🟡"
                    dashboard_lines.append(f"   {level_icon} {alert.get('message', 'Unknown alert')}")
            else:
                dashboard_lines.extend([
                    "",
                    "✅ No active alerts"
                ])
            
            return CommandResult.success("\n".join(dashboard_lines))
            
        except Exception as e:
            return CommandResult.error(f"Error loading dashboard: {str(e)}")
    
    def _monitor(self, args: Namespace) -> CommandResult:
        """Control continuous system monitoring."""
        try:
            start = getattr(args, 'start', False)
            stop = getattr(args, 'stop', False)
            status = getattr(args, 'status', False)
            interval = getattr(args, 'interval', 300)
            
            monitor = SystemMonitor(check_interval=interval)
            
            if start:
                self.logger.info("Starting continuous system monitoring...")
                monitor.start_monitoring()
                return CommandResult.success(f"✅ Monitoring started (interval: {interval}s)")
                
            elif stop:
                self.logger.info("Stopping continuous system monitoring...")
                monitor.stop_monitoring()
                return CommandResult.success("✅ Monitoring stopped")
                
            elif status:
                monitoring_status = monitor.get_monitoring_status()
                
                status_lines = [
                    "📊 Monitoring Status",
                    "=" * 30,
                    f"Active: {'✅ Yes' if monitoring_status.get('active', False) else '❌ No'}",
                    f"Check Interval: {monitoring_status.get('check_interval', 'N/A')}s",
                    f"Total Checks: {monitoring_status.get('total_checks', 'N/A')}",
                    f"Alerts Generated: {monitoring_status.get('alerts_generated', 'N/A')}",
                    f"Average Health: {monitoring_status.get('average_health_score', 'N/A')}"
                ]
                
                if monitoring_status.get('last_check'):
                    status_lines.append(f"Last Check: {monitoring_status.get('last_check')}")
                
                return CommandResult.success("\n".join(status_lines))
                
            else:
                return CommandResult.error("Please specify --start, --stop, or --status")
                
        except Exception as e:
            return CommandResult.error(f"Error with monitoring: {str(e)}")
    
    def _system_status(self, args: Namespace) -> CommandResult:
        """Generate current system status report."""
        try:
            output_dir = getattr(args, 'output_dir', 'reports')
            
            self.logger.info("Generating system status report...")
            
            report_generator = ReportGenerator(output_dir)
            
            # Generate status report
            status_report = report_generator.generate_system_status_report()
            
            # Display key metrics
            current_status = status_report.get('current_status', {})
            monitoring_status = status_report.get('monitoring_status', {})
            
            status_lines = [
                "✅ System status report generated successfully",
                f"📁 Report saved to: {output_dir}/",
                "",
                "📊 Current System Status:",
                f"   Health Score: {current_status.get('health_score', 'N/A')}",
                f"   System Status: {current_status.get('system_overview', {}).get('status', 'Unknown')}",
                f"   Active Alerts: {len(current_status.get('alerts', []))}",
                f"   Monitoring: {'Active' if monitoring_status.get('active', False) else 'Inactive'}"
            ]
            
            return CommandResult.success("\n".join(status_lines))
            
        except Exception as e:
            return CommandResult.error(f"Error generating status report: {str(e)}")

