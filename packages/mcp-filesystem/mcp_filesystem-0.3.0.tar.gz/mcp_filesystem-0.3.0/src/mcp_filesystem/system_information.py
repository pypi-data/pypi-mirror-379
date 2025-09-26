"""
系统信息模块 - 获取跨平台系统信息
仅使用Python标准库，支持Windows、Linux、macOS
"""

import os
import platform
import sys
import socket
import time
import datetime
import getpass
from typing import Dict, Any, Optional


def system_info() -> Dict[str, Any]:
    """
    获取系统信息
    
    Returns:
        Dict[str, Any]: 包含系统各种信息的字典
    """
    info = {}
    
    # 基本信息
    info['timestamp'] = datetime.datetime.now().isoformat()
    info['python_version'] = sys.version
    info['python_implementation'] = platform.python_implementation()
    
    # 平台信息
    info['platform'] = {
        'system': platform.system(),
        'release': platform.release(),
        'version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'architecture': platform.architecture(),
        'platform': platform.platform(),
    }
    
    # 主机信息
    try:
        info['hostname'] = socket.gethostname()
    except:
        info['hostname'] = 'Unknown'
    
    try:
        info['fqdn'] = socket.getfqdn()
    except:
        info['fqdn'] = 'Unknown'
    
    # 用户信息
    try:
        info['current_user'] = getpass.getuser()
    except:
        info['current_user'] = 'Unknown'
    
    # 工作目录
    info['current_working_directory'] = os.getcwd()
    
    # 环境信息
    info['environment'] = {
        'path_separator': os.pathsep,
        'directory_separator': os.sep,
        'line_separator': os.linesep,
    }
    
    # CPU信息
    info['cpu'] = {
        'count': os.cpu_count(),
    }
    
    # 内存信息（跨平台实现）
    info['memory'] = _get_memory_info()
    
    # 磁盘信息（跨平台实现）
    info['disk'] = _get_disk_info()
    
    # 网络信息
    info['network'] = _get_network_info()
    
    # 时间信息
    info['time'] = {
        'timezone': time.tzname,
        'daylight_saving': time.daylight,
        'timezone_offset': time.timezone,
    }
    
    # 文件系统编码
    info['filesystem_encoding'] = sys.getfilesystemencoding()
    
    return info


def _get_memory_info() -> Dict[str, Any]:
    """获取内存信息（跨平台）"""
    memory_info = {}
    
    try:
        if platform.system() == 'Windows':
            # Windows内存信息
            import ctypes
            class MEMORYSTATUSEX(ctypes.Structure):
                _fields_ = [
                    ("dwLength", ctypes.c_ulong),
                    ("dwMemoryLoad", ctypes.c_ulong),
                    ("ullTotalPhys", ctypes.c_ulonglong),
                    ("ullAvailPhys", ctypes.c_ulonglong),
                    ("ullTotalPageFile", ctypes.c_ulonglong),
                    ("ullAvailPageFile", ctypes.c_ulonglong),
                    ("ullTotalVirtual", ctypes.c_ulonglong),
                    ("ullAvailVirtual", ctypes.c_ulonglong),
                    ("ullAvailExtendedVirtual", ctypes.c_ulonglong)
                ]
            
            memory_status = MEMORYSTATUSEX()
            memory_status.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
            ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory_status))
            
            memory_info.update({
                'total_physical': memory_status.ullTotalPhys,
                'available_physical': memory_status.ullAvailPhys,
                'memory_load': memory_status.dwMemoryLoad,
                'total_virtual': memory_status.ullTotalVirtual,
                'available_virtual': memory_status.ullAvailVirtual,
            })
            
        elif platform.system() in ['Linux', 'Darwin']:  # Linux or macOS
            # 使用/proc/meminfo（Linux）或sysctl（macOS）
            if platform.system() == 'Linux':
                try:
                    with open('/proc/meminfo', 'r') as f:
                        meminfo = f.read()
                    lines = meminfo.split('\n')
                    mem_dict = {}
                    for line in lines:
                        if ':' in line:
                            key, value = line.split(':', 1)
                            mem_dict[key.strip()] = value.strip()
                    
                    memory_info.update({
                        'total_physical': int(mem_dict.get('MemTotal', '0 kB').split()[0]) * 1024,
                        'available_physical': int(mem_dict.get('MemAvailable', '0 kB').split()[0]) * 1024,
                        'free_physical': int(mem_dict.get('MemFree', '0 kB').split()[0]) * 1024,
                    })
                except:
                    pass
            else:  # macOS
                try:
                    import subprocess
                    # 使用sysctl命令获取内存信息
                    total_phys = subprocess.check_output(['sysctl', '-n', 'hw.memsize']).decode().strip()
                    memory_info['total_physical'] = int(total_phys)
                except:
                    pass
    except Exception as e:
        memory_info['error'] = f"Failed to get memory info: {str(e)}"
    
    return memory_info


