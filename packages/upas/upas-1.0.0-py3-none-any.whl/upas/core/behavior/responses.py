"""
Multi-packet response management system for UPAS behaviors
"""

import asyncio
import logging
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Any, List, Optional
from dataclasses import dataclass


class ResponseMode(Enum):
    """Response sending modes."""

    SINGLE = "single"  # Single packet response (default)
    SEQUENCE = "sequence"  # Sequential packets with ACK validation
    BURST = "burst"  # Parallel packets (no ACK waiting)
    DELAYED_SEQUENCE = "delayed_sequence"  # Sequential with delays between packets


class PacketStatus(Enum):
    """Status of individual packets in multi-packet response."""

    PENDING = "pending"
    SENT = "sent"
    ACKNOWLEDGED = "acknowledged"
    FAILED = "failed"
    TIMEOUT = "timeout"


@dataclass
class ResponsePacket:
    """Represents a single packet in a multi-packet response."""

    id: str
    payload: str
    destination: Optional[str] = None
    delay: float = 0.0
    timeout: float = 5.0
    retry_count: int = 0
    max_retries: int = 3
    status: PacketStatus = PacketStatus.PENDING

    def __post_init__(self):
        """Validate packet configuration."""
        if self.delay < 0:
            raise ValueError("Delay must be non-negative")
        if self.timeout <= 0:
            raise ValueError("Timeout must be positive")
        if self.max_retries < 0:
            raise ValueError("Max retries must be non-negative")


@dataclass
class MultiPacketResponse:
    """Configuration for multi-packet response."""

    mode: ResponseMode
    packets: List[ResponsePacket]
    global_timeout: float = 30.0
    fail_fast: bool = False
    success_threshold: float = 1.0  # Percentage of packets that must succeed
    ack_validator: Optional[str] = None  # ACK validation strategy

    def __post_init__(self):
        """Validate multi-packet response configuration."""
        if not self.packets:
            raise ValueError("Multi-packet response must have at least one packet")

        if not 0 <= self.success_threshold <= 1:
            raise ValueError("Success threshold must be between 0 and 1")

        if self.global_timeout <= 0:
            raise ValueError("Global timeout must be positive")


class ResponseStrategy(ABC):
    """Abstract base class for response sending strategies."""

    def __init__(self, transport, logger: Optional[logging.Logger] = None):
        """Initialize response strategy."""
        self.transport = transport
        self.transport_name = None  # For service-aware sending
        self.service_name = None  # For service-aware sending
        self.logger = logger or logging.getLogger(__name__)

    @abstractmethod
    async def send_response(self, response: MultiPacketResponse) -> Dict[str, Any]:
        """Send multi-packet response using specific strategy."""
        pass

    async def send_single_packet(self, packet: ResponsePacket) -> bool:
        """Send a single packet and return success status."""
        try:
            self.logger.debug(f"Sending packet {packet.id} to {packet.destination}")

            # Apply delay if specified
            if packet.delay > 0:
                await asyncio.sleep(packet.delay)

            # Convert hex payload to bytes
            if isinstance(packet.payload, str):
                payload_bytes = bytes.fromhex(packet.payload)
            else:
                payload_bytes = packet.payload

            # Send packet via transport layer
            if (
                self.transport_name
                and self.service_name
                and hasattr(self.transport, "send_packet_with_service")
            ):
                # Use service-aware sending via transport layer
                self.logger.debug(
                    f"Sending packet via service '{self.service_name}' on transport '{self.transport_name}'"
                )
                await self.transport.send_packet_with_service(
                    self.transport_name,
                    self.service_name,
                    packet.destination,
                    payload_bytes,
                )
            elif hasattr(self.transport, "send_packet"):
                # Direct transport interface
                await self.transport.send_packet(packet.destination, payload_bytes)
            elif hasattr(self.transport, "send_data"):
                # Legacy interface
                if packet.destination:
                    await self.transport.send_data(
                        packet.payload, destination=packet.destination
                    )
                else:
                    await self.transport.send_data(packet.payload)
            else:
                # Transport layer interface - resolve transport
                transport_name = getattr(
                    self.transport, "default_transport", "ethernet"
                )
                actual_transport = self.transport.get_transport(transport_name)
                await actual_transport.send_packet(packet.destination, payload_bytes)

            packet.status = PacketStatus.SENT
            return True

        except Exception as e:
            self.logger.error(f"Failed to send packet {packet.id}: {e}")
            packet.status = PacketStatus.FAILED
            return False


