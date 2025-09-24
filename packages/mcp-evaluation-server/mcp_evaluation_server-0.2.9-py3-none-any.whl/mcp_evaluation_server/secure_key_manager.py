"""
安全密钥管理模块 - 用于防御性安全目的
实现密钥分割、混淆存储和动态解密
"""

import os
import sys
import base64
import hashlib
import secrets
from typing import Optional, Tuple, List
from pathlib import Path


class SecureKeyManager:
    """
    安全密钥管理器 - 用于保护敏感配置信息
    
    注意：此方案仅增加提取难度，不能提供真正的安全保障
    仅适用于低风险场景，高风险场景请使用外部密钥管理
    """
    
    def __init__(self, salt: Optional[str] = None):
        """
        初始化密钥管理器
        
        Args:
            salt: 自定义盐值，如果未提供则随机生成
        """
        self.salt = salt or secrets.token_hex(16)
        self.segments_count = 5  # 密钥分割成5段
        self.obfuscation_rounds = 3  # 混淆轮数
        
    def _split_key(self, key: str) -> List[str]:
        """将密钥分割成多个片段"""
        # 对密钥进行编码
        encoded = base64.b64encode(key.encode()).decode()
        
        # 添加随机前缀和后缀进行混淆
        prefix = secrets.token_hex(8)
        suffix = secrets.token_hex(8)
        confused = prefix + encoded + suffix
        
        # 分割成多个片段
        segment_length = len(confused) // self.segments_count
        segments = []
        
        for i in range(self.segments_count):
            start = i * segment_length
            end = start + segment_length if i < self.segments_count - 1 else len(confused)
            segments.append(confused[start:end])
        
        return segments
    
    def _obfuscate_segment(self, segment: str, index: int) -> str:
        """对单个片段进行混淆"""
        # 使用片段索引和盐值创建混淆因子
        confusion_factor = hashlib.sha256((self.salt + str(index)).encode()).hexdigest()
        
        # 进行多轮混淆
        confused = segment
        for round_num in range(self.obfuscation_rounds):
            # 每轮使用不同的混淆方法
            if round_num % 3 == 0:
                # 使用简单的base64编码混淆
                confused = base64.b64encode(confused.encode()).decode()
            elif round_num % 3 == 1:
                # 位移混淆
                shift = int(confusion_factor[round_num * 2:round_num * 2 + 2], 16) % len(confused)
                confused = confused[shift:] + confused[:shift]
            else:
                # 简单字符位置交换
                confused_list = list(confused)
                if len(confused_list) > 2:
                    # 交换字符位置 - 使用一致的位置计算逻辑
                    swap_pos1 = int(confusion_factor[round_num * 2:round_num * 2 + 2], 16) % len(confused_list)
                    swap_pos2 = int(confusion_factor[round_num * 2 + 2:round_num * 2 + 4], 16) % len(confused_list)
                    confused_list[swap_pos1], confused_list[swap_pos2] = confused_list[swap_pos2], confused_list[swap_pos1]
                confused = ''.join(confused_list)
        
        return confused
    
    def _deobfuscate_segment(self, confused_segment: str, index: int) -> str:
        """反混淆单个片段"""
        confusion_factor = hashlib.sha256((self.salt + str(index)).encode()).hexdigest()
        
        deconfused = confused_segment
        # 反向进行混淆操作
        for round_num in range(self.obfuscation_rounds - 1, -1, -1):
            if round_num % 3 == 2:
                # 反向字符位置交换 - 使用相同的位置计算逻辑
                deconfused_list = list(deconfused)
                if len(deconfused_list) > 2:
                    # 使用与obfuscation相同的位置计算逻辑
                    swap_pos1 = int(confusion_factor[round_num * 2:round_num * 2 + 2], 16) % len(deconfused_list)
                    swap_pos2 = int(confusion_factor[round_num * 2 + 2:round_num * 2 + 4], 16) % len(deconfused_list)
                    # 再次交换来还原
                    deconfused_list[swap_pos1], deconfused_list[swap_pos2] = deconfused_list[swap_pos2], deconfused_list[swap_pos1]
                deconfused = ''.join(deconfused_list)
            elif round_num % 3 == 1:
                # 反向位移
                shift = int(confusion_factor[round_num * 2:round_num * 2 + 2], 16) % len(deconfused)
                deconfused = deconfused[-shift:] + deconfused[:-shift]
            else:
                # 反向base64编码混淆
                try:
                    deconfused = base64.b64decode(deconfused.encode()).decode()
                except Exception:
                    # 如果base64解码失败，保持原样
                    pass
        
        return deconfused
    
    def _combine_segments(self, segments: List[str]) -> str:
        """组合多个片段还原密钥"""
        # 反混淆每个片段
        deconfused_segments = []
        for i, segment in enumerate(segments):
            deconfused = self._deobfuscate_segment(segment, i)
            deconfused_segments.append(deconfused)
        
        # 组合片段
        combined = ''.join(deconfused_segments)
        
        # 移除前缀和后缀
        # 前缀和后缀都是16个字符（8字节的hex）
        if len(combined) > 32:  # 16前缀 + 16后缀
            actual_content = combined[16:-16]
        else:
            actual_content = combined
        
        # 解码
        try:
            decoded = base64.b64decode(actual_content.encode()).decode()
            return decoded
        except Exception:
            return combined
    
    def encrypt_and_store(self, key: str, storage_path: str) -> bool:
        """
        加密并存储密钥
        
        Args:
            key: 要保护的密钥
            storage_path: 存储路径（目录）
            
        Returns:
            bool: 是否成功
        """
        try:
            storage_dir = Path(storage_path)
            storage_dir.mkdir(parents=True, exist_ok=True)
            
            # 分割密钥
            segments = self._split_key(key)
            
            # 混淆每个片段并存储
            for i, segment in enumerate(segments):
                confused = self._obfuscate_segment(segment, i)
                
                # 使用不同的文件名存储每个片段
                filename = f"key_segment_{i:02d}.dat"
                filepath = storage_dir / filename
                
                # 添加额外的混淆层：将混淆数据伪装成其他文件类型
                disguised_data = self._create_disguise_file(confused)
                filepath.write_text(disguised_data)
            
            # 保存盐值到单独文件
            salt_file = storage_dir / "salt.dat"
            salt_data = self._create_disguise_file(self.salt)
            salt_file.write_text(salt_data)
            
            return True
            
        except Exception as e:
            print(f"❌ 密钥存储失败: {e}")
            return False
    
    def _create_disguise_file(self, content: str) -> str:
        """创建伪装文件内容"""
        # 将内容伪装成配置文件或日志文件
        templates = [
            f"# Configuration file\n# Generated at {secrets.token_hex(8)}\nkey_value={content}\n",
            f"# Log file\n# Timestamp: {secrets.token_hex(8)}\nDEBUG: Processing {content}\n",
            f"; INI file\n[settings]\nparam={content}\n",
            f"{{\"timestamp\": \"{secrets.token_hex(8)}\", \"data\": \"{content}\"}}\n",
        ]
        
        template = secrets.choice(templates)
        return template
    
    def _extract_from_disguise(self, file_content: str) -> str:
        """从伪装文件中提取真实内容"""
        # 尝试不同的提取模式
        patterns = [
            ("key_value=", "\n"),      # 配置文件格式
            ("DEBUG: Processing ", "\n"),  # 日志文件格式  
            ("param=", "\n"),          # INI文件格式
            ("\"data\": \"", "\""),    # JSON格式
        ]
        
        for pattern, end_marker in patterns:
            if pattern in file_content:
                start = file_content.find(pattern) + len(pattern)
                end = file_content.find(end_marker, start)
                if end == -1:
                    end = len(file_content)
                extracted = file_content[start:end].strip()
                return extracted
        
        # 如果没有找到模式，假设整个文件就是内容
        return file_content.strip()
    
    def load_and_decrypt(self, storage_path: str) -> Optional[str]:
        """
        加载并解密密钥
        
        Args:
            storage_path: 存储路径
            
        Returns:
            Optional[str]: 解密后的密钥，失败返回None
        """
        try:
            storage_dir = Path(storage_path)
            
            # 加载盐值
            salt_file = storage_dir / "salt.dat"
            if not salt_file.exists():
                return None
            
            salt_content = salt_file.read_text()
            self.salt = self._extract_from_disguise(salt_content)
            
            # 加载所有片段
            segments = []
            for i in range(self.segments_count):
                filename = f"key_segment_{i:02d}.dat"
                filepath = storage_dir / filename
                
                if not filepath.exists():
                    return None
                
                file_content = filepath.read_text()
                confused_segment = self._extract_from_disguise(file_content)
                segments.append(confused_segment)
            
            # 组合并解密
            key = self._combine_segments(segments)
            return key
            
        except Exception as e:
            print(f"❌ 密钥解密失败: {e}")
            return None
    
    def generate_secure_key(self, length: int = 32) -> str:
        """生成安全的随机密钥"""
        # 生成指定长度的随机字节并转换为base64
        random_bytes = secrets.token_bytes(length)
        return base64.b64encode(random_bytes).decode()[:length]
    
    def validate_integrity(self, storage_path: str) -> bool:
        """验证存储的密钥完整性"""
        try:
            storage_dir = Path(storage_path)
            
            # 检查必要文件是否存在
            salt_file = storage_dir / "salt.dat"
            if not salt_file.exists():
                return False
            
            for i in range(self.segments_count):
                filename = f"key_segment_{i:02d}.dat"
                filepath = storage_dir / filename
                if not filepath.exists():
                    return False
            
            return True
            
        except Exception:
            return False
    
    def cleanup(self, storage_path: str):
        """清理存储的密钥文件"""
        try:
            storage_dir = Path(storage_path)
            
            # 删除所有片段文件
            for i in range(self.segments_count):
                filename = f"key_segment_{i:02d}.dat"
                filepath = storage_dir / filename
                if filepath.exists():
                    filepath.unlink()
            
            # 删除盐值文件
            salt_file = storage_dir / "salt.dat"
            if salt_file.exists():
                salt_file.unlink()
            
            # 如果目录为空，删除目录
            try:
                if storage_dir.exists() and not any(storage_dir.iterdir()):
                    storage_dir.rmdir()
            except OSError:
                pass  # 目录可能不为空，忽略
                
        except Exception as e:
            print(f"⚠️ 清理时出现警告: {e}")


