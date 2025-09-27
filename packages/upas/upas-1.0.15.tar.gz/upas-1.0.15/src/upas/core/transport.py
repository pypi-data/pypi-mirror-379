"""
UPAS Transport Layer

Backward compatibility layer for the refactored transport module.
"""

# Import all classes from the new modular structure for backward compatibility
from .transport import (
    BaseTransport,
    TransportLayer,
    EthernetTransport,
    RawTransport,
)

# Re-export everything to maintain backward compatibility
__all__ = [
    "BaseTransport",
    "TransportLayer",
    "EthernetTransport",
    "RawTransport",
]
