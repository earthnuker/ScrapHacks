#pragma once
#include <TlHelp32.h>
#include <Windows.h>

#include <algorithm>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

#include "Structures.hpp"
#include "Py_Utils.hpp"

using namespace std;

#define DLL_EXPORT extern "C" __declspec(dllexport)

template <typename T> void **GetVTable(T *obj) {
    void *addr = reinterpret_cast<void **>(obj)[0];
    return (void **)(*(void **)addr);
}

string GetLastErrorAsString() {
    DWORD errorMessageID = GetLastError();
    if (errorMessageID == 0)
        return "No error";
    LPSTR messageBuffer = NULL;
    size_t m_size = FormatMessageA(
        FORMAT_MESSAGE_ALLOCATE_BUFFER | FORMAT_MESSAGE_FROM_SYSTEM |
            FORMAT_MESSAGE_IGNORE_INSERTS,
        NULL, errorMessageID, MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT),
        (LPSTR)&messageBuffer, 0, NULL);
    string message(messageBuffer, m_size);
    LocalFree(messageBuffer);
    if (!message.empty() && message[message.length() - 1] == '\n') {
        message.erase(message.length() - 1);
    }
    return message;
}

void SetupStreams() {
    FILE *fIn;
    FILE *fOut;
    freopen_s(&fIn, "conin$", "r", stdin);
    freopen_s(&fOut, "conout$", "w", stdout);
    freopen_s(&fOut, "conout$", "w", stderr);
    ios::sync_with_stdio();
    std::wcout.clear();
    std::cout.clear();
    std::wcerr.clear();
    std::cerr.clear();
    std::wcin.clear();
    std::cin.clear();
}

void SetupConsole() {
    if (!AttachConsole(-1)) {
        if (!AllocConsole()) {
            FreeConsole();
            AllocConsole();
        }
        AttachConsole(GetCurrentProcessId());
    }
    SetupStreams();
}

void SetupConsole(const char *title) {
    SetupConsole();
    SetConsoleTitleA(title);
}

void FreeConsole(bool wait) {
    if (wait) {
        cout << "[?] Press Enter to Exit";
        cin.ignore();
    }
    FreeConsole();
}

bool in_foreground = false;
BOOL CALLBACK EnumWindowsProcMy(HWND hwnd, LPARAM lParam) {
    DWORD lpdwProcessId;
    GetWindowThreadProcessId(hwnd, &lpdwProcessId);
    if (lpdwProcessId == lParam) {
        in_foreground =
            (hwnd == GetForegroundWindow()) || (hwnd == GetActiveWindow());
        return FALSE;
    }
    return TRUE;
}

bool key_down(int keycode, int delay = 100) {
    in_foreground = false;
    EnumWindows(EnumWindowsProcMy, GetCurrentProcessId());
    if (in_foreground) {
        if (GetAsyncKeyState(keycode)) {
            Sleep(delay);
            return true;
        }
    }
    return false;
}

bool key_down_norepeat(int keycode, int delay = 100) {
    in_foreground = false;
    EnumWindows(EnumWindowsProcMy, GetCurrentProcessId());
    if (in_foreground) {
        if (GetAsyncKeyState(keycode)) {
            while (GetAsyncKeyState(keycode)) {
                Sleep(delay);
            }
            return true;
        }
    }
    return false;
}

string hexdump_s(void *addr, size_t count=0xff) {
    ostringstream out;
    uintptr_t offset=reinterpret_cast<uintptr_t>(addr);
    for (size_t i = 0; i < count; ++i) {
        unsigned int val = (unsigned int)(((unsigned char *)(offset+i))[0]);
        if ((i % 16) == 0) {
            out << endl;
            out << setfill('0') << setw(8) << std::hex << std::uppercase << (offset+i) << ": ";
        }
        out << setfill('0') << setw(2) << std::hex << val << " ";
    }
    out << endl;
    return out.str();
}

void hexdump(void *addr, size_t count=0xff) {
    uintptr_t offset=reinterpret_cast<uintptr_t>(addr);
    for (size_t i = 0; i < count; ++i) {
        unsigned int val = (unsigned int)(((unsigned char *)(offset+i))[0]);
        if ((i % 16) == 0) {
            cout << endl;
            cout << setfill('0') << setw(8) << std::hex << std::uppercase << (offset+i) << ": ";
        }
        cout << setfill('0') << setw(2) << std::hex << val << " ";
    }
    cout << endl;
    return;
}

template <typename T> T *__ptr(uintptr_t addr) {
    return reinterpret_cast<T *>(addr);
}

template <typename T> T *__ptr(uintptr_t addr, ptrdiff_t offset) {
    // cout << "[" << (void*)addr << "] + " << (void*)offset << " = ";
    addr = reinterpret_cast<uintptr_t *>(addr)[0] + offset;
    // cout << (void*)addr << endl;;
    auto ret = __ptr<T>(addr);
    return ret;
}

template <typename T, typename... Offsets>
T *__ptr(uintptr_t addr, ptrdiff_t offset, Offsets... offsets) {
    // cout << "[" << (void*)addr << "] + " << (void*)offset << " = ";
    addr = reinterpret_cast<uintptr_t *>(addr)[0] + offset;
    // cout << (void*)addr << endl;;
    auto ret = __ptr<T>(addr, offsets...);
    return ret;
}

template <typename T, typename... Offsets>
T *ptr(uintptr_t addr, Offsets... offsets) {
    auto ret = __ptr<T>(addr, offsets...);
    return ret;
}


template <typename T>
void __to_str(ostream& o, T t)
{
    o << t;
}

template<typename T, typename... Args>
void __to_str(ostream& o, T t, Args... args) // recursive variadic function
{
    __to_str(o, t);
    __to_str(o, args...);
}

template<typename... Args>
const char* to_str(Args... args)
{
    ostringstream oss;
    __to_str(oss, args...);
    return oss.str().c_str();
}

DWORD
PPID() {
    DWORD PID = GetCurrentProcessId();
    HANDLE hSnapShot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    PROCESSENTRY32 procentry;
    if (hSnapShot == INVALID_HANDLE_VALUE) {
        cout << GetLastErrorAsString() << endl;
        return -1;
    }
    if (Process32First(hSnapShot, &procentry)) {
        do {
            if (procentry.th32ProcessID == PID) {
                CloseHandle(hSnapShot);
                return procentry.th32ParentProcessID;
            }
            procentry.dwSize = sizeof(PROCESSENTRY32);
        } while (Process32Next(hSnapShot, &procentry));
    }
    CloseHandle(hSnapShot);
    return -1;
}

vector<uint8_t> fromhex(string input) {
    vector<uint8_t> ret = {};
    if (input.size() % 2) {
        return ret;
    }
    transform(input.begin(), input.end(), input.begin(), ::toupper);
    string hc = "0123456789ABCDEF";
    int v = 0;
    size_t n = 0;
    size_t idx;
    for (unsigned char c : input) {
        idx = hc.find(c);
        if (idx != size_t(-1)) {
            if ((n++) % 2 == 0) {
                v = hc.find(c) << 4;
            } else {
                v |= hc.find(c);
                ret.push_back(v);
            }
        } else {
            cout << "Invalid Character in hex string" << endl;
            ret.clear();
            return ret;
        }
    }
    return ret;
}

vector<string> split(string str, char sep) {
    vector<string> ret;
    string part;
    for (auto n : str) {
        if (n == sep) {
            ret.push_back(part);
            part.clear();
        } else {
            part = part + n;
        }
    }
    if (part != "")
        ret.push_back(part);
    return ret;
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