import os
import json
from construct import *

blocksize = 1024 * 4


def search(pattern, path):
    seen = set()
    with open(path, "rb") as infile:
        buffer = bytearray(infile.read(blocksize))
        while infile.peek(1):
            for block in iter(lambda: infile.read(blocksize), b""):
                buffer += block
                buffer = buffer[-(blocksize * 2) :]
                idx = buffer.find(pattern)
                if idx != -1:
                    pos = (infile.tell() - blocksize * 2) + idx
                    if pos not in seen:
                        seen.add(pos)
    return sorted(seen)


has_pos = [
    "D3DFVF_XYZ",
    "D3DFVF_XYZRHW",
]

num_blend = {
    'D3DFVF_XYZB1': 1,
    'D3DFVF_XYZB2': 2,
    'D3DFVF_XYZB3': 3,
    'D3DFVF_XYZB4': 4,
}

Vertex = Struct(
    "pos" / If(lambda ctx: ctx._._.fvf.position in has_pos, Float32l[3]),
    "rhw" / If(lambda ctx: ctx._._.fvf.position == "D3DFVF_XYZRHW", Float32l),
    "w_blend" / If(lambda ctx: num_blend.get(ctx._._.fvf.position,0)!=0, Int32ul),
    "normal" / If(lambda ctx: ctx._._.fvf.flags.D3DFVF_NORMAL, Float32l[3]),
    "diffuse" / If(lambda ctx: ctx._._.fvf.flags.D3DFVF_DIFFUSE, Int8ul[4]),
    "specular" / If(lambda ctx: ctx._._.fvf.flags.D3DFVF_SPECULAR, Int8ul[4]),
    "tex" / Float32l[this.num_tex_coords][this._._.fvf.num_tex],
)

D3DFVF_POSITION_MASK = 0xE
D3DFVF_TEXCOUNT_MASK = 0xF00
D3DFVF_TEXCOUNT_SHIFT = 8

FVF = "fvf" / Union(
    0,
    "value" / Int32ul,
    "num_tex"
    / Computed(
        lambda ctx: 1 + ((ctx.value & D3DFVF_TEXCOUNT_MASK) >> D3DFVF_TEXCOUNT_MASK)
    ),
    "position"
    / Enum(
        Computed(lambda ctx: (ctx.value & D3DFVF_POSITION_MASK)),
        D3DFVF_XYZ=0x2,
        D3DFVF_XYZRHW=0x4,
        D3DFVF_XYZB1=0x6,
        D3DFVF_XYZB2=0x8,
        D3DFVF_XYZB3=0xA,
        D3DFVF_XYZB4=0xC,
    ),
    "flags"
    / FlagsEnum(
        Int32ul,
        D3DFVF_RESERVED0=0x1,
        D3DFVF_NORMAL=0x10,
        D3DFVF_PSIZE=0x20,
        D3DFVF_DIFFUSE=0x40,
        D3DFVF_SPECULAR=0x80,
    ),
)

LFVF_Data = Struct(
    "unk" / Int32ul,
    "num_entries"/Int32ul,
    "data"/Struct(
        FVF,
        "unk_size" / Int32ul,
        "vertices" / PrefixedArray(Int32ul, Vertex),
    )
    # Terminated,
)

LFVF = Struct(
    Const(b"LFVF"), "size" / Int32ul, "data" / RestreamData(Bytes(this.size), LFVF_Data)
)

files = [
    r"D:\Games\Deep Silver\Scrapland\extracted\Data.packed\models\skies\orbit\sky.sm3",
    r"D:\Games\Deep Silver\Scrapland\extracted\Data.packed\models\chars\boss\boss.sm3",
    r"D:\Games\Deep Silver\Scrapland\extracted\Data.packed\models\chars\dtritus\dtritus.sm3",
    r"D:\Games\Deep Silver\Scrapland\extracted\Data.packed\levels\gdb\map\map3d.emi"
]

vert_pos = {}

for path in files:
    name = os.path.split(path)[-1]
    fh = open(path, "rb")
    offsets = search(b"LFVF", path)
    for offset in sorted(offsets):
        fh.seek(offset)
        print("Offset:", offset)
        s = LFVF.parse_stream(fh)
        print(s)
        print("=" * 10)
        continue
    #     # print(s)
    #     print(path, fh.tell(), list(s.unk_ints), list(s.data.unk), fh.read(8))
    #     s = s.data
    #     vpos = [
    #         tuple(p for p in v.pos) for v in s.vertices
    #     ]  # leave vertices alone because we don't need to reproject shit :|
    #     vert_pos["{}@{}".format(name, hex(offset))] = vpos
    # with open("LFVF_Data.json", "w") as of:
    #     json.dump(vert_pos, of)
    # break
