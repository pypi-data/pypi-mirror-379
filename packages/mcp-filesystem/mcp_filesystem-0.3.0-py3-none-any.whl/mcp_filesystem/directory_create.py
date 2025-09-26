"""
目录创建模块 - 创建单个或多个目录
仅使用Python标准库，支持Windows、Linux、macOS
"""

import os
import platform
import stat
from typing import Dict, Any, Optional


def directory_create(path: str, exist_ok: bool = False, mode: Optional[int] = None, 
                    parents: bool = True) -> Dict[str, Any]:
    """
    创建目录
    
    Args:
        path: 要创建的目录路径
        exist_ok: 如果目录已存在，是否忽略错误（默认False）
        mode: 目录权限模式（仅Unix系统有效，默认0o777）
        parents: 是否创建父目录（默认True）
        
    Returns:
        Dict[str, Any]: 包含创建结果的字典，包含以下字段：
            - success: bool - 创建是否成功
            - path: str - 创建的目录绝对路径
            - created: bool - 是否实际创建了目录（False表示目录已存在）
            - message: str - 操作结果描述
            - error: str - 错误信息（如果发生错误）
            - platform: str - 操作系统平台信息
    """
    result = {
        'success': False,
        'path': '',
        'created': False,
        'message': '',
        'error': '',
        'platform': platform.system()
    }
    
    if not path:
        result['error'] = '目录路径不能为空'
        return result
    
    try:
        # 获取绝对路径
        abs_path = os.path.abspath(path)
        result['path'] = abs_path
        
        # 检查目录是否已存在
        if os.path.exists(abs_path):
            if os.path.isdir(abs_path):
                if exist_ok:
                    result['success'] = True
                    result['created'] = False
                    result['message'] = f'目录已存在: {abs_path}'
                    return result
                else:
                    result['error'] = f'目录已存在: {abs_path}'
                    return result
            else:
                result['error'] = f'路径已存在但不是目录: {abs_path}'
                return result
        
        # 创建目录
        if parents:
            # 创建多级目录
            if mode is not None:
                os.makedirs(abs_path, mode=mode, exist_ok=exist_ok)
            else:
                os.makedirs(abs_path, exist_ok=exist_ok)
        else:
            # 只创建单级目录
            if mode is not None:
                os.mkdir(abs_path, mode=mode)
            else:
                os.mkdir(abs_path)
        
        result['success'] = True
        result['created'] = True
        result['message'] = f'目录创建成功: {abs_path}'
        
        # 设置权限（如果指定了mode且不是Windows）
        if mode is not None and platform.system() != 'Windows':
            try:
                os.chmod(abs_path, mode)
            except OSError as e:
                result['message'] += f' (但权限设置失败: {str(e)})'
        
    except OSError as e:
        result['error'] = f'创建目录时发生系统错误: {str(e)}'
    except Exception as e:
        result['error'] = f'创建目录时发生未知错误: {str(e)}'
    
    return result


def directory_create_simple(path: str) -> bool:
    """
    简化版目录创建函数
    
    Args:
        path: 要创建的目录路径
        
    Returns:
        bool: 创建是否成功
    """
    try:
        result = directory_create(path, exist_ok=True, parents=True)
        return result['success']
    except:
        return False


def create_temp_directory(prefix: str = "temp_", suffix: str = "", 
                         parent_dir: Optional[str] = None) -> Dict[str, Any]:
    """
    创建临时目录
    
    Args:
        prefix: 目录名前缀
        suffix: 目录名后缀
        parent_dir: 父目录路径（None表示系统临时目录）
        
    Returns:
        Dict[str, Any]: 包含临时目录创建结果的字典
    """
    import tempfile
    
    result = {
        'success': False,
        'path': '',
        'message': '',
        'error': ''
    }
    
    try:
        if parent_dir:
            # 确保父目录存在
            parent_result = directory_create(parent_dir, exist_ok=True, parents=True)
            if not parent_result['success']:
                result['error'] = f'无法创建父目录: {parent_result["error"]}'
                return result
        
        # 创建临时目录
        temp_dir = tempfile.mkdtemp(prefix=prefix, suffix=suffix, dir=parent_dir)
        result['success'] = True
        result['path'] = temp_dir
        result['message'] = f'临时目录创建成功: {temp_dir}'
        
    except Exception as e:
        result['error'] = f'创建临时目录时发生错误: {str(e)}'
    
    return result


