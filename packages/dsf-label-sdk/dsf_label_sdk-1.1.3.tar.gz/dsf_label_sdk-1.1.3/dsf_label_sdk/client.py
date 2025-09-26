# dsf_label_sdk/client.py
"""Main SDK Client"""

import requests
from typing import Dict, List, Optional, Union, Any
from urllib.parse import urljoin
import time
from functools import wraps
import logging

from . import __version__
from .exceptions import ValidationError, LicenseError, APIError
from .models import Field, Config, EvaluationResult

logger = logging.getLogger(__name__)


def retry_on_failure(max_retries: int = 3, delay: float = 1.0):
    """Decorator for automatic retry logic"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (requests.RequestException, APIError) as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        time.sleep(delay * (2 ** attempt))  # Exponential backoff
                        logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    else:
                        logger.error(f"All {max_retries} attempts failed.")
            raise last_exception
        return wrapper
    return decorator


class LabelSDK:
    """
    DSF Label SDK Client
    
    This client provides a pythonic interface to the DSF Label API for
    adaptive formula evaluation with support for multiple tiers.
    
    Attributes:
        BASE_URL: Default API endpoint
        TIERS: Available subscription tiers
    """
    
    BASE_URL = 'https://label-api.vercel.app/api/'
    TIERS = {'community', 'professional', 'enterprise'}
    
    def __init__(
        self,
        license_key: Optional[str] = None,
        tier: str = 'community',
        base_url: Optional[str] = None,
        timeout: int = 30,
        max_retries: int = 3,
        verify_ssl: bool = True
    ):
        """
        Initialize the Label SDK client.
        
        Args:
            license_key: License key for premium tiers
            tier: Subscription tier ('community', 'professional', 'enterprise')
            base_url: Override default API endpoint
            timeout: Request timeout in seconds
            max_retries: Maximum retry attempts for failed requests
            verify_ssl: Whether to verify SSL certificates
            
        Raises:
            ValidationError: If tier is invalid
        """
        if tier not in self.TIERS:
            raise ValidationError(f"Invalid tier. Must be one of: {self.TIERS}")
        
        self.license_key = license_key
        self.tier = tier
        self.base_url = base_url or self.BASE_URL
        self.timeout = timeout
        self.max_retries = max_retries
        self.verify_ssl = verify_ssl
        
        # Configure session for connection pooling
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': f'DSF-Label-SDK-Python/{__version__}'
        })
        
        # Validate license on initialization for premium tiers
        if tier != 'community' and license_key:
            self._validate_license()
    
    def _validate_license(self):
        """Internal method to validate license with API"""
        try:
            response = self._make_request('evaluate', {
                'data': {},
                'config': {},
                'tier': self.tier,
                'license_key': self.license_key
            })
            if not response.get('tier'):
                raise LicenseError("License validation failed")
        except APIError as e:
            if e.status_code == 403:
                raise LicenseError(f"Invalid license: {e.message}")
            raise
    
    @retry_on_failure(max_retries=3)
    def _make_request(self, endpoint: str, data: Dict) -> Dict:
        """
        Make HTTP request to API with retry logic.
        
        Args:
            endpoint: API endpoint
            data: Request payload
            
        Returns:
            Response data as dictionary
            
        Raises:
            APIError: If request fails
        """
        url = urljoin(self.base_url, endpoint)
        
        try:
            response = self.session.post(
                url,
                json=data,
                timeout=self.timeout,
                verify=self.verify_ssl
            )
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 403:
                error_data = response.json()
                raise LicenseError(error_data.get('error', 'License error'))
            elif response.status_code >= 400:
                error_data = response.json()
                raise APIError(
                    error_data.get('error', 'API error'),
                    status_code=response.status_code
                )
                
        except requests.RequestException as e:
            raise APIError(f"Request failed: {str(e)}")
    
    def evaluate(
        self,
        data: Dict[str, Any],
        config: Optional[Union[Dict, Config]] = None,
        custom_confidence: Optional[float] = None
    ) -> EvaluationResult:
        """
        Evaluate single data point against configuration.
        
        Args:
            data: Data dictionary to evaluate
            config: Field configuration (dict or Config object)
            custom_confidence: Override default confidence level (0.0-1.0)
            
        Returns:
            EvaluationResult object with score and metadata
            
        Example:
            >>> result = sdk.evaluate(
            ...     data={'temperature': 25, 'pressure': 1.0},
            ...     config={
            ...         'temperature': {'default': 20, 'weight': 1.0},
            ...         'pressure': {'default': 1.0, 'weight': 0.8}
            ...     }
            ... )
            >>> print(f"Score: {result.score:.2f}")
        """
        # Convert Config object to dict if needed
        if isinstance(config, Config):
            config = config.to_dict()
        
        # Validate inputs
        if not isinstance(data, dict):
            raise ValidationError("Data must be a dictionary")
        
        if config and not isinstance(config, dict):
            raise ValidationError("Config must be a dictionary or Config object")
        
        # Build request
        request_data = {
            'data': data,
            'config': config or {},
            'tier': self.tier
        }
        
        if self.license_key:
            request_data['license_key'] = self.license_key
        
        if custom_confidence is not None:
            if not 0.0 <= custom_confidence <= 1.0:
                raise ValidationError("Confidence must be between 0.0 and 1.0")
            request_data['confidence_level'] = custom_confidence
        
        # Make request
        response = self._make_request('evaluate', request_data)
        
        # Return structured result
        return EvaluationResult.from_response(response)
    
    def batch_evaluate(
        self,
        data_points: List[Dict[str, Any]],
        config: Optional[Union[Dict, Config]] = None,
        parallel: bool = True
    ) -> List[EvaluationResult]:
        """
        Evaluate multiple data points (Premium feature).
        
        Args:
            data_points: List of data dictionaries
            config: Shared configuration for all points
            parallel: Whether to use batch endpoint (faster) or sequential
            
        Returns:
            List of EvaluationResult objects
            
        Raises:
            LicenseError: If tier is community
        """
        if self.tier == 'community':
            raise LicenseError("Batch evaluation requires professional or enterprise tier")
        
        if isinstance(config, Config):
            config = config.to_dict()
        
        if parallel and len(data_points) > 1:
            # Use batch endpoint
            request_data = {
                'data_batch': data_points,
                'config': config or {},
                'tier': self.tier,
                'license_key': self.license_key
            }
            
            response = self._make_request('evaluate', request_data)
            scores = response.get('scores', {})
            
            # Convert to EvaluationResult objects
            results = []
            for i in range(len(data_points)):
                results.append(EvaluationResult(
                    score=scores.get(i, 0.0),
                    tier=response.get('tier', self.tier),
                    confidence_level=response.get('threshold', 0.65),
                    metrics=response.get('metrics')
                ))
            
            return results
        else:
            # Sequential evaluation
            return [
                self.evaluate(data, config)
                for data in data_points
            ]
    
    def create_config(self) -> Config:
        """
        Create a new configuration builder.
        
        Returns:
            Config object for building configurations fluently
            
        Example:
            >>> config = sdk.create_config()
            ...     .add_field('temperature', default=20, weight=1.0)
            ...     .add_field('pressure', default=1.0, weight=0.8)
        """
        return Config()
    
    def get_metrics(self) -> Optional[Dict]:
        """
        Get performance metrics (Premium feature).
        
        Returns:
            Dictionary with metrics or None for community tier
        """
        if self.tier == 'community':
            logger.warning("Metrics not available for community tier")
            return None
        
        response = self._make_request('evaluate', {
            'data': {},
            'config': {},
            'tier': self.tier,
            'license_key': self.license_key,
            'get_metrics': True
        })
        
        return response.get('metrics')
    
    def close(self):
        """Close the session and cleanup resources."""
        self.session.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
    
    def __repr__(self):
        return f"LabelSDK(tier='{self.tier}', url='{self.base_url}')"