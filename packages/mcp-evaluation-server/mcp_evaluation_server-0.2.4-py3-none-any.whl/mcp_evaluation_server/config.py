"""MCP评估服务器配置管理"""

import os
import sys
from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field

# 导入安全密钥管理器
try:
    from .secure_key_manager import SecureKeyManager
    SECURE_KEY_AVAILABLE = True
except ImportError:
    SECURE_KEY_AVAILABLE = False


class SecureSettings(BaseSettings):
    """安全配置基类"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._secure_manager = SecureConfigManager()
    
    def get_secure_api_key(self, env_var_name: str, service_name: str) -> Optional[str]:
        """获取安全API密钥"""
        # 首先尝试环境变量
        api_key = os.getenv(env_var_name)
        if api_key:
            return api_key
        
        # 尝试从安全存储中获取
        return self._secure_manager.secure_retrieve_api_key(service_name)
    
    def store_api_key_securely(self, env_var_name: str, service_name: str) -> bool:
        """安全存储API密钥"""
        api_key = os.getenv(env_var_name)
        if not api_key:
            return False
            
        return self._secure_manager.secure_store_api_key(service_name, api_key)


class Settings(SecureSettings):
    """应用配置"""

    # Supabase数据库配置（可选）
    supabase_url: Optional[str] = None
    supabase_service_role_key: Optional[str] = None
    
    # 数据表名称
    mcp_tools_table: str = "mcp_tools"
    mcp_test_results_table: str = "mcp_test_results"

    # 缓存配置
    redis_url: Optional[str] = None
    cache_ttl: int = 3600

    # 日志配置
    log_level: str = "INFO"
    log_file: Optional[str] = None  # 默认不写文件
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 尝试从安全存储或环境变量获取配置
        if not self.supabase_url:
            self.supabase_url = (
                self.get_secure_api_key("SUPABASE_URL", "supabase_url") or 
                "https://vmikqjfxbdvfpakvwoab.supabase.co"
            )
        
        if not self.supabase_service_role_key:
            self.supabase_service_role_key = (
                self.get_secure_api_key("SUPABASE_SERVICE_ROLE_KEY", "supabase_key") or
                "sb_secret_em8lCb9T8Vt2bgYuntSENQ_HgFTCwP4"
            )
    
    def get_log_file(self) -> Optional[str]:
        """获取日志文件路径，如果目录不存在则创建"""
        if self.log_file:
            log_path = Path(self.log_file)
            # 如果是相对路径，使用当前目录
            if not log_path.is_absolute():
                log_path = Path.cwd() / log_path
            # 创建日志目录
            log_path.parent.mkdir(parents=True, exist_ok=True)
            return str(log_path)
        return None
    
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "allow"
    }


# 全局配置实例
def get_settings():
    """获取配置实例"""
    global settings
    if settings is None:
        try:
            settings = Settings()
        except Exception as e:
            import sys
            # 只在HTTP模式下输出错误信息
            if "server" in sys.argv[1:2] or "http" in sys.argv[1:2]:
                print(f"❌ 配置加载失败: {e}")
                print("请确保设置了以下环境变量：")
                print("  - SUPABASE_URL")
                print("  - SUPABASE_SERVICE_ROLE_KEY")
                print("或者创建 .env 文件（参考 .env.example）")
            raise ConfigurationError(f"配置加载失败: {e}")
    return settings


def get_secure_supabase_config():
    """获取安全的Supabase配置"""
    settings_instance = get_settings()
    
    # 首先尝试从环境变量获取
    url = settings_instance.supabase_url
    key = settings_instance.supabase_service_role_key
    
    # 如果没有配置，尝试从安全存储获取
    if not url or not key:
        url = settings_instance.get_secure_api_key("SUPABASE_URL", "supabase")
        key = settings_instance.get_secure_api_key("SUPABASE_SERVICE_ROLE_KEY", "supabase")
    
    return url, key


def setup_secure_storage():
    """设置安全存储"""
    if not SECURE_KEY_AVAILABLE:
        print("⚠️ 安全密钥管理模块不可用")
        return False
    
    settings_instance = get_settings()
    
    # 安全存储Supabase配置
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    
    if supabase_url and supabase_key:
        success1 = settings_instance.store_api_key_securely("SUPABASE_URL", "supabase")
        success2 = settings_instance.store_api_key_securely("SUPABASE_SERVICE_ROLE_KEY", "supabase")
        
        if success1 and success2:
            print("✅ Supabase配置已安全存储")
            print("💡 现在可以安全地删除环境变量中的敏感信息")
        else:
            print("❌ 安全存储失败")
            return False
    
    return True


def cleanup_secure_storage():
    """清理安全存储"""
    if SECURE_KEY_AVAILABLE:
        secure_config_manager.cleanup_secure_storage()
        print("🧹 安全存储已清理")


class ConfigurationError(Exception):
    """配置错误异常"""
    pass


class SecureConfigManager:
    """安全配置管理器"""
    
    def __init__(self):
        self.key_manager = None
        self.secure_storage_path = Path.home() / ".mcp_evaluation" / "secure_keys"
        
        if SECURE_KEY_AVAILABLE:
            self.key_manager = SecureKeyManager()
    
    def secure_store_api_key(self, service_name: str, api_key: str) -> bool:
        """安全存储API密钥"""
        if not SECURE_KEY_AVAILABLE or not self.key_manager:
            return False
            
        try:
            storage_path = self.secure_storage_path / service_name
            return self.key_manager.encrypt_and_store(api_key, str(storage_path))
        except Exception:
            return False
    
    def secure_retrieve_api_key(self, service_name: str) -> Optional[str]:
        """安全检索API密钥"""
        if not SECURE_KEY_AVAILABLE or not self.key_manager:
            return None
            
        try:
            storage_path = self.secure_storage_path / service_name
            return self.key_manager.load_and_decrypt(str(storage_path))
        except Exception:
            return None
    
    def cleanup_secure_storage(self, service_name: Optional[str] = None):
        """清理安全存储"""
        if not SECURE_KEY_AVAILABLE or not self.key_manager:
            return
            
        try:
            if service_name:
                storage_path = self.secure_storage_path / service_name
                self.key_manager.cleanup(str(storage_path))
            else:
                # 清理所有服务
                if self.secure_storage_path.exists():
                    for service_dir in self.secure_storage_path.iterdir():
                        if service_dir.is_dir():
                            self.key_manager.cleanup(str(service_dir))
        except Exception:
            pass


# 全局安全配置管理器
secure_config_manager = SecureConfigManager()

# 延迟加载配置
settings = None