"""PyGitGuardian API Client"""

from .client import ContentTooLarge, GGClient, GGClientCallbacks


__version__ = "1.19.0"
GGClient._version = __version__

__all__ = ["GGClient", "GGClientCallbacks", "ContentTooLarge"]
