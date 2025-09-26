"""
Utility functions for protocol management
"""

import logging
from typing import Union, Dict, Any
from pathlib import Path

from ..core.engine import ProtocolEngine
from .manager import ProtocolManager


def create_engine() -> ProtocolEngine:
    """
    Create a new protocol engine instance.

    Returns:
        ProtocolEngine instance

    Example:
        ```python
        import upas

        # Create engine
        engine = upas.create_engine()
        ```
    """
    return ProtocolEngine()


def transition_to_state(manager: ProtocolManager, state: str) -> bool:
    """
    Utility function to transition protocol manager to a specific state.

    Args:
        manager: ProtocolManager instance
        state: Target state name

    Returns:
        True if transition successful, False otherwise

    Example:
        ```python
        import upas

        manager = upas.ProtocolManager()
        # ... load and start protocol ...

        # Transition to a specific state
        success = upas.transition_to_state(manager, 'CONNECTED')
        ```
    """
    if not isinstance(manager, ProtocolManager):
        raise ValueError("First argument must be a ProtocolManager instance")

    return manager.transition_to_state(state)


def change_protocol(
    manager: ProtocolManager, new_protocol: Union[str, Path, Dict[str, Any]]
) -> bool:
    """
    Utility function to change protocol on a protocol manager.

    Args:
        manager: ProtocolManager instance
        new_protocol: New protocol file path, JSON string, or dict

    Returns:
        True if protocol change successful, False otherwise

    Example:
        ```python
        import upas

        manager = upas.ProtocolManager()
        # ... load and start protocol ...

        # Change to a different protocol
        success = upas.change_protocol(manager, 'new_protocol.json')
        ```
    """
    if not isinstance(manager, ProtocolManager):
        raise ValueError("First argument must be a ProtocolManager instance")

    return manager.change_protocol(new_protocol)


def validate_protocol_data(protocol_data: Dict[str, Any]) -> bool:
    """
    Validate protocol data structure.

    Args:
        protocol_data: Protocol data dictionary

    Returns:
        True if valid, False otherwise
    """
    required_fields = ["name", "behaviors"]

    if not isinstance(protocol_data, dict):
        logging.error("Protocol data must be a dictionary")
        return False

    for field in required_fields:
        if field not in protocol_data:
            logging.error(f"Missing required field: {field}")
            return False

    if not isinstance(protocol_data["behaviors"], list):
        logging.error("Behaviors must be a list")
        return False

    return True


def get_protocol_variables(manager: ProtocolManager) -> Dict[str, Any]:
    """
    Get all variables from a protocol manager.

    Args:
        manager: ProtocolManager instance

    Returns:
        Dictionary of variables
    """
    if not isinstance(manager, ProtocolManager):
        raise ValueError("Argument must be a ProtocolManager instance")

    return manager.get_all_variables()


def set_protocol_variables(manager: ProtocolManager, variables: Dict[str, Any]) -> None:
    """
    Set multiple variables on a protocol manager.

    Args:
        manager: ProtocolManager instance
        variables: Dictionary of variables to set
    """
    if not isinstance(manager, ProtocolManager):
        raise ValueError("First argument must be a ProtocolManager instance")

    if not isinstance(variables, dict):
        raise ValueError("Variables must be a dictionary")

    for key, value in variables.items():
        manager.set_variable(key, value)
