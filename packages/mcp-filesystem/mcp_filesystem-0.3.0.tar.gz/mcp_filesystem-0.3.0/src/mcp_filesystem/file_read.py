"""
文件读取模块 - 读取文件内容，支持跨平台文件读取
仅使用Python标准库，支持Windows、Linux、macOS
支持读取文本文件，处理超长文件，支持读取所有行或特定范围的行
"""

import os
import sys
import codecs
from typing import Dict, Any, List, Optional, Tuple, Union


def file_read(file_path: str, 
             start_line: Optional[int] = None, 
             end_line: Optional[int] = None,
             max_file_size: int = 100 * 1024 * 1024,  # 默认最大100MB
             encoding: str = 'utf-8',
             fallback_encodings: List[str] = None) -> Dict[str, Any]:
    """
    读取文件内容，支持读取所有行或特定范围的行
    
    Args:
        file_path: 文件路径
        start_line: 起始行号（从1开始，包含）
        end_line: 结束行号（包含）
        max_file_size: 最大文件大小（字节），超过此大小会进行特殊处理
        encoding: 首选编码
        fallback_encodings: 备选编码列表
    
    Returns:
        Dict[str, Any]: 包含读取结果的字典
            - success: bool - 是否成功读取
            - content: str - 文件内容（如果成功）
            - lines: List[str] - 文件行列表（如果成功）
            - total_lines: int - 总行数
            - file_size: int - 文件大小
            - encoding: str - 实际使用的编码
            - is_truncated: bool - 是否因文件过大被截断
            - truncated_size: int - 截断前的大小
            - error: str - 错误信息
            - warning: str - 警告信息
    """
    
    # 设置默认备选编码
    if fallback_encodings is None:
        fallback_encodings = ['utf-8', 'latin-1', 'cp1252', 'gbk', 'gb2312']
    
    result = {
        'success': False,
        'content': '',
        'lines': [],
        'total_lines': 0,
        'file_size': 0,
        'encoding': encoding,
        'is_truncated': False,
        'truncated_size': 0,
        'error': '',
        'warning': ''
    }
    
    # 参数验证
    if not file_path:
        result['error'] = '文件路径不能为空'
        return result
    
    if start_line is not None and start_line < 1:
        result['error'] = '起始行号必须大于等于1'
        return result
    
    if end_line is not None and start_line is not None and end_line < start_line:
        result['error'] = '结束行号不能小于起始行号'
        return result
    
    try:
        # 检查文件是否存在
        if not os.path.exists(file_path):
            result['error'] = f'文件不存在: {file_path}'
            return result
        
        # 检查是否为文件
        if not os.path.isfile(file_path):
            result['error'] = f'路径不是文件: {file_path}'
            return result
        
        # 检查文件大小
        file_size = os.path.getsize(file_path)
        result['file_size'] = file_size
        
        # 检查文件是否可读
        if not os.access(file_path, os.R_OK):
            result['error'] = f'文件不可读: {file_path}'
            return result
        
        # 处理超大文件
        if file_size > max_file_size:
            return _handle_large_file(file_path, start_line, end_line, max_file_size, 
                                    encoding, fallback_encodings, result)
        
        # 正常文件读取
        return _read_normal_file(file_path, start_line, end_line, encoding, 
                               fallback_encodings, result)
        
    except Exception as e:
        result['error'] = f'读取文件时发生错误: {str(e)}'
        return result


def _read_normal_file(file_path: str, 
                     start_line: Optional[int], 
                     end_line: Optional[int],
                     encoding: str,
                     fallback_encodings: List[str],
                     result: Dict[str, Any]) -> Dict[str, Any]:
    """读取正常大小的文件"""
    
    # 尝试使用首选编码读取
    content, used_encoding, error = _read_file_with_encoding(file_path, encoding)
    
    if error:
        # 尝试备选编码
        for fallback_encoding in fallback_encodings:
            if fallback_encoding == encoding:
                continue
            content, used_encoding, error = _read_file_with_encoding(file_path, fallback_encoding)
            if not error:
                result['warning'] = f'使用备选编码: {fallback_encoding}'
                break
    
    if error:
        result['error'] = f'无法读取文件（尝试的编码: {encoding}, {", ".join(fallback_encodings)}): {error}'
        return result
    
    result['encoding'] = used_encoding
    result['success'] = True
    
    # 分割行
    lines = content.splitlines()
    result['total_lines'] = len(lines)
    
    # 处理行范围
    if start_line is None and end_line is None:
        # 读取所有行
        result['content'] = content
        result['lines'] = lines
    else:
        # 读取指定范围的行
        start_idx = (start_line or 1) - 1  # 转换为0-based索引
        end_idx = (end_line or len(lines)) - 1
        
        # 边界检查
        start_idx = max(0, min(start_idx, len(lines) - 1))
        end_idx = max(start_idx, min(end_idx, len(lines) - 1))
        
        selected_lines = lines[start_idx:end_idx + 1]
        result['content'] = '\n'.join(selected_lines)
        result['lines'] = selected_lines
        
        if start_line != start_idx + 1 or end_line != end_idx + 1:
            result['warning'] = f'行号已调整到有效范围: {start_idx + 1}-{end_idx + 1}'
    
    return result


