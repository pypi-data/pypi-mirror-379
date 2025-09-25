"""
一个简单的mcp_server，只提供了一个加法工具
"""
from mcp.server.fastmcp import FastMCP

# 创建一个MCP服务器
mcp = FastMCP("Demo")

# 创建一个加法工具
@mcp.tool()
def add(a: int, b: int) -> int:
    """两个数相加"""
    print(a, b)
    return a + b

# 创建一个加法工具
@mcp.tool()
def sayHello(name: str) -> str:
    """向对方说一句你好"""
    return "你好啊 " + name

def main():
    """主函数入口"""
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()