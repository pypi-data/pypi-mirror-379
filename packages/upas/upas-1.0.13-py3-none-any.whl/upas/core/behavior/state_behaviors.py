"""
State-only behaviors for UPAS - behaviors that handle state transitions without network traffic
"""

import asyncio
import logging
from enum import Enum
from typing import Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime


class StateTransitionType(Enum):
    """Types of state transitions."""

    IMMEDIATE = "immediate"  # Immediate state change
    DELAYED = "delayed"  # State change after delay
    CONDITIONAL = "conditional"  # State change based on condition


@dataclass
class StateTransition:
    """Configuration for state transition."""

    target_state: str
    transition_type: StateTransitionType = StateTransitionType.IMMEDIATE
    delay: float = 0.0
    condition: Optional[Dict[str, Any]] = None

    def __post_init__(self):
        """Validate state transition configuration."""
        if self.delay < 0:
            raise ValueError("Delay must be non-negative")

        if self.transition_type == StateTransitionType.DELAYED and self.delay == 0:
            raise ValueError("Delayed transition must have positive delay")


class StateBehavior:
    """
    Behavior that only changes state without sending responses.

    This is useful for protocol state machines where certain triggers
    should only advance the state without generating network traffic.
    """

    def __init__(
        self,
        behavior_id: str,
        state_manager,
        transition: StateTransition,
        logger: Optional[logging.Logger] = None,
    ):
        """
        Initialize state behavior.

        Args:
            behavior_id: Unique identifier for this behavior
            state_manager: State manager instance
            transition: State transition configuration
            logger: Optional logger instance
        """
        self.behavior_id = behavior_id
        self.state_manager = state_manager
        self.transition = transition
        self.logger = logger or logging.getLogger(__name__)

        # Track pending delayed transitions
        self.pending_transitions = {}

    async def execute(
        self, trigger_data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Execute state transition.

        Args:
            trigger_data: Optional trigger data for conditional transitions

        Returns:
            Execution result
        """
        try:
            if self.transition.transition_type == StateTransitionType.IMMEDIATE:
                return await self._execute_immediate_transition()

            elif self.transition.transition_type == StateTransitionType.DELAYED:
                return await self._execute_delayed_transition()

            elif self.transition.transition_type == StateTransitionType.CONDITIONAL:
                return await self._execute_conditional_transition(trigger_data)

            else:
                return {
                    "success": False,
                    "error": f"Unknown transition type: {self.transition.transition_type}",
                }

        except Exception as e:
            self.logger.error(f"Error executing state transition: {e}")
            return {"success": False, "error": str(e)}

    async def _execute_immediate_transition(self) -> Dict[str, Any]:
        """Execute immediate state transition."""
        # For state-only behaviors, we need to get the current state from the actual state machine
        # instead of expecting get_behavior_state method
        try:
            old_state = getattr(self.state_manager, "current_state", "UNKNOWN")

            # Execute state transition on the state machine
            if hasattr(self.state_manager, "trigger"):
                # If it's a proper state machine with trigger method
                self.state_manager.trigger(
                    "transition_to_" + self.transition.target_state
                )
            elif hasattr(self.state_manager, "set_state"):
                # If it has a set_state method
                self.state_manager.set_state(self.transition.target_state)
            elif hasattr(self.state_manager, "current_state"):
                # If we can set current_state directly
                self.state_manager.current_state = self.transition.target_state
            else:
                # Fallback: treat as a behavior scheduler
                if hasattr(self.state_manager, "set_behavior_state"):
                    self.state_manager.set_behavior_state(
                        self.behavior_id, self.transition.target_state
                    )
                else:
                    self.logger.warning(
                        "Cannot execute state transition - no compatible state management method found"
                    )

        except Exception as e:
            old_state = "UNKNOWN"
            self.logger.warning(f"Could not get old state: {e}")

        self.logger.info(
            f"State transition: {self.behavior_id} {old_state} -> {self.transition.target_state}"
        )

        return {
            "success": True,
            "transition_type": "immediate",
            "old_state": old_state,
            "new_state": self.transition.target_state,
            "behavior_id": self.behavior_id,
        }

    async def _execute_delayed_transition(self) -> Dict[str, Any]:
        """Execute delayed state transition."""
        transition_id = f"{self.behavior_id}_{datetime.now().timestamp()}"

        self.logger.info(
            f"Scheduling delayed transition for {self.behavior_id} in {self.transition.delay}s"
        )

        # Schedule the transition
        task = asyncio.create_task(self._delayed_transition_task(transition_id))
        self.pending_transitions[transition_id] = task

        return {
            "success": True,
            "transition_type": "delayed",
            "delay": self.transition.delay,
            "transition_id": transition_id,
            "behavior_id": self.behavior_id,
        }

    async def _delayed_transition_task(self, transition_id: str):
        """Task for executing delayed transition."""
        try:
            await asyncio.sleep(self.transition.delay)

            # Same flexible state handling as immediate transition
            try:
                old_state = getattr(self.state_manager, "current_state", "UNKNOWN")

                # Execute state transition on the state machine
                if hasattr(self.state_manager, "trigger"):
                    self.state_manager.trigger(
                        "transition_to_" + self.transition.target_state
                    )
                elif hasattr(self.state_manager, "set_state"):
                    self.state_manager.set_state(self.transition.target_state)
                elif hasattr(self.state_manager, "current_state"):
                    self.state_manager.current_state = self.transition.target_state
                else:
                    if hasattr(self.state_manager, "set_behavior_state"):
                        self.state_manager.set_behavior_state(
                            self.behavior_id, self.transition.target_state
                        )
                    else:
                        self.logger.warning(
                            "Cannot execute delayed state transition - no compatible state management method found"
                        )

            except Exception as e:
                old_state = "UNKNOWN"
                self.logger.warning(
                    f"Could not get old state for delayed transition: {e}"
                )

            self.logger.info(
                f"Delayed state transition completed: {self.behavior_id} {old_state} -> {self.transition.target_state}"
            )

            # Clean up
            if transition_id in self.pending_transitions:
                del self.pending_transitions[transition_id]

        except asyncio.CancelledError:
            self.logger.debug(f"Delayed transition {transition_id} was cancelled")
        except Exception as e:
            self.logger.error(f"Error in delayed transition {transition_id}: {e}")

    async def _execute_conditional_transition(
        self, trigger_data: Optional[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Execute conditional state transition."""
        if not self.transition.condition:
            return {
                "success": False,
                "error": "No condition specified for conditional transition",
            }

        # Check condition (basic implementation)
        condition_met = self._evaluate_condition(
            self.transition.condition, trigger_data
        )

        if condition_met:
            return await self._execute_immediate_transition()
        else:
            return {
                "success": True,
                "transition_type": "conditional",
                "condition_met": False,
                "behavior_id": self.behavior_id,
            }

    def _evaluate_condition(
        self, condition: Dict[str, Any], trigger_data: Optional[Dict[str, Any]]
    ) -> bool:
        """
        Evaluate transition condition.

        Args:
            condition: Condition configuration
            trigger_data: Trigger data to evaluate against

        Returns:
            True if condition is met
        """
        # Basic condition evaluation
        condition_type = condition.get("type", "always")

        if condition_type == "always":
            return True

        elif condition_type == "never":
            return False

        elif condition_type == "data_contains" and trigger_data:
            pattern = condition.get("pattern", "")
            data = trigger_data.get("data", "")
            return pattern in data

        elif condition_type == "state_equals":
            required_state = condition.get("state")
            # Use flexible state access
            try:
                current_state = getattr(self.state_manager, "current_state", "UNKNOWN")
            except:
                current_state = "UNKNOWN"
            return current_state == required_state

        elif condition_type == "variable_equals":
            var_name = condition.get("variable")
            expected_value = condition.get("value")
            if var_name and hasattr(self.state_manager, "get_state_variable"):
                current_value = self.state_manager.get_state_variable(var_name)
                return current_value == expected_value

        # Default: condition not met
        return False

    def cancel_pending_transitions(self):
        """Cancel all pending delayed transitions."""
        for transition_id, task in self.pending_transitions.items():
            if not task.done():
                task.cancel()
                self.logger.debug(f"Cancelled pending transition {transition_id}")

        self.pending_transitions.clear()

    def get_pending_transitions(self) -> Dict[str, Any]:
        """Get information about pending transitions."""
        return {
            "count": len(self.pending_transitions),
            "transitions": list(self.pending_transitions.keys()),
        }


class StateOnlyBehaviorManager:
    """Manager for state-only behaviors."""

    def __init__(self, state_manager, logger: Optional[logging.Logger] = None):
        """Initialize state-only behavior manager."""
        self.state_manager = state_manager
        self.logger = logger or logging.getLogger(__name__)
        self.state_behaviors = {}

    def create_state_behavior(self, config: Dict[str, Any]) -> StateBehavior:
        """
        Create state behavior from configuration.

        Args:
            config: Behavior configuration

        Returns:
            StateBehavior instance
        """
        behavior_id = config.get("id", "unnamed_state_behavior")

        # Parse transition configuration
        transition_config = config.get("transition", {})

        transition_type_str = transition_config.get("type", "immediate")
        try:
            transition_type = StateTransitionType(transition_type_str)
        except ValueError:
            self.logger.warning(
                f"Unknown transition type: {transition_type_str}, using immediate"
            )
            transition_type = StateTransitionType.IMMEDIATE

        transition = StateTransition(
            target_state=transition_config.get("target_state", "idle"),
            transition_type=transition_type,
            delay=transition_config.get("delay", 0.0),
            condition=transition_config.get("condition"),
        )

        behavior = StateBehavior(
            behavior_id=behavior_id,
            state_manager=self.state_manager,
            transition=transition,
            logger=self.logger,
        )

        self.state_behaviors[behavior_id] = behavior
        return behavior

    def get_state_behavior(self, behavior_id: str) -> Optional[StateBehavior]:
        """Get state behavior by ID."""
        return self.state_behaviors.get(behavior_id)

    def remove_state_behavior(self, behavior_id: str) -> bool:
        """Remove state behavior and cancel pending transitions."""
        if behavior_id in self.state_behaviors:
            behavior = self.state_behaviors[behavior_id]
            behavior.cancel_pending_transitions()
            del self.state_behaviors[behavior_id]
            return True
        return False

    def cancel_all_pending_transitions(self):
        """Cancel all pending transitions across all behaviors."""
        for behavior in self.state_behaviors.values():
            behavior.cancel_pending_transitions()

    def get_manager_stats(self) -> Dict[str, Any]:
        """Get manager statistics."""
        total_pending = sum(
            len(behavior.pending_transitions)
            for behavior in self.state_behaviors.values()
        )

        return {
            "total_behaviors": len(self.state_behaviors),
            "total_pending_transitions": total_pending,
            "behavior_ids": list(self.state_behaviors.keys()),
        }


# Convenience functions
def create_immediate_state_transition(target_state: str) -> StateTransition:
    """Create immediate state transition."""
    return StateTransition(
        target_state=target_state, transition_type=StateTransitionType.IMMEDIATE
    )


def create_delayed_state_transition(target_state: str, delay: float) -> StateTransition:
    """Create delayed state transition."""
    return StateTransition(
        target_state=target_state,
        transition_type=StateTransitionType.DELAYED,
        delay=delay,
    )


def create_conditional_state_transition(
    target_state: str, condition: Dict[str, Any]
) -> StateTransition:
    """Create conditional state transition."""
    return StateTransition(
        target_state=target_state,
        transition_type=StateTransitionType.CONDITIONAL,
        condition=condition,
    )
