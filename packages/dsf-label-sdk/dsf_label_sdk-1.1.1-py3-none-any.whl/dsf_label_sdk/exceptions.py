# dsf_label_sdk/exceptions.py
"""Custom exceptions for the SDK"""


class LabelSDKError(Exception):
    """Base exception for SDK errors."""
    pass


class ValidationError(LabelSDKError):
    """Raised when input validation fails."""
    pass


class LicenseError(LabelSDKError):
    """Raised when license validation fails."""
    pass


class APIError(LabelSDKError):
    """Raised when API request fails."""
    
    def __init__(self, message: str, status_code: Optional[int] = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code