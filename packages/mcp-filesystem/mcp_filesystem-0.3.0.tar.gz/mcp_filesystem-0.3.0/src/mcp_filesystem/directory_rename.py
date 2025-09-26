"""
目录重命名模块 - 重命名或移动目录
仅使用Python标准库，支持Windows、Linux、macOS
"""

import os
import shutil
import platform
from typing import Dict, Any, Optional


def directory_rename(source_path: str, target_path: str, 
                    overwrite: bool = False, 
                    preserve_metadata: bool = True) -> Dict[str, Any]:
    """
    重命名或移动目录
    
    Args:
        source_path: 源目录路径
        target_path: 目标目录路径
        overwrite: 是否覆盖已存在的目标目录（默认False）
        preserve_metadata: 是否保留目录元数据（权限、时间戳等，默认True）
        
    Returns:
        Dict[str, Any]: 包含重命名结果的字典，包含以下字段：
            - success: bool - 重命名是否成功
            - source_path: str - 源目录绝对路径
            - target_path: str - 目标目录绝对路径
            - renamed: bool - 是否实际执行了重命名操作
            - operation: str - 执行的操作类型（'rename' 或 'move'）
            - overwrite: bool - 是否覆盖了现有目录
            - preserve_metadata: bool - 是否保留了元数据
            - message: str - 操作结果描述
            - error: str - 错误信息（如果发生错误）
            - platform: str - 操作系统平台信息
    """
    result = {
        'success': False,
        'source_path': '',
        'target_path': '',
        'renamed': False,
        'operation': '',
        'overwrite': overwrite,
        'preserve_metadata': preserve_metadata,
        'message': '',
        'error': '',
        'platform': platform.system()
    }
    
    if not source_path:
        result['error'] = '源目录路径不能为空'
        return result
    
    if not target_path:
        result['error'] = '目标目录路径不能为空'
        return result
    
    try:
        # 获取绝对路径
        abs_source = os.path.abspath(source_path)
        abs_target = os.path.abspath(target_path)
        result['source_path'] = abs_source
        result['target_path'] = abs_target
        
        # 检查源目录是否存在
        if not os.path.exists(abs_source):
            result['error'] = f'源目录不存在: {abs_source}'
            return result
        
        # 检查源路径是否是目录
        if not os.path.isdir(abs_source):
            result['error'] = f'源路径不是目录: {abs_source}'
            return result
        
        # 检查目标路径是否已存在
        if os.path.exists(abs_target):
            if os.path.isdir(abs_target):
                if overwrite:
                    # 如果允许覆盖，先删除目标目录
                    try:
                        shutil.rmtree(abs_target)
                        result['overwrite'] = True
                    except Exception as e:
                        result['error'] = f'无法删除已存在的目标目录: {str(e)}'
                        return result
                else:
                    result['error'] = f'目标目录已存在: {abs_target}'
                    return result
            else:
                result['error'] = f'目标路径已存在但不是目录: {abs_target}'
                return result
        
        # 保存源目录的元数据（如果需要保留）
        source_stat = None
        if preserve_metadata:
            try:
                source_stat = os.stat(abs_source)
            except:
                # 如果无法获取元数据，继续操作但不保留元数据
                pass
        
        # 确定操作类型（重命名或移动）
        source_parent = os.path.normpath(os.path.dirname(abs_source))
        target_parent = os.path.normpath(os.path.dirname(abs_target))
        
        if source_parent == target_parent:
            result['operation'] = 'rename'
            # 在同一目录下重命名，使用os.rename
            os.rename(abs_source, abs_target)
        else:
            result['operation'] = 'move'
            # 跨目录移动，使用shutil.move
            shutil.move(abs_source, abs_target)
        
        # 如果需要保留元数据，尝试恢复源目录的权限和时间戳
        if preserve_metadata and source_stat is not None:
            try:
                # 恢复权限（仅Unix系统有效）
                if platform.system() != 'Windows':
                    os.chmod(abs_target, source_stat.st_mode)
                # 恢复时间戳
                os.utime(abs_target, (source_stat.st_atime, source_stat.st_mtime))
            except:
                # 如果无法保留元数据，记录警告但不视为错误
                if not result['message']:
                    result['message'] = '目录重命名成功，但无法保留所有元数据'
        
        result['success'] = True
        result['renamed'] = True
        result['message'] = f'目录{result["operation"]}成功: {abs_source} -> {abs_target}'
        
    except PermissionError as e:
        result['error'] = f'权限不足，无法重命名目录: {str(e)}'
    except OSError as e:
        result['error'] = f'重命名目录时发生系统错误: {str(e)}'
    except Exception as e:
        result['error'] = f'重命名目录时发生未知错误: {str(e)}'
    
    return result


