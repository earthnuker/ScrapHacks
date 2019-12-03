#pragma once
#include <Windows.h>

#include <regex>
#include <sstream>

#include "Scrapland.hpp"
#include "Util.hpp"

void DllUnload();


void unhook_d3d8();
void hook_d3d8();

typedef void(_cdecl *t_cmd_func)(vector<string>);

struct t_cmd {
    t_cmd_func func;
    const char* usage;
    const char* doc;
};

void cmd_help(vector<string>);

DWORD
get_protection(void *addr) {
    MEMORY_BASIC_INFORMATION mbi;
    VirtualQuery(addr, &mbi, sizeof(mbi));
    return mbi.Protect;
}

void cmd_write(vector<string> args) {
    MEMORY_BASIC_INFORMATION mbi;
    if (args.size() != 2) {
        scrap_log(ERR_COLOR, "Usage: $w <addr> <data(hex)>\n");
        return;
    }
    void *addr = 0;
    vector<uint8_t> data;
    try {
        addr = (void *)stoull(args[0], 0, 16);
        data = fromhex(args[1]);
    } catch (exception e) {
        scrap_log(ERR_COLOR, "ERROR!\n");
        return;
    }
    uint8_t *buffer = new uint8_t[data.size()];
    size_t idx = 0;
    for (uint8_t v : data) {
        buffer[idx++] = v;
    }
    cout << "W:" << (void *)addr << endl;
    cout << buffer << endl;
    if (VirtualQuery(addr, &mbi, sizeof(mbi)) == 0) {
        scrap_log(ERR_COLOR, "ERROR!\n");
        return;
    };
    VirtualProtect(mbi.BaseAddress, mbi.RegionSize, PAGE_EXECUTE_READWRITE,
                   &mbi.Protect);
    memcpy(addr, buffer, data.size());
    VirtualProtect(mbi.BaseAddress, mbi.RegionSize, mbi.Protect, NULL);
    if (buffer) {
        free(buffer);
    }
    return;
}

void cmd_read(vector<string> args) {
    MEMORY_BASIC_INFORMATION mbi;
    if (args.size() != 2) {
        scrap_log(ERR_COLOR, "Usage: $r <addr> <size>\n");
        return;
    }
    uintptr_t addr = UINTPTR_MAX;
    size_t size = 0;
    unsigned char *buffer;
    try {
        addr = stoull(args[0], 0, 16);
        size = stoull(args[1]);
        buffer = new unsigned char[size];
    } catch (exception e) {
        scrap_log(ERR_COLOR, "ERROR!\n");
        return;
    }
    void *mptr = reinterpret_cast<void *>(addr);
    if (VirtualQuery(mptr, &mbi, sizeof(mbi)) == 0) {
        scrap_log(ERR_COLOR, "ERROR!\n");
        return;
    };
    VirtualProtect(mbi.BaseAddress, mbi.RegionSize, PAGE_EXECUTE_READWRITE,
                   &mbi.Protect);
    string hxd = hexdump_s(mptr, size);
    scrap_log(INFO_COLOR, hxd.c_str());
    VirtualProtect(mbi.BaseAddress, mbi.RegionSize, mbi.Protect, NULL);
    if (buffer) {
        free(buffer);
    }
    return;
}

void cmd_dx8(vector<string> args) {
    if (args.size()!=1) {
        scrap_log(ERR_COLOR, "Usage: $dx8 (hook|unhook)\n");
        return;
    }
    if (args[0]=="hook") {
        hook_d3d8();
        scrap_log(INFO_COLOR,"DX8 hooked!\n");
        return;
    }
    if (args[0]=="unhook") {
        unhook_d3d8();
        scrap_log(INFO_COLOR,"DX8 unhooked!\n");
        return;
    };
    scrap_log(ERR_COLOR,"Invalid argument!\n");
    return;
}

void cmd_dump_py(vector<string> args) {
    stringstream out;
    for (auto mod : Py) {
        for (auto meth : mod.second.methods) {
            out << mod.first << "." << meth.first << " @ "
                    << meth.second->ml_meth << endl;
        }
    }
    scrap_log(INFO_COLOR,out.str().c_str());
}

