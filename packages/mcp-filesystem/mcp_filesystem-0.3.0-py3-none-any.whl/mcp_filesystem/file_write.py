"""
文件写入模块 - 写入文件内容，支持跨平台文件写入
仅使用Python标准库，支持Windows、Linux、macOS
支持覆盖写入、追加写入和指定位置插入三种模式
"""

import os
import tempfile
import shutil
from typing import Dict, Any, Optional, List, Union


def file_write(file_path: str,
               content: Union[str, List[str]],
               mode: str = 'overwrite',
               line_number: Optional[int] = None,
               encoding: str = 'utf-8',
               create_parents: bool = True,
               backup_original: bool = False) -> Dict[str, Any]:
    """
    写入文件内容，支持覆盖写入、追加写入和指定位置插入
    
    Args:
        file_path: 文件路径
        content: 要写入的内容，可以是字符串或字符串列表
        mode: 写入模式 - 'overwrite'(覆盖), 'append'(追加), 'insert'(插入)
        line_number: 插入模式下的行号（从1开始）
        encoding: 文件编码
        create_parents: 是否自动创建父目录
        backup_original: 是否备份原文件
    
    Returns:
        Dict[str, Any]: 包含写入结果的字典
            - success: bool - 是否成功写入
            - file_path: str - 文件路径
            - bytes_written: int - 写入的字节数
            - mode: str - 使用的写入模式
            - line_number: int - 插入的行号（仅插入模式）
            - encoding: str - 使用的编码
            - backup_file: str - 备份文件路径（如果启用了备份）
            - error: str - 错误信息
            - warning: str - 警告信息
    """
    
    result = {
        'success': False,
        'file_path': file_path,
        'bytes_written': 0,
        'mode': mode,
        'line_number': line_number,
        'encoding': encoding,
        'backup_file': '',
        'error': '',
        'warning': ''
    }
    
    # 参数验证
    validation_error = _validate_parameters(file_path, content, mode, line_number, encoding)
    if validation_error:
        result['error'] = validation_error
        return result
    
    # 规范化内容格式
    if isinstance(content, list):
        content_str = '\n'.join(content)
    else:
        content_str = content
    
    try:
        # 检查并创建父目录
        if create_parents:
            parent_dir = os.path.dirname(file_path)
            if parent_dir and not os.path.exists(parent_dir):
                os.makedirs(parent_dir, exist_ok=True)
                result['warning'] = f'已创建父目录: {parent_dir}'
        
        # 备份原文件（如果存在且启用了备份）
        backup_path = ''
        if backup_original and os.path.exists(file_path):
            backup_path = _create_backup(file_path)
            result['backup_file'] = backup_path
        
        # 根据模式执行写入操作
        if mode == 'overwrite':
            return _write_overwrite(file_path, content_str, encoding, result)
        elif mode == 'append':
            return _write_append(file_path, content_str, encoding, result)
        elif mode == 'insert':
            return _write_insert(file_path, content_str, line_number, encoding, result)
        else:
            result['error'] = f'不支持的写入模式: {mode}'
            return result
            
    except Exception as e:
        result['error'] = f'写入文件时发生错误: {str(e)}'
        # 如果备份存在但写入失败，尝试恢复备份
        if backup_path and os.path.exists(backup_path):
            try:
                shutil.copy2(backup_path, file_path)
                result['warning'] += ' 已从备份恢复原文件'
            except Exception as restore_error:
                result['warning'] += f' 备份恢复失败: {str(restore_error)}'
        return result


def _validate_parameters(file_path: str, content: Union[str, List[str]], 
                        mode: str, line_number: Optional[int], encoding: str) -> str:
    """验证参数有效性"""
    
    if not file_path:
        return '文件路径不能为空'
    
    if content is None:
        return '写入内容不能为空'
    
    if isinstance(content, list) and len(content) == 0:
        return '写入内容列表不能为空'
    
    if isinstance(content, str) and len(content.strip()) == 0:
        return '写入内容不能为空字符串'
    
    if mode not in ['overwrite', 'append', 'insert']:
        return f'不支持的写入模式: {mode}，支持的模式: overwrite, append, insert'
    
    if mode == 'insert' and line_number is None:
        return '插入模式必须指定行号'
    
    if mode == 'insert' and line_number is not None and line_number < 1:
        return '行号必须大于等于1'
    
    # 检查编码有效性
    try:
        # 测试编码是否有效
        test_content = "test"
        test_content.encode(encoding)
    except LookupError:
        return f'不支持的编码: {encoding}'
    
    return ''


