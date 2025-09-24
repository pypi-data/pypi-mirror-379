/*
 * 简化的安全密钥管理C扩展模块
 * 仅使用XOR加密和盐值混淆
 */

#include <Python.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

// 简单的XOR加密函数
static void xor_encrypt_decrypt(const char* input, char* output, const char* key, int length) {
    int key_len = strlen(key);
    for (int i = 0; i < length; i++) {
        output[i] = input[i] ^ key[i % key_len];
    }
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
    
    // 分配内存进行加密
    char* encrypted = malloc(key_len + 1);
    if (!encrypted) {
        PyErr_SetString(PyExc_MemoryError, "Memory allocation failed");
        return NULL;
    }
    
    // 使用盐值进行XOR加密
    xor_encrypt_decrypt(key, encrypted, salt, key_len);
    encrypted[key_len] = '\0';
    
    // 分割成段
    PyObject* segment_list = PyList_New(segments);
    int segment_length = key_len / segments;
    
    for (int i = 0; i < segments; i++) {
        int start = i * segment_length;
        int end = (i == segments - 1) ? key_len : start + segment_length;
        int seg_len = end - start;
        
        // 转换为Python bytes对象，然后解码为字符串
        PyObject* py_bytes = PyBytes_FromStringAndSize(encrypted + start, seg_len);
        PyObject* py_segment = PyUnicode_FromEncodedObject(py_bytes, "latin-1", "strict");
        Py_DECREF(py_bytes);
        PyList_SET_ITEM(segment_list, i, py_segment);
    }
    
    free(encrypted);
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
        Py_ssize_t seg_len;
        PyUnicode_AsUTF8AndSize(segment, &seg_len);
        total_length += seg_len;
    }
    
    // 分配内存并组合片段
    char* combined = malloc(total_length + 1);
    int current_pos = 0;
    
    for (int i = 0; i < segments; i++) {
        PyObject* segment = PyList_GetItem(segment_list, i);
        Py_ssize_t seg_len;
        const char* segment_data = PyUnicode_AsUTF8AndSize(segment, &seg_len);
        memcpy(combined + current_pos, segment_data, seg_len);
        current_pos += seg_len;
    }
    combined[total_length] = '\0';
    
    // 使用盐值进行XOR解密
    char* decrypted = malloc(total_length + 1);
    xor_encrypt_decrypt(combined, decrypted, salt, total_length);
    decrypted[total_length] = '\0';
    
    PyObject* result = PyUnicode_FromString(decrypted);
    
    free(combined);
    free(decrypted);
    
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
    
    // 简单的随机数生成
    srand((unsigned int)time(NULL));
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