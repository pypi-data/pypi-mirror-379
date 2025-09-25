"""
MAG SDK - 模型管理客户端API
"""

import requests
from typing import Dict, List, Any, Optional

# 获取基础URL
from .. import _BASE_URL, start, is_running

API_BASE = f"{_BASE_URL}/api"

def _ensure_server_running():
    """确保服务器正在运行"""
    if not is_running():
        if not start():
            raise RuntimeError("无法启动MAG服务器")

def list_model() -> List[Dict[str, Any]]:
    """
    获取所有模型
    
    返回:
        List[Dict[str, Any]]: 模型配置列表
    """
    _ensure_server_running()
    response = requests.get(f"{API_BASE}/models")
    response.raise_for_status()
    return response.json()


def get_model(name: str, detail: bool = True) -> Optional[Dict[str, Any]]:
    """
    获取指定模型的配置

    参数:
        name (str): 模型名称
        detail (bool): 是否返回详细配置，默认为True
                      True - 返回完整的可编辑配置（从API获取）
                      False - 返回基本配置（从本地缓存获取）

    返回:
        Optional[Dict[str, Any]]: 模型配置，如果不存在则返回None
    """
    _ensure_server_running()

    if detail:
        # 返回详细配置（用于编辑）
        try:
            from urllib.parse import quote
            encoded_name = quote(name, safe='')
            response = requests.get(f"{API_BASE}/models/{encoded_name}")

            if response.status_code == 404:
                return None

            response.raise_for_status()
            result = response.json()

            if result.get("status") == "success":
                return result.get("data")
            else:
                return None

        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response.status_code == 404:
                return None
            raise RuntimeError(f"获取模型详细配置时出错: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"获取模型详细配置时出错: {str(e)}")
    else:
        # 返回基本配置
        try:
            # 获取所有模型
            models = list_model()

            # 找到匹配的模型
            for model in models:
                if model["name"] == name:
                    return model

            return None
        except Exception as e:
            raise RuntimeError(f"获取模型时出错: {str(e)}")

def add_model(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    添加新模型
    
    参数:
        config (Dict[str, Any]): 模型配置，必须包含以下字段:
            - name: 模型名称
            - base_url: API基础URL
            - api_key: API密钥
            - model: 模型标识符
    
    返回:
        Dict[str, Any]: 操作结果
    """
    _ensure_server_running()
    
    # 验证必填字段
    required_fields = ["name", "base_url", "api_key", "model"]
    for field in required_fields:
        if field not in config:
            raise ValueError(f"模型配置缺少必填字段: {field}")
    
    response = requests.post(f"{API_BASE}/models", json=config)
    response.raise_for_status()
    return response.json()

def update_model(name: str, config: Dict[str, Any]) -> Dict[str, Any]:
    """
    更新现有模型
    
    参数:
        name (str): 当前模型名称
        config (Dict[str, Any]): 更新后的模型配置
    
    返回:
        Dict[str, Any]: 操作结果
    """
    _ensure_server_running()
    
    # 验证必填字段
    required_fields = ["name", "base_url", "api_key", "model"]
    for field in required_fields:
        if field not in config:
            raise ValueError(f"模型配置缺少必填字段: {field}")
    
    response = requests.put(f"{API_BASE}/models/{name}", json=config)
    response.raise_for_status()
    return response.json()

def delete_model(name: str) -> Dict[str, Any]:
    """
    删除模型
    
    参数:
        name (str): 模型名称
    
    返回:
        Dict[str, Any]: 操作结果
    """
    _ensure_server_running()
    response = requests.delete(f"{API_BASE}/models/{name}")
    response.raise_for_status()
    return response.json()