def _create_backup(file_path: str) -> str:
    """创建文件备份"""
    
    backup_dir = os.path.join(os.path.dirname(file_path), '.backups')
    os.makedirs(backup_dir, exist_ok=True)
    
    filename = os.path.basename(file_path)
    timestamp = str(int(os.path.getmtime(file_path)))
    backup_filename = f"{filename}.backup.{timestamp}"
    backup_path = os.path.join(backup_dir, backup_filename)
    
    shutil.copy2(file_path, backup_path)
    return backup_path


def _write_overwrite(file_path: str, content: str, encoding: str, 
                    result: Dict[str, Any]) -> Dict[str, Any]:
    """覆盖写入模式"""
    
    try:
        # 计算实际字节数
        content_bytes = content.encode(encoding)
        bytes_written = len(content_bytes)
        
        with open(file_path, 'w', encoding=encoding) as f:
            f.write(content)
        
        result['success'] = True
        result['bytes_written'] = bytes_written
        return result
        
    except Exception as e:
        result['error'] = f'覆盖写入失败: {str(e)}'
        return result


def _write_append(file_path: str, content: str, encoding: str, 
                 result: Dict[str, Any]) -> Dict[str, Any]:
    """追加写入模式"""
    
    try:
        # 检查文件是否存在，如果不存在则创建
        file_exists = os.path.exists(file_path)
        
        # 计算要追加内容的字节数
        content_bytes = content.encode(encoding)
        bytes_to_append = len(content_bytes)
        
        with open(file_path, 'a', encoding=encoding) as f:
            # 如果文件已存在且不为空，在追加前添加换行符
            if file_exists and os.path.getsize(file_path) > 0:
                # 检查文件最后是否已有换行符
                with open(file_path, 'r', encoding=encoding) as read_f:
                    lines = read_f.readlines()
                    if lines and not lines[-1].endswith('\n'):
                        f.write('\n')
                        bytes_to_append += len('\n'.encode(encoding))
            
            f.write(content)
        
        result['success'] = True
        result['bytes_written'] = bytes_to_append
        return result
        
    except Exception as e:
        result['error'] = f'追加写入失败: {str(e)}'
        return result


def _write_insert(file_path: str, content: str, line_number: int, 
                 encoding: str, result: Dict[str, Any]) -> Dict[str, Any]:
    """指定位置插入模式"""
    
    try:
        # 读取原文件内容
        original_lines = []
        file_exists = os.path.exists(file_path)
        
        if file_exists:
            with open(file_path, 'r', encoding=encoding) as f:
                original_lines = f.readlines()
        
        # 调整行号到有效范围
        adjusted_line_number = max(1, min(line_number, len(original_lines) + 1))
        if adjusted_line_number != line_number:
            result['warning'] = f'行号已调整到有效范围: {adjusted_line_number}'
            result['line_number'] = adjusted_line_number
        
        # 分割插入内容为行
        insert_lines = content.split('\n')
        if content.endswith('\n'):
            insert_lines = insert_lines[:-1]  # 移除最后的空行
        
        # 构建新内容
        new_lines = []
        
        # 插入位置之前的行
        new_lines.extend(original_lines[:adjusted_line_number - 1])
        
        # 插入的内容
        for i, line in enumerate(insert_lines):
            if i == len(insert_lines) - 1 and not content.endswith('\n'):
                new_lines.append(line)  # 最后一行不加换行符
            else:
                new_lines.append(line + '\n')
        
        # 插入位置之后的行
        new_lines.extend(original_lines[adjusted_line_number - 1:])
        
        # 写入新内容
        new_content = ''.join(new_lines)
        content_bytes = new_content.encode(encoding)
        bytes_written = len(content_bytes)
        
        with open(file_path, 'w', encoding=encoding) as f:
            f.write(new_content)
        
        result['success'] = True
        result['bytes_written'] = bytes_written
        return result
        
    except Exception as e:
        result['error'] = f'插入写入失败: {str(e)}'
        return result


def write_file_overwrite(file_path: str, content: Union[str, List[str]], 
                        encoding: str = 'utf-8') -> Dict[str, Any]:
    """
    覆盖写入文件的便捷函数
    
    Args:
        file_path: 文件路径
        content: 要写入的内容
        encoding: 文件编码
    
    Returns:
        Dict[str, Any]: 写入结果
    """
    return file_write(file_path, content, mode='overwrite', encoding=encoding)