def _handle_large_file(file_path: str,
                      start_line: Optional[int],
                      end_line: Optional[int],
                      max_file_size: int,
                      encoding: str,
                      fallback_encodings: List[str],
                      result: Dict[str, Any]) -> Dict[str, Any]:
    """处理超大文件"""
    
    result['is_truncated'] = True
    result['truncated_size'] = result['file_size']
    result['warning'] = f'文件过大 ({result["file_size"]} 字节 > {max_file_size} 字节)，进行截断处理'
    
    try:
        # 对于超大文件，我们只读取前max_file_size字节
        if start_line is None and end_line is None:
            # 读取文件开头部分
            return _read_file_head(file_path, max_file_size, encoding, fallback_encodings, result)
        else:
            # 尝试读取指定行范围（可能不准确）
            return _read_specific_lines_large(file_path, start_line, end_line, 
                                            max_file_size, encoding, fallback_encodings, result)
    except Exception as e:
        result['error'] = f'处理大文件时发生错误: {str(e)}'
        return result


def _read_file_head(file_path: str, max_size: int, encoding: str, 
                   fallback_encodings: List[str], result: Dict[str, Any]) -> Dict[str, Any]:
    """读取文件开头部分"""
    
    content, used_encoding, error = _read_file_with_encoding(file_path, encoding, max_size)
    
    if error:
        for fallback_encoding in fallback_encodings:
            if fallback_encoding == encoding:
                continue
            content, used_encoding, error = _read_file_with_encoding(file_path, fallback_encoding, max_size)
            if not error:
                result['warning'] += f' 使用备选编码: {fallback_encoding}'
                break
    
    if error:
        result['error'] = f'无法读取文件: {error}'
        return result
    
    result['encoding'] = used_encoding
    result['success'] = True
    result['content'] = content
    result['lines'] = content.splitlines()
    result['total_lines'] = len(result['lines'])
    
    return result


def _read_specific_lines_large(file_path: str,
                              start_line: Optional[int],
                              end_line: Optional[int],
                              max_size: int,
                              encoding: str,
                              fallback_encodings: List[str],
                              result: Dict[str, Any]) -> Dict[str, Any]:
    """在大文件中尝试读取指定行范围"""
    
    # 对于大文件，精确读取指定行很困难，我们尝试近似读取
    try:
        # 使用迭代器逐行读取，避免加载整个文件到内存
        lines = []
        line_count = 0
        current_line = 0
        
        with open(file_path, 'rb') as f:
            # 尝试使用指定编码
            for test_encoding in [encoding] + fallback_encodings:
                try:
                    f.seek(0)
                    decoder = codecs.getincrementaldecoder(test_encoding)()
                    buffer = b''
                    lines = []
                    line_count = 0
                    current_line = 0
                    
                    while True:
                        chunk = f.read(8192)  # 8KB chunks
                        if not chunk:
                            break
                        
                        buffer += chunk
                        text = decoder.decode(chunk, final=False)
                        
                        # 处理文本行
                        while '\n' in text:
                            line, text = text.split('\n', 1)
                            current_line += 1
                            
                            # 检查是否在目标范围内
                            if start_line is None or current_line >= start_line:
                                if end_line is None or current_line <= end_line:
                                    lines.append(line)
                                    line_count += 1
                            
                            # 限制读取的行数，避免内存溢出
                            if line_count >= 1000:  # 最多读取1000行
                                break
                        
                        if line_count >= 1000:
                            break
                    
                    # 处理最后一行
                    if text.strip():
                        current_line += 1
                        if (start_line is None or current_line >= start_line) and \
                           (end_line is None or current_line <= end_line):
                            lines.append(text)
                            line_count += 1
                    
                    result['encoding'] = test_encoding
                    result['success'] = True
                    result['content'] = '\n'.join(lines)
                    result['lines'] = lines
                    result['total_lines'] = current_line
                    
                    if test_encoding != encoding:
                        result['warning'] += f' 使用备选编码: {test_encoding}'
                    
                    # 添加行范围信息
                    actual_start = start_line or 1
                    actual_end = min(end_line or current_line, current_line)
                    result['warning'] += f' 实际读取行: {actual_start}-{actual_end} (共{current_line}行)'
                    
                    return result
                    
                except UnicodeDecodeError:
                    continue  # 尝试下一个编码
        
        result['error'] = '无法使用任何编码读取文件'
        return result
        
    except Exception as e:
        result['error'] = f'读取大文件指定行时发生错误: {str(e)}'
        return result


def _read_file_with_encoding(file_path: str, encoding: str, max_size: Optional[int] = None) -> Tuple[str, str, str]:
    """使用指定编码读取文件，返回内容、使用的编码和错误信息"""
    
    try:
        if max_size:
            # 限制读取大小
            with open(file_path, 'rb') as f:
                content_bytes = f.read(max_size)
            # 尝试解码
            content = content_bytes.decode(encoding)
            return content, encoding, ''
        else:
            # 读取整个文件
            with open(file_path, 'r', encoding=encoding) as f:
                content = f.read()
            return content, encoding, ''
    except UnicodeDecodeError as e:
        return '', encoding, f'编码错误: {str(e)}'
    except Exception as e:
        return '', encoding, f'读取错误: {str(e)}'


