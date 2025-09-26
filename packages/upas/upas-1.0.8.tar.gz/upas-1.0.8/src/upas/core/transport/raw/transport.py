"""
UPAS Raw Transport

Raw packet transport for exotic protocols or direct hardware access.
"""

import socket
import asyncio
import logging

from ..base import BaseTransport
from ..utils import async_socket_sendto, async_socket_recvfrom


logger = logging.getLogger(__name__)


class RawTransport(BaseTransport):
    """
    Raw packet transport for exotic protocols or direct hardware access.

    This transport allows sending/receiving raw packets when standard
    sockets are insufficient.
    """

    def __init__(self, name: str, config: dict):
        """
        Initialize raw transport.

        :param name: Transport name
        :type name: str
        :param config: Raw transport configuration
        :type config: dict
        """
        super().__init__(name, config)
        self.raw_socket = None

    async def start(self) -> None:
        """Start raw transport."""
        self.running = True

        # Raw sockets require root privileges on Linux
        try:
            self.raw_socket = socket.socket(
                socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003)
            )
            self.raw_socket.setblocking(False)

            # Start receiving task
            asyncio.create_task(self._receive_loop())

            self.logger.info(f"Raw transport '{self.name}' started")

        except PermissionError:
            self.logger.error("Raw sockets require root privileges")
            raise
        except Exception as e:
            self.logger.error(f"Failed to start raw transport: {e}")
            raise

    async def _receive_loop(self) -> None:
        """Raw packet receiving loop."""
        while self.running:
            try:
                data, addr = await async_socket_recvfrom(self.raw_socket, 65535)
                source = str(addr) if addr else "unknown"

                # Notify all callbacks
                await self._notify_packet_received(data, source)

            except asyncio.CancelledError:
                break
            except socket.error as e:
                if e.errno == 11:  # EAGAIN - would block
                    await asyncio.sleep(0.01)
                    continue
                self.logger.error(f"Socket error in raw receive: {e}")
                await asyncio.sleep(0.1)
            except Exception as e:
                self.logger.error(f"Error in raw receive loop: {e}")
                await asyncio.sleep(0.1)

    async def send_packet(self, destination: str, payload: bytes) -> None:
        """
        Send raw packet.

        :param destination: Destination (interface or address)
        :type destination: str
        :param payload: Raw packet data
        :type payload: bytes
        """
        if not self.raw_socket:
            raise RuntimeError("Raw transport not started")

        try:
            await async_socket_sendto(self.raw_socket, payload, destination)
        except Exception as e:
            self.logger.error(f"Error sending raw packet: {e}")
            raise

    async def stop(self) -> None:
        """Stop raw transport."""
        self.running = False

        if self.raw_socket:
            self.raw_socket.close()
            self.raw_socket = None

        self.logger.info(f"Raw transport '{self.name}' stopped")
