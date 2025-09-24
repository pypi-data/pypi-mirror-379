"""FastMCP服务器 - MCP工具评估助手（优化Cherry Studio兼容性）"""

import sys
import argparse
from typing import Optional, Dict, Any
from fastmcp import FastMCP
from .fastmcp_config import FastMCPRuntimeConfig
from .database_new import DatabaseManager
from .models import ToolSearchFilter
from .utils import (
    format_tool_info,
    format_search_summary
)
from .tools import (
    search_mcp_tools_basic,
    get_mcp_tool_details as get_tool_details_impl,
    get_tool_test_stats as get_tool_test_stats_impl,
    get_tool_performance_data as get_tool_performance_data_impl
)

# 应用FastMCP运行时配置 - 优化uvx部署和Cherry Studio兼容性
FastMCPRuntimeConfig.apply_all_configurations()

# 初始化FastMCP服务器
mcp = FastMCP("MCP工具评估助手")

# 延迟初始化数据库管理器
db_manager = None

def get_db_manager():
    """获取数据库管理器实例（延迟初始化）"""
    global db_manager
    if db_manager is None:
        db_manager = DatabaseManager()
    return db_manager


@mcp.tool()
async def search_mcp_tools(
    query: Optional[str] = None,
    category: Optional[str] = None,
    min_tashan_score: Optional[float] = None,
    max_tashan_score: Optional[float] = None,
    deployment_method: Optional[str] = None,
    author: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
    sort_by: str = "tashan_score"
) -> Dict[str, Any]:
    """搜索MCP工具
    
    根据关键词、分类、评分等条件搜索MCP工具，返回工具列表和相关信息。
    
    Args:
        query: 搜索关键词，在工具名称和描述中搜索
        category: 工具分类，如"开发工具推荐"、"文档处理"等
        min_tashan_score: 最低他山评分（0-100）
        max_tashan_score: 最高他山评分（0-100）
        deployment_method: 部署方式，如"npm"、"pip"、"docker"等
        author: 工具作者
        limit: 返回结果数量限制，默认20，最大100
        offset: 偏移量，默认0
        sort_by: 排序方式，可选值：tashan_score（默认）、sustainability_score、popularity_score、lobehub_score
    
    Returns:
        包含工具列表、总数和搜索摘要的字典
        
    Example:
        >>> search_mcp_tools(query="github", limit=10)
        {
            "success": True,
            "tools": [...],
            "total_count": 45,
            "search_summary": "找到 10 个工具(共 45 个)基于条件: 关键词 'github'",
            "filters": {...}
        }
      """
    try:
        # DEPRECATED: This tool is deprecated, please use search_mcp_tools_basic instead
        # This tool will be removed in future versions, please migrate to the new split tools:
        # - search_mcp_tools_basic: for basic search  
        # - get_mcp_tool_details: for detailed information
        # 验证参数
        limit = max(1, min(100, limit))
        offset = max(0, offset)
        
        if min_tashan_score is not None:
            min_tashan_score = max(0, min(100, min_tashan_score))
        if max_tashan_score is not None:
            max_tashan_score = max(0, min(100, max_tashan_score))
        
        # 验证排序字段
        valid_sort_fields = ["tashan_score", "sustainability_score", "popularity_score", "lobehub_score"]
        if sort_by not in valid_sort_fields:
            sort_by = "tashan_score"
        
        # 创建搜索过滤器
        filters = ToolSearchFilter(
            query=query,
            category=category,
            min_tashan_score=min_tashan_score,
            max_tashan_score=max_tashan_score,
            deployment_method=deployment_method,
            author=author,
            limit=limit,
            offset=offset
        )
        
        # 搜索查询记录已在配置中禁用
        
        # 执行搜索 - 为了兼容性仍然使用完整的search_tools方法
        tools = await get_db_manager().search_tools(filters)
        
        # 根据sort_by参数进行排序
        if sort_by != "tashan_score":
            valid_sort_fields = {
                "tashan_score", "sustainability_score", "popularity_score", 
                "lobehub_score", "comprehensive_score", "test_timestamp"
            }
            
            if sort_by in valid_sort_fields:
                tools.sort(key=lambda x: getattr(x, sort_by) or 0, reverse=True)
        
        # 获取总数
        total_count = await get_db_manager().get_total_tools_count()
        
        # 格式化工具信息
        formatted_tools = [format_tool_info(tool) for tool in tools]
        
        # 生成搜索摘要
        search_summary = format_search_summary(filters, total_count, len(tools))
        
        result = {
            "success": True,
            "tools": formatted_tools,
            "total_count": total_count,
            "search_summary": search_summary,
            "filters": filters.model_dump(),
            "sort_by": sort_by
        }
        
        return result
        
    except Exception as e:
        return {
            "success": False,
            "tools": [],
            "total_count": 0,
            "search_summary": f"搜索失败: {str(e)}",
            "filters": {},
            "error": str(e)
        }


