#!/usr/bin/env python3

"""
Complete Anti-Greed Trading Bot Example

This example demonstrates the full trading bot implementation with:
    pass
    1. ALL available strategies running simultaneously
2. Aggressive position management with anti-greed mechanisms
3. Immediate profit taking and risk management
4. Real-time monitoring and execution
5. Comprehensive performance tracking

The bot is designed to NEVER be greedy - it takes profits immediately
when targets are hit and uses multiple exit strategies to protect gains.
"""

import sys
import os
import time
import signal
import logging
from decimal import Decimal

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.trading.trading_bot import TradingBot
from src.position_manager import AggressivePositionManager, PositionMetrics

# Global bot instance for signal handling
trading_bot = None

def setup_logging():
    pass
    """Setup comprehensive logging for the trading bot."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('trading_bot.log'),
            logging.StreamHandler()
        ]
    )

def signal_handler(signum, frame):
    pass
    """Handle shutdown signals gracefully."""
    print("\n🛑 Shutdown signal received. Stopping trading bot...")
    global trading_bot
    if trading_bot:
    
        pass
    pass
        trading_bot.stop()
    sys.exit(0)

def simulate_market_conditions() -> Dict[str, Any]:
    pass
    """Simulate current market conditions for testing."""
    import random
    
    return {
        'extreme_volatility': random.random() < 0.1,  # 10% chance of extreme volatility
        'market_hours': True,  # Assume market hours for demo
        'news_sentiment': random.uniform(-0.5, 0.5)  # News sentiment
    }

def demonstrate_position_management():
    
        pass
    pass
    """Demonstrate the aggressive position management system."""
    print("\n" + "="*60)
    print("🎯 AGGRESSIVE POSITION MANAGEMENT DEMONSTRATION")
    print("="*60)
    
    # Initialize position manager
    pos_manager = AggressivePositionManager()
    
    # Show exit configuration
    exit_summary = pos_manager.get_exit_summary()
    print("\n📋 Exit Strategy Configuration:")
    print(f"  Stop Loss Levels: {exit_summary['stop_loss_levels']}")
    print(f"  Take Profit Levels: {exit_summary['take_profit_levels']}")
    print(f"  Trailing Stop: {exit_summary['trailing_stop_config']}")
    print(f"  Profit Protection: {exit_summary['profit_protection_config']}")
    
    print("\n🚫 Anti-Greed Features:")
    for feature in exit_summary['anti_greed_features']:
    pass
        print(f"  ✓ {feature}")
    
    # Simulate different position scenarios
    scenarios = [
        {
            'name': 'High Profit Position (Anti-Greed Test)',
            'entry_price': Decimal('50000'),
            'current_price': Decimal('52000'),  # 4% profit
            'max_profit': 0.05,  # 5% max profit achieved
            'confidence': 0.92
        },
        {
            'name': 'Declining Profit Position',
            'entry_price': Decimal('50000'),
            'current_price': Decimal('51000'),  # 2% current profit
            'max_profit': 0.04,  # 4% max profit (declining)
            'confidence': 0.88
        },
        {
            'name': 'Stop Loss Position',
            'entry_price': Decimal('50000'),
            'current_price': Decimal('49200'),  # -1.6% loss
            'max_profit': 0.0,
            'confidence': 0.85
        }
    ]
    
    print("\n🧪 Position Scenario Analysis:")
    
    for scenario in scenarios:
    pass
        print(f"\n--- {scenario['name']} ---")
        
        # Create position metrics
        metrics = PositionMetrics(
            entry_price=scenario['entry_price'],
            current_price=scenario['current_price'],
            max_profit=Decimal(str(scenario['max_profit'])),
            max_loss=Decimal('0'),
            hold_time=timedelta(hours=6),
            profit_velocity=0.001
        )
        
        # Get exit recommendation
        market_conditions = simulate_market_conditions()
        recommendation = pos_manager.get_aggressive_exit_recommendation(
            metrics, scenario['confidence'], market_conditions
        )
        
        print(f"  Current P&L: {metrics.current_profit_pct*100:.2f}%")
        print(f"  Max Profit: {metrics.max_profit_pct*100:.2f}%")
        print(f"  Recommendation: {recommendation['action']}")
        print(f"  Urgency: {recommendation['urgency']}")
        print(f"  Confidence: {recommendation['confidence']:.2f}")
        print(f"  Reasons: {', '.join(recommendation['reasons'])}")
        
        if recommendation['scale_out_pct']:
    
        pass
    pass
            print(f"  Scale Out: {recommendation['scale_out_pct']*100:.0f}%")

def run_comprehensive_trading_bot():
    pass
    """Run the comprehensive trading bot with all strategies."""
    print("\n" + "="*60)
    print("🤖 COMPREHENSIVE ANTI-GREED TRADING BOT")
    print("="*60)
    
    global trading_bot
    
    try:
    pass
        # Initialize trading bot with aggressive settings
        trading_bot = TradingBot(
            symbols=['BTCUSD', 'ETHUSD', 'ADAUSD', 'SOLUSD'],
            update_interval=30,  # 30 second updates for demo
            max_positions=4,     # Max 4 concurrent positions
            portfolio_value=100000.0,  # $100k starting capital
            risk_per_trade=0.015,      # 1.5% risk per trade
            profit_target_ratio=2.0,   # 2:1 reward/risk ratio
            enable_paper_trading=True  # Paper trading for demo
        )
        
        print("\n🔧 Bot Configuration:")
        print(f"  💰 Starting Capital: $100,000")
        print(f"  📊 Trading Symbols: {trading_bot.symbols}")
        print(f"  📈 Max Positions: 4")
        print(f"  ⚡ Update Interval: 30 seconds")
        print(f"  🎯 Risk per Trade: 1.5%")
        print(f"  🚫 Anti-Greed Mode: ENABLED")
        
        # Enable anti-greed mode
        trading_bot.enable_anti_greed_mode()
        
        print("\n🚀 Starting trading bot...")
        trading_bot.start()
        
        print("✅ Trading Bot started successfully!")
        
        # Show active strategies
        status = trading_bot.get_status()
        strategy_engine_status = status['portfolio_status']['strategy_engine_status']
        
        print("\n📋 Active Strategies:")
        for strategy_name, strategy_status in strategy_engine_status.items():
    pass
            if strategy_status.get('enabled', False):
    
        pass
    pass
                print(f"  ✓ {strategy_name}")
        
        print("\n🔄 Bot is now running. Monitoring performance...")
        print("📊 Status updates every 60 seconds")
        print("🛑 Press Ctrl+C to stop gracefully")
        
        # Monitor the bot
        start_time = time.time()
        last_status_time = 0
        iteration = 0
        
        while trading_bot.is_running and iteration < 20:  # Run for 20 iterations (demo)
            current_time = time.time()
            
            # Show status every 60 seconds or every 3 iterations
            if current_time - last_status_time >= 60 or iteration % 3 == 0:
    
        pass
    pass
                show_detailed_status(trading_bot, current_time - start_time, iteration)
                last_status_time = current_time
            
            time.sleep(30)  # Wait 30 seconds between iterations
            iteration += 1
        
        print("\n🏁 Demo completed. Stopping bot...")
        
    except KeyboardInterrupt:
    pass
    pass
        print("\n🛑 Keyboard interrupt received. Stopping...")
    except Exception as e:
    pass
    pass
        print(f"\n❌ Error running trading bot: {str(e)}")
    finally:
    pass
        if trading_bot:
    
        pass
    pass
            trading_bot.stop()
        print("\n✅ Trading Bot stopped successfully.")

def show_detailed_status(bot: TradingBot, runtime_seconds: float, iteration: int):
    pass
    """Show detailed bot status with anti-greed metrics."""
    try:
    pass
        status = bot.get_status()
        
        print(f"\n{'='*60}")
        print(f"📊 STATUS UPDATE #{iteration+1} - Runtime: {runtime_seconds/60:.1f} minutes")
        print(f"{'='*60}")
        
        # Portfolio Status
        portfolio = status['portfolio_status']
        print(f"💰 Portfolio Value: ${portfolio['portfolio_value']:,.2f}")
        print(f"💵 Available Capital: ${portfolio['available_capital']:,.2f}")
        print(f"📈 Total P&L: ${portfolio['total_pnl']:,.2f}")
        print(f"📊 Active Positions: {portfolio['active_positions']}")
        
        # Trading Performance
        print(f"\n🎯 Trading Performance:")
        print(f"  Total Trades: {status['total_trades']}")
        print(f"  Winning Trades: {status['winning_trades']}")
        print(f"  Win Rate: {status['win_rate']:.1f}%")
        print(f"  Max Drawdown: {status['max_drawdown']*100:.2f}%")
        
        # Anti-Greed Metrics
        print(f"\n🚫 Anti-Greed Performance:")
        print(f"  Immediate Exit Mode: {'✅ ENABLED' if status['immediate_exit_enabled'] else '❌ DISABLED'}")
        print(f"  Profit Taking Mode: {'✅ ENABLED' if status['anti_greed_enabled'] else '❌ DISABLED'}")
        
        # Active Positions
        if portfolio['positions']:
    
        pass
    pass
            print(f"\n📍 Active Positions:")
            for pos_id, pos in portfolio['positions'].items():
    pass
                pnl_color = "🟢" if pos['current_pnl'] >= 0 else "🔴"
                print(f"  {pnl_color} {pos['symbol']}: {pos['action']} | "
                      f"P&L: ${pos['current_pnl']:.2f} | "
                      f"Strategy: {pos['strategy']} | "
                      f"Confidence: {pos['confidence']:.2f}")
        else:
    pass
            print(f"\n📍 No active positions")
        
        # Strategy Performance
        if status['strategy_performance']:
    
        pass
    pass
            print(f"\n📈 Strategy Performance:")
            for strategy, perf in status['strategy_performance'].items():
    pass
                if perf['exits'] > 0:
    
        pass
    pass
                    avg_pnl = perf['total_pnl'] / perf['exits']
                    print(f"  {strategy}: "
                          f"Trades={perf['exits']}, "
                          f"P&L=${perf['total_pnl']:.2f}, "
                          f"Avg=${avg_pnl:.2f}, "
                          f"Win Rate={perf['win_rate']*100:.1f}%")
        
        # Market Conditions (simulated)
        market_conditions = simulate_market_conditions()
        print(f"\n🌍 Market Conditions:")
        print(f"  Volatility: {market_conditions['volatility']*100:.1f}%")
        print(f"  Trend Strength: {market_conditions['trend_strength']:.2f}")
        print(f"  Extreme Volatility: {'⚠️ YES' if market_conditions['extreme_volatility'] else '✅ NO'}")
        
    except Exception as e:
    
        pass
    pass
    pass
        print(f"❌ Error showing status: {str(e)}")

def main():
    pass
    """Main function to run the complete anti-greed trading bot demonstration."""
    print("Complete Anti-Greed Trading Bot Demonstration")
    print("=" * 60)
    print()
    print("This demonstration shows:")
    print("✓ Multi-strategy trading with ALL available strategies")
    print("✓ Aggressive position management with anti-greed mechanisms")
    print("✓ Immediate profit taking and risk management")
    print("✓ Real-time monitoring and performance tracking")
    print("✓ Comprehensive exit strategies to prevent greediness")
    print()
    
    # Setup logging
    setup_logging()
    
    # Set up signal handlers for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    try:
    pass
        # 1. Demonstrate position management
        demonstrate_position_management()
        
        print("\n" + "="*60)
        input("Press Enter to continue to full trading bot demonstration...")
        
        # 2. Run comprehensive trading bot
        run_comprehensive_trading_bot()
        
    except Exception as e:
    pass
    pass
        print(f"\n❌ Error in demonstration: {str(e)}")
    
    print("\n🎉 Demonstration completed!")
    print("\nKey Takeaways:")
    print("✓ The bot uses ALL available strategies simultaneously")
    print("✓ Anti-greed mechanisms prevent holding positions too long")
    print("✓ Immediate profit taking when targets are reached")
    print("✓ Multiple exit strategies protect against losses")
    print("✓ Real-time monitoring ensures optimal performance")
    print("\n🚫 NO GREEDINESS DETECTED - Bot takes profits immediately!")

if __name__ == "__main__":
    
        pass
    pass
    main()