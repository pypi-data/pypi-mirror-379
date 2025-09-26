"""
目录查找模块 - 在指定目录中递归查找匹配的目录名
仅使用Python标准库，支持Windows、Linux、macOS
"""

import os
import platform
import re
from typing import Dict, Any, List, Optional


def directory_find(search_directory: str, directory_name: str, 
                  case_sensitive: bool = False, max_depth: Optional[int] = None) -> Dict[str, Any]:
    """
    在指定目录中递归查找匹配的目录名
    
    Args:
        search_directory: 要搜索的目录路径
        directory_name: 要查找的目录名（支持通配符*和?）
        case_sensitive: 是否区分大小写（默认不区分）
        max_depth: 最大搜索深度（None表示无限制）
        
    Returns:
        Dict[str, Any]: 包含查找结果的字典，包含以下字段：
            - success: bool - 搜索是否成功
            - search_directory: str - 搜索目录的绝对路径
            - directory_name: str - 要查找的目录名
            - matches: List[str] - 匹配的目录绝对路径列表
            - count: int - 匹配的目录数量
            - total_directories_searched: int - 总共搜索的目录数量
            - max_depth_reached: bool - 是否达到最大深度限制
            - error: str - 错误信息（如果发生错误）
    """
    result = {
        'success': False,
        'search_directory': '',
        'directory_name': directory_name,
        'matches': [],
        'count': 0,
        'total_directories_searched': 0,
        'max_depth_reached': False,
        'error': ''
    }
    
    if not search_directory or not directory_name:
        result['error'] = '搜索目录和目录名不能为空'
        return result
    
    try:
        # 获取搜索目录的绝对路径
        search_directory_abs = os.path.abspath(search_directory)
        result['search_directory'] = search_directory_abs
        
        # 检查搜索目录是否存在
        if not os.path.exists(search_directory_abs):
            result['error'] = f'搜索目录不存在: {search_directory_abs}'
            return result
        
        # 检查搜索目录是否为目录
        if not os.path.isdir(search_directory_abs):
            result['error'] = f'搜索路径不是目录: {search_directory_abs}'
            return result
        
        # 预处理目录名（处理通配符）
        pattern = directory_name
        if not case_sensitive:
            pattern = pattern.lower()
        
        # 递归搜索目录
        matches, total_searched, max_depth_reached = _recursive_directory_search(
            search_directory_abs, pattern, case_sensitive, max_depth, 0
        )
        
        result['matches'] = matches
        result['count'] = len(matches)
        result['total_directories_searched'] = total_searched
        result['max_depth_reached'] = max_depth_reached
        result['success'] = True
        
    except Exception as e:
        result['error'] = f"目录查找时发生错误: {str(e)}"
    
    return result


def _recursive_directory_search(current_dir: str, pattern: str, case_sensitive: bool,
                               max_depth: Optional[int], current_depth: int) -> tuple:
    """
    递归搜索目录
    
    Args:
        current_dir: 当前搜索目录
        pattern: 目录名模式
        case_sensitive: 是否区分大小写
        max_depth: 最大深度
        current_depth: 当前深度
        
    Returns:
        tuple: (匹配目录列表, 总共搜索的目录数量, 是否达到最大深度)
    """
    matches = []
    total_searched = 0
    max_depth_reached = False
    
    # 检查深度限制
    if max_depth is not None and current_depth > max_depth:
        return matches, total_searched, True
    
    try:
        # 遍历当前目录
        for item in os.listdir(current_dir):
            item_path = os.path.join(current_dir, item)
            
            # 只处理目录
            if os.path.isdir(item_path):
                total_searched += 1
                
                # 检查目录名是否匹配
                item_name = item if case_sensitive else item.lower()
                if _pattern_match(item_name, pattern):
                    matches.append(item_path)
                
                # 递归搜索子目录
                if max_depth is None or current_depth < max_depth:
                    sub_matches, sub_searched, sub_max_depth = _recursive_directory_search(
                        item_path, pattern, case_sensitive, max_depth, current_depth + 1
                    )
                    matches.extend(sub_matches)
                    total_searched += sub_searched
                    if sub_max_depth:
                        max_depth_reached = True
                        
    except (PermissionError, OSError):
        # 忽略权限错误和系统错误，继续搜索其他目录
        pass
    
    return matches, total_searched, max_depth_reached


