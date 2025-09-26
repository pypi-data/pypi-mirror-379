"""
Steering Directives SDK for Lens Reasoning System

This SDK provides a focused interface for managing steering directives and re-running
reasoning with applied modifications.
"""

import httpx
from typing import List, Optional, Dict, Any
import sys
import os

# Add the parent directory to sys.path to import from models.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from models import ReasoningStepType
except ImportError:
    from .models import ReasoningStepType
try:
    from .exceptions import LensError, SteeringError
except ImportError:
    from exceptions import LensError, SteeringError


class LensSteeringManager:
    """
    Specialized SDK for managing steering directives and guided reasoning.

    This SDK focuses on steering directive management, allowing users to modify
    reasoning processes by adding guidance to specific steps and re-running
    the reasoning with applied directives.

    Example usage:
        manager = LensSteeringManager("https://api.tupl.xyz")

        # Add steering directive to a specific step
        manager.add_steering_directive(
            contract_id="contract_123",
            step_id="step_1",
            target_step_types=[ReasoningStepType.EVIDENCE_GATHERING],
            guidance="Focus specifically on peer-reviewed scientific studies",
            priority=8
        )

        # Re-run with steering applied
        updated_result = manager.apply_steering_and_rerun(contract_id)
        print(f"Updated answer: {updated_result['final_answer']}")
    """

    def __init__(self, base_url: str = "https://api.tupl.xyz", timeout: int = 300):
        """
        Initialize the steering manager

        Args:
            base_url: Base URL of the Lens API server
            timeout: Request timeout in seconds
        """
        self.base_url = base_url.rstrip('/')
        self.client = httpx.Client(timeout=timeout)

    def add_steering_directive(self,
                             contract_id: str,
                             step_id: str,
                             target_step_types: List[ReasoningStepType],
                             guidance: str,
                             priority: int = 5,
                             constraints: Optional[Dict[str, Any]] = None,
                             enforce_order: bool = False) -> Dict[str, Any]:
        """
        Add a steering directive to a specific step in a contract

        Args:
            contract_id: The contract to modify
            step_id: The specific step to add directives to
            target_step_types: Types of reasoning steps this directive applies to
            guidance: The guidance text for the directive
            priority: Priority level (1-10, default: 5)
            constraints: Additional constraints dictionary
            enforce_order: Whether to enforce step order

        Returns:
            Success response with configuration details

        Raises:
            SteeringError: If the directive cannot be added
        """
        try:
            # Convert enum to string values
            target_step_types_str = [step_type.value for step_type in target_step_types]

            response = self.client.post(
                f"{self.base_url}/lens/reasoning/{contract_id}/configure-step-directives",
                json={
                    "contract_id": contract_id,
                    "step_directives": [{
                        "step_id": step_id,
                        "directives": [{
                            "target_step_types": target_step_types_str,
                            "priority": priority,
                            "guidance": guidance,
                            "constraints": constraints or {},
                            "enforce_order": enforce_order
                        }]
                    }]
                }
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise SteeringError(f"Failed to add steering directive: {str(e)}")

    def add_multiple_steering_directives(self,
                                       contract_id: str,
                                       directives: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Add multiple steering directives to different steps

        Args:
            contract_id: The contract to modify
            directives: List of directive configurations, each containing:
                - step_id: str
                - target_step_types: List[ReasoningStepType]
                - guidance: str
                - priority: int (optional, default: 5)
                - constraints: Dict (optional)
                - enforce_order: bool (optional, default: False)

        Returns:
            Success response with configuration details

        Raises:
            SteeringError: If the directives cannot be added
        """
        try:
            step_directives = []
            for directive in directives:
                target_step_types_str = [step_type.value for step_type in directive["target_step_types"]]

                step_directives.append({
                    "step_id": directive["step_id"],
                    "directives": [{
                        "target_step_types": target_step_types_str,
                        "priority": directive.get("priority", 5),
                        "guidance": directive["guidance"],
                        "constraints": directive.get("constraints", {}),
                        "enforce_order": directive.get("enforce_order", False)
                    }]
                })

            response = self.client.post(
                f"{self.base_url}/lens/reasoning/{contract_id}/configure-step-directives",
                json={
                    "contract_id": contract_id,
                    "step_directives": step_directives
                }
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise SteeringError(f"Failed to add multiple steering directives: {str(e)}")

    def apply_steering_and_rerun(self,
                                contract_id: str,
                                preserve_original_trace: bool = True) -> Dict[str, Any]:
        """
        Apply all configured steering directives and re-run the reasoning

        Args:
            contract_id: The contract to re-run with steering
            preserve_original_trace: Whether to preserve the original reasoning trace

        Returns:
            Dictionary containing the updated reasoning result with:
            - success: bool
            - contract_id: str
            - total_steps: int
            - confidence_overall: float
            - execution_time_ms: int
            - final_answer: str
            - directive_impact_summary: Dict
            - directive_change_records: List

        Raises:
            SteeringError: If the steering cannot be applied or reasoning fails
        """
        try:
            response = self.client.post(
                f"{self.base_url}/lens/reasoning/{contract_id}/apply-directives",
                json={
                    "contract_id": contract_id,
                    "preserve_original_trace": preserve_original_trace
                }
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise SteeringError(f"Failed to apply steering and rerun: {str(e)}")

    def get_directive_status(self, contract_id: str) -> Dict[str, Any]:
        """
        Get status of all configured steering directives for a contract

        Args:
            contract_id: The contract to check

        Returns:
            Dictionary containing directive status information:
            - contract_id: str
            - total_steps: int
            - steps_with_directives: int
            - step_statuses: List[Dict]
            - has_pending_directives: bool

        Raises:
            SteeringError: If the status cannot be retrieved
        """
        try:
            response = self.client.get(f"{self.base_url}/lens/reasoning/{contract_id}/directive-status")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise SteeringError(f"Failed to get directive status: {str(e)}")

    def clear_directives(self, contract_id: str) -> Dict[str, Any]:
        """
        Clear all configured steering directives for a contract

        Args:
            contract_id: The contract to clear directives from

        Returns:
            Success response

        Raises:
            SteeringError: If the directives cannot be cleared
        """
        try:
            response = self.client.delete(f"{self.base_url}/lens/reasoning/{contract_id}/clear-directives")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise SteeringError(f"Failed to clear directives: {str(e)}")

    def get_reasoning_trace_with_steering(self, contract_id: str) -> Dict[str, Any]:
        """
        Get detailed reasoning trace showing steering impact

        Args:
            contract_id: The contract ID

        Returns:
            Dictionary containing detailed trace with steering information

        Raises:
            SteeringError: If the trace cannot be retrieved
        """
        try:
            response = self.client.get(f"{self.base_url}/lens/reasoning/trace/{contract_id}")
            if response.status_code == 404:
                raise SteeringError(f"Contract {contract_id} not found")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise SteeringError(f"Failed to get reasoning trace: {str(e)}")

    def close(self):
        """Close the HTTP client"""
        self.client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()