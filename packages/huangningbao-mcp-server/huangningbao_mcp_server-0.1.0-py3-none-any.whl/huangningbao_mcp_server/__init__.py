"""
FastMCP quickstart example.

cd to the `examples/snippets/clients` directory and run:
    uv run server fastmcp_quickstart stdio
"""

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


#需要注意的点
#1：函数下面的注释"""xxxx"""是必要的——告诉大模型这个工具是干什么的
#2：函数名的参数类型名是必须的——有助于模型理解这个工具运行方式
#3：装饰器@mcp.tool() 相当于http中的post（）只发布
#4：装饰器@mcp.resource() 相当于http中的get（）发布并且回传
#5：装饰器@mcp.prompt()


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


# Add a prompt
@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting prompt"""
    styles = {
        "friendly": "Please write a warm, friendly greeting",
        "formal": "Please write a formal, professional greeting",
        "casual": "Please write a casual, relaxed greeting",
    }

    return f"{styles.get(style, styles['friendly'])} for someone named {name}."



def main() -> None:
    mcp.run(transport="stdio")


"""
if __name__ == "__main__":
    #mcp.run(transport="stdio")
    mcp.run(transport="streamable-http")
"""