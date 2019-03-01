#pragma once
#include <functional>
class Hook;

map<uintptr_t, shared_ptr<Hook>> hooks;

class Hook {
private:
	DWORD protect;
	void* orig;
	void* detour;
	uint8_t orig_bytes[6];
	uint8_t jmp_bytes[6];
public:
	Hook(void* func, void* detour) {
		cout << "Hooking: " << func << " -> " << detour << endl;
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
		VirtualProtect(func, 16, PAGE_EXECUTE_READWRITE, &(this->protect));
		memcpy(this->orig_bytes, this->orig, 1 + 4 + 1);
		memcpy(this->orig, this->jmp_bytes, 1 + 4 + 1);
		hooks[src]=shared_ptr<Hook>(this);
	}
	
	~Hook() {
		cout << "Unhooking: " << this->detour << " -> " << this->orig << endl;
		uintptr_t src = reinterpret_cast<uintptr_t>(this->orig);
		memcpy(this->orig, this->orig_bytes, 1 + 4 + 1);
	}

	void disable() {
		memcpy(this->orig, this->orig_bytes, 1 + 4 + 1);
	}
	void enable() {
		memcpy(this->orig, this->jmp_bytes, 1 + 4 + 1);
	}
	
	void* func() {
		return this->orig;
	}

};
