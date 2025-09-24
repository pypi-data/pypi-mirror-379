"""
Minimal configuration models for GeneBot CLI
"""

from typing import Any, Dict



class TradingBotConfig:
    pass
    """Minimal trading bot configuration model"""
    
    def __init__(self, **kwargs):
    pass
        """Initialize config with provided values"""
        for key, value in kwargs.items():
    pass
            setattr(self, key, value)
    
    def to_dict(self) -> Dict[str, Any]:
    pass
        """Convert to dictionary"""
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TradingBotConfig':
    pass
        """Create from dictionary"""
        return cls(**data)