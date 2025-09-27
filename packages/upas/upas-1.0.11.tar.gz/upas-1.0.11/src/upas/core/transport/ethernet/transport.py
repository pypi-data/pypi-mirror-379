"""
UPAS Ethernet Transport

Ethernet/IP transport implementation using modular services.
"""

import socket
import asyncio
import logging
from typing import Dict, Any

from ..base import BaseTransport
from ..utils import parse_address, async_socket_sendto
from .ip_options import IPOptionsConfigurator
from .udp_service import UDPService, UDPMulticastService
from .tcp_service import TCPServerService, TCPClientService


logger = logging.getLogger(__name__)


class EthernetTransport(BaseTransport):
    """
    Ethernet/IP transport implementation using modular services.

    Supports UDP unicast, multicast, and TCP connections through dedicated services.
    """

    def __init__(self, name: str, config: Dict[str, Any]):
        """
        Initialize Ethernet transport.

        :param name: Transport name
        :type name: str
        :param config: Ethernet configuration
        :type config: dict
        """
        super().__init__(name, config)

        # Configuration
        self.ip_options = config.get("ip_options", {})
        self.interface = config.get("interface")
        self.ip_configurator = IPOptionsConfigurator(self.ip_options)

        # Service containers
        self.udp_services = {}
        self.tcp_services = {}

    async def start(self) -> None:
        """Start Ethernet transport services."""
        self.running = True

        services = self.config.get("services", {})

        for service_name, service_config in services.items():
            service_type = service_config.get("type")

            if service_type == "udp_unicast":
                await self._start_udp_service(service_name, service_config)
            elif service_type == "udp_multicast":
                await self._start_multicast_service(service_name, service_config)
            elif service_type == "tcp_server":
                await self._start_tcp_server(service_name, service_config)
            elif service_type == "tcp_client":
                await self._start_tcp_client(service_name, service_config)
            else:
                self.logger.warning(f"Unknown service type: {service_type}")

        self.logger.info(f"Ethernet transport '{self.name}' started")

    async def _start_udp_service(
        self, service_name: str, config: Dict[str, Any]
    ) -> None:
        """Start a UDP unicast service."""
        service = UDPService(service_name, config, self.ip_configurator, self.interface)
        service.add_packet_callback(self._notify_packet_received)
        await service.start()
        self.udp_services[service_name] = service

    async def _start_multicast_service(
        self, service_name: str, config: Dict[str, Any]
    ) -> None:
        """Start a UDP multicast service."""
        service = UDPMulticastService(
            service_name, config, self.ip_configurator, self.interface
        )
        service.add_packet_callback(self._notify_packet_received)
        await service.start()
        self.udp_services[service_name] = service

    async def _start_tcp_server(
        self, service_name: str, config: Dict[str, Any]
    ) -> None:
        """Start a TCP server service."""
        service = TCPServerService(service_name, config)
        service.add_packet_callback(self._notify_packet_received)
        await service.start()
        self.tcp_services[service_name] = service

    async def _start_tcp_client(
        self, service_name: str, config: Dict[str, Any]
    ) -> None:
        """Start a TCP client service."""
        service = TCPClientService(service_name, config)
        service.add_packet_callback(self._notify_packet_received)
        await service.start()
        self.tcp_services[service_name] = service

    async def send_packet(self, destination: str, payload: bytes) -> None:
        """
        Send packet via Ethernet with multiple fallback methods.

        :param destination: Destination address (host:port)
        :type destination: str
        :param payload: Packet payload
        :type payload: bytes
        """
        host, port = parse_address(destination)

        # Method 1: Try using existing UDP service if available
        for service in self.udp_services.values():
            if (
                hasattr(service, "socket")
                and service.socket
                and service.socket.type == socket.SOCK_DGRAM
            ):
                try:
                    await service.send_packet(destination, payload)
                    self.logger.debug("Sent packet via existing UDP service")
                    return
                except Exception as e:
                    self.logger.warning(f"Failed to send via UDP service: {e}")
                    continue

        # Method 2: Create temporary UDP socket
        try:
            self.logger.debug(f"Creating temporary UDP socket for {host}:{port}")
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # Bind to specific interface if specified
            if self.interface:
                try:
                    sock.setsockopt(
                        socket.SOL_SOCKET,
                        socket.SO_BINDTODEVICE,
                        self.interface.encode(),
                    )
                    self.logger.debug(f"Bound socket to interface: {self.interface}")
                except OSError as e:
                    self.logger.warning(
                        f"Failed to bind to interface {self.interface}: {e}"
                    )

            # Configure IP options including Don't Fragment for temporary socket
            self.ip_configurator.configure_socket(sock)

            await async_socket_sendto(sock, payload, (host, port))
            sock.close()
            self.logger.debug("Successfully sent packet via temporary socket")
            return

        except Exception as e:
            self.logger.error(f"Error sending packet via temporary socket: {e}")

        # Method 3: Create datagram endpoint (last resort)
        try:
            self.logger.debug(f"Using datagram endpoint for {host}:{port}")
            loop = asyncio.get_event_loop()
            transport, protocol = await loop.create_datagram_endpoint(
                lambda: asyncio.DatagramProtocol(), remote_addr=(host, port)
            )
            transport.sendto(payload)
            transport.close()
            self.logger.debug("Successfully sent packet via datagram endpoint")

        except Exception as e2:
            self.logger.error(f"All send methods failed: {e2}")
            raise

    async def send_packet_via_service(
        self, service_name: str, destination: str, payload: bytes
    ) -> None:
        """
        Send packet via a specific service.

        :param service_name: Service to use
        :type service_name: str
        :param destination: Destination address
        :type destination: str
        :param payload: Packet payload
        :type payload: bytes
        """
        # Check UDP services first
        if service_name in self.udp_services:
            service = self.udp_services[service_name]
            await service.send_packet(destination, payload)
            return

        # Check TCP services
        if service_name in self.tcp_services:
            service = self.tcp_services[service_name]
            if hasattr(service, "send_packet"):
                await service.send_packet(destination, payload)
            else:
                raise ValueError(
                    f"TCP service '{service_name}' does not support sending packets"
                )
            return

        raise ValueError(f"Service '{service_name}' not found")

    async def stop(self) -> None:
        """Stop Ethernet transport."""
        self.running = False

        # Stop all UDP services
        for service in self.udp_services.values():
            await service.stop()

        # Stop all TCP services
        for service in self.tcp_services.values():
            await service.stop()

        self.udp_services.clear()
        self.tcp_services.clear()

        self.logger.info(f"Ethernet transport '{self.name}' stopped")
