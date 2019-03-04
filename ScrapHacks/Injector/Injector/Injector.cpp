#include "stdafx.h"
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

string fromhex(string input)
{
	transform(input.begin(), input.end(), input.begin(), ::toupper);
	string hc = "0123456789ABCDEF";
	string o = "";
	int n = 0;
	int v = 0;
	for (unsigned char c : input)
	{
		if (hc.find(c) != size_t(-1))
		{
			if ((n++) % 2 == 0)
			{
				v = hc.find(c) << 4;
			}
			else
			{
				o += char(v + hc.find(c));
			}
		}
		else
		{
			cout << "Invalid Character in hex string" << endl;
			return "";
		}
	}
	return o;
}

vector<string> split(string str, char sep)
{
	vector<string> ret;
	string part;
	for (auto n : str)
	{
		if (n == sep)
		{
			ret.push_back(part);
			part.clear();
		}
		else
		{
			part = part + n;
		}
	}
	if (part != "")
		ret.push_back(part);
	return ret;
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

bool ProcRunning(DWORD PID)
{
	bool ret = false;
	HANDLE hSnap = CreateToolhelp32Snapshot(TH32CS_SNAPMODULE | TH32CS_SNAPMODULE32, PID);
	if (hSnap == INVALID_HANDLE_VALUE)
	{
		return false;
	}
	CloseHandle(hSnap);
	return true;
}

bool adjustPrivs(HANDLE hProc)
{
	HANDLE hToken;
	LUID luid;
	TOKEN_PRIVILEGES tkprivs;
	if (!OpenProcessToken(hProc, (TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY), &hToken))
	{
		cout << "[!] Could not Open Process Token: " << GetLastErrorAsString() << endl;
		return 0;
	}
	if (!LookupPrivilegeValue(0, SE_DEBUG_NAME, &luid))
	{
		CloseHandle(hToken);
		cout << "[!] Error Looking up Privilege Value: " << GetLastErrorAsString() << endl;
		return 0;
	}
	tkprivs.PrivilegeCount = 1;
	tkprivs.Privileges[0].Luid = luid;
	tkprivs.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED;
	bool bRet = AdjustTokenPrivileges(hToken, 0, &tkprivs, sizeof(tkprivs), NULL, NULL);
	CloseHandle(hToken);
	if (!bRet)
	{
		cout << "[!] Could Not Adjust Privileges: " << GetLastErrorAsString() << endl;
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
	if (!fexists(dll_name))
	{
		cout << "[!] DLL not found!" << endl;
		return;
	}
	cout << "[*] Injecting DLL " << dll_name << " into PID " << PID << endl;
	cout << "[*] Opening Process Handle" << endl;
	hProc = OpenProcess(PROCESS_ALL_ACCESS, 0, PID);
	GetFullPathNameA(dll_name, MAX_PATH, dll_full_path, 0);
	cout << "[*] Adjusting Privileges of Process" << endl;
	adjustPrivs(hProc);
	if (HasModule(PID, dll_name))
	{
		cout << "[*] DLL already Loaded" << endl;
		CloseHandle(hProc);
		return;
	};
	if (!fexists(dll_full_path))
	{
		cout << "[!] DLL file not found!" << endl;
		CloseHandle(hProc);
		return;
	}
	HINSTANCE hK32 = LoadLibraryA("kernel32");
	cout << "[*] Getting Address of LoadLibrary" << endl;
	LPVOID LoadLibrary_Address = (LPVOID)GetProcAddress(hK32, "LoadLibraryA");
	FreeLibrary(hK32);
	cout << "[+] LoadLibrary is at " << LoadLibrary_Address << endl;
	cout << "[*] Allocating " << strlen(dll_full_path) << " Bytes of Memory" << endl;
	LPVOID mem = VirtualAllocEx(hProc, NULL, strlen(dll_full_path), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);
	if (mem == NULL)
	{
		cout << "[!] Could not Allocate Memory: " << GetLastErrorAsString() << endl;
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

vector<HANDLE> spawn(char* binary) {
	STARTUPINFO startupinfo;
	PROCESS_INFORMATION processinfo;
	ZeroMemory(&startupinfo, sizeof(startupinfo));
	ZeroMemory(&processinfo, sizeof(processinfo));
	startupinfo.cb = sizeof(startupinfo);
	if (!CreateProcessA(NULL, binary, NULL, NULL, FALSE, CREATE_SUSPENDED, NULL, NULL, &startupinfo, &processinfo)) {
		return {};
	}
	return { processinfo.hProcess,processinfo.hThread };
}

int main(int argc, char *argv[])
{
	string prog;
	HANDLE hProc = INVALID_HANDLE_VALUE;
	HANDLE hThread = INVALID_HANDLE_VALUE;
	DWORD PID = 0;
	if ((argc>1)&&fexists(argv[1])) {
		cout << "[*] Spawning process for \"" << argv[1] << "\"" << endl;
		vector<HANDLE> handles = spawn(argv[1]);
		if (handles.empty()) {
			cout << "[!] Error: " << GetLastErrorAsString() << endl;
			return -1;
		}
		hProc = handles[0];
		hThread = handles[1];
		PID = GetProcessId(hProc);
		cout << "[+] Got PID: " << PID << endl;
	} else {
		GetWindowThreadProcessId(FindWindowA("ScrapClass", NULL), &PID);
		if (PID == 0)
		{
			cout << "[*] Waiting for Scrapland to Launch..." << endl;
		}
		while (PID == 0)
		{
			Sleep(100);
			GetWindowThreadProcessId(FindWindowA("ScrapClass", NULL), &PID);
		}
		cout << "[+] Found PID: " << PID << endl;
	}
	InjectDll(PID);
	if (hThread != INVALID_HANDLE_VALUE) {
		while (ResumeThread(hThread));
	}
	cout << "[*] Done!" << endl;
	return 0;
}
