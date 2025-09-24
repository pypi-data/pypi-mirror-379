"""GeneBot Trading Strategies Package."""


# Optional ML strategy
try:
    from .ml_pattern_strategy import MLPatternStrategy
except ImportError:
    MLPatternStrategy = None

__all__ = [
    'StrategyEngine',
    'StrategyRegistry', 
    'SignalProcessor',
    'StrategyConfigManager',
    'BaseStrategy',
    'MovingAverageStrategy',
    'RSIStrategy',
    'MultiIndicatorStrategy',
    'AdvancedMomentumStrategy',
    'MeanReversionStrategy',
    'ATRVolatilityStrategy',
    'MLPatternStrategy'
]