#pragma once
#include <d3d8.h>
#include <d3dx8.h>
uintmax_t frame = 0;
DWORD* GetVTable(void* addr) {
	return (DWORD*)(*(DWORD*)addr);
}
bool overlay = false;
LPD3DXFONT m_pFont;
HFONT hFont;
HBRUSH hBrush;
D3DCOLOR color = D3DCOLOR_ARGB(255,255, 0, 0);
RECT Rect = { 0,0,0,0 };
D3DRECT panel;

size_t size_ht(HashTable<EntityList>* ht);
size_t size_ht(HashTable<Entity>* ht);

LPDIRECT3DDEVICE8 Render(LPDIRECT3DDEVICE8 dev) {
	if (!overlay) {
		return dev;
	}
	char text[4096];
	int32_t money = 0;
	size_t num_ents = 0;
	size_t num_ent_lst = 0;
	if (ptr<void>(P_WORLD, 0)!=nullptr) {
		money = ptr<int32_t>(P_WORLD, O_MONEY)[0];
		num_ents= size_ht(ptr<HashTable<Entity>>(P_WORLD, O_ENTS));
		num_ent_lst = size_ht(ptr<HashTable<EntityList>>(P_WORLD, O_ENTLISTS));
	}
	snprintf(text, 4096, "ScrapHack v0.1\nFrame: [%lld]\nMoney: [%d]\nEntities: [%ld]\nEntity Lists: [%ld]", ++frame, money, num_ents,num_ent_lst);
	if (m_pFont == nullptr) {
		D3DXCreateFont(dev, hFont, &m_pFont);
		CloseHandle(hFont);
	}
	m_pFont->Begin();
	m_pFont->DrawTextA(text, -1, &Rect, DT_CALCRECT, 0);
	m_pFont->DrawTextA(text, -1, &Rect, DT_LEFT, color);
	m_pFont->End();
	return dev;
}

HRESULT WINAPI H_EndScene(LPDIRECT3DDEVICE8 dev) {
	typedef HRESULT(WINAPI *t_func)(LPDIRECT3DDEVICE8);
	shared_ptr<Hook> hook = Hook::get(H_EndScene);
	return hook->func<t_func>(Render(dev));
}

HRESULT WINAPI H_CreateDevice(void* pDirect3D, unsigned int uiAdapter, D3DDEVTYPE pDeviceType, HWND hFocusWindow,
	unsigned long ulBehaviorFlags, D3DPRESENT_PARAMETERS* pPresentationParameters,
	LPDIRECT3DDEVICE8* ppReturnedDeviceInterface) {
	typedef HRESULT(WINAPI *t_func)(void*, unsigned int, D3DDEVTYPE, HWND, unsigned long, D3DPRESENT_PARAMETERS*, LPDIRECT3DDEVICE8*);
	shared_ptr<Hook> hook = Hook::get(H_CreateDevice);
	HRESULT ret = hook->func<t_func>(pDirect3D, uiAdapter, pDeviceType, hFocusWindow, ulBehaviorFlags, pPresentationParameters, ppReturnedDeviceInterface);
	cout << "CreateDevice -> " << ret << endl;
	void* EndScene = reinterpret_cast<void*>(GetVTable(ppReturnedDeviceInterface[0])[35]);
	cout << "EndScene @ " << EndScene << endl; // EndScene
	Hook::addr(EndScene, H_EndScene);
	Hook::drop(H_CreateDevice);
	return ret;
}

LPDIRECT3D8 WINAPI H_Direct3DCreate8(unsigned int SDKVersion) {
	typedef LPDIRECT3D8(_stdcall *t_func)(unsigned int);
	shared_ptr<Hook> hook = Hook::get(H_Direct3DCreate8);
	
	LPDIRECT3D8 ret = hook->func<t_func>(SDKVersion);
	cout << "D3D8-Create: " << SDKVersion << " -> " << ret << endl;
	void *CreateDevice = reinterpret_cast<void*>(GetVTable(ret)[15]);
	void *Release = reinterpret_cast<void*>(GetVTable(ret)[2]);
	cout << "CreateDevice @ " << CreateDevice << endl; // CreateDevice
	Hook::addr(CreateDevice, H_CreateDevice);
	Hook::drop(H_Direct3DCreate8);
	
	return ret;
}

void unhook_d3d8() {
	if (hFont != INVALID_HANDLE_VALUE) {
		CloseHandle(hFont);
	}
	if (m_pFont != nullptr) {
		m_pFont->Release();
	}
	Hook::drop(H_EndScene);
}

void hook_d3d8() {
	hFont = CreateFont(20, 0, 0, 0, FW_BOLD, 0, 0, 0, ANSI_CHARSET, 0, 0, 0, 0, "Verdana");
	hBrush = CreateSolidBrush(D3DCOLOR_ARGB(25, 0, 0, 0));
	Hook::module("d3d8.dll","Direct3DCreate8", H_Direct3DCreate8);
}