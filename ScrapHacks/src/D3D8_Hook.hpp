#pragma once
#include <algorithm>
using namespace std;

#include <Windows.h>

#include <d3d8.h>
#include <d3dx8.h>
#include <dxerr8.h>


#include "D3D8_VMT.hpp"
#include "Hook.hpp"
#include "Scrapland.hpp"
#include "Structures.hpp"
#include "Util.hpp"


uintmax_t frame = 0;
bool hooked = false;
bool overlay = false;
LPD3DXFONT m_pFont;
HFONT hFont;
HBRUSH hBrush;
D3DCOLOR color = D3DCOLOR_XRGB(255, 0, 0);
RECT Rect = {0, 0, 0, 0};
D3DRECT panel;

D3DFILLMODE fillmode = D3DFILLMODE::D3DFILL_SOLID;
boolean use_z;

size_t size_ht(HashTable<EntityList> *ht);
size_t size_ht(HashTable<Entity> *ht);

#define STRINGIFY(x) #x
#define TOSTRING(x) STRINGIFY(x)

#define DX_Check(call) (_DX_Check(call,TOSTRING(call),__LINE__,__FILE__))

HRESULT _DX_Check(HRESULT res,char* call,size_t line, char* file) {
    if (res!=D3D_OK) {
        return DXTraceA(file,line,res,call,true);
    }
    return res;
}

LPDIRECT3DDEVICE8
Render(LPDIRECT3DDEVICE8 dev) {
    if (!overlay) {
        return dev;
    }
    IDirect3DSurface8* surf;
    char text[4096];
    int32_t money = 0;
    size_t num_ents = 0;
    size_t num_ent_lst = 0;
    if (ptr<void>(P_WORLD, 0) != nullptr) {
        money = ptr<int32_t>(P_WORLD, O_MONEY)[0];
        num_ents = size_ht(ptr<HashTable<Entity>>(P_WORLD, O_ENTS));
        num_ent_lst = size_ht(ptr<HashTable<EntityList>>(P_WORLD, O_ENTLISTS));
    }
    snprintf(text, 4096,"ScrapHack v0.1\nFrame: [%lld]\nMoney: [%d]\nEntities: [%ld]\nEntity Lists: [%ld]",++frame, money, num_ents, num_ent_lst);
    if (m_pFont == nullptr) {
        D3DXCreateFont(dev, hFont, &m_pFont);
        hFont = nullptr;
    }
    m_pFont->Begin();
    m_pFont->DrawTextA(text, -1, &Rect, DT_CALCRECT, 0);
    D3DRECT rec = {Rect.left,Rect.top,Rect.right,Rect.bottom};
    // dev->Clear(1,NULL,D3DCLEAR_TARGET,D3DCOLOR_ARGB(10,255,255,255),0,0);
    m_pFont->DrawTextA(text, -1, &Rect, DT_LEFT, color);
    m_pFont->End();
    return dev;
}


LPDIRECT3DDEVICE8
BeforeRender(LPDIRECT3DDEVICE8 dev) {
    return dev;
}

HRESULT WINAPI H_EndScene(LPDIRECT3DDEVICE8 dev) {
    typedef decltype(&H_EndScene) t_func;
    shared_ptr<Hook> hook = Hook::get(H_EndScene);
    return hook->func<t_func>(Render(dev));
}


HRESULT WINAPI H_BeginScene(LPDIRECT3DDEVICE8 dev) {
    typedef decltype(&H_BeginScene) t_func;
    shared_ptr<Hook> hook = Hook::get(H_BeginScene);
    HRESULT ret=hook->func<t_func>(dev);
    BeforeRender(dev);
    return ret;
}


HRESULT WINAPI H_SetLight(LPDIRECT3DDEVICE8 dev, DWORD index,
                          D3DLIGHT8 *light) {
    typedef decltype(&H_SetLight) t_func;
    shared_ptr<Hook> hook = Hook::get(H_SetLight);
    light->Diffuse.r = ((float)rand() / (float)RAND_MAX);
    light->Diffuse.g = ((float)rand() / (float)RAND_MAX);
    light->Diffuse.b = ((float)rand() / (float)RAND_MAX);
    light->Diffuse.a = 1.0;
    light->Specular.r = ((float)rand() / (float)RAND_MAX);
    light->Specular.g = ((float)rand() / (float)RAND_MAX);
    light->Specular.b = ((float)rand() / (float)RAND_MAX);
    light->Specular.r = 1.0;
    light->Ambient.r = ((float)rand() / (float)RAND_MAX);
    light->Ambient.g = ((float)rand() / (float)RAND_MAX);
    light->Ambient.b = ((float)rand() / (float)RAND_MAX);
    light->Ambient.a = 1.0;
    return hook->func<t_func>(dev, index, light);
}

HRESULT WINAPI H_DrawIndexedPrimitive(LPDIRECT3DDEVICE8 dev,
                                      D3DPRIMITIVETYPE Type, UINT minIndex,
                                      UINT NumVertices, UINT startIndex,
                                      UINT primCount) {
    typedef decltype(&H_DrawIndexedPrimitive) t_func;
    DWORD AMBIENT;
    shared_ptr<Hook> hook = Hook::get(H_DrawIndexedPrimitive);
    // dev->GetRenderState(D3DRS_AMBIENT, &AMBIENT);
    // dev->SetRenderState(D3DRS_AMBIENT, D3DCOLOR_XRGB(255, 255, 255));
    dev->SetRenderState(D3DRS_FILLMODE, fillmode);
    dev->SetRenderState(D3DRS_ZENABLE, use_z);
    auto ret = hook->func<t_func>(dev, Type, minIndex, NumVertices, startIndex,
                                  primCount);
    // dev->SetRenderState(D3DRS_AMBIENT, AMBIENT);
    dev->SetRenderState(D3DRS_ZENABLE, 1);
    return ret;
}

void unhook_d3d8() {
    if (!hooked) {
        return;
    }
    if (m_pFont != nullptr) {
        m_pFont->Release();
        m_pFont = nullptr;
    }
    Hook::drop(H_EndScene);
    Hook::drop(H_BeginScene);
    Hook::drop(H_DrawIndexedPrimitive);
    Hook::drop(H_SetLight);
    hooked=false;
}

map<size_t,void*> *dx_hooks = new map<size_t,void*>({
    {VMT_IDirect3DDevice8::m_EndScene,H_EndScene},
    {VMT_IDirect3DDevice8::m_BeginScene,H_BeginScene},
    {VMT_IDirect3DDevice8::m_DrawIndexedPrimitive,H_DrawIndexedPrimitive},
    {VMT_IDirect3DDevice8::m_SetLight,H_SetLight},
});

void hook_d3d8() {
    if (hooked) {
        return;
    }
    void *dev = nullptr;
    while (true) {
        dev = ptr<void>(P_D3DDEV);
        if (dev) {
            break;
        }
        Sleep(100);
    };
    hFont = CreateFontA(15, 0, 0, 0, FW_EXTRABOLD, 0, 0, 0, ANSI_CHARSET, 0, 0,
                        0, 0, "Lucida Console");
    hBrush = CreateSolidBrush(D3DCOLOR_ARGB(25, 0, 0, 0));
    for (auto h: *dx_hooks) {
        Hook::addr(GetVTable(dev)[h.first], h.second);
    }
    hooked=true;
    return;
}
