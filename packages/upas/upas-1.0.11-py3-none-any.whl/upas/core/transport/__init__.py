"""
UPAS Transport Package

Modular transport layer implementation with support for multiple transport types.
"""

# Import the main classes for backward compatibility
from .base import BaseTransport
from .layer import TransportLayer
from .ethernet import EthernetTransport
from .raw import RawTransport

# Import specific services if needed
from .ethernet import (
    UDPService,
    UDPMulticastService,
    TCPServerService,
    TCPClientService,
    IPOptionsConfigurator,
)

# Import utilities
from .utils import parse_address, async_socket_sendto, async_socket_recvfrom

__all__ = [
    # Main classes (backward compatibility)
    "BaseTransport",
    "TransportLayer",
    "EthernetTransport",
    "RawTransport",
    # Ethernet services
    "UDPService",
    "UDPMulticastService",
    "TCPServerService",
    "TCPClientService",
    "IPOptionsConfigurator",
    # Utilities
    "parse_address",
    "async_socket_sendto",
    "async_socket_recvfrom",
]
