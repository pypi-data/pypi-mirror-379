"""
文件信息模块 - 获取跨平台文件信息
仅使用Python标准库，支持Windows、Linux、macOS
"""

import os
import platform
import stat
import time
import datetime
from typing import Dict, Any, Optional


def file_info(file_path: str) -> Dict[str, Any]:
    """
    获取文件的详细信息
    
    Args:
        file_path: 文件路径字符串
        
    Returns:
        Dict[str, Any]: 包含文件各种信息的字典，包含以下字段：
            - exists: bool - 文件是否存在
            - path: str - 文件绝对路径
            - type: str - 路径类型（file, not_exist, error）
            - size: int - 文件大小（字节）
            - last_modified: str - 最后修改时间（ISO格式）
            - last_accessed: str - 最后访问时间（ISO格式）
            - created: str - 创建时间（ISO格式，如果可用）
            - permissions: Dict[str, Any] - 权限信息
            - owner: str - 所有者信息
            - group: str - 组信息
            - error: str - 错误信息（如果发生错误）
    """
    result = {
        'exists': False,
        'path': '',
        'type': 'not_exist',
        'size': 0,
        'last_modified': '',
        'last_accessed': '',
        'created': '',
        'permissions': {},
        'owner': 'Unknown',
        'group': 'Unknown',
        'error': ''
    }
    
    if not file_path:
        result['error'] = '文件路径不能为空'
        return result
    
    try:
        # 检查路径是否存在
        if not os.path.exists(file_path):
            result['exists'] = False
            result['type'] = 'not_exist'
            result['path'] = os.path.abspath(file_path) if file_path else ''
            return result
        
        # 检查是否为文件
        if not os.path.isfile(file_path):
            result['exists'] = True
            result['type'] = 'not_file'
            result['path'] = os.path.abspath(file_path)
            result['error'] = '路径不是文件'
            return result
        
        result['exists'] = True
        result['type'] = 'file'
        result['path'] = os.path.abspath(file_path)
        
        # 获取文件统计信息
        file_stat = os.stat(file_path)
        
        # 文件大小
        result['size'] = file_stat.st_size
        
        # 时间信息
        result['last_modified'] = datetime.datetime.fromtimestamp(
            file_stat.st_mtime
        ).isoformat()
        
        result['last_accessed'] = datetime.datetime.fromtimestamp(
            file_stat.st_atime
        ).isoformat()
        
        # 创建时间（Windows支持，Unix系统可能不支持）
        try:
            result['created'] = datetime.datetime.fromtimestamp(
                file_stat.st_ctime
            ).isoformat()
        except:
            result['created'] = 'Not available'
        
        # 权限信息
        result['permissions'] = _get_permissions_info(file_stat.st_mode)
        
        # 所有者和组信息
        owner_info, group_info = _get_owner_group_info(file_stat)
        result['owner'] = owner_info
        result['group'] = group_info
        
    except Exception as e:
        result['error'] = f"获取文件信息时发生错误: {str(e)}"
    
    return result


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


