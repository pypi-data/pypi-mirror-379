"""
文件创建模块 - 创建单个或多个文件
仅使用Python标准库，支持Windows、Linux、macOS
"""

import os
import platform
import stat
from typing import Dict, Any, Optional, Union


def file_create(path: str, content: Optional[Union[str, bytes]] = None, 
                encoding: str = 'utf-8', exist_ok: bool = False,
                mode: Optional[int] = None) -> Dict[str, Any]:
    """
    创建文件
    
    Args:
        path: 要创建的文件路径
        content: 文件内容，可以是字符串或字节（默认None，创建空文件）
        encoding: 文件编码（仅当content为字符串时有效，默认'utf-8'）
        exist_ok: 如果文件已存在，是否忽略错误（默认False）
        mode: 文件权限模式（仅Unix系统有效，默认None）
        
    Returns:
        Dict[str, Any]: 包含创建结果的字典，包含以下字段：
            - success: bool - 创建是否成功
            - path: str - 创建的文件的绝对路径
            - created: bool - 是否实际创建了文件（False表示文件已存在）
            - size: int - 文件大小（字节）
            - message: str - 操作结果描述
            - error: str - 错误信息（如果发生错误）
            - platform: str - 操作系统平台信息
    """
    result = {
        'success': False,
        'path': '',
        'created': False,
        'size': 0,
        'message': '',
        'error': '',
        'platform': platform.system()
    }
    
    if not path:
        result['error'] = '文件路径不能为空'
        return result
    
    try:
        # 获取绝对路径
        abs_path = os.path.abspath(path)
        result['path'] = abs_path
        
        # 检查文件是否已存在
        if os.path.exists(abs_path):
            if os.path.isfile(abs_path):
                if exist_ok:
                    result['success'] = True
                    result['created'] = False
                    result['size'] = os.path.getsize(abs_path) if os.path.exists(abs_path) else 0
                    result['message'] = f'文件已存在: {abs_path}'
                    return result
                else:
                    result['error'] = f'文件已存在: {abs_path}'
                    return result
            else:
                result['error'] = f'路径已存在但不是文件: {abs_path}'
                return result
        
        # 确保父目录存在
        parent_dir = os.path.dirname(abs_path)
        if parent_dir and not os.path.exists(parent_dir):
            try:
                os.makedirs(parent_dir, exist_ok=True)
            except OSError as e:
                result['error'] = f'无法创建父目录: {str(e)}'
                return result
        
        # 创建文件并写入内容
        if content is None:
            # 创建空文件
            with open(abs_path, 'w', encoding=encoding if isinstance(content, str) else None) as f:
                pass  # 空文件
            result['size'] = 0
        elif isinstance(content, str):
            # 写入字符串内容
            with open(abs_path, 'w', encoding=encoding) as f:
                f.write(content)
            result['size'] = len(content.encode(encoding))
        elif isinstance(content, bytes):
            # 写入字节内容
            with open(abs_path, 'wb') as f:
                f.write(content)
            result['size'] = len(content)
        else:
            result['error'] = f'不支持的内容类型: {type(content)}'
            return result
        
        result['success'] = True
        result['created'] = True
        result['message'] = f'文件创建成功: {abs_path} (大小: {result["size"]} 字节)'
        
        # 设置权限（如果指定了mode且不是Windows）
        if mode is not None and platform.system() != 'Windows':
            try:
                os.chmod(abs_path, mode)
            except OSError as e:
                result['message'] += f' (但权限设置失败: {str(e)})'
        
    except OSError as e:
        result['error'] = f'创建文件时发生系统错误: {str(e)}'
    except UnicodeEncodeError as e:
        result['error'] = f'编码错误: {str(e)}'
    except Exception as e:
        result['error'] = f'创建文件时发生未知错误: {str(e)}'
    
    return result


def file_create_simple(path: str) -> bool:
    """
    简化版文件创建函数
    
    Args:
        path: 要创建的文件路径
        
    Returns:
        bool: 创建是否成功
    """
    try:
        result = file_create(path, exist_ok=True)
        return result['success']
    except:
        return False


def create_temp_file(prefix: str = "temp_", suffix: str = ".txt",
                     content: Optional[Union[str, bytes]] = None,
                     encoding: str = 'utf-8') -> Dict[str, Any]:
    """
    创建临时文件
    
    Args:
        prefix: 文件名前缀
        suffix: 文件名后缀
        content: 文件内容（默认None，创建空文件）
        encoding: 文件编码（默认'utf-8'）
        
    Returns:
        Dict[str, Any]: 包含临时文件创建结果的字典
    """
    import tempfile
    
    result = {
        'success': False,
        'path': '',
        'created': False,
        'size': 0,
        'message': '',
        'error': '',
        'platform': platform.system()
    }
    
    try:
        # 创建临时文件
        with tempfile.NamedTemporaryFile(mode='w' if isinstance(content, str) else 'wb',
                                        prefix=prefix, suffix=suffix,
                                        delete=False, encoding=encoding if isinstance(content, str) else None) as f:
            temp_path = f.name
            
            if content is not None:
                if isinstance(content, str):
                    f.write(content)
                    result['size'] = len(content.encode(encoding))
                elif isinstance(content, bytes):
                    f.write(content)
                    result['size'] = len(content)
        
        result['success'] = True
        result['path'] = temp_path
        result['created'] = True
        result['message'] = f'临时文件创建成功: {temp_path} (大小: {result["size"]} 字节)'
        
    except Exception as e:
        result['error'] = f'创建临时文件时发生错误: {str(e)}'
    
    return result


