#!/usr/bin/env python3
"""
Simple MCP Server Tester
Makes it easier to test your MCP servers interactively
"""

import json
import subprocess
import sys

def test_mcp_server(server_path, method, params=None):
    """Test an MCP server with a given method and parameters"""
    request = {"method": method}
    if params:
        request["params"] = params
    
    try:
        result = subprocess.run(
            ["python3", server_path],
            input=json.dumps(request),
            text=True,
            capture_output=True,
            timeout=10
        )
        
        if result.returncode == 0:
            response = json.loads(result.stdout)
            return response
        else:
            return {"error": f"Server error: {result.stderr}"}
    
    except Exception as e:
        return {"error": str(e)}

def main():
    servers = {
        "1": ("aws-mcp/aws-server.py", "AWS MCP Server"),
        "2": ("database-mcp/sqlite-server.py", "Database MCP Server"),
        "3": ("custom-mcp/template-server.py", "Custom MCP Server"),
        "4": ("local-mcp/filesystem-server.py", "File System MCP Server")
    }
    
    print("MCP Server Tester")
    print("================")
    
    for key, (path, name) in servers.items():
        print(f"{key}. {name}")
    
    choice = input("\nSelect server (1-4): ")
    
    if choice not in servers:
        print("Invalid choice")
        return
    
    server_path, server_name = servers[choice]
    print(f"\nTesting {server_name}")
    
    # List available tools
    print("\nAvailable tools:")
    response = test_mcp_server(server_path, "tools/list")
    
    if "tools" in response:
        for i, tool in enumerate(response["tools"], 1):
            print(f"{i}. {tool['name']}: {tool['description']}")
        
        tool_choice = input(f"\nSelect tool (1-{len(response['tools'])}): ")
        
        try:
            tool_index = int(tool_choice) - 1
            if 0 <= tool_index < len(response["tools"]):
                tool = response["tools"][tool_index]
                tool_name = tool["name"]
                
                # Simple argument collection (you can enhance this)
                args = {}
                if "required" in tool["inputSchema"]:
                    for req_field in tool["inputSchema"]["required"]:
                        value = input(f"Enter {req_field}: ")
                        args[req_field] = value
                
                # Call the tool
                print(f"\nCalling {tool_name}...")
                result = test_mcp_server(server_path, "tools/call", {
                    "name": tool_name,
                    "arguments": args
                })
                
                print("\nResult:")
                print(json.dumps(result, indent=2))
            
            else:
                print("Invalid tool choice")
        
        except ValueError:
            print("Invalid input")
    
    else:
        print("Error:", response.get("error", "Unknown error"))

if __name__ == "__main__":
    main()