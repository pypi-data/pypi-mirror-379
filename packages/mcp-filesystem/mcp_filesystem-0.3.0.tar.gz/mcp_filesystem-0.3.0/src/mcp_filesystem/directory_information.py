"""
目录信息模块 - 获取跨平台目录信息
仅使用Python标准库，支持Windows、Linux、macOS
"""

import os
import platform
import stat
import time
import datetime
from typing import Dict, Any, Optional


def directory_info(directory_path: str) -> Dict[str, Any]:
    """
    获取目录的详细信息
    
    Args:
        directory_path: 目录路径字符串
        
    Returns:
        Dict[str, Any]: 包含目录各种信息的字典，包含以下字段：
            - exists: bool - 目录是否存在
            - path: str - 目录绝对路径
            - type: str - 路径类型（directory, not_exist, error）
            - size: int - 目录总大小（字节）
            - file_count: int - 目录中文件总数
            - directory_count: int - 目录中子目录总数
            - last_modified: str - 最后修改时间（ISO格式）
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
        'file_count': 0,
        'directory_count': 0,
        'last_modified': '',
        'permissions': {},
        'owner': 'Unknown',
        'group': 'Unknown',
        'error': ''
    }
    
    if not directory_path:
        result['error'] = '目录路径不能为空'
        return result
    
    try:
        # 检查路径是否存在
        if not os.path.exists(directory_path):
            result['exists'] = False
            result['type'] = 'not_exist'
            result['path'] = os.path.abspath(directory_path) if directory_path else ''
            return result
        
        # 检查是否为目录
        if not os.path.isdir(directory_path):
            result['exists'] = True
            result['type'] = 'not_directory'
            result['path'] = os.path.abspath(directory_path)
            result['error'] = '路径不是目录'
            return result
        
        result['exists'] = True
        result['type'] = 'directory'
        result['path'] = os.path.abspath(directory_path)
        
        # 获取目录统计信息
        dir_stat = os.stat(directory_path)
        
        # 最后修改时间
        result['last_modified'] = datetime.datetime.fromtimestamp(
            dir_stat.st_mtime
        ).isoformat()
        
        # 权限信息
        result['permissions'] = _get_permissions_info(dir_stat.st_mode)
        
        # 所有者和组信息
        owner_info, group_info = _get_owner_group_info(dir_stat)
        result['owner'] = owner_info
        result['group'] = group_info
        
        # 计算目录大小和文件/目录数量
        size_info = _calculate_directory_size(directory_path)
        result.update(size_info)
        
    except Exception as e:
        result['error'] = f"获取目录信息时发生错误: {str(e)}"
    
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


def _get_owner_group_info(dir_stat) -> tuple:
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
                advapi32.LookupAccountSidW(None, dir_stat.st_uid, None, ctypes.byref(sid_size), 
                                          None, ctypes.byref(domain_size), ctypes.byref(sid_name_use))
                
                if sid_size.value > 0:
                    sid_buf = ctypes.create_string_buffer(sid_size.value)
                    domain_buf = ctypes.create_unicode_buffer(domain_size.value)
                    
                    if advapi32.LookupAccountSidW(None, dir_stat.st_uid, sid_buf, ctypes.byref(sid_size),
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
                owner_info = pwd.getpwuid(dir_stat.st_uid)
                group_info = grp.getgrgid(dir_stat.st_gid)
                owner = owner_info.pw_name
                group = group_info.gr_name
            except:
                # 如果pwd/grp不可用，使用UID/GID
                owner = f"UID:{dir_stat.st_uid}"
                group = f"GID:{dir_stat.st_gid}"
    except Exception:
        # 所有方法都失败，保持默认值
        pass
    
    return owner, group


def _calculate_directory_size(directory_path: str) -> Dict[str, Any]:
    """计算目录大小和文件/目录数量"""
    total_size = 0
    file_count = 0
    dir_count = 0
    
    try:
        for dirpath, dirnames, filenames in os.walk(directory_path):
            # 统计子目录数量（不包括当前目录）
            dir_count += len(dirnames)
            
            # 统计文件数量和大小
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                try:
                    file_stat = os.stat(filepath)
                    total_size += file_stat.st_size
                    file_count += 1
                except (OSError, IOError):
                    # 忽略无法访问的文件
                    continue
        
        # 调整目录计数（os.walk返回的dirnames不包括当前目录）
        # 所以dir_count已经是子目录数量
        
    except Exception as e:
        # 如果遍历出错，返回部分结果
        return {
            'size': total_size,
            'file_count': file_count,
            'directory_count': dir_count,
            'error': f"计算目录大小时发生错误: {str(e)}"
        }
    
    return {
        'size': total_size,
        'file_count': file_count,
        'directory_count': dir_count
    }


def format_directory_info(info: Dict[str, Any]) -> str:
    """
    格式化目录信息为可读字符串
    
    Args:
        info: 目录信息字典
        
    Returns:
        str: 格式化的目录信息字符串
    """
    if info.get('error'):
        return f"错误: {info['error']}"
    
    lines = []
    lines.append("=" * 60)
    lines.append("DIRECTORY INFORMATION")
    lines.append("=" * 60)
    
    # 基本路径信息
    lines.append(f"路径: {info.get('path', 'Unknown')}")
    lines.append(f"是否存在: {'是' if info.get('exists') else '否'}")
    lines.append(f"类型: {info.get('type', 'Unknown')}")
    
    # 大小和数量信息
    size_bytes = info.get('size', 0)
    if size_bytes >= 1024**3:
        size_str = f"{size_bytes / (1024**3):.2f} GB"
    elif size_bytes >= 1024**2:
        size_str = f"{size_bytes / (1024**2):.2f} MB"
    elif size_bytes >= 1024:
        size_str = f"{size_bytes / 1024:.2f} KB"
    else:
        size_str = f"{size_bytes} 字节"
    
    lines.append(f"总大小: {size_str} ({size_bytes} 字节)")
    lines.append(f"文件数量: {info.get('file_count', 0)}")
    lines.append(f"子目录数量: {info.get('directory_count', 0)}")
    
    # 时间信息
    lines.append(f"最后修改: {info.get('last_modified', 'Unknown')}")
    
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
def get_directory_size(directory_path: str) -> int:
    """获取目录大小（简化版）"""
    try:
        info = directory_info(directory_path)
        return info.get('size', 0)
    except:
        return 0


def get_directory_file_count(directory_path: str) -> int:
    """获取目录中文件数量（简化版）"""
    try:
        info = directory_info(directory_path)
        return info.get('file_count', 0)
    except:
        return 0


def get_directory_modification_time(directory_path: str) -> str:
    """获取目录最后修改时间（简化版）"""
    try:
        info = directory_info(directory_path)
        return info.get('last_modified', '')
    except:
        return ''


if __name__ == "__main__":
    # 测试代码
    test_directories = [
        ".",  # 当前目录
        "..",  # 上级目录
        "/tmp",  # 临时目录（Unix）
        "C:\\Windows" if platform.system() == "Windows" else "/usr",  # 系统目录
        "/nonexistent/directory",  # 不存在的目录
    ]
    
    print("目录信息检查测试")
    print("=" * 60)
    
    for test_dir in test_directories:
        print(f"待测试目录: {test_dir}")
        result = directory_info(test_dir)
        print(format_directory_info(result))
        print()