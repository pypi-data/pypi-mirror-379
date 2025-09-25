"""
UPAS Protocol Engine

Main execution engine for UPAS protocols with function registry and state machine support.
"""

import json
import logging
import time
import random
from typing import Dict, Any, List, Optional, Callable, Union

from .behavior import BehaviorExecutor
from .transport import TransportLayer
from .state import StateMachine


class FunctionRegistry:
    """Registry for custom functions that can be used in protocol variables."""

    def __init__(self):
        self._functions: Dict[str, Callable] = {}
        self._builtin_functions: Dict[str, Callable] = {}
        self._setup_builtin_functions()

    def _setup_builtin_functions(self):
        """Setup built-in functions."""
        self._builtin_functions = {
            # Arithmetic functions
            "increment": lambda x=0: (x + 1) % 0xFFFFFFFF,
            "decrement": lambda x=0: (x - 1) % 0xFFFFFFFF,
            "multiply": lambda x=0, factor=2: (x * factor) % 0xFFFFFFFF,
            # Time functions
            "current_time": lambda: int(time.time()),
            "timestamp": lambda: int(time.time()),
            "timestamp_ms": lambda: int(time.time() * 1000),
            # Random functions
            "random_byte": lambda: random.randint(0, 255),
            "random_port": lambda: random.randint(1024, 65535),
            "random_id": lambda: random.randint(0x1000, 0xFFFF),
            # Data manipulation functions
            "checksum_simple": lambda data: sum(
                data if isinstance(data, (list, bytes)) else []
            )
            & 0xFF,
            "crc16": lambda data: self._calculate_crc16(data),
            "reverse_bytes": lambda data: (
                data[::-1] if hasattr(data, "__getitem__") else data
            ),
            # Network functions (newly documented)
            "htons": lambda x: ((x & 0xFF) << 8)
            | ((x >> 8) & 0xFF),  # Host to network short
            "ntohs": lambda x: ((x & 0xFF) << 8)
            | ((x >> 8) & 0xFF),  # Network to host short
            "inet_checksum": lambda data: self._calculate_inet_checksum(data),
            # String/encoding functions
            "hex_encode": lambda data: (
                data.hex() if isinstance(data, bytes) else str(data)
            ),
            "ascii_encode": lambda s: s.encode("ascii") if isinstance(s, str) else s,
        }

    def _calculate_crc16(self, data):
        """Simple CRC16 implementation."""
        if isinstance(data, str):
            data = data.encode("utf-8")
        elif isinstance(data, list):
            data = bytes(data)

        crc = 0xFFFF
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if crc & 1:
                    crc = (crc >> 1) ^ 0xA001
                else:
                    crc >>= 1
        return crc & 0xFFFF

    def _calculate_inet_checksum(self, data):
        """Calculate Internet checksum (RFC 1071)."""
        if isinstance(data, str):
            data = data.encode("utf-8")
        elif isinstance(data, list):
            data = bytes(data)

        # Pad data to even length
        if len(data) % 2:
            data += b"\x00"

        checksum = 0
        for i in range(0, len(data), 2):
            word = (data[i] << 8) + data[i + 1]
            checksum += word
            checksum = (checksum & 0xFFFF) + (checksum >> 16)

        return (~checksum) & 0xFFFF

    def register_function(self, name: str, func: Callable):
        """Register a custom function."""
        if not callable(func):
            raise ValueError(f"Function {name} must be callable")
        self._functions[name] = func

    def register_functions_from_protocol(
        self, functions: Dict[str, Union[str, Callable]]
    ):
        """Register multiple functions from protocol definition."""
        for name, func_def in functions.items():
            if isinstance(func_def, str):
                try:
                    # Safe evaluation of lambda functions
                    if func_def.startswith("lambda"):
                        # Create safe environment for lambda evaluation
                        safe_env = {
                            "__builtins__": {},
                            "sum": sum,
                            "int": int,
                            "time": time,
                            "random": random,
                            "len": len,
                            "max": max,
                            "min": min,
                            "abs": abs,
                            "bytes": bytes,
                            "list": list,
                            "str": str,
                        }
                        func = eval(func_def, safe_env, {})
                        self.register_function(name, func)
                    else:
                        raise ValueError(f"Function {name} must be a lambda expression")
                except Exception as e:
                    logging.error(f"Error evaluating function {name}: {e}")
                    raise ValueError(f"Error evaluating function {name}: {e}")
            elif callable(func_def):
                self.register_function(name, func_def)
            else:
                raise ValueError(f"Function {name} must be a string lambda or callable")

    def get_function(self, name: str) -> Optional[Callable]:
        """Get a function by name (custom functions take precedence)."""
        return self._functions.get(name) or self._builtin_functions.get(name)

    def has_function(self, name: str) -> bool:
        """Check if a function exists."""
        return name in self._functions or name in self._builtin_functions

    def list_functions(self) -> List[str]:
        """List all available functions."""
        return list(self._builtin_functions.keys()) + list(self._functions.keys())


