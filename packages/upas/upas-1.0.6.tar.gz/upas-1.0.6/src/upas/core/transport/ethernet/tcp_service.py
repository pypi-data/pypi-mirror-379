"""
UPAS TCP Services

TCP server and client service implementations.
"""

import asyncio
import logging
from typing import Dict, Any

from ..utils import parse_address


logger = logging.getLogger(__name__)


class TCPServerService:
    """TCP server service implementation."""

    def __init__(self, name: str, config: Dict[str, Any]):
        """
        Initialize TCP server service.

        :param name: Service name
        :type name: str
        :param config: Service configuration
        :type config: dict
        """
        self.name = name
        self.config = config
        self.server = None
        self.running = False
        self.packet_callbacks = []

    async def start(self) -> None:
        """Start TCP server."""
        bind_addr = self.config.get("bind", "0.0.0.0:0")
        host, port = parse_address(bind_addr)

        self.server = await asyncio.start_server(self._handle_connection, host, port)

        self.running = True
        logger.debug(f"Started TCP server '{self.name}' on {host}:{port}")

    async def stop(self) -> None:
        """Stop TCP server."""
        self.running = False
        if self.server:
            self.server.close()
            await self.server.wait_closed()
            self.server = None

    def add_packet_callback(self, callback) -> None:
        """Add callback for received packets."""
        self.packet_callbacks.append(callback)

    async def _handle_connection(
        self,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
    ) -> None:
        """
        Handle incoming TCP connection.

        :param reader: Stream reader
        :type reader: asyncio.StreamReader
        :param writer: Stream writer
        :type writer: asyncio.StreamWriter
        """
        addr = writer.get_extra_info("peername")
        source = f"{addr[0]}:{addr[1]}"

        logger.debug(f"TCP connection from {source}")

        try:
            while self.running:
                data = await reader.read(4096)
                if not data:
                    break

                # Notify all callbacks
                for callback in self.packet_callbacks:
                    try:
                        await callback(data, source)
                    except Exception as e:
                        logger.error(f"Error in packet callback: {e}")

        except asyncio.CancelledError:
            pass
        except Exception as e:
            logger.error(f"Error in TCP connection: {e}")
        finally:
            writer.close()
            await writer.wait_closed()


