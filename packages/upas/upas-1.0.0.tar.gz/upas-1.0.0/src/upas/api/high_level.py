"""
High-level API functions for easy protocol execution
"""

import asyncio
import json
from pathlib import Path
from typing import Union, Dict, Any

from .manager import ProtocolManager


def create_protocol_manager(variables: dict = None) -> ProtocolManager:
    """
    Create a protocol manager with initial variables.

    Args:
        variables: Dictionary of initial variables

    Returns:
        ProtocolManager instance
    """
    manager = ProtocolManager()
    if variables:
        for key, value in variables.items():
            manager.set_variable(key, value)
    return manager


async def run_protocol(
    protocol_path: Union[str, Path],
    duration: float = None,
    variables: dict = None,
) -> dict:
    """
    High-level async function to run a protocol.

    Args:
        protocol_path: Protocol file path, JSON string, or dict
        duration: Optional duration in seconds (None = infinite)
        variables: Optional variables to set

    Returns:
        Dictionary with execution results

    Example:
        ```python
        import upas

        # Run protocol for 30 seconds
        result = await upas.run_protocol('protocol.json', duration=30)

        # Run with variables
        result = await upas.run_protocol(
            'protocol.json',
            duration=60,
            variables={'target': '192.168.1.1', 'interval': 5}
        )
        ```
    """
    manager = ProtocolManager()

    # Set variables if provided
    if variables:
        for key, value in variables.items():
            manager.set_variable(key, value)

    try:
        # Load and start protocol
        await manager.load_protocol(protocol_path)
        await manager.start_async_new()

        # Run for specified duration
        if duration:
            await asyncio.sleep(duration)
            await manager.stop_async()

        # Return execution info
        return {
            "success": True,
            "duration": duration,
            "protocol_info": manager.get_protocol_info(),
            "variables": manager.get_all_variables(),
        }

    except Exception as e:
        await manager.cleanup()
        return {"success": False, "error": str(e), "duration": duration}


def load_protocol(protocol_path: Union[str, Path]) -> Dict[str, Any]:
    """
    Load and validate a protocol file.

    Args:
        protocol_path: Path to protocol file

    Returns:
        Protocol data dictionary

    Example:
        ```python
        import upas

        # Load protocol
        protocol_data = upas.load_protocol('examples/simple_beacon.json')
        print(f"Protocol: {protocol_data['name']}")
        ```
    """
    if isinstance(protocol_path, (str, Path)):
        if isinstance(protocol_path, str) and protocol_path.strip().startswith("{"):
            # JSON string
            return json.loads(protocol_path)
        else:
            # File path
            with open(protocol_path, "r", encoding="utf-8") as f:
                return json.load(f)
    else:
        raise ValueError(f"Unsupported protocol path type: {type(protocol_path)}")