def create_c_extension_wrapper():
    """
    创建C扩展模块的包装器代码模板
    
    注意：这只是一个示例模板，实际C扩展需要单独编译
    """
    
    c_template = '''
/*
 * 安全密钥管理 C扩展模块
 * 用于增强密钥保护的安全性
 */

#include <Python.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/evp.h>
#include <openssl/rand.h>

static PyObject* secure_key_split(PyObject* self, PyObject* args) {
    const char* key;
    int segments;
    
    if (!PyArg_ParseTuple(args, "si", &key, &segments)) {
        return NULL;
    }
    
    // 这里实现C级别的密钥分割逻辑
    // 实际实现会更复杂，包括加密和混淆
    
    PyObject* segment_list = PyList_New(segments);
    // ... 分割逻辑
    
    return segment_list;
}

static PyObject* secure_key_combine(PyObject* self, PyObject* args) {
    PyObject* segment_list;
    
    if (!PyArg_ParseTuple(args, "O", &segment_list)) {
        return NULL;
    }
    
    // 这里实现C级别的密钥组合逻辑
    // 实际实现会更复杂，包括解密和验证
    
    return PyUnicode_FromString("combined_key");
}

static PyMethodDef SecureKeyMethods[] = {
    {"secure_key_split", secure_key_split, METH_VARARGS, "Securely split a key"},
    {"secure_key_combine", secure_key_combine, METH_VARARGS, "Securely combine key segments"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef securekeymodule = {
    PyModuleDef_HEAD_INIT,
    "securekey",
    "Secure key management module",
    -1,
    SecureKeyMethods
};

PyMODINIT_FUNC PyInit_securekey(void) {
    return PyModule_Create(&securekeymodule);
}
'''
    
    return c_template


