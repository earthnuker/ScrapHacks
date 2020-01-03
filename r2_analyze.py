import r2pipe
import os
import json
from datetime import datetime
import subprocess as SP
from tqdm import tqdm
from pprint import pprint
import os
import sys
import yaml

r2cmds = []
x64_dbg_script=[]
script_path = os.path.dirname(os.path.abspath(__file__))
scrap_exe = os.path.abspath(sys.argv[1])
scrapland_folder = os.path.abspath(os.path.dirname(scrap_exe))
r2_script_path=os.path.join(scrapland_folder, "scrap_dissect.r2")
x64_dbg_script_path=os.path.join(scrapland_folder, "scrap_dissect.x32dbg.txt")
json_path=os.path.join(scrapland_folder, "scrap_dissect.json")

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

with open(os.path.join(script_path,"config.yml")) as cfg:
    print("[*] Loading config")
    config = type("Config",(object,),yaml.load(cfg,Loader=yaml.SafeLoader))

for line in config.script.strip().splitlines():
    r2_cmd(line)

analysis(False)

for addr,comment in config.comments.items():
    r2_cmd(f"CC {comment} @ {hex(addr)}")

for t in config.types:
    r2_cmd(f'"td {t}"')

for addr, name in config.flags.items():
    x64_dbg_label(addr,name,"loc")
    r2_cmd(f"f loc.{name} 4 {hex(addr)}")


for addr, name in config.functions.items():
    x64_dbg_label(addr,name,"fcn")
    r2_cmd(f"afr fcn.{name} {hex(addr)}")

for addr,sig in config.function_signatures.items():
    r2_cmd(f'"afs {config.function_signatures[addr]}" @{hex(addr)}')



def vtables():
    ret = {}
    print("[*] Analyzing VTables")
    vtables = r2_cmdJ("avj")
    for c in tqdm(vtables, ascii=True):
        methods = []
        name=config.VMTs.get(c.offset,f"{c.offset:08x}")
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

with open(r2_script_path, "w") as of:
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
    start_program(['cutter','-A','0','-i',r2_script_path,scrap_exe],cwd=scrapland_folder,shell=False)
except FileNotFoundError:
    print("[-] cutter not installed, falling back to r2")
    start_program(['r2','-i',r2_script_path,scrap_exe],cwd=scrapland_folder,shell=False)