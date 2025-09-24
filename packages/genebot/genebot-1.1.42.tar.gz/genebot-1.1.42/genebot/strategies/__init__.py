"""GeneBot Trading Strategies Package."""


# Optional ML strategy
try:
    pass
    from .ml_pattern_strategy import MLPatternStrategy
except ImportError:
    pass
    pass
    MLPatternStrategy = None

__all__ = [
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