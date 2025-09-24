#!/usr/bin/env python3
"""
Error Handling and Recovery Example

This example demonstrates the comprehensive error handling and recovery
mechanisms implemented in the trading bot, including:
    pass
1. Custom exception hierarchy
2. Retry logic with exponential backoff
3. Circuit breaker pattern
4. Graceful degradation
"""

import asyncio
import logging
import random
import sys
from pathlib import Path
from typing import Dict, Any

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import centralized logging system
from genebot.logging.factory import setup_global_config, get_logger
from genebot.logging.config import get_default_config
from genebot.logging.context import LogContext, set_context

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from src.utils.circuit_breaker import circuit_breaker, CircuitBreaker
)


class MockExchangeService:
    pass
    pass
    """Mock exchange service that simulates various failure scenarios."""
    
    def __init__(self):
    pass
        self.failure_rate = 0.3  # 30% failure rate
        self.call_count = 0
        self.consecutive_failures = 0
    
    @retry_with_backoff(max_retries=3, initial_delay=0.5)
    @circuit_breaker("mock_exchange", failure_threshold=5, timeout=10.0)
    async def get_market_data(self, symbol: str) -> Dict[str, Any]:
    pass
        """Simulate getting market data with potential failures."""
        self.call_count += 1
        
        # Simulate network issues
        if random.random() < self.failure_rate:
    
        pass
    pass
            self.consecutive_failures += 1
            if self.consecutive_failures > 3:
    
        pass
    pass
                raise NetworkException(
                    f"Network timeout getting data for {symbol}",
                    status_code=504,
                    retry_after=5
                )
            else:
    pass
                raise RetryableException(f"Temporary error for {symbol}")
        
        # Success case
        self.consecutive_failures = 0
        return {
            'symbol': symbol,
            'price': 50000 + random.randint(-1000, 1000),
            'volume': random.randint(1000, 10000),
            'timestamp': '2024-01-01T12:00:00Z'
        }
    
    async def place_order(self, symbol: str, side: str, amount: float) -> Dict[str, Any]:
    pass
        """Simulate placing an order with potential failures."""
        if random.random() < 0.1:  # 10% failure rate
            raise ExchangeException(f"Order rejected for {symbol}")
        
        return {
            'order_id': f"order_{random.randint(1000, 9999)}",
            'symbol': symbol,
            'side': side,
            'amount': amount,
            'status': 'filled'
        }


class MockStrategyService:
    pass
    """Mock strategy service that can fail."""
    
    def __init__(self):
    pass
        self.enabled = True
        self.failure_count = 0
    
    async def generate_signals(self, market_data: Dict[str, Any]) -> Dict[str, Any]:
    pass
        """Generate trading signals with potential failures."""
        if not self.enabled:
    
        pass
    pass
            raise StrategyException("Strategy is disabled")
        
        # Simulate occasional strategy failures
        if random.random() < 0.05:  # 5% failure rate
            self.failure_count += 1
            raise StrategyException(f"Strategy calculation failed")
        
        return {
            'signal': random.choice(['BUY', 'SELL', 'HOLD']),
            'confidence': random.uniform(0.6, 0.95),
            'strategy': 'mock_strategy'
        }


