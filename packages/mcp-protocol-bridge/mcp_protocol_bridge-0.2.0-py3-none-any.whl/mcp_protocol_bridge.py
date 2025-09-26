#!/usr/bin/env python3
"""Simple MCP proxy server with configurable backends."""

import asyncio
import json
import sys
from pathlib import Path
from typing import List, Dict, Any
from fastmcp import FastMCP
import os
import argparse

def load_config(config_path: str = None) -> List[Dict[str, Any]]:
    """Load server configurations from file or environment."""

    # Try config file first
    if config_path and Path(config_path).exists():
        with open(config_path, 'r') as f:
            config = json.load(f)
            return config.get('servers', [])

    # Fallback to environment variable
    servers_env = os.environ.get('MCP_PROXY_SERVERS')
    if servers_env:
        try:
            return json.loads(servers_env)
        except json.JSONDecodeError:
            print("Error: Invalid JSON in MCP_PROXY_SERVERS environment variable", file=sys.stderr)
            return []

    return []


async def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='MCP Proxy Server')
    parser.add_argument('--config', help='Path to configuration file')
    args = parser.parse_args()

    # Load server configurations
    servers = load_config(args.config)

    if not servers:
        print("No servers configured. Use --config or MCP_PROXY_SERVERS environment variable.", file=sys.stderr)
        print("Example: MCP_PROXY_SERVERS='[{\"name\":\"graphiti\",\"url\":\"http://test-graphiti.yangqianguan.com/mcp/\"}]'", file=sys.stderr)
        sys.exit(1)

    # Create main proxy server
    proxy = FastMCP("MCP-Protocol-Bridge")

    # Mount each configured server as a proxy
    for server_config in servers:
        name = server_config.get('name')
        url = server_config.get('url')

        if not name or not url:
            print(f"Skipping invalid server config: {server_config}", file=sys.stderr)
            continue

        try:
            # Create proxy for this server using FastMCP's built-in functionality
            server_proxy = FastMCP.as_proxy(url, name=f"{name}-original")
            proxy.mount(server_proxy)
            print(f"✅ Mounted {name} -> {url}", file=sys.stderr)
        except Exception as e:
            print(f"❌ Failed to mount {name}: {e}", file=sys.stderr)

    # Run the combined proxy via stdio
    await proxy.run_stdio_async()


if __name__ == "__main__":
    asyncio.run(main())