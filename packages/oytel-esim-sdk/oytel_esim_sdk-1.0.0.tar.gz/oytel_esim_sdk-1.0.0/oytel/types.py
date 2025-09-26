"""
Type definitions for the Oytel eSIM API
"""

from typing import Dict, List, Optional, Any, TypedDict


class Plan(TypedDict):
    """eSIM plan information."""
    id: str
    name: str
    description: str
    coverage: str
    data_allowance: str
    validity_days: int
    pricing: Dict[str, Any]
    features: List[str]
    popular: bool
    available: bool
    environment: str


class PlansResponse(TypedDict):
    """Response from the plans endpoint."""
    plans: List[Plan]
    meta: Dict[str, Any]


class ProvisionRequest(TypedDict, total=False):
    """Request data for eSIM provisioning."""
    plan_id: str
    customer_email: str
    customer_name: str
    reference_id: Optional[str]
    webhook_url: Optional[str]


class ESIMInfo(TypedDict):
    """eSIM information."""
    esim_id: str
    iccid: str
    qr_code_url: str
    activation_code: str
    status: str
    expires_at: str
    plan: Dict[str, Any]
    network_info: Dict[str, Any]
    activation_instructions: Dict[str, List[str]]


class ProvisionResponse(TypedDict):
    """Response from eSIM provisioning."""
    success: bool
    order_id: str
    esim: ESIMInfo
    billing: Dict[str, Any]
    meta: Dict[str, Any]


class ESIMStatus(TypedDict, total=False):
    """eSIM status information."""
    esim_id: str
    iccid: str
    status: str
    plan: Dict[str, Any]
    activation: Dict[str, Any]
    usage: Optional[Dict[str, Any]]
    connection: Optional[Dict[str, Any]]
    analytics: Optional[Dict[str, Any]]


class StatusResponse(TypedDict):
    """Response from eSIM status endpoint."""
    success: bool
    esim: ESIMStatus
    meta: Dict[str, Any]
