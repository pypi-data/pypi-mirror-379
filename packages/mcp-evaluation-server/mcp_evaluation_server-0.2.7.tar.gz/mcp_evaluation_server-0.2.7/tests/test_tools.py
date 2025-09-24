"""新MCP工具模块测试"""

import pytest
from unittest.mock import Mock, AsyncMock, patch
from mcp_evaluation_server.tools import (
    search_mcp_tools_basic,
    get_mcp_tool_details,
    get_tool_test_stats,
    get_tool_performance_data
)
from mcp_evaluation_server.models import (
    ToolSearchFilter, ToolSummary, TestInfo, PerformanceData,
    ToolDetailResponse, ToolSearchBasicResponse
)


class TestSearchMCPToolsBasic:
    """测试基础搜索工具"""
    
    @pytest.mark.asyncio
    async def test_search_tools_basic_success(self):
        """测试成功的基础搜索"""
        # 模拟数据库返回数据
        mock_tools_data = [
            {
                "tool_id": "tool_1",
                "name": "Test Tool 1",
                "author": "Author 1",
                "category": "开发工具推荐",
                "tashan_score": 85.5,
                "description": "A test tool",
                "github_url": "https://github.com/test/tool1"
            },
            {
                "tool_id": "tool_2", 
                "name": "Test Tool 2",
                "author": "Author 2",
                "category": "文档处理",
                "tashan_score": 72.0,
                "description": "Another test tool",
                "github_url": "https://github.com/test/tool2"
            }
        ]
        
        with patch('mcp_evaluation_server.tools.DatabaseManager') as mock_db_class:
            # 设置模拟数据库管理器
            mock_db_manager = AsyncMock()
            mock_db_manager.search_tools_basic.return_value = mock_tools_data
            mock_db_manager.get_total_tools_count.return_value = 50
            mock_db_class.return_value = mock_db_manager
            
            # 执行搜索
            result = await search_mcp_tools_basic(query="test", limit=10)
            
            # 验证结果
            assert isinstance(result, ToolSearchBasicResponse)
            assert result.success is True
            assert len(result.tools) == 2
            assert result.total_count == 50
            assert result.tools[0].name == "Test Tool 1"
            assert result.tools[1].tashan_score == 72.0
            
            # 验证数据库调用
            mock_db_manager.search_tools_basic.assert_called_once()
            call_args = mock_db_manager.search_tools_basic.call_args[0][0]
            assert isinstance(call_args, ToolSearchFilter)
            assert call_args.query == "test"
            assert call_args.limit == 10
    
    @pytest.mark.asyncio 
    async def test_search_tools_basic_with_filters(self):
        """测试带过滤器的基础搜索"""
        mock_tools_data = [
            {
                "tool_id": "tool_1",
                "name": "Filtered Tool",
                "author": "Test Author",
                "category": "开发工具推荐",
                "tashan_score": 90.0,
                "description": "A filtered tool",
                "github_url": "https://github.com/test/filtered"
            }
        ]
        
        with patch('mcp_evaluation_server.tools.DatabaseManager') as mock_db_class:
            mock_db_manager = AsyncMock()
            mock_db_manager.search_tools_basic.return_value = mock_tools_data
            mock_db_manager.get_total_tools_count.return_value = 1
            mock_db_class.return_value = mock_db_manager
            
            # 执行带过滤器的搜索
            result = await search_mcp_tools_basic(
                query="filtered",
                category="开发工具推荐",
                min_tashan_score=80,
                max_tashan_score=95,
                author="Test Author",
                limit=5,
                offset=10
            )
            
            # 验证结果
            assert result.success is True
            assert len(result.tools) == 1
            assert result.tools[0].category == "开发工具推荐"
            
            # 验证过滤器设置
            call_args = mock_db_manager.search_tools_basic.call_args[0][0]
            assert call_args.category == "开发工具推荐"
            assert call_args.min_tashan_score == 80
            assert call_args.max_tashan_score == 95
            assert call_args.author == "Test Author"
            assert call_args.offset == 10
    
    @pytest.mark.asyncio
    async def test_search_tools_basic_validation(self):
        """测试参数验证"""
        with patch('mcp_evaluation_server.tools.DatabaseManager') as mock_db_class:
            mock_db_manager = AsyncMock()
            mock_db_manager.search_tools_basic.return_value = []
            mock_db_manager.get_total_tools_count.return_value = 0
            mock_db_class.return_value = mock_db_manager
            
            # 测试边界值
            result = await search_mcp_tools_basic(
                query="test",
                min_tashan_score=-10,  # 应该被调整为0
                max_tashan_score=150,  # 应该被调整为100
                limit=200,  # 应该被调整为100
                offset=-5  # 应该被调整为0
            )
            
            call_args = mock_db_manager.search_tools_basic.call_args[0][0]
            assert call_args.min_tashan_score == 0
            assert call_args.max_tashan_score == 100
            assert call_args.limit == 100
            assert call_args.offset == 0
    
    @pytest.mark.asyncio
    async def test_search_tools_basic_error_handling(self):
        """测试错误处理"""
        with patch('mcp_evaluation_server.tools.DatabaseManager') as mock_db_class:
            mock_db_manager = AsyncMock()
            mock_db_manager.search_tools_basic.side_effect = Exception("Database error")
            mock_db_class.return_value = mock_db_manager
            
            result = await search_mcp_tools_basic(query="test")
            
            assert result.success is False
            assert len(result.tools) == 0
            assert result.total_count == 0
            assert "Database error" in result.search_summary
            assert result.error == "Database error"


