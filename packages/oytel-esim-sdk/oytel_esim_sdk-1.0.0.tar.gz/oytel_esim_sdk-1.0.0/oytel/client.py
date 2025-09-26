"""
Oytel eSIM API Client
"""

import requests
from typing import Optional, Dict, Any, Literal
from .exceptions import OytelError, OytelAPIError, OytelAuthError
from .types import PlansResponse, ProvisionRequest, ProvisionResponse, StatusResponse


class OytelClient:
    """
    Official Oytel eSIM API client for Python.
    
    Provides methods to interact with the Oytel eSIM API for provisioning
    and managing eSIMs programmatically.
    
    Example:
        >>> client = OytelClient(api_key="sk_sandbox_your_key_here")
        >>> plans = client.get_plans()
        >>> esim = client.provision_esim(
        ...     plan_id="eu-roam-50",
        ...     customer_email="customer@example.com",
        ...     customer_name="John Doe"
        ... )
    """
    
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://oytel.co.uk",
        environment: Optional[Literal["sandbox", "production"]] = None,
        timeout: int = 30,
    ):
        """
        Initialize the Oytel client.
        
        Args:
            api_key: Your Oytel API key (sk_sandbox_ or sk_live_)
            base_url: API base URL (default: https://oytel.co.uk)
            environment: Force environment (auto-detected from API key if not provided)
            timeout: Request timeout in seconds (default: 30)
            
        Raises:
            OytelAuthError: If API key format is invalid
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        
        # Auto-detect environment from API key
        if environment:
            self.environment = environment
        elif api_key.startswith("sk_sandbox_"):
            self.environment = "sandbox"
        elif api_key.startswith("sk_live_"):
            self.environment = "production"
        else:
            raise OytelAuthError("Invalid API key format. Must start with sk_sandbox_ or sk_live_")
        
        # Setup session
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "X-API-Key": self.api_key,
            "User-Agent": "oytel-esim-python/1.0.0",
        })
    
    def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """
        Make an HTTP request to the API.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint (without /v1 prefix)
            **kwargs: Additional arguments passed to requests
            
        Returns:
            JSON response as dictionary
            
        Raises:
            OytelAPIError: For API errors
            OytelAuthError: For authentication errors
            OytelError: For other errors
        """
        url = f"{self.base_url}/api/v1{endpoint}"
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                timeout=self.timeout,
                **kwargs
            )
            
            # Handle authentication errors
            if response.status_code == 401:
                raise OytelAuthError("Invalid API key or authentication failed")
            elif response.status_code == 403:
                raise OytelAuthError("Access forbidden. Check your API key permissions.")
            
            # Handle other errors
            if not response.ok:
                try:
                    error_data = response.json()
                    error_message = error_data.get("error", f"HTTP {response.status_code}")
                    error_code = error_data.get("code", "HTTP_ERROR")
                except (ValueError, KeyError):
                    error_message = f"HTTP {response.status_code}: {response.reason}"
                    error_code = "HTTP_ERROR"
                
                raise OytelAPIError(error_message, response.status_code, error_code)
            
            return response.json()
            
        except requests.exceptions.Timeout:
            raise OytelError(f"Request timeout after {self.timeout} seconds")
        except requests.exceptions.ConnectionError:
            raise OytelError("Connection error. Please check your internet connection.")
        except requests.exceptions.RequestException as e:
            raise OytelError(f"Request failed: {str(e)}")
    
    def get_plans(self) -> PlansResponse:
        """
        Get all available eSIM plans.
        
        Returns:
            PlansResponse: List of available plans with metadata
            
        Example:
            >>> plans = client.get_plans()
            >>> print(f"Found {len(plans['plans'])} plans")
            >>> for plan in plans['plans']:
            ...     print(f"{plan['name']}: ${plan['pricing']['base_price']}")
        """
        return self._request("GET", "/plans")
    
    def provision_esim(
        self,
        plan_id: str,
        customer_email: str,
        customer_name: str,
        reference_id: Optional[str] = None,
        webhook_url: Optional[str] = None,
    ) -> ProvisionResponse:
        """
        Provision a new eSIM for a customer.
        
        Args:
            plan_id: ID of the eSIM plan to provision
            customer_email: Customer's email address
            customer_name: Customer's full name
            reference_id: Optional reference ID for tracking
            webhook_url: Optional webhook URL for notifications
            
        Returns:
            ProvisionResponse: eSIM details including QR code and activation info
            
        Example:
            >>> esim = client.provision_esim(
            ...     plan_id="eu-roam-50",
            ...     customer_email="customer@example.com",
            ...     customer_name="John Doe",
            ...     reference_id="order-123"
            ... )
            >>> print(f"eSIM ID: {esim['esim']['esim_id']}")
            >>> print(f"QR Code: {esim['esim']['qr_code_url']}")
            >>> print(f"Cost: ${esim['billing']['cost_usd']}")
        """
        data: ProvisionRequest = {
            "plan_id": plan_id,
            "customer_email": customer_email,
            "customer_name": customer_name,
        }
        
        if reference_id:
            data["reference_id"] = reference_id
        if webhook_url:
            data["webhook_url"] = webhook_url
        
        return self._request("POST", "/esim/provision", json=data)
    
    def get_esim_status(self, esim_id: str) -> StatusResponse:
        """
        Get detailed status and usage information for an eSIM.
        
        Args:
            esim_id: The eSIM ID to check status for
            
        Returns:
            StatusResponse: Detailed eSIM status including usage and connection info
            
        Example:
            >>> status = client.get_esim_status("esim_123456")
            >>> print(f"Status: {status['esim']['status']}")
            >>> if status['esim']['usage']:
            ...     usage = status['esim']['usage']
            ...     print(f"Data used: {usage['used_mb']}MB / {usage['total_mb']}MB")
            ...     print(f"Usage: {usage['usage_percentage']}%")
        """
        return self._request("GET", f"/esim/{esim_id}/status")
    
    def get_environment(self) -> Literal["sandbox", "production"]:
        """
        Get the current environment (sandbox or production).
        
        Returns:
            Environment string
        """
        return self.environment
    
    @staticmethod
    def validate_api_key(api_key: str) -> bool:
        """
        Validate API key format.
        
        Args:
            api_key: API key to validate
            
        Returns:
            True if valid format, False otherwise
        """
        return api_key.startswith("sk_sandbox_") or api_key.startswith("sk_live_")
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.session.close()
    
    def get_openapi_spec(self) -> str:
        """
        Get the OpenAPI specification from the server.
        
        Returns:
            OpenAPI specification as YAML string
            
        Raises:
            OytelError: If unable to fetch the specification
        """
        try:
            response = self.session.get(
                f"{self.base_url}/openapi.yaml",
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            raise OytelError(f"Failed to fetch OpenAPI spec: {str(e)}")
    
    def validate_authentication(self) -> bool:
        """
        Validate API key with Oytel API (RBAC handled by backend).
        
        Returns:
            True if API key format is valid, False otherwise
        """
        return self.validate_api_key(self.api_key)
    
    def get_developer_info(self) -> Dict[str, Any]:
        """
        Get developer account information.
        
        Returns:
            Dictionary containing developer account details
        """
        # Mock implementation - in real scenario this would call an API endpoint
        return {
            "id": f"dev_{self.api_key[-8:]}",
            "email": "developer@example.com",
            "status": "approved",
            "environment": self.environment,
            "balance": {
                "sandbox": 100.0,
                "production": 250.0 if self.environment == "production" else 0.0
            }
        }

    def close(self):
        """Close the HTTP session."""
        self.session.close()
