#include <iostream>
#include <windows.h>
#include <TlHelp32.h>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string.h>
#define DLL_NAME "ScrapHack.dll"
using namespace std;

string GetLastErrorAsString()
{
    DWORD errorMessageID = GetLastError();
    if (errorMessageID == 0)
        return "No error";
    LPSTR messageBuffer = NULL;
    size_t m_size = FormatMessageA(FORMAT_MESSAGE_ALLOCATE_BUFFER | FORMAT_MESSAGE_FROM_SYSTEM | FORMAT_MESSAGE_IGNORE_INSERTS,
                                   NULL, errorMessageID, MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT), (LPSTR)&messageBuffer, 0, NULL);
    string message(messageBuffer, m_size);
    LocalFree(messageBuffer);
    if (!message.empty() && message[message.length() - 1] == '\n')
    {
        message.erase(message.length() - 1);
    }
    return message;
}

void fail(char *msg)
{
    cerr << "[!] " << msg << ": " << GetLastErrorAsString() << endl;
    exit(1);
}

bool fexists(const char *filename)
{
    ifstream ifile(filename);
    bool ret = ifile.good();
    ifile.close();
    return ret;
}

bool HasModule(int PID, const char *modname)
{
    HANDLE hModuleSnap = CreateToolhelp32Snapshot(TH32CS_SNAPMODULE | TH32CS_SNAPMODULE32, PID);
    MODULEENTRY32 me;
    me.dwSize = sizeof(MODULEENTRY32);
    if (hModuleSnap == INVALID_HANDLE_VALUE)
    {
        return false;
    }
    if (!Module32First(hModuleSnap, &me))
    {
        CloseHandle(hModuleSnap);
        cout << "Error reading Module Snapshot" << endl;
    }
    else
    {
        do
        {
            if (strstr((const char *)me.szModule, modname) != NULL)
                return true;
        } while (Module32Next(hModuleSnap, &me));
        CloseHandle(hModuleSnap);
    }
    return false;
}


bool adjustPrivs(HANDLE hProc)
{
    HANDLE hToken;
    LUID luid;
    TOKEN_PRIVILEGES tkprivs;
    if (!OpenProcessToken(hProc, (TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY), &hToken))
    {
        fail("Could not open process token:");
    }
    if (!LookupPrivilegeValue(0, SE_DEBUG_NAME, &luid))
    {
        CloseHandle(hToken);
        fail("Error looking up privilege value for SE_DEBUG_NAME");
    }
    tkprivs.PrivilegeCount = 1;
    tkprivs.Privileges[0].Luid = luid;
    tkprivs.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED;
    bool bRet = AdjustTokenPrivileges(hToken, 0, &tkprivs, sizeof(tkprivs), NULL, NULL);
    CloseHandle(hToken);
    if (!bRet)
    {
        fail("Could not adjust privileges");
    }
    return bRet;
}

bool Injected(DWORD PID)
{
    return HasModule(PID, DLL_NAME);
}

void InjectDll(DWORD PID)
{
    HANDLE hRemThread, hProc;
    const char *dll_name = DLL_NAME;
    char dll_full_path[MAX_PATH];
    char executable_dir[MAX_PATH];
    GetModuleFileNameA(NULL, executable_dir, MAX_PATH);
    if (!fexists(dll_name))
    {
        fail("DLL not found");
        return;
    }
    cout << "[*] Injecting DLL " << dll_name << " into PID " << PID << endl;
    cout << "[*] Opening process handle" << endl;
    hProc = OpenProcess(PROCESS_ALL_ACCESS, 0, PID);
    GetFullPathNameA(dll_name, MAX_PATH, dll_full_path, 0);
    cout << "[*] Adjusting privileges of process" << endl;
    adjustPrivs(hProc);
    if (HasModule(PID, dll_name))
    {
        cout << "[*] DLL already loaded" << endl;
        CloseHandle(hProc);
        return;
    };
    if (!fexists(dll_full_path))
    {
        CloseHandle(hProc);
        fail("DLL file not found");
    }
    HINSTANCE hK32 = LoadLibraryA("kernel32");
    cout << "[*] Getting address of LoadLibrary" << endl;
    LPVOID LoadLibrary_Address = (LPVOID)GetProcAddress(hK32, "LoadLibraryA");
    FreeLibrary(hK32);
    cout << "[+] LoadLibrary is at " << LoadLibrary_Address << endl;
    cout << "[*] Allocating " << strlen(dll_full_path) << " Bytes of Memory" << endl;
    LPVOID mem = VirtualAllocEx(hProc, NULL, strlen(dll_full_path), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);
    if (mem == NULL)
    {
        fail("Could not allocate memory");
        return;
    }
    cout << "[*] Writing DLL Name to Process Memory at " << mem << endl;
    WriteProcessMemory(hProc, mem, dll_full_path, strlen(dll_full_path), 0);
    cout << "[*] Creating Thread to Load DLL" << endl;
    hRemThread = CreateRemoteThread(hProc, 0, 0, (LPTHREAD_START_ROUTINE)LoadLibrary_Address, mem, 0, 0);
    cout << "[*] Waiting for DLL to load" << endl;
    WaitForSingleObject(hRemThread, INFINITE);
    CloseHandle(hRemThread);
    cout << "[*] Closing Process Handle" << endl;
    CloseHandle(hProc);
    return;
}


int main(int argc, char *argv[])
{
    DWORD PID = 0;
    HWND ScrapWin=FindWindow("ScrapClass",NULL);
    if (!ScrapWin) {
        cerr<<"Error: Scrapland window not found!"<<endl;
        exit(1);
    }
    GetWindowThreadProcessId(ScrapWin,&PID);
    if (PID) {
        InjectDll(PID);
    } else {
        fail("Error getting PID");
    }
}
