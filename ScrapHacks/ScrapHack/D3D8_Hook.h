#pragma once
#include <d3d8.h>
#include <d3dx8.h>
uintmax_t frame = 0;
DWORD* GetVTable(void* addr) {
	return (DWORD*)(*(DWORD*)addr);
}

void Render(LPDIRECT3DDEVICE8 dev) {
	char text[MAX_PATH];
	LPD3DXFONT m_pFont;
	HFONT hFont;
	RECT Rect={0,0,0,0};
	D3DCOLOR color = D3DCOLOR_XRGB(255, 0, 0);
	hFont = CreateFont(50, 0, 0, 0, FW_BOLD, 0, 0, 0, ANSI_CHARSET, 0, 0, 0, 0, "Verdana");
	D3DXCreateFont(dev, hFont, &m_pFont);
	snprintf(text, MAX_PATH, "Frame: %d", ++frame);
	if (m_pFont) {
		m_pFont->Begin();
		m_pFont->DrawTextA(text, -1, &Rect, DT_CALCRECT, 0);
		m_pFont->DrawTextA(text, -1, &Rect, DT_LEFT, color);
		m_pFont->End();
		m_pFont->Release();
		m_pFont = nullptr;
	}

}

HRESULT WINAPI H_EndScene(LPDIRECT3DDEVICE8 dev) {
	typedef HRESULT(WINAPI *t_func)(LPDIRECT3DDEVICE8);
	shared_ptr<Hook> hook = Hook::get(H_EndScene);
	t_func func = reinterpret_cast<t_func>(hook->func());
	Render(dev);
	hook->disable();
	HRESULT ret = func(dev);
	hook->enable();
	return ret;
	
}

HRESULT WINAPI H_CreateDevice(void* pDirect3D, unsigned int uiAdapter, D3DDEVTYPE pDeviceType, HWND hFocusWindow,
	unsigned long ulBehaviorFlags, D3DPRESENT_PARAMETERS* pPresentationParameters,
	LPDIRECT3DDEVICE8* ppReturnedDeviceInterface) {
	typedef HRESULT(WINAPI *t_func)(void*, unsigned int, D3DDEVTYPE, HWND, unsigned long, D3DPRESENT_PARAMETERS*, LPDIRECT3DDEVICE8*);
	shared_ptr<Hook> hook = Hook::get(H_CreateDevice);
	t_func func = reinterpret_cast<t_func>(hook->func());
	hook->disable();
	HRESULT ret = func(pDirect3D, uiAdapter, pDeviceType, hFocusWindow, ulBehaviorFlags, pPresentationParameters, ppReturnedDeviceInterface);
	cout << "Ret:" << ret << endl;
	DWORD *vtable = GetVTable(ppReturnedDeviceInterface[0]);
	cout << "Dev VTable @ " << vtable << endl;
	cout << "Dev VTable[35]: " << (void*)(vtable[35]) << endl; // EndScene
	Hook::addr((void*)vtable[35], H_EndScene);
	Hook::drop(H_CreateDevice);
	return ret;
}

LPDIRECT3D8 WINAPI H_Direct3DCreate8(unsigned int SDKVersion) {
	typedef LPDIRECT3D8(_stdcall *t_func)(unsigned int);
	shared_ptr<Hook> hook = Hook::get(H_Direct3DCreate8);
	t_func func = reinterpret_cast<t_func>(hook->func());
	hook->disable();
	D3DPRESENT_PARAMETERS D3D_Present_Param = { 0,0,D3DFMT_UNKNOWN,0,D3DMULTISAMPLE_NONE,D3DSWAPEFFECT_DISCARD,0,1,0,D3DFMT_UNKNOWN,0,0,0 };
	LPDIRECT3D8 ret = func(SDKVersion);
	cout << "D3D8-Create: " << SDKVersion << " -> " << ret << endl;
	DWORD *vtable = GetVTable(ret);
	cout << "ID3D8 VTable @ " << vtable << endl;
	cout << "ID3D8 VTable[15]: " << (void*)(vtable[15]) << endl; // CreateDevice
	Hook::addr((void*)vtable[15], reinterpret_cast<void*>(H_CreateDevice));
	Hook::drop(H_Direct3DCreate8);
	return ret;
}

void hook_d3d8() {
	Hook::module("d3d8.dll","Direct3DCreate8", H_Direct3DCreate8);
}
