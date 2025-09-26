"""
FileSystem MCP Server - 提供文件系统操作的MCP工具
基于FastMCP框架，支持stdio和streamable-http传输协议
"""

import os
import sys
import argparse
import logging
from typing import Dict, Any, Optional, List, Union
from .config import load_config, get_transport_config

# 如果直接运行此脚本，调整Python路径以支持相对导入
if __name__ == "__main__" and __package__ is None:
    # 获取当前脚本的目录（src/mcp_filesystem）
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 获取项目根目录（src 的父目录）
    project_root = os.path.dirname(os.path.dirname(current_dir))
    # 将项目根目录添加到 sys.path
    sys.path.insert(0, project_root)
    # 设置 __package__ 为当前包名
    __package__ = "src.mcp_filesystem"

# 导入MCP SDK
try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print("错误: 未安装MCP SDK。请使用 'uv add mcp[cli]' 安装。")
    sys.exit(1)

# 导入文件系统功能模块
from .system_information import system_info, format_system_info
from .path_exist import path_exist, format_path_info
from .directory_information import directory_info, format_directory_info
from .directory_find import directory_find, format_directory_find
from .directory_create import directory_create, format_directory_create
from .directory_delete import directory_delete, format_directory_delete
from .directory_list import directory_list, format_directory_list
from .directory_rename import directory_rename, format_directory_rename
from .directory_copy import directory_copy, format_directory_copy
from .directory_move import directory_move, format_directory_move
from .directory_tree import directory_tree, format_directory_tree
from .file_information import file_info, format_file_info
from .file_create import file_create, format_file_create
from .file_delete import file_delete, format_file_delete
from .file_rename import file_rename, format_file_rename
from .file_copy import file_copy, format_file_copy
from .file_move import file_move, format_file_move
from .file_read import file_read, format_read_result
from .file_write import file_write, format_write_result
from .file_find import file_find, format_file_find

# 配置日志记录
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('mcp_filesystem.log', encoding='utf-8')
    ]
)
logger = logging.getLogger("mcp_filesystem")

# 默认配置
DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 8000

