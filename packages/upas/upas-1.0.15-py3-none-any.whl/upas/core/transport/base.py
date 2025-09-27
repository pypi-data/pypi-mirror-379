"""
UPAS Transport Base Classes

Abstract base classes and interfaces for transport implementations.
"""

import logging
from typing import Dict, Any, Callable
from abc import ABC, abstractmethod


class BaseTransport(ABC):
    """
    Abstract base class for all transport implementations.

    Each transport type (Ethernet, LoRa, Bluetooth, etc.) should inherit
    from this class and implement the required methods.
    """

    def __init__(self, name: str, config: Dict[str, Any]):
        """
        Initialize base transport.

        :param name: Transport name identifier
        :type name: str
        :param config: Transport configuration
        :type config: dict
        """
        self.name = name
        self.config = config
        self.logger = logging.getLogger(f"{__name__}.{name}")
        self.running = False
        self.callbacks = []

    @abstractmethod
    async def start(self) -> None:
        """Start the transport layer."""
        pass

    @abstractmethod
    async def stop(self) -> None:
        """Stop the transport layer."""
        pass

    @abstractmethod
    async def send_packet(self, destination: str, payload: bytes) -> None:
        """
        Send a packet through this transport.

        :param destination: Destination address
        :type destination: str
        :param payload: Packet payload
        :type payload: bytes
        """
        pass

    def add_packet_callback(self, callback: Callable[[bytes, str], None]) -> None:
        """
        Add a callback for received packets.

        :param callback: Callback function (payload, source) -> None
        :type callback: callable
        """
        self.callbacks.append(callback)

    async def _notify_packet_received(self, payload: bytes, source: str) -> None:
        """
        Notify all callbacks of received packet.

        :param payload: Received payload
        :type payload: bytes
        :param source: Source address
        :type source: str
        """
        for callback in self.callbacks:
            try:
                await callback(payload, source)
            except Exception as e:
                self.logger.error(f"Error in packet callback: {e}")
