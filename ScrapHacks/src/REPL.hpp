#pragma once
#include <Windows.h>
#include <DbgHelp.h>

#define ASMJIT_EMBED
#define ASMTK_EMBED

#include <regex>
#include <sstream>
#include <string>

#include <asmtk/asmtk.h>
#include <Zydis/Zydis.h>
#include "Scrapland.hpp"
#include "Util.hpp"

void DllUnload();


void unhook_d3d8();
void hook_d3d8();

struct Command;

typedef void(_cdecl *t_cmd_func)(Command*,vector<string>);

size_t assemble(vector<string> assembly,uint64_t base) {
    using namespace asmjit;
    using namespace asmtk;

    char err_msg[1024];
    Error err;
    
    CodeInfo ci(ArchInfo::kIdX86);
    ci.setBaseAddress(base);
    CodeHolder code;
    code.init(ci);
    x86::Assembler a(&code);
    AsmParser p(&a);
    
    for (string line:assembly) {
        if (err = p.parse((line+"\n").c_str())) {
            snprintf(err_msg,1024,"PARSE ERROR: [%s] %08x (%s)\n",line.c_str(), err, DebugUtils::errorAsString(err));
            cerr<<err_msg<<endl;
            scrap_log(ERR_COLOR,err_msg);
            return 0;
        }
    }
    if (err=code.flatten()) {
        snprintf(err_msg,1024,"FLATTEN ERROR: %08x (%s)\n", err, DebugUtils::errorAsString(err));
        cerr<<err_msg<<endl;
        scrap_log(ERR_COLOR,err_msg);
        return 0;
    }
    if (err=code.resolveUnresolvedLinks()) {
        snprintf(err_msg,1024,"RESOLVE ERROR: %08x (%s)\n", err, DebugUtils::errorAsString(err));
        cerr<<err_msg<<endl;
        scrap_log(ERR_COLOR,err_msg);
        return 0;
    }
    CodeBuffer& buffer = code.sectionById(0)->buffer();
    
    if (base==0) {
        return buffer.size();
    }

    MEMORY_BASIC_INFORMATION mbi;
    
    if (VirtualQuery((void*)base, &mbi, sizeof(mbi)) == 0) {
        cerr<<"ERROR: "<< GetLastErrorAsString() <<endl;
        scrap_log(ERR_COLOR, "ERROR: ");
        scrap_log(ERR_COLOR, GetLastErrorAsString());
        scrap_log(ERR_COLOR, "\n");
        return 0;
    };
    if (!VirtualProtect(mbi.BaseAddress, mbi.RegionSize, PAGE_EXECUTE_READWRITE, &mbi.Protect))
    {
        cerr<<"ERROR: "<< GetLastErrorAsString() <<endl;
        scrap_log(ERR_COLOR, "ERROR: ");
        scrap_log(ERR_COLOR, GetLastErrorAsString());
        scrap_log(ERR_COLOR, "\n");
        return 0;
    };
    cout<<"CODE: "<< hexdump_s((void*)base,buffer.size()) << endl;
    memcpy((void*)base,buffer.data(),buffer.size());
    scrap_log(INFO_COLOR,"Code:"+hexdump_s((void*)base,buffer.size()));
    VirtualProtect(mbi.BaseAddress, mbi.RegionSize, mbi.Protect, NULL);
    return buffer.size();
}

size_t asm_size(vector<string> assembly) {
    return assemble(assembly,0);
}

string disassemble(void* addr, size_t num,bool compact) {
    stringstream ret;
    ZyanU64 z_addr = reinterpret_cast<uintptr_t>(addr);
    ZydisDecoder decoder;
    ZydisFormatter formatter;
    ZydisDecoderInit(&decoder, ZYDIS_MACHINE_MODE_LONG_COMPAT_32, ZYDIS_ADDRESS_WIDTH_32);
    ZydisFormatterInit(&formatter, ZYDIS_FORMATTER_STYLE_INTEL);
    
    ZydisDecodedInstruction instruction;
    while (ZYAN_SUCCESS(ZydisDecoderDecodeBuffer(&decoder, addr, -1, &instruction)))
    {
        char buffer[256];
        ZydisFormatterFormatInstruction(&formatter, &instruction, buffer, sizeof(buffer), z_addr);
        if (!compact) {
            ret<< "[" << std::hex << setfill('0') << setw(8) << z_addr << "]: ";
        }

        ret << buffer;
        
        if (compact) {
            ret<<"; ";
        } else {
            ret<<endl;
        }
        addr = reinterpret_cast<void*>(z_addr += instruction.length);
        num--;
        if (num==0) {
            break;
        }
    }
    return ret.str();
}

