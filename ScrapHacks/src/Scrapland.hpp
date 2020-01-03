#pragma once
#include "Structures.hpp"

#include <sstream>
using namespace std;

// OFFSETS
#define O_MONEY 0x2090
#define O_ALARM 0x1C6C
#define O_ALARM_GROW 0x1C68
#define O_ENTS 0x4
#define O_ENTLISTS 0x2b8

// POINTERS
#define P_WORLD 0x7FE944
#define P_VARS 0x7FBE4C
#define P_PY_MODS 0x79C698

// FUNCTION ADDRESSES
#define P_CON_HANDLER 0x402190
#define P_SCRAP_LOG 0x4134C0
#define P_SCRAP_EXEC 0x5a8390
#define P_SCRAP_EXIT 0x4010c0
#define P_D3DCHECK 0x602a70
#define P_D3DDEV 0x852914
#define P_Py_InitModule 0x5A8FB0
#define P_PyArg_ParseTuple 0x5bb9d0


#define MSG_COLOR scrap_RGB(128,0,255)
#define WARN_COLOR scrap_RGB(255,128,0)
#define ERR_COLOR scrap_RGB(255,0,0)
#define INFO_COLOR scrap_RGB(0,0,255)


uint32_t scrap_RGB(uint8_t r,uint8_t g,uint8_t b) {
    return r|g<<8|b<<16;
}

// FUNCTION TYPES
typedef int(_cdecl *t_scrap_log)(unsigned int color, const char *message);
typedef int(_cdecl *t_scrap_exec)(const char *code);
typedef int(_cdecl *t_PyArg_ParseTuple)(void *PyObj, char *format, ...);
typedef int(_cdecl *t_Py_InitModule)(const char *name, void *methods,
                                     const char *doc, void *passthrough,
                                     int module_api_version);

// GLOBAL FUNCTIONS
auto scrap_exec = (t_scrap_exec)P_SCRAP_EXEC;
auto pyarg_parsetuple = (t_PyArg_ParseTuple)P_PyArg_ParseTuple;
auto py_initmodule = (t_Py_InitModule)P_Py_InitModule;

int scrap_log(unsigned int color,const char* msg) {
    return ((t_scrap_log)P_SCRAP_LOG)(color,msg);
}

int scrap_log(uint8_t r,uint8_t g,uint8_t b,const char* msg) {
    return ((t_scrap_log)P_SCRAP_LOG)(scrap_RGB(r,g,b),msg);
}


int scrap_log(unsigned int color,string msg) {
    return ((t_scrap_log)P_SCRAP_LOG)(color,msg.c_str());
}

int scrap_log(uint8_t r,uint8_t g,uint8_t b,string msg) {
    return ((t_scrap_log)P_SCRAP_LOG)(scrap_RGB(r,g,b),msg.c_str());
}


size_t size_ht(HashTable<EntityList> *ht) {
    size_t cnt = 0;
    for (size_t i = 0; i < ht->size; ++i) {
        HashTableEntry<EntityList> *ent = ht->chains[i];
        if (ent) {
            while (ent) {
                ++cnt;
                ent = ent->next;
            }
        }
    }
    return cnt;
}

size_t size_ht(HashTable<Entity> *ht) {
    size_t cnt = 0;
    for (size_t i = 0; i < ht->size; ++i) {
        HashTableEntry<Entity> *ent = ht->chains[i];
        if (ent) {
            while (ent) {
                ++cnt;
                ent = ent->next;
            }
        }
    }
    return cnt;
}

size_t dump_ht(HashTable<EntityList> *ht) {
    size_t cnt = 0;
    for (size_t i = 0; i < ht->size; ++i) {
        HashTableEntry<EntityList> *ent = ht->chains[i];
        if (ent) {
            cout << i << ": ";
            while (ent) {
                ++cnt;
                cout << "[ " << ent->name << ": " << ent->data << "]";
                if (ent->next) {
                    cout << " -> ";
                };
                ent = ent->next;
            }
            cout << endl;
        }
    }
    cout << cnt << " Entries" << endl;
    return cnt;
}


size_t dump_ht(HashTable<Entity> *ht) {
    size_t cnt = 0;
    for (size_t i = 0; i < ht->size; ++i) {
        HashTableEntry<Entity> *ent = ht->chains[i];
        if (ent) {
            cout << i << ": ";
            while (ent) {
                ++cnt;
                cout << "[ " << ent->name << ": " << ent->data << "]";
                if (ent->next) {
                    cout << " -> ";
                };
                ent = ent->next;
            }
            cout << endl;
        }
    }
    cout << cnt << " Entries" << endl;
    return cnt;
}

size_t dump_ht(HashTable<EntityList> *ht,stringstream *out) {
    size_t cnt = 0;
    for (size_t i = 0; i < ht->size; ++i) {
        HashTableEntry<EntityList> *ent = ht->chains[i];
        if (ent) {
            *out << i << ": ";
            while (ent) {
                ++cnt;
                *out << "[ " << ent->name << ": " << ent->data << "]";
                if (ent->next) {
                    *out << " -> ";
                };
                ent = ent->next;
            }
            *out << endl;
        }
    }
    *out << cnt << " Entries" << endl;
    return cnt;
}

size_t dump_ht(HashTable<Entity> *ht,stringstream *out) {
    size_t cnt = 0;
    for (size_t i = 0; i < ht->size; ++i) {
        HashTableEntry<Entity> *ent = ht->chains[i];
        if (ent) {
            *out << i << ": ";
            while (ent) {
                ++cnt;
                *out << "[ " << ent->name << ": " << ent->data << "]";
                if (ent->next) {
                    *out << " -> ";
                };
                ent = ent->next;
            }
            *out << endl;
        }
    }
    *out << cnt << " Entries" << endl;
    return cnt;
}