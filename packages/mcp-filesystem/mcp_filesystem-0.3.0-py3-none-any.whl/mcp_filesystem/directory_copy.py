"""
目录复制模块 - 复制目录及其所有内容
仅使用Python标准库，支持Windows、Linux、macOS
"""

import os
import shutil
import platform
import stat
from typing import Dict, Any, Optional, List
import time


def directory_copy(source_path: str, target_path: str, 
                  overwrite: bool = False, 
                  preserve_metadata: bool = True,
                  symlinks: bool = False,
                  ignore: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    复制目录及其所有内容到新位置
    
    Args:
        source_path: 源目录路径
        target_path: 目标目录路径
        overwrite: 是否覆盖已存在的目标目录（默认False）
        preserve_metadata: 是否保留文件和目录的元数据（权限、时间戳等，默认True）
        symlinks: 是否复制符号链接（默认False）
        ignore: 要忽略的文件/目录模式列表（默认None）
        
    Returns:
        Dict[str, Any]: 包含复制结果的字典，包含以下字段：
            - success: bool - 复制是否成功
            - source_path: str - 源目录绝对路径
            - target_path: str - 目标目录绝对路径
            - copied: bool - 是否实际执行了复制操作
            - files_copied: int - 复制的文件数量
            - directories_copied: int - 复制的目录数量
            - total_size: int - 复制的总字节数
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
        'copied': False,
        'files_copied': 0,
        'directories_copied': 0,
        'total_size': 0,
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
        
        # 检查是否尝试复制到自身或子目录
        if abs_target.startswith(abs_source + os.sep) or abs_target == abs_source:
            result['error'] = '不能将目录复制到自身或其子目录中'
            return result
        
        # 执行复制操作
        copy_stats = _copy_directory_tree(abs_source, abs_target, preserve_metadata, symlinks, ignore)
        
        result.update(copy_stats)
        result['success'] = True
        result['copied'] = True
        result['message'] = f'目录复制成功: {abs_source} -> {abs_target}'
        
    except PermissionError as e:
        result['error'] = f'权限不足，无法复制目录: {str(e)}'
    except OSError as e:
        result['error'] = f'复制目录时发生系统错误: {str(e)}'
    except Exception as e:
        result['error'] = f'复制目录时发生未知错误: {str(e)}'
    
    return result


def _copy_directory_tree(source: str, target: str, preserve_metadata: bool, 
                        symlinks: bool, ignore: Optional[List[str]]) -> Dict[str, Any]:
    """
    递归复制目录树
    
    Args:
        source: 源目录路径
        target: 目标目录路径
        preserve_metadata: 是否保留元数据
        symlinks: 是否复制符号链接
        ignore: 忽略模式列表
        
    Returns:
        Dict[str, Any]: 复制统计信息
    """
    stats = {
        'files_copied': 0,
        'directories_copied': 0,
        'total_size': 0
    }
    
    # 创建目标目录
    os.makedirs(target, exist_ok=True)
    stats['directories_copied'] += 1
    
    # 保存源目录的元数据（如果需要保留）
    source_stat = None
    if preserve_metadata:
        try:
            source_stat = os.stat(source)
            # 恢复目录权限和时间戳
            if platform.system() != 'Windows':
                os.chmod(target, source_stat.st_mode)
            os.utime(target, (source_stat.st_atime, source_stat.st_mtime))
        except:
            pass  # 如果无法保留元数据，继续操作
    
    # 遍历源目录
    for item in os.listdir(source):
        source_item = os.path.join(source, item)
        target_item = os.path.join(target, item)
        
        # 检查是否应该忽略此项目
        if ignore and _should_ignore(item, ignore):
            continue
        
        if os.path.isdir(source_item):
            # 递归复制子目录
            sub_stats = _copy_directory_tree(source_item, target_item, preserve_metadata, symlinks, ignore)
            stats['files_copied'] += sub_stats['files_copied']
            stats['directories_copied'] += sub_stats['directories_copied']
            stats['total_size'] += sub_stats['total_size']
        else:
            # 复制文件
            file_stats = _copy_file(source_item, target_item, preserve_metadata, symlinks)
            stats['files_copied'] += file_stats['files_copied']
            stats['total_size'] += file_stats['total_size']
    
    return stats


def _copy_file(source: str, target: str, preserve_metadata: bool, symlinks: bool) -> Dict[str, Any]:
    """
    复制单个文件
    
    Args:
        source: 源文件路径
        target: 目标文件路径
        preserve_metadata: 是否保留元数据
        symlinks: 是否复制符号链接
        
    Returns:
        Dict[str, Any]: 文件复制统计信息
    """
    stats = {
        'files_copied': 0,
        'total_size': 0
    }
    
    try:
        if symlinks and os.path.islink(source):
            # 复制符号链接
            linkto = os.readlink(source)
            os.symlink(linkto, target)
        else:
            # 复制文件内容
            shutil.copy2(source, target) if preserve_metadata else shutil.copy(source, target)
        
        # 获取文件大小
        try:
            file_size = os.path.getsize(source)
            stats['total_size'] = file_size
        except:
            file_size = 0
        
        stats['files_copied'] = 1
        
    except Exception:
        # 如果文件复制失败，跳过此文件
        pass
    
    return stats


def _should_ignore(item: str, ignore_patterns: List[str]) -> bool:
    """
    检查项目是否应该被忽略
    
    Args:
        item: 项目名称
        ignore_patterns: 忽略模式列表
        
    Returns:
        bool: 是否应该忽略
    """
    for pattern in ignore_patterns:
        if pattern in item or fnmatch.fnmatch(item, pattern):
            return True
    return False


def directory_copy_simple(source_path: str, target_path: str) -> bool:
    """
    简化版目录复制函数
    
    Args:
        source_path: 源目录路径
        target_path: 目标目录路径
        
    Returns:
        bool: 复制是否成功
    """
    try:
        result = directory_copy(source_path, target_path, overwrite=False, preserve_metadata=True)
        return result['success']
    except:
        return False


def safe_directory_copy(source_path: str, target_path: str, 
                       max_retries: int = 3) -> Dict[str, Any]:
    """
    安全复制目录（带重试机制）
    
    Args:
        source_path: 源目录路径
        target_path: 目标目录路径
        max_retries: 最大重试次数（默认3次）
        
    Returns:
        Dict[str, Any]: 包含复制结果的字典
    """
    result = {
        'success': False,
        'source_path': '',
        'target_path': '',
        'copied': False,
        'retries': 0,
        'message': '',
        'error': ''
    }
    
    for attempt in range(max_retries):
        try:
            copy_result = directory_copy(source_path, target_path, overwrite=False, preserve_metadata=True)
            result.update(copy_result)
            result['retries'] = attempt + 1
            
            if copy_result['success']:
                return result
            
            # 如果复制失败但不是因为权限问题，等待后重试
            if "权限" not in copy_result.get('error', ''):
                time.sleep(0.5)  # 等待500ms后重试
            else:
                break  # 权限问题不需要重试
                
        except Exception as e:
            result['error'] = f'第{attempt + 1}次尝试失败: {str(e)}'
            if attempt < max_retries - 1:
                time.sleep(0.5)
    
    return result


def format_directory_copy(result: Dict[str, Any]) -> str:
    """
    格式化目录复制结果为可读字符串
    
    Args:
        result: 目录复制结果字典
        
    Returns:
        str: 格式化的复制结果字符串
    """
    if result.get('error'):
        return f"错误: {result['error']}"
    
    lines = []
    lines.append("=" * 60)
    lines.append("DIRECTORY COPY RESULTS")
    lines.append("=" * 60)
    
    lines.append(f"源路径: {result.get('source_path', 'Unknown')}")
    lines.append(f"目标路径: {result.get('target_path', 'Unknown')}")
    lines.append(f"操作状态: {'成功' if result.get('success') else '失败'}")
    lines.append(f"目录复制: {'是' if result.get('copied') else '否'}")
    lines.append(f"文件数量: {result.get('files_copied', 0)}")
    lines.append(f"目录数量: {result.get('directories_copied', 0)}")
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


def batch_directory_copy(copy_list: list, overwrite: bool = False) -> Dict[str, Any]:
    """
    批量复制目录
    
    Args:
        copy_list: 复制列表，每个元素为 (source_path, target_path) 元组
        overwrite: 是否覆盖已存在的目标目录
        
    Returns:
        Dict[str, Any]: 包含批量复制结果的字典
    """
    result = {
        'success': True,
        'total_count': len(copy_list),
        'success_count': 0,
        'failed_count': 0,
        'total_files_copied': 0,
        'total_directories_copied': 0,
        'total_size': 0,
        'operations': [],
        'message': ''
    }
    
    if not copy_list:
        result['message'] = '复制列表为空'
        return result
    
    for i, (source_path, target_path) in enumerate(copy_list):
        operation_result = directory_copy(source_path, target_path, overwrite)
        operation_result['index'] = i
        
        result['operations'].append(operation_result)
        
        if operation_result['success']:
            result['success_count'] += 1
            result['total_files_copied'] += operation_result.get('files_copied', 0)
            result['total_directories_copied'] += operation_result.get('directories_copied', 0)
            result['total_size'] += operation_result.get('total_size', 0)
        else:
            result['failed_count'] += 1
            result['success'] = False
    
    result['message'] = f'批量复制完成: 成功 {result["success_count"]}/{result["total_count"]}'
    
    return result


# 导入fnmatch用于模式匹配（在函数中使用）
import fnmatch


if __name__ == "__main__":
    # 测试代码
    print("目录复制功能测试")
    print("=" * 60)
    
    # 创建测试目录结构
    test_dirs = [
        "./test_copy_source",
        "./test_copy_source/sub1",
        "./test_copy_source/sub1/sub2",
        "./test_copy_source/sub3",
        "./test_copy_target"
    ]
    
    # 创建测试目录和文件
    for test_dir in test_dirs:
        os.makedirs(test_dir, exist_ok=True)
    
    # 创建测试文件
    test_files = [
        "./test_copy_source/file1.txt",
        "./test_copy_source/sub1/file2.txt",
        "./test_copy_source/sub1/sub2/file3.txt",
        "./test_copy_source/sub3/file4.txt"
    ]
    
    for test_file in test_files:
        with open(test_file, "w") as f:
            f.write(f"这是 {test_file} 的测试内容")
    
    # 测试用例
    test_cases = [
        ("./test_copy_source", "./test_copy_dest1", False, True),      # 简单复制
        ("./test_copy_source", "./test_copy_dest2", True, True),       # 覆盖复制（目标不存在）
        ("./nonexistent_dir", "./test_copy_dest3", False, True),       # 不存在的源目录
        ("", "./test_copy_dest4", False, True),                        # 空源路径
        ("./test_copy_source", "./test_copy_source/sub1", False, True), # 复制到子目录（应该失败）
    ]
    
    for i, (source, target, overwrite, preserve_metadata) in enumerate(test_cases, 1):
        print(f"测试用例 {i}:")
        print(f"  源目录: {source}")
        print(f"  目标目录: {target}")
        print(f"  覆盖: {overwrite}")
        print(f"  保留元数据: {preserve_metadata}")
        
        result = directory_copy(source, target, overwrite, preserve_metadata)
        print(format_directory_copy(result))
        print()
    
    # 测试安全复制
    print("安全复制测试:")
    safe_result = safe_directory_copy("./test_copy_source", "./test_copy_safe_dest", max_retries=2)
    print(format_directory_copy(safe_result))
    print()
    
    # 测试批量复制
    print("批量复制测试:")
    # 创建一些测试目录
    batch_sources = [
        "./batch_source1",
        "./batch_source2",
        "./batch_source3"
    ]
    
    for batch_source in batch_sources:
        os.makedirs(batch_source, exist_ok=True)
        with open(os.path.join(batch_source, "test.txt"), "w") as f:
            f.write(f"测试文件在 {batch_source}")
    
    batch_operations = [
        ("./batch_source1", "./batch_dest1"),
        ("./batch_source2", "./batch_dest2"),
        ("./batch_source3", "./batch_dest3")
    ]
    
    batch_result = batch_directory_copy(batch_operations, overwrite=False)
    print(f"批量复制结果: {batch_result['message']}")
    print(f"成功: {batch_result['success_count']}, 失败: {batch_result['failed_count']}")
    print(f"总文件数: {batch_result['total_files_copied']}")
    print(f"总目录数: {batch_result['total_directories_copied']}")
    print(f"总大小: {_format_size(batch_result['total_size'])}")
    
    # 清理测试目录
    print("\n清理测试目录...")
    import shutil
    test_dirs_to_clean = [
        "./test_copy_source", "./test_copy_dest1", "./test_copy_dest2",
        "./test_copy_safe_dest", "./batch_source1", "./batch_source2", 
        "./batch_source3", "./batch_dest1", "./batch_dest2", "./batch_dest3"
    ]
    
    for clean_dir in test_dirs_to_clean:
        if os.path.exists(clean_dir):
            try:
                shutil.rmtree(clean_dir)
                print(f"已清理: {clean_dir}")
            except Exception as e:
                print(f"清理失败 {clean_dir}: {e}")
    
    print("\n测试完成！")