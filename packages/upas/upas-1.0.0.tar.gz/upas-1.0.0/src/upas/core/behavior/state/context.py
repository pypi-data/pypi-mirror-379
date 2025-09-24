"""
UPAS State Context Manager

Manages execution context and state for behaviors.
"""

import logging
from typing import Dict, Any, Optional


class ExecutionContext:
    """Manages execution context for behaviors."""

    def __init__(self):
        """Initialize execution context."""
        self.state_machine = None
        self.transport_layer = None
        self.function_registry = None
        self.behavior_executor = (
            None  # Reference to behavior executor for state change notifications
        )
        self.variables: Dict[str, Any] = {}
        self.logger = logging.getLogger(__name__)

    def set_state_machine(self, state_machine) -> None:
        """
        Set state machine reference.

        :param state_machine: State machine instance
        :type state_machine: object
        """
        self.state_machine = state_machine

    def set_transport_layer(self, transport_layer) -> None:
        """
        Set transport layer reference.

        :param transport_layer: Transport layer instance
        :type transport_layer: object
        """
        self.transport_layer = transport_layer

    def set_function_registry(self, function_registry) -> None:
        """
        Set function registry reference.

        :param function_registry: Function registry instance
        :type function_registry: object
        """
        self.function_registry = function_registry

    def set_behavior_executor(self, behavior_executor) -> None:
        """
        Set behavior executor reference.

        :param behavior_executor: Behavior executor instance
        :type behavior_executor: object
        """
        self.behavior_executor = behavior_executor

    def set_variables(self, variables: Dict[str, Any]) -> None:
        """
        Set variables dictionary.

        :param variables: Variables dictionary
        :type variables: dict
        """
        if variables:
            self.variables.update(variables)

    def get_current_state(self) -> Optional[str]:
        """
        Get current state from state machine.

        :return: Current state or None
        :rtype: str or None
        """
        if self.state_machine:
            return self.state_machine.get_current_state()
        return None

    def should_behavior_run(self, active_states: Optional[list]) -> bool:
        """
        Check if behavior should run based on current state.

        :param active_states: List of states where behavior should be active
        :type active_states: list or None
        :return: True if behavior should run
        :rtype: bool
        """
        if not active_states:
            # No state restriction, always run
            return True

        if not self.state_machine:
            # No state machine, always run
            return True

        current_state = self.get_current_state()
        return current_state in active_states