class SingleResponseStrategy(ResponseStrategy):
    """Strategy for single packet responses (default behavior)."""

    async def send_response(self, response: MultiPacketResponse) -> Dict[str, Any]:
        """Send single packet response."""
        if not response.packets:
            return {"success": False, "error": "No packets to send"}

        # Take only the first packet for single mode
        packet = response.packets[0]
        success = await self.send_single_packet(packet)

        return {
            "success": success,
            "packets_sent": 1 if success else 0,
            "packets_total": 1,
            "mode": "single",
        }


class BurstResponseStrategy(ResponseStrategy):
    """Strategy for parallel packet sending (burst mode)."""

    async def send_response(self, response: MultiPacketResponse) -> Dict[str, Any]:
        """Send all packets in parallel."""
        self.logger.info(f"Sending {len(response.packets)} packets in burst mode")

        # Create tasks for all packets
        tasks = []
        for packet in response.packets:
            task = asyncio.create_task(self.send_single_packet(packet))
            tasks.append(task)

        # Wait for all tasks with global timeout
        try:
            results = await asyncio.wait_for(
                asyncio.gather(*tasks, return_exceptions=True),
                timeout=response.global_timeout,
            )

            # Count successes
            success_count = sum(1 for result in results if result is True)
            success_rate = success_count / len(response.packets)

            overall_success = success_rate >= response.success_threshold

            return {
                "success": overall_success,
                "packets_sent": success_count,
                "packets_total": len(response.packets),
                "success_rate": success_rate,
                "mode": "burst",
            }

        except asyncio.TimeoutError:
            self.logger.error("Burst response timed out")
            return {
                "success": False,
                "error": "Global timeout exceeded",
                "mode": "burst",
            }