def directory_rename_simple(source_path: str, target_path: str) -> bool:
    """
    简化版目录重命名函数
    
    Args:
        source_path: 源目录路径
        target_path: 目标目录路径
        
    Returns:
        bool: 重命名是否成功
    """
    try:
        result = directory_rename(source_path, target_path, overwrite=False, preserve_metadata=True)
        return result['success']
    except:
        return False


def directory_move(source_path: str, target_path: str, 
                  overwrite: bool = False) -> Dict[str, Any]:
    """
    移动目录到新位置（directory_rename的别名）
    
    Args:
        source_path: 源目录路径
        target_path: 目标目录路径
        overwrite: 是否覆盖已存在的目标目录
        
    Returns:
        Dict[str, Any]: 包含移动结果的字典
    """
    return directory_rename(source_path, target_path, overwrite, preserve_metadata=True)


def safe_directory_rename(source_path: str, target_path: str, 
                         max_retries: int = 3) -> Dict[str, Any]:
    """
    安全重命名目录（带重试机制）
    
    Args:
        source_path: 源目录路径
        target_path: 目标目录路径
        max_retries: 最大重试次数（默认3次）
        
    Returns:
        Dict[str, Any]: 包含重命名结果的字典
    """
    import time
    
    result = {
        'success': False,
        'source_path': '',
        'target_path': '',
        'renamed': False,
        'retries': 0,
        'message': '',
        'error': ''
    }
    
    for attempt in range(max_retries):
        try:
            rename_result = directory_rename(source_path, target_path, overwrite=False, preserve_metadata=True)
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


def format_directory_rename(result: Dict[str, Any]) -> str:
    """
    格式化目录重命名结果为可读字符串
    
    Args:
        result: 目录重命名结果字典
        
    Returns:
        str: 格式化的重命名结果字符串
    """
    if result.get('error'):
        return f"错误: {result['error']}"
    
    lines = []
    lines.append("=" * 60)
    lines.append("DIRECTORY RENAME RESULTS")
    lines.append("=" * 60)
    
    lines.append(f"源路径: {result.get('source_path', 'Unknown')}")
    lines.append(f"目标路径: {result.get('target_path', 'Unknown')}")
    lines.append(f"操作状态: {'成功' if result.get('success') else '失败'}")
    lines.append(f"目录重命名: {'是' if result.get('renamed') else '否'}")
    lines.append(f"操作类型: {result.get('operation', 'Unknown')}")
    lines.append(f"覆盖模式: {'是' if result.get('overwrite') else '否'}")
    lines.append(f"保留元数据: {'是' if result.get('preserve_metadata') else '否'}")
    lines.append(f"平台: {result.get('platform', 'Unknown')}")
    
    if result.get('retries'):
        lines.append(f"重试次数: {result['retries']}")
    
    if result.get('message'):
        lines.append(f"消息: {result['message']}")
    
    lines.append("=" * 60)
    return '\n'.join(lines)