class ProtocolEngine:
    """Main protocol execution engine with function registry and state machine support."""

    def __init__(self):
        self.transport_layer = TransportLayer()
        self.behavior_executor = BehaviorExecutor()
        self.function_registry = FunctionRegistry()
        self.state_machine: Optional[StateMachine] = None
        self.protocol_definition: Optional[Dict[str, Any]] = None
        self.logger = logging.getLogger(__name__)
        self.running = False

    async def load_protocol(self, protocol_path: str):
        """Load protocol definition from JSON file."""
        try:
            with open(protocol_path, "r", encoding="utf-8") as f:
                self.protocol_definition = json.load(f)

            # Register custom functions if present
            if "functions" in self.protocol_definition:
                self.function_registry.register_functions_from_protocol(
                    self.protocol_definition["functions"]
                )
                self.logger.info(
                    f"Registered {len(self.protocol_definition['functions'])} custom functions"
                )

            # Initialize state machine if present
            if "state_machine" in self.protocol_definition:
                self._setup_state_machine(self.protocol_definition["state_machine"])
                self.logger.info("State machine initialized")

            # Setup transports
            if "transports" in self.protocol_definition:
                await self.transport_layer.register_transports(
                    self.protocol_definition["transports"]
                )

            # Setup behaviors with function registry and state machine
            if "behaviors" in self.protocol_definition:
                await self.behavior_executor.setup_behaviors(
                    self.protocol_definition["behaviors"],
                    self.function_registry,
                    self.state_machine,
                    self.protocol_definition.get("variables", {}),
                    self.transport_layer,
                )

            self.logger.info(
                f"Protocol loaded successfully: {self.protocol_definition.get('protocol', {}).get('name', 'Unknown')}"
            )

        except Exception as e:
            self.logger.error(f"Error loading protocol: {e}")
            raise

    def _setup_state_machine(self, state_machine_config: Dict[str, Any]):
        """Setup state machine from configuration."""
        initial_state = state_machine_config.get("initial_state", "IDLE")
        self.state_machine = StateMachine(initial_state)

        # Add states
        if "states" in state_machine_config:
            for state_name, state_config in state_machine_config["states"].items():
                self.state_machine.add_state(
                    state_name,
                    description=state_config.get("description", ""),
                    entry_action=state_config.get("entry_action"),
                    exit_action=state_config.get("exit_action"),
                )

        # Add transitions
        if "transitions" in state_machine_config:
            for transition in state_machine_config["transitions"]:
                self.state_machine.add_transition(
                    from_state=transition["from"],
                    to_state=transition["to"],
                    trigger=transition["trigger"],
                    condition=transition.get("condition"),
                    action=transition.get("action"),
                )

    async def start(self):
        """Start the protocol engine."""
        if self.running:
            return

        self.running = True
        self.logger.info("Starting protocol engine")

        try:
            # Start transport layer
            await self.transport_layer.start()

            # Start behavior executor
            await self.behavior_executor.start()

            self.logger.info("Protocol engine started successfully")

        except Exception as e:
            self.logger.error(f"Error starting protocol engine: {e}")
            self.running = False
            raise

    async def stop(self):
        """Stop the protocol engine."""
        if not self.running:
            return

        self.running = False
        self.logger.info("Stopping protocol engine")

        try:
            # Stop behavior executor
            await self.behavior_executor.stop()

            # Stop transport layer
            await self.transport_layer.stop()

            self.logger.info("Protocol engine stopped successfully")

        except Exception as e:
            self.logger.error(f"Error stopping protocol engine: {e}")
            raise

    def transition_state(self, new_state: str, trigger: str = "manual") -> bool:
        """Transition the state machine to a new state."""
        if self.state_machine:
            success = self.state_machine.transition_to(new_state, trigger)
            if success and self.behavior_executor:
                # Notify behavior executor of state change
                self.behavior_executor.on_state_change(new_state)
            return success
        else:
            self.logger.warning("No state machine configured")
            return False

    def get_current_state(self) -> Optional[str]:
        """Get the current state."""
        return self.state_machine.get_current_state() if self.state_machine else None

    def get_statistics(self) -> Dict[str, Any]:
        """Get current engine statistics."""
        stats = {
            "running": self.running,
            "current_state": self.get_current_state(),
            "loaded_protocol": None,
            "registered_functions": len(self.function_registry.list_functions()),
            "behaviors": {},
        }

        if self.protocol_definition:
            stats["loaded_protocol"] = self.protocol_definition.get("protocol", {}).get(
                "name", "Unknown"
            )

        if self.behavior_executor:
            stats["behaviors"] = {
                "running": self.behavior_executor.get_running_behaviors(),
                "total": len(self.behavior_executor.behaviors),
            }

        return stats

    def is_running(self) -> bool:
        """Check if the engine is currently running."""
        return self.running