def format_file_create(result: Dict[str, Any]) -> str:
    """
    格式化文件创建结果为可读字符串
    
    Args:
        result: 文件创建结果字典
        
    Returns:
        str: 格式化的创建结果字符串
    """
    if result.get('error'):
        return f"错误: {result['error']}"
    
    lines = []
    lines.append("=" * 60)
    lines.append("FILE CREATE RESULTS")
    lines.append("=" * 60)
    
    lines.append(f"目标路径: {result.get('path', 'Unknown')}")
    lines.append(f"操作状态: {'成功' if result.get('success') else '失败'}")
    lines.append(f"文件创建: {'是' if result.get('created') else '否（已存在）'}")
    lines.append(f"文件大小: {result.get('size', 0)} 字节")
    lines.append(f"平台: {result.get('platform', 'Unknown')}")
    
    if result.get('message'):
        lines.append(f"消息: {result['message']}")
    
    lines.append("=" * 60)
    return '\n'.join(lines)


def get_file_permissions(path: str) -> Dict[str, Any]:
    """
    获取文件权限信息
    
    Args:
        path: 文件路径
        
    Returns:
        Dict[str, Any]: 包含权限信息的字典
    """
    result = {
        'success': False,
        'path': '',
        'exists': False,
        'is_file': False,
        'permissions': '',
        'mode': 0,
        'size': 0,
        'error': ''
    }
    
    if not path:
        result['error'] = '文件路径不能为空'
        return result
    
    try:
        abs_path = os.path.abspath(path)
        result['path'] = abs_path
        
        if not os.path.exists(abs_path):
            result['error'] = f'文件不存在: {abs_path}'
            return result
        
        if not os.path.isfile(abs_path):
            result['error'] = f'路径不是文件: {abs_path}'
            return result
        
        # 获取权限和大小信息
        st = os.stat(abs_path)
        result['mode'] = st.st_mode
        result['permissions'] = stat.filemode(st.st_mode)
        result['size'] = st.st_size
        result['exists'] = True
        result['is_file'] = True
        result['success'] = True
        
    except Exception as e:
        result['error'] = f'获取文件权限时发生错误: {str(e)}'
    
    return result


if __name__ == "__main__":
    # 测试代码
    print("文件创建功能测试")
    print("=" * 60)
    
    # 清理之前的测试文件
    import shutil
    test_files = [
        "./test_file1.txt",
        "./test_file2.txt", 
        "./test_file3.txt",
        "./test_file5.txt",
        "./test_dir4"
    ]
    
    for file_path in test_files:
        if os.path.exists(file_path):
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
    
    # 测试用例
    test_cases = [
        ("./test_file1.txt", None, 'utf-8', False, None),           # 创建空文件
        ("./test_file2.txt", "Hello, World!", 'utf-8', False, None), # 创建带内容的文件
        ("./test_file3.txt", b"Binary content", 'utf-8', False, None), # 创建二进制文件
        ("./test_file1.txt", None, 'utf-8', False, None),           # 重复创建（应失败）
        ("./test_file1.txt", None, 'utf-8', True, None),            # 重复创建（exist_ok=True）
        ("", None, 'utf-8', False, None),                           # 空路径
        ("./test_dir4/test_file4.txt", "Nested file", 'utf-8', False, None), # 嵌套目录中的文件
        ("./test_file5.txt", "Permission test", 'utf-8', False, 0o644), # 创建带权限的文件
    ]
    
    for i, (path, content, encoding, exist_ok, mode) in enumerate(test_cases, 1):
        print(f"测试用例 {i}:")
        print(f"  路径: {path}")
        print(f"  内容: {type(content).__name__ if content is not None else 'None'}")
        print(f"  编码: {encoding}")
        print(f"  exist_ok: {exist_ok}")
        print(f"  mode: {mode}")
        
        result = file_create(path, content, encoding, exist_ok, mode)
        print(format_file_create(result))
        print()
    
    # 测试临时文件创建
    print("临时文件创建测试:")
    temp_result = create_temp_file(prefix="test_temp_", suffix=".txt", content="Temporary file content")
    print(format_file_create(temp_result))
    print()
    
    # 测试权限获取
    print("文件权限获取测试:")
    perm_result = get_file_permissions("./test_file1.txt")
    if perm_result['success']:
        print(f"权限: {perm_result['permissions']}")
        print(f"模式: {oct(perm_result['mode'])}")
        print(f"大小: {perm_result['size']} 字节")
    else:
        print(f"错误: {perm_result['error']}")