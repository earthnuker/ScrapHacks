import r2pipe
import os
import json
from tqdm import tqdm
from pprint import pprint
import os
import sys

r2cmds = []
scrap_exe = sys.argv[1]
folder = os.path.abspath(os.path.dirname(scrap_exe))

assert os.path.isfile(scrap_exe), "File not found!"
r2 = r2pipe.open(scrap_exe)
file_hashes = r2.cmdj("itj")
target_hashes = {
    "sha1": "d2dde960e8eca69d60c2e39a439088b75f0c89fa",
    "md5": "a934c85dca5ab1c32f05c0977f62e186",
}

assert file_hashes == target_hashes, "Hash mismatch"


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


print("[*] Running 'aaaaa'")

r2_cmd("aaaaa")

#0x7fac20
#0x7fac19
#0x7faa4c
#0x7fac1c # activate viewer
#0x84d400

#0x413ee0

#0x7d2094 refcnt
flags = {0x7FE944: ("P_World", 4), 0x79C698: ("Py_Mods", 4),0x852914: ("P_D3D8_Dev",4)}

types = ["struct PyMethodDef {char *ml_name; void *ml_meth; int ml_flags; char *ml_doc;};"]

func_sigs = {
    0x5a8390: "int py_exec(const char* script);",
    0x5bb9d0: "int PyArg_ParseTuple(void* PyObj, char* format, ...);",
    0x4134c0: "int write_log(unsigned int color, const char* msg);",
    0x47C1E0: "int ht_hash_ent_list(const char* str);",
    0x404BB0: "int ht_hash_ent(const char* str);",
    0x4016f0: "int reg_get_val(const char* value);",
    0x414280: "int prepare_html_log(const char* filename);",
    0x6b1c70: "bool strcmp(const char* s1,const char* s2);",
    0x5A8FB0: "void* Py_InitModule(const char* name,void* methods);",
    0x5E3800: "int fopen_1(const char* filename);",
    0x419950: "int fopen_2(const char* filename);",
    0x41AB50: "int open_pak(const char* filename, int unk_1,void* unk_ptr);",
    0x404460: "int register_c_callback(const char* name,void* func);"
    0x414070: "void throw_assertion_2(const char* check,const char* file, unsigned int line);"
    0x5FBC50: "void throw_assertion_1(const char* check,const char* file,const char* date, unsigned int line);",
    0x5bc140: "static char* convertsimple1(void *arg, char **p_format, void *p_va);"
}

functions = {
    0x6b1c70: "strcmp",
    0x5bb9d0: "PyArg_ParseTuple",
    0x5dd510: "init_engine_3d",
    0x401180: "create_window",
    0x401240: "create_main_window",
    0x4016f0: "reg_get_val",
    0x4134c0: "write_log",
    0x414280: "prepare_html_log",
    0x418220: "get_version_info",
    0x4137e0: "write_html_log",
    0x402190: "handle_console_input",
    0x5F9520: "handle_render_console_input",
    0x404A50: "find_entity",
    0x47C1E0: "ht_hash_ent_list",
    0x404BB0: "ht_hash_ent",
    0x404460: "register_c_callback",
    0x417470: "load_game",
    0x5E3800: "fopen_1",
    0x419950: "fopen_2",
    0x403370: "debug_init",
    0x401770: "init",
    0x4026D0: "init_py",
    0x405B40: "init_py_sub",
    0x5A8FB0: "Py_InitModule",
    0x41AB50: "open_pak",
    0x5A8390: "py_exec",
    0x414570: "setup_game_vars",
    0x5FBC50: "throw_assertion_1",
    0x414070: "throw_assertion_2",
    0x5F7000: "load_m3d_ini",
    0x650F80: "load_sm3",
    0x6665A0: "load_m3d_1",
    0x666900: "load_m3d_2",
    0x479B20: "world_constructor",
    0x479B40: "world_init",
    0x402510: "world_deinit",
    0x479870: "make_world",
    0x602a70: "render_frame"
}

for t in types:
    r2_cmd(f'"td {t}"')

for addr, args in flags.items():
    name, size = args
    r2_cmd(f"f loc.{name} {size} {hex(addr)}")
    
for addr, name in functions.items():
    r2_cmd(f"afr fcn.{name} {hex(addr)}")
    if addr in func_sigs:
        r2_cmd(f'"afs {func_sigs[addr]}" @{hex(addr)}')


def vtables():
    ret = {}
    print("[*] Analyzing VTables")
    vtables = r2_cmdJ("avj")
    for c in tqdm(vtables, ascii=True):
        methods = []
        for m in tqdm(c.methods, ascii=True, leave=False):
            methods.append(hex(m.offset))
            r2.cmd(f"afr @{hex(m.offset)} 2>{os.devnull}")
        ret[hex(c.offset)] = methods
    return ret


def c_callbacks():
    print("[*] Parsing C Callbacks")
    funcs = {}
    res = r2_cmd("/r fcn.register_c_callback ~CALL[1]").splitlines()
    for addr in tqdm(res, ascii=True):
        func, name = r2_cmdJ(f"s {addr};so -3;pdj 2")
        func = func.refs[0].addr
        name = r2_cmd(f"psz @{hex(name.refs[0].addr)}").strip()
        r2_cmd(f"afr fcn.CB_{name} {hex(func)} 2>NUL")
        funcs[name] = hex(func)
    return funcs


