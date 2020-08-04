#pragma once
#include <Windows.h>

#include <functional>
#include <iostream>
#include <map>
#include <vector>
#include <asmjit/asmjit.h>

using namespace std;


vector<uint8_t> make_trampoline(uintptr_t orig,uintptr_t hook) {
    using namespace asmjit;
    vector<uint8_t> ret;
    JitRuntime rt;
    CodeHolder code;
    CodeInfo ci=rt.codeInfo();
    code.init(ci);
    x86::Assembler a(&code);
    a.jmp(hook);
    a.ret();
    code.flatten();
    code.resolveUnresolvedLinks();
    code.relocateToBase(orig);
    size_t code_size=code.sectionById(0)->buffer().size();
    uint8_t* buffer=new uint8_t[code_size];
    code.copyFlattenedData((void*)buffer, code_size, CodeHolder::kCopyWithPadding);
    for (size_t i=0;i<code_size;++i) {
        ret.push_back(buffer[i]);
    }
    delete buffer;
    return ret;
}


class Hook {
  private:
    MEMORY_BASIC_INFORMATION mbi;
    void *orig;
    void *detour;
    bool enabled;
    uint8_t *orig_bytes;
    uint8_t *jmp_bytes;
    size_t size;
    static map<uintptr_t, shared_ptr<Hook>> hooks;

  public:
    Hook(void *func, void *detour) {
        uintptr_t dest = reinterpret_cast<uintptr_t>(detour);
        uintptr_t src = reinterpret_cast<uintptr_t>(func);
        this->orig = func;
        this->detour = detour;
        vector<uint8_t> code = make_trampoline(src,dest);
        this->orig_bytes = new uint8_t[code.size()];
        this->jmp_bytes = new uint8_t[code.size()];
        this->size = code.size();
        this->enabled = false;
        uint8_t* func_b = reinterpret_cast<uint8_t*>(this->orig);
        for (size_t i=0;i<this->size;++i) {
            this->orig_bytes[i]=func_b[i];
            this->jmp_bytes[i]=code[i];
        }
        VirtualQuery(this->orig, &mbi, sizeof(mbi));
        VirtualProtect(mbi.BaseAddress, mbi.RegionSize, PAGE_EXECUTE_READWRITE,
                       &mbi.Protect);
        VirtualProtect(mbi.BaseAddress, mbi.RegionSize, mbi.Protect, NULL);
        cout<<"Constructed hook from "<<func<<" to "<<detour<<", size: " << this->size<<endl;
    }

    ~Hook() {
        cout << "Unhooking: [" << this->orig << " <- " << this->detour << "]"
             << endl;
        this->disable();
    }


    static void addr(uintptr_t _addr, void *detour) {
        Hook::addr(reinterpret_cast<void*>(_addr),detour);
    }

    static void addr(void *addr, void *detour) {
        cout << "Hooking: [" << addr << " -> " << detour << "]" << endl;
        uintptr_t key = reinterpret_cast<uintptr_t>(detour);
        hooks[key] = make_shared<Hook>(addr, detour);
        hooks[key]->enable();
    }

    static void module(const char *mod, const char *func, void *detour) {
        cout << "Hooking: [" << mod << "]." << func << " -> " << detour << endl;
        void *addr = GetProcAddress(GetModuleHandle(mod), func);
        if (addr != NULL) {
            Hook::addr(addr, detour);
        } else {
            cerr << "[" << mod << "]." << func << " not found!" << endl;
        };
    }

    static shared_ptr<Hook> get(void *func) {
        uintptr_t addr = reinterpret_cast<uintptr_t>(func);
        return Hook::get(addr);
    }

    static shared_ptr<Hook> get(uintptr_t addr) { return hooks.at(addr); }

    static size_t drop(void *func) {
        uintptr_t addr = reinterpret_cast<uintptr_t>(func);
        return Hook::drop(addr);
    }

    static size_t drop(uintptr_t addr) { return hooks.erase(addr); }

    static void clear() {
        cout << "Clearing Hooks" << endl;
        for (pair<uintptr_t, shared_ptr<Hook>> h : hooks) {
            h.second->disable();
        }
        return hooks.clear();
    }

    void disable() {
        if (this->enabled) {
            cout << "Disabling: [" << this->orig << " <- " << this->detour <<
            "]"
            << endl;
            VirtualProtect(mbi.BaseAddress, mbi.RegionSize,
                           PAGE_EXECUTE_READWRITE, NULL);
            memcpy(this->orig, this->orig_bytes, this->size);
            VirtualProtect(mbi.BaseAddress, mbi.RegionSize, mbi.Protect, NULL);
            this->enabled = false;
        }
    }
    void enable() {
        if (!this->enabled) {
            cout << "Enabling: [" << this->orig << " -> " << this->detour <<
            "]" << endl;
            VirtualProtect(mbi.BaseAddress, mbi.RegionSize,
                           PAGE_EXECUTE_READWRITE, NULL);
            memcpy(this->orig, this->jmp_bytes, this->size);
            VirtualProtect(mbi.BaseAddress, mbi.RegionSize, mbi.Protect, NULL);
            this->enabled = true;
        }
    }

    template <typename F, typename... Args> void func_void(Args... args) {
        this->disable();
        reinterpret_cast<F>(this->orig)(args...);
        this->enable();
        return;
    }

    template <typename F, typename... Args> auto func(Args... args) {
        this->disable();
        auto ret = reinterpret_cast<F>(this->orig)(args...);
        this->enable();
        return ret;
    }
};

map<uintptr_t, shared_ptr<Hook>> Hook::hooks;