def batch_directory_rename(rename_list: list, overwrite: bool = False) -> Dict[str, Any]:
    """
    批量重命名目录
    
    Args:
        rename_list: 重命名列表，每个元素为 (source_path, target_path) 元组
        overwrite: 是否覆盖已存在的目标目录
        
    Returns:
        Dict[str, Any]: 包含批量重命名结果的字典
    """
    result = {
        'success': True,
        'total_count': len(rename_list),
        'success_count': 0,
        'failed_count': 0,
        'operations': [],
        'message': ''
    }
    
    if not rename_list:
        result['message'] = '重命名列表为空'
        return result
    
    for i, (source_path, target_path) in enumerate(rename_list):
        operation_result = directory_rename(source_path, target_path, overwrite)
        operation_result['index'] = i
        
        result['operations'].append(operation_result)
        
        if operation_result['success']:
            result['success_count'] += 1
        else:
            result['failed_count'] += 1
            result['success'] = False
    
    result['message'] = f'批量重命名完成: 成功 {result["success_count"]}/{result["total_count"]}'
    
    return result


if __name__ == "__main__":
    # 测试代码
    print("目录重命名功能测试")
    print("=" * 60)
    
    # 创建测试目录
    test_dirs = [
        "./test_rename_dir1",
        "./test_rename_dir2/sub1",
        "./test_rename_dir3",
        "./test_rename_target"
    ]
    
    for test_dir in test_dirs:
        os.makedirs(test_dir, exist_ok=True)
    
    # 在部分目录中创建测试文件
    with open("./test_rename_dir2/sub1/test.txt", "w") as f:
        f.write("test content")
    
    # 测试用例
    test_cases = [
        ("./test_rename_dir1", "./test_renamed_dir1", False),      # 简单重命名
        ("./test_rename_dir2", "./new_location/test_moved_dir2", False),  # 移动到新目录
        ("./test_rename_dir3", "./test_renamed_dir3", False),      # 另一个重命名
        ("./test_renamed_dir1", "./test_rename_target", True),     # 覆盖已存在的目录
        ("./nonexistent_dir", "./new_dir", False),                 # 不存在的源目录
        ("./test_moved_dir2", "./test_rename_target", False),      # 目标目录已存在（不允许覆盖）
    ]
    
    for i, (source, target, overwrite) in enumerate(test_cases, 1):
        print(f"测试用例 {i}:")
        print(f"  源目录: {source}")
        print(f"  目标目录: {target}")
        print(f"  覆盖: {overwrite}")
        
        result = directory_rename(source, target, overwrite)
        print(format_directory_rename(result))
        print()
    
    # 测试安全重命名
    print("安全重命名测试:")
    safe_result = safe_directory_rename("./test_renamed_dir3", "./test_safe_renamed", max_retries=2)
    print(format_directory_rename(safe_result))
    print()
    
    # 测试批量重命名
    print("批量重命名测试:")
    # 创建一些测试目录
    batch_dirs = [
        "./batch_test1",
        "./batch_test2",
        "./batch_test3"
    ]
    
    for batch_dir in batch_dirs:
        os.makedirs(batch_dir, exist_ok=True)
    
    batch_operations = [
        ("./batch_test1", "./batch_renamed1"),
        ("./batch_test2", "./batch_renamed2"),
        ("./batch_test3", "./batch_renamed3")
    ]
    
    batch_result = batch_directory_rename(batch_operations, overwrite=False)
    print(f"批量重命名结果: {batch_result['message']}")
    print(f"成功: {batch_result['success_count']}, 失败: {batch_result['failed_count']}")
    
    # 清理测试目录
    print("\n清理测试目录...")
    import shutil
    test_dirs_to_clean = [
        "./test_renamed_dir1", "./test_moved_dir2", "./test_safe_renamed",
        "./test_rename_target", "./batch_renamed1", "./batch_renamed2", "./batch_renamed3"
    ]
    
    for clean_dir in test_dirs_to_clean:
        if os.path.exists(clean_dir):
            try:
                shutil.rmtree(clean_dir)
                print(f"已清理: {clean_dir}")
            except Exception as e:
                print(f"清理失败 {clean_dir}: {e}")
    
    print("\n测试完成！")