struct Command {
    t_cmd_func func;
    string usage;
    string doc;
    map<string,Command*> subcommands;


    Command(t_cmd_func func=nullptr,string usage="",string doc="",map<string,Command*> subcommands={}) {
        this->func=func;
        this->usage=usage;
        this->doc=doc;
        this->subcommands=subcommands;
    }

    
    Command(string usage="",string doc="",map<string,Command*> subcommands={}): 
        Command(nullptr,usage,doc,subcommands) {};

    void add_subcommand(string name,Command *cmd) {
        this->subcommands[name]=cmd;
    }

    void set_subcommands(const map<string,Command*> &subcommands) {
        for (auto subcmd:subcommands) {
            this->add_subcommand(subcmd.first,subcmd.second);
        }
    }

    bool has_subcommand(string cmd) {
        return this->subcommands.count(cmd)>0;
    }

    void exec(vector<string> args) {
        if (args.size()>1) {
            string cmd=args[0];
            if (this->has_subcommand(cmd)) {
                // matching subcommand found, strip first part and forward args
                args.erase(args.begin());
                return this->subcommands[cmd]->exec(args);
            };
        }
        // args vector empty or no subcommand found, check if we have a func ptr and call it
        if (this->func!=nullptr) {
            this->func(this,args);
            return;
        }
        scrap_log(ERR_COLOR, "Unknown command!\n");
        return;
    }

};

struct REPL {
    
    map<string,Command*> commands;
    REPL(map<string,Command*> commands) {
        this->commands=commands;
    }

    bool has_command(string cmd) {
        return this->commands.count(cmd)>0;
    }

    bool exec(vector<string> args) {
        vector<tuple<string,Command*>> cmd_stack;
        map<string,Command*> cmds=this->commands;
        if (args.size()==0) {
            return false;
        }
        while (cmds.count(args[0])) {
            cmd_stack.push_back(make_tuple(args[0],cmds[args[0]]));
            cmds=cmds[args[0]]->subcommands;
            args.erase(args.begin());
            if (args.empty()) break;
        }
        while (cmd_stack.size()) {
            auto elem=cmd_stack.back();
            string cmd=get<0>(elem);
            Command* cmd_ptr=get<1>(elem);
            cmd_stack.pop_back();
            if (cmd_ptr->func!=nullptr) {
                cmd_ptr->func(cmd_ptr,args);
                return true;
            }
            args.insert(args.begin(),cmd);
        }
        return false;
    }

    string help(vector<string> args) {
        map<string,Command*> cmds=this->commands;
        string ret;
        if (args.empty()) {
            return this->show_commands(cmds);
        }
        pair<string,Command*> cmd=make_pair("",nullptr);
        for (string part: args) {
            if (cmds.count(part)==0) {
                return "No help for (sub)command '"+part+"'";
            }
            cmd=make_pair(part,cmds[part]);
            cmds=cmd.second->subcommands;
        }
        ret=cmd.first+": "+cmd.second->usage+"\n";
        if (cmds.size()) {
            ret+="Subcommands:\n"+this->show_commands(cmds,1)+"\n";
        };
        return ret;
    }

    string show_commands(map<string,Command*> cmds,size_t depth=0) {
        string s;
        for (auto cmd:cmds) {
            for (size_t n=0;n<depth;++n) {
                s+="    ";
            }
            s+=cmd.first+": "+cmd.second->doc+" ("+cmd.second->usage+")\n"+this->show_commands(cmd.second->subcommands,depth+1);
        }
        return s;
    }

};

DWORD
get_protection(void *addr) {
    MEMORY_BASIC_INFORMATION mbi;
    VirtualQuery(addr, &mbi, sizeof(mbi));
    return mbi.Protect;
}

