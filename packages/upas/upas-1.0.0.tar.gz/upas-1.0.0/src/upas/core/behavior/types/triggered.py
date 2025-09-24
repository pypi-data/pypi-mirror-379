"""
UPAS Triggered (One-Shot) Behavior

One-shot behavior implementation with optional delay and state transitions.
"""

import asyncio
import logging

from ..base import BehaviorConfig
from ..payload import PayloadBuilder
from ..responses import MultiPacketResponseManager, ResponseMode
from ..scheduling.timing import TimingManager


class TriggeredBehavior:
    """Handles one-shot behavior execution."""

    def __init__(
        self,
        behavior_name: str,
        behavior_config: BehaviorConfig,
        payload_builder: PayloadBuilder,
        execution_context,
    ):
        """
        Initialize triggered (one-shot) behavior.

        :param behavior_name: Name of the behavior
        :type behavior_name: str
        :param behavior_config: Behavior configuration
        :type behavior_config: BehaviorConfig
        :param payload_builder: Payload builder instance
        :type payload_builder: PayloadBuilder
        :param execution_context: Execution context
        :type execution_context: ExecutionContext
        """
        self.behavior_name = behavior_name
        self.behavior_config = behavior_config
        self.payload_builder = payload_builder
        self.execution_context = execution_context
        self.timing_manager = TimingManager()
        self.logger = logging.getLogger(__name__)

        # Add response manager for persistent connections
        self.response_manager = MultiPacketResponseManager(
            transport=execution_context.transport_layer, logger=self.logger
        )

    async def execute(self) -> None:
        """Execute one-shot behavior."""
        config = self.behavior_config.config
        delay_ms = config.get("delay", 0)
        delay = self.timing_manager.convert_ms_to_seconds(delay_ms)

        self.logger.debug(
            f"🚀 Starting one-shot behavior {self.behavior_name} with delay {delay}s"
        )

        try:
            # Wait for delay
            if delay > 0:
                await asyncio.sleep(delay)

            # Check if behavior should still run
            if not self.execution_context.should_behavior_run(
                self.behavior_config.active_states
            ):
                self.logger.info(
                    f"One-shot behavior {self.behavior_name} skipped due to state"
                )
                return

            # Execute behavior once
            success = await self._execute_action()

            # Handle state transition based on execution result
            await self._handle_transition(success)

            self.logger.info(f"One-shot behavior {self.behavior_name} completed")

        except asyncio.CancelledError:
            self.logger.info(f"One-shot behavior {self.behavior_name} cancelled")
        except Exception as e:
            self.logger.error(f"Error in one-shot behavior {self.behavior_name}: {e}")
            # Handle error transition
            await self._handle_transition(False)

    async def _execute_action(self) -> bool:
        """
        Execute the one-shot behavior action.

        :return: True if successful
        :rtype: bool
        """
        config = self.behavior_config.config

        try:
            # Build payload with variable substitution
            payload_hex = self.payload_builder.build_payload(config.get("payload", []))

            # Get transport and destination
            transport_name = config.get("transport", "primary")
            service_name = config.get("service")
            destination = config.get("destination", "unknown")

            # Resolve variables in destination
            destination = (
                self.payload_builder.variable_resolver.resolve_destination_variables(
                    destination
                )
            )

            self.logger.warning(f"🚀 {self.behavior_name}: one_shot → {destination}")

            # Use ResponseManager for persistent connections (like reactive behaviors)
            success = await self.response_manager.send_responses(
                transport_name=transport_name,
                service_name=service_name,
                destination=destination,
                payloads=[payload_hex],  # ResponseManager expects a list
                mode=ResponseMode.SINGLE,
                ack_timeout=5.0,
                retry_count=3,
            )

            if success:
                self.logger.info(
                    f"Successfully sent {len(payload_hex)//2} bytes via transport {transport_name}"
                )
            else:
                self.logger.error(
                    f"Failed to send one-shot packet via {transport_name}"
                )

            return success

        except Exception as e:
            self.logger.error(
                f"Error executing one-shot behavior {self.behavior_name}: {e}"
            )
            return False

    async def _handle_transition(self, success: bool) -> None:
        """
        Handle state transition based on execution result.

        :param success: Whether execution was successful
        :type success: bool
        """
        config = self.behavior_config.config
        transition = config.get("transition")

        if transition and self.execution_context.state_machine:
            if isinstance(transition, str):
                # Simple transition string
                self.execution_context.state_machine.transition_to(transition)
                self.logger.info(
                    f"One-shot behavior {self.behavior_name} triggered transition to {transition}"
                )
            elif isinstance(transition, dict):
                # Complex transition based on success/error
                if success and "success" in transition:
                    new_state = transition["success"]
                    self.execution_context.state_machine.transition_to(new_state)
                    self.logger.info(
                        f"One-shot behavior {self.behavior_name} triggered transition to {new_state}"
                    )
                elif not success and "error" in transition:
                    new_state = transition["error"]
                    self.execution_context.state_machine.transition_to(new_state)
                    self.logger.info(
                        f"One-shot behavior {self.behavior_name} error triggered transition to {new_state}"
                    )