void cmd_dump_ents(vector<string> args) {
    stringstream out;
    out << "Entities:" << endl;
    dump_ht(ptr<HashTable<Entity>>(P_WORLD, O_ENTS), &out);
    out << "Entity Lists:" << endl;
    dump_ht(ptr<HashTable<EntityList>>(P_WORLD, O_ENTLISTS), &out);
    scrap_log(INFO_COLOR,out.str().c_str());
    return;
}

void cmd_toggle_overlay(vector<string> args) {
    overlay=!overlay;
    if (overlay) {
        scrap_log(INFO_COLOR,"Overlay enabled!\n");
    } else {
        scrap_log(INFO_COLOR,"Overlay disabled!\n");
    }
}

void cmd_print_alarm(vector<string> args) {
    stringstream out;
    float *alarm = ptr<float>(P_WORLD, O_ALARM);
    float *alarm_grow = ptr<float>(P_WORLD, O_ALARM_GROW);
    out << "Alarm: " << alarm[0] << " + " << alarm_grow[0] << endl;
    scrap_log(INFO_COLOR,out.str().c_str());
    return;
}

void cmd_unload(vector<string> args) { 
    scrap_log(INFO_COLOR,"Unloading ScrapHacks... bye!\n");
    DllUnload(); 
}

static map<string, t_cmd> commands = {
    {"w", {
        cmd_write,
        "Usage: $w <addr> <data(hex)>",
        "Write memory"
    }},
    {"r", {
        cmd_read,
        "Usage: $r <addr> <num_bytes>",
        "Read memory"
    }},
    {"unload", {
        cmd_unload,
        "Usage: $unload",
        "Unload ScrapHacks"
    }},
    {"dx8", {
        cmd_dx8,
        "Usage: $dx8 (hook|unhook)",
        "Hook/Unhook DirectX 8 functions"
    }},
    {"dump_py",{
        cmd_dump_py,
        "Usage: $dump_py",
        "Dump python modules to console"
    }},
    {"overlay",{
        cmd_toggle_overlay,
        "Usage: $overlay",
        "Toggle DX8 Overlay"
    }},
    {"alarm",{
        cmd_print_alarm,
        "Usage: $alarm",
        "Print alarm status"
    }},
    {"ents",{
        cmd_dump_ents,
        "Usage: $ents",
        "Dump entity information"
    }},
    {"help", {
        cmd_help,
        "Usage: $help [command]",
        "Print help for ScrapHacks command"}},
};


void cmd_help(vector<string> args) {
    if (args.size()!=1) {
        for (auto cmd: commands) {
            scrap_log(INFO_COLOR,cmd.first.c_str());
            scrap_log(INFO_COLOR,": ");
            scrap_log(INFO_COLOR,cmd.second.doc);
            scrap_log(INFO_COLOR,"\n");
        }
        return;
    }
    if (!commands.count(args[0])) {
        scrap_log(ERR_COLOR, "Unknown command '");
        scrap_log(ERR_COLOR, args[0].c_str());
        scrap_log(ERR_COLOR, "'!\n");
        return;
    }
    t_cmd cmd=commands[args[0]];
    scrap_log(INFO_COLOR,args[0].c_str());
    scrap_log(INFO_COLOR,": ");
    scrap_log(INFO_COLOR,cmd.usage);
    scrap_log(INFO_COLOR,"\n\t");
    scrap_log(INFO_COLOR,cmd.doc);
    scrap_log(INFO_COLOR,"\n");
    return;
}


void handle_command(const char *_cmd) {
    scrap_log(ERR_COLOR, "$");
    scrap_log(ERR_COLOR, _cmd);
    scrap_log(ERR_COLOR, "\n");
    cout << "CMD: '" << _cmd << "'" << endl;
    vector<string> cmd = split(string(_cmd), ' ');
    if (cmd.size() == 0) {
        return;
    }
    if (commands.count(cmd[0])) {
        string command = cmd[0];
        cmd.erase(cmd.begin());
        commands[command].func(cmd);
    } else {
        scrap_log(ERR_COLOR, "Unknown command '");
        scrap_log(ERR_COLOR, cmd[0].c_str());
        scrap_log(ERR_COLOR, "'!\n");
    }
    return;
}