def is_text_file(file_path: str, sample_size: int = 4096) -> bool:
    """
    检查文件是否为文本文件
    
    Args:
        file_path: 文件路径
        sample_size: 采样大小（字节）
    
    Returns:
        bool: 是否为文本文件
    """
    
    if not os.path.isfile(file_path):
        return False
    
    try:
        with open(file_path, 'rb') as f:
            sample = f.read(sample_size)
        
        # 检查是否包含空字节（二进制文件的特征）
        if b'\0' in sample:
            return False
        
        # 检查是否大部分字符是可打印的或非控制字符
        printable_count = 0
        total_count = len(sample)
        
        for byte in sample:
            # 扩展可打印字符定义：包括所有非控制字符（字节值 > 31 且 != 127）
            # 以及制表符、换行符、回车符
            if (byte > 31 and byte != 127) or byte in [9, 10, 13]:
                printable_count += 1
        
        # 降低阈值到80%，适应包含非ASCII字符的文本文件
        return (printable_count / total_count) > 0.8 if total_count > 0 else True
        
    except Exception:
        return False


def get_file_line_count(file_path: str, encoding: str = 'utf-8') -> int:
    """
    快速获取文件行数
    
    Args:
        file_path: 文件路径
        encoding: 文件编码
    
    Returns:
        int: 文件行数
    """
    
    if not os.path.isfile(file_path):
        return 0
    
    try:
        line_count = 0
        with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
            for _ in f:
                line_count += 1
        return line_count
    except Exception:
        return 0


def format_read_result(result: Dict[str, Any]) -> str:
    """
    格式化读取结果为可读字符串
    
    Args:
        result: 读取结果字典
    
    Returns:
        str: 格式化的结果字符串
    """
    
    lines = []
    lines.append("=" * 60)
    lines.append("FILE READ RESULT")
    lines.append("=" * 60)
    
    lines.append(f"成功: {'是' if result.get('success') else '否'}")
    
    if result.get('error'):
        lines.append(f"错误: {result['error']}")
    
    if result.get('warning'):
        lines.append(f"警告: {result['warning']}")
    
    lines.append(f"文件大小: {result.get('file_size', 0)} 字节")
    lines.append(f"总行数: {result.get('total_lines', 0)}")
    lines.append(f"编码: {result.get('encoding', 'Unknown')}")
    
    if result.get('is_truncated'):
        lines.append(f"文件截断: 是 (原大小: {result.get('truncated_size', 0)} 字节)")
    
    if result.get('success'):
        content = result.get('content', '')
        lines.append(f"内容长度: {len(content)} 字符")
        lines.append("-" * 40)
        lines.append("内容预览:")
        lines.append("-" * 40)
        
        # 显示前10行或全部内容（如果行数少）
        if len(content) > 1000:
            lines.append(content[:1000] + "... [内容截断]")
        else:
            lines.append(content)
    
    lines.append("=" * 60)
    return '\n'.join(lines)


# 便捷函数
def read_file_lines(file_path: str, encoding: str = 'utf-8') -> List[str]:
    """读取文件所有行（简化版）"""
    try:
        result = file_read(file_path, encoding=encoding)
        if result['success']:
            return result['lines']
        return []
    except Exception:
        return []


def read_file_content(file_path: str, encoding: str = 'utf-8') -> str:
    """读取文件内容（简化版）"""
    try:
        result = file_read(file_path, encoding=encoding)
        if result['success']:
            return result['content']
        return ''
    except Exception:
        return ''


def read_file_range(file_path: str, start_line: int, end_line: int, encoding: str = 'utf-8') -> List[str]:
    """读取文件指定行范围（简化版）"""
    try:
        result = file_read(file_path, start_line=start_line, end_line=end_line, encoding=encoding)
        if result['success']:
            return result['lines']
        return []
    except Exception:
        return []


if __name__ == "__main__":
    # 测试代码
    print("文件读取功能测试")
    print("=" * 60)
    
    # 测试文件列表
    test_files = [
        __file__,  # 当前文件
        "README.md",  # 项目README文件
        "/nonexistent/file.txt",  # 不存在的文件
    ]
    
    for test_file in test_files:
        print(f"测试文件: {test_file}")
        result = file_read(test_file)
        print(format_read_result(result))
        print()
    
    # 测试文本文件检测
    print("文本文件检测测试")
    print("=" * 60)
    for test_file in test_files[:2]:  # 只测试存在的文件
        is_text = is_text_file(test_file)
        print(f"{test_file}: {'是文本文件' if is_text else '不是文本文件'}")
    
    print()
    
    # 测试行数统计
    print("文件行数统计测试")
    print("=" * 60)
    for test_file in test_files[:2]:  # 只测试存在的文件
        line_count = get_file_line_count(test_file)
        print(f"{test_file}: {line_count} 行")