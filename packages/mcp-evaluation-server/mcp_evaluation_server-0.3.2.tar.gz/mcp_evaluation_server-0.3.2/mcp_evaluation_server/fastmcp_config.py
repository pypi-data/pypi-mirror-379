"""FastMCP配置管理

专门为uvx部署和Cherry Studio兼容性优化
与现有的安全配置系统分离，专注于运行时配置
"""

import os
import sys
import logging
import warnings
from typing import Dict, Any, Optional

# 禁用所有print输出，避免干扰MCP通信
_original_print = print
def _silent_print(*args, **kwargs):
    pass
print = _silent_print


class FastMCPRuntimeConfig:
    """FastMCP运行时配置类
    
    专注于环境变量、日志和警告的配置
    与SecureSettings分离，处理运行时行为
    """
    
    @staticmethod
    def setup_environment():
        """设置环境变量 - 优化uvx部署和Cherry Studio兼容性"""
        # 禁用FastMCP横幅和启动信息
        os.environ["FASTMCP_DISABLE_BANNER"] = "1"
        
        # 设置编码，确保在Cherry Studio中正常工作
        os.environ["PYTHONIOENCODING"] = "utf-8"
        
        # 禁用Python开发模式，避免额外输出
        os.environ["PYTHONDEVMODE"] = "0"
        
        # 优化性能相关设置
        os.environ["PYTHONUNBUFFERED"] = "1"
        
        # 设置stdio模式，控制配置输出
        os.environ["MCP_STDIO_MODE"] = "true"
        
    @staticmethod
    def configure_logging():
        """配置日志 - 完全静默，避免干扰MCP通信"""
        # 设置根日志级别为最高
        logging.getLogger().setLevel(logging.CRITICAL)
        
        # 禁用特定模块的日志输出
        disabled_loggers = [
            "fastmcp",
            "mcp_evaluation_server",
            "urllib3",
            "httpx",
            "supabase",
            "httpcore",
            "anyio"
        ]
        
        for logger_name in disabled_loggers:
            logger = logging.getLogger(logger_name)
            logger.setLevel(logging.CRITICAL)
            # 移除所有处理器
            for handler in logger.handlers[:]:
                logger.removeHandler(handler)
            # 添加NullHandler防止"No handler found"警告
            logger.addHandler(logging.NullHandler())
        
        # 处理根日志器
        root_logger = logging.getLogger()
        # 移除现有处理器
        for handler in root_logger.handlers[:]:
            root_logger.removeHandler(handler)
        # 添加NullHandler
        root_logger.addHandler(logging.NullHandler())
    
    @staticmethod
    def configure_warnings():
        """配置警告过滤 - 完全静默"""
        # 禁用所有警告
        warnings.filterwarnings("ignore")
        
        # 禁用特定类型的警告
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        warnings.filterwarnings("ignore", category=FutureWarning)
        warnings.filterwarnings("ignore", category=UserWarning)
        warnings.filterwarnings("ignore", category=ImportWarning)
        warnings.filterwarnings("ignore", category=ResourceWarning)
        
        # 禁用特定的警告消息
        warnings.filterwarnings("ignore", message=".*No handler found.*")
        warnings.filterwarnings("ignore", message=".*has no attribute.*")
    
    @staticmethod
    def get_stdio_config() -> Dict[str, Any]:
        """获取stdio模式配置"""
        return {
            "transport": "stdio",
            "log_level": "CRITICAL",
            "silent": True
        }
    
    @classmethod
    def apply_all_configurations(cls):
        """应用所有配置"""
        cls.setup_environment()
        cls.configure_logging()
        cls.configure_warnings()


# 向后兼容的别名
FastMCPConfig = FastMCPRuntimeConfig