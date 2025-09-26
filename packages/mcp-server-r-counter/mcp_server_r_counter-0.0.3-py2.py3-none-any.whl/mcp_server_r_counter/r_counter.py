from mcp.server.fastmcp import FastMCP
import os

# Configure FastMCP with proper host binding for containers
host = os.environ.get("HOST", "0.0.0.0")
port = int(os.environ.get("PORT", 8000))

mcp = FastMCP("r_counter", host=host, port=port)

@mcp.tool()
async def count(query: str) -> str:
    """Count number of R's or r's in the input query"""
    return str(query.lower().count("r"))

def main():
    transport = os.environ.get("MCP_TRANSPORT", "stdio")

    if transport == "streamable-http":
        # Use streamable HTTP transport for JSON-RPC over HTTP
        mcp.run(transport="streamable-http")
    else:
        # Use stdio transport for local development
        mcp.run(transport="stdio")

if __name__ == "__main__":
    main()