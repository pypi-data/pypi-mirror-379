"""
Security configuration for Bitbucket MCP Server
Provides transport-aware authentication and credential handling
"""

import os
from typing import Any, Optional

from fastmcp.utilities.logging import get_logger

logger = get_logger(__name__)

# Simple bearer token authentication implementation
class SimpleBearerAuth:
    """Simple bearer token authentication for FastMCP servers."""

    def __init__(self, tokens: list[str]):
        """Initialize with a list of valid tokens."""
        self.valid_tokens = set(tokens)

    async def authenticate(self, headers: dict) -> bool:
        """Check if the request has a valid bearer token."""
        auth_header = headers.get("authorization", "")
        if auth_header.startswith("Bearer "):
            token = auth_header[7:]
            return token in self.valid_tokens
        return False


def get_server_auth(transport: Optional[str] = None):
    """
    Get appropriate authentication based on transport type

    Args:
        transport: Transport type ('stdio', 'http', 'sse', or None for auto-detect)

    Returns:
        Auth provider or None for no authentication
    """
    # Auto-detect transport if not provided
    if transport is None:
        # Check if running with HTTP server (port is set)
        if os.getenv("FASTMCP_PORT") or os.getenv("PORT"):
            transport = "http"
        else:
            transport = "stdio"

    # STDIO doesn't need server auth (client controls environment)
    if transport == "stdio":
        logger.info("STDIO transport detected - no server authentication required")
        return None

    # HTTP/SSE needs authentication
    if transport in ["http", "sse"]:
        # Check for auth token in environment
        auth_token = os.getenv("MCP_AUTH_TOKEN")

        if auth_token:
            logger.info("HTTP transport detected - enabling Bearer token authentication")
            # For now, return None since we need to handle auth differently
            # The actual auth check will happen in middleware
            return None
        else:
            logger.warning(
                "HTTP transport detected but MCP_AUTH_TOKEN not set! "
                "Server is unprotected. Set MCP_AUTH_TOKEN environment variable."
            )
            return None

    return None


def should_require_client_credentials(transport: Optional[str] = None) -> bool:
    """
    Determine if client should provide their own Bitbucket credentials

    Args:
        transport: Transport type

    Returns:
        True if client should provide credentials, False to use server credentials
    """
    # Auto-detect transport if not provided
    if transport is None:
        transport = "http" if (os.getenv("FASTMCP_PORT") or os.getenv("PORT")) else "stdio"

    # For HTTP, prefer client credentials for multi-tenancy
    if transport in ["http", "sse"]:
        # Check if server has its own credentials configured
        has_server_creds = bool(
            os.getenv("BITBUCKET_USERNAME") and
            os.getenv("BITBUCKET_APP_PASSWORD")
        )

        # If server has no credentials, client MUST provide them
        if not has_server_creds:
            return True

        # If configured, allow server credentials (single-tenant mode)
        # You can change this to always require client credentials
        return os.getenv("REQUIRE_CLIENT_CREDENTIALS", "false").lower() == "true"

    # STDIO always uses provided credentials (from client's env config)
    return False


def validate_credentials(config) -> bool:
    """
    Validate that necessary credentials are available

    Args:
        config: Config instance to validate

    Returns:
        True if valid credentials are available
    """
    # Check for auth token (Bearer) first
    if config.auth_token:
        return True

    # Check for username/password
    if config.username and config.app_password:
        return True

    return False


def get_security_warnings(transport: Optional[str] = None) -> list[str]:
    """
    Get list of security warnings for current configuration

    Returns:
        List of warning messages
    """
    warnings = []

    if transport is None:
        transport = "http" if (os.getenv("FASTMCP_PORT") or os.getenv("PORT")) else "stdio"

    if transport in ["http", "sse"]:
        if not os.getenv("MCP_AUTH_TOKEN"):
            warnings.append(
                "⚠️  HTTP server running without authentication! "
                "Set MCP_AUTH_TOKEN to protect your server."
            )

        if os.getenv("BITBUCKET_USERNAME") and os.getenv("BITBUCKET_APP_PASSWORD"):
            if not os.getenv("REQUIRE_CLIENT_CREDENTIALS"):
                warnings.append(
                    "⚠️  Server is using embedded Bitbucket credentials. "
                    "Consider setting REQUIRE_CLIENT_CREDENTIALS=true for multi-tenant mode."
                )

    return warnings