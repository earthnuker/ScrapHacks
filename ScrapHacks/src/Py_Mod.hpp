#pragma once
#include "Scrapland.hpp"

using namespace std;

static void *py_asm(void *self, void *args)
{
    void* ret;
    void *addr = nullptr;
    char *asm_code;
    if (!PyArg_ParseTuple(args, "s|i", &asm_code, &addr))
    {
        return nullptr;
    }
    string code(asm_code);
    size_t data_size=asm_size(split(code,';'));
    if (addr==nullptr) {
        addr = malloc(data_size);
        if (addr==nullptr) {
            scrap_log(ERR_COLOR, "ERROR: ");
            scrap_log(ERR_COLOR, "malloc() failed");
            scrap_log(ERR_COLOR, "\n");
            return Py_BuildValue("s",nullptr);
        }
        char ptr[255];
        snprintf(ptr,255,"Buffer @ %p\n",(void*)addr);
        scrap_log(INFO_COLOR,ptr);
        ret=Py_BuildValue("(l,l)", data_size, addr);
    } else {
        ret=Py_BuildValue("(l,l)", data_size, addr);
    }
    assemble(split(code,';'),reinterpret_cast<uint64_t>(addr));
    return ret;
}

static void *py_dasm(void *self, void *args) {
    // TODO: return list of (addr,asm)
    return nullptr;
}

static void *py_read_mem(void *self, void *args)
{
    //TODO: implement reading memory and return data as hex string
    void* ret = nullptr;
    void *addr = nullptr;
    size_t size = 256;
    char *data;
    if (!PyArg_ParseTuple(args, "ii", &addr, &size))
    {
        return nullptr;
    }
    char* buffer=new char[size*2];
    for (size_t i=0;i<size;++i) {
        
    }
    return ret;
}

static void *py_write_mem(void *self, void *args) {
    //TODO: implement (return None or error string)
    return nullptr;
}

static PyMethodDef SH_Methods[] = {
    // {"asm", py_asm, 1},
    // {"read", py_read_mem, 1},
    // {"write", py_write_mem, 1},
    {NULL, NULL}
};

void InitPyMod()
{
    Py_InitModule("_ScrapHack", SH_Methods, nullptr, nullptr, 1007);
}
