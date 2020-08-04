#include <Windows.h>

#define DLL_EXPORT extern "C" __declspec(dllexport)

using namespace std;

void DllInit(HMODULE);
void DllUnload();
void DllPreInit();

HANDLE hThread = INVALID_HANDLE_VALUE;
bool loaded = false;
HMODULE mod = nullptr;

DLL_EXPORT void init_ScrapHack() {
    DllPreInit();
    if (!loaded) {
        Sleep(1000);
        hThread = CreateThread(NULL, NULL, (LPTHREAD_START_ROUTINE)DllInit, mod,
                               0, 0);
        CloseHandle(hThread);
        loaded = true;
    }
}

BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call,
                      LPVOID lpReserved) {
    mod = hModule;
    return true;
}