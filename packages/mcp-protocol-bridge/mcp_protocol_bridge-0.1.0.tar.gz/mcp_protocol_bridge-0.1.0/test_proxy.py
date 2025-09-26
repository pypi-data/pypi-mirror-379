#!/usr/bin/env python3
"""Test the MCP proxy by sending test messages via stdio."""

import asyncio
import json
import subprocess
import sys

async def test_mcp_proxy():
    """Test the MCP proxy via stdio communication."""

    # Start the proxy process
    process = await asyncio.create_subprocess_exec(
        "uv", "run", "python", "mcp_proxy.py", "--config", "graphiti-config.json",
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    try:
        # Wait a moment for startup
        await asyncio.sleep(2)

        # Send initialize request
        init_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {},
                    "resources": {}
                },
                "clientInfo": {
                    "name": "test-client",
                    "version": "1.0.0"
                }
            }
        }

        print("📤 Sending initialize request...")
        request_bytes = (json.dumps(init_request) + "\n").encode('utf-8')
        process.stdin.write(request_bytes)
        await process.stdin.drain()

        # Read response with timeout
        try:
            response_line = await asyncio.wait_for(process.stdout.readline(), timeout=10.0)
            if response_line:
                response = json.loads(response_line.decode('utf-8').strip())
                print("📥 Initialize response received:")
                print(json.dumps(response, indent=2))

                if response.get("result"):
                    print("✅ Initialize successful!")

                    # Send tools/list request
                    tools_request = {
                        "jsonrpc": "2.0",
                        "id": 2,
                        "method": "tools/list"
                    }

                    print("\n📤 Sending tools/list request...")
                    tools_bytes = (json.dumps(tools_request) + "\n").encode('utf-8')
                    process.stdin.write(tools_bytes)
                    await process.stdin.drain()

                    # Read tools response
                    tools_response_line = await asyncio.wait_for(process.stdout.readline(), timeout=10.0)
                    if tools_response_line:
                        tools_response = json.loads(tools_response_line.decode('utf-8').strip())
                        print("📥 Tools response received:")
                        print(json.dumps(tools_response, indent=2))

                        if tools_response.get("result"):
                            tools = tools_response["result"].get("tools", [])
                            print(f"✅ Found {len(tools)} tools via proxy")
                        else:
                            print("ℹ️  Tools response received (may be empty or error)")
                else:
                    print("❌ Initialize failed")
            else:
                print("❌ No response received")

        except asyncio.TimeoutError:
            print("⏰ Response timeout")

    except Exception as e:
        print(f"❌ Test error: {e}")

    finally:
        # Clean shutdown
        process.terminate()
        try:
            await asyncio.wait_for(process.wait(), timeout=5.0)
            print("🛑 Process terminated cleanly")
        except asyncio.TimeoutError:
            process.kill()
            print("🛑 Process killed")

if __name__ == "__main__":
    print("🚀 Testing MCP Proxy with Graphiti...")
    asyncio.run(test_mcp_proxy())