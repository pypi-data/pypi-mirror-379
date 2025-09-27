"""
Configuration module for Bitbucket MCP Server
Handles environment variables and HTTP header-based configuration
"""

import os
from typing import Any, Dict, Optional

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """
    Configuration class that can retrieve settings from multiple sources:
    1. Environment variables (for STDIO connections)
    2. HTTP headers (for HTTP/SSE connections)
    3. Default values
    """

    def __init__(self, headers: Optional[Dict[str, str]] = None):
        """
        Initialize configuration with optional HTTP headers

        Args:
            headers: Optional HTTP headers dict for HTTP/SSE connections
        """
        self.headers = headers or {}
        self._cached_values: Dict[str, Any] = {}

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value from headers (with X- prefix) or environment

        Priority order:
        1. HTTP header (X-BITBUCKET-{KEY} or X-{KEY})
        2. Environment variable (BITBUCKET_{KEY} or {KEY}) - only if allowed
        3. Default value
        """
        # Check cache first
        if key in self._cached_values:
            return self._cached_values[key]

        # Try HTTP headers first (case-insensitive)
        if self.headers:
            # Try with X-BITBUCKET- prefix
            header_key = f"X-BITBUCKET-{key}".replace('_', '-')
            for h_key, h_val in self.headers.items():
                if h_key.upper() == header_key.upper():
                    self._cached_values[key] = h_val
                    return h_val

            # Try with just X- prefix
            header_key = f"X-{key}".replace('_', '-')
            for h_key, h_val in self.headers.items():
                if h_key.upper() == header_key.upper():
                    self._cached_values[key] = h_val
                    return h_val

        # Try environment variables (with security check for HTTP mode)
        # Skip env vars for sensitive data if client should provide credentials
        sensitive_keys = ["USERNAME", "APP_PASSWORD", "WORKSPACE", "REPO"]
        is_sensitive = key.upper() in sensitive_keys

        # In HTTP mode with REQUIRE_CLIENT_CREDENTIALS, don't use server env for sensitive data
        if is_sensitive and self.headers and os.getenv("REQUIRE_CLIENT_CREDENTIALS", "false").lower() == "true":
            # Don't use server's credentials, require client to provide them
            self._cached_values[key] = default
            return default

        # First try with BITBUCKET_ prefix
        env_key = f"BITBUCKET_{key}"
        value = os.getenv(env_key)
        if value is not None:
            self._cached_values[key] = value
            return value

        # Then try without prefix
        value = os.getenv(key)
        if value is not None:
            self._cached_values[key] = value
            return value

        # Return default
        self._cached_values[key] = default
        return default

    def get_bool(self, key: str, default: bool = False) -> bool:
        """Get configuration value as boolean"""
        value = self.get(key)
        if value is None:
            return default
        if isinstance(value, bool):
            return value
        # Convert string to bool
        return str(value).lower() in ('true', '1', 'yes', 'on')

    @property
    def workspace(self) -> str:
        """Get workspace configuration"""
        return self.get("WORKSPACE", "")

    @property
    def repo_slug(self) -> str:
        """Get repository slug configuration"""
        return self.get("REPO", "")

    @property
    def username(self) -> Optional[str]:
        """Get Bitbucket username"""
        return self.get("USERNAME")

    @property
    def app_password(self) -> Optional[str]:
        """Get Bitbucket app password"""
        return self.get("APP_PASSWORD")

    @property
    def no_tools(self) -> bool:
        """Check if tools should be disabled"""
        return self.get_bool("NO_TOOLS", False)

    @property
    def auth_token(self) -> Optional[str]:
        """Get Bearer auth token from Authorization header"""
        if self.headers:
            auth_header = self.headers.get("Authorization") or self.headers.get("authorization")
            if auth_header and auth_header.startswith("Bearer "):
                return auth_header[7:]  # Remove "Bearer " prefix
        return None


# Global configuration instance (for backward compatibility)
_global_config = Config()

# Legacy exports for backward compatibility
WORKSPACE = _global_config.workspace
REPO_SLUG = _global_config.repo_slug
BITBUCKET_USERNAME = _global_config.username
BITBUCKET_APP_PASSWORD = _global_config.app_password
NO_TOOLS = _global_config.no_tools

# API Configuration
BASE_URL = "https://api.bitbucket.org/2.0"
DEFAULT_TIMEOUT = 30.0

# Server Configuration
SERVER_NAME = "bitbucket_mcp"
SERVER_INSTRUCTIONS = """An essential toolset for common Bitbucket workflows including pipelines, pull requests, and repository management"""


def get_config(headers: Optional[Dict[str, str]] = None) -> Config:
    """
    Get a configuration instance, optionally with HTTP headers

    Args:
        headers: Optional HTTP headers for HTTP/SSE connections

    Returns:
        Config instance
    """
    if headers:
        return Config(headers)
    return _global_config


def update_global_config(headers: Optional[Dict[str, str]] = None):
    """
    Update the global configuration with HTTP headers
    This should be called early in the request lifecycle for HTTP/SSE connections
    """
    global _global_config
    _global_config = Config(headers)