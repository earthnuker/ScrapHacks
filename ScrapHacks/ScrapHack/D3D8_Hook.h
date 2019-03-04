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
D3DCOLOR color = D3DCOLOR_XRGB(255, 0, 0);
RECT Rect = { 0,0,0,0 };
D3DRECT panel;

void Render(LPDIRECT3DDEVICE8 dev) {
	if (!overlay) {
		return;
	}
	char text[MAX_PATH];
	snprintf(text, MAX_PATH, "Frame: [%lld]\nTest", ++frame);
	if (m_pFont == nullptr) {
		D3DXCreateFont(dev, hFont, &m_pFont);
		CloseHandle(hFont);
	}
	m_pFont->Begin();
	m_pFont->DrawTextA(text, -1, &Rect, DT_CALCRECT, 0);
	
	dev->Clear(0, NULL, D3DCLEAR_ZBUFFER, D3DCOLOR_ARGB(25, 0, 0, 0),0.5,0);
	
	m_pFont->DrawTextA(text, -1, &Rect, DT_LEFT, color);
	m_pFont->End();
}

HRESULT WINAPI H_EndScene(LPDIRECT3DDEVICE8 dev) {
	typedef HRESULT(WINAPI *t_func)(LPDIRECT3DDEVICE8);
	shared_ptr<Hook> hook = Hook::get(H_EndScene);
	_asm push esi;
	_asm pushad;
	Render(dev);
	hook->disable();
	HRESULT ret = hook->func<t_func>()(dev);
	hook->enable();
	_asm popad;
	_asm pop esi;
	return ret;
}

HRESULT WINAPI H_CreateDevice(void* pDirect3D, unsigned int uiAdapter, D3DDEVTYPE pDeviceType, HWND hFocusWindow,
	unsigned long ulBehaviorFlags, D3DPRESENT_PARAMETERS* pPresentationParameters,
	LPDIRECT3DDEVICE8* ppReturnedDeviceInterface) {
	_asm push esi;
	_asm pushad;
	typedef HRESULT(WINAPI *t_func)(void*, unsigned int, D3DDEVTYPE, HWND, unsigned long, D3DPRESENT_PARAMETERS*, LPDIRECT3DDEVICE8*);
	shared_ptr<Hook> hook = Hook::get(H_CreateDevice);
	hook->disable();
	HRESULT ret = hook->func<t_func>()(pDirect3D, uiAdapter, pDeviceType, hFocusWindow, ulBehaviorFlags, pPresentationParameters, ppReturnedDeviceInterface);
	cout << "CreateDevice ->" << ret << endl;
	void* EndScene = reinterpret_cast<void*>(GetVTable(ppReturnedDeviceInterface[0])[35]);
	cout << "EndScene @ " << EndScene << endl; // EndScene
	Hook::addr(EndScene, H_EndScene);
	Hook::drop(H_CreateDevice);
	_asm popad;
	_asm pop esi;

	return ret;
}

LPDIRECT3D8 WINAPI H_Direct3DCreate8(unsigned int SDKVersion) {
	typedef LPDIRECT3D8(_stdcall *t_func)(unsigned int);
	shared_ptr<Hook> hook = Hook::get(H_Direct3DCreate8);
	
	_asm push esi;
	_asm pushad;

	hook->disable();
	LPDIRECT3D8 ret = hook->func<t_func>()(SDKVersion);
	cout << "D3D8-Create: " << SDKVersion << " -> " << ret << endl;
	void *CreateDevice = reinterpret_cast<void*>(GetVTable(ret)[15]);
	cout << "CreateDevice @ " << CreateDevice << endl; // CreateDevice
	Hook::addr(CreateDevice, H_CreateDevice);
	Hook::drop(H_Direct3DCreate8);
	_asm popad;
	_asm pop esi;

	return ret;
}

void hook_d3d8() {
	hFont = CreateFont(20, 0, 0, 0, FW_BOLD, 0, 0, 0, ANSI_CHARSET, 0, 0, 0, 0, "Verdana");
	hBrush = CreateSolidBrush(D3DCOLOR_ARGB(25, 0, 0, 0));
	Hook::module("d3d8.dll","Direct3DCreate8", H_Direct3DCreate8);
}