@mcp.tool()
async def health_check() -> Dict[str, Any]:
    """服务健康检查
    
    检查数据库连接和服务状态。
    
    Returns:
        包含健康状态和系统信息的字典
    """
    try:
        # 检查数据库连接
        db_healthy = await get_db_manager().health_check()
        
        # 获取工具总数
        total_tools = await get_db_manager().get_total_tools_count()
        
        result = {
            "success": True,
            "status": "healthy" if db_healthy else "unhealthy",
            "database_connected": db_healthy,
            "total_tools": total_tools,
            "timestamp": asyncio.get_event_loop().time()
        }
        
        return result
        
    except Exception as e:
        return {
            "success": False,
            "status": "error",
            "database_connected": False,
            "total_tools": 0,
            "timestamp": asyncio.get_event_loop().time(),
            "error": str(e)
        }


@mcp.tool()
async def search_mcp_tools_basic(
    query: Optional[str] = None,
    category: Optional[str] = None,
    min_tashan_score: Optional[float] = None,
    max_tashan_score: Optional[float] = None,
    deployment_method: Optional[str] = None,
    author: Optional[str] = None,
    limit: int = 20,
    offset: int = 0
) -> Dict[str, Any]:
    """搜索MCP工具 - 基础版本
    
    提供快速、轻量的工具搜索功能，返回基本信息用于列表展示。
    
    Args:
        query: 搜索关键词，在工具名称和描述中搜索
        category: 工具分类，如"开发工具推荐"、"文档处理"等
        min_tashan_score: 最低他山评分（0-100）
        max_tashan_score: 最高他山评分（0-100）
        deployment_method: 部署方式，如"npm"、"pip"、"docker"等
        author: 工具作者
        limit: 返回结果数量限制，默认20，最大100
        offset: 偏移量，默认0
    
    Returns:
        包含工具摘要列表和搜索摘要的字典
        
    Example:
        >>> search_mcp_tools_basic(query="github", limit=10)
        {
            "success": True,
            "tools": [...],
            "total_count": 45,
            "search_summary": "找到 10 个工具(共 45 个)基于条件: 关键词 'github'",
            "filters": {...},
            "error": None
        }
    """
    try:
        # 验证参数
        limit = max(1, min(100, limit))
        offset = max(0, offset)
        
        if min_tashan_score is not None:
            min_tashan_score = max(0, min(100, min_tashan_score))
        if max_tashan_score is not None:
            max_tashan_score = max(0, min(100, max_tashan_score))
        
        # 创建搜索过滤器
        filters = ToolSearchFilter(
            query=query,
            category=category,
            min_tashan_score=min_tashan_score,
            max_tashan_score=max_tashan_score,
            deployment_method=deployment_method,
            author=author,
            limit=limit,
            offset=offset
        )
        
        # 直接使用数据库管理器进行搜索
        tools = await get_db_manager().search_tools(filters)
        
        # 获取总数
        total_count = await get_db_manager().get_total_tools_count()
        
        # 格式化工具信息为基本格式
        basic_tools = []
        for tool in tools:
            basic_tools.append({
                "tool_id": tool.tool_id,
                "tool_name": tool.tool_name,
                "description": tool.description,
                "category": tool.category,
                "author": tool.author,
                "tashan_score": tool.tashan_score,
                "deployment_method": tool.deployment_method,
                "github_url": tool.github_url,
                "lobehub_url": tool.lobehub_url
            })
        
        # 生成搜索摘要
        filter_parts = []
        if query:
            filter_parts.append(f"关键词 '{query}'")
        if category:
            filter_parts.append(f"分类 '{category}'")
        if author:
            filter_parts.append(f"作者 '{author}'")
        
        filter_text = "基于条件: " + ", ".join(filter_parts) if filter_parts else "所有工具"
        search_summary = f"找到 {len(tools)} 个工具({filter_text})"
        
        result = {
            "success": True,
            "tools": basic_tools,
            "total_count": total_count,
            "search_summary": search_summary,
            "filters": filters.model_dump(),
            "error": None
        }
        
        return result
        
    except Exception as e:
        return {
            "success": False,
            "tools": [],
            "total_count": 0,
            "search_summary": f"搜索失败: {str(e)}",
            "filters": {"query": query, "category": category, "limit": limit, "offset": offset},
            "error": str(e)
        }