class SequenceResponseStrategy(ResponseStrategy):
    """Strategy for sequential packet sending with optional ACK validation."""

    def __init__(
        self, transport, logger: Optional[logging.Logger] = None, ack_validator=None
    ):
        """Initialize sequence response strategy."""
        super().__init__(transport, logger)
        self.ack_validator = ack_validator

        # Auto-enable TCP ACK validation if transport supports it
        if not ack_validator and hasattr(transport, "send_packet_with_service"):
            self.ack_validator = "tcp_auto"  # Enable automatic TCP ACK waiting

    async def send_response(self, response: MultiPacketResponse) -> Dict[str, Any]:
        """Send packets sequentially with optional ACK validation."""
        self.logger.info(f"Sending {len(response.packets)} packets sequentially")
        self.logger.debug(f"ACK validator configured: {self.ack_validator}")

        success_count = 0
        failed_packets = []

        for i, packet in enumerate(response.packets):
            self.logger.debug(
                f"Sending packet {i+1}/{len(response.packets)}: {packet.id}"
            )

            # Attempt to send packet with retries
            packet_success = await self._send_packet_with_retries(packet)

            if packet_success:
                success_count += 1

                # Wait for ACK if validator is configured
                if (
                    self.ack_validator and i < len(response.packets) - 1
                ):  # Not last packet
                    self.logger.debug(
                        f"Waiting for ACK after packet {packet.id} (validator: {self.ack_validator})"
                    )
                    ack_received = await self._wait_for_ack(packet)
                    if not ack_received:
                        self.logger.warning(f"No ACK received for packet {packet.id}")
                        if response.fail_fast:
                            break
                else:
                    self.logger.debug(
                        f"Skipping ACK wait: validator={self.ack_validator}, last_packet={i >= len(response.packets) - 1}"
                    )
            else:
                failed_packets.append(packet.id)
                if response.fail_fast:
                    self.logger.error(f"Packet {packet.id} failed, stopping sequence")
                    break

        success_rate = success_count / len(response.packets)
        overall_success = success_rate >= response.success_threshold

        return {
            "success": overall_success,
            "packets_sent": success_count,
            "packets_total": len(response.packets),
            "failed_packets": failed_packets,
            "success_rate": success_rate,
            "mode": "sequence",
        }

    async def _send_packet_with_retries(self, packet: ResponsePacket) -> bool:
        """Send packet with retry logic, including pre-send delay."""
        # Apply packet delay BEFORE sending (not on retries)
        packet_delay = getattr(packet, "delay", 0)
        if packet_delay > 0:
            self.logger.debug(
                f"Applying delay of {packet_delay}s before sending packet {packet.id}"
            )
            await asyncio.sleep(packet_delay)

        for attempt in range(packet.max_retries + 1):
            if attempt > 0:
                self.logger.debug(f"Retrying packet {packet.id}, attempt {attempt}")
                await asyncio.sleep(0.5 * attempt)  # Exponential backoff

            success = await self.send_single_packet(packet)
            if success:
                return True

            packet.retry_count = attempt + 1

        return False

    async def _wait_for_ack(self, packet: ResponsePacket) -> bool:
        """Wait for ACK validation (if configured)."""
        if not self.ack_validator:
            return True  # No validation needed

        try:
            if self.ack_validator == "tcp_auto":
                # For TCP connections, wait for socket drain confirmation
                # This ensures the data is transmitted at TCP level
                await self._wait_tcp_ack(packet)
                return True
            else:
                # Custom ACK validator
                await asyncio.sleep(0.1)  # Simulate ACK wait
                return True

        except asyncio.TimeoutError:
            self.logger.warning(f"ACK timeout for packet {packet.id}")
            return False

    async def _wait_tcp_ack(self, packet: ResponsePacket) -> None:
        """Wait for TCP level ACK by checking connection drain status."""
        ack_timeout = getattr(packet, "timeout", 1.0)  # Default 1 second timeout

        self.logger.debug(
            f"Waiting for TCP ACK for packet {packet.id} (timeout: {ack_timeout}s)"
        )

        # Try to get TCP drain status from the transport layer
        tcp_drained = False
        try:
            # Check if we have access to transport layer and specific service
            if (
                hasattr(self.transport, "transports")
                and self.service_name
                and hasattr(self.transport, "get_service")
            ):
                self.logger.debug(
                    f"Using service-specific TCP drain: {self.transport_name}.{self.service_name}"
                )
                # Get the specific TCP service used for sending
                tcp_service = self.transport.get_service(
                    self.transport_name, self.service_name
                )
                if tcp_service and hasattr(
                    tcp_service, "get_last_connection_drain_status"
                ):
                    self.logger.debug(f"Calling drain on service: {tcp_service}")
                    # Call the specific TCP service method to wait for drain
                    tcp_drained = await asyncio.wait_for(
                        tcp_service.get_last_connection_drain_status(),
                        timeout=ack_timeout,
                    )
                    if tcp_drained:
                        self.logger.debug(
                            f"TCP connection drained for packet {packet.id} via service {self.service_name}"
                        )
                        return  # Return immediately after successful drain
                else:
                    self.logger.debug(
                        f"Service not found or no drain method: {tcp_service}"
                    )
            else:
                self.logger.debug(
                    f"Transport conditions not met: transports={hasattr(self.transport, 'transports')}, service_name={self.service_name}, get_service={hasattr(self.transport, 'get_service')}"
                )

            # Fallback: check all transports if service-specific lookup failed
            if not tcp_drained and hasattr(self.transport, "transports"):
                self.logger.debug("Trying fallback transport lookup")
                for (
                    transport_name,
                    transport_service,
                ) in self.transport.transports.items():
                    if hasattr(transport_service, "get_last_connection_drain_status"):
                        self.logger.debug(
                            f"Found drain method on transport: {transport_name}"
                        )
                        # Call the TCP service method to wait for drain
                        tcp_drained = await asyncio.wait_for(
                            transport_service.get_last_connection_drain_status(),
                            timeout=ack_timeout,
                        )
                        if tcp_drained:
                            self.logger.debug(
                                f"TCP connection drained for packet {packet.id}"
                            )
                            return  # Return immediately after successful drain

        except asyncio.TimeoutError:
            self.logger.warning(f"TCP drain timeout for packet {packet.id}")
        except Exception as e:
            self.logger.debug(f"Could not check TCP drain status: {e}")

        # Fallback only if TCP drain check failed
        if not tcp_drained:
            self.logger.debug(f"Using fallback delay for packet {packet.id}")
            # Pour un vrai comportement TCP, l'ACK devrait arriver en quelques millisecondes
            # Utilisons un délai beaucoup plus court et réaliste
            await asyncio.sleep(
                min(ack_timeout, 0.010)
            )  # Cap à 10ms pour un comportement TCP très réaliste

        self.logger.debug(f"TCP ACK wait completed for packet {packet.id}")


