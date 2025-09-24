"""MCP工具搜索模块 - 拆分后的工具实现"""

import logging
from typing import List, Optional, Dict, Any
from .database import DatabaseManager
from .models import (
    ToolSearchFilter, ToolSummary, TestInfo, PerformanceData,
    ToolDetailResponse, ToolSearchBasicResponse
)
from .utils import format_search_summary, log_search_query

logger = logging.getLogger(__name__)


async def search_mcp_tools_basic(
    query: Optional[str] = None,
    category: Optional[str] = None,
    min_tashan_score: Optional[float] = None,
    max_tashan_score: Optional[float] = None,
    deployment_method: Optional[str] = None,
    author: Optional[str] = None,
    limit: int = 20,
    offset: int = 0
) -> ToolSearchBasicResponse:
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
        包含工具摘要列表和搜索摘要的响应对象
        
    Example:
        >>> search_mcp_tools_basic(query="github", limit=10)
        ToolSearchBasicResponse(
            success=True,
            tools=[ToolSummary(...), ...],
            total_count=45,
            search_summary="找到 10 个工具(共 45 个)基于条件: 关键词 'github'",
            filters=ToolSearchFilter(...),
            error=None
        )
    """
    try:
        # 初始化数据库管理器
        db_manager = DatabaseManager()
        
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
        
        # 记录搜索查询
        log_search_query(filters)
        
        # 执行基础搜索
        tools_data = await db_manager.search_tools_basic(filters)
        
        # 获取总数
        total_count = await db_manager.get_total_tools_count()
        
        # 转换为ToolSummary对象
        tools = []
        for tool_data in tools_data:
            try:
                tool_summary = ToolSummary(**tool_data)
                tools.append(tool_summary)
            except Exception as e:
                logger.warning(f"解析工具摘要失败: {tool_data}, 错误: {e}")
                continue
        
        # 生成搜索摘要
        search_summary = format_search_summary(filters, total_count, len(tools))
        
        result = ToolSearchBasicResponse(
            success=True,
            tools=tools,
            total_count=total_count,
            search_summary=search_summary,
            filters=filters,
            error=None
        )
        
        logger.info(f"基础搜索完成: {search_summary}")
        return result
        
    except Exception as e:
        logger.error(f"基础搜索工具失败: {e}")
        return ToolSearchBasicResponse(
            success=False,
            tools=[],
            total_count=0,
            search_summary=f"搜索失败: {str(e)}",
            filters=ToolSearchFilter(),  # 空过滤器
            error=str(e)
        )


async def get_mcp_tool_details(
    tool_id: str,
    include_performance_data: bool = True,
    include_test_results: bool = True,
    test_results_limit: int = 5
) -> ToolDetailResponse:
    """获取MCP工具详细信息
    
    根据工具ID获取完整的工具信息，包括基本信息、测试统计、性能数据和最近的测试结果。
    
    Args:
        tool_id: 工具唯一标识符
        include_performance_data: 是否包含性能数据，默认True
        include_test_results: 是否包含测试结果，默认True
        test_results_limit: 测试结果数量限制，默认5
    
    Returns:
        包含完整工具详情的响应对象
        
    Example:
        >>> get_mcp_tool_details("tool_123")
        ToolDetailResponse(
            success=True,
            tool_details={
                "basic_info": {...},
                "test_stats": {...},
                "performance_data": {...},
                "recent_results": [...]
            },
            error=None
        )
    """
    try:
        # 初始化数据库管理器
        db_manager = DatabaseManager()
        
        if not tool_id:
            raise ValueError("工具ID不能为空")
        
        # 获取工具详情
        tool_details = await db_manager.get_tool_details(tool_id)
        
        if not tool_details:
            return ToolDetailResponse(
                success=False,
                tool_details=None,
                error=f"未找到ID为 '{tool_id}' 的工具"
            )
        
        # 根据参数选择性包含数据
        if not include_performance_data:
            tool_details["performance_data"] = None
        
        if not include_test_results:
            tool_details["recent_results"] = []
        else:
            # 限制测试结果数量
            tool_details["recent_results"] = tool_details.get("recent_results", [])[:test_results_limit]
        
        result = ToolDetailResponse(
            success=True,
            tool_details=tool_details,
            error=None
        )
        
        logger.info(f"获取工具详情成功: {tool_id}")
        return result
        
    except ValueError as e:
        logger.warning(f"参数验证失败: {e}")
        return ToolDetailResponse(
            success=False,
            tool_details=None,
            error=str(e)
        )
    except Exception as e:
        logger.error(f"获取工具详情失败: {e}")
        return ToolDetailResponse(
            success=False,
            tool_details=None,
            error=str(e)
        )


async def get_tool_test_stats(tool_id: str) -> TestInfo:
    """获取工具测试统计信息
    
    Args:
        tool_id: 工具唯一标识符
    
    Returns:
        测试统计信息对象
    """
    try:
        db_manager = DatabaseManager()
        
        if not tool_id:
            raise ValueError("工具ID不能为空")
        
        # 获取测试统计
        stats_data = await db_manager.get_tool_test_stats(tool_id)
        
        test_info = TestInfo(**stats_data)
        
        logger.info(f"获取测试统计成功: {tool_id}")
        return test_info
        
    except Exception as e:
        logger.error(f"获取测试统计失败: {e}")
        # 返回默认的测试统计
        return TestInfo(
            total_tests=0,
            successful_tests=0,
            failed_tests=0,
            success_rate=0,
            avg_execution_time=0,
            latest_test_time=None,
            test_status_distribution={"success": 0, "failed": 0, "other": 0}
        )


async def get_tool_performance_data(tool_id: str) -> PerformanceData:
    """获取工具性能数据
    
    Args:
        tool_id: 工具唯一标识符
    
    Returns:
        性能数据对象
    """
    try:
        db_manager = DatabaseManager()
        
        if not tool_id:
            raise ValueError("工具ID不能为空")
        
        # 获取性能数据
        performance_data = await db_manager.get_tool_performance_data(tool_id)
        
        perf_data = PerformanceData(**performance_data)
        
        logger.info(f"获取性能数据成功: {tool_id}")
        return perf_data
        
    except Exception as e:
        logger.error(f"获取性能数据失败: {e}")
        # 返回默认的性能数据
        return PerformanceData(
            scores={
                "tashan_score": 0,
                "utility_score": 0,
                "sustainability_score": 0,
                "popularity_score": 0,
                "lobehub_score": 0,
                "comprehensive_score": 0
            },
            performance_trend=[],
            calculated_metrics={"performance_index": 0, "reliability_score": 0}
        )