#!/usr/bin/env python3
"""
setup.py for mcp-evaluation-server
包含C扩展模块的编译配置
"""

from setuptools import setup, find_packages, Extension
import os

# C扩展模块配置 - 仅在有编译环境时编译
try:
    securekey_ext = Extension(
        'mcp_evaluation_server.securekey_ext',
        sources=['mcp_evaluation_server/securekey_ext_simple.c'],
        extra_compile_args=['-O2', '-Wall'],
    )
    has_c_extension = True
except:
    securekey_ext = None
    has_c_extension = False

# Read the version from pyproject.toml or set a default
def get_version():
    try:
        import tomllib
        with open("pyproject.toml", "rb") as f:
            data = tomllib.load(f)
            return data["project"]["version"]
    except (ImportError, FileNotFoundError, KeyError):
        return "0.2.11"

# Read the long description from README
def get_long_description():
    readme_path = "docs/README_PYPI.md"
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    elif os.path.exists("README.md"):
        with open("README.md", "r", encoding="utf-8") as f:
            return f.read()
    return "MCP工具评估助手服务器"

setup(
    name="mcp-evaluation-server",
    version=get_version(),
    description="MCP工具评估助手服务器",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="gqy20",
    author_email="qingyu_ge@foxmail.com",
    maintainer="gqy20",
    maintainer_email="qingyu_ge@foxmail.com",
    url="https://github.com/gqy20/mcp-evaluation-server",
    license="MIT",
    
    # Package discovery
    packages=find_packages(include=["mcp_evaluation_server", "mcp_evaluation_server.*"]),
    
    # Include package data - 只包含C源文件，不包含预编译的.so文件
    package_data={
        "mcp_evaluation_server": ["*.json", "*.yml", "*.yaml", "*.txt", "*.c"],
    },
    include_package_data=True,
    
    # C扩展模块 - 仅在有C扩展时包含
    ext_modules=[securekey_ext] if has_c_extension else [],
    
    # Dependencies
    install_requires=[
        "fastmcp>=2.0.0",
        "pydantic>=2.0.0",
        "supabase>=2.0.0",
        "python-dotenv>=1.0.0",
    ],
    
    # Optional dependencies
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "isort>=5.0.0",
            "mypy>=1.0.0",
        ],
        "redis": [
            "redis>=5.0.0",
        ],
    },
    
    # Entry points
    entry_points={
        "console_scripts": [
            "mcp-evaluation-server=mcp_evaluation_server.main:main",
        ],
    },
    
    # Python version requirement
    python_requires=">=3.11",
    
    # C扩展特定配置
    zip_safe=False,  # C扩展不能使用zip安全模式
    
    # PyPI classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
    ],
    
    # Keywords
    keywords=["mcp", "evaluation", "tools", "server"],
)