def write_file_append(file_path: str, content: Union[str, List[str]], 
                     encoding: str = 'utf-8') -> Dict[str, Any]:
    """
    追加写入文件的便捷函数
    
    Args:
        file_path: 文件路径
        content: 要追加的内容
        encoding: 文件编码
    
    Returns:
        Dict[str, Any]: 写入结果
    """
    return file_write(file_path, content, mode='append', encoding=encoding)


def write_file_insert(file_path: str, content: Union[str, List[str]], 
                     line_number: int, encoding: str = 'utf-8') -> Dict[str, Any]:
    """
    在指定行插入内容的便捷函数
    
    Args:
        file_path: 文件路径
        content: 要插入的内容
        line_number: 插入的行号（从1开始）
        encoding: 文件编码
    
    Returns:
        Dict[str, Any]: 写入结果
    """
    return file_write(file_path, content, mode='insert', line_number=line_number, 
                     encoding=encoding)


def format_write_result(result: Dict[str, Any]) -> str:
    """
    格式化写入结果为可读字符串
    
    Args:
        result: 写入结果字典
    
    Returns:
        str: 格式化的结果字符串
    """
    
    lines = []
    lines.append("=" * 60)
    lines.append("FILE WRITE RESULT")
    lines.append("=" * 60)
    
    lines.append(f"成功: {'是' if result.get('success') else '否'}")
    lines.append(f"文件路径: {result.get('file_path', '')}")
    lines.append(f"写入模式: {result.get('mode', '')}")
    
    if result.get('line_number'):
        lines.append(f"插入行号: {result['line_number']}")
    
    if result.get('error'):
        lines.append(f"错误: {result['error']}")
    
    if result.get('warning'):
        lines.append(f"警告: {result['warning']}")
    
    lines.append(f"写入字节数: {result.get('bytes_written', 0)}")
    lines.append(f"编码: {result.get('encoding', 'Unknown')}")
    
    if result.get('backup_file'):
        lines.append(f"备份文件: {result['backup_file']}")
    
    lines.append("=" * 60)
    return '\n'.join(lines)


if __name__ == "__main__":
    # 测试代码
    print("文件写入功能测试")
    print("=" * 60)
    
    # 创建测试目录
    test_dir = "test_write_files"
    os.makedirs(test_dir, exist_ok=True)
    
    # 测试用例
    test_cases = [
        {
            'name': '覆盖写入新文件',
            'file': os.path.join(test_dir, 'test_overwrite_new.txt'),
            'content': '这是覆盖写入的新文件内容\n第二行',
            'mode': 'overwrite'
        },
        {
            'name': '覆盖写入已存在文件',
            'file': os.path.join(test_dir, 'test_overwrite_exist.txt'),
            'content': ['第一行', '第二行', '第三行'],
            'mode': 'overwrite'
        },
        {
            'name': '追加写入',
            'file': os.path.join(test_dir, 'test_append.txt'),
            'content': '这是追加的内容',
            'mode': 'append'
        },
        {
            'name': '在第二行插入',
            'file': os.path.join(test_dir, 'test_insert.txt'),
            'content': '插入的内容',
            'mode': 'insert',
            'line_number': 2
        },
        {
            'name': '错误测试 - 空路径',
            'file': '',
            'content': '测试内容',
            'mode': 'overwrite'
        },
        {
            'name': '错误测试 - 无效模式',
            'file': os.path.join(test_dir, 'test_invalid_mode.txt'),
            'content': '测试内容',
            'mode': 'invalid_mode'
        }
    ]
    
    # 先创建一些测试文件
    for test_case in test_cases[1:4]:  # 为存在文件的测试用例创建初始文件
        if test_case['file'] and not test_case['file'].startswith('test_invalid'):
            with open(test_case['file'], 'w', encoding='utf-8') as f:
                f.write("初始内容\n第二行初始内容\n第三行初始内容")
    
    # 执行测试
    for i, test_case in enumerate(test_cases, 1):
        print(f"测试 {i}: {test_case['name']}")
        print(f"文件: {test_case['file']}")
        
        kwargs = {
            'file_path': test_case['file'],
            'content': test_case['content'],
            'mode': test_case['mode'],
            'encoding': 'utf-8'
        }
        
        if test_case['mode'] == 'insert' and 'line_number' in test_case:
            kwargs['line_number'] = test_case['line_number']
        
        result = file_write(**kwargs)
        print(format_write_result(result))
        print()
    
    # 清理测试文件
    try:
        shutil.rmtree(test_dir)
        print(f"已清理测试目录: {test_dir}")
    except Exception as e:
        print(f"清理测试目录失败: {e}")