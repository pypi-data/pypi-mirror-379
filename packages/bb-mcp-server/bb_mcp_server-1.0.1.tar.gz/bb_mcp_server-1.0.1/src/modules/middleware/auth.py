"""
Authentication Middleware for Bitbucket MCP Server
Provides bearer token authentication for HTTP transport
"""

import os
from typing import Optional

from fastmcp.server.middleware import Middleware, MiddlewareContext
from fastmcp.utilities.logging import get_logger

logger = get_logger(__name__)


class BearerAuthMiddleware(Middleware):
    """
    Middleware that validates bearer tokens for HTTP requests.
    Only active when MCP_AUTH_TOKEN is set.
    """

    def __init__(self):
        """Initialize the auth middleware."""
        super().__init__()
        self.auth_token = os.getenv("MCP_AUTH_TOKEN")
        self.enabled = bool(self.auth_token)

        if self.enabled:
            logger.info("Bearer token authentication enabled")
        else:
            logger.warning("Bearer token authentication disabled - no MCP_AUTH_TOKEN set")

    async def on_request(self, context: MiddlewareContext, call_next):
        """
        Check bearer token on all requests if authentication is enabled.
        """
        # Skip auth if not enabled
        if not self.enabled:
            return await call_next(context)

        # Try to get headers
        headers = self._get_headers(context)

        # Check authorization header
        auth_header = headers.get("authorization", "")

        if not auth_header.startswith("Bearer "):
            # No bearer token provided
            raise ValueError("Authentication required: Missing Bearer token")

        token = auth_header[7:]  # Remove "Bearer " prefix

        if token != self.auth_token:
            # Invalid token
            raise ValueError("Authentication failed: Invalid token")

        # Token is valid, continue
        return await call_next(context)

    def _get_headers(self, context: MiddlewareContext) -> dict:
        """Extract headers from the context."""
        try:
            # Try FastMCP's get_http_headers if available
            from fastmcp.server.dependencies import get_http_headers
            headers = get_http_headers()
            if headers:
                return {k.lower(): v for k, v in headers.items()}
        except:
            pass

        # Fallback to empty dict for STDIO
        return {}