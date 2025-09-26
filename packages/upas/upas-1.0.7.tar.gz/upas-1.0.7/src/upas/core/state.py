"""
UPAS State Management

State machine implementation for protocol orchestration.
"""

import logging
from typing import Dict, Any, List, Optional
from dataclasses import dataclass


class StateTransitionError(Exception):
    """Exception raised when a state transition fails."""

    pass


@dataclass
class StateInfo:
    """Information about a protocol state."""

    name: str
    description: str = ""
    entry_action: Optional[str] = None
    exit_action: Optional[str] = None


@dataclass
class TransitionInfo:
    """Information about a state transition."""

    from_state: str
    to_state: str
    trigger: str
    condition: Optional[str] = None
    action: Optional[str] = None


class StateMachine:
    """State machine for protocol orchestration with support for conditions and actions."""

    def __init__(self, initial_state: str = "IDLE"):
        self.current_state = initial_state
        self.states: Dict[str, StateInfo] = {}
        self.transitions: List[TransitionInfo] = []
        self.state_history: List[str] = [initial_state]
        self.logger = logging.getLogger(__name__)

        # Add default IDLE state
        self.add_state("IDLE", "Default idle state")

    def add_state(
        self,
        name: str,
        description: str = "",
        entry_action: Optional[str] = None,
        exit_action: Optional[str] = None,
    ):
        """Add a state to the state machine."""
        self.states[name] = StateInfo(
            name=name,
            description=description,
            entry_action=entry_action,
            exit_action=exit_action,
        )
        self.logger.debug(f"Added state: {name} - {description}")

    def add_transition(
        self,
        from_state: str,
        to_state: str,
        trigger: str,
        condition: Optional[str] = None,
        action: Optional[str] = None,
    ):
        """Add a transition between states."""
        transition = TransitionInfo(
            from_state=from_state,
            to_state=to_state,
            trigger=trigger,
            condition=condition,
            action=action,
        )
        self.transitions.append(transition)
        self.logger.debug(
            f"Added transition: {from_state} -> {to_state} on '{trigger}'"
        )

    def can_transition(
        self, to_state: str, trigger: str, context: Optional[Dict[str, Any]] = None
    ) -> bool:
        """Check if a transition is valid."""
        if to_state not in self.states:
            return False

        # Find matching transition
        for transition in self.transitions:
            if (
                transition.from_state == self.current_state
                or transition.from_state == "*"
            ):
                if transition.to_state == to_state and transition.trigger == trigger:
                    # Check condition if present
                    if transition.condition:
                        if context and self._evaluate_condition(
                            transition.condition, context
                        ):
                            return True
                        elif transition.condition.lower() in ["true", "always"]:
                            return True
                        else:
                            return False
                    else:
                        return True

        return False

    def transition_to(
        self,
        new_state: str,
        trigger: str = "manual",
        context: Optional[Dict[str, Any]] = None,
    ) -> bool:
        """Transition to a new state."""
        if new_state not in self.states:
            self.logger.error(f"State {new_state} does not exist")
            raise StateTransitionError(f"State {new_state} does not exist")

        # Check if transition is valid
        if not self.can_transition(new_state, trigger, context):
            self.logger.warning(
                f"No valid transition from {self.current_state} to {new_state} with trigger '{trigger}'"
            )
            return False

        # Execute exit action of current state
        current_state_info = self.states.get(self.current_state)
        if current_state_info and current_state_info.exit_action:
            self._execute_action(current_state_info.exit_action, context)

        # Find and execute transition action
        for transition in self.transitions:
            if (
                transition.from_state == self.current_state
                or transition.from_state == "*"
            ):
                if transition.to_state == new_state and transition.trigger == trigger:
                    if transition.action:
                        self._execute_action(transition.action, context)
                    break

        old_state = self.current_state
        self.current_state = new_state
        self.state_history.append(new_state)

        # Execute entry action of new state
        new_state_info = self.states.get(new_state)
        if new_state_info and new_state_info.entry_action:
            self._execute_action(new_state_info.entry_action, context)

        self.logger.warning(f"🔄 State: {old_state} → {new_state}")
        return True

    def force_transition(self, new_state: str) -> bool:
        """Force transition to new state without validation."""
        if new_state not in self.states:
            self.logger.error(f"State {new_state} does not exist")
            return False

        old_state = self.current_state
        self.current_state = new_state
        self.state_history.append(new_state)

        self.logger.warning(f"Forced state transition: {old_state} -> {new_state}")
        return True

    def simple_transition_to(self, new_state: str) -> bool:
        """
        Simple transition to new state without triggers/conditions.

        This is a simplified version for basic state changes triggered by behaviors.
        It bypasses the complex transition validation but still executes entry/exit actions.

        :param new_state: Target state name
        :return: True if transition successful, False otherwise
        """
        if new_state not in self.states:
            self.logger.error(f"State {new_state} does not exist")
            return False

        if new_state == self.current_state:
            self.logger.debug(f"Already in state {new_state}, no transition needed")
            return True

        old_state = self.current_state

        # Execute exit action of current state
        current_state_info = self.states.get(self.current_state)
        if current_state_info and current_state_info.exit_action:
            self._execute_action(current_state_info.exit_action)

        # Change state
        self.current_state = new_state
        self.state_history.append(new_state)

        # Execute entry action of new state
        new_state_info = self.states.get(new_state)
        if new_state_info and new_state_info.entry_action:
            self._execute_action(new_state_info.entry_action)

        self.logger.info(f"Simple state transition: {old_state} -> {new_state}")
        return True

    def is_state_active(self, state_name: str) -> bool:
        """Check if a specific state is currently active."""
        return self.current_state == state_name

    def is_in_states(self, states: List[str]) -> bool:
        """Check if current state is in the given list of states."""
        return self.current_state in states

    def get_current_state(self) -> str:
        """Get the current state."""
        return self.current_state

    def get_state_info(self, state_name: str) -> Optional[StateInfo]:
        """Get information about a specific state."""
        return self.states.get(state_name)

    def get_available_transitions(self) -> List[TransitionInfo]:
        """Get all available transitions from current state."""
        available = []
        for transition in self.transitions:
            if (
                transition.from_state == self.current_state
                or transition.from_state == "*"
            ):
                available.append(transition)
        return available

    def get_state_history(self) -> List[str]:
        """Get the state transition history."""
        return self.state_history.copy()

    def reset_to_initial(self, initial_state: str = None):
        """Reset state machine to initial state."""
        if initial_state:
            if initial_state not in self.states:
                raise StateTransitionError(
                    f"Initial state {initial_state} does not exist"
                )
            self.current_state = initial_state
        else:
            self.current_state = self.state_history[0] if self.state_history else "IDLE"

        self.state_history = [self.current_state]
        self.logger.info(f"State machine reset to: {self.current_state}")

    def _evaluate_condition(self, condition: str, context: Dict[str, Any]) -> bool:
        """Evaluate a condition string with given context."""
        try:
            # Simple condition evaluation
            if "==" in condition:
                left, right = condition.split("==", 1)
                left_val = context.get(left.strip())
                right_val = right.strip().strip("\"'")
                return str(left_val) == right_val
            elif "!=" in condition:
                left, right = condition.split("!=", 1)
                left_val = context.get(left.strip())
                right_val = right.strip().strip("\"'")
                return str(left_val) != right_val
            elif ">" in condition:
                left, right = condition.split(">", 1)
                left_val = context.get(left.strip(), 0)
                right_val = float(right.strip())
                return float(left_val) > right_val
            elif "<" in condition:
                left, right = condition.split("<", 1)
                left_val = context.get(left.strip(), 0)
                right_val = float(right.strip())
                return float(left_val) < right_val
            else:
                # Try to evaluate as boolean variable
                return bool(context.get(condition.strip(), False))
        except Exception as e:
            self.logger.error(f"Error evaluating condition '{condition}': {e}")
            return False

    def _execute_action(self, action: str, context: Optional[Dict[str, Any]] = None):
        """Execute an action string."""
        # Basic action execution - can be enhanced with proper action system
        self.logger.info(f"Executing action: {action}")

        # For now, just log the action
        # In a full implementation, this would execute actual functions
        # based on the action string (e.g., "send_discovery_beacon", "cleanup_session")

    def __str__(self) -> str:
        """String representation of the state machine."""
        return f"StateMachine(current={self.current_state}, states={len(self.states)}, transitions={len(self.transitions)})"

    def __repr__(self) -> str:
        """Detailed representation of the state machine."""
        return f"StateMachine(current_state='{self.current_state}', states={list(self.states.keys())}, history={self.state_history})"
