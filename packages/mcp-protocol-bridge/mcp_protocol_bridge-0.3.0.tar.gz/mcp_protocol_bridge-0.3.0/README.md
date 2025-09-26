# Simple MCP Proxy

A minimal MCP proxy server that bridges HTTP-based MCP servers to stdio protocol using FastMCP.

## Quick Start

### 1. Install with uv

```bash
uv sync
```

### 2. Create Configuration

See `graphiti-config.json` for example:

```json
{
  "servers": [
    {
      "name": "graphiti",
      "url": "http://test-graphiti.yangqianguan.com/mcp/"
    }
  ]
}
```

### 3. Run the Proxy

```bash
uv run python mcp_protocol_bridge.py --config graphiti-config.json
```

### 4. Test the Proxy

```bash
uv run python test_proxy.py
```

## Alternative Usage

### Environment Variables

```bash
export MCP_PROXY_SERVERS='[{"name":"graphiti","url":"http://test-graphiti.yangqianguan.com/mcp/"}]'
uv run python mcp_protocol_bridge.py
```

### Integration with Junie/Claude Code

Add to your MCP configuration:

```json
{
  "mcpServers": {
    "graphiti-proxy": {
      "command": "uv",
      "args": ["run", "python", "/path/to/mcp_protocol_bridge.py", "--config", "/path/to/graphiti-config.json"],
      "cwd": "/path/to/mcp-protocol-bridge"
    }
  }
}
```

## What It Does

✅ **Bridges HTTP to stdio**: Converts HTTP MCP servers to stdio protocol
✅ **Multiple servers**: Configure multiple backends in one proxy
✅ **Zero complexity**: Just 70 lines leveraging FastMCP's built-in proxy
✅ **uv ready**: Fast dependency management and execution

## How It Works

1. FastMCP's `as_proxy()` handles all the complex MCP protocol bridging
2. We just mount HTTP servers with simple configuration
3. Each server gets its own namespace (e.g., `/graphiti/`)
4. Single stdio interface for all backends

That's it! FastMCP does all the heavy lifting. 🚀