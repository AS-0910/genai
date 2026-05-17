from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather", port=9001)

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get the current weather for a given location."""
    # This is a placeholder implementation. In a real implementation, you would
    # call a weather API to get the actual weather data.
    return f"The current weather in {location} is sunny with a temperature of 25°C."


if __name__ == "__main__":
    mcp.run(transport="streamable-http")