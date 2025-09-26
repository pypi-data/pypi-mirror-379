"""
路径存在性检查模块 - 检查路径是否存在及其类型
仅使用Python标准库，支持Windows、Linux、macOS
"""

import os
from typing import Dict, Any


def path_exist(path: str) -> Dict[str, Any]:
    """
    检查路径是否存在及其类型
    
    Args:
        path: 要检查的路径字符串
        
    Returns:
        Dict[str, Any]: 包含路径检查结果的字典，包含以下字段：
            - exists: bool - 路径是否存在
            - type: str - 路径类型（file, directory, not_exist）
            - absolute_path: str - 绝对路径
            - error: str - 错误信息（如果发生错误）
    """
    result = {
        'exists': False,
        'type': 'not_exist',
        'absolute_path': '',
        'error': ''
    }
    
    if not path:
        result['error'] = '路径不能为空'
        return result
    
    try:
        # 检查路径是否存在
        if not os.path.exists(path):
            result['exists'] = False
            result['type'] = 'not_exist'
            result['absolute_path'] = os.path.abspath(path) if path else ''
            return result
        
        result['exists'] = True
        result['absolute_path'] = os.path.abspath(path)
        
        # 判断路径类型
        if os.path.isfile(path):
            result['type'] = 'file'
        elif os.path.isdir(path):
            result['type'] = 'directory'
        else:
            result['type'] = 'other'
        
    except Exception as e:
        result['error'] = f"检查路径时发生错误: {str(e)}"
    
    return result


def format_path_info(info: Dict[str, Any]) -> str:
    """
    格式化路径信息为可读字符串
    
    Args:
        info: 路径信息字典
        
    Returns:
        str: 格式化的路径信息字符串
    """
    if info.get('error'):
        return f"错误: {info['error']}"
    
    exists_text = "存在" if info.get('exists') else "不存在"
    type_text = {
        'file': '文件',
        'directory': '目录', 
        'not_exist': '不存在',
        'other': '其他类型'
    }.get(info.get('type', 'not_exist'), '未知类型')
    
    return f"绝对路径: {info.get('absolute_path', 'Unknown')}\n是否存在: {exists_text}\n路径类型: {type_text}"


# 便捷函数
def path_exists(path: str) -> bool:
    """检查路径是否存在（简化版）"""
    try:
        return os.path.exists(path)
    except:
        return False


def is_file(path: str) -> bool:
    """检查路径是否是文件"""
    try:
        return os.path.isfile(path)
    except:
        return False


def is_directory(path: str) -> bool:
    """检查路径是否是目录"""
    try:
        return os.path.isdir(path)
    except:
        return False


if __name__ == "__main__":
    # 测试代码
    test_paths = [
        ".",  # 当前目录
        __file__,  # 当前文件
        "/nonexistent/path",  # 不存在的路径
        "/",  # 根目录
    ]
    
    print("路径存在性检查测试")
    print("=" * 40)
    
    for test_path in test_paths:
        print(f"待测试路径: {test_path}")
        result = path_exist(test_path)
        print(format_path_info(result))
        print("-" * 40)