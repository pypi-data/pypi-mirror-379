"""
Periodic behavior implementation for UPAS
"""

import asyncio
import logging

from ..base import BehaviorConfig
from ..payload.builder import PayloadBuilder
from ..scheduling.timing import TimingManager
from ..responses import MultiPacketResponseManager, ResponseMode


class PeriodicBehavior:
    """Handles periodic behavior execution."""

    def __init__(
        self,
        behavior_name: str,
        behavior_config: BehaviorConfig,
        payload_builder: PayloadBuilder,
        execution_context,
    ):
        """
        Initialize periodic behavior.

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
        """Execute periodic behavior loop."""
        config = self.behavior_config.config
        interval_ms = config.get("interval", 1000)
        interval = self.timing_manager.convert_ms_to_seconds(interval_ms)
        repeat_count = config.get("repeat_count", -1)
        jitter_ms = config.get("jitter", 0)

        self.logger.info(
            f"Starting periodic behavior {self.behavior_name} with interval {interval}s"
        )

        count = 0
        while True:
            # Check repeat count
            if repeat_count > 0 and count >= repeat_count:
                self.logger.info(
                    f"Periodic behavior {self.behavior_name} completed {count} iterations"
                )
                break

            try:
                # Check if behavior should still run based on current state
                if not self.execution_context.should_behavior_run(
                    self.behavior_config.active_states
                ):
                    self.logger.debug(
                        f"Behavior {self.behavior_name} paused due to state change"
                    )
                    await asyncio.sleep(1)  # Check again in 1 second
                    continue

                # Execute behavior action
                success = await self._execute_action()

                # Handle state transition based on execution result
                await self._handle_transition(success)

                count += 1

            except asyncio.CancelledError:
                self.logger.info(f"Periodic behavior {self.behavior_name} cancelled")
                break
            except Exception as e:
                self.logger.error(
                    f"Error in periodic behavior {self.behavior_name}: {e}"
                )
                await asyncio.sleep(1)  # Wait before retry

            # Wait for next iteration
            try:
                await self.timing_manager.sleep_with_jitter(interval, jitter_ms)
            except asyncio.CancelledError:
                break

    async def _execute_action(self) -> bool:
        """
        Execute the periodic behavior action.

        :return: True if successful
        :rtype: bool
        """
        config = self.behavior_config.config

        try:
            # Get payload from config
            payload = config.get("payload", [])

            # Build payload with variable substitution
            payload_hex = self.payload_builder.build_payload(payload)

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

            self.logger.warning(f"📡 {self.behavior_name}: periodic → {destination}")

            # Use ResponseManager only for TCP services to get persistent connections
            if service_name and service_name.startswith("tcp"):
                # TCP services - use ResponseManager for persistent connections
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
                        f"Failed to send periodic packet via {transport_name}"
                    )

                return success
            else:
                # UDP services - use original method
                payload_bytes = self.payload_builder.hex_to_bytes(payload_hex)

                # Send packet via transport
                if service_name:
                    # Use specific service
                    await self.execution_context.transport_layer.send_packet_with_service(
                        transport_name, service_name, destination, payload_bytes
                    )
                else:
                    # Use transport directly
                    await self.execution_context.transport_layer.send_packet(
                        transport_name, destination, payload_bytes
                    )

                self.logger.info(
                    f"Successfully sent {len(payload_bytes)} bytes via transport {transport_name}"
                )
                return True

        except Exception as e:
            self.logger.error(
                f"Error executing periodic behavior {self.behavior_name}: {e}"
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
            if success and "success" in transition:
                new_state = transition["success"]
                self.execution_context.state_machine.transition_to(new_state)
                self.logger.info(
                    f"Periodic behavior {self.behavior_name} triggered transition to {new_state}"
                )
            elif not success and "error" in transition:
                new_state = transition["error"]
                self.execution_context.state_machine.transition_to(new_state)
                self.logger.info(
                    f"Periodic behavior {self.behavior_name} error triggered transition to {new_state}"
                )
