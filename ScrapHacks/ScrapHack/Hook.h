#pragma once
#include <functional>
class Hook
{
private:
	MEMORY_BASIC_INFORMATION mbi;
	void *orig;
	void *detour;
	bool enabled;
	uint8_t orig_bytes[6];
	uint8_t jmp_bytes[6];
	static map<uintptr_t, shared_ptr<Hook>> hooks;

public:
	Hook(void *func, void *detour)
	{
		uintptr_t dest = reinterpret_cast<uintptr_t>(detour);
		uintptr_t src = reinterpret_cast<uintptr_t>(func);
		this->orig = func;
		this->detour = detour;
		this->jmp_bytes[0] = 0x68; // push
		this->jmp_bytes[1] = (dest >> 0) & 0xff;
		this->jmp_bytes[2] = (dest >> 8) & 0xff;
		this->jmp_bytes[3] = (dest >> 16) & 0xff;
		this->jmp_bytes[4] = (dest >> 24) & 0xff;
		this->jmp_bytes[5] = 0xC3; // ret
		VirtualQuery(func, &mbi, sizeof(mbi));
		VirtualProtect(mbi.BaseAddress, mbi.RegionSize, PAGE_EXECUTE_READWRITE, &mbi.Protect);
		memcpy(this->orig_bytes, this->orig, 1 + 4 + 1);
		VirtualProtect(mbi.BaseAddress, mbi.RegionSize, mbi.Protect, NULL);
		this->enabled = false;
	}

	~Hook()
	{
		cout << "Unhooking: [" << this->orig << " <- " << this->detour << "]" << endl;
		this->disable();
	}

	static void addr(void *addr, void *detour)
	{
		cout << "Hooking: [" << addr << " -> " << detour << "]" << endl;
		uintptr_t key = reinterpret_cast<uintptr_t>(detour);
		hooks[key] = make_shared<Hook>(addr, detour);
		hooks[key]->enable();
	}

	static void module(const char *mod, const char *func, void *detour)
	{
		cout << "Hooking: [" << mod << "]." << func << " -> " << detour << endl;
		void *addr = GetProcAddress(GetModuleHandle(mod), func);
		if (addr != NULL)
		{
			Hook::addr(addr, detour);
		}
		else
		{
			cerr << "[" << mod << "]." << func << " not found!" << endl;
		};
	}

	static shared_ptr<Hook> get(void *func)
	{
		uintptr_t addr = reinterpret_cast<uintptr_t>(func);
		return Hook::get(addr);
	}

	static shared_ptr<Hook> get(uintptr_t addr)
	{
		return hooks.at(addr);
	}

	static size_t drop(void *func)
	{
		uintptr_t addr = reinterpret_cast<uintptr_t>(func);
		return Hook::drop(addr);
	}

	static size_t drop(uintptr_t addr)
	{
		return hooks.erase(addr);
	}

	static void clear()
	{
		cout << "Clearing Hooks" << endl;
		for (pair<uintptr_t, shared_ptr<Hook>> h : hooks)
		{
			h.second->disable();
		}
		return hooks.clear();
	}

	void disable()
	{
		if (enabled)
		{
			//cout << "Disabling: [" << this->orig << " <- " << this->detour << "]" << endl;
			VirtualProtect(mbi.BaseAddress, mbi.RegionSize, PAGE_EXECUTE_READWRITE, NULL);
			memcpy(this->orig, this->orig_bytes, 1 + 4 + 1);
			VirtualProtect(mbi.BaseAddress, mbi.RegionSize, mbi.Protect, NULL);
			enabled = false;
		}
	}
	void enable()
	{
		if (!enabled)
		{
			//cout << "Enabling: [" << this->orig << " -> " << this->detour << "]" << endl;
			VirtualProtect(mbi.BaseAddress, mbi.RegionSize, PAGE_EXECUTE_READWRITE, NULL);
			memcpy(this->orig, this->jmp_bytes, 1 + 4 + 1);
			VirtualProtect(mbi.BaseAddress, mbi.RegionSize, mbi.Protect, NULL);
			enabled = true;
		}
	}

	void *get_orig()
	{
		return this->orig;
	}

	template <typename F, typename... Args>
	void func_void(Args... args)
	{
		disable();
		reinterpret_cast<F>(this->orig)(args...);
		enable();
		return;
	}

	template <typename F, typename... Args>
	decltype(auto) func(Args... args)
	{
		disable();
		auto ret = reinterpret_cast<F>(this->orig)(args...);
		enable();
		return ret;
	}
};

map<uintptr_t, shared_ptr<Hook>> Hook::hooks;
