from fastmcp import FastMCP
from ant import base64_data
import re
import json
from fastmcp.tools.tool import ToolResult
from mcp.types import TextContent

mcp = FastMCP("mcp test echo service")


@mcp.tool()
def echo(input_str: str) -> str:
    """将输入的内容原样返回"""
    return input_str

@mcp.tool()
def echo_image(command: str) -> ToolResult:
    """返回图片内容"""
    output = []
    mo = re.match( r'^(\d+) images', command)
    print(mo.group(1))
    for i in range(int(mo.group(1))):
        output.append(base64_data)
    output_str = json.dumps(output)
    print(f"output_str: {len(output_str)}")
    return ToolResult(content=[TextContent(type="text", text=f"{output_str}")])

if __name__ == "__main__":
    mcp.run(transport="streamable-http")