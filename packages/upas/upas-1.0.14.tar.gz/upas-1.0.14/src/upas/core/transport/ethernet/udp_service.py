"""
UPAS UDP Services

UDP unicast and multicast service implementations.
"""

import socket
import struct
import asyncio
import logging
from typing import Dict, Any

from ..utils import parse_address, async_socket_sendto, async_socket_recvfrom
from .ip_options import IPOptionsConfigurator


logger = logging.getLogger(__name__)


class UDPService:
    """Base UDP service implementation."""

    def __init__(
        self,
        name: str,
        config: Dict[str, Any],
        ip_configurator: IPOptionsConfigurator,
        interface: str = None,
    ):
        """
        Initialize UDP service.

        :param name: Service name
        :type name: str
        :param config: Service configuration
        :type config: dict
        :param ip_configurator: IP options configurator
        :type ip_configurator: IPOptionsConfigurator
        :param interface: Network interface to bind to
        :type interface: str
        """
        self.name = name
        self.config = config
        self.ip_configurator = ip_configurator
        self.interface = interface
        self.socket = None
        self.running = False
        self.packet_callbacks = []
        self._receive_task = None

    async def start(self) -> None:
        """Start UDP service."""
        bind_addr = self.config.get("bind", "0.0.0.0:0")
        host, port = parse_address(bind_addr)

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind to specific interface if specified
        if self.interface:
            try:
                self.socket.setsockopt(
                    socket.SOL_SOCKET, socket.SO_BINDTODEVICE, self.interface.encode()
                )
                logger.debug(f"Bound socket to interface: {self.interface}")
            except OSError as e:
                logger.warning(f"Failed to bind to interface {self.interface}: {e}")

        # Configure IP options
        self.ip_configurator.configure_socket(self.socket)

        self.socket.bind((host, port))
        self.socket.setblocking(False)

        self.running = True

        # Start receiving task
        self._receive_task = asyncio.create_task(self._receive_loop())

        logger.debug(f"Started UDP service '{self.name}' on {host}:{port}")

    async def stop(self) -> None:
        """Stop UDP service."""
        self.running = False

        # Cancel receive task if running
        if self._receive_task and not self._receive_task.done():
            self._receive_task.cancel()
            try:
                await self._receive_task
            except asyncio.CancelledError:
                pass

        if self.socket:
            self.socket.close()
            self.socket = None

    async def send_packet(self, destination: str, payload: bytes) -> None:
        """
        Send UDP packet.

        :param destination: Destination address
        :type destination: str
        :param payload: Packet payload
        :type payload: bytes
        """
        if not self.socket:
            raise RuntimeError(f"UDP service '{self.name}' not started")

        host, port = parse_address(destination)
        await async_socket_sendto(self.socket, payload, (host, port))

    def add_packet_callback(self, callback) -> None:
        """Add callback for received packets."""
        self.packet_callbacks.append(callback)

    async def _receive_loop(self) -> None:
        """UDP packet receiving loop."""
        while self.running:
            try:
                result = await async_socket_recvfrom(self.socket)
                if not result or len(result) != 2:
                    # Handle empty or malformed response
                    await asyncio.sleep(0.01)
                    continue

                data, addr = result
                source = f"{addr[0]}:{addr[1]}"

                # Notify all callbacks
                for callback in self.packet_callbacks:
                    try:
                        await callback(data, source)
                    except Exception as e:
                        logger.error(f"Error in packet callback: {e}")

            except asyncio.CancelledError:
                break
            except socket.error as e:
                if e.errno == 11:  # EAGAIN - would block
                    await asyncio.sleep(0.01)
                    continue
                logger.error(f"Socket error in UDP receive: {e}")
                await asyncio.sleep(0.1)
            except Exception as e:
                logger.error(f"Error in UDP receive loop: {e}")
                await asyncio.sleep(0.1)


class UDPMulticastService(UDPService):
    """UDP multicast service implementation."""

    async def start(self) -> None:
        """Start UDP multicast service."""
        await super().start()

        # Join multicast groups
        multicast_groups = self.config.get("multicast_groups", [])
        for group in multicast_groups:
            try:
                mreq = struct.pack("4sl", socket.inet_aton(group), socket.INADDR_ANY)
                self.socket.setsockopt(
                    socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq
                )
                logger.debug(f"Joined multicast group: {group}")
            except Exception as e:
                logger.error(f"Failed to join multicast group {group}: {e}")

        logger.debug(f"Started multicast service '{self.name}'")
