"""
UPAS Core Behavior System

Backward compatibility layer for the refactored behavior module.
"""

# Import all classes from the new modular structure for backward compatibility
from .behavior.executor import BehaviorExecutor
from .behavior.base import BehaviorType, BehaviorState, BehaviorConfig

# Re-export everything to maintain backward compatibility
__all__ = [
    "BehaviorExecutor",
    "BehaviorType",
    "BehaviorState",
    "BehaviorConfig",
]
