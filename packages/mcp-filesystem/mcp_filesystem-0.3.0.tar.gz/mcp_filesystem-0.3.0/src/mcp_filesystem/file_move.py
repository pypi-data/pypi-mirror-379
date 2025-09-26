"""
文件移动模块 - 移动单个或多个文件到新位置
仅使用Python标准库，支持Windows、Linux、macOS
"""

import os
import shutil
import platform
import time
from typing import Dict, Any, List, Tuple


def file_move(source_path: str, target_path: str, 
             overwrite: bool = False, 
             preserve_metadata: bool = True) -> Dict[str, Any]:
    """
    移动文件到新位置
    
    Args:
        source_path: 源文件路径
        target_path: 目标文件路径
        overwrite: 是否覆盖已存在的目标文件（默认False）
        preserve_metadata: 是否保留文件的元数据（权限、时间戳等，默认True）
        
    Returns:
        Dict[str, Any]: 包含移动结果的字典，包含以下字段：
            - success: bool - 移动是否成功
            - source_path: str - 源文件绝对路径
            - target_path: str - 目标文件绝对路径
            - moved: bool - 是否实际执行了移动操作
            - size: int - 文件大小（字节）
            - overwrite: bool - 是否覆盖了现有文件
            - preserve_metadata: bool - 是否保留了元数据
            - message: str - 操作结果描述
            - error: str - 错误信息（如果发生错误）
            - platform: str - 操作系统平台信息
    """
    result = {
        'success': False,
        'source_path': '',
        'target_path': '',
        'moved': False,
        'size': 0,
        'overwrite': overwrite,
        'preserve_metadata': preserve_metadata,
        'message': '',
        'error': '',
        'platform': platform.system()
    }
    
    if not source_path:
        result['error'] = '源文件路径不能为空'
        return result
    
    if not target_path:
        result['error'] = '目标文件路径不能为空'
        return result
    
    try:
        # 获取绝对路径
        abs_source = os.path.abspath(source_path)
        abs_target = os.path.abspath(target_path)
        result['source_path'] = abs_source
        result['target_path'] = abs_target
        
        # 检查源文件是否存在
        if not os.path.exists(abs_source):
            result['error'] = f'源文件不存在: {abs_source}'
            return result
        
        # 检查源路径是否是文件
        if not os.path.isfile(abs_source):
            result['error'] = f'源路径不是文件: {abs_source}'
            return result
        
        # 检查目标路径是否已存在
        if os.path.exists(abs_target):
            if overwrite:
                # 如果启用覆盖，检查目标路径是否是文件
                if os.path.isfile(abs_target):
                    # 删除已存在的文件
                    try:
                        os.remove(abs_target)
                        result['overwrite'] = True
                    except Exception as e:
                        result['error'] = f'无法删除已存在的目标文件: {str(e)}'
                        return result
                else:
                    result['error'] = f'目标路径已存在但不是文件: {abs_target}'
                    return result
            else:
                result['error'] = f'目标文件已存在: {abs_target}'
                return result
        
        # 确保目标目录存在
        target_dir = os.path.dirname(abs_target)
        if target_dir and not os.path.exists(target_dir):
            try:
                os.makedirs(target_dir, exist_ok=True)
            except OSError as e:
                result['error'] = f'无法创建目标目录: {str(e)}'
                return result
        
        # 保存源文件的元数据（如果需要保留）
        source_stat = None
        if preserve_metadata:
            try:
                source_stat = os.stat(abs_source)
            except:
                # 如果无法获取元数据，继续操作但不保留元数据
                pass
        
        # 获取文件大小
        try:
            file_size = os.path.getsize(abs_source)
            result['size'] = file_size
        except:
            file_size = 0
        
        # 执行移动操作
        shutil.move(abs_source, abs_target)
        
        # 如果需要保留元数据，尝试恢复源文件的权限和时间戳
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
                    result['message'] = '文件移动成功，但无法保留所有元数据'
        
        result['success'] = True
        result['moved'] = True
        result['message'] = f'文件移动成功: {abs_source} -> {abs_target} (大小: {file_size} 字节)'
        
    except PermissionError as e:
        result['error'] = f'权限不足，无法移动文件: {str(e)}'
    except OSError as e:
        result['error'] = f'移动文件时发生系统错误: {str(e)}'
    except Exception as e:
        result['error'] = f'移动文件时发生未知错误: {str(e)}'
    
    return result


