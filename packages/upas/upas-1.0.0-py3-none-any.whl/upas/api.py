"""
UPAS Programmatic API - Compatibility Layer

This module maintains backward compatibility while the actual implementation
has been moved to the api/ module for better organization.
"""

# Import everything from the new modular API explicitly
from .api import (
    ProtocolManager,
    run_protocol,
    create_protocol_manager,
    load_protocol,
    create_engine,
    transition_to_state,
    change_protocol,
)

# Maintain backward compatibility
__all__ = [
    # Core manager
    "ProtocolManager",
    # High-level functions
    "run_protocol",
    "create_protocol_manager",
    "load_protocol",
    # Utility functions
    "create_engine",
    "transition_to_state",
    "change_protocol",
]
