#include <sstream>
#include <regex>
#include <Windows.h>
#include "Util.h"

DWORD get_protection(void *addr)
{
    MEMORY_BASIC_INFORMATION mbi;
    VirtualQuery(addr, &mbi, sizeof(mbi));
    return mbi.Protect;
}

void handle_command(const char *_cmd)
{
    cout<<"CMD: '"<<_cmd<<"'"<<endl;
    vector<string> cmd = split(string(_cmd), ' ');
    cout<<"PARTS: ";
    for (string c:cmd) {
        cout<<"'"<<c<<"' ";
    }
    cout<<endl;
    if (cmd.size() == 0)
    {
        cout<<"EMPTY!"<<endl;
        return;
    }
    scrap_log(0x00ff00,_cmd);
    scrap_log(0x00ff00,"\n");
    if (cmd[0] == "r")
    {
        if (cmd.size()!=2) {
            scrap_log(0xff0000, "Usage: $r <addr> [size]\n");
            return;
        }
        scrap_log(0xff0000, "READ!\n");
        cout<<"READ!"<<endl;
    }
    else if (cmd[0] == "w")
    {
        if (cmd.size()!=2) {
            scrap_log(0xff0000, "Usage: $w <addr> <hex_data>\n");
            return;
        }
        scrap_log(0xff0000, "WRITE!\n");
        cout<<"WRITE!"<<endl;
    }
    else
    {
        scrap_log(0xff0000, "Unknown command!\n");
    }

    scrap_log(0x00ff00, "HAXX\n");
    return;
}