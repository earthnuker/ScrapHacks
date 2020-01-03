#pragma once
using namespace std;
template <typename T> struct HashTableEntry;

struct Vector3 {
    float x;
    float y;
    float z;
};

struct Matrix3x3 {
    struct Vector3 a;
    struct Vector3 b;
    struct Vector3 c;
};

struct PyMethodDef {
    char *ml_name;
    void *ml_meth;
    int ml_flags;
    char *ml_doc;
};

struct PyMod {
    char *name;
    void *init_func;
};

struct Module {
    PyMod *mod;
    map<string, PyMethodDef *> methods;
};

struct Entity {
    void *vmt;
    const char *name;
};

struct EntityList {
    const char *name;
    void *unk_1;
    void *unk_2;
    const char *mod;
    const char *func;
};

struct GameVar {
    struct GameVar* next;
    const char* name;
    const char* desc;
    uint8_t type;
    uint8_t subtype;
    uint16_t unk;
    void* value;
    void* default;
};

struct PakEntry {
    unsigned char* filename;
    uint32_t locked;
    void* data;
    uint32_t seek;
};

struct HashIndexEntry {
    uint32_t offset;
    uint32_t size;
    uint32_t status;
    const char* name;
    struct HashIndexEntry* next;
};

struct HashIndex {
    uint32_t size;
    struct HashIndexEntry** data;
};


template <typename T> struct HashTable {
    uint32_t size;
    struct HashTableEntry<T> **chains;
};

template <typename T> struct HashTableEntry {
    T *data;
    const char *name;
    HashTableEntry *next;
};