import r2pipe
import os
import json
from datetime import datetime
import subprocess as SP
from tqdm import tqdm
from pprint import pprint
import os
import sys

r2cmds = []
x64_dbg_script=[]
scrap_exe = os.path.abspath(sys.argv[1])
folder = os.path.abspath(os.path.dirname(scrap_exe))
script_path=os.path.join(folder, "scrap_dissect.r2")
x64_dbg_script_path=os.path.join(folder, "scrap_dissect.x32dbg.txt")
json_path=os.path.join(folder, "scrap_dissect.json")

assert os.path.isfile(scrap_exe), "File not found!"
r2 = r2pipe.open(scrap_exe)
file_hashes = r2.cmdj("itj")
target_hashes = {
    "sha1": "d2dde960e8eca69d60c2e39a439088b75f0c89fa",
    "md5": "a934c85dca5ab1c32f05c0977f62e186",
}

assert file_hashes == target_hashes, "Hash mismatch"

def x64_dbg_label(addr,name,prefix=None):
    global x64_dbg_script
    if isinstance(addr,int):
        addr=hex(addr)
    if prefix:
        x64_dbg_script.append(f'lbl {addr},"{prefix}.{name}"')
    else:
        x64_dbg_script.append(f'lbl {addr},"{name}"')

def r2_cmd(cmd):
    global r2, r2cmds
    r2cmds.append(cmd)
    return r2.cmd(cmd)


def r2_cmdj(cmd):
    global r2, r2cmds
    r2cmds.append(cmd)
    return r2.cmdj(cmd)


def r2_cmdJ(cmd):
    global r2, r2cmds
    r2cmds.append(cmd)
    return r2.cmdJ(cmd)

t_start=datetime.today()

def analysis(full=False):
    print("[*] Running analysis")
    steps=[]
    if full:
        steps=[
            "e anal.dataref = true",
            # "e anal.esil = true",
            "e anal.jmp.after = true",
            "e anal.jmp.indir = true",
            "e anal.loads = true",
            "e anal.pushret = true",
            "e anal.refstr = true",
            "e anal.strings = true",
            "e anal.vinfun = true",
            "e asm.anal = true",
        ]
    steps+=["aaaaa"]
    for ac in steps:
        print(f"[*] Running '{ac}'")
        r2_cmd(f"{ac} 2>NUL")
    
# 0x7fac20
# 0x7fac19
# 0x7faa4c
# 0x7fac1c # activate viewer
# 0x84d400 # lib preloaded

# 0x413ee0

# 0x7d2094 refcnt

comments= {
    0x6113f9:"Check if Window exists"
}

flags = {
    0x7FE944: "P_World", 
    0x7FBE4C: "P_Vars", 
    0x79C698: "Py_Mods", 
    0x852914: "P_D3D8_Dev", 
    0x7FCC00: "N_Paks_opened", 
    0x7fcbec: "Hash_Index_Size", 
    0x7fcbf0: "P_Hash_Index", 
    0x7fcc08: "Lst_File", 
    0x7fcc04: "Pak_Locked", 
    0x7fc1b0: "Pak_Index", 
    0x84cb64: "P_ConHandler", 
    0x801e10: "num_arrows", 
    0x7fac84: "P_Callbacks", 
    0x80b2cc: "P_ActClassList", 
    0x807a20: "P_Scorer", 
    0x80a398: "P_SoundSys", 
    0x84cb58: "H_RichEd",
    0x84cb4c: "P_HWND_Console",
    0x80cb40: "Console_Win_Buffer",
    0x84d400: "Lib_preloaded",
    0x7fac1c: "Activate_Viewer",
    0x8b18f0: "P_Models",
    0x8b18f4: "P_Scenes",
    0x8b18f8: "P_ActiveModels",
    0x803bc0: "net_is_server",
    0x8045e4: "net_is_master",
    0x8038a8: "net_is_client",
    0x7fadd8: "is_python",
    0x7fc084: "pak_lock",
    0x7fbe7c: "current_language",
}