async def demonstrate_error_handling():
    pass
    """Demonstrate comprehensive error handling capabilities."""
    # Setup centralized logging
    config = get_default_config()
    setup_global_config(config)
    
    # Set example context
    example_context = LogContext(
        component="examples",
        operation="error_handling",
        session_id=f"example_{int(asyncio.get_event_loop().time())}"
    )
    set_context(example_context)
    
    logger = get_logger('examples.error_handling')
    logger.info("Starting Error Handling and Recovery Demonstration")
    
    print("🚀 Starting Error Handling and Recovery Demonstration\n")
    
    # Initialize services
    exchange_service = MockExchangeService()
    strategy_service = MockStrategyService()
    
    # Register components with graceful degradation manager
    graceful_degradation_manager.register_component(
        "exchange_service",
        fallback_handler=lambda error: print(f"📉 Exchange fallback: {error}"),
        critical=True
    )
    
    graceful_degradation_manager.register_component(
        "strategy_service",
        fallback_handler=lambda error: print(f"🧠 Strategy fallback: {error}"),
        critical=False
    )
    
    # Start health monitoring
    await graceful_degradation_manager.start_health_monitoring()
    
    print("1. Testing Retry Logic with Exponential Backoff")
    print("=" * 50)
    
    # Test retry logic
    for i in range(5):
    pass
        try:
    pass
            data = await exchange_service.get_market_data("BTC/USD")
            print(f"✅ Successfully got market data: ${data['price']:,}")
        except Exception as e:
    pass
    pass
            print(f"❌ Failed to get market data: {e}")
            await graceful_degradation_manager.record_component_error("exchange_service", e)
    
    print(f"\n📊 Exchange service stats: {exchange_service.call_count} calls made")
    
    print("\n2. Testing Circuit Breaker Pattern")
    print("=" * 50)
    
    # Create a circuit breaker for testing
    cb = CircuitBreaker("test_service", failure_threshold=3, timeout=5.0)
    
    async def failing_service():
    pass
        if random.random() < 0.8:  # 80% failure rate
            raise ExchangeException("Service unavailable")
        return "Success"
    
    # Test circuit breaker
    for i in range(8):
    pass
        try:
    pass
            result = await cb.call(failing_service)
            print(f"✅ Call {i+1}: {result}")
        except CircuitBreakerException as e:
    pass
    pass
            print(f"⚡ Call {i+1}: Circuit breaker is open - {e}")
        except ExchangeException as e:
    pass
    pass
            print(f"❌ Call {i+1}: Service failed - {e}")
    
    print(f"\n📊 Circuit breaker stats: {cb.get_stats()}")
    
    print("\n3. Testing Graceful Degradation")
    print("=" * 50)
    
    # Simulate component failures
    await graceful_degradation_manager.update_component_status(
        "exchange_service",
        ComponentStatus.DEGRADED,
        "High latency detected"
    )
    
    # Check system health
    health = graceful_degradation_manager.get_system_health()
    print(f"🏥 System Health:")
    print(f"   Service Level: {health['service_level']}")
    print(f"   Health: {health['health_percentage']:.1f}%")
    print(f"   Available: {health['availability_percentage']:.1f}%")
    
    # Test operation execution with degraded components
    if graceful_degradation_manager.can_execute_operation(["exchange_service"]):
    
        pass
    pass
        print("✅ Can still execute trading operations")
    else:
    pass
        print("❌ Cannot execute trading operations")
    
    print("\n4. Testing Strategy Error Handling")
    print("=" * 50)
    
    # Test strategy with error handling
    for i in range(3):
    pass
        try:
    pass
            market_data = {'symbol': 'ETH/USD', 'price': 3000}
            signals = await strategy_service.generate_signals(market_data)
            print(f"✅ Generated signal: {signals['signal']} (confidence: {signals['confidence']:.2f})")
        except StrategyException as e:
    pass
    pass
            print(f"❌ Strategy failed: {e}")
            await graceful_degradation_manager.record_component_error("strategy_service", e)
    
    print("\n5. Final System Status")
    print("=" * 50)
    
    # Get final system health
    final_health = graceful_degradation_manager.get_system_health()
    print(f"🏥 Final System Health:")
    print(f"   Service Level: {final_health['service_level']}")
    print(f"   Total Components: {final_health['total_components']}")
    print(f"   Healthy Components: {final_health['healthy_components']}")
    print(f"   Available Components: {final_health['available_components']}")
    
    # Show component details
    print(f"\n📋 Component Status:")
    for name, status in final_health['components'].items():
    pass
        status_emoji = {
            'healthy': '✅',
            'degraded': '⚠️',
            'failed': '❌',
            'disabled': '🚫'
        }.get(status['status'], '❓')
        
        print(f"   {status_emoji} {name}: {status['status']}")
        if status['error_count'] > 0:
    
        pass
    pass
            print(f"      Errors: {status['error_count']}")
            if status['last_error']:
    
        pass
    pass
                print(f"      Last Error: {status['last_error']}")
    
    # Stop health monitoring
    await graceful_degradation_manager.stop_health_monitoring()
    
    print("\n🎉 Error Handling Demonstration Complete!")


if __name__ == "__main__":
    
        pass
    pass
    asyncio.run(demonstrate_error_handling())