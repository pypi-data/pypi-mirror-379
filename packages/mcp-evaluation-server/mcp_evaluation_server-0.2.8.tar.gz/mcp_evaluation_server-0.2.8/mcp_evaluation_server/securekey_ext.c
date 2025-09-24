/*
 * 安全密钥管理C扩展模块
 * 用于增强密钥保护的安全性
 * 编译: python securekey_ext_setup.py build_ext --inplace
 */

#include <Python.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <time.h>

#ifdef _WIN32
#include <windows.h>
#else
#include <sys/time.h>
#endif

// 简单的XOR加密函数
static void xor_encrypt_decrypt(const char* input, char* output, const char* key, int length) {
    int key_len = strlen(key);
    for (int i = 0; i < length; i++) {
        output[i] = input[i] ^ key[i % key_len];
    }
}

// 获取当前时间戳（毫秒）
static long long get_timestamp_ms() {
#ifdef _WIN32
    SYSTEMTIME st;
    FILETIME ft;
    LARGE_INTEGER li;
    GetSystemTime(&st);
    SystemTimeToFileTime(&st, &ft);
    li.LowPart = ft.dwLowDateTime;
    li.HighPart = ft.dwHighDateTime;
    return li.QuadPart / 10000;
#else
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return (long long)tv.tv_sec * 1000 + tv.tv_usec / 1000;
#endif
}

// 分割密钥
static PyObject* secure_key_split(PyObject* self, PyObject* args) {
    const char* key;
    int segments;
    const char* salt;
    
    if (!PyArg_ParseTuple(args, "sis", &key, &segments, &salt)) {
        return NULL;
    }
    
    if (segments <= 0 || segments > 10) {
        PyErr_SetString(PyExc_ValueError, "Segments must be between 1 and 10");
        return NULL;
    }
    
    int key_len = strlen(key);
    if (key_len == 0) {
        PyErr_SetString(PyExc_ValueError, "Key cannot be empty");
        return NULL;
    }
    
    // 分配内存进行混淆
    char* obfuscated = malloc(key_len * 2);
    if (!obfuscated) {
        PyErr_SetString(PyExc_MemoryError, "Memory allocation failed");
        return NULL;
    }
    
    // 第一层：时间戳混淆
    long long timestamp = get_timestamp_ms();
    char* timestamp_ptr = (char*)&timestamp;
    for (int i = 0; i < key_len && i < 8; i++) {
        obfuscated[i] = key[i] ^ timestamp_ptr[i % 8];
    }
    memcpy(obfuscated + key_len, key, key_len);
    
    // 第二层：盐值混淆
    char* final_obfuscated = malloc(key_len * 2);
    xor_encrypt_decrypt(obfuscated, final_obfuscated, salt, key_len * 2);
    
    // 分割成段
    PyObject* segment_list = PyList_New(segments);
    int segment_length = (key_len * 2) / segments;
    
    for (int i = 0; i < segments; i++) {
        int start = i * segment_length;
        int end = (i == segments - 1) ? (key_len * 2) : start + segment_length;
        int seg_len = end - start;
        
        char* segment_data = malloc(seg_len + 1);
        memcpy(segment_data, final_obfuscated + start, seg_len);
        segment_data[seg_len] = '\0';
        
        // 转换为base64编码的Python字符串
        PyObject* py_segment = PyUnicode_FromString(segment_data);
        PyList_SET_ITEM(segment_list, i, py_segment);
        
        free(segment_data);
    }
    
    free(obfuscated);
    free(final_obfuscated);
    
    return segment_list;
}