def file_move_simple(source_path: str, target_path: str) -> bool:
    """
    简化版文件移动函数
    
    Args:
        source_path: 源文件路径
        target_path: 目标文件路径
        
    Returns:
        bool: 移动是否成功
    """
    try:
        result = file_move(source_path, target_path, overwrite=False, preserve_metadata=True)
        return result['success']
    except:
        return False


def safe_file_move(source_path: str, target_path: str, 
                  max_retries: int = 3) -> Dict[str, Any]:
    """
    安全移动文件（带重试机制）
    
    Args:
        source_path: 源文件路径
        target_path: 目标文件路径
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
            move_result = file_move(source_path, target_path, overwrite=True, preserve_metadata=True)
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


def format_file_move(result: Dict[str, Any]) -> str:
    """
    格式化文件移动结果为可读字符串
    
    Args:
        result: 文件移动结果字典
        
    Returns:
        str: 格式化的移动结果字符串
    """
    if result.get('error'):
        return f"错误: {result['error']}"
    
    lines = []
    lines.append("=" * 60)
    lines.append("FILE MOVE RESULTS")
    lines.append("=" * 60)
    
    lines.append(f"源路径: {result.get('source_path', 'Unknown')}")
    lines.append(f"目标路径: {result.get('target_path', 'Unknown')}")
    lines.append(f"操作状态: {'成功' if result.get('success') else '失败'}")
    lines.append(f"文件移动: {'是' if result.get('moved') else '否'}")
    lines.append(f"文件大小: {_format_size(result.get('size', 0))}")
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


def move_files(move_list: List[Tuple[str, str]], 
               overwrite: bool = False, 
               preserve_metadata: bool = True) -> Dict[str, Any]:
    """
    批量移动文件
    
    Args:
        move_list: 移动列表，每个元素为 (source_path, target_path) 元组
        overwrite: 是否覆盖已存在的目标文件（默认False）
        preserve_metadata: 是否保留元数据（默认True）
        
    Returns:
        Dict[str, Any]: 包含批量移动结果的字典
    """
    result = {
        'success': True,
        'total_files': len(move_list),
        'successful_moves': 0,
        'failed_moves': 0,
        'total_size': 0,
        'moved_files': [],
        'failed_files': [],
        'message': '',
        'error': ''
    }
    
    if not move_list:
        result['message'] = '文件列表为空'
        return result
    
    for source_path, target_path in move_list:
        move_result = file_move(source_path, target_path, overwrite, preserve_metadata)
        
        if move_result['success']:
            result['successful_moves'] += 1
            if move_result['moved']:
                result['moved_files'].append((source_path, target_path))
                result['total_size'] += move_result.get('size', 0)
        else:
            result['success'] = False
            result['failed_moves'] += 1
            result['failed_files'].append({
                'source_path': source_path,
                'target_path': target_path,
                'error': move_result.get('error', '未知错误')
            })
    
    result['message'] = f'批量移动完成: 成功 {result["successful_moves"]} 个，失败 {result["failed_moves"]} 个'
    
    return result


if __name__ == "__main__":
    # 测试代码
    print("文件移动功能测试")
    print("=" * 60)
    
    # 创建测试文件
    test_files = [
        "./test_move_source1.txt",
        "./test_move_source2.txt",
        "./test_move_source3.txt",
        "./test_move_source4.txt"
    ]
    
    # 创建测试文件
    for test_file in test_files:
        try:
            with open(test_file, 'w') as f:
                f.write(f"这是 {test_file} 的测试内容")
        except:
            pass  # 文件可能已存在
    
    # 测试用例
    test_cases = [
        ("./test_move_source1.txt", "./test_move_dest1.txt", False, True),      # 正常移动
        ("./test_move_source2.txt", "./test_move_dest2.txt", False, True),      # 正常移动
        ("./nonexistent_file.txt", "./test_move_dest3.txt", False, True),       # 移动不存在的文件
        ("./test_move_source3.txt", "./test_move_dest2.txt", False, True),      # 目标文件已存在（不覆盖）
        ("./test_move_source3.txt", "./test_move_dest2.txt", True, True),       # 目标文件已存在（覆盖）
        ("./test_move_source4.txt", "./test_move_dest4.txt", False, False),     # 不保留元数据
        ("", "./test_move_dest5.txt", False, True),                             # 空源路径
        ("./test_move_source1.txt", "", False, True),                           # 空目标路径
    ]
    
    for i, (source, target, overwrite, preserve_metadata) in enumerate(test_cases, 1):
        print(f"测试用例 {i}:")
        print(f"  源文件: {source}")
        print(f"  目标文件: {target}")
        print(f"  覆盖: {overwrite}")
        print(f"  保留元数据: {preserve_metadata}")
        
        result = file_move(source, target, overwrite, preserve_metadata)
        print(format_file_move(result))
        print()
    
    # 测试安全移动
    print("安全移动测试:")
    # 创建一个可能无法立即移动的文件（模拟被占用）
    protected_file = "./test_protected_source.txt"
    protected_target = "./test_protected_dest.txt"
    try:
        with open(protected_file, 'w') as f:
            f.write("受保护的文件内容")
    except:
        pass
    
    safe_result = safe_file_move(protected_file, protected_target, max_retries=2)
    print(format_file_move(safe_result))
    print()
    
    # 测试批量移动
    print("批量移动测试:")
    # 创建一些测试文件用于批量移动
    batch_files = [
        ("./test_batch_source1.txt", "./test_batch_dest1.txt"),
        ("./test_batch_source2.txt", "./test_batch_dest2.txt"),
        ("./test_batch_source3.txt", "./test_batch_dest3.txt")
    ]
    
    for source_path, target_path in batch_files:
        try:
            with open(source_path, 'w') as f:
                f.write(f"批量测试文件: {source_path}")
        except:
            pass
    
    batch_result = move_files(batch_files + [("./nonexistent_batch.txt", "./new_batch.txt")], 
                             overwrite=True, preserve_metadata=True)
    print("批量移动结果:")
    print(f"总文件数: {batch_result['total_files']}")
    print(f"成功移动: {batch_result['successful_moves']}")
    print(f"失败移动: {batch_result['failed_moves']}")
    print(f"总大小: {_format_size(batch_result['total_size'])}")
    print(f"消息: {batch_result['message']}")
    
    if batch_result['failed_files']:
        print("失败文件列表:")
        for failed in batch_result['failed_files']:
            print(f"  - {failed['source_path']} -> {failed['target_path']}: {failed['error']}")
    
    # 清理测试文件
    print("\n清理测试文件...")
    files_to_clean = [
        "./test_move_source1.txt", "./test_move_source2.txt", "./test_move_source3.txt", 
        "./test_move_source4.txt", "./test_move_dest1.txt", "./test_move_dest2.txt", 
        "./test_move_dest4.txt", "./test_protected_source.txt", "./test_protected_dest.txt",
        "./test_batch_source1.txt", "./test_batch_source2.txt", "./test_batch_source3.txt",
        "./test_batch_dest1.txt", "./test_batch_dest2.txt", "./test_batch_dest3.txt"
    ]
    
    for clean_file in files_to_clean:
        if os.path.exists(clean_file) and os.path.isfile(clean_file):
            try:
                os.remove(clean_file)
                print(f"已清理: {clean_file}")
            except Exception as e:
                print(f"清理失败 {clean_file}: {e}")
    
    print("\n测试完成！")