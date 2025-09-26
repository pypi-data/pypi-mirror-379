"""
Memara Python SDK - Official Python client for the Memara API
"""

__version__ = "0.1.0"

from .client import Memara
from .exceptions import MemaraAPIError, MemaraAuthError, MemaraError
from .models import Memory, Space

__all__ = [
    "Memara",
    "MemaraError",
    "MemaraAPIError",
    "MemaraAuthError",
    "Memory",
    "Space",
]
