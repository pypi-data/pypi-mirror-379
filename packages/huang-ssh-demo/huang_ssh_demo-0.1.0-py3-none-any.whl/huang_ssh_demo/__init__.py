# server.py
from mcp.server.fastmcp import FastMCP
import paramiko
import json
from typing import Dict, List, Any
import re

# Create an MCP server for Linux system inspection
mcp = FastMCP("LinuxSystemInspector")

class SSHClient:
    def __init__(self):
        self.client = None
    
    def connect(self, hostname: str, username: str, password: str = None, port: int = 22, key_filename: str = None) -> bool:
        """建立SSH连接"""
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            if key_filename:
                self.client.connect(hostname, port=port, username=username, key_filename=key_filename)
            else:
                self.client.connect(hostname, port=port, username=username, password=password)
            
            return True
        except Exception as e:
            return False
    
    def execute_command(self, command: str) -> Dict[str, Any]:
        """执行SSH命令并返回结果"""
        if not self.client:
            return {"success": False, "error": "SSH连接未建立"}
        
        try:
            stdin, stdout, stderr = self.client.exec_command(command)
            exit_status = stdout.channel.recv_exit_status()
            output = stdout.read().decode('utf-8').strip()
            error = stderr.read().decode('utf-8').strip()
            
            return {
                "success": exit_status == 0,
                "output": output,
                "error": error,
                "exit_status": exit_status
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def close(self):
        """关闭SSH连接"""
        if self.client:
            self.client.close()

# 创建全局SSH客户端实例
ssh_client = SSHClient()

@mcp.tool()
def connect_to_server(hostname: str, username: str, password: str = None, port: int = 22, key_filename: str = None) -> str:
    """
    连接到远程Linux服务器
    
    Args:
        hostname: 服务器地址
        username: 用户名
        password: 密码（可选，如果使用密钥认证）
        port: SSH端口，默认22
        key_filename: SSH私钥文件路径（可选）
    
    Returns:
        连接状态信息
    """
    success = ssh_client.connect(hostname, username, password, port, key_filename)
    if success:
        return f"成功连接到服务器 {hostname}"
    else:
        return f"连接服务器 {hostname} 失败"

@mcp.tool()
def disconnect_server() -> str:
    """断开SSH连接"""
    ssh_client.close()
    return "已断开SSH连接"

@mcp.tool()
def check_system_info() -> Dict[str, Any]:
    """检查系统基本信息"""
    commands = {
        "hostname": "hostname",
        "os_info": "cat /etc/os-release",
        "kernel_version": "uname -r",
        "uptime": "uptime",
        "date": "date"
    }
    
    results = {}
    for key, command in commands.items():
        result = ssh_client.execute_command(command)
        results[key] = result
    
    return results

@mcp.tool()
def check_cpu_usage() -> Dict[str, Any]:
    """检查CPU使用情况"""
    result = ssh_client.execute_command("top -bn1 | grep 'Cpu(s)'")
    
    if result["success"]:
        # 解析CPU使用率
        cpu_line = result["output"]
        cpu_usage = {}
        
        # 匹配CPU使用率百分比
        patterns = {
            'user': r'(\d+\.\d+)%us',
            'system': r'(\d+\.\d+)%sy',
            'idle': r'(\d+\.\d+)%id'
        }
        
        for key, pattern in patterns.items():
            match = re.search(pattern, cpu_line)
            if match:
                cpu_usage[key] = float(match.group(1))
        
        return {"success": True, "cpu_usage": cpu_usage, "raw_output": cpu_line}
    else:
        return result

@mcp.tool()
def check_memory_usage() -> Dict[str, Any]:
    """检查内存使用情况"""
    result = ssh_client.execute_command("free -h")
    
    if result["success"]:
        lines = result["output"].split('\n')
        memory_info = {}
        
        if len(lines) >= 2:
            # 解析内存信息
            headers = lines[0].split()
            values = lines[1].split()
            
            for i, header in enumerate(headers):
                if i < len(values):
                    memory_info[header] = values[i]
        
        return {"success": True, "memory_info": memory_info, "raw_output": result["output"]}
    else:
        return result

@mcp.tool()
def check_disk_usage() -> Dict[str, Any]:
    """检查磁盘使用情况"""
    result = ssh_client.execute_command("df -h")
    
    if result["success"]:
        lines = result["output"].split('\n')
        disk_info = []
        
        for line in lines[1:]:  # 跳过标题行
            if line.strip():
                parts = line.split()
                if len(parts) >= 6:
                    disk_info.append({
                        "filesystem": parts[0],
                        "size": parts[1],
                        "used": parts[2],
                        "available": parts[3],
                        "use_percent": parts[4],
                        "mounted_on": parts[5]
                    })
        
        return {"success": True, "disk_info": disk_info, "raw_output": result["output"]}
    else:
        return result

@mcp.tool()
def check_running_processes(process_name: str = None) -> Dict[str, Any]:
    """检查运行中的进程"""
    if process_name:
        command = f"ps aux | grep {process_name} | grep -v grep"
    else:
        command = "ps aux --sort=-%cpu | head -10"
    
    result = ssh_client.execute_command(command)
    
    if result["success"]:
        processes = []
        lines = result["output"].split('\n')
        
        for line in lines:
            if line.strip():
                parts = line.split()
                if len(parts) >= 11:
                    processes.append({
                        "user": parts[0],
                        "pid": parts[1],
                        "cpu": parts[2],
                        "mem": parts[3],
                        "command": ' '.join(parts[10:])
                    })
        
        return {"success": True, "processes": processes, "raw_output": result["output"]}
    else:
        return result

@mcp.tool()
def check_network_status() -> Dict[str, Any]:
    """检查网络状态"""
    commands = {
        "network_interfaces": "ip addr show",
        "listening_ports": "netstat -tuln",
        "established_connections": "netstat -tun | grep ESTABLISHED"
    }
    
    results = {}
    for key, command in commands.items():
        result = ssh_client.execute_command(command)
        results[key] = result
    
    return results

@mcp.tool()
def check_system_logs(log_type: str = "syslog", lines: int = 50) -> Dict[str, Any]:
    """检查系统日志"""
    log_files = {
        "syslog": "/var/log/syslog",
        "messages": "/var/log/messages",
        "dmesg": "dmesg",
        "auth": "/var/log/auth.log"
    }
    
    log_file = log_files.get(log_type, "/var/log/syslog")
    
    if log_type == "dmesg":
        command = f"dmesg | tail -{lines}"
    else:
        command = f"tail -{lines} {log_file}"
    
    result = ssh_client.execute_command(command)
    return result

@mcp.tool()
def comprehensive_inspection() -> Dict[str, Any]:
    """执行全面的系统巡检"""
    inspection_results = {}
    
    # 系统信息
    inspection_results["system_info"] = check_system_info()
    
    # CPU使用率
    inspection_results["cpu_usage"] = check_cpu_usage()
    
    # 内存使用情况
    inspection_results["memory_usage"] = check_memory_usage()
    
    # 磁盘使用情况
    inspection_results["disk_usage"] = check_disk_usage()
    
    # 网络状态
    inspection_results["network_status"] = check_network_status()
    
    # 关键进程
    inspection_results["key_processes"] = check_running_processes()
    
    # 系统日志摘要
    inspection_results["system_logs"] = check_system_logs("syslog", 20)
    
    return inspection_results

@mcp.tool()
def execute_custom_command(command: str) -> Dict[str, Any]:
    """
    执行自定义命令
    
    Args:
        command: 要执行的Linux命令
    
    Returns:
        命令执行结果
    """
    return ssh_client.execute_command(command)

def main() -> None:
    mcp.run(transport="stdio")