VMTs = {
    0x78d4d8: "Py_entity",
    0x78cc6c: "World",
    0x78b680: "FilePak_1",
    0x78b6a4: "FilePak_2",
    0x78b638: "AbstractFile",
    0x78b4d8: "App",
    0x78b480: "Window",
    0x78b5c0: "File",
    0x78b65c: "FileMem",
    0x78b6d0: "IDevice_1",
    0x78b6f4: "IDevice_2",
    0x78b6fc: "IDevice_Kb",
    0x78b720: "IDevice_Mouse",
    0x78b74c: "IDevice_Joy",
    0x7933ac: "3d_Gfx",
    0x7933a0: "NodeFX",
}

types = [
    "struct PyMethodDef { char *ml_name; void *ml_meth; int ml_flags; char *ml_doc;};",
    "struct GameVar { struct GameVar* next; const char* name; const char* desc; uint64_t d_type; void* value; void* def_value; };",
    "struct HT_Entry { void* data; const char* key; struct HT_Entry* next;};",
    "struct PakEntry { unsigned char* filename; bool locked; void* data; uint32_t seek;};",
    "struct HashIndexEntry { uint32_t offset; uint32_t size; uint32_t status; const char* name; struct HashIndexEntry* next; };",
    "struct HashIndex { uint32_t size; struct HashIndexEntry** data; };",
    "struct HashTableEntry { void* data; const char *key; struct HashTableEntry* next; };",
    "struct HashTable { uint32_t size; struct HashTableEntry** data; };",
]

func_sigs = {
    0x5A8390: "int py_exec(const char* script);",
    0x5BB9D0: "int PyArg_ParseTuple(void* PyObj, char* format, ...);",
    0x413ee0: "int dbg_log(const char* fmt,...);",
    0x4134C0: "int write_log(unsigned int color, const char* msg);",
    0x47C1E0: "int ht_hash_ent_list(const char* str);",
    0x404BB0: "int ht_hash_ent(const char* str);",
    0x4016F0: "int reg_get_val(const char* value);",
    0x414280: "int prepare_html_log(const char* filename);",
    0x6597d0: "bool read_ini_entry(void* dest,const char* key, const char* section);",
    0x5A8FB0: "void* Py_InitModule(const char* name,void* methods);",
    0x5E3800: "int fopen_from_pak(const char* filename);",
    0x419950: "int fopen_2(const char* filename);",
    0x41AB50: "int open_pak(const char* filename, int unk_1,void* unk_ptr);",
    0x404460: "int register_c_callback(const char* name,void* func);",
    0x414070: "void throw_assertion_2(const char* check,const char* file,const char* date, unsigned int line);",
    0x5FBC50: "void throw_assertion_1(const char* check,const char* file, unsigned int line);",
    0x5BC140: "static char* convertsimple1(void *arg, char **p_format, void *p_va);",
    0x5E3800: "int32_t fopen_from_pak(const char* filename,const char* mode);",
    0x5a90f0: "void* Py_BuildValue(const char* format, ...);"
}

