# main.py
from fastmcp import FastMCP
from tools.qwen_content_search import content
from tools.md2excel import MarkdownConverter

app = FastMCP("qnvip-qwen-mcp")

# 注册工具
app.tool(description="使用青优千问搜索查询公司文档，代码规范，技术文档，需求文档，周报，日报，代码，获取原文")(content)

# 注册MCP优化的方法
app.tool(description="将Markdown文件转换为Excel文件")(MarkdownConverter.convert_md_to_excel_for_mcp)


def main():
    """MCP服务入口点"""
    app.run(transport="stdio")

if __name__ == "__main__":
    main()
