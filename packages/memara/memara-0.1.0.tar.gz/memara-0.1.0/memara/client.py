"""
Memara Python SDK Client

Main client class for interacting with the Memara API.
"""

import os
from typing import Any, Dict, List, Optional
from urllib.parse import urljoin

import httpx

from .exceptions import (
    MemaraAPIError,
    MemaraAuthError,
    MemaraError,
    MemaraNotFoundError,
    MemaraRateLimitError,
    MemaraServerError,
    MemaraValidationError,
)
from .models import CreateMemoryRequest, CreateSpaceRequest, Memory, Space


class Memara:
    """
    Main Memara SDK client.

    Provides access to Memara API functionality.
    Supports both space-scoped (bare API) and user-scoped API keys.
    
    Space-scoped keys (starting with 'sk_bare_api_') are automatically detected
    and space_id parameters are ignored since the key is already scoped.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ):
        """Initialize the Memara client.

        Args:
            api_key: Your Memara API key (or set MEMARA_API_KEY env var)
            base_url: API base URL (or set MEMARA_API_URL env var)
            timeout: Request timeout in seconds (default: 30.0)

        Raises:
            MemaraAuthError: If no API key is provided
        """
        self.api_key = api_key or os.getenv("MEMARA_API_KEY")
        if not self.api_key:
            raise MemaraAuthError(
                "API key required. Set MEMARA_API_KEY env var or pass api_key parameter."
            )

        # Default to production API, fallback to local for development
        default_url = os.getenv("MEMARA_API_URL", "https://api.memara.io")
        self.base_url = (base_url or default_url).rstrip("/")
        self.timeout = timeout

        # Initialize HTTP client
        self._client = httpx.Client(timeout=timeout)

        # Set up headers
        self._headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
            "User-Agent": "memara-python-sdk/0.1.0",
        }
        
        # Detect if this is a space-scoped API key (bare API integration)
        self._is_space_scoped = self._detect_space_scoped_api()

    def _request(
        self,
        method: str,
        path: str,
        json: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make HTTP request to Memara API with error handling."""
        url = urljoin(self.base_url + "/", path.lstrip("/"))

        try:
            response = self._client.request(
                method=method, url=url, json=json, params=params, headers=self._headers
            )

            # Handle error status codes
            if response.status_code == 401:
                raise MemaraAuthError("Invalid API key")
            elif response.status_code == 404:
                raise MemaraNotFoundError("Resource", "requested")
            elif response.status_code == 422:
                raise MemaraValidationError("Validation failed")
            elif response.status_code == 429:
                raise MemaraRateLimitError()
            elif response.status_code >= 500:
                raise MemaraServerError()
            elif not response.is_success:
                raise MemaraAPIError(
                    f"API error: {response.status_code}", response.status_code
                )

            return response.json() if response.content else {}

        except httpx.RequestError as e:
            raise MemaraError(f"Request failed: {str(e)}")
    
    def _detect_space_scoped_api(self) -> bool:
        """
        Detect if the API key is space-scoped (bare API integration).
        Space-scoped keys start with 'sk_bare_api_' and have socket-access URLs.
        """
        return (
            self.api_key.startswith('sk_bare_api_') or 
            'socket-access' in self.base_url
        )

    # Memory operations
    def create_memory(
        self,
        content: str,
        tags: Optional[List[str]] = None,
        source: str = "sdk",
        importance: int = 5,
        space_id: Optional[str] = None,
    ) -> Memory:
        """
        Create a new memory.
        
        For space-scoped API keys (bare API), space_id is ignored as the key 
        is already scoped to a specific space.
        """
        data = {
            "content": content,
            "tags": tags or [],
            "source": source,
            "importance": importance,
        }

        # For space-scoped APIs, don't send space_id (it's implicit)
        params = {}
        if not self._is_space_scoped and space_id:
            params["space_id"] = space_id
            
        response = self._request("POST", "/memories", json=data, params=params)
        return Memory(**response)

    def get_memory(self, memory_id: str, space_id: Optional[str] = None) -> Memory:
        """
        Get a memory by ID.
        
        For space-scoped API keys (bare API), space_id is ignored as the key 
        is already scoped to a specific space.
        """
        # For space-scoped APIs, don't send space_id (it's implicit)
        params = {}
        if not self._is_space_scoped and space_id:
            params["space_id"] = space_id
            
        response = self._request("GET", f"/memories/{memory_id}", params=params)
        return Memory(**response)

    def search_memories(
        self,
        query: str,
        limit: int = 10,
        space_id: Optional[str] = None,
        cross_space: bool = False,
    ) -> List[Memory]:
        """
        Search memories by query.
        
        For space-scoped API keys (bare API), space_id and cross_space are ignored 
        as the key is already scoped to a specific space.
        """
        data = {"query": query, "limit": limit}
        params = {}
        
        # For space-scoped APIs, don't send space_id or cross_space (search is implicit to the scoped space)
        if not self._is_space_scoped:
            if space_id:
                params["space_id"] = space_id
            if cross_space:
                params["cross_space"] = "true"

        response = self._request("POST", "/memories/search", json=data, params=params)
        return [Memory(**item) for item in response]

    def delete_memory(
        self, memory_id: str, space_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Delete a memory.
        
        For space-scoped API keys (bare API), space_id is ignored as the key 
        is already scoped to a specific space.
        """
        # For space-scoped APIs, don't send space_id (it's implicit)
        params = {}
        if not self._is_space_scoped and space_id:
            params["space_id"] = space_id
            
        return self._request("DELETE", f"/memories/{memory_id}", params=params)

    # Space operations
    def list_spaces(self) -> List[Space]:
        """List all user spaces."""
        response = self._request("GET", "/spaces")
        spaces_data = (
            response if isinstance(response, list) else response.get("spaces", [])
        )
        return [Space(**space) for space in spaces_data]

    def create_space(
        self,
        name: str,
        icon: str = "📁",
        color: str = "#6366F1",
        template_type: str = "custom",
    ) -> Space:
        """Create a new space."""
        data = {
            "name": name,
            "icon": icon,
            "color": color,
            "template_type": template_type,
        }
        response = self._request("POST", "/spaces", json=data)
        return Space(**response)

    def close(self):
        """Close HTTP client."""
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
