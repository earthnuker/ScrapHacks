#define WIN32_LEAN_AND_MEAN
#include "stdafx.h"
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <iomanip>
#include <iostream>
#include <typeinfo>
#include <functional>
#include <Windows.h>
#include <TlHelp32.h>

#pragma comment(lib, "d3d8.lib")
#pragma comment(lib, "d3dx8.lib")
#pragma comment(lib, "legacy_stdio_definitions.lib")

using namespace std;

#include "Scrapland.h"
#include "Util.h"
#include "Structures.h"
#include "Py_Utils.h"
#include "Hook.h"
#include "VMT_Hook.h"
#include "D3D8_Hook.h"

HMODULE hD3D8Dll = 0;

bool initialized = false;
bool running = true;
HMODULE mod = 0;

void DllUnload(HMODULE);
void hook_exit();

size_t dump_ht(HashTable<EntityList>* ht) {
	size_t cnt = 0;
	for (size_t i = 0; i < ht->size; ++i) {
		HashTableEntry<EntityList>* ent = ht->chains[i];
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

size_t dump_ht(HashTable<Entity>* ht) {
	size_t cnt = 0;
	for (size_t i = 0; i < ht->size; ++i) {
		HashTableEntry<Entity>* ent = ht->chains[i];
		if (ent) {
			cout << i << ": ";
			while (ent) {
				++cnt;
				cout << "[ " << ent->name << ": " << ent->data<<"]";
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

void MainLoop(HMODULE mod)
{
	Sleep(100);
	hook_exit();
	cout << "[*] Starting main Loop" << endl;
	cout << endl;
	cout << "[F3 ] Unload ScrapHacks" << endl;
	cout << "[F5 ] Show Overlay" << endl;
	cout << "[F6 ] Show Alarm status" << endl;
	cout << "[F7 ] Set Money to 0x7fffffff" << endl;
	cout << "[F8 ] Dump python modules" << endl;
	cout << "[F9 ] Dump Entity hashtable" << endl;
	cout << "[F10] Enable python tracing" << endl;
	cout << "[ F ] \"Handbrake\" (*Will* crash the game after some time!)" << endl;

	while (running)
	{
		Sleep(100);

		while (key_down('F'))
		{
			scrap_exec("dbg.brake()");
		}
		if (key_down_norepeat(VK_F3))
		{
			break;
		}

		if (key_down_norepeat(VK_F5))
		{
			overlay = !overlay;
		}
		if (key_down_norepeat(VK_F6))
		{
			
			float* alarm = ptr<float>(P_WORLD, O_ALARM);
			float* alarm_grow = ptr<float>(P_WORLD, O_ALARM_GROW);
			cout << "Alarm: " << alarm[0] << " + " << alarm_grow[0] << endl;
		}
		if (key_down_norepeat(VK_F7))
		{
			int32_t *money = ptr<int32_t>(P_WORLD,O_MONEY);
			*money = 0x7fffffff;
		}
		if (key_down_norepeat(VK_F8))
		{
			for (auto mod : Py)
			{
				for (auto meth : mod.second.methods)
				{
					cout << mod.first << "." << meth.first << " @ " << meth.second->ml_meth << endl;
				}
			}
		}

		if (key_down_norepeat(VK_F9)) {
			cout << "Entities:" << endl;
			dump_ht(ptr<HashTable<Entity>>(P_WORLD, O_ENTS));
			cout << "Entity Lists:" << endl;
			dump_ht(ptr<HashTable<EntityList>>(P_WORLD, O_ENTLISTS));
		}
		if (key_down_norepeat(VK_F10))
		{
			scrap_exec("dbg.settrace()");
		}
	}
	FreeLibraryAndExitThread(mod, 0);
}

void InitConsole()
{
	char me[1024];
	GetModuleFileName(mod, me, 1024);
	SetupConsole(me);
}

void handle_command(const char* cmd) {
	cout << "CMD: " << cmd << endl;
	scrap_log(0x00ff00, "HAXX: ");
	scrap_log(0x00ff00,cmd);
	scrap_log(0x00ff00,"\n");
	return;
}

int hooked_console(const char* cmd) {
	typedef int(_cdecl *t_func)(const char*);
	shared_ptr<Hook> hook = Hook::get(hooked_console);
	if (cmd[0] == '$') {
		handle_command(++cmd);
		return 0;
	}
	int ret= hook->func<t_func>(cmd);
	return ret;
}

void hook_console() {
	Hook::addr(reinterpret_cast<void*>(P_CON_HANDLER) , hooked_console);
}

void H_Exit(){
	typedef void(_cdecl *t_func)(void);
	shared_ptr<Hook> hook = Hook::get(H_Exit);
	DllUnload(mod);
	hook->disable();
	HWND hMainWindow = ptr<HWND>(0x7FA830, 0x7c)[0];
	SendMessage(hMainWindow, WM_CLOSE, 0, 0);
	return;
}

void hook_exit() {
	//void* p_exit = ptr<void*>(0x7fa830,0x0, 0x20);
	Hook::addr(reinterpret_cast<void*>(0x4010c0), H_Exit);
}

DWORD PPID() {
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

void DllPreInit(HMODULE _mod) {
	char mfn[1024];
	char inj[MAX_PATH];
	DWORD INJ_PID=0;
	InitConsole();
	GetModuleFileName(0, mfn, 1024);
	Py = get_modules(P_PY_MODS);
	cout << "[+] ScrapHacks v0.1 Loaded in " << mfn << " (PID: " << std::hex << GetCurrentProcessId() <<std::dec << ")" << endl;
	GetEnvironmentVariable("Inj_PID", inj, MAX_PATH);
	SetEnvironmentVariable("Inj_PID", NULL);
	hook_console();
	sscanf(inj, "%d", &INJ_PID);
	cout << INJ_PID << "," << PPID() << endl;
	if (PPID() == INJ_PID) {
		hook_d3d8();
		overlay = true;
	}
	else {
		cout << "[-] No launched by Injector, not hooking DX8" << endl;
	}
}

void DllInit(HMODULE _mod)
{
	initialized = true;
	mod = _mod;
	Sleep(3000);
	cout << "[*] World: " << ptr<void>(P_WORLD, 0) << endl;
	cout << "[*] Importing python dbg module" << endl;
	scrap_exec("import dbg");
	scrap_log(0xff0000, "ScrapHacks loaded!\n");
	CreateThread(NULL, NULL, (LPTHREAD_START_ROUTINE)MainLoop, mod, 0, 0);
	cout << "[*] Starting message pump" << endl;
	MSG msg;
	while (GetMessage(&msg, NULL, 0, 0))
	{
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}
	return;
}

void DllUnload(HMODULE _mod) {
	SetConsoleCtrlHandler(NULL, false);
	unhook_d3d8();
	Hook::clear();
	scrap_log(0xff0000, "ScrapHacks unloaded!\n");
	cout << "[+] ScrapHacks unloaded, you can now close the console!" << endl;
	FreeConsole();
	DestroyWindow(GetConsoleWindow());
	return;
}