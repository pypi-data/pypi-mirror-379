"""
目录树模块 - 获取目录树结构，包括所有子目录和文件
仅使用Python标准库，支持Windows、Linux、macOS
"""

import os
import platform
import stat
import datetime
from typing import Dict, Any, List, Optional, Union


def directory_tree(root_path: str, 
                  max_depth: int = -1,
                  include_files: bool = True,
                  include_directories: bool = True,
                  sort_by: str = 'name',
                  reverse: bool = False) -> Dict[str, Any]:
    """
    获取目录树结构
    
    Args:
        root_path: 根目录路径
        max_depth: 最大遍历深度，-1表示无限制
        include_files: 是否包含文件
        include_directories: 是否包含目录
        sort_by: 排序方式 ('name', 'size', 'modified')
        reverse: 是否反向排序
        
    Returns:
        Dict[str, Any]: 包含目录树结果的字典，包含以下字段：
            - success: bool - 操作是否成功
            - root: str - 根目录的绝对路径
            - total_directories: int - 总目录数（包括根目录）
            - total_files: int - 总文件数
            - tree: Dict - 目录树结构
            - error: str - 错误信息（如果发生错误）
    """
    result = {
        'success': False,
        'root': '',
        'total_directories': 0,
        'total_files': 0,
        'tree': {},
        'error': ''
    }
    
    if not root_path:
        result['error'] = '根目录路径不能为空'
        return result
    
    try:
        # 获取根目录的绝对路径
        abs_path = os.path.abspath(root_path)
        result['root'] = abs_path
        
        # 检查目录是否存在
        if not os.path.exists(abs_path):
            result['error'] = f'目录不存在: {abs_path}'
            return result
        
        # 检查是否为目录
        if not os.path.isdir(abs_path):
            result['error'] = f'路径不是目录: {abs_path}'
            return result
        
        # 构建目录树
        tree, dir_count, file_count = _build_directory_tree(
            abs_path, 
            max_depth, 
            include_files, 
            include_directories,
            sort_by,
            reverse,
            current_depth=0
        )
        
        result['tree'] = tree
        result['total_directories'] = dir_count
        result['total_files'] = file_count
        result['success'] = True
        
    except PermissionError as e:
        result['error'] = f'权限不足，无法访问目录: {str(e)}'
    except Exception as e:
        result['error'] = f'构建目录树时发生错误: {str(e)}'
    
    return result


def _build_directory_tree(path: str, 
                         max_depth: int,
                         include_files: bool,
                         include_directories: bool,
                         sort_by: str,
                         reverse: bool,
                         current_depth: int = 0) -> tuple:
    """
    递归构建目录树
    
    Returns:
        tuple: (树节点字典, 目录计数, 文件计数)
    """
    # 检查深度限制
    if max_depth >= 0 and current_depth > max_depth:
        return {}, 0, 0
    
    try:
        # 获取当前目录的基本信息
        node = _get_directory_node(path)
        dir_count = 1  # 当前目录
        file_count = 0
        
        children = []
        
        # 遍历目录内容
        for item_name in os.listdir(path):
            item_path = os.path.join(path, item_name)
            
            try:
                if os.path.isdir(item_path):
                    # 处理子目录
                    if include_directories:
                        child_node, child_dir_count, child_file_count = _build_directory_tree(
                            item_path, 
                            max_depth, 
                            include_files, 
                            include_directories,
                            sort_by,
                            reverse,
                            current_depth + 1
                        )
                        if child_node:
                            children.append(child_node)
                            dir_count += child_dir_count
                            file_count += child_file_count
                else:
                    # 处理文件
                    if include_files:
                        file_node = _get_file_node(item_path, item_name)
                        children.append(file_node)
                        file_count += 1
                        
            except PermissionError:
                # 跳过无权限访问的项目
                continue
            except Exception:
                # 跳过其他错误
                continue
        
        # 排序子节点
        if children:
            node['children'] = _sort_tree_nodes(children, sort_by, reverse)
        else:
            node['children'] = []
        
        return node, dir_count, file_count
        
    except PermissionError:
        # 无权限访问目录，返回空节点
        return _get_directory_node(path, accessible=False), 1, 0
    except Exception:
        # 其他错误，返回空节点
        return _get_directory_node(path, accessible=False), 1, 0


