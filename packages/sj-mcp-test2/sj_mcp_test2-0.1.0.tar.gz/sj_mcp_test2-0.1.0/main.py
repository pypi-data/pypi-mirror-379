# -*- coding: utf-8 -*-
"""
FastMCP 快速入门示例。
首先，请切换到 `examples/snippets/clients` 目录，然后运行以下命令来启动服务器：
    uv run server fastmcp_quickstart stdio
"""
# 从 mcp.server.fastmcp 模块中导入 FastMCP 类，这是构建 MCP 服务器的核心。
from mcp.server.fastmcp import FastMCP
# 创建一个 MCP 服务器实例，并将其命名为 "Demo"。
# 这个名字会向连接到此服务器的 AI 客户端展示。
mcp = FastMCP("Demo")
@mcp.tool()
def create_txt_file():
    """
      这个工具的功能是在指定目录下写入指定内容
      """
    # 文件路径
    file_path = "D:/test.txt"

    try:
        # 创建并写入文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("这是一个测试文件\n")
            file.write("创建时间：2024年\n")
            file.write("文件创建成功！\n")

        print(f"文件创建成功：{file_path}")
        return True

    except Exception as e:
        print(f"文件创建失败：{e}")
        return False

# # 使用 @mcp.tool() 装饰器来定义一个“工具”。
# # 工具是 AI 可以调用的具体函数，用于执行特定的操作。
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    这个工具的功能是计算两个整数的和。
    文档字符串（docstring）会作为工具的描述，帮助 AI 理解其功能。
    """
    return a + b
# 使用 @mcp.resource() 装饰器来定义一个“资源”。
# 资源代表 AI 可以访问的数据或信息。这里的路径 "greeting://{name}" 是动态的，
# {name} 部分可以被实际的名称替换，例如 "greeting://World"。
# @mcp.resource("greeting://{name}")
# def get_greeting(name: str) -> str:
#     """
#     根据提供的名称，获取一句个性化的问候语。
#     """
#     # 使用 f-string 格式化字符串，返回包含名字的问候语。
#     return f"Hello, {name}!"
# # 使用 @mcp.prompt() 装饰器来定义一个“提示词模板”。
# # 这个功能可以根据输入动态生成更复杂的、用于指导大语言模型（LLM）的指令（Prompt）。
# @mcp.prompt()
# def greet_user(name: str, style: str = "friendly") -> str:
#     """
#     根据给定的名字和风格，生成一句问候语的提示词。
#     """
#     # 定义一个字典，存储不同风格对应的提示词文本。
#     styles = {
#         "friendly": "Please write a warm, friendly greeting",
#         "formal": "Please write a formal, professional greeting",
#         "casual": "Please write a casual, relaxed greeting",
#     }
#
#     # 根据传入的 style 参数，从字典中获取对应的提示词。
#     # 如果 style 参数无效或未提供，则默认使用 "friendly" 风格。
#     # 最后，将选择的风格提示词与用户名组合，形成一个完整的指令。
#     return f"{styles.get(style, styles['friendly'])} for someone named {name}."
if __name__ == "__main__":

    mcp.run(transport="stdio")