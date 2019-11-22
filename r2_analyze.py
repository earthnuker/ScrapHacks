import r2pipe
import os
import json
from tqdm import tqdm
from pprint import pprint
import os
import sys
r2cmds=[]
scrap_exe=sys.argv[1]
folder=os.path.join(os.path.dirname(scrap_exe))
r2 = r2pipe.open(scrap_exe)

assert r2.cmdj("itj")['sha1'] == "d2dde960e8eca69d60c2e39a439088b75f0c89fa","Hash mismatch"
assert r2.cmdj("itj")['md5'] == "a934c85dca5ab1c32f05c0977f62e186","Hash mismatch"

def r2_cmd(cmd):
    global r2,r2cmds
    r2cmds.append(cmd)
    return r2.cmd(cmd)

def r2_cmdj(cmd):
    global r2,r2cmds
    r2cmds.append(cmd)
    return r2.cmdj(cmd)

def r2_cmdJ(cmd):
    global r2,r2cmds
    r2cmds.append(cmd)
    return r2.cmdJ(cmd)


print("[*] Running 'aaaa'")

r2_cmd("aaaa")

flags = {0x7FE944: ("World_Ptr", 4), 0x79C698: ("Py_Mods", 4)}

functions = {
    0x404A50: "find_entity",
    0x404BB0: "ht_hash",
    0x404460: "reg_c_callback",
    0x417470: "load_game",
    0x5E3800: "fopen_1",
    0x419950: "fopen_2",
    0x403370: "debug_init",
    0x401770: "init",
    0x4026D0: "init_py",
    0x5A8FB0: "init_py_mod",
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
}

for addr, args in flags.items():
    name, size = args
    r2_cmd(f"f {name} {size} {hex(addr)}")

for addr, name in functions.items():
    r2_cmd(f"afr {name} {hex(addr)}")

def vtables():
    ret={}
    print("[*] Analyzing VTables")
    vtables = r2_cmdJ("avj")
    for c in tqdm(vtables,ascii=True):
        methods=[]
        for m in tqdm(c.methods,ascii=True,leave=False):
            methods.append(hex(m.offset))
            r2.cmd(f"afr @{hex(m.offset)} 2>NUL")
        ret[hex(c.offset)]=methods
    return ret

def c_callbacks():
    print("[*] Parsing C Callbacks")
    funcs={}
    res = r2_cmd("/r 0x404460 ~CALL[1]").splitlines()
    for addr in tqdm(res,ascii=True):
        func,name=r2_cmdJ(f"s {addr};so -3;pdj 2")
        func=func.refs[0].addr
        name=r2_cmd(f"psz @{hex(name.refs[0].addr)}").strip()
        r2_cmd(f"afr CB_{name} {hex(func)} 2>NUL")
        funcs[name]=hex(func)
    return funcs

def assertions():
    assertions = {}
    for a_addr in ['0x414070','0x5fbc50']:
        print(f"[*] Parsing C assertions for {a_addr}")
        res = r2_cmd(f"/r {a_addr} ~CALL[1]").splitlines()
        print()
        for line in tqdm(res, ascii=True):
            addr = line.strip()
            file, msg = r2_cmdJ(f"s {addr};so -2;pij 2")  # seek and print disassembly
            try:
                file = r2_cmd(f"psz @{file.refs[0].addr}").strip()
                msg = r2_cmd(f"psz @{msg.refs[0].addr}").strip()
                path = os.path.abspath(file.replace("\\\\", "\\"))
                assertions.setdefault(path, [])
                assertions[path].append([int(addr, 16), msg])
            except:
                pass
    return assertions


def world():
    print("[*] Parsing World offsets")
    res = r2_cmd("/r 0x7fe944 ~&fcn,DATA[0,1]").splitlines()
    print()
    for hit in res:
        func, offset = hit.split()
        offset = int(offset, 16)
        print("=" * 5, func, "=" * 5)
        for op in r2_cmdJ(f"pdfj @{func}")["ops"]:
            if op.offset >= offset:
                # print(op.disasm,op.get('refs',[]))
                print(op.disasm)


def py_mods():
    print("[*] Parsing Python modules")
    res = r2_cmd("/r 0x5a8fb0 ~CALL[1]").splitlines()
    print()
    py_mods={}
    for call_loc in tqdm(res,ascii=True):
        args = r2_cmdJ(f"s {call_loc};so -3;pdj 3")
        refs = []
        if not all([arg.type=="push" for arg in args]):
            continue
        for arg in args:
            refs.append(hex(arg.val))
        doc,methods,name=refs
        doc=r2_cmd(f"psz @{doc}").strip()
        name=r2_cmd(f"psz @{name}").strip()
        r2_cmd(f"s {methods}")
        r2_cmd(f"f PyMethodDef_{name} 4 {methods}")
        py_mods[name]={'methods_addr':methods,'doc':doc,'methods':{}}
        while True:
            m_name,m_func,_,m_doc=[v.value for v in r2_cmdJ(f"pfj xxxx")]
            if m_name==0:
                break
            m_name,m_func,m_doc=map(hex,(m_name,m_func,m_doc))
            m_name=r2_cmd(f"psz @{m_name}").strip()
            r2_cmd(f"f Py_{name}_{m_name}_doc 4 {m_doc}")
            m_doc=r2_cmd(f"psz @{m_doc}").strip()
            py_mods[name]['methods'][m_name]={'addr':m_func,'doc':m_doc}
            r2_cmd(f"afr Py_{name}_{m_name} {m_func} 2>NUL")
            r2_cmd("s +16")
    return py_mods


def game_vars():
    print("[*] Parsing Game variables")
    res = r2_cmd("/r 0x414570 ~CALL[1]").splitlines()
    print()
    for line in tqdm(res,ascii=True):
        addr = line.strip()
        args = r2_cmdJ(f"s {addr};so -4;pdj 4")  # seek and print disassembly
        args_a = []
        for arg in args:
            if "refs" in arg:
                addr = hex(arg.refs[0].addr)
                s = r2_cmd(f"ps @{hex(arg.refs[0].addr)}").strip()
                args_a.append((addr, s))
        print(args_a)

ret=dict(
    py_mods=py_mods(),
    assertions=assertions(),
    c_callbacks=c_callbacks(),
    vtables=vtables(),
    #game_vars=game_vars(),
    #world=world(),
)


with open(os.path.join(folder,"Scrap_dissect.json"),"w") as of:
    json.dump(ret,of,indent=4)
print("[+] Wrote Scrap_dissect.json")
with open(os.path.join(folder,"Scrap_dissect.r2"),"w") as of:
    wcmds=[]
    for cmd in r2cmds:
        for start in ['f ','afr ','aaaa']:
            if cmd.startswith(start):
                wcmds.append(cmd)
                break
    of.write("\n".join(wcmds))
print("[+] Wrote Scrap_dissect.r2")
print("[*] Done!")
print("[*] Run 'r2 -i Scrap_dissect.r2 Scrap.exe' to load parsed infos into radare2")
