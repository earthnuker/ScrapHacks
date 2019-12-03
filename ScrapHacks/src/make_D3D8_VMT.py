import os
import sys
import re
outfile,infile=sys.argv[1:]

re_interface=re.compile(r"^DECLARE_INTERFACE_{0,1}\((.*?)\)$")
re_method=re.compile(r"^\w*STDMETHOD_{0,1}\((.*?)\)\((.*?)\).*;")
name=None
idx=0
VMTs={}
with open(infile,"r") as infh:
    for line in infh:
        line=line.strip()
        interf=re_interface.match(line)
        meth=re_method.match(line)
        if interf:
            idx=0
            name="VMT_"+"_".join([name for name in interf.groups()[0].split(", ") if name!="IUnknown"])
            VMTs[name]={}
        if meth:
            meth_name,meth_args=meth.groups()
            meth_name=meth_name.split(",")[-1].strip()
            VMTs[name][meth_name]=idx
            idx+=1
print(f"Generating: {outfile} from {infile} ...")
with open(outfile,"w") as ofh:
    for name in sorted(VMTs.keys()):
        print(f"namespace {name} {{",file=ofh)
        for method,idx in sorted(VMTs[name].items(),key=lambda v:v[1]):
            print(f"\tconst size_t m_{method} = {idx};",file=ofh)
        print("}",file=ofh)