class TCPClientService:
    """TCP client service implementation with persistent connections."""

    def __init__(self, name: str, config: Dict[str, Any]):
        """
        Initialize TCP client service.

        :param name: Service name
        :type name: str
        :param config: Service configuration
        :type config: dict
        """
        self.name = name
        self.config = config
        self.connections = {}  # connection_key -> connection_info
        self.connection_locks = {}  # connection_key -> asyncio.Lock
        self.running = False
        self.packet_callbacks = []

    async def start(self) -> None:
        """Start TCP client service."""
        self.running = True
        logger.debug(f"Started TCP client service '{self.name}'")

    async def stop(self) -> None:
        """Stop TCP client service and close all connections."""
        self.running = False

        # Close all active connections
        for conn_key, conn_info in list(self.connections.items()):
            if (
                isinstance(conn_info, dict)
                and conn_info.get("type") == "tcp_client_persistent"
            ):
                try:
                    # Cancel response task if exists
                    task = conn_info.get("response_task")
                    if task and not task.done():
                        task.cancel()
                        try:
                            await task
                        except asyncio.CancelledError:
                            pass

                    # Close writer
                    writer = conn_info.get("writer")
                    if writer:
                        writer.close()
                        await writer.wait_closed()
                        logger.debug(f"Closed persistent TCP connection: {conn_key}")

                except Exception as e:
                    logger.error(f"Error closing connection {conn_key}: {e}")

        self.connections.clear()
        self.connection_locks.clear()

    def add_packet_callback(self, callback) -> None:
        """Add callback for received packets."""
        self.packet_callbacks.append(callback)

    async def send_packet(self, destination: str, payload: bytes) -> None:
        """
        Send packet via TCP client with persistent connections.

        :param destination: Destination address
        :type destination: str
        :param payload: Packet payload
        :type payload: bytes
        """
        host, port = parse_address(destination)
        timeout = self.config.get("connect_timeout", 10)

        logger.debug(f"Using TCP client service '{self.name}' to send to {host}:{port}")

        connection_key = f"{self.name}_{host}_{port}"
        # Ensure a per-connection lock exists
        lock = self.connection_locks.setdefault(connection_key, asyncio.Lock())

        # Use the lock to avoid concurrent connect attempts for same service/host:port
        async with lock:
            try:
                # Check if we have an existing persistent connection
                existing = self.connections.get(connection_key)
                if (
                    isinstance(existing, dict)
                    and existing.get("type") == "tcp_client_persistent"
                ):
                    writer = existing.get("writer")
                    if writer and not writer.is_closing():
                        try:
                            writer.write(payload)
                            await writer.drain()
                            logger.debug(
                                f"Sent packet via persistent connection to {host}:{port}"
                            )
                            return
                        except Exception as e:
                            logger.warning(
                                f"Persistent connection failed, creating new one: {e}"
                            )
                            # Clean up the failed connection
                            await self._cleanup_connection(connection_key)

                # No usable connection -> create new persistent one
                logger.debug(f"Creating new persistent TCP connection to {host}:{port}")

                reader, writer = await asyncio.wait_for(
                    asyncio.open_connection(host, port), timeout=timeout
                )

                # Send the packet
                writer.write(payload)
                await writer.drain()

                # Store the persistent connection with response handler
                source = f"{host}:{port}"
                response_task = asyncio.create_task(
                    self._handle_responses(reader, writer, source, connection_key)
                )

                self.connections[connection_key] = {
                    "type": "tcp_client_persistent",
                    "reader": reader,
                    "writer": writer,
                    "response_task": response_task,
                    "created": asyncio.get_event_loop().time(),
                }

                logger.debug(
                    f"Sent packet via new persistent TCP connection to {host}:{port}"
                )

            except asyncio.TimeoutError:
                logger.error(f"TCP connection timeout to {host}:{port}")
                raise
            except Exception as e:
                logger.error(f"Error in TCP client send: {e}")
                raise

    async def _handle_responses(
        self,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
        source: str,
        connection_key: str,
    ) -> None:
        """
        Handle incoming responses from TCP client connection.
        This version maintains persistent connections.

        :param reader: Stream reader
        :type reader: asyncio.StreamReader
        :param writer: Stream writer
        :type writer: asyncio.StreamWriter
        :param source: Source address for packet callbacks
        :type source: str
        :param connection_key: Connection key for tracking
        :type connection_key: str
        """
        try:
            logger.debug(f"TCP client response handler started for {source}")

            while self.running:
                data = await reader.read(4096)
                if not data:
                    # Connection closed by remote, mark for cleanup
                    logger.debug(f"TCP connection closed by remote: {source}")
                    break

                # Notify all callbacks about received data
                for callback in self.packet_callbacks:
                    try:
                        await callback(data, source)
                    except Exception as e:
                        logger.error(f"Error in packet callback: {e}")

        except asyncio.CancelledError:
            logger.debug(f"TCP client response handler cancelled for {source}")
        except Exception as e:
            logger.error(f"Error in TCP client response handler for {source}: {e}")
        finally:
            # Clean up connection only if it's really closed or on error
            await self._cleanup_connection(connection_key)

    async def _cleanup_connection(self, connection_key: str) -> None:
        """
        Clean up a failed TCP client connection.

        :param connection_key: Connection key to clean up
        :type connection_key: str
        """
        conn_info = self.connections.get(connection_key)
        if not conn_info:
            return

        try:
            # Cancel response task if exists
            task = conn_info.get("response_task")
            if task and not task.done():
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass

            # Close writer
            writer = conn_info.get("writer")
            if writer:
                if not writer.is_closing():
                    writer.close()
                await writer.wait_closed()

        except Exception as e:
            logger.debug(f"Error cleaning up TCP connection {connection_key}: {e}")
        finally:
            # Remove from connections dict
            self.connections.pop(connection_key, None)

    async def get_last_connection_drain_status(self) -> bool:
        """
        Check drain status of the most recently used TCP connection.

        Returns True if the last connection is properly drained (data sent).
        This is used by multi-packet response strategies to ensure proper timing.
        """
        try:
            # Get the most recently used connection
            if not self.connections:
                return True  # No connections, consider drained

            # Find the most recent persistent connection
            latest_conn_info = None
            for conn_info in self.connections.values():
                if (
                    isinstance(conn_info, dict)
                    and conn_info.get("type") == "tcp_client_persistent"
                ):
                    latest_conn_info = conn_info
                    break  # Take first persistent connection found

            if not latest_conn_info:
                return True  # No persistent connections

            writer = latest_conn_info.get("writer")
            if not writer or writer.is_closing():
                return True  # Connection closed, consider drained

            # Perform drain operation to ensure data is sent
            # This will wait until the TCP stack confirms transmission
            await writer.drain()
            logger.debug("TCP connection drain completed successfully")
            return True

        except Exception as e:
            logger.debug(f"Error checking TCP drain status: {e}")
            return False
