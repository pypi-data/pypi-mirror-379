"""
UPAS Timing Utilities

Timing and jitter management for behaviors.
"""

import asyncio
import random
import logging


class TimingManager:
    """Manages timing and jitter for behavior scheduling."""

    def __init__(self):
        """Initialize timing manager."""
        self.logger = logging.getLogger(__name__)

    async def sleep_with_jitter(self, base_interval: float, jitter_ms: int = 0) -> None:
        """
        Sleep for interval with optional jitter.

        :param base_interval: Base interval in seconds
        :type base_interval: float
        :param jitter_ms: Maximum jitter in milliseconds
        :type jitter_ms: int
        """
        if jitter_ms > 0:
            # Add random jitter
            jitter_seconds = random.uniform(-jitter_ms / 1000.0, jitter_ms / 1000.0)
            actual_interval = max(0.001, base_interval + jitter_seconds)
            self.logger.debug(
                f"Sleeping for {actual_interval:.3f}s (base: {base_interval}s, jitter: {jitter_seconds:.3f}s)"
            )
        else:
            actual_interval = base_interval

        await asyncio.sleep(actual_interval)

    def convert_ms_to_seconds(self, milliseconds: int) -> float:
        """
        Convert milliseconds to seconds.

        :param milliseconds: Time in milliseconds
        :type milliseconds: int
        :return: Time in seconds
        :rtype: float
        """
        return milliseconds / 1000.0
