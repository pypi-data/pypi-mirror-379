"""
Query Processing SDK for Lens Reasoning System

This SDK provides a focused interface for processing queries and getting reasoning results.
"""

import httpx
from typing import List, Optional, Dict, Any
import sys
import os

# Add the parent directory to sys.path to import from models.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from .exceptions import LensError, ProcessingError
except ImportError:
    from exceptions import LensError, ProcessingError


class LensQueryProcessor:
    """
    Simplified SDK for query processing and reasoning.

    This SDK focuses specifically on processing queries through the Lens reasoning system
    and retrieving results. It provides a clean interface for basic reasoning tasks.

    Example usage:
        processor = LensQueryProcessor("https://api.tupl.xyz")

        # Process a query
        result = processor.process_query("What are the implications of AI in healthcare?")
        print(f"Answer: {result['final_answer']}")
        print(f"Contract ID: {result['contract_id']}")

        # Get detailed contract information
        contract = processor.get_contract(result['contract_id'])
        print(f"Confidence: {contract['confidence_overall']}")
    """

    def __init__(self, base_url: str = "https://api.tupl.xyz", timeout: int = 300):
        """
        Initialize the query processor

        Args:
            base_url: Base URL of the Lens API server
            timeout: Request timeout in seconds
        """
        self.base_url = base_url.rstrip('/')
        self.client = httpx.Client(timeout=timeout)

    def process_query(self,
                     query: str,
                     initial_docs: Optional[List[str]] = None,
                     reasoning_mode: str = "comprehensive",
                     workflow_id: Optional[str] = None,
                     workflow_name: Optional[str] = None) -> Dict[str, Any]:
        """
        Process a query through the Lens reasoning system

        Args:
            query: The question or problem to reason about
            initial_docs: Initial documents to include in context
            reasoning_mode: Reasoning mode (comprehensive, focused, or policy_guided)
            workflow_id: Optional workflow identifier
            workflow_name: Optional workflow name

        Returns:
            Dictionary containing:
            - success: bool
            - contract_id: str
            - final_answer: str
            - confidence_overall: float
            - execution_time_ms: int
            - total_steps: int
            - knowledge_gaps: List[str]

        Raises:
            ProcessingError: If the reasoning process fails
        """
        try:
            response = self.client.post(
                f"{self.base_url}/lens/reasoning/process",
                json={
                    "query": query,
                    "initial_docs": initial_docs,
                    "reasoning_mode": reasoning_mode,
                    "workflow_id": workflow_id,
                    "workflow_name": workflow_name
                }
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise ProcessingError(f"Failed to process query: {str(e)}")

    def get_contract(self, contract_id: str) -> Dict[str, Any]:
        """
        Get complete contract details including reasoning trace

        Args:
            contract_id: The contract ID to retrieve

        Returns:
            Dictionary containing complete contract information

        Raises:
            ProcessingError: If the contract cannot be retrieved
        """
        try:
            response = self.client.get(f"{self.base_url}/lens/contracts/{contract_id}")
            if response.status_code == 404:
                raise ProcessingError(f"Contract {contract_id} not found")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise ProcessingError(f"Failed to get contract: {str(e)}")

    def get_reasoning_trace(self, contract_id: str) -> Dict[str, Any]:
        """
        Get detailed step-by-step reasoning trace

        Args:
            contract_id: The contract ID

        Returns:
            Dictionary containing detailed reasoning steps and analysis

        Raises:
            ProcessingError: If the trace cannot be retrieved
        """
        try:
            response = self.client.get(f"{self.base_url}/lens/reasoning/trace/{contract_id}")
            if response.status_code == 404:
                raise ProcessingError(f"Contract {contract_id} not found")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise ProcessingError(f"Failed to get reasoning trace: {str(e)}")

    def list_contracts(self,
                      workflow_id: Optional[str] = None,
                      limit: int = 20) -> List[Dict[str, Any]]:
        """
        List existing contracts with optional filtering

        Args:
            workflow_id: Optional workflow ID to filter by
            limit: Maximum number of contracts to return

        Returns:
            List of contract summaries

        Raises:
            ProcessingError: If the request fails
        """
        try:
            params = {"limit": limit}
            if workflow_id:
                params["workflow_id"] = workflow_id

            response = self.client.get(f"{self.base_url}/lens/contracts", params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise ProcessingError(f"Failed to list contracts: {str(e)}")

    def close(self):
        """Close the HTTP client"""
        self.client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()