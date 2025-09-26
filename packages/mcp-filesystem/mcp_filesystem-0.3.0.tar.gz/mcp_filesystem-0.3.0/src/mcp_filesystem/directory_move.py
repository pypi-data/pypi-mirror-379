"""
目录移动模块 - 移动目录到新位置
仅使用Python标准库，支持Windows、Linux、macOS
"""

import os
import shutil
import platform
from typing import Dict, Any, Optional
import time


def directory_move(source_path: str, target_path: str, 
                  overwrite: bool = False, 
                  preserve_metadata: bool = True) -> Dict[str, Any]:
    """
    移动目录到新位置
    
    Args:
        source_path: 源目录路径
        target_path: 目标目录路径
        overwrite: 是否覆盖已存在的目标目录（默认False）
        preserve_metadata: 是否保留目录元数据（权限、时间戳等，默认True）
        
    Returns:
        Dict[str, Any]: 包含移动结果的字典，包含以下字段：
            - success: bool - 移动是否成功
            - source_path: str - 源目录绝对路径
            - target_path: str - 目标目录绝对路径
            - moved: bool - 是否实际执行了移动操作
            - overwrite: bool - 是否覆盖了现有目录
            - preserve_metadata: bool - 是否保留了元数据
            - files_moved: int - 移动的文件数量
            - directories_moved: int - 移动的目录数量
            - total_size: int - 移动的总字节数
            - message: str - 操作结果描述
            - error: str - 错误信息（如果发生错误）
            - platform: str - 操作系统平台信息
    """
    result = {
        'success': False,
        'source_path': '',
        'target_path': '',
        'moved': False,
        'overwrite': overwrite,
        'preserve_metadata': preserve_metadata,
        'files_moved': 0,
        'directories_moved': 0,
        'total_size': 0,
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
        
        # 检查是否尝试移动到自身或子目录
        if abs_target.startswith(abs_source + os.sep) or abs_target == abs_source:
            result['error'] = '不能将目录移动到自身或其子目录中'
            return result
        
        # 保存源目录的元数据（如果需要保留）
        source_stat = None
        if preserve_metadata:
            try:
                source_stat = os.stat(abs_source)
            except:
                # 如果无法获取元数据，继续操作但不保留元数据
                pass
        
        # 获取移动前的目录统计信息
        move_stats = _get_directory_stats(abs_source)
        result['files_moved'] = move_stats['files_count']
        result['directories_moved'] = move_stats['directories_count']
        result['total_size'] = move_stats['total_size']
        
        # 执行移动操作
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
                    result['message'] = '目录移动成功，但无法保留所有元数据'
        
        result['success'] = True
        result['moved'] = True
        result['message'] = f'目录移动成功: {abs_source} -> {abs_target}'
        
    except PermissionError as e:
        result['error'] = f'权限不足，无法移动目录: {str(e)}'
    except OSError as e:
        result['error'] = f'移动目录时发生系统错误: {str(e)}'
    except Exception as e:
        result['error'] = f'移动目录时发生未知错误: {str(e)}'
    
    return result


def _get_directory_stats(directory_path: str) -> Dict[str, int]:
    """
    获取目录的统计信息（文件数量、目录数量、总大小）
    
    Args:
        directory_path: 目录路径
        
    Returns:
        Dict[str, int]: 包含统计信息的字典
    """
    stats = {
        'files_count': 0,
        'directories_count': 0,
        'total_size': 0
    }
    
    try:
        for root, dirs, files in os.walk(directory_path):
            stats['directories_count'] += len(dirs)
            stats['files_count'] += len(files)
            
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    stats['total_size'] += os.path.getsize(file_path)
                except:
                    # 如果无法获取文件大小，跳过
                    pass
    except:
        # 如果无法遍历目录，返回基本统计
        pass
    
    return stats


def directory_move_simple(source_path: str, target_path: str) -> bool:
    """
    简化版目录移动函数
    
    Args:
        source_path: 源目录路径
        target_path: 目标目录路径
        
    Returns:
        bool: 移动是否成功
    """
    try:
        result = directory_move(source_path, target_path, overwrite=False, preserve_metadata=True)
        return result['success']
    except:
        return False


def safe_directory_move(source_path: str, target_path: str, 
                       max_retries: int = 3) -> Dict[str, Any]:
    """
    安全移动目录（带重试机制）
    
    Args:
        source_path: 源目录路径
        target_path: 目标目录路径
        max_retries: 最大重试次数（默认3次）
        
    Returns:
        Dict[str, Any]: 包含移动结果的字典
    """
    result = {
        'success': False,
        'source_path': '',
        'target_path': '',
        'moved': False,
        'retries': 0,
        'message': '',
        'error': ''
    }
    
    for attempt in range(max_retries):
        try:
            move_result = directory_move(source_path, target_path, overwrite=False, preserve_metadata=True)
            result.update(move_result)
            result['retries'] = attempt + 1
            
            if move_result['success']:
                return result
            
            # 如果移动失败但不是因为权限问题，等待后重试
            if "权限" not in move_result.get('error', ''):
                time.sleep(0.5)  # 等待500ms后重试
            else:
                break  # 权限问题不需要重试
                
        except Exception as e:
            result['error'] = f'第{attempt + 1}次尝试失败: {str(e)}'
            if attempt < max_retries - 1:
                time.sleep(0.5)
    
    return result


def format_directory_move(result: Dict[str, Any]) -> str:
    """
    格式化目录移动结果为可读字符串
    
    Args:
        result: 目录移动结果字典
        
    Returns:
        str: 格式化的移动结果字符串
    """
    if result.get('error'):
        return f"错误: {result['error']}"
    
    lines = []
    lines.append("=" * 60)
    lines.append("DIRECTORY MOVE RESULTS")
    lines.append("=" * 60)
    
    lines.append(f"源路径: {result.get('source_path', 'Unknown')}")
    lines.append(f"目标路径: {result.get('target_path', 'Unknown')}")
    lines.append(f"操作状态: {'成功' if result.get('success') else '失败'}")
    lines.append(f"目录移动: {'是' if result.get('moved') else '否'}")
    lines.append(f"文件数量: {result.get('files_moved', 0)}")
    lines.append(f"目录数量: {result.get('directories_moved', 0)}")
    lines.append(f"总大小: {_format_size(result.get('total_size', 0))}")
    lines.append(f"覆盖模式: {'是' if result.get('overwrite') else '否'}")
    lines.append(f"保留元数据: {'是' if result.get('preserve_metadata') else '否'}")
    lines.append(f"平台: {result.get('platform', 'Unknown')}")
    
    if result.get('retries'):
        lines.append(f"重试次数: {result['retries']}")
    
    if result.get('message'):
        lines.append(f"消息: {result['message']}")
    
    lines.append("=" * 60)
    return '\n'.join(lines)


def _format_size(size_bytes: int) -> str:
    """
    格式化文件大小
    
    Args:
        size_bytes: 字节大小
        
    Returns:
        str: 格式化后的大小字符串
    """
    if size_bytes == 0:
        return "0B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.2f}{size_names[i]}"


def batch_directory_move(move_list: list, overwrite: bool = False) -> Dict[str, Any]:
    """
    批量移动目录
    
    Args:
        move_list: 移动列表，每个元素为 (source_path, target_path) 元组
        overwrite: 是否覆盖已存在的目标目录
        
    Returns:
        Dict[str, Any]: 包含批量移动结果的字典
    """
    result = {
        'success': True,
        'total_count': len(move_list),
        'success_count': 0,
        'failed_count': 0,
        'total_files_moved': 0,
        'total_directories_moved': 0,
        'total_size': 0,
        'operations': [],
        'message': ''
    }
    
    if not move_list:
        result['message'] = '移动列表为空'
        return result
    
    for i, (source_path, target_path) in enumerate(move_list):
        operation_result = directory_move(source_path, target_path, overwrite)
        operation_result['index'] = i
        
        result['operations'].append(operation_result)
        
        if operation_result['success']:
            result['success_count'] += 1
            result['total_files_moved'] += operation_result.get('files_moved', 0)
            result['total_directories_moved'] += operation_result.get('directories_moved', 0)
            result['total_size'] += operation_result.get('total_size', 0)
        else:
            result['failed_count'] += 1
            result['success'] = False
    
    result['message'] = f'批量移动完成: 成功 {result["success_count"]}/{result["total_count"]}'
    
    return result


if __name__ == "__main__":
    # 测试代码
    print("目录移动功能测试")
    print("=" * 60)
    
    # 创建测试目录结构
    test_dirs = [
        "./test_move_source",
        "./test_move_source/sub1",
        "./test_move_source/sub1/sub2",
        "./test_move_source/sub3",
        "./test_move_target"
    ]
    
    # 创建测试目录和文件
    for test_dir in test_dirs:
        os.makedirs(test_dir, exist_ok=True)
    
    # 创建测试文件
    test_files = [
        "./test_move_source/file1.txt",
        "./test_move_source/sub1/file2.txt",
        "./test_move_source/sub1/sub2/file3.txt",
        "./test_move_source/sub3/file4.txt"
    ]
    
    for test_file in test_files:
        with open(test_file, "w") as f:
            f.write(f"这是 {test_file} 的测试内容")
    
    # 测试用例
    test_cases = [
        ("./test_move_source", "./test_move_dest1", False, True),      # 简单移动
        ("./test_move_dest1", "./test_move_dest2", True, True),       # 覆盖移动（目标不存在）
        ("./nonexistent_dir", "./test_move_dest3", False, True),      # 不存在的源目录
        ("", "./test_move_dest4", False, True),                       # 空源路径
        ("./test_move_dest2", "./test_move_dest2/sub1", False, True), # 移动到子目录（应该失败）
    ]
    
    for i, (source, target, overwrite, preserve_metadata) in enumerate(test_cases, 1):
        print(f"测试用例 {i}:")
        print(f"  源目录: {source}")
        print(f"  目标目录: {target}")
        print(f"  覆盖: {overwrite}")
        print(f"  保留元数据: {preserve_metadata}")
        
        result = directory_move(source, target, overwrite, preserve_metadata)
        print(format_directory_move(result))
        print()
    
    # 测试安全移动
    print("安全移动测试:")
    # 重新创建测试目录用于安全移动测试
    os.makedirs("./test_safe_move_source", exist_ok=True)
    with open("./test_safe_move_source/test.txt", "w") as f:
        f.write("安全移动测试内容")
    
    safe_result = safe_directory_move("./test_safe_move_source", "./test_safe_move_dest", max_retries=2)
    print(format_directory_move(safe_result))
    print()
    
    # 测试批量移动
    print("批量移动测试:")
    # 创建一些测试目录
    batch_sources = [
        "./batch_move_source1",
        "./batch_move_source2",
        "./batch_move_source3"
    ]
    
    for batch_source in batch_sources:
        os.makedirs(batch_source, exist_ok=True)
        with open(os.path.join(batch_source, "test.txt"), "w") as f:
            f.write(f"测试文件在 {batch_source}")
    
    batch_operations = [
        ("./batch_move_source1", "./batch_move_dest1"),
        ("./batch_move_source2", "./batch_move_dest2"),
        ("./batch_move_source3", "./batch_move_dest3")
    ]
    
    batch_result = batch_directory_move(batch_operations, overwrite=False)
    print(f"批量移动结果: {batch_result['message']}")
    print(f"成功: {batch_result['success_count']}, 失败: {batch_result['failed_count']}")
    print(f"总文件数: {batch_result['total_files_moved']}")
    print(f"总目录数: {batch_result['total_directories_moved']}")
    print(f"总大小: {_format_size(batch_result['total_size'])}")
    
    # 清理测试目录
    print("\n清理测试目录...")
    test_dirs_to_clean = [
        "./test_move_dest1", "./test_move_dest2", "./test_move_dest3",
        "./test_safe_move_dest", "./batch_move_dest1", "./batch_move_dest2", 
        "./batch_move_dest3"
    ]
    
    for clean_dir in test_dirs_to_clean:
        if os.path.exists(clean_dir):
            try:
                shutil.rmtree(clean_dir)
                print(f"已清理: {clean_dir}")
            except Exception as e:
                print(f"清理失败 {clean_dir}: {e}")
    
    print("\n测试完成！")