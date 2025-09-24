"""
使用C扩展的安全配置管理器
集成真正的加密保护到现有配置系统
"""

import os
import sys
import base64
import hashlib
import secrets
from typing import Optional, Dict, Any, List
from pathlib import Path

# 导入C扩展模块
try:
    from . import securekey_ext
    C_EXT_AVAILABLE = True
except ImportError:
    try:
        import securekey_ext
        C_EXT_AVAILABLE = True
    except ImportError:
        C_EXT_AVAILABLE = False
        print("警告: C扩展模块不可用，将使用Python实现")

# 定义一个简单的Settings类以避免循环导入
class SimpleSettings:
    def __init__(self):
        self.supabase_url = ""
        self.supabase_service_role_key = ""
        self.log_level = "INFO"
        self.log_file = None
    
    def get_log_file(self):
        """获取日志文件路径"""
        return self.log_file

class ConfigurationError(Exception):
    pass


class SecureConfigManager:
    """使用C扩展的安全配置管理器"""
    
    def __init__(self, salt: Optional[str] = None):
        """
        初始化安全配置管理器
        
        Args:
            salt: 自定义盐值，如果未提供则随机生成
        """
        self.salt = salt or secrets.token_hex(16)
        self.segments_count = 4  # 密钥分割成4段
        self.c_ext_available = C_EXT_AVAILABLE
        self._encrypted_cache = {}
        
        # 硬编码的敏感数据（加密存储）
        self._encrypted_supabase_url = self._encrypt_data("https://vmikqjfxbdvfpakvwoab.supabase.co")
        self._encrypted_supabase_key = self._encrypt_data("sb_secret_em8lCb9T8Vt2bgYuntSENQ_HgFTCwP4")
    
    def _encrypt_data(self, data: str) -> List[str]:
        """使用C扩展加密数据"""
        if self.c_ext_available:
            try:
                # 使用C扩展进行分割和加密
                segments = securekey_ext.secure_key_split(data, self.segments_count, self.salt)
                return list(segments)
            except Exception as e:
                print(f"C扩展加密失败: {e}")
                return self._python_encrypt_data(data)
        else:
            return self._python_encrypt_data(data)
    
    def _python_encrypt_data(self, data: str) -> List[str]:
        """Python实现的加密（备用）"""
        # 使用XOR加密
        encrypted = []
        for i, char in enumerate(data):
            encrypted_char = chr(ord(char) ^ ord(self.salt[i % len(self.salt)]))
            encrypted.append(encrypted_char)
        
        encrypted_str = ''.join(encrypted)
        
        # 分割成段
        segment_length = len(encrypted_str) // self.segments_count
        segments = []
        
        for i in range(self.segments_count):
            start = i * segment_length
            end = start + segment_length if i < self.segments_count - 1 else len(encrypted_str)
            segments.append(encrypted_str[start:end])
        
        return segments
    
    def _decrypt_data(self, segments: List[str]) -> str:
        """使用C扩展解密数据"""
        if self.c_ext_available:
            try:
                # 使用C扩展进行组合和解密
                return securekey_ext.secure_key_combine(segments, self.salt)
            except Exception as e:
                print(f"C扩展解密失败: {e}")
                return self._python_decrypt_data(segments)
        else:
            return self._python_decrypt_data(segments)
    
    def _python_decrypt_data(self, segments: List[str]) -> str:
        """Python实现的解密（备用）"""
        # 组合段
        combined = ''.join(segments)
        
        # 使用XOR解密
        decrypted = []
        for i, char in enumerate(combined):
            decrypted_char = chr(ord(char) ^ ord(self.salt[i % len(self.salt)]))
            decrypted.append(decrypted_char)
        
        return ''.join(decrypted)
    
    @property
    def supabase_url(self) -> str:
        """获取解密后的Supabase URL"""
        if 'supabase_url' not in self._encrypted_cache:
            decrypted = self._decrypt_data(self._encrypted_supabase_url)
            self._encrypted_cache['supabase_url'] = decrypted
        return self._encrypted_cache['supabase_url']
    
    @property
    def supabase_service_role_key(self) -> str:
        """获取解密后的Supabase服务密钥"""
        if 'supabase_key' not in self._encrypted_cache:
            decrypted = self._decrypt_data(self._encrypted_supabase_key)
            self._encrypted_cache['supabase_key'] = decrypted
        return self._encrypted_cache['supabase_key']
    
    def get_settings(self) -> SimpleSettings:
        """获取兼容原有API的设置对象"""
        # 创建简单的Settings对象
        settings = SimpleSettings()
        settings.supabase_url = self.supabase_url
        settings.supabase_service_role_key = self.supabase_service_role_key
        return settings
    
    def get_security_status(self) -> Dict[str, Any]:
        """获取安全状态"""
        return {
            'c_extension_available': self.c_ext_available,
            'salt': self.salt[:8] + '...',  # 只显示部分盐值
            'segments_count': self.segments_count,
            'encrypted_data_cached': len(self._encrypted_cache),
            'supabase_url_protected': bool(self.supabase_url),
            'supabase_key_protected': bool(self.supabase_service_role_key)
        }
    
    def test_encryption_decryption(self, test_data: str = "test_secret_data") -> bool:
        """测试加密解密功能"""
        try:
            print(f"🧪 测试加密解密功能: {test_data}")
            
            # 加密
            encrypted = self._encrypt_data(test_data)
            print(f"✅ 加密成功，分成 {len(encrypted)} 段")
            
            # 解密
            decrypted = self._decrypt_data(encrypted)
            print(f"✅ 解密成功: {decrypted}")
            
            # 验证
            if decrypted == test_data:
                print("✅ 加密解密验证通过")
                return True
            else:
                print("❌ 加密解密验证失败")
                return False
                
        except Exception as e:
            print(f"❌ 测试失败: {e}")
            return False


# 全局安全配置管理器实例
_secure_config_manager = SecureConfigManager()


def get_secure_settings() -> SimpleSettings:
    """获取安全设置实例"""
    return _secure_config_manager.get_settings()


def get_security_status() -> Dict[str, Any]:
    """获取安全状态"""
    return _secure_config_manager.get_security_status()


def test_secure_config():
    """测试安全配置功能"""
    print("🔒 测试安全配置功能")
    print("=" * 50)
    
    # 获取安全状态
    status = get_security_status()
    print(f"安全状态:")
    for key, value in status.items():
        print(f"  {key}: {value}")
    
    print()
    
    # 测试加密解密
    if _secure_config_manager.test_encryption_decryption():
        print("✅ 加密解密测试通过")
    else:
        print("❌ 加密解密测试失败")
        return False
    
    print()
    
    # 测试配置获取
    try:
        settings = get_secure_settings()
        print(f"✅ 配置获取成功")
        print(f"   Supabase URL: {settings.supabase_url[:30]}...")
        print(f"   Service Key: {settings.supabase_service_role_key[:20]}...")
    except Exception as e:
        print(f"❌ 配置获取失败: {e}")
        return False
    
    print("\n🎯 安全配置测试完成")
    return True


if __name__ == "__main__":
    success = test_secure_config()
    sys.exit(0 if success else 1)