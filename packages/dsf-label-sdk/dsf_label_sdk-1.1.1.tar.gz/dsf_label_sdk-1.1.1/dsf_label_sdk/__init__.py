# dsf_label_sdk/__init__.py
"""
DSF Label SDK - Adaptive Formula Evaluation Client
==================================================
Professional SDK for interacting with the DSF Label API.

Basic Usage:
    from dsf_label_sdk import LabelSDK
    
    sdk = LabelSDK()  # Community tier
    result = sdk.evaluate(data={'field1': 5}, config={...})
    
Advanced Usage:
    sdk = LabelSDK(license_key='PRO-2026-12-31-XXXX', tier='professional')
    results = sdk.batch_evaluate([...])
"""

__version__ = '1.1.1'
__author__ = 'Jaime Alexander Jimenez'
__email__ = 'contacto@softwarefinanzas.com.co'

from .client import LabelSDK
from .exceptions import (
    LabelSDKError,
    ValidationError, 
    LicenseError,
    APIError
)
from .models import Field, Config, EvaluationResult

__all__ = [
    'LabelSDK',
    'Field',
    'Config',
    'EvaluationResult',
    'LabelSDKError',
    'ValidationError',
    'LicenseError',
    'APIError'
]