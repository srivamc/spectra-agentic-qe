"""
ContractIQ Layer 1 - Discovery Agent
API/UI discovery and verification agent.
"""
from __future__ import annotations
import asyncio
from typing import Any, Dict, List
from loguru import logger
from core.context_manager import ContractIQContext


class DiscoveryAgent:
    """Layer 1 Agent - Discovers and verifies API endpoints and UI components."""

    def __init__(self, context: ContractIQContext):
        self.context = context
        self.discovered_endpoints: List[Dict[str, Any]] = []

    async def discover(self, knowledge_base: Dict[str, Any]) -> Dict[str, Any]:
        """Discover and verify all endpoints from knowledge base."""
        logger.info("Discovery phase started")

        endpoints = knowledge_base.get("endpoints", [])
        verified = []

        for endpoint in endpoints:
            if await self._verify_endpoint(endpoint):
                verified.append(endpoint)

        logger.success(f"Discovery complete: {len(verified)}/{len(endpoints)} endpoints verified")
        return {"verified_endpoints": verified}

    async def _verify_endpoint(self, endpoint: Dict[str, Any]) -> bool:
        """Verify endpoint is accessible."""
        import httpx
        try:
            base_url = self.context.target_url or ""
            url = f"{base_url}{endpoint['path']}"
            async with httpx.AsyncClient(timeout=5) as client:
                response = await client.request(method=endpoint['method'], url=url)
                return response.status_code < 500
        except Exception as e:
            logger.warning(f"Endpoint verification failed: {endpoint['path']} - {e}")
            return False