void cmd_disassemble(Command* cmd, vector<string> args) {
    MEMORY_BASIC_INFORMATION mbi;
    if (args.size()<1) {
        scrap_log(ERR_COLOR, cmd->usage);
        scrap_log(ERR_COLOR, "\n");
        return;
    }
    uintptr_t addr = UINTPTR_MAX;
    size_t size = 0xff;
    try {
        addr = stoull(args[0], 0, 16);
        if (args.size()>1) {
            size = stoull(args[1]);
        }
    } catch (exception e) {
        scrap_log(ERR_COLOR, "ERROR: ");
        scrap_log(ERR_COLOR, e.what());
        scrap_log(ERR_COLOR, "\n");
        return;
    }
    void *mptr = reinterpret_cast<void *>(addr);
    if (VirtualQuery(mptr, &mbi, sizeof(mbi)) == 0) {
        scrap_log(ERR_COLOR, "ERROR: ");
        scrap_log(ERR_COLOR, GetLastErrorAsString());
        scrap_log(ERR_COLOR, "\n");
        return;
    };
    if (!VirtualProtect(mbi.BaseAddress, mbi.RegionSize, PAGE_EXECUTE_READWRITE,
                   &mbi.Protect)) {
        scrap_log(ERR_COLOR, "ERROR: ");
        scrap_log(ERR_COLOR, GetLastErrorAsString());
        scrap_log(ERR_COLOR, "\n");
        return;
    };
    string dasm = disassemble(mptr, size, false);
    scrap_log(INFO_COLOR, dasm);
    VirtualProtect(mbi.BaseAddress, mbi.RegionSize, mbi.Protect, NULL);
    return;
}

void cmd_exec(Command* cmd, vector<string> args) {
    void *addr;
    MEMORY_BASIC_INFORMATION mbi;
    if (args.size()<1) {
        scrap_log(ERR_COLOR, cmd->usage);
        scrap_log(ERR_COLOR, "\n");
    }
    try {
        addr = (void *)stoull(args[0], 0, 16);
    } catch (exception e) {
        scrap_log(ERR_COLOR, "ERROR: ");
        scrap_log(ERR_COLOR, e.what());
        scrap_log(ERR_COLOR, "\n");
        return;
    }
    
    if (VirtualQuery(addr, &mbi, sizeof(mbi)) == 0) {
        scrap_log(ERR_COLOR, "ERROR: ");
        scrap_log(ERR_COLOR, GetLastErrorAsString());
        scrap_log(ERR_COLOR, "\n");
        return;
    };
    if (!VirtualProtect(mbi.BaseAddress, mbi.RegionSize, PAGE_EXECUTE_READWRITE, &mbi.Protect))
    {
        scrap_log(ERR_COLOR, "ERROR: ");
        scrap_log(ERR_COLOR, GetLastErrorAsString());
        scrap_log(ERR_COLOR, "\n");
    };
    CreateThread(NULL,0,(LPTHREAD_START_ROUTINE)addr,0,NULL,NULL);
}

void cmd_write(Command* cmd,vector<string> args) {
    MEMORY_BASIC_INFORMATION mbi;
    if (args.size()==0) {
        scrap_log(ERR_COLOR, cmd->usage);
        scrap_log(ERR_COLOR, "\n");
        return;
    }
    uint8_t *buffer = nullptr;
    vector<uint8_t> data;
    try {
        if (args.size()>1) {
            buffer = (uint8_t *)stoull(args[0], 0, 16);
            data = fromhex(args[1]);
        } else {
            data = fromhex(args[0]);
            buffer = new uint8_t[data.size()];
            if (buffer==nullptr) {
                scrap_log(ERR_COLOR, "ERROR: ");
                scrap_log(ERR_COLOR, "new[] failed");
                scrap_log(ERR_COLOR, "\n");
                return;
            }
            char ptr[255];
            snprintf(ptr,255,"Buffer @ %p\n",buffer);
            scrap_log(INFO_COLOR,ptr);
        }
    } catch (exception e) {
        scrap_log(ERR_COLOR, "ERROR: ");
        scrap_log(ERR_COLOR, e.what());
        scrap_log(ERR_COLOR, "\n");
        return;
    }
    if (VirtualQuery(buffer, &mbi, sizeof(mbi)) == 0) {
        scrap_log(ERR_COLOR, "ERROR: ");
        scrap_log(ERR_COLOR, GetLastErrorAsString());
        scrap_log(ERR_COLOR, "\n");
        return;
    };
    if (!VirtualProtect(mbi.BaseAddress, mbi.RegionSize, PAGE_EXECUTE_READWRITE, &mbi.Protect))
    {
        scrap_log(ERR_COLOR, "ERROR: ");
        scrap_log(ERR_COLOR, GetLastErrorAsString());
        scrap_log(ERR_COLOR, "\n");
    };
    
    size_t idx = 0;
    for (uint8_t v : data) {
        buffer[idx++] = v;
    }

    VirtualProtect(mbi.BaseAddress, mbi.RegionSize, mbi.Protect, NULL);
    return;
}

