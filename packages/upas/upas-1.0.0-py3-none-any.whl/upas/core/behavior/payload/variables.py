"""
UPAS Payload Variables System

Handles variable resolution and substitution in payloads.
"""

import re
import logging
from typing import Dict, Any


class VariableResolver:
    """Handles variable resolution for payload construction."""

    def __init__(self, variables: Dict[str, Any] = None):
        """
        Initialize variable resolver.

        :param variables: Initial variables dictionary
        :type variables: dict
        """
        self.variables = variables or {}
        self.logger = logging.getLogger(__name__)

    def set_variable(self, name: str, value: Any) -> None:
        """
        Set a variable value.

        :param name: Variable name
        :type name: str
        :param value: Variable value
        :type value: Any
        """
        self.variables[name] = value

    def get_variable(self, name: str, default: Any = None) -> Any:
        """
        Get a variable value.

        :param name: Variable name
        :type name: str
        :param default: Default value if not found
        :type default: Any
        :return: Variable value
        :rtype: Any
        """
        return self.variables.get(name, default)

    def resolve_destination_variables(self, destination: str) -> str:
        """
        Resolve variables in destination address.

        :param destination: Destination with potential variables
        :type destination: str
        :return: Resolved destination
        :rtype: str
        """
        result = destination

        # Replace variables in format [VARIABLE_NAME] or [VARIABLE_NAME:type]
        pattern = r"\[([A-Z_][A-Z0-9_]*)(?::([a-z]+))?\]"

        def replace_var(match):
            var_name = match.group(1)
            var_type = match.group(2)  # Optional type (e.g., 'int')

            value = self.variables.get(var_name, match.group(0))

            # If variable not found, return original match
            if value == match.group(0):
                return value

            # Apply type conversion if specified
            if var_type == "int":
                try:
                    # Handle hex values (e.g., 'E9B2' -> 59826)
                    if isinstance(value, str) and all(
                        c in "0123456789ABCDEFabcdef" for c in value
                    ):
                        value = int(value, 16)
                    else:
                        value = int(value)
                except (ValueError, TypeError):
                    # If conversion fails, return original value as string
                    pass

            return str(value)

        result = re.sub(pattern, replace_var, result)
        return result
