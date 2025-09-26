# MCP Protocol Bridge

A minimal MCP proxy server that bridges HTTP-based MCP servers to stdio protocol using FastMCP.

## Quick Start

### 1. Install with uv

```bash
uv sync
```

### 2. Run the Proxy

```bash
uv run python mcp_protocol_bridge.py --servers 'graphiti=http://test-graphiti.yangqianguan.com/mcp/'
```

### Multiple Servers

```bash
uv run python mcp_protocol_bridge.py --servers 'graphiti=http://test-graphiti.yangqianguan.com/mcp/,feishu=https://mcp.fintopia.tech/feishu'
```

### Integration with Claude Code

Add to your MCP configuration:

```json
{
  "mcpServers": {
    "proxy": {
      "command": "uv",
      "args": ["run", "python", "/path/to/mcp_protocol_bridge.py", "--servers", "graphiti=http://test-graphiti.yangqianguan.com/mcp/"],
      "cwd": "/path/to/mcp-protocol-bridge"
    }
  }
}
```

## Usage

### Arguments

- `--servers`, `-s`: Comma-separated list of servers in format `name=url`
  - Each server is specified as `name=url`
  - Multiple servers are separated by commas
  - Example: `'server1=http://example.com/mcp,server2=https://api.example.org/mcp'`

### Help

```bash
uv run python mcp_protocol_bridge.py --help
```

## What It Does

✅ **Bridges HTTP to stdio**: Converts HTTP MCP servers to stdio protocol
✅ **Multiple servers**: Configure multiple backends in one proxy
✅ **Simple configuration**: Just use command-line arguments
✅ **uv ready**: Fast dependency management and execution

## How It Works

1. Parses your server configuration from `--servers` argument
2. FastMCP's `as_proxy()` handles all the complex MCP protocol bridging
3. Each server gets mounted with its configured name
4. Single stdio interface for all backends

That's it! FastMCP does all the heavy lifting. 🚀