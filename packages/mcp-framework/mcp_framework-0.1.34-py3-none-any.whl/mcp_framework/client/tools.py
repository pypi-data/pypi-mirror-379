"""
MCP 工具调用客户端
提供便捷的工具列表获取和工具调用功能
"""

from typing import Dict, Any, List, Optional
from .base import MCPStdioClient


class Tool:
    """工具信息类"""
    
    def __init__(self, name: str, description: str = "", input_schema: Optional[Dict[str, Any]] = None):
        self.name = name
        self.description = description
        self.input_schema = input_schema or {}
    
    def __repr__(self):
        return f"Tool(name='{self.name}', description='{self.description}')"


class ToolsClient(MCPStdioClient):
    """MCP 工具调用客户端"""
    
    def __init__(self, 
                 server_script: str,
                 alias: Optional[str] = None,
                 server_args: Optional[List[str]] = None,
                 client_name: str = "mcp-framework-client",
                 client_version: str = "1.0.0",
                 startup_timeout: float = 5.0,
                 response_timeout: float = 30.0):
        """
        初始化 MCP 工具调用客户端
        
        Args:
            server_script: 服务器脚本路径
            alias: 服务器别名（重要参数，用于多实例管理）
            server_args: 额外的服务器参数
            client_name: 客户端名称
            client_version: 客户端版本
            startup_timeout: 启动超时时间（秒）
            response_timeout: 响应超时时间（秒）
        """
        super().__init__(
            server_script=server_script,
            alias=alias,
            server_args=server_args,
            client_name=client_name,
            client_version=client_version,
            startup_timeout=startup_timeout,
            response_timeout=response_timeout
        )
        self._tools_cache = None
    
    async def _ensure_connected(self):
        """确保客户端已连接和初始化"""
        if not self.is_connected:
            await self.connect()
        if not self.is_initialized:
            await self.initialize()
    
    async def list_tools(self, force_refresh: bool = False) -> List[Tool]:
        """
        获取可用工具列表
        
        Args:
            force_refresh: 是否强制刷新缓存
            
        Returns:
            List[Tool]: 工具列表
            
        Raises:
            Exception: 获取工具列表失败
        """
        await self._ensure_connected()
        
        # 使用缓存（除非强制刷新）
        if self._tools_cache is not None and not force_refresh:
            return self._tools_cache
        
        response = await self.send_request("tools/list")
        
        if "error" in response:
            raise Exception(f"获取工具列表失败: {response['error']}")
        
        result = response.get("result", {})
        tools_data = result.get("tools", [])
        
        # 转换为 Tool 对象
        tools = []
        for tool_data in tools_data:
            tool = Tool(
                name=tool_data.get("name", ""),
                description=tool_data.get("description", ""),
                input_schema=tool_data.get("inputSchema", {})
            )
            tools.append(tool)
        
        # 缓存结果
        self._tools_cache = tools
        return tools
    
    async def get_tool(self, tool_name: str) -> Optional[Tool]:
        """
        获取特定工具的信息
        
        Args:
            tool_name: 工具名称
            
        Returns:
            Optional[Tool]: 工具对象，如果不存在则返回 None
        """
        tools = await self.list_tools()
        
        for tool in tools:
            if tool.name == tool_name:
                return tool
        
        return None
    
    async def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        调用指定工具
        
        Args:
            tool_name: 工具名称
            arguments: 工具参数
            
        Returns:
            Dict[str, Any]: 工具执行结果
            
        Raises:
            Exception: 工具调用失败
        """
        await self._ensure_connected()
        
        params = {
            "name": tool_name,
            "arguments": arguments
        }
        
        response = await self.send_request("tools/call", params)
        
        if "error" in response:
            raise Exception(f"工具调用失败: {response['error']}")
        
        return response.get("result", {})
    
    async def tool_exists(self, tool_name: str) -> bool:
        """
        检查工具是否存在
        
        Args:
            tool_name: 工具名称
            
        Returns:
            bool: 工具是否存在
        """
        tool = await self.get_tool(tool_name)
        return tool is not None
    
    async def get_tool_names(self) -> List[str]:
        """
        获取所有工具名称列表
        
        Returns:
            List[str]: 工具名称列表
        """
        tools = await self.list_tools()
        return [tool.name for tool in tools]
    
    async def validate_tool_arguments(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        验证工具参数（基于工具的输入模式）
        
        Args:
            tool_name: 工具名称
            arguments: 要验证的参数
            
        Returns:
            Dict[str, Any]: 验证结果，包含 valid 字段和可能的错误信息
        """
        tool = await self.get_tool(tool_name)
        
        if not tool:
            return {
                "valid": False,
                "errors": [f"工具 '{tool_name}' 不存在"]
            }
        
        # 简单的参数验证（基于 JSON Schema）
        input_schema = tool.input_schema
        errors = []
        
        # 检查必需参数
        required_props = input_schema.get("required", [])
        for prop in required_props:
            if prop not in arguments:
                errors.append(f"缺少必需参数: {prop}")
        
        # 检查参数类型（简化版本）
        properties = input_schema.get("properties", {})
        for arg_name, arg_value in arguments.items():
            if arg_name in properties:
                prop_schema = properties[arg_name]
                expected_type = prop_schema.get("type")
                
                if expected_type == "string" and not isinstance(arg_value, str):
                    errors.append(f"参数 '{arg_name}' 应为字符串类型")
                elif expected_type == "integer" and not isinstance(arg_value, int):
                    errors.append(f"参数 '{arg_name}' 应为整数类型")
                elif expected_type == "boolean" and not isinstance(arg_value, bool):
                    errors.append(f"参数 '{arg_name}' 应为布尔类型")
                elif expected_type == "object" and not isinstance(arg_value, dict):
                    errors.append(f"参数 '{arg_name}' 应为对象类型")
                elif expected_type == "array" and not isinstance(arg_value, list):
                    errors.append(f"参数 '{arg_name}' 应为数组类型")
        
        return {
            "valid": len(errors) == 0,
            "errors": errors
        }


# 便捷函数
async def list_server_tools(server_script: str, 
                           alias: Optional[str] = None,
                           **kwargs) -> List[Tool]:
    """
    便捷函数：获取服务器工具列表
    
    Args:
        server_script: 服务器脚本路径
        alias: 服务器别名
        **kwargs: 其他客户端参数
        
    Returns:
        List[Tool]: 工具列表
    """
    async with ToolsClient(server_script, alias, **kwargs) as client:
        return await client.list_tools()


async def call_server_tool(server_script: str,
                          tool_name: str,
                          arguments: Dict[str, Any],
                          alias: Optional[str] = None,
                          **kwargs) -> Dict[str, Any]:
    """
    便捷函数：调用服务器工具
    
    Args:
        server_script: 服务器脚本路径
        tool_name: 工具名称
        arguments: 工具参数
        alias: 服务器别名
        **kwargs: 其他客户端参数
        
    Returns:
        Dict[str, Any]: 工具执行结果
    """
    async with ToolsClient(server_script, alias, **kwargs) as client:
        return await client.call_tool(tool_name, arguments)