class TestGetMCPToolDetails:
    """测试获取工具详情工具"""
    
    @pytest.mark.asyncio
    async def test_get_tool_details_success(self):
        """测试成功获取工具详情"""
        mock_tool_details = {
            "basic_info": {
                "tool_id": "tool_123",
                "name": "Test Tool",
                "author": "Test Author",
                "description": "A comprehensive test tool"
            },
            "test_stats": {
                "total_tests": 10,
                "successful_tests": 8,
                "failed_tests": 2,
                "success_rate": 80.0
            },
            "performance_data": {
                "scores": {"tashan_score": 85.0},
                "performance_trend": [],
                "calculated_metrics": {"performance_index": 85.0}
            },
            "recent_results": [
                {"test_id": "test_1", "test_status": "success"},
                {"test_id": "test_2", "test_status": "failed"}
            ]
        }
        
        with patch('mcp_evaluation_server.tools.DatabaseManager') as mock_db_class:
            mock_db_manager = AsyncMock()
            mock_db_manager.get_tool_details.return_value = mock_tool_details
            mock_db_class.return_value = mock_db_manager
            
            result = await get_mcp_tool_details("tool_123")
            
            assert isinstance(result, ToolDetailResponse)
            assert result.success is True
            assert result.tool_details is not None
            assert result.tool_details["basic_info"]["name"] == "Test Tool"
            assert result.tool_details["test_stats"]["success_rate"] == 80.0
            assert len(result.tool_details["recent_results"]) == 2
            
            mock_db_manager.get_tool_details.assert_called_once_with("tool_123")
    
    @pytest.mark.asyncio
    async def test_get_tool_details_not_found(self):
        """测试工具不存在的情况"""
        with patch('mcp_evaluation_server.tools.DatabaseManager') as mock_db_class:
            mock_db_manager = AsyncMock()
            mock_db_manager.get_tool_details.return_value = None
            mock_db_class.return_value = mock_db_manager
            
            result = await get_mcp_tool_details("nonexistent_tool")
            
            assert result.success is False
            assert result.tool_details is None
            assert "未找到ID为 'nonexistent_tool' 的工具" in result.error
    
    @pytest.mark.asyncio
    async def test_get_tool_details_optional_data(self):
        """测试可选数据包含控制"""
        mock_tool_details = {
            "basic_info": {"tool_id": "tool_123", "name": "Test Tool"},
            "test_stats": {"total_tests": 5, "success_rate": 100.0},
            "performance_data": {"scores": {"tashan_score": 90.0}},
            "recent_results": [{"test_id": "test_1"}, {"test_id": "test_2"}, {"test_id": "test_3"}]
        }
        
        with patch('mcp_evaluation_server.tools.DatabaseManager') as mock_db_class:
            mock_db_manager = AsyncMock()
            mock_db_manager.get_tool_details.return_value = mock_tool_details
            mock_db_class.return_value = mock_db_manager
            
            # 测试不包含性能数据
            result1 = await get_mcp_tool_details("tool_123", include_performance_data=False)
            assert result1.success is True
            assert result1.tool_details["performance_data"] is None
            assert len(result1.tool_details["recent_results"]) == 3
            
            # 测试限制测试结果数量
            result2 = await get_mcp_tool_details("tool_123", test_results_limit=2)
            assert result2.success is True
            assert len(result2.tool_details["recent_results"]) == 2
    
    @pytest.mark.asyncio
    async def test_get_tool_details_empty_id(self):
        """测试空工具ID"""
        result = await get_mcp_tool_details("")
        
        assert result.success is False
        assert result.tool_details is None
        assert "工具ID不能为空" in result.error
    
    @pytest.mark.asyncio
    async def test_get_tool_details_error_handling(self):
        """测试错误处理"""
        with patch('mcp_evaluation_server.tools.DatabaseManager') as mock_db_class:
            mock_db_manager = AsyncMock()
            mock_db_manager.get_tool_details.side_effect = Exception("Connection failed")
            mock_db_class.return_value = mock_db_manager
            
            result = await get_mcp_tool_details("tool_123")
            
            assert result.success is False
            assert result.tool_details is None
            assert result.error == "Connection failed"


