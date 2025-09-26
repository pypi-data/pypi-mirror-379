"""
文件删除模块 - 删除单个或多个文件
仅使用Python标准库，支持Windows、Linux、macOS
"""

import os
import platform
from typing import Dict, Any, List


def file_delete(path: str, force: bool = False) -> Dict[str, Any]:
    """
    删除文件
    
    Args:
        path: 要删除的文件路径
        force: 是否强制删除（忽略部分错误，默认False）
        
    Returns:
        Dict[str, Any]: 包含删除结果的字典，包含以下字段：
            - success: bool - 删除是否成功
            - path: str - 删除的文件绝对路径
            - deleted: bool - 是否实际删除了文件（False表示文件不存在）
            - force: bool - 是否强制删除
            - message: str - 操作结果描述
            - error: str - 错误信息（如果发生错误）
            - platform: str - 操作系统平台信息
    """
    result = {
        'success': False,
        'path': '',
        'deleted': False,
        'force': force,
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
        
        # 检查文件是否存在
        if not os.path.exists(abs_path):
            if force:
                result['success'] = True
                result['deleted'] = False
                result['message'] = f'文件不存在（强制模式）: {abs_path}'
                return result
            else:
                result['error'] = f'文件不存在: {abs_path}'
                return result
        
        # 检查路径是否是文件
        if not os.path.isfile(abs_path):
            result['error'] = f'路径不是文件: {abs_path}'
            return result
        
        # 执行删除操作
        os.remove(abs_path)
        
        result['success'] = True
        result['deleted'] = True
        result['message'] = f'文件删除成功: {abs_path}'
        
    except PermissionError as e:
        result['error'] = f'权限不足，无法删除文件: {str(e)}'
    except OSError as e:
        if force:
            result['success'] = True
            result['deleted'] = False
            result['message'] = f'文件删除失败但强制模式忽略: {str(e)}'
        else:
            result['error'] = f'删除文件时发生系统错误: {str(e)}'
    except Exception as e:
        result['error'] = f'删除文件时发生未知错误: {str(e)}'
    
    return result


def file_delete_simple(path: str) -> bool:
    """
    简化版文件删除函数
    
    Args:
        path: 要删除的文件路径
        
    Returns:
        bool: 删除是否成功
    """
    try:
        result = file_delete(path, force=False)
        return result['success']
    except:
        return False


def safe_file_delete(path: str, max_retries: int = 3) -> Dict[str, Any]:
    """
    安全删除文件（带重试机制）
    
    Args:
        path: 要删除的文件路径
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
            delete_result = file_delete(path, force=False)
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


def format_file_delete(result: Dict[str, Any]) -> str:
    """
    格式化文件删除结果为可读字符串
    
    Args:
        result: 文件删除结果字典
        
    Returns:
        str: 格式化的删除结果字符串
    """
    if result.get('error'):
        return f"错误: {result['error']}"
    
    lines = []
    lines.append("=" * 60)
    lines.append("FILE DELETE RESULTS")
    lines.append("=" * 60)
    
    lines.append(f"目标路径: {result.get('path', 'Unknown')}")
    lines.append(f"操作状态: {'成功' if result.get('success') else '失败'}")
    lines.append(f"文件删除: {'是' if result.get('deleted') else '否（不存在或其他原因）'}")
    lines.append(f"强制模式: {'是' if result.get('force') else '否'}")
    lines.append(f"平台: {result.get('platform', 'Unknown')}")
    
    if result.get('retries'):
        lines.append(f"重试次数: {result['retries']}")
    
    if result.get('message'):
        lines.append(f"消息: {result['message']}")
    
    lines.append("=" * 60)
    return '\n'.join(lines)


def delete_files(file_list: List[str], force: bool = False) -> Dict[str, Any]:
    """
    批量删除文件
    
    Args:
        file_list: 要删除的文件路径列表
        force: 是否强制删除（默认False）
        
    Returns:
        Dict[str, Any]: 包含批量删除结果的字典
    """
    result = {
        'success': True,
        'total_files': len(file_list),
        'successful_deletes': 0,
        'failed_deletes': 0,
        'deleted_files': [],
        'failed_files': [],
        'message': '',
        'error': ''
    }
    
    if not file_list:
        result['message'] = '文件列表为空'
        return result
    
    for file_path in file_list:
        delete_result = file_delete(file_path, force)
        
        if delete_result['success']:
            result['successful_deletes'] += 1
            if delete_result['deleted']:
                result['deleted_files'].append(file_path)
        else:
            result['successful'] = False
            result['failed_deletes'] += 1
            result['failed_files'].append({
                'path': file_path,
                'error': delete_result.get('error', '未知错误')
            })
    
    result['message'] = f'批量删除完成: 成功 {result["successful_deletes"]} 个，失败 {result["failed_deletes"]} 个'
    
    return result


if __name__ == "__main__":
    # 测试代码
    print("文件删除功能测试")
    print("=" * 60)
    
    # 创建测试文件
    test_files = [
        "./test_delete_file1.txt",
        "./test_delete_file2.txt",
        "./test_delete_file3.txt",
        "./test_delete_file4.txt"
    ]
    
    # 创建测试文件
    for test_file in test_files:
        try:
            with open(test_file, 'w') as f:
                f.write(f"测试内容: {test_file}")
        except:
            pass  # 文件可能已存在
    
    # 测试用例
    test_cases = [
        ("./test_delete_file1.txt", False),      # 正常删除
        ("./test_delete_file2.txt", False),      # 正常删除
        ("./nonexistent_file.txt", True),        # 删除不存在的文件（强制模式）
        ("./nonexistent_file.txt", False),       # 删除不存在的文件（非强制模式）
        ("./test_delete_file3.txt", False),      # 正常删除
    ]
    
    for i, (path, force) in enumerate(test_cases, 1):
        print(f"测试用例 {i}:")
        print(f"  路径: {path}")
        print(f"  强制: {force}")
        
        result = file_delete(path, force)
        print(format_file_delete(result))
        print()
    
    # 测试安全删除
    print("安全删除测试:")
    # 创建一个可能无法立即删除的文件（模拟被占用）
    protected_file = "./test_delete_file4.txt"
    try:
        with open(protected_file, 'w') as f:
            f.write("受保护的文件内容")
    except:
        pass
    
    safe_result = safe_file_delete(protected_file, max_retries=2)
    print(format_file_delete(safe_result))
    print()
    
    # 测试批量删除
    print("批量删除测试:")
    # 创建一些测试文件用于批量删除
    batch_files = [
        "./test_batch_file1.txt",
        "./test_batch_file2.txt",
        "./test_batch_file3.txt"
    ]
    
    for batch_file in batch_files:
        try:
            with open(batch_file, 'w') as f:
                f.write(f"批量测试文件: {batch_file}")
        except:
            pass
    
    batch_result = delete_files(batch_files + ["./nonexistent_batch.txt"], force=True)
    print("批量删除结果:")
    print(f"总文件数: {batch_result['total_files']}")
    print(f"成功删除: {batch_result['successful_deletes']}")
    print(f"失败删除: {batch_result['failed_deletes']}")
    print(f"消息: {batch_result['message']}")
    
    if batch_result['failed_files']:
        print("失败文件列表:")
        for failed in batch_result['failed_files']:
            print(f"  - {failed['path']}: {failed['error']}")
    
    print("\n测试完成！")