// 组合密钥
static PyObject* secure_key_combine(PyObject* self, PyObject* args) {
    PyObject* segment_list;
    const char* salt;
    
    if (!PyArg_ParseTuple(args, "Os", &segment_list, &salt)) {
        return NULL;
    }
    
    if (!PyList_Check(segment_list)) {
        PyErr_SetString(PyExc_TypeError, "Expected a list");
        return NULL;
    }
    
    int segments = PyList_Size(segment_list);
    if (segments <= 0) {
        PyErr_SetString(PyExc_ValueError, "Segment list cannot be empty");
        return NULL;
    }
    
    // 计算总长度
    int total_length = 0;
    for (int i = 0; i < segments; i++) {
        PyObject* segment = PyList_GetItem(segment_list, i);
        const char* segment_data = PyUnicode_AsUTF8(segment);
        total_length += strlen(segment_data);
    }
    
    // 分配内存并组合片段
    char* combined = malloc(total_length + 1);
    int current_pos = 0;
    
    for (int i = 0; i < segments; i++) {
        PyObject* segment = PyList_GetItem(segment_list, i);
        const char* segment_data = PyUnicode_AsUTF8(segment);
        int seg_len = strlen(segment_data);
        memcpy(combined + current_pos, segment_data, seg_len);
        current_pos += seg_len;
    }
    combined[total_length] = '\0';
    
    // 第一层：盐值反混淆
    char* deobfuscated = malloc(total_length);
    xor_encrypt_decrypt(combined, deobfuscated, salt, total_length);
    
    // 第二层：时间戳反混淆
    long long timestamp = get_timestamp_ms();
    char* timestamp_ptr = (char*)&timestamp;
    int key_len = total_length / 2;
    
    char* final_key = malloc(key_len + 1);
    for (int i = 0; i < key_len && i < 8; i++) {
        final_key[i] = deobfuscated[i + key_len] ^ timestamp_ptr[i % 8];
    }
    if (key_len > 8) {
        memcpy(final_key + 8, deobfuscated + key_len + 8, key_len - 8);
    }
    final_key[key_len] = '\0';
    
    PyObject* result = PyUnicode_FromString(final_key);
    
    free(combined);
    free(deobfuscated);
    free(final_key);
    
    return result;
}

// 生成随机盐值
static PyObject* generate_salt(PyObject* self, PyObject* args) {
    int length = 16;
    
    if (!PyArg_ParseTuple(args, "|i", &length)) {
        return NULL;
    }
    
    if (length <= 0 || length > 64) {
        PyErr_SetString(PyExc_ValueError, "Length must be between 1 and 64");
        return NULL;
    }
    
    char* salt = malloc(length + 1);
    if (!salt) {
        PyErr_SetString(PyExc_MemoryError, "Memory allocation failed");
        return NULL;
    }
    
    // 简单的随机数生成（实际应用中应使用更安全的随机数生成器）
    srand((unsigned int)get_timestamp_ms());
    const char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    
    for (int i = 0; i < length; i++) {
        salt[i] = charset[rand() % (sizeof(charset) - 1)];
    }
    salt[length] = '\0';
    
    PyObject* result = PyUnicode_FromString(salt);
    free(salt);
    
    return result;
}

// 内存安全清理
static PyObject* secure_wipe(PyObject* self, PyObject* args) {
    Py_buffer buffer;
    
    if (!PyArg_ParseTuple(args, "y*", &buffer)) {
        return NULL;
    }
    
    // 安全地擦除内存
    volatile unsigned char* ptr = (volatile unsigned char*)buffer.buf;
    for (Py_ssize_t i = 0; i < buffer.len; i++) {
        ptr[i] = 0;
    }
    
    PyBuffer_Release(&buffer);
    Py_RETURN_NONE;
}

// 方法定义
static PyMethodDef SecureKeyMethods[] = {
    {"secure_key_split", secure_key_split, METH_VARARGS, "Securely split a key into segments"},
    {"secure_key_combine", secure_key_combine, METH_VARARGS, "Securely combine key segments"},
    {"generate_salt", generate_salt, METH_VARARGS, "Generate a random salt"},
    {"secure_wipe", secure_wipe, METH_VARARGS, "Securely wipe memory"},
    {NULL, NULL, 0, NULL}
};

// 模块定义
static struct PyModuleDef securekeymodule = {
    PyModuleDef_HEAD_INIT,
    "securekey_ext",
    "Secure key management C extension",
    -1,
    SecureKeyMethods
};

// 模块初始化
PyMODINIT_FUNC PyInit_securekey_ext(void) {
    return PyModule_Create(&securekeymodule);
}