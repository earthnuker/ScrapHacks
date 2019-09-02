#pragma once

//OFFSETS
#define O_MONEY 0x2090
#define O_ALARM 0x1C6C
#define O_ALARM_GROW 0x1C68
#define O_ENTS 0x4
#define O_ENTLISTS 0x2b8

//POINTERS
#define P_WORLD 0x7FE944
#define P_PY_MODS 0x79C698
#define P_CON_HANDLER 0x402190
#define P_SCRAP_LOG 0x4134C0
#define P_SCRAP_EXEC 0x5a8390
#define P_SCRAP_EXIT 0x4010c0

//FUNCTION TYPES
#define T_SCRAP_LOG int(_cdecl *)(unsigned int, const char *)
#define T_SCRAP_EXEC int(_cdecl *)(const char *)

auto scrap_log = (T_SCRAP_LOG)P_SCRAP_LOG;
auto scrap_exec = (T_SCRAP_EXEC)P_SCRAP_EXEC;
