"""
Payload processing system for UPAS behaviors.

Handles payload building, pattern matching, and variable substitution.
"""

from .builder import PayloadBuilder
from .variables import VariableResolver
from .counters import CounterManager

__all__ = [
    "PayloadBuilder",
    "VariableResolver",
    "CounterManager",
]
