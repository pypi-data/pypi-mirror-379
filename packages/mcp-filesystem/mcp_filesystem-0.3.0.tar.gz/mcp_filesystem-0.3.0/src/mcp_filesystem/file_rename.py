"""
文件重命名模块 - 重命名单个或多个文件
仅使用Python标准库，支持Windows、Linux、macOS
"""

import os
import platform
import shutil
from typing import Dict, Any, List, Tuple


def file_rename(old_path: str, new_path: str, overwrite: bool = False) -> Dict[str, Any]:
    """
    重命名文件
    
    Args:
        old_path: 原文件路径
        new_path: 新文件路径
        overwrite: 是否覆盖已存在的目标文件（默认False）
        
    Returns:
        Dict[str, Any]: 包含重命名结果的字典，包含以下字段：
            - success: bool - 重命名是否成功
            - old_path: str - 原文件绝对路径
            - new_path: str - 新文件绝对路径
            - renamed: bool - 是否实际重命名了文件
            - overwrite: bool - 是否启用覆盖模式
            - message: str - 操作结果描述
            - error: str - 错误信息（如果发生错误）
            - platform: str - 操作系统平台信息
    """
    result = {
        'success': False,
        'old_path': '',
        'new_path': '',
        'renamed': False,
        'overwrite': overwrite,
        'message': '',
        'error': '',
        'platform': platform.system()
    }
    
    if not old_path or not new_path:
        result['error'] = '文件路径不能为空'
        return result
    
    try:
        # 获取绝对路径
        abs_old_path = os.path.abspath(old_path)
        abs_new_path = os.path.abspath(new_path)
        result['old_path'] = abs_old_path
        result['new_path'] = abs_new_path
        
        # 检查原文件是否存在
        if not os.path.exists(abs_old_path):
            result['error'] = f'原文件不存在: {abs_old_path}'
            return result
        
        # 检查原路径是否是文件
        if not os.path.isfile(abs_old_path):
            result['error'] = f'原路径不是文件: {abs_old_path}'
            return result
        
        # 检查新路径是否已存在
        if os.path.exists(abs_new_path):
            if overwrite:
                # 如果启用覆盖，检查新路径是否是文件
                if os.path.isfile(abs_new_path):
                    # 删除已存在的文件
                    os.remove(abs_new_path)
                else:
                    result['error'] = f'新路径已存在但不是文件: {abs_new_path}'
                    return result
            else:
                result['error'] = f'新路径已存在: {abs_new_path}'
                return result
        
        # 执行重命名操作
        os.rename(abs_old_path, abs_new_path)
        
        result['success'] = True
        result['renamed'] = True
        result['message'] = f'文件重命名成功: {abs_old_path} -> {abs_new_path}'
        
    except PermissionError as e:
        result['error'] = f'权限不足，无法重命名文件: {str(e)}'
    except OSError as e:
        result['error'] = f'重命名文件时发生系统错误: {str(e)}'
    except Exception as e:
        result['error'] = f'重命名文件时发生未知错误: {str(e)}'
    
    return result


def file_rename_simple(old_path: str, new_path: str) -> bool:
    """
    简化版文件重命名函数
    
    Args:
        old_path: 原文件路径
        new_path: 新文件路径
        
    Returns:
        bool: 重命名是否成功
    """
    try:
        result = file_rename(old_path, new_path, overwrite=False)
        return result['success']
    except:
        return False


def safe_file_rename(old_path: str, new_path: str, max_retries: int = 3) -> Dict[str, Any]:
    """
    安全重命名文件（带重试机制）
    
    Args:
        old_path: 原文件路径
        new_path: 新文件路径
        max_retries: 最大重试次数（默认3次）
        
    Returns:
        Dict[str, Any]: 包含重命名结果的字典
    """
    import time
    
    result = {
        'success': False,
        'old_path': '',
        'new_path': '',
        'renamed': False,
        'retries': 0,
        'message': '',
        'error': ''
    }
    
    for attempt in range(max_retries):
        try:
            rename_result = file_rename(old_path, new_path, overwrite=True)
            result.update(rename_result)
            result['retries'] = attempt + 1
            
            if rename_result['success']:
                return result
            
            # 如果重命名失败但不是因为权限问题，等待后重试
            if "权限" not in rename_result.get('error', ''):
                time.sleep(0.5)  # 等待500ms后重试
            else:
                break  # 权限问题不需要重试
                
        except Exception as e:
            result['error'] = f'第{attempt + 1}次尝试失败: {str(e)}'
            if attempt < max_retries - 1:
                time.sleep(0.5)
    
    return result


