
"""
Bitbucket MCP Server
Main entry point that uses the composite pattern to combine tools and resources
Version: 2.2.0 - Transport-aware security and authentication
"""
import os
import sys

from fastmcp import FastMCP
from fastmcp.utilities.logging import get_logger

from src.modules.middleware import BearerAuthMiddleware
from src.utils.config import SERVER_INSTRUCTIONS, SERVER_NAME
from src.utils.security import get_security_warnings

try:
    # Try relative import first (for package installation)
    from .resources_server import server as resources_server
    from .tools_server import server as tools_server
except ImportError:
    # Fall back to absolute import (for local development)
    from resources_server import server as resources_server
    from tools_server import server as tools_server

logger = get_logger(__name__)

# Detect transport
transport = "http" if (os.getenv("FASTMCP_PORT") or os.getenv("PORT") or "--http" in sys.argv) else "stdio"

# Show security warnings
warnings = get_security_warnings(transport)
for warning in warnings:
    logger.warning(warning)

# Create server
server = FastMCP(
    SERVER_NAME,
    instructions=SERVER_INSTRUCTIONS
)

# Add authentication middleware for HTTP transport
if transport in ["http", "sse"]:
    server.add_middleware(BearerAuthMiddleware())
    logger.info("Authentication middleware enabled for HTTP transport")

if os.getenv("NO_TOOLS") is None:
    server.mount(tools_server)

server.mount(resources_server)

def main():
    # Run with appropriate transport
    if transport in ["http", "sse"]:
        # Run as HTTP server
        import asyncio
        port = int(os.getenv("FASTMCP_PORT", os.getenv("PORT", "8000")))
        host = os.getenv("FASTMCP_HOST", "localhost")
        logger.info(f"Starting HTTP server on {host}:{port}")
        asyncio.run(server.run_http_async(host=host, port=port))
    else:
        # Run as STDIO server (default)
        server.run()

if __name__ == "__main__":
    main()
    
