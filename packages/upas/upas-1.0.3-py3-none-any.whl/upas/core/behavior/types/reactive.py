"""
Reactive behavior implementation for UPAS with advanced pattern matching
"""

import asyncio
import logging
import re

from ..base import BehaviorConfig
from ..payload.builder import PayloadBuilder
from ..payload.patterns import EnhancedPatternProcessor
from ..responses import MultiPacketResponseManager, ResponseMode


class ReactiveBehavior:
    """Handles reactive behavior execution with packet triggers."""

    def __init__(
        self,
        behavior_name: str,
        behavior_config: BehaviorConfig,
        payload_builder: PayloadBuilder,
        execution_context,
    ):
        """
        Initialize reactive behavior.

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
        self.logger = logging.getLogger(__name__)

        # Initialize components
        self.payload_analyzer = EnhancedPatternProcessor()

        # Initialize multi-packet response manager
        self.response_manager = MultiPacketResponseManager(
            transport=execution_context.transport_layer, logger=self.logger
        )

    async def execute(self) -> None:
        """Execute reactive behavior loop."""
        config = self.behavior_config.config

        self.logger.info(f"Starting reactive behavior {self.behavior_name}")

        # Setup packet listener for this behavior
        listen_transport_name = config.get("listen_transport")
        if (
            not listen_transport_name
            or listen_transport_name
            not in self.execution_context.transport_layer.transports
        ):
            self.logger.error(
                f"Invalid listen_transport for behavior {self.behavior_name}: {listen_transport_name}"
            )
            return

        listen_transport = self.execution_context.transport_layer.transports[
            listen_transport_name
        ]

        # Register packet callback for this behavior
        async def packet_callback(payload: bytes, source: str):
            try:
                await self._handle_packet(payload, source)
            except Exception as e:
                self.logger.error(
                    f"Error handling packet in reactive behavior {self.behavior_name}: {e}"
                )

        listen_transport.add_packet_callback(packet_callback)
        self.logger.debug(
            f"Registered packet callback for reactive behavior {self.behavior_name}"
        )

        # Keep the behavior running
        try:
            while True:
                # Check if behavior should still run
                if not self.execution_context.should_behavior_run(
                    self.behavior_config.active_states
                ):
                    await asyncio.sleep(1)
                    continue

                await asyncio.sleep(0.1)  # Small sleep to prevent busy loop

        except asyncio.CancelledError:
            self.logger.info(f"Reactive behavior {self.behavior_name} cancelled")

    async def _handle_packet(self, payload: bytes, source: str) -> None:
        """
        Handle received packet for reactive behavior.

        :param payload: Received payload
        :type payload: bytes
        :param source: Source address
        :type source: str
        """
        config = self.behavior_config.config

        # Check if behavior should run based on current state
        if not self.execution_context.should_behavior_run(
            self.behavior_config.active_states
        ):
            return

        # Get trigger configuration
        trigger_config = config.get("trigger") or config.get("triggers", [{}])[0]

        self.logger.info(
            f"Reactive behavior {self.behavior_name}: received packet from {source}, "
            f"payload: {payload.hex()[:50]}... (length: {len(payload)})"
        )

        # Check source pattern if specified
        source_pattern = trigger_config.get("source_pattern")
        if source_pattern:
            if not self._match_address_pattern(source, source_pattern):
                self.logger.debug(
                    f"Source {source} doesn't match pattern {source_pattern}"
                )
                return
            else:
                self.logger.info(f"Source {source} matches pattern {source_pattern}")

        # Check payload pattern if specified
        payload_pattern = trigger_config.get("payload_pattern")
        if payload_pattern:
            if not self._match_payload_pattern(payload, payload_pattern):
                self.logger.info("Payload doesn't match pattern")
                return
            else:
                self.logger.info("Payload matches pattern!")
        else:
            self.logger.info("No payload pattern specified, accepting all payloads")

        # Trigger matched! Execute response if configured
        self.logger.debug(
            f"🎯 Reactive behavior {self.behavior_name}: trigger matched from {source}"
        )

        # Check if there are responses to send
        config = self.behavior_config.config
        has_responses = (
            "response" in config
            or "responses" in config
            or "response_transport" in config
        )

        if has_responses:
            success = await self._execute_response(source)
        else:
            # Silent behavior - just log and mark as successful
            self.logger.info(
                f"🔇 Silent behavior {self.behavior_name}: no responses configured, executing transition only"
            )
            success = True

        # Handle state transition based on execution result
        await self._handle_transition(success)

    def _match_address_pattern(self, address: str, pattern: str) -> bool:
        """
        Match address against pattern with wildcard support.

        :param address: Address to match
        :type address: str
        :param pattern: Pattern with potential wildcards
        :type pattern: str
        :return: True if matches
        :rtype: bool
        """
        # Convert wildcard pattern to regex
        regex_pattern = pattern.replace("*", ".*").replace("?", ".")
        regex_pattern = f"^{regex_pattern}$"

        try:
            return bool(re.match(regex_pattern, address))
        except re.error:
            self.logger.warning(f"Invalid pattern: {pattern}")
            return False

    def _match_payload_pattern(self, payload: bytes, pattern: str) -> bool:
        """
        Match payload against pattern using the existing PayloadAnalyzer with CAPTURE support.

        :param payload: Payload to match
        :type payload: bytes
        :param pattern: Pattern to match against (can contain variables, CAPTURE, WILDCARD, etc.)
        :type pattern: str
        :return: True if matches
        :rtype: bool
        """
        if pattern == "any":
            return True

        payload_hex = payload.hex().upper()

        # Check for CAPTURE patterns and use advanced matching
        if "[CAPTURE:" in pattern:
            match_success, captured_vars = (
                self.payload_analyzer.match_pattern_with_capture(
                    pattern, payload_hex, self.payload_builder
                )
            )

            # Store captured variables in the variable resolver
            for var_name, value in captured_vars.items():
                self.payload_builder.variable_resolver.variables[var_name] = value
                self.logger.info(f"Captured variable {var_name} = {value}")

            return match_success

        # For patterns with wildcards AND variables, resolve variables first while preserving wildcards
        if ("[WILDCARD:" in pattern or "[SKIP:" in pattern) and self._has_variables(
            pattern
        ):
            return self._match_pattern_with_variables_and_wildcards(
                pattern, payload_hex
            )

        # For patterns with wildcards but no variables, use the pattern processor directly
        if "[WILDCARD:" in pattern or "[SKIP:" in pattern:
            return self.payload_analyzer.pattern_processor.match_with_wildcards(
                pattern, payload_hex
            )

        # For regular patterns with variables, expand them first
        if "[" in pattern and "]" in pattern:
            try:
                # Build the expected pattern by expanding variables
                expanded_pattern = self.payload_builder.build_payload([pattern])
                if expanded_pattern:
                    expected_hex = expanded_pattern.upper()
                    self.logger.debug(f"Expanded pattern: {pattern} -> {expected_hex}")
                    self.logger.debug(f"Received payload: {payload_hex}")
                    # Compare the expanded pattern with received payload
                    if expected_hex == payload_hex:
                        return True
                    # Also try partial matching for flexibility
                    if expected_hex in payload_hex or payload_hex in expected_hex:
                        return True
                else:
                    self.logger.warning(f"Failed to expand pattern: {pattern}")
            except Exception as e:
                self.logger.error(f"Error expanding pattern {pattern}: {e}")

        # Fallback to simple pattern matching
        if pattern.upper() in payload_hex:
            return True

        return False

    async def _execute_response(self, trigger_source: str) -> bool:
        """
        Execute response for triggered reactive behavior.

        :param trigger_source: Source that triggered the behavior
        :type trigger_source: str
        :return: True if successful
        :rtype: bool
        """
        config = self.behavior_config.config
        response_config = config.get("response", {})

        try:
            # Handle response delay
            delay = response_config.get("delay", 0) / 1000.0  # Convert ms to seconds
            if delay > 0:
                self.logger.info(f"⏱️ {self.behavior_name}: applying delay of {delay}s")
                await asyncio.sleep(delay)

            # Check if there are actually packets/payloads to send
            has_packets = "packets" in response_config
            has_payload = (
                "payload" in response_config
                and response_config.get("payload")
                and len(response_config.get("payload", [])) > 0
            )

            if not has_packets and not has_payload:
                # Delay-only response - no packets to send
                self.logger.info(
                    f"🔇 {self.behavior_name}: delay-only response (no packets to send)"
                )
                return True

            # Get response transport and destination
            response_transport_name = config.get(
                "response_transport", config.get("transport")
            )
            # Use service from response config, fallback to behavior's service
            response_service_name = response_config.get("service") or config.get(
                "service"
            )
            destination = response_config.get("destination", "unknown")

            # Debug log to see which service is being used
            self.logger.info(
                f"Reactive behavior {self.behavior_name}: using service '{response_service_name}' for response"
            )

            # Handle special destination values
            if destination == "sender":
                destination = trigger_source
            else:
                # Resolve variables in destination address
                destination = self.payload_builder.variable_resolver.resolve_destination_variables(
                    destination
                )

            # Check if we have a new-style multi-packet configuration
            if "packets" in response_config:
                # New multi-packet API
                multi_response = self.response_manager.create_response_from_config(
                    response_config
                )

                # Update destination for all packets if not individually specified
                for packet in multi_response.packets:
                    if not packet.destination:
                        packet.destination = destination

                self.logger.warning(
                    f"📤 {self.behavior_name}: response → {destination}"
                )

                # Convert packets to payloads for send_responses
                response_payloads = []
                for packet in multi_response.packets:
                    # Build payload using payload_builder for variable expansion
                    built_payload = self.payload_builder.build_payload(packet.payload)
                    response_payloads.append(built_payload)

                success = await self.response_manager.send_responses(
                    transport_name=response_transport_name,
                    service_name=response_service_name,
                    destination=destination,
                    payloads=response_payloads,
                    mode=multi_response.mode,
                    ack_timeout=response_config.get("ack_timeout", 5.0),
                    retry_count=response_config.get("retry_count", 3),
                )

                if success:
                    self.logger.info(
                        f"Successfully sent {len(multi_response.packets)} response(s) via {response_transport_name}"
                    )

                return success

            # Build response payload(s)
            response_payloads = []
            if isinstance(response_config.get("payload"), list):
                # Check if it's a list of payload configs or a single payload config
                payload_configs = response_config.get("payload", [])
                if (
                    payload_configs
                    and isinstance(payload_configs[0], dict)
                    and "payload" in payload_configs[0]
                ):
                    # Multiple payload configurations
                    for payload_config in payload_configs:
                        payload = self.payload_builder.build_payload(
                            payload_config.get("payload", [])
                        )
                        response_payloads.append(payload)
                else:
                    # Single payload configuration
                    payload = self.payload_builder.build_payload(payload_configs)
                    response_payloads.append(payload)
            else:
                # Single payload
                payload = self.payload_builder.build_payload(
                    response_config.get("payload", [])
                )
                response_payloads.append(payload)

            # Determine response mode
            response_mode_str = response_config.get("mode", "single")
            try:
                response_mode = ResponseMode(response_mode_str)
            except ValueError:
                self.logger.warning(
                    f"Unknown response mode: {response_mode_str}, using single"
                )
                response_mode = ResponseMode.SINGLE

            # Send response(s)
            self.logger.warning(f"📤 {self.behavior_name}: response → {destination}")

            success = await self.response_manager.send_responses(
                transport_name=response_transport_name,
                service_name=response_service_name,
                destination=destination,
                payloads=response_payloads,
                mode=response_mode,
                ack_timeout=response_config.get("ack_timeout", 5.0),
                retry_count=response_config.get("retry_count", 3),
            )

            if success:
                self.logger.info(
                    f"Successfully sent {len(response_payloads)} response(s) via {response_transport_name}"
                )
            else:
                self.logger.error(
                    f"Failed to send one or more responses via {response_transport_name}"
                )
            return success

        except Exception as e:
            self.logger.error(
                f"Error executing reactive response {self.behavior_name}: {e}"
            )
            return False

    async def _handle_transition(self, success: bool) -> None:
        """
        Handle state transition based on execution result.

        :param success: Whether execution was successful
        :type success: bool
        """
        config = self.behavior_config.config

        # Look for transition in root config first
        transition = config.get("transition")

        # If not found, look in response config (for delay-only behaviors)
        if not transition:
            response_config = config.get("response", {})
            transition = response_config.get("transition")

        if transition and self.execution_context.state_machine:
            if success and isinstance(transition, str):
                # Simple transition string
                self.execution_context.state_machine.transition_to(transition)
                self.logger.warning(
                    f"🎯 Reactive behavior {self.behavior_name} triggered transition to {transition}"
                )
                # Notify behavior executor of state change
                if self.execution_context.behavior_executor:
                    self.execution_context.behavior_executor.on_state_change(transition)
            elif isinstance(transition, dict):
                # Complex transition based on success/error
                if success and "success" in transition:
                    new_state = transition["success"]
                    self.execution_context.state_machine.transition_to(new_state)
                    self.logger.warning(
                        f"🎯 Reactive behavior {self.behavior_name} triggered transition to {new_state}"
                    )
                    # Notify behavior executor of state change
                    if self.execution_context.behavior_executor:
                        self.execution_context.behavior_executor.on_state_change(
                            new_state
                        )
                elif not success and "error" in transition:
                    new_state = transition["error"]
                    self.execution_context.state_machine.transition_to(new_state)
                    self.logger.warning(
                        f"🎯 Reactive behavior {self.behavior_name} error triggered transition to {new_state}"
                    )
                    # Notify behavior executor of state change
                    if self.execution_context.behavior_executor:
                        self.execution_context.behavior_executor.on_state_change(
                            new_state
                        )

    def _has_variables(self, pattern):
        """Check if pattern contains variables (non-wildcard, non-SKIP tokens)"""
        import re

        # Find all [...] tokens
        tokens = re.findall(r"\[([^]]+)\]", pattern)
        for token in tokens:
            # Skip wildcard and SKIP tokens
            if not (token.startswith("WILDCARD:") or token.startswith("SKIP:")):
                return True
        return False

    def _match_pattern_with_variables_and_wildcards(self, pattern, payload_hex):
        """Match patterns that have both variables and wildcards/SKIP tokens"""
        try:
            # Use simple string masking approach for SKIP patterns
            return self._simple_skip_match(pattern, payload_hex)
        except Exception as e:
            self.logger.error(
                f"Error matching pattern with variables and wildcards: {e}"
            )
            return False

    def _resolve_variables_preserve_wildcards(self, pattern):
        """Resolve variables in pattern while preserving WILDCARD: and SKIP: tokens"""
        import re

        # Get variables from execution context
        variables = getattr(self.execution_context, "variables", {})

        # Find all tokens
        def replace_token(match):
            token = match.group(1)
            if token.startswith("WILDCARD:") or token.startswith("SKIP:"):
                # Preserve wildcard tokens as-is
                return f"[{token}]"
            else:
                # Try to resolve variable - extract variable name (before : if present)
                var_name = token.split(":")[0]
                if var_name in variables:
                    return variables[var_name]
                else:
                    self.logger.warning(f"Variable {var_name} not found in context")
                    return f"[{token}]"  # Keep unresolved variables as-is

        resolved = re.sub(r"\[([^]]+)\]", replace_token, pattern)
        return resolved

    def _simple_skip_match(self, pattern, payload_hex):
        """Simple pattern matching with SKIP wildcards using string masking"""
        import re

        # Get variables from execution context
        variables = getattr(self.execution_context, "variables", {})

        # 1. Resolve variables while preserving SKIP tokens
        def replace_variable(match):
            token = match.group(1)
            if token.startswith("SKIP:"):
                return f"[{token}]"
            else:
                var_name = token.split(":")[0]
                if var_name in variables:
                    return variables[var_name]
                else:
                    return f"[{token}]"

        resolved_pattern = re.sub(r"\[([^]]+)\]", replace_variable, pattern)
        self.logger.debug(f"Pattern with variables resolved: {resolved_pattern}")

        # 2. Build masked pattern and payload step by step
        pattern_parts = []
        payload_parts = []
        pattern_pos = 0
        payload_pos = 0

        # Find all SKIP tokens in order
        skip_matches = list(re.finditer(r"\[SKIP:(\d+)\]", resolved_pattern))

        for match in skip_matches:
            skip_length = int(match.group(1)) * 2  # *2 for hex characters

            # Add the part before this SKIP
            before_skip = resolved_pattern[pattern_pos : match.start()]
            pattern_parts.append(before_skip)
            payload_parts.append(
                payload_hex.upper()[payload_pos : payload_pos + len(before_skip)]
            )

            # Add the masked SKIP part
            pattern_parts.append("X" * skip_length)
            payload_parts.append("X" * skip_length)

            # Update positions
            pattern_pos = match.end()
            payload_pos += len(before_skip) + skip_length

        # Add the remaining part after the last SKIP
        if pattern_pos < len(resolved_pattern):
            remaining_pattern = resolved_pattern[pattern_pos:]
            pattern_parts.append(remaining_pattern)
            payload_parts.append(
                payload_hex.upper()[payload_pos : payload_pos + len(remaining_pattern)]
            )

        # Combine parts
        pattern_for_compare = "".join(pattern_parts)
        payload_for_compare = "".join(payload_parts)

        self.logger.debug(f"Masked pattern:  {pattern_for_compare}")
        self.logger.debug(f"Masked payload:  {payload_for_compare}")

        # 3. Compare masked strings
        return pattern_for_compare == payload_for_compare
