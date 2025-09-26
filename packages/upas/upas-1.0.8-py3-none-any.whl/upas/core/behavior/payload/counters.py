"""
UPAS Counter Management System

Handles counters for payload construction with automatic increment.
"""

import logging
from typing import Dict


class CounterManager:
    """Manages counters for payload construction."""

    def __init__(self):
        """Initialize counter manager."""
        self._counters: Dict[str, int] = {}
        self.logger = logging.getLogger(__name__)

    def get_counter(self, counter_name: str, function: str = None) -> int:
        """
        Get counter value, optionally applying function.

        :param counter_name: Counter name
        :type counter_name: str
        :param function: Function to apply (e.g., 'increment')
        :type function: str
        :return: Counter value
        :rtype: int
        """
        counter_key = f"{counter_name}_{function}" if function else counter_name

        if counter_key not in self._counters:
            self._counters[counter_key] = 0

        if function == "increment":
            self._counters[counter_key] = (self._counters[counter_key] + 1) % 0xFFFFFFFF

        return self._counters[counter_key]

    def set_counter(self, counter_name: str, value: int, function: str = None) -> None:
        """
        Set counter value.

        :param counter_name: Counter name
        :type counter_name: str
        :param value: Counter value
        :type value: int
        :param function: Function suffix
        :type function: str
        """
        counter_key = f"{counter_name}_{function}" if function else counter_name
        self._counters[counter_key] = value

    def reset_counter(self, counter_name: str, function: str = None) -> None:
        """
        Reset counter to zero.

        :param counter_name: Counter name
        :type counter_name: str
        :param function: Function suffix
        :type function: str
        """
        counter_key = f"{counter_name}_{function}" if function else counter_name
        self._counters[counter_key] = 0

    def reset_all_counters(self) -> None:
        """Reset all counters to zero."""
        self._counters.clear()
