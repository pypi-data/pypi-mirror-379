"""
UPAS Packet Builder

Dynamic packet construction with variable substitution and functions.
"""

import struct
import time
import random
import logging
from typing import Dict, Any, List, Union, Optional


class VariableResolver:
    """
    Resolves variables and functions in packet definitions.

    Handles variable substitution, function calls, and value formatting.
    """

    def __init__(self):
        """Initialize variable resolver."""
        self.variables = {}
        self.functions = {}
        self.counters = {}
        self.logger = logging.getLogger(__name__)

        # Register built-in functions
        self._register_builtin_functions()

    def _register_builtin_functions(self) -> None:
        """Register built-in utility functions."""
        self.functions.update(
            {
                "increment": lambda x: (x + 1) % 0xFFFFFFFF,
                "timestamp": lambda: int(time.time()),
                "random_port": lambda: random.randint(1024, 65535),
                "current_time": lambda: int(time.time()),
                "inc": lambda x: (x + 1) % 0xFFFFFFFF,
                "set": lambda x: x,
            }
        )

    def register_variables(self, variables: Dict[str, Any]) -> None:
        """
        Register variables for substitution.

        :param variables: Variable definitions
        :type variables: dict
        """
        self.variables.update(variables)
        self.logger.debug(f"Registered {len(variables)} variables")

    def register_functions(self, functions: Dict[str, Any]) -> None:
        """
        Register custom functions.

        :param functions: Function definitions
        :type functions: dict
        """
        for name, func_def in functions.items():
            if isinstance(func_def, str):
                # Simple lambda function
                try:
                    self.functions[name] = eval(func_def)
                except Exception as e:
                    self.logger.error(f"Failed to compile function {name}: {e}")
            elif callable(func_def):
                self.functions[name] = func_def

        self.logger.debug(f"Registered {len(functions)} functions")

    def resolve_value(self, value: str) -> bytes:
        """
        Resolve a value string to bytes.

        Handles various formats:
        - [VAR_NAME:size] - Variable reference
        - [VAR_NAME:size:function] - Variable with function
        - Raw hex string - Direct hex conversion
        - Mixed strings with variables and hex

        :param value: Value string to resolve
        :type value: str
        :return: Resolved bytes
        :rtype: bytes
        """
        value = value.strip()

        # Handle simple variable references [VAR:size:func]
        if value.startswith("[") and value.endswith("]") and value.count("[") == 1:
            return self._resolve_variable_reference(value[1:-1])

        # Handle mixed strings with variables and hex data
        if "[" in value and "]" in value:
            return self._resolve_mixed_string(value)

        # Handle raw hex strings
        if all(c in "0123456789abcdefABCDEF " for c in value):
            # Remove spaces and convert to bytes
            hex_string = value.replace(" ", "")
            if len(hex_string) % 2 == 1:
                hex_string = "0" + hex_string
            return bytes.fromhex(hex_string)

        # Handle string literals
        return value.encode("utf-8")

    def _resolve_mixed_string(self, value: str) -> bytes:
        """
        Resolve a mixed string containing both hex data and variable references.

        :param value: Mixed string to resolve
        :type value: str
        :return: Resolved bytes
        :rtype: bytes
        """
        result = b""
        current_pos = 0

        while current_pos < len(value):
            # Find next variable reference
            start_bracket = value.find("[", current_pos)
            if start_bracket == -1:
                # No more variables, process remaining as hex
                remaining = value[current_pos:].strip()
                if remaining:
                    hex_string = remaining.replace(" ", "")
                    if hex_string and len(hex_string) % 2 == 1:
                        hex_string = "0" + hex_string
                    if hex_string:
                        result += bytes.fromhex(hex_string)
                break

            # Process hex data before the variable
            if start_bracket > current_pos:
                hex_part = value[current_pos:start_bracket].strip()
                if hex_part:
                    hex_string = hex_part.replace(" ", "")
                    if hex_string and len(hex_string) % 2 == 1:
                        hex_string = "0" + hex_string
                    if hex_string:
                        result += bytes.fromhex(hex_string)

            # Find the end of the variable reference
            end_bracket = value.find("]", start_bracket)
            if end_bracket == -1:
                break

            # Process the variable reference
            var_ref = value[start_bracket + 1 : end_bracket]
            result += self._resolve_variable_reference(var_ref)

            current_pos = end_bracket + 1

        return result

    def _resolve_variable_reference(self, ref: str) -> bytes:
        """
        Resolve a variable reference.

        :param ref: Variable reference string
        :type ref: str
        :return: Resolved bytes
        :rtype: bytes
        """
        parts = ref.split(":")
        var_name = parts[0]
        size = int(parts[1]) if len(parts) > 1 else 4
        func_name = parts[2] if len(parts) > 2 else None

        # Get variable value
        if var_name in self.variables:
            value = self.variables[var_name]
        elif var_name in self.counters:
            value = self.counters[var_name]
        else:
            # Initialize counter variables
            self.counters[var_name] = 0
            value = 0

        # Apply function if specified
        if func_name:
            if func_name == "increment" or func_name == "++":
                self.counters[var_name] = self.functions["increment"](value)
                value = self.counters[var_name]
            elif func_name.startswith("set(") and func_name.endswith(")"):
                # Handle set(value) function
                try:
                    set_value_str = func_name[4:-1]  # Extract value between parentheses
                    set_value = int(set_value_str)
                    self.counters[var_name] = set_value
                    value = set_value
                except ValueError as e:
                    self.logger.warning(f"Invalid set function parameter: {func_name}")
                    value = 0
            elif func_name in self.functions:
                value = self.functions[func_name](value)
            else:
                self.logger.warning(f"Unknown function: {func_name}")

        # Convert to bytes based on size
        return self._value_to_bytes(value, size)

    def _value_to_bytes(self, value: Union[int, str, bytes], size: int) -> bytes:
        """
        Convert value to bytes with specified size.

        :param value: Value to convert
        :type value: int, str, or bytes
        :param size: Target size in bytes
        :type size: int
        :return: Converted bytes
        :rtype: bytes
        """
        if isinstance(value, bytes):
            return value[:size] if len(value) > size else value.ljust(size, b"\x00")

        if isinstance(value, str):
            if value.startswith("0x"):
                value = int(value, 16)
            elif all(c in "0123456789abcdefABCDEF" for c in value):
                # Hex string
                hex_bytes = bytes.fromhex(value)
                return (
                    hex_bytes[:size]
                    if len(hex_bytes) > size
                    else hex_bytes.ljust(size, b"\x00")
                )
            else:
                # String literal
                str_bytes = value.encode("utf-8")
                return (
                    str_bytes[:size]
                    if len(str_bytes) > size
                    else str_bytes.ljust(size, b"\x00")
                )

        if isinstance(value, int):
            # Pack as big-endian integer
            if size == 1:
                return struct.pack(">B", value & 0xFF)
            elif size == 2:
                return struct.pack(">H", value & 0xFFFF)
            elif size == 4:
                return struct.pack(">I", value & 0xFFFFFFFF)
            elif size == 8:
                return struct.pack(">Q", value & 0xFFFFFFFFFFFFFFFF)
            else:
                # Variable size - use as many bytes as needed
                byte_value = value.to_bytes((value.bit_length() + 7) // 8, "big")
                return (
                    byte_value[:size]
                    if len(byte_value) > size
                    else byte_value.ljust(size, b"\x00")
                )

        return b"\x00" * size


class PacketBuilder:
    """
    Main packet builder class.

    Constructs packets from JSON definitions with variable substitution.
    """

    def __init__(self):
        """Initialize packet builder."""
        self.logger = logging.getLogger(__name__)
        self.resolver = VariableResolver()

    def register_variables(self, variables: Dict[str, Any]) -> None:
        """
        Register variables for packet construction.

        :param variables: Variable definitions
        :type variables: dict
        """
        self.resolver.register_variables(variables)

    def register_functions(self, functions: Dict[str, Any]) -> None:
        """
        Register functions for packet construction.

        :param functions: Function definitions
        :type functions: dict
        """
        self.resolver.register_functions(functions)

    def set_variable_value(self, name: str, value: Any) -> None:
        """
        Set a variable value or counter.

        :param name: Variable name
        :type name: str
        :param value: Variable value
        :type value: Any
        """
        if isinstance(value, int):
            self.resolver.counters[name] = value
        else:
            self.resolver.variables[name] = value

    def build_packet(
        self, payload_definition: List[Union[str, Dict[str, Any]]]
    ) -> bytes:
        """
        Build a packet from payload definition.

        :param payload_definition: List of payload elements
        :type payload_definition: list
        :return: Constructed packet
        :rtype: bytes
        """
        packet_data = b""

        for element in payload_definition:
            if isinstance(element, str):
                # Simple string element
                packet_data += self.resolver.resolve_value(element)
            elif isinstance(element, dict):
                # Dictionary element with key-value pairs
                for key, value in element.items():
                    if key in ["prefix", "suffix", "data"]:
                        packet_data += self.resolver.resolve_value(str(value))
                    elif key == "counter":
                        packet_data += self.resolver.resolve_value(str(value))
                    else:
                        # Custom field
                        packet_data += self.resolver.resolve_value(str(value))

        return packet_data

    def build_from_hex_pattern(
        self, hex_pattern: str, variables: Optional[Dict[str, Any]] = None
    ) -> bytes:
        """
        Build packet from hex pattern with variable substitution.

        :param hex_pattern: Hex pattern string
        :type hex_pattern: str
        :param variables: Optional variables for substitution
        :type variables: dict, optional
        :return: Constructed packet
        :rtype: bytes
        """
        if variables:
            self.register_variables(variables)

        # Simple hex pattern parsing
        return self.resolver.resolve_value(hex_pattern)

    def get_variable_value(self, name: str) -> Any:
        """
        Get current value of a variable.

        :param name: Variable name
        :type name: str
        :return: Variable value
        :rtype: Any
        """
        if name in self.resolver.variables:
            return self.resolver.variables[name]
        elif name in self.resolver.counters:
            return self.resolver.counters[name]
        return None

    def set_variable_value(self, name: str, value: Any) -> None:
        """
        Set variable value.

        :param name: Variable name
        :type name: str
        :param value: New value
        :type value: Any
        """
        if name in self.resolver.counters:
            self.resolver.counters[name] = value
        else:
            self.resolver.variables[name] = value

    def reset_counters(self) -> None:
        """Reset all counter variables to zero."""
        for name in self.resolver.counters:
            self.resolver.counters[name] = 0

        self.logger.debug("Reset all counters")


# Example usage functions for testing
def create_industrial_hello_packet(sequence: int = 1) -> bytes:
    """
    Create an industrial hello packet.

    :param sequence: Sequence number
    :type sequence: int
    :return: Packet bytes
    :rtype: bytes
    """
    builder = PacketBuilder()

    # Register industrial variables
    builder.register_variables(
        {"PREFIX": "a0b1c2d3e4f5", "DEVICE_ID": "ab12cd", "SUFFIX": "ef34ab56"}
    )

    # Set sequence counter
    builder.set_variable_value("SEQ", sequence)

    # Build packet
    payload_def = [
        "[PREFIX:6]",
        "00 20 00 00 00 30 00 00 00 00 00 00 00 00 01 08",
        "00 00 00 [DEVICE_ID:3] 00 00 00 01 00 00 00 01 00 00",
        "00 [SEQ:4] 00 00 00 00",
        "[SUFFIX:4]",
    ]

    return builder.build_packet(payload_def)


def create_udp_discovery_packet(request_id: int = 2) -> bytes:
    """
    Create a UDP discovery packet.

    :param request_id: Request ID
    :type request_id: int
    :return: Packet bytes
    :rtype: bytes
    """
    builder = PacketBuilder()

    builder.register_variables(
        {"PREFIX": "a0b1c2d3e4f5", "DEVICE_ID": "ab12cd", "SUFFIX": "ef34ab56"}
    )

    builder.set_variable_value("REQ_ID", request_id)

    payload_def = [
        "[PREFIX:6]",
        "00 20 00 00 00 28 01 08 00 00 00 [DEVICE_ID:3] 08 04",
        "00 00 00 [DEVICE_ID:3] 00 00 00 [REQ_ID:4] 00 00 00 01",
        "[SUFFIX:4]",
    ]

    return builder.build_packet(payload_def)