class MultiPacketResponseManager:
    """Manager for multi-packet response strategies."""

    def __init__(self, transport, logger: Optional[logging.Logger] = None):
        """Initialize multi-packet response manager."""
        self.transport = transport
        self.logger = logger or logging.getLogger(__name__)

        # Initialize strategies
        self.strategies = {
            ResponseMode.SINGLE: SingleResponseStrategy(transport, logger),
            ResponseMode.BURST: BurstResponseStrategy(transport, logger),
            ResponseMode.SEQUENCE: SequenceResponseStrategy(transport, logger),
            ResponseMode.DELAYED_SEQUENCE: SequenceResponseStrategy(transport, logger),
        }

    def create_response_from_config(
        self, config: Dict[str, Any]
    ) -> MultiPacketResponse:
        """Create multi-packet response from configuration."""
        # Parse response mode
        mode_str = config.get("mode", "single")
        try:
            mode = ResponseMode(mode_str)
        except ValueError:
            self.logger.warning(f"Unknown response mode: {mode_str}, using single")
            mode = ResponseMode.SINGLE

        # Parse packets
        packets = []
        packet_configs = config.get("packets", [])

        # Handle backward compatibility: single payload
        if "payload" in config and not packet_configs:
            payload_raw = config["payload"]
            # Handle payload as either list or string
            if isinstance(payload_raw, list):
                payload = "".join(payload_raw)
            else:
                payload = payload_raw
            packet_configs = [{"payload": payload}]

        for i, packet_config in enumerate(packet_configs):
            # Handle payload as either list (new format) or string (backward compatibility)
            payload_raw = packet_config.get("payload", "")
            if isinstance(payload_raw, list):
                payload = "".join(payload_raw)  # Join list of strings
            else:
                payload = payload_raw  # Use string directly

            packet = ResponsePacket(
                id=packet_config.get("id", f"packet_{i}"),
                payload=payload,
                destination=packet_config.get("destination"),
                delay=packet_config.get("delay", 0.0),
                timeout=packet_config.get("timeout", 5.0),
                max_retries=packet_config.get("max_retries", 3),
            )
            packets.append(packet)

        return MultiPacketResponse(
            mode=mode,
            packets=packets,
            global_timeout=config.get("global_timeout", 30.0),
            fail_fast=config.get("fail_fast", False),
            success_threshold=config.get("success_threshold", 1.0),
            ack_validator=config.get(
                "ack_validator"
            ),  # Parse ack_validator from config
        )

    async def send_multi_response(
        self, response: MultiPacketResponse
    ) -> Dict[str, Any]:
        """Send multi-packet response using appropriate strategy."""
        strategy = self.strategies.get(response.mode)
        if not strategy:
            return {"success": False, "error": f"No strategy for mode: {response.mode}"}

        # Configure ACK validator if specified and strategy supports it
        if response.ack_validator and hasattr(strategy, "ack_validator"):
            strategy.ack_validator = response.ack_validator
            self.logger.debug(f"Configured ACK validator: {response.ack_validator}")

        self.logger.info(
            f"Executing {response.mode.value} response with {len(response.packets)} packets"
        )

        start_time = asyncio.get_event_loop().time()
        result = await strategy.send_response(response)
        end_time = asyncio.get_event_loop().time()

        result["execution_time"] = end_time - start_time
        return result

    async def send_responses(
        self,
        transport_name: str,
        service_name: Optional[str],
        destination: str,
        payloads: List[str],
        mode: ResponseMode = ResponseMode.SINGLE,
        ack_timeout: float = 5.0,
        retry_count: int = 3,
    ) -> bool:
        """
        Simplified interface for sending responses (backward compatibility).

        :param transport_name: Transport to use
        :param service_name: Service to use (optional)
        :param destination: Destination address
        :param payloads: List of payload strings
        :param mode: Response mode
        :param ack_timeout: ACK timeout
        :param retry_count: Retry count
        :return: True if successful
        """
        try:
            # Get the transport layer (not the specific transport)
            if hasattr(self.transport, "send_packet_with_service") and service_name:
                # Use transport layer with service support
                transport_layer = self.transport
                actual_transport = None
            elif hasattr(self.transport, "get_transport"):
                # Get the specific transport
                actual_transport = self.transport.get_transport(transport_name)
                transport_layer = self.transport
                if not actual_transport:
                    self.logger.error(f"Transport '{transport_name}' not found")
                    return False
            else:
                # Assume transport is already the right one
                actual_transport = self.transport
                transport_layer = None

            # Create packets from payloads
            packets = []
            for i, payload in enumerate(payloads):
                packet = ResponsePacket(
                    id=f"response_{i}",
                    payload=payload,
                    destination=destination,
                    timeout=ack_timeout,
                    max_retries=retry_count,
                )
                packets.append(packet)

            # Create response
            response = MultiPacketResponse(
                mode=mode,
                packets=packets,
                global_timeout=ack_timeout * len(payloads),
                fail_fast=True,
                success_threshold=1.0,
            )

            # Create strategy with the appropriate transport and service info
            strategy = self.strategies.get(mode)
            if strategy:
                if transport_layer and service_name:
                    # Set transport layer and service for service-aware sending
                    strategy.transport = transport_layer
                    strategy.transport_name = transport_name
                    strategy.service_name = service_name
                elif actual_transport:
                    # Update strategy transport for direct sending
                    strategy.transport = actual_transport
                    strategy.transport_name = None
                    strategy.service_name = None

            # Send response
            result = await self.send_multi_response(response)
            return result.get("success", False)

        except Exception as e:
            self.logger.error(f"Error sending responses: {e}")
            return False


