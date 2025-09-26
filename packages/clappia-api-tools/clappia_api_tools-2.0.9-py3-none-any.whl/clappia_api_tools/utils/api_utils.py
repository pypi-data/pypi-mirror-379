import json
from typing import Any

import requests

from clappia_api_tools.utils.logging_utils import get_logger

logger = get_logger(__name__)


class ClappiaAPIUtils:
    """Abstract base API utilities with common functionality for all Clappia API interactions"""

    def __init__(
        self,
        base_url: str,
        timeout: int = 30,
    ):
        """
        Initialize API utilities with configurable parameters

        Args:
            base_url: API base URL
            timeout: Request timeout in seconds
        """
        self.base_url = base_url
        self.timeout = timeout

    def validate_environment(self) -> tuple[bool, str]:
        """Validate that required configuration is available"""
        if not self.base_url:
            return (
                False,
                "Base URL is not configured",
            )
        return True, ""

    def get_headers(
        self,
        data: Any | None = None,
        params: dict[str, Any] | None = None,
    ) -> dict[str, str]:
        """Get standard headers for API requests"""
        return {"Content-Type": "application/json"}

    def handle_response(
        self, response: requests.Response
    ) -> tuple[bool, str | None, dict[str, Any] | None]:
        """
        Handle API response and return structured result

        Returns:
            Tuple of (success: bool, error_message: str, data: dict)
        """
        if response.status_code == 200:
            try:
                return True, None, response.json()
            except json.JSONDecodeError:
                logger.warning(f"Valid response but invalid JSON: {response.text}")
                return True, None, {"raw_response": response.text}

        error_message = self._format_error_message(response)
        return False, error_message, None

    def _format_error_message(self, response: requests.Response) -> str:
        """Format error message from API response"""
        if response.status_code in [400, 401, 403, 404]:
            try:
                error_data = response.json()
                return f"API Error ({response.status_code}): {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"API Error ({response.status_code}): {response.text}"
        else:
            return f"Unexpected API response ({response.status_code}): {response.text}"

    def make_request(
        self,
        method: str,
        endpoint: str,
        data: Any | None = None,
        params: dict[str, Any] | None = None,
    ) -> tuple[bool, str | None, Any | None]:
        """
        Make HTTP request to Clappia API

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint (will be appended to base_url)
            data: Request body data (for POST/PUT requests)
            params: Query parameters (for GET requests)

        Returns:
            Tuple of (success: bool, error_message: str, response_data: dict)
        """
        env_valid, env_error = self.validate_environment()
        if not env_valid:
            return False, f"Configuration error: {env_error}", None

        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        headers = self.get_headers(data, params)
        try:
            logger.info(
                f"Making {method} request to {url}, headers: {headers}, data: {data}, params: {params}"
            )
            if data:
                logger.debug(f"Request data: {json.dumps(data, indent=2)}")

            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                json=data,
                params=params,
                timeout=self.timeout,
            )

            logger.info(f"Response status: {response.status_code}")
            logger.debug(f"Response body: {response.text}")

            return self.handle_response(response)

        except requests.exceptions.Timeout:
            return False, f"Request timeout after {self.timeout} seconds", None
        except requests.exceptions.ConnectionError:
            return False, "Connection error - unable to reach Clappia API", None
        except Exception as e:
            return False, f"Unexpected error: {e!s}", None


class ClappiaAPIKeyUtils(ClappiaAPIUtils):
    """API utilities for Clappia API key authentication"""

    def __init__(
        self,
        api_key: str,
        base_url: str,
        timeout: int = 30,
    ):
        """
        Initialize API utilities with configurable parameters

        Args:
            api_key: Clappia API key
            base_url: API base URL
            timeout: Request timeout in seconds
        """
        super().__init__(base_url, timeout)
        self.api_key = api_key

    def validate_environment(self) -> tuple[bool, str]:
        """Validate that required configuration is available"""
        if not self.api_key:
            return (
                False,
                "API key is not configured",
            )
        return super().validate_environment()

    def get_headers(
        self,
        data: Any | None = None,
        params: dict[str, Any] | None = None,
    ) -> dict[str, str]:
        """Get standard headers for API requests"""
        headers = super().get_headers(data, params)
        headers["x-api-key"] = self.api_key
        return headers


class ClappiaAuthTokenUtils(ClappiaAPIUtils):
    """API utilities for Clappia auth token authentication with workplace ID support"""

    def __init__(
        self,
        auth_token: str,
        workplace_id: str,
        base_url: str,
        timeout: int = 30,
    ):
        """
        Initialize API utilities with auth token and workplace ID

        Args:
            auth_token: Clappia Auth token
            workplace_id: Clappia Workplace ID
            base_url: API base URL
            timeout: Request timeout in seconds
        """
        super().__init__(base_url, timeout)
        self.auth_token = auth_token
        self.workplace_id = workplace_id

    def validate_environment(self) -> tuple[bool, str]:
        """Validate that required configuration is available"""
        if not self.auth_token:
            return (
                False,
                "Auth token is not configured",
            )
        if not self.workplace_id:
            return (
                False,
                "Workplace ID is not configured",
            )
        return super().validate_environment()

    def get_headers(
        self,
        data: Any | None = None,
        params: dict[str, Any] | None = None,
    ) -> dict[str, str]:
        """Get standard headers for API requests with auth token and optional app_id"""
        headers = super().get_headers(data, params)
        headers["Authorization"] = self.auth_token
        headers["workplaceId"] = self.workplace_id

        # Add appId header if present in request data or params
        if params and "appId" in params:
            headers["appId"] = params["appId"]
        elif data and "appId" in data:
            headers["appId"] = data["appId"]

        return headers