def _get_directory_node(path: str, accessible: bool = True) -> Dict[str, Any]:
    """获取目录节点信息"""
    node = {
        'name': os.path.basename(path),
        'path': path,
        'type': 'directory',
        'accessible': accessible,
        'children': [],
        'size': 0,
        'last_modified': '',
        'last_modified_timestamp': 0,
        'permissions': {},
        'owner': 'Unknown',
        'group': 'Unknown'
    }
    
    if not accessible:
        return node
    
    try:
        # 获取目录状态信息
        dir_stat = os.stat(path)
        
        # 最后修改时间
        node['last_modified'] = datetime.datetime.fromtimestamp(
            dir_stat.st_mtime
        ).isoformat()
        node['last_modified_timestamp'] = dir_stat.st_mtime
        
        # 权限信息
        node['permissions'] = _get_permissions_info(dir_stat.st_mode)
        
        # 所有者和组信息
        owner, group = _get_owner_group_info(dir_stat)
        node['owner'] = owner
        node['group'] = group
        
    except Exception as e:
        node['error'] = f'获取目录信息时发生错误: {str(e)}'
    
    return node


def _get_file_node(path: str, name: str) -> Dict[str, Any]:
    """获取文件节点信息"""
    node = {
        'name': name,
        'path': path,
        'type': 'file',
        'accessible': True,
        'size': 0,
        'last_modified': '',
        'last_modified_timestamp': 0,
        'permissions': {},
        'owner': 'Unknown',
        'group': 'Unknown'
    }
    
    try:
        # 获取文件状态信息
        file_stat = os.stat(path)
        
        node['size'] = file_stat.st_size
        
        # 最后修改时间
        node['last_modified'] = datetime.datetime.fromtimestamp(
            file_stat.st_mtime
        ).isoformat()
        node['last_modified_timestamp'] = file_stat.st_mtime
        
        # 权限信息
        node['permissions'] = _get_permissions_info(file_stat.st_mode)
        
        # 所有者和组信息
        owner, group = _get_owner_group_info(file_stat)
        node['owner'] = owner
        node['group'] = group
        
    except Exception as e:
        node['error'] = f'获取文件信息时发生错误: {str(e)}'
        node['accessible'] = False
    
    return node


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


def _sort_tree_nodes(nodes: List[Dict], sort_by: str, reverse: bool) -> List[Dict]:
    """对树节点列表进行排序"""
    if not nodes:
        return nodes
    
    # 定义排序键函数
    sort_functions = {
        'name': lambda x: x['name'].lower(),
        'size': lambda x: x.get('size', 0),
        'modified': lambda x: x.get('last_modified_timestamp', 0)
    }
    
    sort_key = sort_functions.get(sort_by, sort_functions['name'])
    
    try:
        sorted_nodes = sorted(nodes, key=sort_key, reverse=reverse)
    except Exception:
        # 如果排序失败，按名称排序
        sorted_nodes = sorted(nodes, key=lambda x: x['name'].lower(), reverse=reverse)
    
    return sorted_nodes


def format_directory_tree(result: Dict[str, Any], indent: str = "  ") -> str:
    """
    格式化目录树结果为可读字符串
    
    Args:
        result: 目录树结果字典
        indent: 缩进字符串
        
    Returns:
        str: 格式化的树形结构字符串
    """
    if result.get('error'):
        return f"错误: {result['error']}"
    
    if not result.get('success'):
        return "操作失败"
    
    lines = []
    lines.append("=" * 80)
    lines.append("DIRECTORY TREE")
    lines.append("=" * 80)
    
    lines.append(f"根目录: {result.get('root', 'Unknown')}")
    lines.append(f"总目录数: {result.get('total_directories', 0)}")
    lines.append(f"总文件数: {result.get('total_files', 0)}")
    lines.append("")
    
    tree = result.get('tree', {})
    if not tree:
        lines.append("目录为空")
    else:
        lines.extend(_format_tree_node(tree, "", indent))
    
    lines.append("=" * 80)
    return '\n'.join(lines)