class TestGetToolTestStats:
    """测试获取工具测试统计"""
    
    @pytest.mark.asyncio
    async def test_get_test_stats_success(self):
        """测试成功获取测试统计"""
        mock_stats_data = {
            "total_tests": 20,
            "successful_tests": 15,
            "failed_tests": 5,
            "success_rate": 75.0,
            "avg_execution_time": 2.5,
            "latest_test_time": "2024-01-01T12:00:00",
            "test_status_distribution": {"success": 15, "failed": 5, "other": 0}
        }
        
        with patch('mcp_evaluation_server.tools.DatabaseManager') as mock_db_class:
            mock_db_manager = AsyncMock()
            mock_db_manager.get_tool_test_stats.return_value = mock_stats_data
            mock_db_class.return_value = mock_db_manager
            
            result = await get_tool_test_stats("tool_123")
            
            assert isinstance(result, TestInfo)
            assert result.total_tests == 20
            assert result.success_rate == 75.0
            assert result.avg_execution_time == 2.5
            
            mock_db_manager.get_tool_test_stats.assert_called_once_with("tool_123")
    
    @pytest.mark.asyncio
    async def test_get_test_stats_error_handling(self):
        """测试错误处理"""
        with patch('mcp_evaluation_server.tools.DatabaseManager') as mock_db_class:
            mock_db_manager = AsyncMock()
            mock_db_manager.get_tool_test_stats.side_effect = Exception("Database error")
            mock_db_class.return_value = mock_db_manager
            
            result = await get_tool_test_stats("tool_123")
            
            assert isinstance(result, TestInfo)
            assert result.total_tests == 0  # 默认值
            assert result.success_rate == 0.0


class TestGetToolPerformanceData:
    """测试获取工具性能数据"""
    
    @pytest.mark.asyncio
    async def test_get_performance_data_success(self):
        """测试成功获取性能数据"""
        mock_perf_data = {
            "scores": {
                "tashan_score": 85.0,
                "utility_score": 80.0,
                "sustainability_score": 90.0
            },
            "performance_trend": [
                {"timestamp": "2024-01-01T12:00:00", "execution_time": 2.0, "status": "success"},
                {"timestamp": "2024-01-02T12:00:00", "execution_time": 1.8, "status": "success"}
            ],
            "calculated_metrics": {
                "performance_index": 85.0,
                "reliability_score": 95.0
            }
        }
        
        with patch('mcp_evaluation_server.tools.DatabaseManager') as mock_db_class:
            mock_db_manager = AsyncMock()
            mock_db_manager.get_tool_performance_data.return_value = mock_perf_data
            mock_db_class.return_value = mock_db_manager
            
            result = await get_tool_performance_data("tool_123")
            
            assert isinstance(result, PerformanceData)
            assert result.scores["tashan_score"] == 85.0
            assert len(result.performance_trend) == 2
            assert result.calculated_metrics["performance_index"] == 85.0
            
            mock_db_manager.get_tool_performance_data.assert_called_once_with("tool_123")
    
    @pytest.mark.asyncio
    async def test_get_performance_data_error_handling(self):
        """测试错误处理"""
        with patch('mcp_evaluation_server.tools.DatabaseManager') as mock_db_class:
            mock_db_manager = AsyncMock()
            mock_db_manager.get_tool_performance_data.side_effect = Exception("Database error")
            mock_db_class.return_value = mock_db_manager
            
            result = await get_tool_performance_data("tool_123")
            
            assert isinstance(result, PerformanceData)
            assert result.scores["tashan_score"] == 0  # 默认值
            assert len(result.performance_trend) == 0