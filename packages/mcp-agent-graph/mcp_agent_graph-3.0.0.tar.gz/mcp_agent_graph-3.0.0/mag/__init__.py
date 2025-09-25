"""
MCP Agent Graph (MAG) SDK - Agent Development Framework

Simple Python interface for working with MAG agent system.
"""

import multiprocessing
import os
import sys
import time
import signal
import atexit
import subprocess
import importlib.util
import threading
import tempfile
from pathlib import Path

# 全局状态
_SERVER_PROCESS = None
_MCP_CLIENT_PROCESS = None
_SERVER_PORT = 9999
_MCP_CLIENT_PORT = 8765
_BASE_URL = f"http://127.0.0.1:{_SERVER_PORT}"
_is_server_running = False
_lock = threading.Lock()

# 服务器日志文件
_temp_dir = tempfile.gettempdir()
_log_dir = Path(_temp_dir) / "mag_sdk_logs"
_log_dir.mkdir(exist_ok=True)
_server_log = _log_dir / "mag_server.log"
_mcp_log = _log_dir / "mcp_client.log"

def _clean_shutdown():
    """在程序退出时确保进程被清理"""
    shutdown()

def _get_script_path(script_name):
    """获取SDK内部脚本的路径"""
    package_dir = Path(__file__).parent
    return str(package_dir / script_name)

def _start_server():
    """启动MAG服务器进程"""
    global _SERVER_PROCESS
    if _SERVER_PROCESS and _SERVER_PROCESS.poll() is None:
        return  # 已经在运行

    main_script = _get_script_path("main.py")
    
    # 打开日志文件
    log_file = open(_server_log, "w")
    
    # 启动服务器进程
    _SERVER_PROCESS = subprocess.Popen(
        [sys.executable, main_script],
        stdout=log_file,
        stderr=log_file,
        start_new_session=True  # 使进程独立运行
    )
    print(f"MAG服务器已启动 (PID: {_SERVER_PROCESS.pid}), 日志: {_server_log}")

def _start_mcp_client():
    """启动MCP客户端进程"""
    global _MCP_CLIENT_PROCESS
    if _MCP_CLIENT_PROCESS and _MCP_CLIENT_PROCESS.poll() is None:
        return  # 已经在运行

    mcp_script = _get_script_path("mcp_client.py")
    
    # 打开日志文件
    log_file = open(_mcp_log, "w")
    
    # 启动MCP客户端进程
    _MCP_CLIENT_PROCESS = subprocess.Popen(
        [sys.executable, mcp_script],
        stdout=log_file,
        stderr=log_file,
        start_new_session=True  # 使进程独立运行
    )
    print(f"MCP客户端已启动 (PID: {_MCP_CLIENT_PROCESS.pid}), 日志: {_mcp_log}")

def _wait_for_server(timeout=30):
    """等待服务器启动并响应"""
    import requests
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(f"{_BASE_URL}/health")
            if response.status_code == 200:
                return True
        except requests.RequestException:
            pass
        time.sleep(1)
    return False

def start():
    """
    启动MAG服务器和MCP客户端
    
    这个函数会启动必要的后台服务，使SDK可以正常工作。
    每个Python进程只需要调用一次。
    
    返回:
        bool: 是否成功启动服务
    """
    global _is_server_running
    
    with _lock:
        if _is_server_running:
            return True
            
        # 启动服务器
        _start_server()
        
        # 等待服务器启动
        if not _wait_for_server():
            print("错误: 服务器启动超时")
            shutdown()
            return False
        
        # 设置进程已启动标志
        _is_server_running = True
        
        return True

def shutdown():
    """
    关闭MAG服务器和MCP客户端
    
    这个函数会安全地终止所有后台进程。
    """
    global _is_server_running, _SERVER_PROCESS, _MCP_CLIENT_PROCESS
    
    with _lock:
        if not _is_server_running:
            return
            
        # 尝试通过API优雅关闭
        try:
            import requests
            requests.post(f"{_BASE_URL}/api/system/shutdown", timeout=5)
            time.sleep(3) 
        except:
            pass
            
        # 终止MCP客户端进程
        if _MCP_CLIENT_PROCESS:
            try:
                if _MCP_CLIENT_PROCESS.poll() is None:
                    _MCP_CLIENT_PROCESS.terminate()
                    _MCP_CLIENT_PROCESS.wait(timeout=5)
            except:
                if _MCP_CLIENT_PROCESS.poll() is None:
                    _MCP_CLIENT_PROCESS.kill()
            _MCP_CLIENT_PROCESS = None
            
        # 终止服务器进程
        if _SERVER_PROCESS:
            try:
                if _SERVER_PROCESS.poll() is None:
                    _SERVER_PROCESS.terminate()
                    _SERVER_PROCESS.wait(timeout=5)
            except:
                if _SERVER_PROCESS.poll() is None:
                    _SERVER_PROCESS.kill()
            _SERVER_PROCESS = None
            
        _is_server_running = False

def is_running():
    """
    检查MAG服务是否正在运行
    
    返回:
        bool: 服务是否正在运行
    """
    return _is_server_running

# 会话管理
from .client.conversation import (
    chat_completions,
    list_conversations,
    get_conversation_detail,
    get_conversation_metadata,
    update_conversation_status,
    permanently_delete_conversation,
    update_conversation_title,
    update_conversation_tags,
    compact_conversation
)

# 模型管理
from .client.model import (
    list_model,
    get_model,
    add_model,
    update_model,
    delete_model
)

# MCP服务器管理
from .client.mcp import (
    get_mcp_config,
    update_mcp_config,
    mcp_status,
    connect,
    mcptools,
    add_mcp,
    remove_mcp,
    disconnect,
    test_mcptool,
    mcp_gen_prompt,
    gen_mcp
)


# 图管理
from .client.graph import (
    list_graph,
    get_graph_config,
    get_graph_detail,
    run_graph,
    generate as gen_graph,
    optimize as update_graph,
    graph_gen_prompt,
    save_graph,
    delete_graph,
    rename_graph,
    import_graph,
    export_graph,
    graph_to_mcp
)

#
# run_graph = run
# import_graph = import_graph
# export_graph = export
# generate_graph = generate_graph
# optimize_graph = optimize
# get_optimize_prompt = get_optimize_prompt