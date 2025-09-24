"""
安全密钥管理C扩展模块
编译说明: python setup.py build_ext --inplace
"""

from setuptools import setup, Extension

module = Extension(
    'securekey_ext',
    sources=['securekey_ext_simple.c'],
    extra_compile_args=['-O2', '-Wall'],
)

setup(
    name='SecureKeyExtension',
    version='1.0',
    description='Secure key management C extension',
    ext_modules=[module],
)