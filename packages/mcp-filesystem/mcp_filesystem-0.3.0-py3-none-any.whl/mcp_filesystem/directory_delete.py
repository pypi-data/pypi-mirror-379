"""
目录删除模块 - 删除单个或多个目录
仅使用Python标准库，支持Windows、Linux、macOS
"""

import os
import shutil
import platform
from typing import Dict, Any, Optional


def directory_delete(path: str, recursive: bool = True, force: bool = False) -> Dict[str, Any]:
    """
    删除目录
    
    Args:
        path: 要删除的目录路径
        recursive: 是否递归删除目录内容（默认True）
        force: 是否强制删除（忽略部分错误，默认False）
        
    Returns:
        Dict[str, Any]: 包含删除结果的字典，包含以下字段：
            - success: bool - 删除是否成功
            - path: str - 删除的目录绝对路径
            - deleted: bool - 是否实际删除了目录（False表示目录不存在）
            - recursive: bool - 是否递归删除
            - force: bool - 是否强制删除
            - message: str - 操作结果描述
            - error: str - 错误信息（如果发生错误）
            - platform: str - 操作系统平台信息
    """
    result = {
        'success': False,
        'path': '',
        'deleted': False,
        'recursive': recursive,
        'force': force,
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
        
        # 检查目录是否存在
        if not os.path.exists(abs_path):
            if force:
                result['success'] = True
                result['deleted'] = False
                result['message'] = f'目录不存在（强制模式）: {abs_path}'
                return result
            else:
                result['error'] = f'目录不存在: {abs_path}'
                return result
        
        # 检查路径是否是目录
        if not os.path.isdir(abs_path):
            result['error'] = f'路径不是目录: {abs_path}'
            return result
        
        # 检查目录是否为空（如果不递归删除）
        if not recursive:
            try:
                if os.listdir(abs_path):
                    result['error'] = f'目录不为空，无法删除: {abs_path}'
                    return result
            except OSError as e:
                result['error'] = f'无法访问目录内容: {str(e)}'
                return result
        
        # 执行删除操作
        if recursive:
            shutil.rmtree(abs_path)
        else:
            os.rmdir(abs_path)
        
        result['success'] = True
        result['deleted'] = True
        result['message'] = f'目录删除成功: {abs_path}'
        
    except PermissionError as e:
        result['error'] = f'权限不足，无法删除目录: {str(e)}'
    except OSError as e:
        if force:
            result['success'] = True
            result['deleted'] = False
            result['message'] = f'目录删除失败但强制模式忽略: {str(e)}'
        else:
            result['error'] = f'删除目录时发生系统错误: {str(e)}'
    except Exception as e:
        result['error'] = f'删除目录时发生未知错误: {str(e)}'
    
    return result


def directory_delete_simple(path: str) -> bool:
    """
    简化版目录删除函数
    
    Args:
        path: 要删除的目录路径
        
    Returns:
        bool: 删除是否成功
    """
    try:
        result = directory_delete(path, recursive=True, force=False)
        return result['success']
    except:
        return False


def safe_directory_delete(path: str, max_retries: int = 3) -> Dict[str, Any]:
    """
    安全删除目录（带重试机制）
    
    Args:
        path: 要删除的目录路径
        max_retries: 最大重试次数（默认3次）
        
    Returns:
        Dict[str, Any]: 包含删除结果的字典
    """
    import time
    
    result = {
        'success': False,
        'path': '',
        'deleted': False,
        'retries': 0,
        'message': '',
        'error': ''
    }
    
    for attempt in range(max_retries):
        try:
            delete_result = directory_delete(path, recursive=True, force=False)
            result.update(delete_result)
            result['retries'] = attempt + 1
            
            if delete_result['success']:
                return result
            
            # 如果删除失败但不是因为权限问题，等待后重试
            if "权限" not in delete_result.get('error', ''):
                time.sleep(0.5)  # 等待500ms后重试
            else:
                break  # 权限问题不需要重试
                
        except Exception as e:
            result['error'] = f'第{attempt + 1}次尝试失败: {str(e)}'
            if attempt < max_retries - 1:
                time.sleep(0.5)
    
    return result


def format_directory_delete(result: Dict[str, Any]) -> str:
    """
    格式化目录删除结果为可读字符串
    
    Args:
        result: 目录删除结果字典
        
    Returns:
        str: 格式化的删除结果字符串
    """
    if result.get('error'):
        return f"错误: {result['error']}"
    
    lines = []
    lines.append("=" * 60)
    lines.append("DIRECTORY DELETE RESULTS")
    lines.append("=" * 60)
    
    lines.append(f"目标路径: {result.get('path', 'Unknown')}")
    lines.append(f"操作状态: {'成功' if result.get('success') else '失败'}")
    lines.append(f"目录删除: {'是' if result.get('deleted') else '否（不存在或其他原因）'}")
    lines.append(f"递归删除: {'是' if result.get('recursive') else '否'}")
    lines.append(f"强制模式: {'是' if result.get('force') else '否'}")
    lines.append(f"平台: {result.get('platform', 'Unknown')}")
    
    if result.get('retries'):
        lines.append(f"重试次数: {result['retries']}")
    
    if result.get('message'):
        lines.append(f"消息: {result['message']}")
    
    lines.append("=" * 60)
    return '\n'.join(lines)


def cleanup_empty_directories(root_path: str, remove_root: bool = False) -> Dict[str, Any]:
    """
    清理空目录
    
    Args:
        root_path: 根目录路径
        remove_root: 是否删除根目录本身（如果为空）
        
    Returns:
        Dict[str, Any]: 包含清理结果的字典
    """
    result = {
        'success': False,
        'root_path': '',
        'directories_removed': 0,
        'message': '',
        'error': ''
    }
    
    if not root_path:
        result['error'] = '根目录路径不能为空'
        return result
    
    try:
        abs_root = os.path.abspath(root_path)
        result['root_path'] = abs_root
        
        if not os.path.exists(abs_root) or not os.path.isdir(abs_root):
            result['error'] = f'根目录不存在或不是目录: {abs_root}'
            return result
        
        directories_removed = 0
        
        # 递归遍历目录树，从叶子节点开始删除空目录
        for root, dirs, files in os.walk(abs_root, topdown=False):
            # 跳过根目录（如果需要保留）
            if root == abs_root and not remove_root:
                continue
                
            # 如果目录为空，则删除
            if not dirs and not files:
                try:
                    os.rmdir(root)
                    directories_removed += 1
                except OSError:
                    # 目录不为空或无法删除，跳过
                    pass
        
        result['success'] = True
        result['directories_removed'] = directories_removed
        result['message'] = f'清理完成，删除了 {directories_removed} 个空目录'
        
    except Exception as e:
        result['error'] = f'清理空目录时发生错误: {str(e)}'
    
    return result


if __name__ == "__main__":
    # 测试代码
    print("目录删除功能测试")
    print("=" * 60)
    
    # 创建测试目录结构
    test_dirs = [
        "./test_delete_dir1",
        "./test_delete_dir2/sub1/sub2",
        "./test_delete_dir3",
        "./test_delete_dir4/protected"  # 可能无法删除的目录
    ]
    
    # 创建测试目录
    import tempfile
    temp_dir = tempfile.mkdtemp(prefix="test_temp_", dir=".")
    test_dirs.append(temp_dir)
    
    for test_dir in test_dirs:
        os.makedirs(test_dir, exist_ok=True)
        # 在部分目录中创建测试文件
        if "sub2" in test_dir:
            with open(os.path.join(test_dir, "test.txt"), "w") as f:
                f.write("test content")
    
    # 测试用例
    test_cases = [
        ("./test_delete_dir1", False, False),      # 删除空目录（非递归）
        ("./test_delete_dir2", True, False),       # 递归删除非空目录
        ("./nonexistent_dir", True, True),         # 删除不存在的目录（强制模式）
        ("./test_delete_dir3", False, False),      # 删除空目录
        (temp_dir, True, False),                   # 删除临时目录
    ]
    
    for i, (path, recursive, force) in enumerate(test_cases, 1):
        print(f"测试用例 {i}:")
        print(f"  路径: {path}")
        print(f"  递归: {recursive}")
        print(f"  强制: {force}")
        
        result = directory_delete(path, recursive, force)
        print(format_directory_delete(result))
        print()
    
    # 测试安全删除
    print("安全删除测试:")
    safe_result = safe_directory_delete("./test_delete_dir4", max_retries=2)
    print(format_directory_delete(safe_result))
    print()
    
    # 测试空目录清理
    print("空目录清理测试:")
    # 创建一些空目录用于测试
    os.makedirs("./test_cleanup/empty1/empty2", exist_ok=True)
    os.makedirs("./test_cleanup/non_empty", exist_ok=True)
    with open("./test_cleanup/non_empty/file.txt", "w") as f:
        f.write("test")
    
    cleanup_result = cleanup_empty_directories("./test_cleanup", remove_root=False)
    if cleanup_result['success']:
        print(f"清理结果: {cleanup_result['message']}")
    else:
        print(f"清理错误: {cleanup_result['error']}")
    
    print("\n测试完成！")