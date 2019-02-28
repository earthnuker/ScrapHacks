#pragma once
#define P_WORLD 0x7FE944
#define P_PY_MODS 0x79C698
#define O_MONEY 0x2090

auto scrap_log = (int(_cdecl*)(int, const char*))0x4134C0;
auto scrap_exec = (void(_cdecl*)(const char*))0x5a8390;
