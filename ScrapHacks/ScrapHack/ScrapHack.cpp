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
using namespace std;

#include "Scrapland.h"
#include "Util.h"
#include "Structures.h"
#include "Py_Utils.h"
#include "Hook.h"

#define SIZE 6

HMODULE hD3D8Dll = 0;

bool initialized = false;
bool running = true;
HMODULE mod = 0;

void MainLoop(HMODULE mod)
{
	Sleep(100);
	cout << "[*] Starting main Loop" << endl;
	cout << endl;
	cout << "[F3 ] Unload ScrapHacks" << endl;
	cout << "[F7 ] Set Money to 0x7fffffff" << endl;
	cout << "[F8 ] Dump python modules" << endl;
	cout << "[F10] Enable python tracing" << endl;
	cout << "[ F ] \"Handbrake\" (*Will* crash the game after some time!)" << endl;

	while (running)
	{
		Sleep(100);
		if (key_down_norepeat(VK_F10))
		{
			scrap_exec("dbg.settrace()");
		}
		while (key_down('F'))
		{
			scrap_exec("dbg.brake()");
		}
		if (key_down_norepeat(VK_F6))
		{
			/*
			int32_t* alarm = reinterpret_cast<int32_t*>(ptr(WORLD, { 0x1C6C }));
			int16_t* alarm = reinterpret_cast<int16_t*>(ptr(WORLD, { 0x1C6C }));
			*/
		}
		if (key_down_norepeat(VK_F7))
		{
			/*==========================
			mov     ecx, [7FE944h]
			mov     edx, [ecx + 2090h]
			==========================*/
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
		if (key_down_norepeat(VK_F3))
		{
			break;
		}
	}
	SetConsoleCtrlHandler(NULL, false);
	hooks.clear();
	scrap_log(0xff0000, "ScrapHacks unloaded!\n");
	cout << "[+] ScrapHacks unloaded, you can now close the console!" << endl;
	FreeConsole();
	PostQuitMessage(0);
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

int my_console(const char* cmd) {
	typedef int(_cdecl *t_func)(const char*);
	shared_ptr<Hook> hook = hooks[P_CON_HANDLER];
	t_func func= reinterpret_cast<t_func>(hook->func());
	if (cmd[0] == '$') {
		handle_command(++cmd);
		return 0;
	}
	hook->disable();
	int ret=func(cmd);
	hook->enable();
	return ret;
}

void hook_console() {
	new Hook(reinterpret_cast<void*>(P_CON_HANDLER) , my_console);
}


void DllPreInit(HMODULE _mod) {
	char mfn[1024];
	InitConsole();
	GetModuleFileName(0, mfn, 1024);
	Py = get_modules(P_PY_MODS);
	hD3D8Dll = GetModuleHandle("d3d8.dll");
	cout << "[+] ScrapHacks v0.1 Loaded in " << mfn << endl;
	cout << "[*] D3D8 DLL @0x" << hD3D8Dll << endl;
	hook_console();
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