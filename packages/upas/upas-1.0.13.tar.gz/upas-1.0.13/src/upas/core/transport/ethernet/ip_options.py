"""
UPAS IP Options Configuration

Handles IP-level socket configuration including Don't Fragment, TTL, TOS, etc.
"""

import socket
import platform
import logging
from typing import Dict, Any


logger = logging.getLogger(__name__)


class IPOptionsConfigurator:
    """Configures IP options on sockets."""

    def __init__(self, ip_options: Dict[str, Any]):
        """
        Initialize IP options configurator.

        :param ip_options: IP options configuration
        :type ip_options: dict
        """
        self.ip_options = ip_options
        self.dont_fragment = ip_options.get("dont_fragment", True)
        self.ttl = ip_options.get("ttl")
        self.tos = ip_options.get("tos")

    def configure_socket(self, sock: socket.socket) -> None:
        """
        Configure IP options on a socket including Don't Fragment flag.

        :param sock: Socket to configure
        :type sock: socket.socket
        """
        try:
            self._configure_dont_fragment(sock)
            self._configure_ttl(sock)
            self._configure_tos(sock)
        except Exception as e:
            logger.warning(f"Failed to configure IP options: {e}")

    def _configure_dont_fragment(self, sock: socket.socket) -> None:
        """Configure Don't Fragment flag based on platform."""
        if not self.dont_fragment:
            return

        try:
            if platform.system() == "Linux":
                # Use numeric values for Linux compatibility
                IP_MTU_DISCOVER = 10
                IP_PMTUDISC_DO = 2

                if hasattr(socket, "IP_MTU_DISCOVER"):
                    sock.setsockopt(
                        socket.IPPROTO_IP, socket.IP_MTU_DISCOVER, socket.IP_PMTUDISC_DO
                    )
                else:
                    sock.setsockopt(socket.IPPROTO_IP, IP_MTU_DISCOVER, IP_PMTUDISC_DO)
                logger.debug("Set Don't Fragment flag (Linux)")
            elif platform.system() == "Windows":
                sock.setsockopt(socket.IPPROTO_IP, socket.IP_DONTFRAGMENT, 1)
                logger.debug("Set Don't Fragment flag (Windows)")
            elif platform.system() == "Darwin":  # macOS
                sock.setsockopt(socket.IPPROTO_IP, socket.IP_DONTFRAG, 1)
                logger.debug("Set Don't Fragment flag (macOS)")
            else:
                logger.warning(f"Don't Fragment not supported on {platform.system()}")
        except Exception as e:
            logger.warning(f"Failed to set Don't Fragment flag: {e}")

    def _configure_ttl(self, sock: socket.socket) -> None:
        """Configure TTL if specified."""
        if self.ttl:
            try:
                sock.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, self.ttl)
                logger.debug(f"Set TTL to {self.ttl}")
            except Exception as e:
                logger.warning(f"Failed to set TTL: {e}")

    def _configure_tos(self, sock: socket.socket) -> None:
        """Configure TOS if specified."""
        if self.tos:
            try:
                sock.setsockopt(socket.IPPROTO_IP, socket.IP_TOS, self.tos)
                logger.debug(f"Set TOS to {self.tos}")
            except Exception as e:
                logger.warning(f"Failed to set TOS: {e}")
