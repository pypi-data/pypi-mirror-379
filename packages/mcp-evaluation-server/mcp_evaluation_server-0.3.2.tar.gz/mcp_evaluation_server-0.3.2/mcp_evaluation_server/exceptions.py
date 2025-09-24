"""
自定义异常类定义
"""

from typing import Optional, Dict, Any


class MCPDatabaseError(Exception):
    """数据库相关异常的基类"""
    
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        self.message = message
        self.details = details or {}
        super().__init__(self.message)


class MCPDatabaseConnectionError(MCPDatabaseError):
    """数据库连接异常"""
    pass


class MCPDatabaseQueryError(MCPDatabaseError):
    """数据库查询异常"""
    
    def __init__(self, message: str, query: Optional[str] = None, details: Optional[Dict[str, Any]] = None):
        self.query = query
        super().__init__(message, details)


class MCPConfigurationError(Exception):
    """配置相关异常"""
    pass


class MCPValidationError(Exception):
    """数据验证异常"""
    
    def __init__(self, message: str, field_name: Optional[str] = None, invalid_value: Optional[Any] = None):
        self.field_name = field_name
        self.invalid_value = invalid_value
        super().__init__(message)


class MCPTimeoutError(Exception):
    """操作超时异常"""
    
    def __init__(self, message: str, timeout_seconds: Optional[float] = None):
        self.timeout_seconds = timeout_seconds
        super().__init__(message)


class MCPAuthenticationError(Exception):
    """认证相关异常"""
    pass


class MCPRateLimitError(Exception):
    """速率限制异常"""
    
    def __init__(self, message: str, retry_after: Optional[float] = None):
        self.retry_after = retry_after
        super().__init__(message)