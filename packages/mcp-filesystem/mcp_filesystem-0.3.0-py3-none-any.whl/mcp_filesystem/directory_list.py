"""
目录列表模块 - 列出目录中的文件和子目录
仅使用Python标准库，支持Windows、Linux、macOS
"""

import os
import platform
import stat
import datetime
from typing import Dict, Any, List, Optional, Callable


def directory_list(directory_path: str, 
                  sort_by: str = 'name', 
                  reverse: bool = False,
                  filter_type: Optional[str] = None) -> Dict[str, Any]:
    """
    列出目录中的所有文件和子目录
    
    Args:
        directory_path: 要列出的目录路径
        sort_by: 排序方式 ('name', 'size', 'modified', 'type')
        reverse: 是否反向排序
        filter_type: 过滤类型 ('file', 'directory', None表示不过滤)
        
    Returns:
        Dict[str, Any]: 包含列表结果的字典，包含以下字段：
            - success: bool - 操作是否成功
            - directory: str - 目录的绝对路径
            - total_count: int - 总项目数
            - file_count: int - 文件数量
            - directory_count: int - 子目录数量
            - items: List[Dict] - 项目列表，每个项目包含详细信息
            - error: str - 错误信息（如果发生错误）
    """
    result = {
        'success': False,
        'directory': '',
        'total_count': 0,
        'file_count': 0,
        'directory_count': 0,
        'items': [],
        'error': ''
    }
    
    if not directory_path:
        result['error'] = '目录路径不能为空'
        return result
    
    try:
        # 获取目录的绝对路径
        abs_path = os.path.abspath(directory_path)
        result['directory'] = abs_path
        
        # 检查目录是否存在
        if not os.path.exists(abs_path):
            result['error'] = f'目录不存在: {abs_path}'
            return result
        
        # 检查是否为目录
        if not os.path.isdir(abs_path):
            result['error'] = f'路径不是目录: {abs_path}'
            return result
        
        # 获取目录内容
        items = []
        file_count = 0
        dir_count = 0
        
        for item_name in os.listdir(abs_path):
            item_path = os.path.join(abs_path, item_name)
            
            # 过滤类型
            if filter_type == 'file' and not os.path.isfile(item_path):
                continue
            if filter_type == 'directory' and not os.path.isdir(item_path):
                continue
            
            # 获取项目详细信息
            item_info = _get_item_info(item_path, item_name)
            items.append(item_info)
            
            # 统计数量
            if item_info['type'] == 'file':
                file_count += 1
            elif item_info['type'] == 'directory':
                dir_count += 1
        
        # 排序
        sorted_items = _sort_items(items, sort_by, reverse)
        
        result['items'] = sorted_items
        result['total_count'] = len(items)
        result['file_count'] = file_count
        result['directory_count'] = dir_count
        result['success'] = True
        
    except PermissionError as e:
        result['error'] = f'权限不足，无法访问目录: {str(e)}'
    except Exception as e:
        result['error'] = f'列出目录内容时发生错误: {str(e)}'
    
    return result


def _get_item_info(item_path: str, item_name: str) -> Dict[str, Any]:
    """获取单个项目的详细信息"""
    item_info = {
        'name': item_name,
        'path': item_path,
        'type': 'unknown',
        'size': 0,
        'last_modified': '',
        'last_modified_timestamp': 0,  # 添加时间戳用于排序
        'permissions': {},
        'owner': 'Unknown',
        'group': 'Unknown'
    }
    
    try:
        # 获取文件状态
        item_stat = os.stat(item_path)
        
        # 确定类型
        if os.path.isfile(item_path):
            item_info['type'] = 'file'
            item_info['size'] = item_stat.st_size
        elif os.path.isdir(item_path):
            item_info['type'] = 'directory'
        elif os.path.islink(item_path):
            item_info['type'] = 'link'
        else:
            item_info['type'] = 'other'
        
        # 最后修改时间
        item_info['last_modified'] = datetime.datetime.fromtimestamp(
            item_stat.st_mtime
        ).isoformat()
        item_info['last_modified_timestamp'] = item_stat.st_mtime
        
        # 权限信息
        item_info['permissions'] = _get_permissions_info(item_stat.st_mode)
        
        # 所有者和组信息
        owner, group = _get_owner_group_info(item_stat)
        item_info['owner'] = owner
        item_info['group'] = group
        
    except Exception as e:
        # 如果无法获取详细信息，至少保留基本名称和类型
        item_info['error'] = f'获取项目信息时发生错误: {str(e)}'
    
    return item_info


