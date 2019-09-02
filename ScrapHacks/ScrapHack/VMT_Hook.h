
#pragma once
class VMT_Hook
{
private:
	MEMORY_BASIC_INFORMATION mbi;
	void *orig;
	void *detour;
	DWORD *vtable;
	size_t ord;
	bool enabled;
	static map<uintptr_t, shared_ptr<VMT_Hook>> hooks;
	static DWORD *GetVTable(void *addr)
	{
		return (DWORD *)*(DWORD *)addr;
	};

public:
	VMT_Hook(void *obj, size_t ord, void *detour)
	{
		this->vtable = GetVTable(obj);
		this->detour = detour;
		this->orig = reinterpret_cast<void *>(vtable[ord]);
		this->ord = ord;
		this->enabled = false;

		VirtualQuery(&this->vtable[this->ord], &mbi, sizeof(mbi));
		cout << "Hooking: " << this->vtable << "[" << this->ord << "]: (" << this->orig << " -> " << this->detour << ")" << endl;
	}

	~VMT_Hook()
	{
		cout << "Unhooking: " << this->vtable << "[" << this->ord << "]: (" << this->orig << " -> " << this->detour << ")" << endl;
		this->disable();
	}

	static void create(void *obj, size_t ord, void *detour)
	{
		uintptr_t key = reinterpret_cast<uintptr_t>(detour);
		hooks[key] = make_shared<VMT_Hook>(obj, ord, detour);
		hooks[key]->enable();
	}

	static shared_ptr<VMT_Hook> get(void *func)
	{
		uintptr_t addr = reinterpret_cast<uintptr_t>(func);
		return VMT_Hook::get(addr);
	}

	static shared_ptr<VMT_Hook> get(uintptr_t addr)
	{
		return hooks.at(addr);
	}

	static size_t drop(void *func)
	{
		uintptr_t addr = reinterpret_cast<uintptr_t>(func);
		return VMT_Hook::drop(addr);
	}

	static size_t drop(uintptr_t addr)
	{
		return hooks.erase(addr);
	}

	static void clear()
	{
		return hooks.clear();
	}

	void disable()
	{
		if (enabled)
		{
			cout << "Disabling: " << this->vtable << "[" << this->ord << "]: (" << this->orig << " -> " << this->detour << ")" << endl;
			VirtualProtect(mbi.BaseAddress, mbi.RegionSize, PAGE_EXECUTE_READWRITE, NULL);
			this->vtable[ord] = reinterpret_cast<DWORD>(this->orig);
			VirtualProtect(mbi.BaseAddress, mbi.RegionSize, mbi.Protect, NULL);
			enabled = false;
		}
	}
	void enable()
	{
		if (!enabled)
		{
			cout << "Enabling: " << this->vtable << "[" << this->ord << "]: (" << this->orig << " -> " << this->detour << ")" << endl;
			VirtualProtect(mbi.BaseAddress, mbi.RegionSize, PAGE_EXECUTE_READWRITE, NULL);
			this->vtable[ord] = reinterpret_cast<DWORD>(this->detour);
			VirtualProtect(mbi.BaseAddress, mbi.RegionSize, mbi.Protect, NULL);
			enabled = true;
		}
	}

	template <typename T>
	T func()
	{
		return reinterpret_cast<T>(this->orig);
	}
};

map<uintptr_t, shared_ptr<VMT_Hook>> VMT_Hook::hooks;