def _get_owner_group_info(file_stat) -> tuple:
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
                advapi32.LookupAccountSidW(None, file_stat.st_uid, None, ctypes.byref(sid_size), 
                                          None, ctypes.byref(domain_size), ctypes.byref(sid_name_use))
                
                if sid_size.value > 0:
                    sid_buf = ctypes.create_string_buffer(sid_size.value)
                    domain_buf = ctypes.create_unicode_buffer(domain_size.value)
                    
                    if advapi32.LookupAccountSidW(None, file_stat.st_uid, sid_buf, ctypes.byref(sid_size),
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
                owner_info = pwd.getpwuid(file_stat.st_uid)
                group_info = grp.getgrgid(file_stat.st_gid)
                owner = owner_info.pw_name
                group = group_info.gr_name
            except:
                # 如果pwd/grp不可用，使用UID/GID
                owner = f"UID:{file_stat.st_uid}"
                group = f"GID:{file_stat.st_gid}"
    except Exception:
        # 所有方法都失败，保持默认值
        pass
    
    return owner, group


def format_file_info(info: Dict[str, Any]) -> str:
    """
    格式化文件信息为可读字符串
    
    Args:
        info: 文件信息字典
        
    Returns:
        str: 格式化的文件信息字符串
    """
    if info.get('error'):
        return f"错误: {info['error']}"
    
    lines = []
    lines.append("=" * 60)
    lines.append("FILE INFORMATION")
    lines.append("=" * 60)
    
    # 基本路径信息
    lines.append(f"路径: {info.get('path', 'Unknown')}")
    lines.append(f"是否存在: {'是' if info.get('exists') else '否'}")
    lines.append(f"类型: {info.get('type', 'Unknown')}")
    
    # 大小信息
    size_bytes = info.get('size', 0)
    if size_bytes >= 1024**3:
        size_str = f"{size_bytes / (1024**3):.2f} GB"
    elif size_bytes >= 1024**2:
        size_str = f"{size_bytes / (1024**2):.2f} MB"
    elif size_bytes >= 1024:
        size_str = f"{size_bytes / 1024:.2f} KB"
    else:
        size_str = f"{size_bytes} 字节"
    
    lines.append(f"大小: {size_str} ({size_bytes} 字节)")
    
    # 时间信息
    lines.append(f"最后修改: {info.get('last_modified', 'Unknown')}")
    lines.append(f"最后访问: {info.get('last_accessed', 'Unknown')}")
    lines.append(f"创建时间: {info.get('created', 'Unknown')}")
    
    # 权限信息
    perm_info = info.get('permissions', {})
    lines.append(f"权限: {perm_info.get('symbolic', 'Unknown')} ({perm_info.get('octal', 'Unknown')})")
    
    # 所有者和组
    lines.append(f"所有者: {info.get('owner', 'Unknown')}")
    lines.append(f"组: {info.get('group', 'Unknown')}")
    
    # 详细权限
    if perm_info:
        user_perm = perm_info.get('user', {})
        group_perm = perm_info.get('group', {})
        other_perm = perm_info.get('other', {})
        
        lines.append("详细权限:")
        lines.append(f"  用户: 读{'✓' if user_perm.get('read') else '✗'} "
                    f"写{'✓' if user_perm.get('write') else '✗'} "
                    f"执行{'✓' if user_perm.get('execute') else '✗'}")
        lines.append(f"  组:   读{'✓' if group_perm.get('read') else '✗'} "
                    f"写{'✓' if group_perm.get('write') else '✗'} "
                    f"执行{'✓' if group_perm.get('execute') else '✗'}")
        lines.append(f"  其他: 读{'✓' if other_perm.get('read') else '✗'} "
                    f"写{'✓' if other_perm.get('write') else '✗'} "
                    f"执行{'✓' if other_perm.get('execute') else '✗'}")
    
    lines.append("=" * 60)
    return '\n'.join(lines)


# 便捷函数
def get_file_size(file_path: str) -> int:
    """获取文件大小（简化版）"""
    try:
        info = file_info(file_path)
        return info.get('size', 0)
    except:
        return 0


def get_file_modification_time(file_path: str) -> str:
    """获取文件最后修改时间（简化版）"""
    try:
        info = file_info(file_path)
        return info.get('last_modified', '')
    except:
        return ''


def get_file_permissions(file_path: str) -> Dict[str, Any]:
    """获取文件权限信息（简化版）"""
    try:
        info = file_info(file_path)
        return info.get('permissions', {})
    except:
        return {}


def is_file_readable(file_path: str) -> bool:
    """检查文件是否可读"""
    try:
        info = file_info(file_path)
        return info.get('permissions', {}).get('readable', False)
    except:
        return False


def is_file_writable(file_path: str) -> bool:
    """检查文件是否可写"""
    try:
        info = file_info(file_path)
        return info.get('permissions', {}).get('writable', False)
    except:
        return False


def is_file_executable(file_path: str) -> bool:
    """检查文件是否可执行"""
    try:
        info = file_info(file_path)
        return info.get('permissions', {}).get('executable', False)
    except:
        return False


if __name__ == "__main__":
    # 测试代码
    test_files = [
        __file__,  # 当前文件
        "README.md",  # 项目README文件
        "/nonexistent/file.txt",  # 不存在的文件
        ".",  # 目录（应该返回错误）
    ]
    
    print("文件信息检查测试")
    print("=" * 60)
    
    for test_file in test_files:
        print(f"待测试文件: {test_file}")
        result = file_info(test_file)
        print(format_file_info(result))
        print()