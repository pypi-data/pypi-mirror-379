"""
UPAS Transport Layer Manager

Main transport layer manager that orchestrates multiple transport instances.
"""

import logging
from typing import Dict, Any, Optional

from .base import BaseTransport
from .ethernet import EthernetTransport
from .raw import RawTransport


logger = logging.getLogger(__name__)


class TransportLayer:
    """
    Main transport layer manager.

    Manages multiple transport instances and routes packets between them.
    """

    def __init__(self):
        """Initialize transport layer."""
        self.logger = logging.getLogger(__name__)
        self.transports = {}
        self.running = False

    async def register_transports(
        self, transport_configs: Dict[str, Dict[str, Any]]
    ) -> None:
        """
        Register multiple transports from configuration.

        :param transport_configs: Transport configurations
        :type transport_configs: dict
        """
        for transport_name, config in transport_configs.items():
            transport_type = config.get("type", "ethernet")

            if transport_type == "ethernet":
                transport = EthernetTransport(transport_name, config)
            elif transport_type == "raw":
                transport = RawTransport(transport_name, config)
            else:
                self.logger.error(f"Unknown transport type: {transport_type}")
                continue

            self.transports[transport_name] = transport
            self.logger.debug(f"Registered transport: {transport_name}")

    async def start(self) -> None:
        """Start all registered transports."""
        self.running = True

        for transport in self.transports.values():
            await transport.start()

        self.logger.info("Transport layer started")

    async def stop(self) -> None:
        """Stop all transports."""
        self.running = False

        for transport in self.transports.values():
            await transport.stop()

        self.logger.info("Transport layer stopped")

    async def send_packet(
        self, transport_name: str, destination: str, payload: bytes
    ) -> None:
        """
        Send packet through specified transport.

        :param transport_name: Transport to use
        :type transport_name: str
        :param destination: Destination address
        :type destination: str
        :param payload: Packet payload
        :type payload: bytes
        :raises KeyError: If transport not found
        """
        if transport_name not in self.transports:
            raise KeyError(f"Transport not found: {transport_name}")

        transport = self.transports[transport_name]
        await transport.send_packet(destination, payload)

    async def send_packet_with_service(
        self, transport_name: str, service_name: str, destination: str, payload: bytes
    ) -> None:
        """
        Send packet through specified transport using a specific service.

        :param transport_name: Transport to use
        :type transport_name: str
        :param service_name: Service to use within the transport
        :type service_name: str
        :param destination: Destination address
        :type destination: str
        :param payload: Packet payload
        :type payload: bytes
        :raises KeyError: If transport not found
        :raises ValueError: If service not found or not supported
        """
        if transport_name not in self.transports:
            raise KeyError(f"Transport not found: {transport_name}")

        transport = self.transports[transport_name]

        # Check if transport supports service-specific sending
        if hasattr(transport, "send_packet_via_service"):
            await transport.send_packet_via_service(service_name, destination, payload)
        else:
            # Fallback to regular send_packet
            self.logger.warning(
                f"Transport {transport_name} does not support service-specific sending, using regular send"
            )
            await transport.send_packet(destination, payload)

    def get_transport(self, name: str) -> Optional[BaseTransport]:
        """
        Get transport by name.

        :param name: Transport name
        :type name: str
        :return: Transport instance or None
        :rtype: BaseTransport or None
        """
        return self.transports.get(name)