functions = {
    0x6B1C70: "strcmp",
    0x5BB9D0: "PyArg_ParseTuple",
    0x5DD510: "init_engine_3d",
    0x401180: "create_window",
    0x401240: "create_main_window",
    0x4016F0: "reg_get_val",
    0x4134C0: "write_log",
    0x414280: "prepare_html_log",
    0x418220: "get_version_info",
    0x4137E0: "write_html_log",
    0x402190: "handle_console_input",
    0x5F9520: "handle_render_console_input",
    0x404A50: "find_entity",
    0x47C1E0: "ht_hash_ent_list",
    0x404BB0: "ht_hash_ent",
    0x404460: "register_c_callback",
    0x417470: "load_game",
    0x5E3800: "fopen_from_pak",
    0x5e3500: "fopen",
    0x403370: "init_debug",
    0x401770: "init",
    0x4026D0: "init_py",
    0x405B40: "init_py_sub",
    0x5A8FB0: "Py_InitModule",
    0x41AB50: "open_pak",
    0x5A8390: "py_exec",
    0x414570: "setup_game_vars",
    0x5FBC50: "throw_assertion_1",
    0x414070: "throw_assertion_2",
    0x5F7000: "read_ini",
    0x650F80: "load_sm3",
    0x6665A0: "load_m3d_1",
    0x666900: "load_m3d_2",
    0x479B20: "world_constructor",
    0x479B40: "init_world",
    0x402510: "deinit_world",
    0x479870: "make_world",
    0x602A70: "render_frame",
    0x6B738C: "handle_exception",
    0x5B9E70: "py_getattr",
    0x413ee0: "dbg_log",
    0x5f75e0: "init_d3d",
    0x63a2f0: "gdi_draw_line",
    0x5e3250: "read_stream",
    0x5e3bb0: "read_stream_wrapper",
    0x50b9b0: "init_scorer",
    0x582e10: "init_action_class_list",
    0x528910: "init_sound_sys",
    0x5268d0: "try_init_sound_sys",
    0x404280: "cPyFunction_set_func",
    0x414680: "load_config",
    0x414810: "save_config",
    0x4f42a0: "close_server_socket",
    0x4f4d10: "close_server",
    0x4f48e0: "close_client",
    0x4f4fb0: "is_server",
    0x4f4a10: "is_client",
    0x4fac50: "is_master",
    0x526910: "close_sound_sys",
    0x526520: "shutdown_sound_sys",
    0x5dd700: "close_3d_engine",
    0x5a7320: "close_window",
    0x5dff20: "set_exception_handler",
    0x5a7f20: "get_console_wnd",
    0x5a73a0: "show_console",
    0x666c60: "read_m3d",
    0x417df0: "snprintf",
    0x5fc930: "printf",
    0x6597d0: "read_ini_entry",
    0x5fc0a0: "engine_debug_log",
    0x5a7440: "create_console_window",
    0x6114e0: "setup_window",
    0x404420: "clear_functions",
    0x405ca0: "close_py_subsys",
    0x50bcb0: "close_scorer",
    0x479b20: "close_world",
    0x582e70: "close_action_class",
    0x50b6a0: "get_scorer",
    0x50ea20: "scorer_parse_type",
    0x636580: "list_models",
    0x5a90f0: "Py_BuildValue",
    0x41c5a0: "has_lst_file",
    0x5a8e90: "py_error",
    0x5a9890: "get_module_dict",
    0x5c7bb0: "get_current_thread",
    0x5aa140: "preload_lib",
    0x413c10: "sprintf",
    0x405850: "check_is_python",
    0x47bf90: "setup_ent_list",
    0x474f80: "ent_list_get_set",
}

# 0x853954 ??? some obj ptr

# [0x7fbe98]

# [0x853954]+0x2a3cc debug flag, checked in 0x006113a0 called from 0x005dd5ea
cfg="""
e asm.cmt.right = true
e cmd.stack = true
e scr.utf8 = true
e asm.describe = false
e graph.cmtright = true
e cfg.sandbox = false
e cfg.newtab = true
e cfg.fortunes.type = tips,fun,creepy,nsfw
e dbg.status = true
e pdb.autoload = true
e emu.str = true
e asm.flags.offset = true
""".strip().splitlines()
for line in cfg:
    r2_cmd(line)

analysis(False)

for addr,comment in comments.items():
    r2_cmd(f"CC {comment} @ {hex(addr)}")

for t in types:
    r2_cmd(f'"td {t}"')

for addr, name in flags.items():
    x64_dbg_label(addr,name,"loc")
    r2_cmd(f"f loc.{name} 4 {hex(addr)}")

for addr, name in functions.items():
    x64_dbg_label(addr,name,"fcn")
    r2_cmd(f"afr fcn.{name} {hex(addr)}")
    if addr in func_sigs:
        r2_cmd(f'"afs {func_sigs[addr]}" @{hex(addr)}')