void cmd_read(Command* cmd,vector<string> args) {
    MEMORY_BASIC_INFORMATION mbi;
    if (args.size()<1) {
        scrap_log(ERR_COLOR, cmd->usage);
        scrap_log(ERR_COLOR, "\n");
        return;
    }
    uintptr_t addr = UINTPTR_MAX;
    size_t size = 0xff;
    unsigned char *buffer;
    try {
        addr = stoull(args[0], 0, 16);
        if (args.size()>1) {
            size = stoull(args[1]);
        }
        buffer = new unsigned char[size];
    } catch (exception e) {
        scrap_log(ERR_COLOR, "ERROR: ");
        scrap_log(ERR_COLOR, e.what());
        scrap_log(ERR_COLOR, "\n");
        return;
    }
    void *mptr = reinterpret_cast<void *>(addr);
    if (VirtualQuery(mptr, &mbi, sizeof(mbi)) == 0) {
        scrap_log(ERR_COLOR, "ERROR: ");
        scrap_log(ERR_COLOR, GetLastErrorAsString());
        scrap_log(ERR_COLOR, "\n");
        return;
    };
    if (!VirtualProtect(mbi.BaseAddress, mbi.RegionSize, PAGE_EXECUTE_READWRITE,
                   &mbi.Protect)) {
        scrap_log(ERR_COLOR, "ERROR: ");
        scrap_log(ERR_COLOR, GetLastErrorAsString());
        scrap_log(ERR_COLOR, "\n");
        return;
    };
    string hxd = hexdump_s(mptr, size);
    scrap_log(INFO_COLOR, hxd);
    VirtualProtect(mbi.BaseAddress, mbi.RegionSize, mbi.Protect, NULL);
    if (buffer) {
        free(buffer);
    }
    return;
}

void cmd_hook_dx8(Command* cmd,vector<string> args) {
    hook_d3d8();
    scrap_log(INFO_COLOR,"DX8 hooked!\n");
    return;
}

void cmd_unhook_dx8(Command* cmd,vector<string> args) {
    unhook_d3d8();
    scrap_log(INFO_COLOR,"DX8 unhooked!\n");
    return;
}


void cmd_dx8(Command* cmd,vector<string> args) {
    if (args.size()!=1) {
        scrap_log(ERR_COLOR, cmd->usage);
        scrap_log(ERR_COLOR, "\n");
        return;
    }
     if (args[0]=="zenable:true") {
        use_z=true;
        scrap_log(INFO_COLOR,"DX8 mode switched!\n");
        return;
    };
    if (args[0]=="zenable:false") {
        use_z=false;
        scrap_log(INFO_COLOR,"DX8 mode switched!\n");
        return;
    };
    
    if (args[0]=="fill:wire") {
        fillmode=D3DFILLMODE::D3DFILL_WIREFRAME;
        scrap_log(INFO_COLOR,"DX8 mode switched!\n");
        return;
    };
    
    if (args[0]=="fill:solid") {
        fillmode=D3DFILLMODE::D3DFILL_SOLID;
        scrap_log(INFO_COLOR,"DX8 mode switched!\n");
        return;
    };
    
    if (args[0]=="fill:point") {
        fillmode=D3DFILLMODE::D3DFILL_POINT;
        scrap_log(INFO_COLOR,"DX8 mode switched!\n");
        return;
    };
    scrap_log(ERR_COLOR,"Invalid argument!\n");
    return;
}

