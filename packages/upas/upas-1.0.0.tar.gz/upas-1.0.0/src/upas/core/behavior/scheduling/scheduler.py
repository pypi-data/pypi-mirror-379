"""
Behavior scheduling system for UPAS with advanced timing control
"""

import asyncio
import logging
from typing import Dict

from ..base import BehaviorConfig, BehaviorState
from ..state import ExecutionContext
from .timing import TimingManager


class BehaviorScheduler:
    """Schedules and manages behavior execution lifecycle."""

    def __init__(self, execution_context: ExecutionContext):
        """
        Initialize behavior scheduler.

        :param execution_context: Execution context for behaviors
        :type execution_context: ExecutionContext
        """
        self.execution_context = execution_context
        self.timing_manager = TimingManager()
        self.behavior_tasks: Dict[str, asyncio.Task] = {}
        self.behavior_states: Dict[str, BehaviorState] = {}
        self.running = False
        self.logger = logging.getLogger(__name__)

    async def start_behavior(
        self, behavior_name: str, behavior_config: BehaviorConfig, behavior_executor
    ) -> bool:
        """
        Start a specific behavior.

        :param behavior_name: Name of the behavior
        :type behavior_name: str
        :param behavior_config: Behavior configuration
        :type behavior_config: BehaviorConfig
        :param behavior_executor: Behavior executor function
        :type behavior_executor: callable
        :return: True if started successfully
        :rtype: bool
        """
        if not self.execution_context.should_behavior_run(
            behavior_config.active_states
        ):
            self.logger.debug(f"Behavior {behavior_name} not active in current state")
            return False

        if (
            behavior_name in self.behavior_tasks
            and not self.behavior_tasks[behavior_name].done()
        ):
            self.logger.warning(f"Behavior {behavior_name} already running")
            return False

        try:
            # Create and start behavior task
            task = asyncio.create_task(behavior_executor())
            self.behavior_tasks[behavior_name] = task
            self.behavior_states[behavior_name] = BehaviorState.RUNNING

            self.logger.info(f"Started behavior: {behavior_name}")
            return True

        except Exception as e:
            self.logger.error(f"Failed to start behavior {behavior_name}: {e}")
            self.behavior_states[behavior_name] = BehaviorState.ERROR
            return False

    async def stop_behavior(self, behavior_name: str) -> None:
        """
        Stop a specific behavior.

        :param behavior_name: Name of the behavior to stop
        :type behavior_name: str
        """
        if behavior_name in self.behavior_tasks:
            task = self.behavior_tasks[behavior_name]
            if not task.done():
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass

            del self.behavior_tasks[behavior_name]
            self.behavior_states[behavior_name] = BehaviorState.IDLE
            self.logger.info(f"Stopped behavior: {behavior_name}")

    async def stop_all_behaviors(self) -> None:
        """Stop all running behaviors."""
        self.running = False

        # Stop all behavior tasks
        for behavior_name in list(self.behavior_tasks.keys()):
            await self.stop_behavior(behavior_name)

        self.logger.info("All behaviors stopped")

    def on_state_change(
        self, new_state: str, behaviors: Dict[str, BehaviorConfig]
    ) -> None:
        """
        Handle state machine state changes.

        :param new_state: New state
        :type new_state: str
        :param behaviors: All behavior configurations
        :type behaviors: dict
        """
        self.logger.info(f"State changed to: {new_state}")

        # Check all behaviors and start/stop them based on active_states
        for behavior_name, behavior_config in behaviors.items():
            should_run = self.execution_context.should_behavior_run(
                behavior_config.active_states
            )
            is_running = (
                behavior_name in self.behavior_tasks
                and not self.behavior_tasks[behavior_name].done()
            )

            if should_run and not is_running:
                # Behavior should start (will be handled by main executor)
                self.logger.info(
                    f"Behavior {behavior_name} should start due to state change"
                )
            elif not should_run and is_running:
                # Stop behavior
                task = self.behavior_tasks.get(behavior_name)
                if task and not task.done():
                    task.cancel()
                    self.behavior_states[behavior_name] = BehaviorState.PAUSED
                    self.logger.info(
                        f"Paused behavior {behavior_name} due to state change"
                    )

    def get_behavior_state(self, behavior_name: str) -> BehaviorState:
        """
        Get state of a specific behavior.

        :param behavior_name: Name of the behavior
        :type behavior_name: str
        :return: Behavior state
        :rtype: BehaviorState
        """
        return self.behavior_states.get(behavior_name, BehaviorState.IDLE)