def vtables():
    ret = {}
    print("[*] Analyzing VTables")
    vtables = r2_cmdJ("avj")
    for c in tqdm(vtables, ascii=True):
        methods = []
        name=VMTs.get(c.offset,f"{c.offset:08x}")
        x64_dbg_label(c.offset,name,"vmt")
        r2_cmd(f"f vmt.{name} 4 {hex(c.offset)}")
        for idx,m in enumerate(tqdm(c.methods, ascii=True, leave=False)):
            methods.append(hex(m.offset))
            x64_dbg_label(m.offset,f"{name}.{idx}","fcn.vmt")
            r2_cmd(f"afr fcn.vmt.{name}.{idx} {hex(m.offset)} 2>NUL")
        ret[hex(c.offset)] = methods
    return ret


def c_callbacks():
    print("[*] Parsing C Callbacks")
    funcs = {}
    res = r2_cmd("/r fcn.register_c_callback ~CALL[1]").splitlines()
    for addr in tqdm(res, ascii=True):
        r2_cmd(f"s {addr}")
        r2_cmd(f"so -3")
        func, name = r2_cmdJ(f"pdj 2")
        func = func.refs[0].addr
        name = r2_cmd(f"psz @{hex(name.refs[0].addr)}").strip()
        r2_cmd(f"afr fcn.callbacks.{name} {hex(func)} 2>NUL")
        x64_dbg_label(func,f"{name}","fcn.callbacks")
        funcs[name] = hex(func)
    return funcs


def assertions():
    assertions = {}
    for (n_args, a_addr) in [
        (4, "fcn.throw_assertion_1"),
        (3, "fcn.throw_assertion_2"),
    ]:
        print(f"[*] Parsing C assertions for {a_addr}")
        res = r2_cmd(f"/r {a_addr} ~CALL[1]").splitlines()
        print()
        for line in tqdm(res, ascii=True):
            addr = line.strip()
            r2_cmd(f"s {addr}")
            r2_cmd(f"so -{n_args}")
            dis=r2_cmdJ(f"pij {n_args}")
            if n_args == 4:
                file, msg, date, line = dis
            elif n_args == 3:
                date = None
                file, msg, line = dis
            try:
                file = r2_cmd(f"psz @{file.refs[0].addr}").strip()
                msg = r2_cmd(f"psz @{msg.refs[0].addr}").strip()
                if date:
                    date = r2_cmd(f"psz @{date.refs[0].addr}").strip()
                line = line.val
                file = file.replace("\\\\", "\\")
                assertions.setdefault(file, [])
                assertions[file].append(
                    {"line": line, "date": date, "addr": addr, "msg": msg}
                )
            except:
                pass
    for path in assertions:
        assertions[path].sort(key=lambda v: v["line"])
    return assertions


def bb_refs(addr):
    ret = {}
    res = r2_cmd(f"/r {addr} ~fcn[0,1]").splitlines()
    print()
    for ent in res:
        func, hit = ent.split()
        ret[hit] = {"asm": [], "func": func}
        for ins in r2_cmdJ(f"pdbj @{hit}"):
            ret[hit]["asm"].append(ins.disasm)
    return ret


def world():
    print("[*] Parsing World offsets")
    return bb_refs("loc.P_World")


def render():
    print("[*] Parsing D3D_Device offsets")
    return bb_refs("loc.P_D3D8_Dev")


