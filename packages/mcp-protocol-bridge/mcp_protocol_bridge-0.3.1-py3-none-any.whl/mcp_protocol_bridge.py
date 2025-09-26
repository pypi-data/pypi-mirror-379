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

def parse_servers_arg(servers_arg: str) -> List[Dict[str, str]]:
    """Parse servers argument in format 'name1=url1,name2=url2'."""
    servers = []

    for server_pair in servers_arg.split(','):
        server_pair = server_pair.strip()
        if not server_pair:
            continue

        if '=' not in server_pair:
            raise ValueError(f"Invalid server format: {server_pair}. Expected 'name=url'")

        name, url = server_pair.split('=', 1)
        servers.append({'name': name.strip(), 'url': url.strip()})

    return servers


def load_config(servers_arg: str = None) -> List[Dict[str, Any]]:
    """Load server configurations from CLI servers argument."""
    if not servers_arg:
        return []

    try:
        return parse_servers_arg(servers_arg)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


async def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='MCP Proxy Server')
    parser.add_argument('--servers', '-s', help='Servers in format "name1=url1,name2=url2"')
    args = parser.parse_args()

    # Load server configurations
    servers = load_config(args.servers)

    if not servers:
        print("No servers configured. Use --servers argument.", file=sys.stderr)
        print("Example: --servers 'graphiti=http://test-graphiti.yangqianguan.com/mcp/,feishu=https://mcp.fintopia.tech/feishu'", file=sys.stderr)
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

def entry_main():
    asyncio.run(main())

if __name__ == "__main__":
    asyncio.run(main())