def _pattern_match(name: str, pattern: str) -> bool:
    """
    简单的通配符匹配函数
    支持 *（匹配任意字符）和 ?（匹配单个字符）
    
    Args:
        name: 要匹配的名称
        pattern: 模式字符串
        
    Returns:
        bool: 是否匹配
    """
    if pattern == '*':
        return True
    
    # 将通配符模式转换为正则表达式
    # 转义特殊字符，然后将*替换为.*，?替换为.
    regex_pattern = '^' + re.escape(pattern).replace('\\*', '.*').replace('\\?', '.') + '$'
    
    # 使用re模块进行匹配
    return re.match(regex_pattern, name) is not None


def format_directory_find(result: Dict[str, Any]) -> str:
    """
    格式化目录查找结果为可读字符串
    
    Args:
        result: 目录查找结果字典
        
    Returns:
        str: 格式化的查找结果字符串
    """
    if result.get('error'):
        return f"错误: {result['error']}"
    
    if not result.get('success'):
        return "搜索失败"
    
    lines = []
    lines.append("=" * 60)
    lines.append("DIRECTORY FIND RESULTS")
    lines.append("=" * 60)
    
    lines.append(f"搜索目录: {result.get('search_directory', 'Unknown')}")
    lines.append(f"目标目录名: {result.get('directory_name', 'Unknown')}")
    lines.append(f"搜索状态: {'成功' if result.get('success') else '失败'}")
    lines.append(f"匹配数量: {result.get('count', 0)}")
    lines.append(f"搜索目录总数: {result.get('total_directories_searched', 0)}")
    
    if result.get('max_depth_reached'):
        lines.append("注意: 已达到最大搜索深度限制")
    
    matches = result.get('matches', [])
    if matches:
        lines.append("匹配的目录:")
        for i, match in enumerate(matches, 1):
            lines.append(f"  {i}. {match}")
    else:
        lines.append("未找到匹配的目录")
    
    lines.append("=" * 60)
    return '\n'.join(lines)


# 便捷函数
def find_directories(search_directory: str, directory_name: str) -> List[str]:
    """
    查找目录的简化版本
    
    Args:
        search_directory: 搜索目录
        directory_name: 目录名
        
    Returns:
        List[str]: 匹配的目录路径列表
    """
    try:
        result = directory_find(search_directory, directory_name)
        return result.get('matches', []) if result.get('success') else []
    except:
        return []


def find_directory(search_directory: str, directory_name: str) -> Optional[str]:
    """
    查找单个目录（返回第一个匹配项）
    
    Args:
        search_directory: 搜索目录
        directory_name: 目录名
        
    Returns:
        Optional[str]: 第一个匹配的目录路径，如果没有则返回None
    """
    try:
        result = directory_find(search_directory, directory_name)
        matches = result.get('matches', []) if result.get('success') else []
        return matches[0] if matches else None
    except:
        return None


def directory_exists_in_path(search_directory: str, directory_name: str) -> bool:
    """
    检查指定目录中是否存在匹配的目录
    
    Args:
        search_directory: 搜索目录
        directory_name: 目录名
        
    Returns:
        bool: 是否存在匹配的目录
    """
    try:
        result = directory_find(search_directory, directory_name)
        return result.get('count', 0) > 0 if result.get('success') else False
    except:
        return False


if __name__ == "__main__":
    # 测试代码
    print("目录查找功能测试")
    print("=" * 60)
    
    # 测试用例
    test_cases = [
        (".", "src", True, None),  # 在当前目录查找src目录
        (".", "*py*", False, 2),   # 查找所有包含py的目录（最大深度2）
        (".", "test_*", False, 1), # 查找以test_开头的目录
        ("/nonexistent", "src", False, None),  # 不存在的目录
        (".", "", False, None),    # 空目录名
    ]
    
    for i, (search_dir, dir_name, case_sensitive, max_depth) in enumerate(test_cases, 1):
        print(f"测试用例 {i}:")
        print(f"  搜索目录: {search_dir}")
        print(f"  目录名: {dir_name}")
        print(f"  区分大小写: {case_sensitive}")
        print(f"  最大深度: {max_depth}")
        
        result = directory_find(search_dir, dir_name, case_sensitive, max_depth)
        print(format_directory_find(result))
        print()