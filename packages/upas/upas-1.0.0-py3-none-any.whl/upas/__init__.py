"""
UPAS - Universal Protocol Analysis & Simulation

A powerful Python framework for protocol analysis and simulation.
"""

__version__ = "1.0.0"
__author__ = "BitsDiver Team"
__email__ = "contact@bitsdiver.com"

# Core components
from .core.engine import ProtocolEngine
from .core.transport import TransportLayer
from .core.behavior import BehaviorExecutor
from .core.packet import PacketBuilder

# High-level API
from .api import (
    run_protocol,
    load_protocol,
    create_engine,
    transition_to_state,
    change_protocol,
    create_protocol_manager,
    ProtocolManager,
)

__all__ = [
    # Core components
    "ProtocolEngine",
    "TransportLayer",
    "BehaviorExecutor",
    "PacketBuilder",
    # High-level API
    "run_protocol",
    "load_protocol",
    "create_engine",
    "transition_to_state",
    "change_protocol",
    "create_protocol_manager",
    "ProtocolManager",
]
