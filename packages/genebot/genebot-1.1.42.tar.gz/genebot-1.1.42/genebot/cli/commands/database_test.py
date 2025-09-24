"""Database testing CLI command."""

import argparse
import sys
from typing import Optional

from ...database.testing import run_database_tests, run_database_benchmarks, DatabaseTestSuite, DatabaseBenchmark
from ..result import CommandResult
from .base import BaseCommand


def add_database_test_parser(subparsers):
    pass
    """Add database test command parser."""
    parser = subparsers.add_parser(
        'db-test',
        help='Run comprehensive database tests and benchmarks'
    )
    
    parser.add_argument(
        '--database-url',
        type=str,
        help='Database URL to test (default: uses configured database)'
    )
    
    parser.add_argument(
        '--benchmark',
        action='store_true',
        help='Run performance benchmarks in addition to tests'
    )
    
    parser.add_argument(
        '--use-temp-db',
        action='store_true',
        default=True,
        help='Use temporary database for testing (default: true)'
    )
    
    parser.add_argument(
        '--no-temp-db',
        action='store_true',
        help='Use actual database instead of temporary database'
    )
    
    parser.add_argument(
        '--test-only',
        type=str,
        choices=[
            'connection', 'schema', 'crud', 'performance', 
            'integrity', 'concurrent', 'all'
        ],
        help='Run only specific test category'
    )
    
    parser.add_argument(
        '--output-format',
        type=str,
        choices=['console', 'json', 'csv'],
        default='console',
        help='Output format for test results'
    )
    
    parser.set_defaults(func=handle_database_test)


def handle_database_test(args) -> CommandResult:
    
        pass
    pass
    """Handle database test command."""
    try:
    pass
        # Determine database URL
        database_url = args.database_url
        use_temp_db = args.use_temp_db and not args.no_temp_db
        
        print("🧪 GeneBot Database Testing Utility")
        print("=" * 50)
        
        if use_temp_db:
    
        pass
    pass
            print("📝 Using temporary database for testing")
        else:
    pass
            print(f"📝 Testing database: {database_url or 'default'}")
        
        # Run tests
        if args.test_only and args.test_only != 'all':
    
        pass
    pass
            test_results = run_specific_tests(args.test_only, database_url, use_temp_db)
        else:
    
        pass
    pass
            test_results = run_database_tests(database_url, use_temp_db)
        
        # Run benchmarks if requested
        benchmark_results = None
        if args.benchmark:
    
        pass
    pass
            print("\n🏃 Running performance benchmarks...")
            benchmark_results = run_database_benchmarks(database_url)
        
        # Output results
        if args.output_format == 'json':
    
        pass
    pass
            output_json_results(test_results, benchmark_results)
        elif args.output_format == 'csv':
    
        pass
    pass
            output_csv_results(test_results, benchmark_results)
        else:
    pass
            # Console output is already handled by the test suite
        
        # Determine overall success
        failed_tests = [r for r in test_results if not r.success]
        if failed_tests:
    
        pass
    pass
            print(f"\n❌ {len(failed_tests)} tests failed!")
            return CommandResult(
                success=False,
                message=f"Database tests completed with {len(failed_tests)} failures",
                data={
                    'test_results': test_results,
                    'benchmark_results': benchmark_results,
                    'failed_tests': len(failed_tests)
                }
            )
        else:
    pass
            print(f"\n✅ All {len(test_results)} tests passed!")
            return CommandResult(
                success=True,
                message="All database tests passed successfully",
                data={
                    'test_results': test_results,
                    'benchmark_results': benchmark_results,
                    'total_tests': len(test_results)
                }
            )
    
    except Exception as e:
    pass
    pass
        print(f"❌ Error running database tests: {e}")
        return CommandResult(
            success=False,
            message=f"Database test error: {str(e)}",
            data={'error': str(e)}
        )


def run_specific_tests(test_category: str, database_url: Optional[str], use_temp_db: bool):
    pass
    """Run specific category of tests."""
    with DatabaseTestSuite(database_url, use_temp_db) as test_suite:
    
        pass
    pass
        print(f"🧪 Running {test_category} tests...")
        
        if test_category == 'connection':
    
        pass
    pass
            test_suite.test_database_connection()
            test_suite.test_connection_pool()
        elif test_category == 'schema':
    
        pass
    pass
            test_suite.test_schema_creation()
            test_suite.test_schema_integrity()
            test_suite.test_table_constraints()
        elif test_category == 'crud':
    
        pass
    pass
            test_suite.test_crud_operations()
            test_suite.test_bulk_operations()
            test_suite.test_transaction_handling()
        elif test_category == 'performance':
    
        pass
    pass
            test_suite.test_insert_performance()
            test_suite.test_query_performance()
            test_suite.test_index_performance()
        elif test_category == 'integrity':
    
        pass
    pass
            test_suite.test_data_validation()
            test_suite.test_foreign_key_constraints()
        elif test_category == 'concurrent':
    
        pass
    pass
            test_suite.test_concurrent_access()
        
        test_suite._print_summary()
        return test_suite.results


def output_json_results(test_results, benchmark_results):
    pass
    """Output results in JSON format."""
    import json
    
    output = {
        'test_results': [
            {
                'success': r.success,
                'message': r.message,
                'duration': r.duration,
                'timestamp': r.timestamp.isoformat(),
                'details': r.details
            }
            for r in test_results
        ]
    }
    
    if benchmark_results:
    
        pass
    pass
        output['benchmark_results'] = benchmark_results
    
    print(json.dumps(output, indent=2))


def output_csv_results(test_results, benchmark_results):
    pass
    """Output results in CSV format."""
    import csv
    import sys
    
    writer = csv.writer(sys.stdout)
    
    # Write test results
    for result in test_results:
    pass
        writer.writerow([
            result.test_name,
            result.success,
            result.message,
            result.duration,
            result.timestamp.isoformat()
        ])
    
    # Write benchmark results if available
    if benchmark_results:
    
        pass
    pass
        writer.writerow([])  # Empty row
        writer.writerow(['Benchmark Results'])
        for benchmark_name, results in benchmark_results.items():
    pass
            writer.writerow([benchmark_name])
            if isinstance(results, dict):
    
        pass
    pass
                for key, value in results.items():
    pass
                    writer.writerow(['', key, value])


class DatabaseTestCommand(BaseCommand):
    pass
    """Database testing command implementation."""
    
    def run(self, args) -> CommandResult:
    pass
        """Execute the database test command."""
        return handle_database_test(args)