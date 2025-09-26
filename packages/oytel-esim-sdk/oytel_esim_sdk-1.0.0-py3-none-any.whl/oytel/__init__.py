"""
Oytel eSIM API SDK for Python

Official Python SDK for the Oytel eSIM API.
Provides easy integration for eSIM provisioning and management.
"""

from .client import OytelClient
from .exceptions import OytelError, OytelAPIError, OytelAuthError
from .types import (
    Plan,
    PlansResponse,
    ProvisionRequest,
    ProvisionResponse,
    ESIMInfo,
    ESIMStatus,
    StatusResponse,
)

__version__ = "1.0.0"
__author__ = "Oytel Mobile"
__email__ = "developers@oytel.co.uk"

__all__ = [
    "OytelClient",
    "OytelError",
    "OytelAPIError", 
    "OytelAuthError",
    "Plan",
    "PlansResponse",
    "ProvisionRequest",
    "ProvisionResponse",
    "ESIMInfo",
    "ESIMStatus",
    "StatusResponse",
]
