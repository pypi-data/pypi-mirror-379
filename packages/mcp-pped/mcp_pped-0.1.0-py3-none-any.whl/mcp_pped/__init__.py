import argparse
from .server import mcp  # 从当前包下的 server.py 导入 mcp 实例

def main():
    """MCP Server for Personal Protective Equipment (PPE) Detection."""
    parser = argparse.ArgumentParser(
        description="A MCP server that detects PPE (safety helmets, vests, etc.) in images."
    )
    # 您可以在这里添加自定义的命令行参数
    # 例如： parser.add_argument("--model-path", help="Path to the model weights")
    parser.parse_args()  # 解析参数

    # 启动 MCP 服务器！
    mcp.run()

if __name__ == "__main__":
    main()