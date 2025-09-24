#!/usr/bin/env python3
import asyncio
import json
import sys
import websockets
import os
from typing import Dict, Any, List

class ZosMcpClient:
    def __init__(self):
        mainframe_host = os.getenv('ZOS_HOST', 'localhost')
        mainframe_port = os.getenv('ZOS_PORT', '8080')
        self.uri = f"ws://{mainframe_host}:{mainframe_port}/mcp"
        self.websocket = None
        self.request_id = 0

    async def connect(self):
        self.websocket = await websockets.connect(self.uri)

    async def disconnect(self):
        if self.websocket:
            await self.websocket.close()

    def get_next_id(self) -> int:
        self.request_id += 1
        return self.request_id

    async def send_request(self, method: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        request = {
            "jsonrpc": "2.0",
            "method": method,
            "id": self.get_next_id()
        }
        if params:
            request["params"] = params

        await self.websocket.send(json.dumps(request))
        response = await self.websocket.recv()
        return json.loads(response)

    async def list_tools(self) -> List[Dict[str, Any]]:
        response = await self.send_request("tools/list")
        return response.get("result", {}).get("tools", [])

    async def call_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        params = {
            "name": name,
            "arguments": arguments
        }
        response = await self.send_request("tools/call", params)
        return response.get("result", {})

async def handle_stdio():
    client = ZosMcpClient()
    
    try:
        await client.connect()
        
        while True:
            try:
                line = await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)
                if not line:
                    break
                
                request = json.loads(line.strip())
                method = request.get("method")
                params = request.get("params", {})
                request_id = request.get("id")
                
                response = {
                    "jsonrpc": "2.0",
                    "id": request_id
                }
                
                try:
                    if method == "tools/list":
                        tools = await client.list_tools()
                        response["result"] = {"tools": tools}
                    elif method == "tools/call":
                        tool_name = params.get("name")
                        arguments = params.get("arguments", {})
                        result = await client.call_tool(tool_name, arguments)
                        response["result"] = result
                    else:
                        response["error"] = {
                            "code": -32601,
                            "message": "Method not found"
                        }
                except Exception as e:
                    response["error"] = {
                        "code": -32603,
                        "message": str(e)
                    }
                
                print(json.dumps(response), flush=True)
                
            except json.JSONDecodeError:
                continue
            except EOFError:
                break
                
    except Exception as e:
        error_response = {
            "jsonrpc": "2.0",
            "error": {
                "code": -32603,
                "message": f"Connection error: {str(e)}"
            }
        }
        print(json.dumps(error_response), flush=True)
    finally:
        await client.disconnect()

def main():
    asyncio.run(handle_stdio())

if __name__ == "__main__":
    main()