def _format_tree_node(node: Dict[str, Any], prefix: str, indent: str) -> List[str]:
    """递归格式化树节点"""
    lines = []
    
    # 当前节点显示
    name = node.get('name', 'Unknown')
    node_type = node.get('type', 'unknown')
    accessible = node.get('accessible', True)
    
    if not accessible:
        line = f"{prefix}{name}/ [权限不足]"
    elif node_type == 'directory':
        line = f"{prefix}{name}/"
    else:
        # 文件节点显示大小
        size = node.get('size', 0)
        if size >= 1024**3:
            size_str = f"{size / (1024**3):.1f}G"
        elif size >= 1024**2:
            size_str = f"{size / (1024**2):.1f}M"
        elif size >= 1024:
            size_str = f"{size / 1024:.1f}K"
        else:
            size_str = f"{size}B"
        line = f"{prefix}{name} ({size_str})"
    
    lines.append(line)
    
    # 处理子节点
    children = node.get('children', [])
    if children:
        for i, child in enumerate(children):
            is_last = i == len(children) - 1
            child_prefix = prefix + ("└── " if is_last else "├── ")
            child_indent = prefix + ("    " if is_last else "│   ")
            lines.extend(_format_tree_node(child, child_prefix, child_indent))
    
    return lines


def get_tree_size(tree: Dict[str, Any]) -> int:
    """
    计算目录树的总大小（递归计算所有文件大小）
    
    Args:
        tree: 目录树节点
        
    Returns:
        int: 总大小（字节）
    """
    total_size = 0
    
    if tree.get('type') == 'file':
        total_size += tree.get('size', 0)
    elif tree.get('type') == 'directory':
        for child in tree.get('children', []):
            total_size += get_tree_size(child)
    
    return total_size


def find_in_tree(tree: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    """
    在目录树中查找指定名称的项目
    
    Args:
        tree: 目录树节点
        name: 要查找的名称（支持通配符匹配）
        
    Returns:
        List[Dict]: 匹配的项目列表
    """
    matches = []
    
    # 简单的通配符匹配
    if '*' in name or '?' in name:
        import fnmatch
        if fnmatch.fnmatch(tree.get('name', ''), name):
            matches.append(tree)
    else:
        # 精确匹配
        if tree.get('name') == name:
            matches.append(tree)
    
    # 递归查找子节点
    for child in tree.get('children', []):
        matches.extend(find_in_tree(child, name))
    
    return matches


if __name__ == "__main__":
    # 测试代码
    print("目录树功能测试")
    print("=" * 60)
    
    # 测试用例
    test_cases = [
        (".", -1, True, True, 'name', False),      # 当前目录，无深度限制
        (".", 1, True, True, 'name', False),       # 当前目录，深度1
        (".", 0, True, True, 'name', False),       # 当前目录，深度0（只显示根目录）
        (".", -1, True, False, 'name', False),     # 只显示文件
        (".", -1, False, True, 'name', False),     # 只显示目录
        (".", -1, True, True, 'size', True),       # 按大小反向排序
        ("/nonexistent", -1, True, True, 'name', False),  # 不存在的目录
        ("", -1, True, True, 'name', False),       # 空路径
    ]
    
    for i, (root_path, max_depth, include_files, include_dirs, sort_by, reverse) in enumerate(test_cases, 1):
        print(f"测试用例 {i}:")
        print(f"  根目录: {root_path}")
        print(f"  最大深度: {max_depth}")
        print(f"  包含文件: {include_files}")
        print(f"  包含目录: {include_dirs}")
        print(f"  排序: {sort_by}")
        print(f"  反向: {reverse}")
        
        result = directory_tree(root_path, max_depth, include_files, include_dirs, sort_by, reverse)
        print(format_directory_tree(result))
        print()
    
    # 测试辅助函数
    print("辅助函数测试:")
    result = directory_tree(".", max_depth=-1)  # 使用无深度限制以包含所有文件
    if result['success']:
        tree = result['tree']
        total_size = get_tree_size(tree)
        print(f"目录树总大小: {total_size} bytes")
        
        # 查找测试
        matches = find_in_tree(tree, "*.py")
        print(f"找到 {len(matches)} 个Python文件")
        for match in matches[:3]:  # 显示前3个匹配项
            print(f"  - {match.get('name')}")