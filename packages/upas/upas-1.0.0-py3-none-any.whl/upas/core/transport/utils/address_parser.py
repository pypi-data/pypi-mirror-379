"""
UPAS Transport Utilities

Common utilities for transport implementations.
"""

from typing import Tuple


def parse_address(address: str) -> Tuple[str, int]:
    """
    Parse address string into host and port.

    :param address: Address string (host:port)
    :type address: str
    :return: (host, port) tuple
    :rtype: tuple
    """
    if ":" in address:
        host, port_str = address.rsplit(":", 1)
        port = int(port_str)
    else:
        host = address
        port = 0

    return host, port