def _get_permissions_info(mode: int) -> Dict[str, Any]:
    """从文件模式获取权限信息"""
    permissions = {}
    
    # 八进制权限表示
    permissions['octal'] = oct(mode & 0o777)
    
    # 符号表示
    perm_str = stat.filemode(mode)
    permissions['symbolic'] = perm_str
    
    # 详细权限分解
    permissions['readable'] = bool(mode & stat.S_IRUSR)
    permissions['writable'] = bool(mode & stat.S_IWUSR)
    permissions['executable'] = bool(mode & stat.S_IXUSR)
    
    # 用户权限
    permissions['user'] = {
        'read': bool(mode & stat.S_IRUSR),
        'write': bool(mode & stat.S_IWUSR),
        'execute': bool(mode & stat.S_IXUSR)
    }
    
    # 组权限
    permissions['group'] = {
        'read': bool(mode & stat.S_IRGRP),
        'write': bool(mode & stat.S_IWGRP),
        'execute': bool(mode & stat.S_IXGRP)
    }
    
    # 其他用户权限
    permissions['other'] = {
        'read': bool(mode & stat.S_IROTH),
        'write': bool(mode & stat.S_IWOTH),
        'execute': bool(mode & stat.S_IXOTH)
    }
    
    return permissions


def _get_owner_group_info(item_stat) -> tuple:
    """获取所有者和组信息（跨平台）"""
    owner = 'Unknown'
    group = 'Unknown'
    
    try:
        if platform.system() == 'Windows':
            # Windows系统，尝试获取所有者信息
            try:
                import ctypes
                from ctypes import wintypes
                
                # 获取文件安全信息
                advapi32 = ctypes.windll.advapi32
                kernel32 = ctypes.windll.kernel32
                
                # 获取当前进程令牌
                token = wintypes.HANDLE()
                advapi32.OpenProcessToken(kernel32.GetCurrentProcess(), 0x0008, ctypes.byref(token))
                
                # 查找账户SID
                sid = wintypes.DWORD()
                sid_size = wintypes.DWORD()
                domain_size = wintypes.DWORD()
                sid_name_use = wintypes.DWORD()
                
                # 第一次调用获取所需大小
                advapi32.LookupAccountSidW(None, item_stat.st_uid, None, ctypes.byref(sid_size), 
                                          None, ctypes.byref(domain_size), ctypes.byref(sid_name_use))
                
                if sid_size.value > 0:
                    sid_buf = ctypes.create_string_buffer(sid_size.value)
                    domain_buf = ctypes.create_unicode_buffer(domain_size.value)
                    
                    if advapi32.LookupAccountSidW(None, item_stat.st_uid, sid_buf, ctypes.byref(sid_size),
                                                 domain_buf, ctypes.byref(domain_size), ctypes.byref(sid_name_use)):
                        owner = domain_buf.value + '\\' + sid_buf.value.decode('utf-16le', errors='ignore')
            except:
                # 如果上述方法失败，使用简单方法
                try:
                    owner = os.getlogin()
                except:
                    pass
        else:
            # Unix-like系统（Linux, macOS）
            try:
                import pwd
                import grp
                owner_info = pwd.getpwuid(item_stat.st_uid)
                group_info = grp.getgrgid(item_stat.st_gid)
                owner = owner_info.pw_name
                group = group_info.gr_name
            except:
                # 如果pwd/grp不可用，使用UID/GID
                owner = f"UID:{item_stat.st_uid}"
                group = f"GID:{item_stat.st_gid}"
    except Exception:
        # 所有方法都失败，保持默认值
        pass
    
    return owner, group


def _sort_items(items: List[Dict], sort_by: str, reverse: bool) -> List[Dict]:
    """对项目列表进行排序"""
    if not items:
        return items
    
    # 定义排序键函数
    sort_functions = {
        'name': lambda x: x['name'].lower(),
        'size': lambda x: x['size'],
        'modified': lambda x: x.get('last_modified_timestamp', 0),  # 使用时间戳而不是字符串
        'type': lambda x: x['type']
    }
    
    sort_key = sort_functions.get(sort_by, sort_functions['name'])
    
    try:
        sorted_items = sorted(items, key=sort_key, reverse=reverse)
    except Exception:
        # 如果排序失败，按名称排序
        sorted_items = sorted(items, key=lambda x: x['name'].lower(), reverse=reverse)
    
    return sorted_items


