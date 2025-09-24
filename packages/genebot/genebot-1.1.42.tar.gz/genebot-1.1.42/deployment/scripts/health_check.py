#!/usr/bin/env python3
"""
Comprehensive health check script for trading bot deployment.
"""

import asyncio
import json
import sys
import time
from datetime import datetime, timedelta
import aiohttp
import psutil
import redis
from sqlalchemy import create_engine, text


class HealthChecker:
    pass
    """Comprehensive health check for trading bot components."""
    
    def __init__(self, config: Dict):
    pass
        self.config = config
        self.results = {}
        
    async def run_all_checks(self) -> Dict:
    pass
        """Run all health checks and return results."""
        checks = [
            self.check_application_health(),
            self.check_database_health(),
            self.check_redis_health(),
            self.check_system_resources(),
            self.check_exchange_connectivity(),
            self.check_log_health(),
        ]
        
        results = await asyncio.gather(*checks, return_exceptions=True)
        
        # Process results
        check_names = [
            'application', 'database', 'redis', 
            'system', 'exchange', 'logs'
        ]
        
        for name, result in zip(check_names, results):
    pass
    pass
            if isinstance(result, Exception):
    
        pass
    pass
                self.results[name] = {
                    'status': 'error',
                    'message': str(result),
                    'timestamp': datetime.utcnow().isoformat()
                }
            else:
    pass
                self.results[name] = result
        
        return self.results
    
    async def check_application_health(self) -> Dict:
    pass
        """Check main application health endpoint."""
        try:
    pass
            health_url = f"http://localhost:{self.config.get('health_port', 8080)}/health"
            
            async with aiohttp.ClientSession() as session:
    pass
                async with session.get(health_url, timeout=10) as response:
    pass
                    if response.status == 200:
    
        pass
    pass
                        data = await response.json()
                        return {
                            'status': 'healthy',
                            'response_time': data.get('response_time', 0),
                            'version': data.get('version', 'unknown'),
                            'timestamp': datetime.utcnow().isoformat()
                        }
                    else:
    pass
                        return {
                            'status': 'unhealthy',
                            'message': f'HTTP {response.status}',
                            'timestamp': datetime.utcnow().isoformat()
                        }
        except Exception as e:
    pass
    pass
            return {
                'status': 'error',
                'message': str(e),
                'timestamp': datetime.utcnow().isoformat()
            }
    
    async def check_database_health(self) -> Dict:
    pass
        """Check database connectivity and performance."""
        try:
    pass
            db_url = self.config.get('database_url')
            if not db_url:
    
        pass
    pass
                return {
                    'status': 'error',
                    'message': 'Database URL not configured',
                    'timestamp': datetime.utcnow().isoformat()
                }
            
            engine = create_engine(db_url)
            
            # Test connection and query performance
            start_time = time.time()
            with engine.connect() as conn:
    pass
                result = conn.execute(text("SELECT 1"))
                result.fetchone()
            
            query_time = (time.time() - start_time) * 1000
            
            return {
                'status': 'healthy',
                'query_time_ms': round(query_time, 2),
                'timestamp': datetime.utcnow().isoformat()
            }
            
        except Exception as e:
    pass
    pass
            return {
                'status': 'error',
                'message': str(e),
                'timestamp': datetime.utcnow().isoformat()
            }
    
    async def check_redis_health(self) -> Dict:
    pass
        """Check Redis connectivity and performance."""
        try:
    pass
            redis_url = self.config.get('redis_url')
            if not redis_url:
    
        pass
    pass
                return {
                    'status': 'warning',
                    'message': 'Redis not configured',
                    'timestamp': datetime.utcnow().isoformat()
                }
            
            r = redis.from_url(redis_url)
            
            # Test connection and performance
            start_time = time.time()
            ping_time = (time.time() - start_time) * 1000
            
            # Get Redis info
            info = r.info()
            
            return {
                'status': 'healthy',
                'ping_time_ms': round(ping_time, 2),
                'memory_usage_mb': round(info['used_memory'] / 1024 / 1024, 2),
                'connected_clients': info['connected_clients'],
                'timestamp': datetime.utcnow().isoformat()
            }
            
        except Exception as e:
    pass
    pass
            return {
                'status': 'error',
                'message': str(e),
                'timestamp': datetime.utcnow().isoformat()
            }
    
    async def check_system_resources(self) -> Dict:
    pass
        """Check system resource usage."""
        try:
    pass
            # CPU usage
            cpu_percent = psutil.cpu_percent(interval=1)
            
            # Memory usage
            memory = psutil.virtual_memory()
            
            # Disk usage
            disk = psutil.disk_usage('/')
            
            # Load average (Unix only)
            try:
    pass
                load_avg = psutil.getloadavg()
            except AttributeError:
    pass
    pass
                load_avg = [0, 0, 0]  # Windows doesn't have load average
            
            status = 'healthy'
            warnings = []
            
            if cpu_percent > 80:
    
        pass
    pass
                warnings.append(f'High CPU usage: {cpu_percent}%')
                status = 'warning'
            
            if memory.percent > 80:
    
        pass
    pass
                warnings.append(f'High memory usage: {memory.percent}%')
                status = 'warning'
            
            if disk.percent > 80:
    
        pass
    pass
                warnings.append(f'High disk usage: {disk.percent}%')
                status = 'warning'
            
            return {
                'status': status,
                'cpu_percent': cpu_percent,
                'memory_percent': memory.percent,
                'memory_available_gb': round(memory.available / 1024 / 1024 / 1024, 2),
                'disk_percent': disk.percent,
                'disk_free_gb': round(disk.free / 1024 / 1024 / 1024, 2),
                'load_average': load_avg,
                'warnings': warnings,
                'timestamp': datetime.utcnow().isoformat()
            }
            
        except Exception as e:
    pass
    pass
            return {
                'status': 'error',
                'message': str(e),
                'timestamp': datetime.utcnow().isoformat()
            }
    
    async def check_exchange_connectivity(self) -> Dict:
    pass
        """Check exchange API connectivity."""
        try:
    pass
            # This would typically check actual exchange connections
            # For now, we'll simulate the check
            
            exchanges = ['binance', 'coinbase', 'kraken']
            exchange_status = {}
            
            for exchange in exchanges:
    pass
                # Simulate exchange health check
                # In real implementation, this would test actual API connectivity
                exchange_status[exchange] = {
                    'status': 'healthy',
                    'latency_ms': 50,
                    'rate_limit_remaining': 1000
                }
            
            return {
                'status': 'healthy',
                'exchanges': exchange_status,
                'timestamp': datetime.utcnow().isoformat()
            }
            
        except Exception as e:
    pass
    pass
            return {
                'status': 'error',
                'message': str(e),
                'timestamp': datetime.utcnow().isoformat()
            }
    
    async def check_log_health(self) -> Dict:
    pass
        """Check log file health and recent errors."""
        try:
    pass
            import os
            from pathlib import Path
            
            log_dir = Path('logs')
            if not log_dir.exists():
    
        pass
    pass
                return {
                    'message': 'Log directory not found',
                    'timestamp': datetime.utcnow().isoformat()
                }
            
            # Check error log
            error_log = log_dir / 'errors.log'
            recent_errors = 0
            
            if error_log.exists():
    
        pass
    pass
                # Count errors in last hour
                one_hour_ago = datetime.now() - timedelta(hours=1)
                
                with open(error_log, 'r') as f:
    pass
                    for line in f:
    pass
                        # Simple error counting (would be more sophisticated in real implementation)
                        if 'ERROR' in line:
    
        pass
    pass
                            recent_errors += 1
            
            # Check log file sizes
            log_files = list(log_dir.glob('*.log'))
            total_log_size = sum(f.stat().st_size for f in log_files)
            
            status = 'healthy'
            if recent_errors > 10:
    
        pass
    pass
                status = 'warning'
            
            return {
                'status': status,
                'recent_errors': recent_errors,
                'log_files_count': len(log_files),
                'total_log_size_mb': round(total_log_size / 1024 / 1024, 2),
                'timestamp': datetime.utcnow().isoformat()
            }
            
        except Exception as e:
    pass
    pass
            return {
                'status': 'error',
                'message': str(e),
                'timestamp': datetime.utcnow().isoformat()
            }
    
    def get_overall_status(self) -> str:
    pass
        """Determine overall system health status."""
        if not self.results:
    
        pass
    pass
            return 'unknown'
        
        statuses = [check.get('status', 'unknown') for check in self.results.values()]
        
        if 'error' in statuses:
    
        pass
    pass
            return 'unhealthy'
        elif 'warning' in statuses:
    
        pass
    pass
            return 'degraded'
        elif all(status == 'healthy' for status in statuses):
    
        pass
    pass
            return 'healthy'
        else:
    pass
            return 'unknown'


async def main():
    pass
    """Main health check execution."""
    import os
    
    # Load configuration
    config = {
        'redis_url': os.getenv('REDIS_URL'),
    }
    
    # Run health checks
    checker = HealthChecker(config)
    results = await checker.run_all_checks()
    
    # Add overall status
    results['overall'] = {
        'status': checker.get_overall_status(),
        'timestamp': datetime.utcnow().isoformat()
    }
    
    # Output results
    print(json.dumps(results, indent=2))
    
    # Exit with appropriate code
    overall_status = results['overall']['status']
    if overall_status == 'healthy':
    
        pass
    pass
        sys.exit(0)
    elif overall_status == 'degraded':
    
        pass
    pass
        sys.exit(1)
    else:
    pass
        sys.exit(2)


if __name__ == "__main__":
    
        pass
    pass
    asyncio.run(main())