void cmd_dump_stack(Command* cmd, vector<string> args) {
    stringstream ret;
    void** stack=(void**)_AddressOfReturnAddress();
    cout<<"ESP:    "<<stack<<endl;
    for (size_t n=0;n<0x100;++n) {
        if (!addr_exists(stack[n])) {
            continue;
        }
        bool r,w,x;
        char R=(r=can_read(stack[n])) ? 'R' : ' ';
        char W=(w=can_write(stack[n])) ? 'W' : ' ';
        char X=(x=can_execute(stack[n])) ? 'X' : ' ';
        ret<< std::hex << setfill('0') << setw(8) << stack+(n*sizeof(void*)) << ": "<<stack[n]<<" "<<R<<W<<X;
        if (r && !x) {
            ret<<" [ "<<hexdump_s(stack[n],0xf,true)<<"]";
        } else if (r && x) {
            ret<<" [ "<<disassemble(stack[n],5,true)<<"]";
        }
        ret<<endl;
    }
    scrap_log(INFO_COLOR,ret.str());
    return;
}

void cmd_dump_py(Command* cmd,vector<string> args) {
    stringstream out;
    for (auto mod : Py) {
        for (auto meth : mod.second.methods) {
            out << mod.first << "." << meth.first << " @ "
                    << meth.second->ml_meth << endl;
        }
    }
    scrap_log(INFO_COLOR,out.str());
}

void cmd_dump_vars(Command* cmd, vector<string> args) {
    stringstream out;
    GameVar* var=ptr<GameVar>(P_VARS,0);
    out << "GameVars:" << endl;
    while (var!=nullptr) {
        out<<var->name<< "[" <<std::hex <<(uint16_t)var->type <<","<< (uint16_t)var->subtype << std::dec << "]: " << var->desc<<" ("<<var->value<<", "<<var->default<<")"<<endl;
        var=var->next;
    }
    scrap_log(INFO_COLOR,out.str());
}

void cmd_dump_ents(Command* cmd,vector<string> args) {
    stringstream out;
    out << "Entities:" << endl;
    dump_ht(ptr<HashTable<Entity>>(P_WORLD, O_ENTS), &out);
    out << "Entity Lists:" << endl;
    dump_ht(ptr<HashTable<EntityList>>(P_WORLD, O_ENTLISTS), &out);
    scrap_log(INFO_COLOR,out.str());
    return;
}

void cmd_toggle_overlay(Command* cmd,vector<string> args) {
    if (!hooked) {
        scrap_log(INFO_COLOR,"DX8 not hooked, run '$dx8 hook' first!\n");
        return;
    }
    overlay=!overlay;
    if (overlay) {
        scrap_log(INFO_COLOR,"Overlay enabled!\n");
    } else {
        scrap_log(INFO_COLOR,"Overlay disabled!\n");
    }
}

void cmd_enable_overlay(Command* cmd,vector<string> args) {
    if (!overlay) {
        cmd_toggle_overlay(cmd,args);
    }
}

void cmd_disable_overlay(Command* cmd,vector<string> args) {
    if (overlay) {
        cmd_toggle_overlay(cmd,args);
    }
}


void cmd_print_alarm(Command* cmd,vector<string> args) {
    stringstream out;
    float alarm = ptr<float>(P_WORLD, O_ALARM)[0];
    float alarm_grow = ptr<float>(P_WORLD, O_ALARM_GROW)[0];
    if (alarm_grow<0) {
        out << "Alarm: " << alarm << " - " << alarm_grow << endl;
    } else {
        out << "Alarm: " << alarm << " + " << alarm_grow << endl;
    }
    scrap_log(INFO_COLOR,out.str());
    return;
}

void cmd_unload(Command* cmd,vector<string> args) { 
    scrap_log(INFO_COLOR,"Unloading ScrapHacks... bye!\n");
    DllUnload(); 
}