def format_file_rename(result: Dict[str, Any]) -> str:
    """
    格式化文件重命名结果为可读字符串
    
    Args:
        result: 文件重命名结果字典
        
    Returns:
        str: 格式化的重命名结果字符串
    """
    if result.get('error'):
        return f"错误: {result['error']}"
    
    lines = []
    lines.append("=" * 60)
    lines.append("FILE RENAME RESULTS")
    lines.append("=" * 60)
    
    lines.append(f"原路径: {result.get('old_path', 'Unknown')}")
    lines.append(f"新路径: {result.get('new_path', 'Unknown')}")
    lines.append(f"操作状态: {'成功' if result.get('success') else '失败'}")
    lines.append(f"文件重命名: {'是' if result.get('renamed') else '否'}")
    lines.append(f"覆盖模式: {'是' if result.get('overwrite') else '否'}")
    lines.append(f"平台: {result.get('platform', 'Unknown')}")
    
    if result.get('retries'):
        lines.append(f"重试次数: {result['retries']}")
    
    if result.get('message'):
        lines.append(f"消息: {result['message']}")
    
    lines.append("=" * 60)
    return '\n'.join(lines)


def rename_files(rename_list: List[Tuple[str, str]], overwrite: bool = False) -> Dict[str, Any]:
    """
    批量重命名文件
    
    Args:
        rename_list: 要重命名的文件路径元组列表，每个元组为 (原路径, 新路径)
        overwrite: 是否覆盖已存在的目标文件（默认False）
        
    Returns:
        Dict[str, Any]: 包含批量重命名结果的字典
    """
    result = {
        'success': True,
        'total_files': len(rename_list),
        'successful_renames': 0,
        'failed_renames': 0,
        'renamed_files': [],
        'failed_files': [],
        'message': '',
        'error': ''
    }
    
    if not rename_list:
        result['message'] = '文件列表为空'
        return result
    
    for old_path, new_path in rename_list:
        rename_result = file_rename(old_path, new_path, overwrite)
        
        if rename_result['success']:
            result['successful_renames'] += 1
            if rename_result['renamed']:
                result['renamed_files'].append((old_path, new_path))
        else:
            result['success'] = False
            result['failed_renames'] += 1
            result['failed_files'].append({
                'old_path': old_path,
                'new_path': new_path,
                'error': rename_result.get('error', '未知错误')
            })
    
    result['message'] = f'批量重命名完成: 成功 {result["successful_renames"]} 个，失败 {result["failed_renames"]} 个'
    
    return result


if __name__ == "__main__":
    # 测试代码
    print("文件重命名功能测试")
    print("=" * 60)
    
    # 创建测试文件
    test_files = [
        "./test_rename_file1.txt",
        "./test_rename_file2.txt",
        "./test_rename_file3.txt",
        "./test_rename_file4.txt"
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
        ("./test_rename_file1.txt", "./test_renamed_file1.txt", False),      # 正常重命名
        ("./test_rename_file2.txt", "./test_renamed_file2.txt", False),      # 正常重命名
        ("./nonexistent_file.txt", "./new_name.txt", False),                 # 重命名不存在的文件
        ("./test_rename_file3.txt", "./test_renamed_file2.txt", False),      # 新路径已存在（不覆盖）
        ("./test_rename_file3.txt", "./test_renamed_file2.txt", True),       # 新路径已存在（覆盖）
        ("./test_rename_file4.txt", "./test_renamed_file4.txt", False),      # 正常重命名
    ]
    
    for i, (old_path, new_path, overwrite) in enumerate(test_cases, 1):
        print(f"测试用例 {i}:")
        print(f"  原路径: {old_path}")
        print(f"  新路径: {new_path}")
        print(f"  覆盖: {overwrite}")
        
        result = file_rename(old_path, new_path, overwrite)
        print(format_file_rename(result))
        print()
    
    # 测试安全重命名
    print("安全重命名测试:")
    # 创建一个可能无法立即重命名的文件（模拟被占用）
    protected_file = "./test_protected_file.txt"
    new_protected_file = "./test_protected_renamed.txt"
    try:
        with open(protected_file, 'w') as f:
            f.write("受保护的文件内容")
    except:
        pass
    
    safe_result = safe_file_rename(protected_file, new_protected_file, max_retries=2)
    print(format_file_rename(safe_result))
    print()
    
    # 测试批量重命名
    print("批量重命名测试:")
    # 创建一些测试文件用于批量重命名
    batch_files = [
        ("./test_batch_file1.txt", "./test_batch_renamed1.txt"),
        ("./test_batch_file2.txt", "./test_batch_renamed2.txt"),
        ("./test_batch_file3.txt", "./test_batch_renamed3.txt")
    ]
    
    for old_path, new_path in batch_files:
        try:
            with open(old_path, 'w') as f:
                f.write(f"批量测试文件: {old_path}")
        except:
            pass
    
    batch_result = rename_files(batch_files + [("./nonexistent_batch.txt", "./new_batch.txt")], overwrite=True)
    print("批量重命名结果:")
    print(f"总文件数: {batch_result['total_files']}")
    print(f"成功重命名: {batch_result['successful_renames']}")
    print(f"失败重命名: {batch_result['failed_renames']}")
    print(f"消息: {batch_result['message']}")
    
    if batch_result['failed_files']:
        print("失败文件列表:")
        for failed in batch_result['failed_files']:
            print(f"  - {failed['old_path']} -> {failed['new_path']}: {failed['error']}")
    
    print("\n测试完成！")