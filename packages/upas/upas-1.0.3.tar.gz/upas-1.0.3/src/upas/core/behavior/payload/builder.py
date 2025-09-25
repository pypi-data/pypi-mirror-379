"""
Payload builder for UPAS with enhanced pattern support and variable substitution
"""

import re
import logging
from typing import List

from .patterns import EnhancedPatternProcessor
from .variables import VariableResolver
from .counters import CounterManager


class PayloadBuilder:
    """Builds payloads with variable substitution, wildcards, and function application."""

    def __init__(
        self,
        variable_resolver: VariableResolver = None,
        counter_manager: CounterManager = None,
        function_registry=None,
    ):
        """
        Initialize payload builder with enhanced pattern support.

        :param variable_resolver: Variable resolver instance
        :type variable_resolver: VariableResolver
        :param counter_manager: Counter manager instance
        :type counter_manager: CounterManager
        :param function_registry: Function registry for custom functions
        :type function_registry: object
        """
        self.variable_resolver = variable_resolver or VariableResolver()
        self.counter_manager = counter_manager or CounterManager()
        self.function_registry = function_registry
        self.pattern_processor = EnhancedPatternProcessor()
        self.logger = logging.getLogger(__name__)

    def build_payload(self, payload_template: List[str]) -> str:
        """
        Build payload from template with variable substitution and wildcard support.

        :param payload_template: Payload template as list of strings
        :type payload_template: List[str]
        :return: Built payload as hex string
        :rtype: str
        """
        if not payload_template:
            return ""

        # Join all payload parts
        full_payload = "".join(payload_template)

        # Process wildcards first
        processed_payload = self._process_wildcards(full_payload)

        # Variable substitution
        result = processed_payload

        # Pattern for variable references: [NAME] or [NAME:size] or [NAME:size:function]
        pattern = r"\[([A-Z_][A-Z0-9_]*):?(\d+)?:?([a-z_]*)\]"

        def replace_variable(match):
            var_name = match.group(1)
            size = match.group(2)
            function = match.group(3)

            # Get variable value
            if var_name in self.variable_resolver.variables:
                value = str(self.variable_resolver.variables[var_name])
            elif var_name.startswith("COUNTER"):
                # Handle counters
                counter_value = self.counter_manager.get_counter(var_name, function)

                # Format counter value based on size
                if size:
                    counter_size = int(size)
                    if counter_size == 1:
                        value = f"{counter_value:02x}"
                    elif counter_size == 2:
                        value = f"{counter_value:04x}"
                    elif counter_size == 4:
                        value = f"{counter_value:08x}"
                    elif counter_size == 8:
                        value = f"{counter_value:016x}"
                    else:
                        value = f"{counter_value:0{counter_size*2}x}"
                else:
                    value = f"{counter_value:08x}"
            else:
                self.logger.warning(f"Unknown variable: {var_name}")
                return match.group(0)  # Keep original if unknown

            # Apply function if specified and function registry available
            if function and self.function_registry:
                try:
                    func = getattr(self.function_registry, function, None)
                    if func:
                        # Handle hex string values
                        if isinstance(value, str) and all(
                            c in "0123456789abcdefABCDEF" for c in value
                        ):
                            # Hex string, convert to int
                            int_value = int(value, 16)
                            result_value = func(int_value)
                            if size:
                                value = f"{result_value:0{int(size)*2}x}"
                            else:
                                value = f"{result_value:08x}"
                        else:
                            result_value = func(value)
                            value = str(result_value)
                except Exception as e:
                    self.logger.error(
                        f"Error applying function {function} to {var_name}: {e}"
                    )

            return value

        # Apply variable substitution
        result = re.sub(pattern, replace_variable, result)
        return result

    def _process_wildcards(self, payload: str) -> str:
        """
        Process wildcard patterns in payload template.

        Args:
            payload: Raw payload string with possible wildcards

        Returns:
            Processed payload with wildcards handled
        """
        # For template building, we generate actual bytes for wildcards
        # [WILDCARD:n] or [SKIP:n] -> generate n bytes of zeros or pattern

        def replace_wildcard(match):
            size = int(match.group(1))
            # Generate pattern bytes (could be configurable)
            return "00" * size  # Generate zeros for now

        # Replace wildcard patterns
        result = self.pattern_processor.wildcard_regex.sub(replace_wildcard, payload)

        return result

    def supports_wildcards(self, pattern: str) -> bool:
        """
        Check if pattern contains wildcard markers.

        Args:
            pattern: Pattern to check

        Returns:
            True if pattern contains wildcards
        """
        return bool(self.pattern_processor.wildcard_regex.search(pattern))

    def hex_to_bytes(self, hex_string: str) -> bytes:
        """
        Convert hex string to bytes, handling various formats.

        :param hex_string: Hex string to convert
        :type hex_string: str
        :return: Bytes representation
        :rtype: bytes
        """
        if not hex_string:
            return b""

        # Check if this looks like a hex string
        clean_hex = hex_string.replace(" ", "").replace("0x", "")

        if all(c in "0123456789abcdefABCDEF" for c in clean_hex):
            # It's a hex string
            if len(clean_hex) % 2 != 0:
                clean_hex = "0" + clean_hex  # Pad with leading zero

            try:
                return bytes.fromhex(clean_hex)
            except ValueError as e:
                self.logger.error(f"Invalid hex string: {hex_string}, error: {e}")
                # Fallback to ASCII bytes
                return hex_string.encode("ascii", errors="ignore")
        else:
            # Not hex, treat as ASCII
            self.logger.warning(
                f"Payload doesn't appear to be hex, treating as ASCII: {hex_string}"
            )
            return hex_string.encode("ascii", errors="ignore")
