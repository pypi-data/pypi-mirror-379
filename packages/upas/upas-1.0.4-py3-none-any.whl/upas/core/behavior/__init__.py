"""
UPAS Behavior Package

Modular behavior system with support for periodic, reactive, and one-shot behaviors.
"""

# Import the main classes for backward compatibility
from .executor import BehaviorExecutor
from .base import BehaviorType, BehaviorState, BehaviorConfig

# Import modular components for advanced usage
from .payload import PayloadBuilder, VariableResolver, CounterManager
from .state import ExecutionContext
from .scheduling import BehaviorScheduler, TimingManager
from .types import PeriodicBehavior, ReactiveBehavior, TriggeredBehavior
from .responses import MultiPacketResponseManager, ResponseMode
from .state_behaviors import (
    StateOnlyBehaviorManager,
    StateTransition,
    StateTransitionType,
)

__all__ = [
    # Main classes (backward compatibility)
    "BehaviorExecutor",
    "BehaviorType",
    "BehaviorState",
    "BehaviorConfig",
    # Modular components
    "PayloadBuilder",
    "VariableResolver",
    "CounterManager",
    "ExecutionContext",
    "BehaviorScheduler",
    "TimingManager",
    # Behavior types
    "PeriodicBehavior",
    "ReactiveBehavior",
    "TriggeredBehavior",
    # New features
    "MultiPacketResponseManager",
    "ResponseMode",
    "StateOnlyBehaviorManager",
    "StateTransition",
    "StateTransitionType",
]