def format_directory_create(result: Dict[str, Any]) -> str:
    """
    格式化目录创建结果为可读字符串
    
    Args:
        result: 目录创建结果字典
        
    Returns:
        str: 格式化的创建结果字符串
    """
    if result.get('error'):
        return f"错误: {result['error']}"
    
    lines = []
    lines.append("=" * 60)
    lines.append("DIRECTORY CREATE RESULTS")
    lines.append("=" * 60)
    
    lines.append(f"目标路径: {result.get('path', 'Unknown')}")
    lines.append(f"操作状态: {'成功' if result.get('success') else '失败'}")
    lines.append(f"目录创建: {'是' if result.get('created') else '否（已存在）'}")
    lines.append(f"平台: {result.get('platform', 'Unknown')}")
    
    if result.get('message'):
        lines.append(f"消息: {result['message']}")
    
    lines.append("=" * 60)
    return '\n'.join(lines)


def get_directory_permissions(path: str) -> Dict[str, Any]:
    """
    获取目录权限信息
    
    Args:
        path: 目录路径
        
    Returns:
        Dict[str, Any]: 包含权限信息的字典
    """
    result = {
        'success': False,
        'path': '',
        'exists': False,
        'is_directory': False,
        'permissions': '',
        'mode': 0,
        'error': ''
    }
    
    if not path:
        result['error'] = '目录路径不能为空'
        return result
    
    try:
        abs_path = os.path.abspath(path)
        result['path'] = abs_path
        
        if not os.path.exists(abs_path):
            result['error'] = f'目录不存在: {abs_path}'
            return result
        
        if not os.path.isdir(abs_path):
            result['error'] = f'路径不是目录: {abs_path}'
            return result
        
        # 获取权限信息
        st = os.stat(abs_path)
        result['mode'] = st.st_mode
        result['permissions'] = stat.filemode(st.st_mode)
        result['exists'] = True
        result['is_directory'] = True
        result['success'] = True
        
    except Exception as e:
        result['error'] = f'获取目录权限时发生错误: {str(e)}'
    
    return result


if __name__ == "__main__":
    # 测试代码
    print("目录创建功能测试")
    print("=" * 60)
    
    # 测试用例
    test_cases = [
        ("./test_dir1", False, None, True),      # 创建单级目录
        ("./test_dir2/sub1/sub2", True, None, True),  # 创建多级目录
        ("./test_dir1", False, None, True),      # 重复创建（应失败）
        ("./test_dir1", True, None, True),       # 重复创建（exist_ok=True）
        ("", False, None, True),                 # 空路径
        ("./test_dir3", False, 0o755, True),     # 创建带权限的目录
    ]
    
    for i, (path, exist_ok, mode, parents) in enumerate(test_cases, 1):
        print(f"测试用例 {i}:")
        print(f"  路径: {path}")
        print(f"  exist_ok: {exist_ok}")
        print(f"  mode: {mode}")
        print(f"  parents: {parents}")
        
        result = directory_create(path, exist_ok, mode, parents)
        print(format_directory_create(result))
        print()
    
    # 测试临时目录创建
    print("临时目录创建测试:")
    temp_result = create_temp_directory(prefix="test_temp_", parent_dir=".")
    print(format_directory_create(temp_result))
    print()
    
    # 测试权限获取
    print("目录权限获取测试:")
    perm_result = get_directory_permissions("./test_dir1")
    if perm_result['success']:
        print(f"权限: {perm_result['permissions']}")
        print(f"模式: {oct(perm_result['mode'])}")
    else:
        print(f"错误: {perm_result['error']}")