"""
配置文件处理模块
支持从config.toml读取配置，并提供默认值
"""
import os
import tomllib
from typing import Dict, Any, Optional

# 默认配置
DEFAULT_CONFIG = {
    "server": {
        "transport": "stdio",
    },
    "http": {
        "host": "0.0.0.0",
        "port": 8000,
    }
}

def load_config(config_path: Optional[str] = None) -> Dict[str, Any]:
    """
    加载配置文件
    
    Args:
        config_path: 配置文件路径，如果为None则尝试从默认位置加载
        
    Returns:
        配置字典
    """
    if config_path is None:
        # 尝试从当前目录和项目根目录查找config.toml
        possible_paths = [
            "config.toml",
            "../config.toml",
            "../../config.toml"
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                config_path = path
                break
        else:
            # 如果没有找到配置文件，返回默认配置
            return DEFAULT_CONFIG.copy()
    
    try:
        with open(config_path, 'rb') as f:
            config = tomllib.load(f)
        
        # 合并默认配置和用户配置
        merged_config = DEFAULT_CONFIG.copy()
        _deep_merge(merged_config, config)
        return merged_config
        
    except Exception as e:
        print(f"警告: 加载配置文件失败 ({e})，使用默认配置")
        return DEFAULT_CONFIG.copy()

def _deep_merge(base: Dict[str, Any], update: Dict[str, Any]) -> None:
    """
    深度合并两个字典
    
    Args:
        base: 基础字典（会被修改）
        update: 更新字典
    """
    for key, value in update.items():
        if (key in base and isinstance(base[key], dict) 
            and isinstance(value, dict)):
            _deep_merge(base[key], value)
        else:
            base[key] = value

def get_transport_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    获取传输协议配置
    
    Args:
        config: 完整配置字典
        
    Returns:
        传输协议相关配置
    """
    return {
        "transport": config.get("server", {}).get("transport", "stdio"),
        "host": config.get("http", {}).get("host", "0.0.0.0"),
        "port": config.get("http", {}).get("port", 8000),
    }