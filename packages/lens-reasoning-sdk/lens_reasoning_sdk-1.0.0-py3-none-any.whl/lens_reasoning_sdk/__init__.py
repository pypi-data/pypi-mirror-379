"""
Lens Reasoning SDK

A Python SDK for the Lens Reasoning System focused on query processing and reasoning.
For steering directives management, use the Lens UI overlay (Ctrl/Cmd + Shift + L).
"""

from .query_processor import LensQueryProcessor
from .exceptions import LensError, ContractNotFoundError, ProcessingError

__version__ = "1.0.0"
__all__ = [
    "LensQueryProcessor",   # Focused SDK for query processing
    "LensError",
    "ContractNotFoundError",
    "ProcessingError"
]