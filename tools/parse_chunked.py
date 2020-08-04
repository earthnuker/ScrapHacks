from construct import *
import binascii
import os

Chunked = LazyBound(lambda: struct)


class CustomError(SymmetricAdapter):
    def __init__(self, msg):
        super(SymmetricAdapter, self).__init__(Pass)
        self._message = msg

    def _decode(self, obj, context, path):
        # print("Error",path)
        # print(str(context))
        msg = "Invalid ID: " + repr(context.id)
        raise ValidationError(message=msg, path=this.path)


RGB = NamedTuple("RGB", "R G B", Int8ul[3])

RGBA = NamedTuple("RGBA", "R G B A", Int8ul[4])


def make_chain(*sizes):
    "utility function to make sequence of byte arrays"
    return Sequence(*[Bytes(s) for s in sizes])


child_nodes = "children" / Struct("num" / Int32ul, "nodes" / Chunked[this.num])

subchunks = {
    b"SM3\0": Struct(
        "unk" / Bytes(4),
        "timestamp" / Timestamp(Int32ul, 1, 1970),
        child_nodes,
        "scene" / Chunked,
    ),
    b"SCN\0": Struct(
        "version" / Int32ul,
        "m3d_name" / PascalString(Int32ul, "utf8"),
        "name" / PascalString(Int32ul, "utf8"),
        child_nodes,
    ),
    b"INI\0": Struct(
        "data"
        / PrefixedArray(Int32ul, PrefixedArray(Int32ul, PascalString(Int32ul, "utf8"))),
        "colors?" / Sequence(Int8ul, Int8ul, Int8ul, Int8ul, Float32l)[2],
        "unk_data" / Bytes(0x18),
        "unk_float" / Float32l,
        "unk_int" / Int32ul,
        child_nodes,
    ),
    b"EMI\0": Struct(
        "version"/Int32ul,
        "num_materials"/Int32ul,
        "num_unk"/Int32ul,
        "materials"/Chunked
    ),

    b"MAT\0": Struct(
        "tris"/Int32ul,
        "name"/PascalString(Int32ul,"utf8"),
        "idx"/Bytes(this.tris*4*4)
    ),

    None: Bytes(lambda ctx:ctx.size),
}

struct = Struct(
    "id" / Bytes(4),
    "size" / Int32ul,
    "data" / Switch(this.id, subchunks, default=subchunks[None]),
)


def io_peek(fh, n):
    p = fh.tell()
    ret = fh.read(n)
    fh.seek(p)
    return ret


basedir = r"D:/Games/Deep Silver/Scrapland/extracted/Data.packed"

files = [
    r"Models/Elements/AnilloEstructuraA/AnilloEstructuraA.SM3",
    r"models/elements/antenaa/antenaa.lod1.sm3",
    r"models/elements/abshield/anm/loop.cm3",
    r"levels/fake/map/map3d.amc",
    r"levels/shipedit/map/map3d.dum",
    r"levels/menu/map/map3d.emi",
    r"Models/Skies/Menu/Sky.SM3",
    r"Levels/Menu/Map/Map3D.SM3",
    r"Models/Elements/AnilloEstructuraD/AnilloEstructuraD.LOD1.SM3",
    r"levels/menu/map/map3d.amc",
    r"levels/menu/map/map3d.dum",
    r"levels/menu/map/scenecamera/anm/loop.cm3",
    r"models/chars/boss/boss.sm3",
    r"models/chars/boss/anm/boss_walk.cm3",
]
for file in files:
    file = os.path.join(basedir, file).replace("/","\\")
    print()
    print("#" * 3, file)
    with open(file, "rb") as infile:
        try:
            data = struct.parse_stream(infile)
            # assert infile.read()==b"","leftover data"
        except Exception as ex:
            print("Error:", ex)
            data = None
        if data:
            print(data)
        print("OFFSET:", hex(infile.tell()))
        print("NEXT:", io_peek(infile, 16))
        print("NEXT:", binascii.hexlify(io_peek(infile, 16)))
