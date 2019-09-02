#pragma once
#include <string>
#define DLL_EXPORT extern "C" __declspec(dllexport)

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

void SetupStreams()
{
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

void SetupConsole()
{
	if (!AllocConsole())
	{
		FreeConsole();
		AllocConsole();
	}
	AttachConsole(GetCurrentProcessId());
	SetupStreams();
}

void SetupConsole(const char *title)
{
	SetupConsole();
	SetConsoleTitleA(title);
}

void FreeConsole(bool wait)
{
	if (wait)
	{
		cout << "[?] Press Enter to Exit";
		cin.ignore();
	}
	FreeConsole();
}

bool in_foreground = false;
BOOL CALLBACK EnumWindowsProcMy(HWND hwnd, LPARAM lParam)
{
	DWORD lpdwProcessId;
	GetWindowThreadProcessId(hwnd, &lpdwProcessId);
	if (lpdwProcessId == lParam)
	{
		in_foreground = (hwnd == GetForegroundWindow()) || (hwnd == GetActiveWindow());
		return FALSE;
	}
	return TRUE;
}

bool key_down(int keycode, int delay = 100)
{
	in_foreground = false;
	EnumWindows(EnumWindowsProcMy, GetCurrentProcessId());
	if (in_foreground)
	{
		if (GetAsyncKeyState(keycode))
		{
			Sleep(delay);
			return true;
		}
	}
	return false;
}

bool key_down_norepeat(int keycode, int delay = 100)
{
	in_foreground = false;
	EnumWindows(EnumWindowsProcMy, GetCurrentProcessId());
	if (in_foreground)
	{
		if (GetAsyncKeyState(keycode))
		{
			while (GetAsyncKeyState(keycode))
			{
				Sleep(delay);
			}
			return true;
		}
	}
	return false;
}

void hexdump(void *addr, size_t count)
{
	for (size_t i = 0; i < count; ++i)
	{
		unsigned int val = (unsigned int)((unsigned char *)addr)[i];
		cout << setfill('0') << setw(2) << std::hex << val << " ";
		if (((i + 1) % 16) == 0)
		{
			cout << endl;
		}
	}
	cout << endl;
}

template <typename T>
T *__ptr(uintptr_t addr)
{
	return reinterpret_cast<T *>(addr);
}

template <typename T>
T *__ptr(uintptr_t addr, ptrdiff_t offset)
{
	//cout << "[" << (void*)addr << "] + " << (void*)offset << " = ";
	addr = reinterpret_cast<uintptr_t *>(addr)[0] + offset;
	//cout << (void*)addr << endl;;
	auto ret = __ptr<T>(addr);
	return ret;
}

template <typename T, typename... Offsets>
T *__ptr(uintptr_t addr, ptrdiff_t offset, Offsets... offsets)
{
	//cout << "[" << (void*)addr << "] + " << (void*)offset << " = ";
	addr = reinterpret_cast<uintptr_t *>(addr)[0] + offset;
	//cout << (void*)addr << endl;;
	auto ret = __ptr<T>(addr, offsets...);
	return ret;
}

template <typename T, typename... Offsets>
T *ptr(uintptr_t addr, Offsets... offsets)
{
	auto ret = __ptr<T>(addr, offsets...);
	return ret;
}