def register_tools(mcp_instance: FastMCP) -> None:
    """注册所有工具函数到MCP实例"""
    
    # 系统信息工具
    @mcp_instance.tool()
    def get_system_info() -> str:
        """获取系统信息，包括操作系统类型，cpu架构等。"""
        try:
            info = system_info()
            return format_system_info(info)
        except Exception as e:
            return f"获取系统信息时发生错误: {str(e)}"

    # 路径存在性检查工具
    @mcp_instance.tool()
    def check_path_exists(path: str) -> str:
        """
        检查路径是否存，如果存在，进一步判断这个路径是文件还是目录，返回路径类型。
        
        Args:
            path: 要检查的路径
        """
        try:
            result = path_exist(path)
            return format_path_info(result)
        except Exception as e:
            return f"检查路径存在性时发生错误: {str(e)}"

    # 目录信息工具
    @mcp_instance.tool()
    def get_directory_info(directory_path: str) -> str:
        """
        获取目录的详细信息，包括目录占磁盘空间，权限等信息。
        
        Args:
            directory_path: 目录路径
        """
        try:
            result = directory_info(directory_path)
            return format_directory_info(result)
        except Exception as e:
            return f"获取目录信息时发生错误: {str(e)}"

    # 目录查找工具
    @mcp_instance.tool()
    def find_directory(directory_path: str, name_pattern: str) -> str:
        """
        在指定目录中查找子目录
        
        Args:
            directory_path: 要搜索的目录路径
            name_pattern: 目录名模式（支持通配符，比如搜索名称中有trade的所有目录，可传参*trade*）
        """
        try:
            result = directory_find(directory_path, name_pattern)
            return format_directory_find(result)
        except Exception as e:
            return f"查找目录时发生错误: {str(e)}"

    # 目录创建工具
    @mcp_instance.tool()
    def create_directory(path: str, exist_ok: bool = False, parents: bool = True) -> str:
        """
        创建目录
        
        Args:
            path: 要创建的目录路径
            exist_ok: 如果目录已存在是否忽略错误（默认False）
            parents: 是否创建父目录（默认True）
        """
        try:
            result = directory_create(path, exist_ok=exist_ok, parents=parents)
            return format_directory_create(result)
        except Exception as e:
            return f"创建目录时发生错误: {str(e)}"

    # 目录删除工具
    @mcp_instance.tool()
    def delete_directory(path: str, recursive: bool = True) -> str:
        """
        删除目录
        
        Args:
            path: 要删除的目录路径
            recursive: 是否递归删除子目录和文件（默认True）
        """
        try:
            result = directory_delete(path, recursive=recursive)
            return format_directory_delete(result)
        except Exception as e:
            return f"删除目录时发生错误: {str(e)}"

    # 目录列表工具
    @mcp_instance.tool()
    def list_directory(directory_path: str, sort_by: str = 'name', 
                      reverse: bool = False, filter_type: Optional[str] = None) -> str:
        """
        列出目录内容
        
        Args:
            directory_path: 要列出的目录路径
            sort_by: 排序方式（name/size/modified/type，默认name）
            reverse: 是否反向排序（默认False）
            filter_type: 过滤类型（file/directory，默认不过滤）
        """
        try:
            result = directory_list(directory_path, sort_by=sort_by, 
                                  reverse=reverse, filter_type=filter_type)
            return format_directory_list(result)
        except Exception as e:
            return f"列出目录内容时发生错误: {str(e)}"

    # 目录重命名工具
    @mcp_instance.tool()
    def rename_directory(old_path: str, new_path: str) -> str:
        """
        重命名目录
        
        Args:
            old_path: 原目录路径
            new_path: 新目录路径
        """
        try:
            result = directory_rename(old_path, new_path)
            return format_directory_rename(result)
        except Exception as e:
            return f"重命名目录时发生错误: {str(e)}"

    # 目录复制工具
    @mcp_instance.tool()
    def copy_directory(source_path: str, destination_path: str, 
                      overwrite: bool = False) -> str:
        """
        复制目录
        
        Args:
            source_path: 源目录路径
            destination_path: 目标目录路径
            overwrite: 是否覆盖已存在的目录（默认False）
        """
        try:
            result = directory_copy(source_path, destination_path, overwrite=overwrite)
            return format_directory_copy(result)
        except Exception as e:
            return f"复制目录时发生错误: {str(e)}"

    # 目录移动工具
    @mcp_instance.tool()
    def move_directory(source_path: str, destination_path: str, 
                      overwrite: bool = False) -> str:
        """
        移动目录
        
        Args:
            source_path: 源目录路径
            destination_path: 目标目录路径
            overwrite: 是否覆盖已存在的目录（默认False）
        """
        try:
            result = directory_move(source_path, destination_path, overwrite=overwrite)
            return format_directory_move(result)
        except Exception as e:
            return f"移动目录时发生错误: {str(e)}"

    # 目录树工具
    @mcp_instance.tool()
    def get_directory_tree(directory_path: str, max_depth: int = 10) -> str:
        """
        获取目录树结构，相当于Linux中的tree命令，可指定最大深度。从而不用反复调用list_directory方法。
        
        Args:
            directory_path: 目录路径
            max_depth: 最大深度（默认10）
        """
        try:
            result = directory_tree(directory_path, max_depth=max_depth)
            return format_directory_tree(result)
        except Exception as e:
            return f"获取目录树时发生错误: {str(e)}"

    # 文件信息工具
    @mcp_instance.tool()
    def get_file_info(file_path: str) -> str:
        """
        获取文件信息
        
        Args:
            file_path: 文件路径
        """
        try:
            result = file_info(file_path)
            return format_file_info(result)
        except Exception as e:
            return f"获取文件信息时发生错误: {str(e)}"

    # 文件创建工具
    @mcp_instance.tool()
    def create_file(path: str, content: Optional[str] = None, 
                   encoding: str = 'utf-8', exist_ok: bool = False) -> str:
        """
        创建文件
        
        Args:
            path: 文件路径
            content: 文件内容（可选）
            encoding: 文件编码（默认utf-8）
            exist_ok: 如果文件已存在是否忽略错误（默认False）
        """
        try:
            result = file_create(path, content=content, encoding=encoding, exist_ok=exist_ok)
            return format_file_create(result)
        except Exception as e:
            return f"创建文件时发生错误: {str(e)}"

    # 文件删除工具
    @mcp_instance.tool()
    def delete_file(file_path: str) -> str:
        """
        删除文件
        
        Args:
            file_path: 文件路径
        """
        try:
            result = file_delete(file_path)
            return format_file_delete(result)
        except Exception as e:
            return f"删除文件时发生错误: {str(e)}"

    # 文件重命名工具
    @mcp_instance.tool()
    def rename_file(old_path: str, new_path: str) -> str:
        """
        重命名文件
        
        Args:
            old_path: 原文件路径
            new_path: 新文件路径
        """
        try:
            result = file_rename(old_path, new_path)
            return format_file_rename(result)
        except Exception as e:
            return f"重命名文件时发生错误: {str(e)}"

    # 文件复制工具
    @mcp_instance.tool()
    def copy_file(source_path: str, destination_path: str, overwrite: bool = False) -> str:
        """
        复制文件
        
        Args:
            source_path: 源文件路径
            destination_path: 目标文件路径
            overwrite: 是否覆盖已存在的文件（默认False）
        """
        try:
            result = file_copy(source_path, destination_path, overwrite=overwrite)
            return format_file_copy(result)
        except Exception as e:
            return f"复制文件时发生错误: {str(e)}"

    # 文件移动工具
    @mcp_instance.tool()
    def move_file(source_path: str, destination_path: str, 
                 overwrite: bool = False) -> str:
        """
        移动文件
        
        Args:
            source_path: 源文件路径
            destination_path: 目标文件路径
            overwrite: 是否覆盖已存在的文件（默认False）
        """
        try:
            result = file_move(source_path, destination_path, overwrite=overwrite)
            return format_file_move(result)
        except Exception as e:
            return f"移动文件时发生错误: {str(e)}"

    # 文件读取工具
    @mcp_instance.tool()
    def read_file(file_path: str, start_line: Optional[int] = None, 
                 end_line: Optional[int] = None, encoding: str = 'utf-8') -> str:
        """
        读取文件内容
        
        Args:
            file_path: 文件路径
            start_line: 起始行号（可选）
            end_line: 结束行号（可选）
            encoding: 文件编码（默认utf-8）
        """
        try:
            result = file_read(file_path, start_line=start_line, 
                              end_line=end_line, encoding=encoding)
            return format_read_result(result)
        except Exception as e:
            return f"读取文件时发生错误: {str(e)}"

    # 文件写入工具
    @mcp_instance.tool()
    def write_file(file_path: str, content: str, mode: str = 'overwrite', 
                  line_number: Optional[int] = None, encoding: str = 'utf-8') -> str:
        """
        写入文件内容
        
        Args:
            file_path: 文件路径
            content: 要写入的内容
            mode: 写入模式（overwrite/append/insert，默认overwrite）
            line_number: 插入模式下的行号（仅插入模式需要）
            encoding: 文件编码（默认utf-8）
        """
        try:
            result = file_write(file_path, content, mode=mode, 
                               line_number=line_number, encoding=encoding)
            return format_write_result(result)
        except Exception as e:
            return f"写入文件时发生错误: {str(e)}"

    # 文件查找工具
    @mcp_instance.tool()
    def find_file(directory_path: str, name_pattern: str) -> str:
        """
        在指定目录中查找文件
        
        Args:
            directory_path: 要搜索的目录路径
            name_pattern: 文件名模式（支持通配符）
        """
        try:
            result = file_find(directory_path, name_pattern)
            return format_file_find(result)
        except Exception as e:
            return f"查找文件时发生错误: {str(e)}"



