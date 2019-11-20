#pragma once
#include <Windows.h>
#include <d3d8.h>
#include <d3dx8.h>
#include <dxerr8.h>
uintmax_t frame = 0;
DWORD *GetVTable(void *addr)
{
    return (DWORD *)(*(DWORD *)addr);
}
bool overlay = false;
LPD3DXFONT m_pFont;
HFONT hFont;
HBRUSH hBrush;
D3DCOLOR color = D3DCOLOR_ARGB(255, 255, 0, 0);
RECT Rect = {0, 0, 0, 0};
D3DRECT panel;

size_t size_ht(HashTable<EntityList> *ht);
size_t size_ht(HashTable<Entity> *ht);

LPDIRECT3DDEVICE8 Render(LPDIRECT3DDEVICE8 dev)
{
    if (!overlay)
    {
        return dev;
    }
    char text[4096];
    int32_t money = 0;
    size_t num_ents = 0;
    size_t num_ent_lst = 0;
    if (ptr<void>(P_WORLD, 0) != nullptr)
    {
        money = ptr<int32_t>(P_WORLD, O_MONEY)[0];
        num_ents = size_ht(ptr<HashTable<Entity>>(P_WORLD, O_ENTS));
        num_ent_lst = size_ht(ptr<HashTable<EntityList>>(P_WORLD, O_ENTLISTS));
    }
    snprintf(text, 4096, "ScrapHack v0.1\nFrame: [%lld]\nMoney: [%d]\nEntities: [%ld]\nEntity Lists: [%ld]", ++frame, money, num_ents, num_ent_lst);
    if (m_pFont == nullptr)
    {
        D3DXCreateFont(dev, hFont, &m_pFont);
        CloseHandle(hFont);
    }
    m_pFont->Begin();
    m_pFont->DrawTextA(text, -1, &Rect, DT_CALCRECT, 0);
    m_pFont->DrawTextA(text, -1, &Rect, DT_LEFT, color);
    m_pFont->End();
    return dev;
}

HRESULT WINAPI H_EndScene(LPDIRECT3DDEVICE8 dev)
{
    typedef HRESULT(WINAPI * t_func)(LPDIRECT3DDEVICE8);
    shared_ptr<Hook> hook = Hook::get(H_EndScene);
    return hook->func<t_func>(Render(dev));
}

void unhook_d3d8()
{
    if (hFont != INVALID_HANDLE_VALUE)
    {
        CloseHandle(hFont);
    }
    if (m_pFont != nullptr)
    {
        m_pFont->Release();
    }
    Hook::drop(H_EndScene);
}

void hook_d3d8()
{
    typedef void(_cdecl * t_func)();
    hFont = CreateFont(20, 0, 0, 0, FW_BOLD, 0, 0, 0, ANSI_CHARSET, 0, 0, 0, 0, "Verdana");
    hBrush = CreateSolidBrush(D3DCOLOR_ARGB(25, 0, 0, 0));
    Hook::addr(ptr<void>(0x853954,0x2a3d8,0,4*35,0),H_EndScene);
    shared_ptr<Hook> hook = Hook::get(hook_d3d8);
    hook->func_void<t_func>();
    hook->disable();
    Hook::drop(hook_d3d8);
    return;
}
