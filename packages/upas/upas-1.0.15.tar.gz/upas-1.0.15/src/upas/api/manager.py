"""
Protocol Manager - Core protocol control and management
"""

import asyncio
import json
import logging
import threading
import time
from pathlib import Path
from typing import Optional, Dict, Any, Union, Callable

from ..core.engine import ProtocolEngine


class ProtocolManager:
    """
    High-level protocol manager for programmatic control.

    Allows dynamic state transitions, protocol switching, and
    event-driven protocol execution.
    """

    def __init__(self, protocol_data: Union[str, Path, Dict[str, Any]] = None):
        """
        Initialize protocol manager.

        Args:
            protocol_data: Protocol file path, JSON string, or dict (optional)
        """
        self.protocol_data = (
            self._load_protocol_data(protocol_data) if protocol_data else None
        )
        self.engine = ProtocolEngine()
        self.running = False
        self._stop_event = threading.Event()
        self._thread = None
        self._state_callbacks = {}
        self._protocol_callbacks = {}
        self._protocol_loaded = False
        self._variables = {}  # Local variable storage

    def _load_protocol_data(
        self, protocol_data: Union[str, Path, Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Load protocol data from various sources."""
        if isinstance(protocol_data, dict):
            return protocol_data
        elif isinstance(protocol_data, (str, Path)):
            if isinstance(protocol_data, str) and protocol_data.strip().startswith("{"):
                # JSON string
                return json.loads(protocol_data)
            else:
                # File path
                with open(protocol_data, "r", encoding="utf-8") as f:
                    return json.load(f)
        else:
            raise ValueError(f"Unsupported protocol data type: {type(protocol_data)}")

    async def _load_protocol_into_engine(self):
        """Load protocol data into engine."""
        if not self.protocol_data:
            raise ValueError("No protocol data to load")

        try:
            # Load protocol data directly into engine
            self.engine.protocol_definition = self.protocol_data

            # Register custom functions if present
            if "functions" in self.protocol_data:
                self.engine.function_registry.register_functions_from_protocol(
                    self.protocol_data["functions"]
                )
                logging.info(
                    f"Registered {len(self.protocol_data['functions'])} custom functions"
                )

            # Initialize state machine if present
            if "state_machine" in self.protocol_data:
                self.engine._setup_state_machine(self.protocol_data["state_machine"])
                logging.info("State machine initialized")

            # Setup transports
            if "transports" in self.protocol_data:
                await self.engine.transport_layer.register_transports(
                    self.protocol_data["transports"]
                )

            # Setup behaviors with function registry and state machine
            if "behaviors" in self.protocol_data:
                # Merge local variables with protocol variables
                protocol_vars = self.protocol_data.get("variables", {})
                protocol_vars.update(self._variables)

                await self.engine.behavior_executor.setup_behaviors(
                    self.protocol_data["behaviors"],
                    self.engine.function_registry,
                    self.engine.state_machine,
                    protocol_vars,
                    self.engine.transport_layer,
                )

            logging.info(
                f"Protocol loaded successfully: {self.protocol_data.get('name', 'Unknown')}"
            )

        except Exception as e:
            logging.error(f"Failed to load protocol: {e}")
            raise

    async def start_async(self, duration: Optional[float] = None) -> None:
        """
        Start protocol execution asynchronously.

        Args:
            duration: Optional duration in seconds (None = infinite)
        """
        if self.running:
            raise RuntimeError("Protocol is already running")

        await self._load_protocol_into_engine()
        self.running = True

        try:
            start_time = time.time()
            await self.engine.start()

            # Wait for the specified duration or until stopped
            while self.running:
                # Check duration
                if duration and (time.time() - start_time) >= duration:
                    break

                # Check for state transitions
                current_state = self.get_current_state()
                if current_state and current_state in self._state_callbacks:
                    self._state_callbacks[current_state]()

                await asyncio.sleep(0.1)  # Wait a bit

        except Exception as e:
            logging.error(f"Protocol execution error: {e}")
        finally:
            await self.engine.stop()
            self.running = False

    def start(self, duration: Optional[float] = None) -> None:
        """
        Start protocol execution synchronously.

        Args:
            duration: Optional duration in seconds (None = infinite)
        """
        if self.running:
            raise RuntimeError("Protocol is already running")

        self.running = True
        self._stop_event.clear()

        def _run():
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(self.start_async(duration))
            except Exception as e:
                logging.error(f"Protocol execution error: {e}")
            finally:
                self.running = False

        self._thread = threading.Thread(target=_run, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        """Stop protocol execution."""
        if self.running:
            self.running = False
            self._stop_event.set()
            if self._thread:
                self._thread.join(timeout=5.0)

    def transition_to_state(self, state: str) -> bool:
        """
        Transition to a specific state.

        Args:
            state: Target state name

        Returns:
            True if transition successful, False otherwise
        """
        if not self.engine or not hasattr(self.engine, "state_machine"):
            return False

        try:
            return self.engine.state_machine.transition_to(state)
        except Exception as e:
            logging.error(f"State transition failed: {e}")
            return False

    def change_protocol(self, new_protocol: Union[str, Path, Dict[str, Any]]) -> bool:
        """
        Change to a different protocol.

        Args:
            new_protocol: New protocol file path, JSON string, or dict

        Returns:
            True if protocol change successful, False otherwise
        """
        try:
            was_running = self.running

            # Stop current protocol if running
            if was_running:
                self.stop()

            # Load new protocol
            self.protocol_data = self._load_protocol_data(new_protocol)
            self._protocol_loaded = False

            # Restart if it was running
            if was_running:
                self.start()

            # Notify callbacks
            for callback in self._protocol_callbacks.values():
                callback()

            return True

        except Exception as e:
            logging.error(f"Protocol change failed: {e}")
            return False

    def register_state_callback(self, state: str, callback: Callable[[], None]) -> None:
        """
        Register callback for state transitions.

        Args:
            state: State name to monitor
            callback: Function to call when entering this state
        """
        self._state_callbacks[state] = callback

    def register_protocol_callback(
        self, name: str, callback: Callable[[], None]
    ) -> None:
        """
        Register callback for protocol changes.

        Args:
            name: Callback identifier
            callback: Function to call when protocol changes
        """
        self._protocol_callbacks[name] = callback

    def get_current_state(self) -> Optional[str]:
        """Get current state."""
        if self.engine and self.engine.state_machine:
            return self.engine.state_machine.current_state
        return None

    def get_variables(self) -> Dict[str, Any]:
        """Get current protocol variables."""
        return dict(self._variables)

    def set_variable(self, name: str, value: Any) -> None:
        """
        Set protocol variable.

        Args:
            name: Variable name
            value: Variable value
        """
        self._variables[name] = value
        # Also set on engine if it has variables
        if self.engine and hasattr(self.engine, "variables"):
            self.engine.variables[name] = value

    def get_variable(self, name: str) -> Any:
        """
        Get protocol variable.

        Args:
            name: Variable name

        Returns:
            Variable value or None if not found
        """
        return self._variables.get(name)

    def get_all_variables(self) -> Dict[str, Any]:
        """Get all protocol variables."""
        return dict(self._variables)

    def remove_variable(self, name: str) -> bool:
        """
        Remove a protocol variable.

        Args:
            name: Variable name

        Returns:
            True if variable was removed, False if not found
        """
        removed = self._variables.pop(name, None) is not None
        # Also remove from engine if it has variables
        if self.engine and hasattr(self.engine, "variables"):
            self.engine.variables.pop(name, None)
        return removed

    async def load_protocol(
        self, protocol_path: Union[str, Path, Dict[str, Any]]
    ) -> None:
        """
        Load protocol from file or dict.

        Args:
            protocol_path: Protocol file path, JSON string, or dict
        """
        self.protocol_data = self._load_protocol_data(protocol_path)
        await self._load_protocol_into_engine()
        self._protocol_loaded = True

    def get_protocol_info(self) -> Dict[str, Any]:
        """Get information about the loaded protocol."""
        if self.protocol_data:
            return {
                "name": self.protocol_data.get("name", "Unknown"),
                "version": self.protocol_data.get("version", "1.0"),
                "description": self.protocol_data.get("description", ""),
                "loaded": self._protocol_loaded,
            }
        return {"loaded": False}

    async def start_async_new(self) -> None:
        """Start protocol execution asynchronously."""
        if not self._protocol_loaded:
            raise RuntimeError("No protocol loaded. Call load_protocol() first.")

        if self.running:
            raise RuntimeError("Protocol is already running")

        await self._load_protocol_into_engine()
        self.running = True

        try:
            await self.engine.start()
        except Exception as e:
            self.running = False
            logging.error(f"Failed to start protocol: {e}")
            raise

    async def stop_async(self) -> None:
        """Stop protocol execution asynchronously."""
        if self.running:
            try:
                await self.engine.stop()
            except Exception as e:
                logging.error(f"Error stopping protocol: {e}")
            finally:
                self.running = False

    async def cleanup(self) -> None:
        """Clean up resources."""
        if self.running:
            await self.stop_async()

        if self.engine:
            try:
                # Stop the engine if it has a stop method
                if hasattr(self.engine, "stop"):
                    await self.engine.stop()
                # Clean up engine resources
                self.engine.protocol_definition = None
                if (
                    hasattr(self.engine, "behavior_executor")
                    and self.engine.behavior_executor
                ):
                    await self.engine.behavior_executor.stop_all_behaviors()
                if (
                    hasattr(self.engine, "transport_layer")
                    and self.engine.transport_layer
                ):
                    await self.engine.transport_layer.stop()
            except Exception as e:
                logging.error(f"Error during cleanup: {e}")

    async def switch_protocol(
        self, new_protocol_path: Union[str, Path, Dict[str, Any]]
    ) -> None:
        """
        Switch to a different protocol.

        Args:
            new_protocol_path: New protocol file path, JSON string, or dict
        """
        was_running = self.running

        # Stop current protocol if running
        if was_running:
            await self.stop_async()

        # Load new protocol
        await self.load_protocol(new_protocol_path)

        # Start new protocol if the old one was running
        if was_running:
            await self.start_async_new()