def parse_arguments():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description="MCP FileSystem Server")
    
    # 配置文件参数
    parser.add_argument("--config", default=None,
                       help="配置文件路径（默认：自动查找config.toml）")
    
    # 传输协议选择（互斥）
    transport_group = parser.add_mutually_exclusive_group(required=False)
    transport_group.add_argument("--stdio", action="store_true", 
                               help="使用stdio传输协议")
    transport_group.add_argument("--streamable-http", action="store_true", 
                               help="使用streamable-http传输协议")
    transport_group.add_argument("--sse", action="store_true", 
                               help="使用SSE传输协议")
    
    # HTTP相关参数
    parser.add_argument("--host", default=None, 
                       help=f"HTTP服务器主机地址（默认：从配置文件或{DEFAULT_HOST}）")
    parser.add_argument("--port", type=int, default=None, 
                       help=f"HTTP服务器端口（默认：从配置文件或{DEFAULT_PORT}）")
    
    return parser.parse_args()

def main() -> None:
    """主函数 - 运行MCP server，支持stdio、streamable-http和SSE传输协议"""
    args = parse_arguments()
    
    # 加载配置文件
    config = load_config(args.config)
    transport_config = get_transport_config(config)
    
    # 确定传输协议（命令行参数优先于配置文件）
    transport = "stdio"
    if args.stdio:
        transport = "stdio"
    elif args.streamable_http:
        transport = "streamable-http"
    elif args.sse:
        transport = "sse"
    else:
        # 如果没有命令行参数，使用配置文件中的设置
        transport = transport_config["transport"]
    
    # 确定主机和端口（命令行参数优先于配置文件）
    host = args.host if args.host is not None else transport_config["host"]
    port = args.port if args.port is not None else transport_config["port"]
    
    logger.info(f"加载配置完成: 传输协议={transport}, 主机={host}, 端口={port}")
    
    # 根据传输协议创建和配置MCP server实例
    if transport == "stdio":
        # 创建MCP server实例
        mcp = FastMCP("FileSystem")
        # 注册工具到实例
        register_tools(mcp)
        
        logger.info("启动MCP FileSystem Server，传输协议: stdio")
        print("启动MCP FileSystem Server，传输协议: stdio")
        mcp.run(transport="stdio")
    else:
        # 对于HTTP-based协议，创建带有host和port参数的实例
        mcp = FastMCP("FileSystem", host=host, port=port)
        register_tools(mcp)  # 注册工具
        
        if transport == "streamable-http":
            logger.info(f"启动MCP FileSystem Server，传输协议: streamable-http")
            logger.info(f"服务器监听地址: http://{host}:{port}")
            print(f"启动MCP FileSystem Server，传输协议: streamable-http")
            print(f"服务器监听地址: http://{host}:{port}")
            mcp.run(transport="streamable-http")
        elif transport == "sse":
            logger.info(f"启动MCP FileSystem Server，传输协议: SSE")
            logger.info(f"服务器监听地址: http://{host}:{port}/sse")
            print(f"启动MCP FileSystem Server，传输协议: SSE")
            print(f"服务器监听地址: http://{host}:{port}/sse")
            mcp.run(transport="sse")

if __name__ == "__main__":
    main()
