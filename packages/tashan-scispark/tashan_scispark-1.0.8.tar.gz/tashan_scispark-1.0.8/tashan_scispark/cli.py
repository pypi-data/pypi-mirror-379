#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
TaShan SciSpark CLI Interface

Command line interface for TaShan SciSpark academic research assistant.
"""

import argparse
import sys
import os
import logging
from typing import Optional

# 添加当前目录到Python路径以支持相对导入
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

def setup_logging(verbose: bool = False) -> None:
    """
    设置日志配置
    
    Args:
        verbose: 是否启用详细日志输出
    """
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

def run_mcp_server(transport: str = "stdio", host: str = "localhost", port: int = 8000) -> None:
    """
    启动MCP服务器
    
    Args:
        transport: 传输协议 ("stdio" 或 "http")
        host: HTTP服务器主机地址
        port: HTTP服务器端口
    """
    try:
        from .mcp_server import main as mcp_main
        
        if transport == "http":
            # 设置环境变量用于HTTP传输
            os.environ["MCP_TRANSPORT"] = "http"
            os.environ["MCP_HOST"] = host
            os.environ["MCP_PORT"] = str(port)
            print(f"启动TaShan SciSpark MCP服务器 (HTTP传输) - http://{host}:{port}")
        else:
            print("启动TaShan SciSpark MCP服务器 (STDIO传输)")
        
        mcp_main()
        
    except ImportError as e:
        print(f"错误: 无法导入MCP服务器模块: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"错误: 启动MCP服务器失败: {e}")
        sys.exit(1)

def run_celery_worker() -> None:
    """
    启动Celery工作进程
    """
    try:
        from .celery_worker import main as worker_main
        print("启动TaShan SciSpark Celery Worker")
        worker_main()
        
    except ImportError as e:
        print(f"错误: 无法导入Celery Worker模块: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"错误: 启动Celery Worker失败: {e}")
        sys.exit(1)

def show_version() -> None:
    """显示版本信息"""
    try:
        from . import __version__, __description__
        print(f"TaShan SciSpark v{__version__}")
        print(__description__)
    except ImportError:
        print("TaShan SciSpark v1.0.0")
        print("Academic Research Assistant MCP Server")

def main() -> None:
    """
    主命令行入口点
    """
    parser = argparse.ArgumentParser(
        description="TaShan SciSpark - Academic Research Assistant MCP Server",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # 启动MCP服务器 (STDIO传输，用于Claude Desktop)
  tashan-scispark mcp

  # 启动MCP服务器 (HTTP传输)
  tashan-scispark mcp --transport http --port 8000

  # 启动Celery工作进程
  tashan-scispark worker

  # 显示版本信息
  tashan-scispark --version
        """
    )
    
    parser.add_argument(
        "--version", 
        action="store_true",
        help="显示版本信息"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="启用详细日志输出"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="可用命令")
    
    # MCP服务器子命令
    mcp_parser = subparsers.add_parser("mcp", help="启动MCP服务器")
    mcp_parser.add_argument(
        "--transport",
        choices=["stdio", "http"],
        default="stdio",
        help="传输协议 (默认: stdio)"
    )
    mcp_parser.add_argument(
        "--host",
        default="localhost",
        help="HTTP服务器主机地址 (默认: localhost)"
    )
    mcp_parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="HTTP服务器端口 (默认: 8000)"
    )
    
    # Celery Worker子命令
    worker_parser = subparsers.add_parser("worker", help="启动Celery工作进程")
    
    args = parser.parse_args()
    
    # 设置日志
    setup_logging(args.verbose)
    
    # 处理版本信息
    if args.version:
        show_version()
        return
    
    # 处理子命令
    if args.command == "mcp":
        run_mcp_server(args.transport, args.host, args.port)
    elif args.command == "worker":
        run_celery_worker()
    else:
        # 默认启动MCP服务器
        print("未指定命令，启动MCP服务器 (STDIO传输)")
        run_mcp_server()

if __name__ == "__main__":
    main()