def format_directory_list(result: Dict[str, Any]) -> str:
    """
    格式化目录列表结果为可读字符串
    
    Args:
        result: 目录列表结果字典
        
    Returns:
        str: 格式化的列表结果字符串
    """
    if result.get('error'):
        return f"错误: {result['error']}"
    
    if not result.get('success'):
        return "操作失败"
    
    lines = []
    lines.append("=" * 80)
    lines.append("DIRECTORY LISTING")
    lines.append("=" * 80)
    
    lines.append(f"目录: {result.get('directory', 'Unknown')}")
    lines.append(f"总项目数: {result.get('total_count', 0)}")
    lines.append(f"文件数量: {result.get('file_count', 0)}")
    lines.append(f"子目录数量: {result.get('directory_count', 0)}")
    lines.append("")
    
    items = result.get('items', [])
    if not items:
        lines.append("目录为空")
    else:
        # 表头
        header = f"{'名称':<30} {'类型':<10} {'大小':<12} {'修改时间':<20} {'权限':<10}"
        lines.append(header)
        lines.append("-" * 80)
        
        # 项目列表
        for item in items:
            name = item.get('name', 'Unknown')
            item_type = item.get('type', 'unknown')
            
            # 格式化大小
            size = item.get('size', 0)
            if item_type == 'directory':
                size_str = '<DIR>'
            elif size >= 1024**3:
                size_str = f"{size / (1024**3):.1f}G"
            elif size >= 1024**2:
                size_str = f"{size / (1024**2):.1f}M"
            elif size >= 1024:
                size_str = f"{size / 1024:.1f}K"
            else:
                size_str = f"{size}B"
            
            # 格式化修改时间
            modified = item.get('last_modified', '')
            if modified:
                # 只显示日期部分
                modified_str = modified.split('T')[0]
            else:
                modified_str = 'Unknown'
            
            # 权限符号表示
            permissions = item.get('permissions', {})
            perm_str = permissions.get('symbolic', 'Unknown')
            
            line = f"{name:<30} {item_type:<10} {size_str:<12} {modified_str:<20} {perm_str:<10}"
            lines.append(line)
    
    lines.append("=" * 80)
    return '\n'.join(lines)


# 便捷函数
def list_files(directory_path: str) -> List[str]:
    """
    列出目录中的所有文件（简化版）
    
    Args:
        directory_path: 目录路径
        
    Returns:
        List[str]: 文件路径列表
    """
    try:
        result = directory_list(directory_path, filter_type='file')
        return [item['path'] for item in result.get('items', [])] if result.get('success') else []
    except:
        return []


def list_directories(directory_path: str) -> List[str]:
    """
    列出目录中的所有子目录（简化版）
    
    Args:
        directory_path: 目录路径
        
    Returns:
        List[str]: 子目录路径列表
    """
    try:
        result = directory_list(directory_path, filter_type='directory')
        return [item['path'] for item in result.get('items', [])] if result.get('success') else []
    except:
        return []


def get_directory_contents(directory_path: str) -> List[str]:
    """
    列出目录中的所有项目名称（简化版）
    
    Args:
        directory_path: 目录路径
        
    Returns:
        List[str]: 项目名称列表
    """
    try:
        result = directory_list(directory_path)
        return [item['name'] for item in result.get('items', [])] if result.get('success') else []
    except:
        return []


if __name__ == "__main__":
    # 测试代码
    print("目录列表功能测试")
    print("=" * 60)
    
    # 测试用例
    test_cases = [
        (".", 'name', False, None),      # 当前目录，按名称排序
        (".", 'size', True, 'file'),     # 当前目录，按大小反向排序，只显示文件
        (".", 'modified', False, 'directory'),  # 当前目录，按修改时间排序，只显示目录
        ("/nonexistent", 'name', False, None),  # 不存在的目录
        ("", 'name', False, None),       # 空路径
    ]
    
    for i, (dir_path, sort_by, reverse, filter_type) in enumerate(test_cases, 1):
        print(f"测试用例 {i}:")
        print(f"  目录: {dir_path}")
        print(f"  排序: {sort_by}")
        print(f"  反向: {reverse}")
        print(f"  过滤: {filter_type}")
        
        result = directory_list(dir_path, sort_by, reverse, filter_type)
        print(format_directory_list(result))
        print()
    
    # 测试便捷函数
    print("便捷函数测试:")
    print(f"文件列表: {list_files('.')}")
    print(f"目录列表: {list_directories('.')}")
    print(f"所有项目: {get_directory_contents('.')}")