@mcp.tool()
async def get_mcp_tool_details(
    tool_id: str,
    include_performance_data: bool = True,
    include_test_results: bool = True,
    test_results_limit: int = 5
) -> Dict[str, Any]:
    """获取MCP工具详细信息
    
    根据工具ID获取完整的工具信息，包括基本信息、测试统计、性能数据和最近的测试结果。
    
    Args:
        tool_id: 工具唯一标识符
        include_performance_data: 是否包含性能数据，默认True
        include_test_results: 是否包含测试结果，默认True
        test_results_limit: 测试结果数量限制，默认5
    
    Returns:
        包含完整工具详情的字典
        
    Example:
        >>> get_mcp_tool_details("tool_123")
        {
            "success": True,
            "tool_details": {
                "basic_info": {...},
                "test_stats": {...},
                "performance_data": {...},
                "recent_results": [...]
            },
            "error": None
        }
    """
    try:
        # 调用工具模块中的详情函数
        result = await get_tool_details_impl(
            tool_id=tool_id,
            include_performance_data=include_performance_data,
            include_test_results=include_test_results,
            test_results_limit=test_results_limit
        )
        
        # 转换为字典返回
        return result.model_dump()
        
    except Exception as e:
        return {
            "success": False,
            "tool_details": None,
            "error": str(e)
        }


@mcp.tool()
async def get_tool_test_stats(
    tool_id: str
) -> Dict[str, Any]:
    """获取工具测试统计信息
    
    Args:
        tool_id: 工具唯一标识符
    
    Returns:
        测试统计信息字典
    """
    try:
        # 调用工具模块中的测试统计函数
        result = await get_tool_test_stats_impl(tool_id)
        
        # 转换为字典返回
        return result.model_dump()
        
    except Exception as e:
        return {
            "total_tests": 0,
            "successful_tests": 0,
            "failed_tests": 0,
            "success_rate": 0,
            "avg_execution_time": 0,
            "latest_test_time": None,
            "test_status_distribution": {"success": 0, "failed": 0, "other": 0}
        }


@mcp.tool()
async def get_tool_performance_data(
    tool_id: str
) -> Dict[str, Any]:
    """获取工具性能数据
    
    Args:
        tool_id: 工具唯一标识符
    
    Returns:
        性能数据字典
    """
    try:
        # 调用工具模块中的性能数据函数
        result = await get_tool_performance_data_impl(tool_id)
        
        # 转换为字典返回
        return result.model_dump()
        
    except Exception as e:
        return {
            "scores": {
                "tashan_score": 0,
                "utility_score": 0,
                "sustainability_score": 0,
                "popularity_score": 0,
                "lobehub_score": 0,
                "comprehensive_score": 0
            },
            "performance_trend": [],
            "calculated_metrics": {"performance_index": 0, "reliability_score": 0}
        }