def _get_disk_info() -> Dict[str, Any]:
    """获取磁盘信息（跨平台）"""
    disk_info = {}
    
    try:
        if platform.system() == 'Windows':
            # Windows磁盘信息
            import ctypes
            drives = []
            bitmask = ctypes.windll.kernel32.GetLogicalDrives()
            for letter in range(26):
                if bitmask & 1:
                    drives.append(chr(65 + letter) + ':')
                bitmask >>= 1
            
            disk_info['drives'] = drives
            
            # 获取当前磁盘使用情况
            try:
                free_bytes = ctypes.c_ulonglong(0)
                total_bytes = ctypes.c_ulonglong(0)
                ctypes.windll.kernel32.GetDiskFreeSpaceExW(
                    ctypes.c_wchar_p(os.getcwd()[:2]), 
                    None, 
                    ctypes.byref(total_bytes), 
                    ctypes.byref(free_bytes)
                )
                disk_info['current_drive'] = {
                    'total_space': total_bytes.value,
                    'free_space': free_bytes.value,
                    'used_space': total_bytes.value - free_bytes.value,
                }
            except:
                pass
                
        else:  # Unix-like systems (Linux, macOS)
            # 使用os.statvfs获取磁盘信息
            try:
                stat = os.statvfs('/')
                disk_info['root_filesystem'] = {
                    'block_size': stat.f_frsize,
                    'total_blocks': stat.f_blocks,
                    'free_blocks': stat.f_bfree,
                    'available_blocks': stat.f_bavail,
                    'total_space': stat.f_blocks * stat.f_frsize,
                    'free_space': stat.f_bfree * stat.f_frsize,
                    'available_space': stat.f_bavail * stat.f_frsize,
                }
            except:
                pass
    except Exception as e:
        disk_info['error'] = f"Failed to get disk info: {str(e)}"
    
    return disk_info


def _get_network_info() -> Dict[str, Any]:
    """获取网络信息"""
    network_info = {}
    
    try:
        # 获取本地IP地址
        try:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            network_info['local_ip'] = local_ip
        except:
            network_info['local_ip'] = 'Unknown'
        
        # 获取所有网络接口的IP地址
        try:
            import netifaces
            # 注意：netifaces是第三方库，但我们不能使用
            # 这里使用socket的替代方法
            network_info['interfaces'] = 'Network interface details require netifaces library'
        except:
            network_info['interfaces'] = 'Network interface details not available without netifaces'
        
    except Exception as e:
        network_info['error'] = f"Failed to get network info: {str(e)}"
    
    return network_info


def format_system_info(info: Dict[str, Any]) -> str:
    """
    格式化系统信息为可读字符串
    
    Args:
        info: 系统信息字典
        
    Returns:
        str: 格式化的系统信息字符串
    """
    lines = []
    lines.append("=" * 60)
    lines.append("SYSTEM INFORMATION")
    lines.append("=" * 60)
    
    # 基本信息
    lines.append(f"Timestamp: {info.get('timestamp', 'Unknown')}")
    lines.append(f"Python Version: {info.get('python_version', 'Unknown').splitlines()[0]}")
    lines.append(f"Python Implementation: {info.get('python_implementation', 'Unknown')}")
    
    # 平台信息
    platform_info = info.get('platform', {})
    lines.append(f"Operating System: {platform_info.get('system', 'Unknown')} {platform_info.get('release', 'Unknown')}")
    lines.append(f"Architecture: {platform_info.get('machine', 'Unknown')}")
    lines.append(f"Platform: {platform_info.get('platform', 'Unknown')}")
    
    # 主机信息
    lines.append(f"Hostname: {info.get('hostname', 'Unknown')}")
    lines.append(f"FQDN: {info.get('fqdn', 'Unknown')}")
    lines.append(f"Current User: {info.get('current_user', 'Unknown')}")
    lines.append(f"Working Directory: {info.get('current_working_directory', 'Unknown')}")
    
    # CPU信息
    cpu_info = info.get('cpu', {})
    lines.append(f"CPU Count: {cpu_info.get('count', 'Unknown')}")
    
    # 内存信息
    memory_info = info.get('memory', {})
    if 'total_physical' in memory_info:
        total_gb = memory_info['total_physical'] / (1024**3)
        lines.append(f"Total Memory: {total_gb:.2f} GB")
    if 'available_physical' in memory_info:
        available_gb = memory_info['available_physical'] / (1024**3)
        lines.append(f"Available Memory: {available_gb:.2f} GB")
    
    # 磁盘信息
    disk_info = info.get('disk', {})
    if 'current_drive' in disk_info:
        drive_info = disk_info['current_drive']
        if 'total_space' in drive_info:
            total_gb = drive_info['total_space'] / (1024**3)
            free_gb = drive_info['free_space'] / (1024**3)
            lines.append(f"Current Drive - Total: {total_gb:.2f} GB, Free: {free_gb:.2f} GB")
    elif 'root_filesystem' in disk_info:
        fs_info = disk_info['root_filesystem']
        if 'total_space' in fs_info:
            total_gb = fs_info['total_space'] / (1024**3)
            free_gb = fs_info['free_space'] / (1024**3)
            lines.append(f"Root Filesystem - Total: {total_gb:.2f} GB, Free: {free_gb:.2f} GB")
    
    # 网络信息
    network_info = info.get('network', {})
    lines.append(f"Local IP: {network_info.get('local_ip', 'Unknown')}")
    
    lines.append("=" * 60)
    return '\n'.join(lines)


if __name__ == "__main__":
    # 测试代码
    info = system_info()
    print(format_system_info(info))