def assertions():
    assertions = {}
    for (n_args,a_addr) in [(4,"fcn.throw_assertion_1"), (3,"fcn.throw_assertion_2")]:
        print(f"[*] Parsing C assertions for {a_addr}")
        res = r2_cmd(f"/r {a_addr} ~CALL[1]").splitlines()
        print()
        for line in tqdm(res, ascii=True):
            addr = line.strip()
            dis=r2_cmdJ(f"s {addr};so -{n_args};pij {n_args}")  # seek and print disassembly
            if n_args==4:
                file, msg, date, line = dis
            elif n_args==3:
                date=None
                file, msg, line = dis
            try:
                file = r2_cmd(f"psz @{file.refs[0].addr}").strip()
                msg = r2_cmd(f"psz @{msg.refs[0].addr}").strip()
                if date:
                    r2_cmd(f"psz @{date.refs[0].addr}").strip()
                line=line.val
                file=file.replace("\\\\", "\\")
                os.path.isabs(file):
                    file = os.path.abspath(file)
                assertions.setdefault(path, [])
                assertions[path].append({'line':line,'date':date,'addr':addr,'msg': msg})
            except:
                pass
    for path in assertions:
        assertions[path].sort(key=lambda v:v['line'])
    return assertions

def bb_refs(addr):
    ret={}
    res = r2_cmd(f"/r {addr} ~fcn[0,1]").splitlines()
    print()
    for ent in res:
        func,hit=ent.split()
        ret[hit]={'asm':[],'func':func}
        for ins in r2_cmdJ(f"pdbj @{hit}"):
            ret[hit]['asm'].append(ins.disasm)
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
        args = r2_cmdJ(f"s {call_loc};so -3;pdj 3")
        refs = []
        if not all([arg.type == "push" for arg in args]):
            continue
        for arg in args:
            refs.append(hex(arg.val))
        doc, methods, name = refs
        doc = r2_cmd(f"psz @{doc}").strip()
        name = r2_cmd(f"psz @{name}").strip()
        r2_cmd(f"s {methods}")
        r2_cmd(f"f loc.py.MethodDef_{name} 4 {methods}")
        py_mods[name] = {"methods_addr": methods, "doc": doc, "methods": {}}
        while True:
            m_name, m_func, _, m_doc = [v.value for v in r2_cmdJ(f"pfj xxxx")]
            if m_name == 0:
                break
            m_name, m_func, m_doc = map(hex, (m_name, m_func, m_doc))
            m_name = r2_cmd(f"psz @{m_name}").strip()
            r2_cmd(f"f Py_{name}_{m_name}_doc 4 {m_doc}")
            m_doc = r2_cmd(f"psz @{m_doc}").strip()
            py_mods[name]["methods"][m_name] = {"addr": m_func, "doc": m_doc}
            r2_cmd(f"afr fcn.py.{name}.{m_name} {m_func} 2>NUL")
            r2_cmd("s +16")
    return py_mods


def game_vars():
    ret={}
    print("[*] Parsing Game variables")
    res = r2_cmd("/r fcn.setup_game_vars ~CALL[1]").splitlines()
    print()
    for line in tqdm(res, ascii=True):
        addr = line.strip()
        r2_cmd(f"s {addr}")
        args = r2_cmd("pdj -5")  # seek and print disassembly
        if not args:
            continue
        args=json.loads(args)
        args_a = []
        push_cnt=0
        for arg in args[::-1]:
            if arg['type'] not in ["push","mov"]:
                continue
            if arg['type']=="push":
                push_cnt+=1
            args_a.append(arg)
            if push_cnt==3:
                break
        if len(args_a)!=4:
            continue
        if not all(['val' in v for v in args_a]):
            continue
        addr,name,_,desc=[v['val'] for v in args_a]
        name=r2_cmd(f"psz @{hex(name)}").strip()
        desc=r2_cmd(f"psz @{hex(desc)}").strip()
        addr=hex(addr)
        r2_cmd(f"f var_{name} 4 {addr}")
        ret[addr]={'name':name,'desc':desc}
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

r2_cmd("aaaaa") # Propagate type infos

with open(os.path.join(folder, "Scrap_dissect.json"), "w") as of:
    json.dump(ret, of, indent=4)
print("[+] Wrote Scrap_dissect.json")

with open(os.path.join(folder, "Scrap_dissect.r2"), "w") as of:
    wcmds = []
    for cmd in r2cmds:
        for start in ["f ", "afr ", "aaaaa","afs"]:
            if cmd.strip('"').startswith(start):
                wcmds.append(cmd)
                break
    of.write("\n".join(wcmds))

print("[+] Wrote Scrap_dissect.r2")
print(f"[*] Done, now cd to '{folder}'...")
print(
    "[*] ...and run 'r2 -i Scrap_dissect.r2 Scrap.exe' to load the parsed infos into radare2"
)
