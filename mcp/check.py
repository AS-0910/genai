import requests
import json

def load_mcp_config(config_file_path):
    print(f"Loading configuration from {config_file_path}...")
    with open(config_file_path, "r") as f:
        config = json.load(f)
        server_config = config["servers"]["weather"]
        return {
            "url": server_config["url"],
        }

def check_mcp_server(mcp_server):
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "jsonrpc": "2.0",
        "id": "1",
        "method": "initialize",
        "params": {}
    }
    response = requests.post(mcp_server["url"], json=payload, headers=headers)
    if response.status_code == 200:
        print("MCP server is reachable and working!")
        print(f"Response: {response.text}")
    else:
        print(f"MCP server responded with status code: {response.status_code}")
        print(f"Response text: {response.text}")

if __name__ == "__main__":
    CONFIG_FILE = ".vscode/mcp.json"
    mcp_server_config = load_mcp_config(CONFIG_FILE)
    check_mcp_server(mcp_server_config)