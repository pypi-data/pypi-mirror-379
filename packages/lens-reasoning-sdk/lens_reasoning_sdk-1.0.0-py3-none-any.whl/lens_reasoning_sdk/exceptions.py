"""
Custom exceptions for the Lens Reasoning SDK
"""

class LensError(Exception):
    """Base exception for all Lens SDK errors"""
    pass

class ContractNotFoundError(LensError):
    """Raised when a reasoning contract cannot be found"""
    pass

class ProcessingError(LensError):
    """Raised when query processing fails"""
    pass

class SteeringError(LensError):
    """Raised when steering directive operations fail"""
    pass

class ConfigurationError(LensError):
    """Raised when there are configuration issues"""
    pass