"""
Authentication module for Bitbucket MCP Server
Handles multiple authentication methods:
1. Bearer Token from Authorization header
2. Basic Auth from X-BITBUCKET-USERNAME and X-BITBUCKET-APP-PASSWORD headers
3. Basic Auth from environment variables
"""

from base64 import b64encode
from typing import Dict, Optional

from src.utils.config import Config, get_config


def get_auth_headers(config: Optional[Config] = None) -> Dict[str, str]:
    """
    Generate auth headers for Bitbucket API with support for multiple auth methods

    Priority order:
    1. Bearer token from Authorization header
    2. Basic Auth from X-BITBUCKET-USERNAME and X-BITBUCKET-APP-PASSWORD headers
    3. Basic Auth from BITBUCKET_USERNAME and BITBUCKET_APP_PASSWORD env vars

    Args:
        config: Optional Config instance (will use global if not provided)

    Returns:
        Dict containing Authorization and Content-Type headers

    Raises:
        ValueError: If no authentication method is available
    """
    if config is None:
        config = get_config()

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # Check for Bearer token first
    auth_token = config.auth_token
    if auth_token:
        headers["Authorization"] = f"Bearer {auth_token}"
        return headers

    # Check for Basic Auth credentials
    username = config.username
    password = config.app_password

    if not username or not password:
        raise ValueError(
            "Authentication required. Provide either:\n"
            "1. Bearer token in Authorization header, or\n"
            "2. X-BITBUCKET-USERNAME and X-BITBUCKET-APP-PASSWORD headers, or\n"
            "3. BITBUCKET_USERNAME and BITBUCKET_APP_PASSWORD environment variables"
        )

    # Generate Basic Auth header
    credentials = f"{username}:{password}"
    encoded = b64encode(credentials.encode()).decode('ascii')
    headers["Authorization"] = f"Basic {encoded}"

    return headers