void cmd_asm(Command* cmd, vector<string> args) {
    string code;
    uintptr_t buffer_addr;
    bool has_addr=false;
    if (args.size()<1) {
        scrap_log(ERR_COLOR, cmd->usage);
        return;
    }
    try {
        buffer_addr=stoull(args[0], 0, 16);
        has_addr=true;
    } catch (exception e) {
        // NOP
        has_addr=false;
    }
    if (has_addr) {
        // remove address from args
        args.erase(args.begin());
    }
    for (string arg:args) {
        code+=arg+" ";
    };
    size_t data_size=asm_size(split(code,';'));
    if (!has_addr) {
        buffer_addr = (uintptr_t)malloc(data_size);
        if (buffer_addr==0) {
            scrap_log(ERR_COLOR, "ERROR: ");
            scrap_log(ERR_COLOR, "malloc() failed");
            scrap_log(ERR_COLOR, "\n");
            return;
        }
        char ptr[255];
        snprintf(ptr,255,"Buffer @ %p\n",(void*)buffer_addr);
        scrap_log(INFO_COLOR,ptr);
    }
    assemble(split(code,';'),buffer_addr);
}


void cmd_help(Command* cmd,vector<string> args);

static REPL* repl=new REPL(
{
    {"mem",new Command("Usage: $mem (read|write)","Manipulate memory",{
        {"read",new Command(cmd_read,"Usage: $mem read <addr> [size]","Read memory")},
        {"write",new Command(cmd_write,"Usage: $mem write [addr] <data(hex)>","Write memory, if no address is specifiew we VirtualAlloc() a region")},
        {"exec",new Command(cmd_exec,"Usage: $exec <addr>","Start a new thread at the specified address")},
        {"asm",new Command(cmd_asm,"Usage: $asm [addr] <inst1>;<inst2>;...","Assemble instructions at address, if no address is given allocate memory and assemble code into that")},
        {"stack",new Command(cmd_dump_stack,"Usage: $mem stack","Dump stack contents")},
        {"dasm",new Command(cmd_disassemble,"Usage: $mem dasm <addr> [num_inst]","Disassemble memory at address")},
    })},
    {"unload",new Command(cmd_unload,"Usage: $unload","Unload ScrapHacks")},
    {"dx8",new Command(cmd_dx8,"Usage: $dx8 <subcommand>","Manipulate DirectX 8 functions and state",{
        {"overlay",new Command("Usage: $dx8 overlay <subcommand>","Control DX8 overlay",{
            {"toggle",new Command(cmd_toggle_overlay,"Usage: $dx8 overlay toggle","Toggle overlay")},
            {"enable",new Command(cmd_enable_overlay,"Usage: $dx8 overlay enable","Enable overlay")},
            {"disable",new Command(cmd_disable_overlay,"Usage: $dx8 overlay disable","Disable overlay")},
        })},
        {"hook",new Command(cmd_hook_dx8,"Usage: $dx8 hook","Enable DirectX 8 hook")},
        {"unhook",new Command(cmd_unhook_dx8,"Usage: $dx8 hook","Disable DirectX 8 hook")}
    })},
    {"dump",new Command("Usage: $dump <subcommand>","Dump various data to the console",{
        {"py",new Command(cmd_dump_py,"Usage: $dump py","Dump python module information")},
        {"ents",new Command(cmd_dump_ents,"Usage: $dump ents","Dump entity information")},
        {"alarm",new Command(cmd_print_alarm,"Usage: $dump alarm","Print alarm status")},
        {"vars",new Command(cmd_dump_vars,"Usage: $dump vars","Print engine variables")},
    })},
    {"help",new Command(cmd_help,"Usage: $help [command]","Print help for ScrapHacks command")}
});

void cmd_help(Command* cmd,vector<string> args) {
    scrap_log(INFO_COLOR,repl->help(args)+"\n");
};

void handle_command(const char *_cmd) {
    scrap_log(ERR_COLOR, "$");
    scrap_log(ERR_COLOR, _cmd);
    scrap_log(ERR_COLOR, "\n");
    cout << "CMD: '" << _cmd << "'" << endl;
    repl->exec(split(string(_cmd), ' '));
    return;
}