def py_mods():
    print("[*] Parsing Python modules")
    res = r2_cmd("/r fcn.Py_InitModule ~CALL[1]").splitlines()
    print()
    py_mods = {}
    for call_loc in tqdm(res, ascii=True):
        r2_cmd(f"s {call_loc}")
        r2_cmd(f"so -3")
        args = r2_cmdJ("pdj 3")
        refs = []
        if not all([arg.type == "push" for arg in args]):
            continue
        for arg in args:
            refs.append(hex(arg.val))
        doc, methods, name = refs
        doc = r2_cmd(f"psz @{doc}").strip()
        name = r2_cmd(f"psz @{name}").strip()
        r2_cmd(f"s {methods}")
        r2_cmd(f"f py.{name} 4 {methods}")
        x64_dbg_label(methods,f"{name}","py")
        py_mods[name] = {"methods_addr": methods, "doc": doc, "methods": {}}
        while True:
            m_name, m_func, _, m_doc = [v.value for v in r2_cmdJ(f"pfj xxxx")]
            if m_name == 0:
                break
            m_name, m_func, m_doc = map(hex, (m_name, m_func, m_doc))
            m_name = r2_cmd(f"psz @{m_name}").strip()
            r2_cmd(f"f py.{name}.{m_name}.__doc__ 4 {m_doc}")
            if int(m_doc,16)!=0:
                x64_dbg_label(m_doc,f"{name}.{m_name}.__doc__","py")
                m_doc = r2_cmd(f"psz @{m_doc}").strip()
            else:
                m_doc=None
            py_mods[name]["methods"][m_name] = {"addr": m_func, "doc": m_doc}
            r2_cmd(f"afr py.{name}.{m_name} {m_func} 2>NUL")
            x64_dbg_label(m_func,f"{name}.{m_name}","fcn.py")
            r2_cmd("s +16")
    return py_mods


def game_vars():
    ret = {}
    print("[*] Parsing Game variables")
    res = r2_cmd("/r fcn.setup_game_vars ~CALL[1]").splitlines()
    print()
    for line in tqdm(res, ascii=True):
        addr = line.strip()
        r2_cmd(f"s {addr}")
        args = r2_cmd("pdj -5")  # seek and print disassembly
        if not args:
            continue
        args = json.loads(args)
        args_a = []
        push_cnt = 0
        for arg in args[::-1]:
            if arg["type"] not in ["push", "mov"]:
                continue
            if arg["type"] == "push":
                push_cnt += 1
            args_a.append(arg)
            if push_cnt == 3:
                break
        if len(args_a) != 4:
            continue
        if not all(["val" in v for v in args_a]):
            continue
        addr, name, _, desc = [v["val"] for v in args_a]
        name = r2_cmd(f"psz @{hex(name)}").strip()
        desc = r2_cmd(f"psz @{hex(desc)}").strip()
        addr = hex(addr)
        r2_cmd(f"f loc.gvar.{name} 4 {addr}")
        x64_dbg_label(addr,f"{name}","loc.gvar")
        ret[addr] = {"name": name, "desc": desc}
    return ret


ret = dict(
    game_vars=game_vars(),
    c_callbacks=c_callbacks(),
    py_mods=py_mods(),
    assertions=assertions(),
    vtables=vtables(),
    world=world(),
    render=render(),
)

analysis(True)

with open(json_path, "w") as of:
    json.dump(ret, of, indent=4)

print("[+] Wrote scrap_dissect.json")

with open(x64_dbg_script_path,"w") as of:
    of.write("\n".join(x64_dbg_script))

print("[+] Wrote scrap_dissect.x32dbg.txt")

with open(script_path, "w") as of:
    wcmds = []
    for cmd in r2cmds:
        record=True
        for start in ["p","/","s"]:
            if cmd.strip('"').startswith(start):
                record=False
        if record:
            wcmds.append(cmd)
    of.write("\n".join(wcmds))

print("[+] Wrote scrap_dissect.r2")

r2.quit()

def start_program(cmdl,**kwargs):
    if os.name=='nt':
        return SP.Popen(['cmd','/c','start']+cmdl,**kwargs)
    else:
        return SP.Popen(cmdl,**kwargs)

print("[+] Analysis took:",datetime.today()-t_start)


print("[+] Executing Cutter")
try:
    start_program(['cutter','-A','0','-i',script_path,scrap_exe],cwd=folder,shell=False)
except FileNotFoundError:
    print("[-] cutter not installed, falling back to r2")
    start_program(['r2','-i',script_path,scrap_exe],cwd=folder,shell=False)