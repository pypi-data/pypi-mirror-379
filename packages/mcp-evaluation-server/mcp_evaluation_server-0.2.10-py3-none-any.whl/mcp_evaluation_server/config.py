"""MCP评估服务器配置管理"""

from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """应用配置 - 使用硬编码配置确保在任何环境下都能正常工作"""

    # Supabase数据库配置 - 硬编码
    supabase_url: str = "https://vmikqjfxbdvfpakvwoab.supabase.co"
    supabase_service_role_key: str = "sb_secret_em8lCb9T8Vt2bgYuntSENQ_HgFTCwP4"
    
    # 数据表名称 - 硬编码
    mcp_tools_table: str = "mcp_test_results"
    mcp_test_results_table: str = "mcp_test_results"

    # 缓存配置 - 硬编码
    redis_url: Optional[str] = None
    cache_ttl: int = 3600

    # 日志配置 - 硬编码
    log_level: str = "INFO"
    log_file: Optional[str] = None  # 默认不写文件
    
    def get_log_file(self) -> Optional[str]:
        """获取日志文件路径，如果目录不存在则创建"""
        if self.log_file:
            log_path = Path(self.log_file)
            # 如果是相对路径，使用当前目录
            if not log_path.is_absolute():
                log_path = Path.cwd() / log_path
            
            # 确保目录存在
            log_path.parent.mkdir(parents=True, exist_ok=True)
            return str(log_path)
        return None
    
    def __str__(self) -> str:
        """安全字符串表示，隐藏敏感信息"""
        safe_info = {
            "supabase_url": f"{self.supabase_url[:20]}..." if self.supabase_url else "Not set",
            "supabase_service_role_key": f"{'*' * 20}..." if self.supabase_service_role_key else "Not set",
            "mcp_tools_table": self.mcp_tools_table,
            "mcp_test_results_table": self.mcp_test_results_table,
            "redis_url": "Enabled" if self.redis_url else "Disabled",
            "cache_ttl": self.cache_ttl,
            "log_level": self.log_level,
            "log_file": "Enabled" if self.log_file else "Disabled"
        }
        return f"Settings({', '.join(f'{k}={v}' for k, v in safe_info.items())})"
    
    def __repr__(self) -> str:
        """安全表示，隐藏敏感信息"""
        return self.__str__()
    
    def model_dump(self, **kwargs) -> dict:
        """安全的字典输出，隐藏敏感信息"""
        data = super().model_dump(**kwargs)
        if 'supabase_service_role_key' in data:
            data['supabase_service_role_key'] = '*' * 20 + "..."
        return data
    
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "allow"
    }


# 全局配置实例
_settings_instance = None

def get_settings() -> Settings:
    """获取配置实例 - 单例模式"""
    global _settings_instance
    if _settings_instance is None:
        _settings_instance = Settings()
    return _settings_instance


class ConfigurationError(Exception):
    """配置错误异常"""
    pass