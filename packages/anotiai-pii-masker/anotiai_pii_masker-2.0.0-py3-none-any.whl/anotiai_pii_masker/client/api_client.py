"""
RunPod API client for AnotiAI PII detection services.
"""

import json
import time
import logging
from typing import Dict, Any, Optional, Tuple
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .exceptions import (
    APIError, AuthenticationError, NetworkError, 
    ValidationError, RateLimitError, ServerError
)
from .config import ClientConfig

logger = logging.getLogger(__name__)


class RunPodAPIClient:
    """Client for communicating with RunPod serverless endpoints."""
    
    def __init__(self, config: Optional[ClientConfig] = None):
        """Initialize the API client."""
        if config is None:
            config = ClientConfig.from_env()
        
        self.config = config
        self.session = self._create_session()
        
        if not config.is_valid():
            raise ValidationError(
                "API key and endpoint ID are required. "
                "Set ANOTIAI_API_KEY and ANOTIAI_ENDPOINT_ID environment variables "
                "or provide them in the configuration."
            )
    
    def _create_session(self) -> requests.Session:
        """Create a configured requests session with retries."""
        session = requests.Session()
        
        # Configure retry strategy
        retry_strategy = Retry(
            total=self.config.retry_attempts,
            backoff_factor=self.config.retry_delay,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST"]
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        # Set default headers
        session.headers.update({
            "Authorization": f"Bearer {self.config.api_key}",
            "Content-Type": "application/json"
        })
        
        return session
    
    def _make_request(self, action: str, **kwargs) -> Dict[str, Any]:
        """Make a request to the RunPod endpoint."""
        url = f"{self.config.base_url}/{self.config.endpoint_id}/runsync"
        
        payload = {
            "input": {
                "action": action,
                **kwargs
            }
        }
        
        try:
            logger.debug(f"Making request to {url} with action: {action}")
            response = self.session.post(
                url, 
                json=payload, 
                timeout=self.config.timeout
            )
            
            # Handle HTTP errors
            if response.status_code == 401:
                raise AuthenticationError("Invalid API key or unauthorized access")
            elif response.status_code == 429:
                raise RateLimitError("Rate limit exceeded")
            elif response.status_code >= 500:
                raise ServerError(f"Server error: {response.status_code}")
            elif response.status_code >= 400:
                raise APIError(f"Client error: {response.status_code}", response.status_code)
            
            response.raise_for_status()
            
            # Parse response
            result = response.json()
            
            # Check RunPod-specific status
            if result.get("status") == "FAILED":
                error_msg = result.get("error", "Unknown error")
                raise APIError(f"Request failed: {error_msg}")
            
            # Handle queued requests
            if result.get("status") == "IN_QUEUE":
                # For sync requests, this shouldn't happen often
                # but we can add polling logic if needed
                raise APIError("Request is queued. Try again in a moment.")
            
            # Return the output data
            if "output" in result:
                return result["output"]
            else:
                return result
                
        except requests.exceptions.Timeout:
            raise NetworkError(f"Request timeout after {self.config.timeout} seconds")
        except requests.exceptions.ConnectionError:
            raise NetworkError("Connection error. Please check your internet connection.")
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Network error: {str(e)}")
        except json.JSONDecodeError:
            raise APIError("Invalid response format from server")
    
    def health_check(self) -> Dict[str, Any]:
        """Perform a health check on the API endpoint."""
        return self._make_request("health")
    
    def get_model_version(self) -> Dict[str, Any]:
        """Get the model version information."""
        return self._make_request("model_version")
    
    def mask_text(self, text: str, confidence_threshold: float = 0.5) -> Tuple[str, Dict[str, Any]]:
        """
        Mask PII in the provided text.
        
        Args:
            text: The text to process
            confidence_threshold: Minimum confidence threshold for PII detection
            
        Returns:
            Tuple of (masked_text, pii_map)
        """
        if not text or not isinstance(text, str):
            raise ValidationError("Text must be a non-empty string")
        
        if not 0 <= confidence_threshold <= 1:
            raise ValidationError("Confidence threshold must be between 0 and 1")
        
        result = self._make_request(
            "mask",
            text=text,
            confidence_threshold=confidence_threshold
        )
        
        return result["masked_text"], result["pii_map"]
    
    def unmask_text(self, masked_text: str, pii_map: Dict[str, Any]) -> str:
        """
        Unmask PII in the provided text.
        
        Args:
            masked_text: The masked text
            pii_map: The PII mapping dictionary
            
        Returns:
            The unmasked text
        """
        if not masked_text or not isinstance(masked_text, str):
            raise ValidationError("Masked text must be a non-empty string")
        
        if not pii_map or not isinstance(pii_map, dict):
            raise ValidationError("PII map must be a non-empty dictionary")
        
        result = self._make_request(
            "unmask",
            masked_text=masked_text,
            pii_map=pii_map
        )
        
        return result["unmasked_text"]
    
    def detect_pii(self, text: str, confidence_threshold: float = 0.5) -> Dict[str, Any]:
        """
        Detect PII in text without masking.
        
        Args:
            text: The text to analyze
            confidence_threshold: Minimum confidence threshold
            
        Returns:
            Dictionary with detection results
        """
        # This would require adding a new action to the RunPod handler
        # For now, we'll use mask_text and extract the entities
        result = self._make_request(
            "mask",
            text=text,
            confidence_threshold=confidence_threshold
        )
        
        return {
            "entities_found": result["entities_found"],
            "pii_map": result["pii_map"],
            "confidence_threshold": result["confidence_threshold"]
        }
