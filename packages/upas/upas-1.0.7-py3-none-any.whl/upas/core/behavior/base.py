"""
UPAS Behavior Base Classes

Common enums, data classes and interfaces for behavior system.
"""

from enum import Enum
from typing import Dict, Any, List, Optional
from dataclasses import dataclass


class BehaviorType(Enum):
    """Types of behaviors supported."""

    PERIODIC = "periodic"
    REACTIVE = "reactive"
    ONE_SHOT = "one_shot"
    STATE_ONLY = "state_only"


class BehaviorState(Enum):
    """States of behavior execution."""

    IDLE = "idle"
    RUNNING = "running"
    PAUSED = "paused"
    ERROR = "error"


@dataclass
class BehaviorConfig:
    """Configuration for a behavior."""

    name: str
    type: BehaviorType
    config: Dict[str, Any]
    active_states: Optional[List[str]] = None