def main():
    """启动FastMCP服务器 - 支持多种部署模式和命令行参数"""
    parser = argparse.ArgumentParser(
        description="MCP工具评估助手服务器 - 支持uvx部署和Cherry Studio集成"
    )
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    # server 子命令
    server_parser = subparsers.add_parser('server', help='启动MCP服务器')
    server_parser.add_argument(
        '--transport', 
        choices=['stdio', 'sse', 'streamable-http'], 
        default='stdio',
        help='传输模式 (默认: stdio)'
    )
    server_parser.add_argument(
        '--host', 
        default='127.0.0.1',
        help='HTTP服务器监听地址 (默认: 127.0.0.1)'
    )
    server_parser.add_argument(
        '--port', 
        type=int, 
        default=8000,
        help='HTTP服务器端口 (默认: 8000)'
    )
    
    # test 子命令
    test_parser = subparsers.add_parser('test', help='运行测试')
    test_parser.add_argument('test_type', nargs='?', choices=['unit', 'integration', 'all'], help='测试类型')
    
    # info 子命令
    info_parser = subparsers.add_parser('info', help='显示服务器信息')
    
    # 解析参数
    args = parser.parse_args()
    
    # 如果没有指定命令，默认使用server模式
    if args.command is None:
        args.command = 'server'
    
    # 执行对应命令
    if args.command == 'server':
        start_server(args.transport, args.host, args.port)
    elif args.command == 'test':
        run_test(args.test_type)
    elif args.command == 'info':
        show_info()
    else:
        parser.print_help()


def start_server(transport: str = 'stdio', host: str = '127.0.0.1', port: int = 8000):
    """启动MCP服务器"""
    print(f"启动MCP服务器 - 传输模式: {transport}", file=sys.stderr)
    
    if transport == 'stdio':
        # stdio模式 - Cherry Studio兼容
        mcp.run(transport="stdio")
    elif transport == 'sse':
        # SSE模式
        mcp.run(transport="sse", host=host, port=port)
    elif transport == 'streamable-http':
        # HTTP模式
        mcp.run(transport="streamable-http", host=host, port=port)
    else:
        print(f"不支持的传输模式: {transport}", file=sys.stderr)
        sys.exit(1)


def run_test(test_type: Optional[str] = None):
    """运行测试"""
    import subprocess
    import os
    
    print(f"运行测试: {test_type or 'all'}", file=sys.stderr)
    
    try:
        if test_type == 'unit':
            cmd = ['uv', 'run', 'pytest', 'tests/', '-m', 'unit']
        elif test_type == 'integration':
            cmd = ['uv', 'run', 'pytest', 'tests/', '-m', 'integration']
        else:
            cmd = ['uv', 'run', 'pytest', 'tests/']
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        print("STDOUT:", result.stdout, file=sys.stderr)
        print("STDERR:", result.stderr, file=sys.stderr)
        print(f"测试完成，退出码: {result.returncode}", file=sys.stderr)
        
    except Exception as e:
        print(f"运行测试失败: {e}", file=sys.stderr)
        sys.exit(1)


def show_info():
    """显示服务器信息"""
    import asyncio
    
    print("MCP工具评估助手服务器信息", file=sys.stderr)
    print(f"版本: 0.3.2", file=sys.stderr)
    print(f"支持的传输模式: stdio, sse, streamable-http", file=sys.stderr)
    print(f"注册的工具数量: 5", file=sys.stderr)
    
    # 尝试连接数据库
    try:
        db = DatabaseManager()
        is_healthy = asyncio.run(db.health_check())
        total_tools = asyncio.run(db.get_total_tools_count())
        print(f"数据库状态: {'健康' if is_healthy else '不健康'}", file=sys.stderr)
        print(f"工具总数: {total_tools}", file=sys.stderr)
    except Exception as e:
        print(f"数据库连接失败: {e}", file=sys.stderr)


def run_simple_server():
    """运行简化的MCP服务器"""
    import asyncio
    import os
    import sys
    
    # 添加项目路径以便导入
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    sys.path.insert(0, project_root)
    
    # 导入简化的服务器
    from .simple_server import SimpleMCPServer, run_stdio_server
    
    # 静默模式 - 禁用警告但不重定向stdio
    import warnings
    warnings.filterwarnings("ignore")
    
    # 运行简化的服务器
    asyncio.run(run_stdio_server())


if __name__ == "__main__":
    # 检查是否使用simple_server模式
    if "--simple" in sys.argv:
        run_simple_server()
    else:
        # 默认使用FastMCP模式以支持所有新工具
        main()