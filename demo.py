from mcp.server.fastmcp import FastMCP
mcp = FastMCP("天气查询服务")
@mcp.tool()
def get_weather(city: str) -> str:
    """获取指定城市的天气信息"""
    return f"{city}今日晴，28℃"
if __name__ == "__main__":
    print("MCP Server starting...", flush=True)  # 确保输出
    mcp.run(transport="stdio")
