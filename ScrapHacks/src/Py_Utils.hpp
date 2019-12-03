#pragma once
#include <iostream>
#include <map>
#include <string>

#include "Structures.hpp"

using namespace std;

map<string, Module> Py;

PyMethodDef *find_method_table(uintptr_t base, uintptr_t needle) {
    for (ptrdiff_t offset = 0; offset < 64; ++offset) {
        uintptr_t instr = reinterpret_cast<uintptr_t *>(base + offset)[0];
        if (instr == needle) {
            uintptr_t mod_addr =
                reinterpret_cast<uintptr_t *>(base + offset - (1 + 4))[0];
            return reinterpret_cast<PyMethodDef *>(mod_addr);
        }
    }
    return reinterpret_cast<PyMethodDef *>(0);
}

map<string, Module> get_modules(uintptr_t base) {
    map<string, Module> Py;
    PyMod *modules = reinterpret_cast<PyMod *>(base);
    for (size_t i = 0; modules[i].init_func != NULL; i++) {
        Module mod;
        mod.mod = &modules[i];
        PyMethodDef *method_table =
            find_method_table((size_t)modules[i].init_func,
                              reinterpret_cast<uintptr_t>(modules[i].name));
        for (size_t j = 0;
             method_table != NULL && method_table[j].ml_name != NULL; j++) {
            mod.methods[method_table[j].ml_name] = &method_table[j];
        }
        Py[mod.mod->name] = mod;
    }
    return Py;
}

void *get_py(const char *mod, const char *meth) {
    try {
        return Py.at(mod).methods.at(meth)->ml_meth;
    } catch (out_of_range) {
        return NULL;
    }
}

void inject(const char *mod, const char *meth, void *detour) {
    try {
        void *orig = get_py(mod, meth);
        Py.at(mod).methods.at(meth)->ml_meth = detour;
        cout << mod << "." << meth << ": " << orig << " -> " << detour << endl;
    } catch (out_of_range) {
        cout << mod << "." << meth << " not found!" << endl;
    }
}