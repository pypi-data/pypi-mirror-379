"""
AgentMind API Client - handles communication with hosted service
"""
import os
import time
import requests
from typing import Optional, Dict, Any, List
from urllib.parse import urljoin
from datetime import datetime


class APIClient:
    """Internal API client for AgentMind hosted service"""
    
    def __init__(self, api_key: str, base_url: Optional[str] = None):
        self.api_key = api_key
        self.base_url = (base_url or "https://api.agent-mind.com").rstrip('/')
        self.api_version = "v1"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "agentmind-python/0.2.0"
        })
        
        # Track usage for client-side rate limiting
        self._last_request_time = 0
        self._request_count = 0
    
    def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None
    ) -> Any:
        """Make API request with retries and error handling"""
        
        # Simple client-side rate limiting
        current_time = time.time()
        if current_time - self._last_request_time < 0.1:  # Max 10 req/sec
            time.sleep(0.1 - (current_time - self._last_request_time))
        
        # Build full URL
        url = f"{self.base_url}/api/{self.api_version}/{endpoint}"
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                json=data,
                params=params,
                timeout=30
            )
            
            # Track for rate limiting
            self._last_request_time = time.time()
            self._request_count += 1
            
            # Handle errors
            if response.status_code == 401:
                raise AuthenticationError("Invalid API key")
            elif response.status_code == 429:
                raise RateLimitError("Rate limit exceeded")
            elif response.status_code == 402:
                raise PaymentRequiredError("Payment required - upgrade your plan")
            elif response.status_code >= 500:
                raise ServerError(f"Server error: {response.status_code}")
            
            response.raise_for_status()
            
            # Return JSON if available, otherwise raw text
            try:
                return response.json()
            except:
                return response.text
            
        except requests.exceptions.Timeout:
            raise TimeoutError("Request timed out")
        except requests.exceptions.ConnectionError:
            raise ConnectionError("Could not connect to AgentMind API")
    
    def remember(
        self,
        content: Any,
        user_id: Optional[str] = None,
        session_id: Optional[str] = None,
        memory_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        ttl: Optional[int] = None
    ) -> str:
        """Store a memory via API"""
        data = {
            "content": content,
            "user_id": user_id,
            "session_id": session_id,
            "id": memory_id,
            "metadata": metadata,
            "ttl": ttl
        }
        # Remove None values
        data = {k: v for k, v in data.items() if v is not None}
        
        response = self._make_request("POST", "memories/remember", data=data)
        return response["memory_id"]
    
    def recall(
        self,
        query: str,
        strategy: str = "llm",  # Default to intelligent LLM recall
        limit: int = 5,
        user_id: Optional[str] = None,
        session_id: Optional[str] = None,
        filters: Optional[Dict[str, Any]] = None
    ) -> List[Any]:
        """Recall memories via API"""
        data = {
            "query": query,
            "strategy": strategy,
            "limit": limit,
            "user_id": user_id,
            "session_id": session_id,
            "filters": filters
        }
        # Remove None values
        data = {k: v for k, v in data.items() if v is not None}
        
        return self._make_request("POST", "memories/recall", data=data)
    
    def get(self, memory_id: str, include_metadata: bool = False) -> Any:
        """Get a specific memory by ID"""
        params = {"include_metadata": include_metadata} if include_metadata else {}
        return self._make_request("GET", f"memories/get/{memory_id}", params=params)
    
    def exists(self, memory_id: str) -> bool:
        """Check if a memory exists"""
        return self._make_request("GET", f"memories/exists/{memory_id}")
    
    def delete(self, memory_id: str) -> bool:
        """Delete a memory"""
        response = self._make_request("DELETE", f"memories/delete/{memory_id}")
        return response.get("deleted", False)

    def update(self, memory_id: str, updates: Dict[str, Any]) -> bool:
        """Update a memory's content and metadata"""
        response = self._make_request("PUT", f"memories/update/{memory_id}", data=updates)
        return response.get("updated", False)
    
    def list_memories(
        self,
        include_data: bool = False,
        limit: int = 100,
        offset: int = 0,
        **filters
    ) -> List[Dict[str, Any]]:
        """List memories with filters"""
        params = {
            "include_data": include_data,
            "limit": limit,
            "offset": offset,
            **filters
        }
        response = self._make_request("GET", "memories/list", params=params)
        
        # If response is a dict with 'items' key, return just the items
        if isinstance(response, dict) and 'items' in response:
            return response['items']
        
        # Otherwise return as-is (for backward compatibility)
        return response
    
    def forget(
        self,
        query: str,
        user_id: Optional[str] = None,
        confirm_all: bool = False,
        limit: int = 10
    ) -> Dict[str, Any]:
        """
        Intelligently forget memories matching a query.

        Args:
            query: Search query to find memories to delete
            user_id: Optional user filter
            confirm_all: If True, delete all matches; if False, delete best match only
            limit: Maximum number of memories to delete

        Returns:
            Dict with success status, deleted count, and deleted memories
        """
        data = {
            "query": query,
            "user_id": user_id,
            "confirm_all": confirm_all,
            "limit": limit
        }
        # Remove None values
        data = {k: v for k, v in data.items() if v is not None}

        return self._make_request("POST", "memories/forget", data=data)

    def forget_before(self, date: Any, user_id: Optional[str] = None) -> int:
        """Delete memories before a certain date"""
        if isinstance(date, datetime):
            date = date.isoformat()

        data = {
            "date": date,
            "user_id": user_id
        }
        data = {k: v for k, v in data.items() if v is not None}

        response = self._make_request("POST", "memories/forget_before", data=data)
        return response["deleted_count"]
    
    def clear_session(self, session_id: str) -> int:
        """Clear all memories from a session"""
        response = self._make_request("DELETE", f"memories/clear_session/{session_id}")
        return response["deleted_count"]
    
    def summarize_session(self, session_id: str) -> str:
        """Get or create a session summary"""
        return self._make_request("POST", f"memories/summarize_session/{session_id}")
    
    def export_user_data(self, user_id: str) -> Dict[str, Any]:
        """Export all user data (GDPR compliance)"""
        return self._make_request("GET", f"memories/export_user/{user_id}")
    
    def delete_user_data(self, user_id: str) -> int:
        """Delete all user data (GDPR right to erasure)"""
        response = self._make_request("DELETE", f"memories/delete_user/{user_id}")
        return response["deleted_count"]
    
    def health_check(self) -> bool:
        """Check if API is healthy"""
        try:
            response = self._make_request("GET", "health")
            return response.get("status") == "healthy"
        except:
            return False


# Custom exceptions
class AgentMindError(Exception):
    """Base exception for AgentMind"""
    pass

class AuthenticationError(AgentMindError):
    """Invalid API key"""
    pass

class RateLimitError(AgentMindError):
    """Rate limit exceeded"""
    pass

class PaymentRequiredError(AgentMindError):
    """Payment required - need to upgrade plan"""
    pass

class ServerError(AgentMindError):
    """Server-side error"""
    pass