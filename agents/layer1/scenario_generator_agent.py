"""
ContractIQ Layer 1 - Scenario Generator Agent
Generates test scenarios from spec knowledge base.
"""
from __future__ import annotations
import asyncio
from typing import Any, Dict, List
from loguru import logger
from core.context_manager import ContractIQContext


class ScenarioGeneratorAgent:
    """Layer 1 Agent - Generates test scenarios from knowledge base."""

    def __init__(self, context: ContractIQContext):
        self.context = context

    async def generate_scenarios(self, knowledge_base: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate comprehensive test scenarios."""
        logger.info("Scenario generation started")

        scenarios = []
        endpoints = knowledge_base.get("endpoints", [])

        for endpoint in endpoints:
            # Happy path scenario
            scenarios.append(self._create_happy_path(endpoint))

            # Error scenarios
            scenarios.extend(self._create_error_scenarios(endpoint))

            # Security scenarios
            if endpoint.get("security"):
                scenarios.extend(self._create_security_scenarios(endpoint))

        logger.success(f"Generated {len(scenarios)} test scenarios")
        return scenarios

    def _create_happy_path(self, endpoint: Dict) -> Dict[str, Any]:
        return {
            "name": f"Happy path: {endpoint['method']} {endpoint['path']}",
            "type": "happy_path",
            "endpoint": endpoint,
            "expected_status": 200
        }

    def _create_error_scenarios(self, endpoint: Dict) -> List[Dict[str, Any]]:
        return [
            {"name": f"404: {endpoint['method']} {endpoint['path']}", "type": "error", "endpoint": endpoint, "expected_status": 404},
            {"name": f"400: Invalid params {endpoint['method']} {endpoint['path']}", "type": "validation", "endpoint": endpoint, "expected_status": 400}
        ]

    def _create_security_scenarios(self, endpoint: Dict) -> List[Dict[str, Any]]:
        return [
            {"name": f"401: No auth {endpoint['method']} {endpoint['path']}", "type": "security", "endpoint": endpoint, "expected_status": 401}
        ]
