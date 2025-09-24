"""
System Health CLI Command
========================

CLI command for running comprehensive system health checks.
"""

import asyncio
import json
from pathlib import Path
from argparse import Namespace
from typing import Dict, Any

from ..base_command import BaseCommand
from ...system.health_checker import (
    HealthStatus
)


class SystemHealthCommand(BaseCommand):
    pass
    """System health check command."""
    
    def get_name(self) -> str:
    pass
        return "system-health"
    
    def get_description(self) -> str:
    pass
        return "Run comprehensive system health checks"
    
    def configure_parser(self, parser):
    pass
        """Configure the argument parser."""
        parser.add_argument(
            '--quick', 
            action='store_true',
            help='Run quick health check without detailed reports'
        )
        parser.add_argument(
            '--output-dir', 
            type=Path,
            default=Path('reports'),
            help='Directory to save health reports (default: reports)'
        )
        parser.add_argument(
            '--format',
            choices=['json', 'html', 'both'],
            default='both',
            help='Output format for reports (default: both)'
        )
        parser.add_argument(
            '--components',
            nargs='+',
            choices=['database', 'cli', 'trading', 'performance', 'config', 'filesystem'],
            help='Specific components to check (default: all)'
        )
        parser.add_argument(
            '--timeout',
            type=int,
            default=300,
            help='Timeout in seconds for health checks (default: 300)'
        )
        parser.add_argument(
            '--continuous',
            action='store_true',
            help='Start continuous monitoring mode'
        )
        parser.add_argument(
            '--interval',
            type=int,
            default=60,
            help='Interval in minutes for continuous monitoring (default: 60)'
        )
        parser.add_argument(
            '--no-database',
            action='store_true',
            help='Skip database health checks'
        )
        parser.add_argument(
            '--no-cli',
            action='store_true',
            help='Skip CLI health checks'
        )
        parser.add_argument(
            '--no-trading',
            action='store_true',
            help='Skip trading system health checks'
        )
        parser.add_argument(
            '--no-performance',
            action='store_true',
            help='Skip performance health checks'
        )
    
    async def execute(self, args: Namespace, context) -> Dict[str, Any]:
    pass
        """Execute the system health check command."""
        try:
    pass
            if args.quick:
    
        pass
    pass
                return await self._run_quick_check(args)
            elif args.continuous:
    
        pass
    pass
                return await self._run_continuous_monitoring(args)
            else:
    pass
                return await self._run_comprehensive_check(args)
                
        except KeyboardInterrupt:
    pass
    pass
            return {
                "success": False,
                "message": "Health check interrupted by user",
                "interrupted": True
            }
        except Exception as e:
    pass
    pass
            return {
                "success": False,
                "message": f"Health check failed: {str(e)}",
                "error": str(e)
            }
    
    async def _run_quick_check(self, args: Namespace) -> Dict[str, Any]:
    pass
        """Run a quick health check."""
        print("🏥 Running quick system health check...")
        
        # Configure health checker
        checker = SystemHealthChecker()
        self._configure_checker(checker, args)
        
        # Run health check
        report = await checker.run_comprehensive_health_check()
        
        # Display results
        self._display_health_summary(report)
        
        return {
            "success": True,
            "message": "Quick health check completed",
            "overall_status": report.overall_status.value,
            "summary": report.summary,
            "component_count": len(report.components)
        }
    
    async def _run_comprehensive_check(self, args: Namespace) -> Dict[str, Any]:
    pass
        """Run comprehensive health check with reports."""
        print("🏥 Running comprehensive system health check...")
        
        # Configure health checker
        checker = SystemHealthChecker()
        self._configure_checker(checker, args)
        
        # Run health check
        report = await checker.run_comprehensive_health_check()
        
        # Save reports
        report_paths = await self._save_reports(checker, report, args)
        
        # Display results
        self._display_health_summary(report)
        self._display_component_details(report)
        
        if report.recommendations:
    
        pass
    pass
            self._display_recommendations(report)
        
        print(f"\n📄 Reports saved:")
        for path in report_paths:
    pass
            print(f"  - {path}")
        
        return {
            "success": True,
            "message": "Comprehensive health check completed",
            "overall_status": report.overall_status.value,
            "summary": report.summary,
            "report_paths": [str(p) for p in report_paths],
            "component_count": len(report.components)
        }
    
    async def _run_continuous_monitoring(self, args: Namespace) -> Dict[str, Any]:
    pass
        """Run continuous health monitoring."""
        print("🔄 Starting continuous system health monitoring...")
        print(f"   Interval: {args.interval} minutes")
        print("   Press Ctrl+C to stop")
        
        # Configure health checker
        checker = SystemHealthChecker()
        self._configure_checker(checker, args)
        
        # Configure pipeline
        pipeline = AutomatedTestingPipeline(checker)
        pipeline.configure_schedule(interval_minutes=args.interval)
        
        try:
    pass
            await pipeline.start_continuous_monitoring()
            
            return {
                "success": True,
                "message": "Continuous monitoring completed",
                "monitoring_stopped": True
            }
            
        except KeyboardInterrupt:
    pass
    pass
            pipeline.stop_monitoring()
            print("\n🛑 Monitoring stopped by user")
            
            return {
                "success": True,
                "message": "Monitoring stopped by user",
                "interrupted": True
            }
    
    def _configure_checker(self, checker: SystemHealthChecker, args: Namespace):
    pass
        """Configure the health checker based on arguments."""
        config = {
            "timeout_seconds": args.timeout,
            "database_enabled": not args.no_database,
            "cli_enabled": not args.no_cli,
            "trading_enabled": not args.no_trading,
            "performance_enabled": not args.no_performance
        }
        
        # If specific components are requested, enable only those
        if args.components:
    
        pass
    pass
            config.update({
                "database_enabled": "database" in args.components,
                "cli_enabled": "cli" in args.components,
                "trading_enabled": "trading" in args.components,
                "performance_enabled": "performance" in args.components
            })
        
        checker.configure_checks(**config)
    
    async def _save_reports(self, checker: SystemHealthChecker, report, args: Namespace) -> list:
    pass
        """Save health reports in requested formats."""
        report_paths = []
        timestamp = report.timestamp.strftime("%Y%m%d_%H%M%S")
        
        # Ensure output directory exists
        args.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Save JSON report
        if args.format in ['json', 'both']:
    
        pass
    pass
            json_path = args.output_dir / f"health_check_{timestamp}.json"
            checker.save_report(report, json_path)
            report_paths.append(json_path)
        
        # Save HTML report
        if args.format in ['html', 'both']:
    
        pass
    pass
            html_report = checker.generate_html_report(report)
            html_path = args.output_dir / f"health_check_{timestamp}.html"
            html_path.write_text(html_report)
            report_paths.append(html_path)
        
        return report_paths
    
    def _display_health_summary(self, report):
    pass
        """Display health check summary."""
        status_emoji = {
            HealthStatus.HEALTHY: "✅",
            HealthStatus.WARNING: "⚠️",
            HealthStatus.CRITICAL: "❌",
            HealthStatus.UNKNOWN: "❓"
        }
        
        emoji = status_emoji.get(report.overall_status, "❓")
        
        print(f"\n{emoji} SYSTEM HEALTH SUMMARY")
        print("=" * 50)
        print(f"Overall Status: {report.overall_status.value}")
        print(f"Check Time: {report.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total Duration: {report.summary.get('total_check_time', 0):.2f}s")
        print()
        
        summary = report.summary
        print(f"Components Checked: {summary.get('total_components', 0)}")
        print(f"  ✅ Healthy: {summary.get('healthy', 0)}")
        print(f"  ⚠️  Warnings: {summary.get('warnings', 0)}")
        print(f"  ❌ Critical: {summary.get('critical', 0)}")
        print(f"Health Score: {summary.get('health_percentage', 0):.1f}%")
    
    def _display_component_details(self, report):
    pass
        """Display detailed component health information."""
        print("\n🔍 COMPONENT DETAILS")
        print("=" * 50)
        
        for component in report.components:
    pass
            status_emoji = {
                HealthStatus.HEALTHY: "✅",
                HealthStatus.WARNING: "⚠️",
                HealthStatus.CRITICAL: "❌",
                HealthStatus.UNKNOWN: "❓"
            }
            
            emoji = status_emoji.get(component.status, "❓")
            
            print(f"{emoji} {component.component_name}")
            print(f"   Status: {component.status.value}")
            print(f"   Message: {component.message}")
            print(f"   Duration: {component.check_duration:.2f}s")
            
            # Show key details for failed components
            if component.status in [HealthStatus.WARNING, HealthStatus.CRITICAL]:
    
        pass
    pass
                if 'issues' in component.details:
    
        pass
    pass
                    issues = component.details['issues']
                    if issues:
    
        pass
    pass
                        print(f"   Issues:")
                        for issue in issues[:3]:  # Show first 3 issues
                            print(f"     - {issue}")
                        if len(issues) > 3:
    
        pass
    pass
                            print(f"     ... and {len(issues) - 3} more")
            
            print()
    
    def _display_recommendations(self, report):
    pass
        """Display health recommendations."""
        print("💡 RECOMMENDATIONS")
        print("=" * 50)
        
        for i, recommendation in enumerate(report.recommendations, 1):
    pass
            print(f"{i}. {recommendation}")
        
        print()


# Register command variants
class HealthCommand(SystemHealthCommand):
    pass
    """Alias for system-health command."""
    
    def get_name(self) -> str:
    pass
        return "health"


class CheckHealthCommand(SystemHealthCommand):
    pass
    """Another alias for system-health command."""
    
    def get_name(self) -> str:
    pass
        return "check-health"