# Convenience functions
def create_single_response(
    payload: str, destination: Optional[str] = None
) -> MultiPacketResponse:
    """Create a single packet response."""
    packet = ResponsePacket(
        id="single_packet", payload=payload, destination=destination
    )

    return MultiPacketResponse(mode=ResponseMode.SINGLE, packets=[packet])


def create_burst_response(
    payloads: List[str], destinations: Optional[List[str]] = None
) -> MultiPacketResponse:
    """Create a burst response with multiple packets."""
    packets = []

    for i, payload in enumerate(payloads):
        destination = (
            destinations[i] if destinations and i < len(destinations) else None
        )
        packet = ResponsePacket(
            id=f"burst_packet_{i}", payload=payload, destination=destination
        )
        packets.append(packet)

    return MultiPacketResponse(mode=ResponseMode.BURST, packets=packets)


def create_sequence_response(
    payloads: List[str],
    delays: Optional[List[float]] = None,
    destinations: Optional[List[str]] = None,
) -> MultiPacketResponse:
    """Create a sequential response with optional delays."""
    packets = []

    for i, payload in enumerate(payloads):
        delay = delays[i] if delays and i < len(delays) else 0.0
        destination = (
            destinations[i] if destinations and i < len(destinations) else None
        )

        packet = ResponsePacket(
            id=f"seq_packet_{i}", payload=payload, destination=destination, delay=delay
        )
        packets.append(packet)

    return MultiPacketResponse(mode=ResponseMode.SEQUENCE, packets=packets)