# 使用示例
def demo_secure_key_management():
    """演示安全密钥管理的使用"""
    print("🔐 安全密钥管理演示")
    print("=" * 50)
    
    # 创建密钥管理器
    key_manager = SecureKeyManager()
    
    # 生成或使用现有密钥
    test_key = "sb_secret_very_secure_api_key_123456789"
    print(f"🔑 原始密钥: {test_key[:20]}...")
    
    # 存储路径
    storage_path = "./secure_storage"
    
    # 加密并存储
    print("📁 加密并存储密钥...")
    if key_manager.encrypt_and_store(test_key, storage_path):
        print("✅ 密钥存储成功")
        
        # 验证完整性
        if key_manager.validate_integrity(storage_path):
            print("✅ 密钥完整性验证通过")
        else:
            print("❌ 密钥完整性验证失败")
            return
        
        # 加载并解密
        print("🔓 加载并解密密钥...")
        recovered_key = key_manager.load_and_decrypt(storage_path)
        
        if recovered_key == test_key:
            print("✅ 密钥解密成功，验证通过")
            print(f"🔑 恢复密钥: {recovered_key[:20]}...")
        else:
            print("❌ 密钥解密失败")
    else:
        print("❌ 密钥存储失败")
    
    # 清理
    print("🧹 清理存储文件...")
    key_manager.cleanup(storage_path)
    print("✅ 清理完成")


if __name__ == "__main__":
    demo_secure_key_management()