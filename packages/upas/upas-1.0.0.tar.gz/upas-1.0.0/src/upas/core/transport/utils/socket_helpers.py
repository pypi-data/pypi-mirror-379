"""
UPAS Socket Helpers

Async socket utilities and helpers.
"""

import asyncio
import socket
import logging
from typing import Tuple


logger = logging.getLogger(__name__)


async def async_socket_sendto(
    sock: socket.socket, data: bytes, address: Tuple[str, int]
) -> None:
    """
    Send data through socket using async method with fallbacks.

    :param sock: Socket to use
    :type sock: socket.socket
    :param data: Data to send
    :type data: bytes
    :param address: Destination address
    :type address: tuple
    """
    loop = asyncio.get_event_loop()

    try:
        # Try modern async socket method
        if hasattr(loop, "sock_sendto"):
            await loop.sock_sendto(sock, data, address)
        else:
            # Fallback to executor
            await loop.run_in_executor(None, lambda: sock.sendto(data, address))
    except Exception as e:
        logger.error(f"Error in async socket sendto: {e}")
        raise


async def async_socket_recvfrom(
    sock: socket.socket, bufsize: int = 4096
) -> Tuple[bytes, Tuple[str, int]]:
    """
    Receive data from socket using async method with fallbacks.

    :param sock: Socket to use
    :type sock: socket.socket
    :param bufsize: Buffer size
    :type bufsize: int
    :return: (data, address) tuple
    :rtype: tuple
    """
    loop = asyncio.get_event_loop()

    try:
        # Try modern async socket method
        if hasattr(loop, "sock_recvfrom"):
            return await loop.sock_recvfrom(sock, bufsize)
        else:
            # Fallback to executor
            return await loop.run_in_executor(None, lambda: sock.recvfrom(bufsize))
    except BlockingIOError:
        # Normal for non-blocking sockets when no data is available
        raise
    except OSError as e:
        if e.errno == 11:  # EAGAIN/EWOULDBLOCK - Resource temporarily unavailable
            # This is normal for non-blocking sockets, don't log as error
            raise BlockingIOError("No data available") from e
        else:
            logger.error(f"Error in async socket recvfrom: {e}")
            raise
    except Exception as e:
        logger.error(f"Error in async socket recvfrom: {e}")
        raise
