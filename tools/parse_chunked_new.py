import os
import sys
import struct
import string
from pprint import pprint
from io import BytesIO
from contextlib import contextmanager
from datetime import timedelta, datetime
import glob

printable_chars = set(bytes(string.printable, "ascii")) - set(b"\n\r\t\x0b\x0c")


def hexdump(data, cols=16, offset=0, markers=None):
    if markers is None:
        markers = []
    lines = []
    while True:
        hexdata = " ".join("{:02X}".format(v) for v in data[:cols]).ljust(
            3 * cols - 1, " "
        )
        print_data = "".join(
            [chr(v) if v in printable_chars else "." for v in data[:cols]]
        )
        lines.append("{:04X}   {}   {}".format(offset, hexdata, print_data))
        offset += len(data[:cols])
        data = data[cols:]
        if not data:
            break
    return "\n".join(lines).strip()


@contextmanager
def seek_to(fh, offset, pos=None):
    if pos is None:
        pos = fh.tell()
    fh.seek(offset)
    yield
    fh.seek(pos)

def read_array(s,fh):
    ret=[]
    count = read_struct("<I", fh)[0]
    size = struct.calcsize(s)
    for _ in range(count):
        ret.append(read_struct(s,fh))
    return ret


def read_struct(s, fh):
    size = struct.calcsize(s)
    return struct.unpack(s, fh.read(size))


def read_str(fh):
    size = read_struct("<I", fh)[0]
    return fh.read(size)


def read_block(fh):
    try:
        pos = fh.tell()
        magic = str(fh.read(4).rstrip(b"\x00"), "utf8")
        size = read_struct("<I", fh)[0]
        data = fh.read(size)
        return magic, data
    except struct.error:
        fh.seek(pos)
        return


vals = set()

# ================================
class Parser:
    depth = 0
    dump_size = 0x100

    def __init__(self, debug=False):
        self.debug = debug

    def _default(self, magic, fh):
        print("=====", magic, "=====")
        if self.debug:
            print(hexdump(fh.read(self.dump_size)))
            rest = len(fh.read())
            if rest:
                print("<{} more bytes>".format(rest))
        fh.seek(0)
        return "<Unparsed {} ({} bytes)>".format(magic, len(fh.read()))

    def parse(self, magic, data, depth=0):
        print("{}[{}] {} bytes".format("  " * self.depth, magic, len(data)))
        self.depth += 1
        fh = BytesIO(data)
        ret = getattr(self, magic, lambda fh: self._default(magic, fh))(fh)
        pos = fh.tell()
        leftover = len(fh.read())
        fh.seek(pos)
        self.depth -= 1
        if leftover:
            print("{}[{}] {} bytes unparsed".format("  " * self.depth, magic, leftover))
            if self.debug:
                print(hexdump(fh.read(self.dump_size)))
                rest = len(fh.read())
                if rest:
                    print("<{} more bytes>".format(rest))
            print("-" * 50)
        return ret

    def parse_block(self, fh):
        block = read_block(fh)
        if block:
            return self.parse(*block)

    # Block definitions

    def SM3(self, fh):
        ret = {}
        ret["unk_1"] = fh.read(4)  # always F8156500
        ret["timestamp_2"] = datetime.fromtimestamp(read_struct("<I", fh)[0])
        ret["unk_2"] = fh.read(4)  # always 00000000
        ret["scene"] = self.parse_block(fh)
        assert fh.read() == b"", "Leftover Data"
        return ret

    def SCN(self, fh):
        ret = {}
        ret["unk_1"] = read_struct("<I", fh)[0]
        ret["model_name"] = read_str(fh)
        ret["node_name"] = read_str(fh)
        if read_struct("<I", fh)[0]:
            ret["ini_1"] = self.parse_block(fh)
        ret["unk_c_1"] = read_struct("<BBBB", fh)
        ret["unk_f_1"] = read_struct("<f", fh)[0]
        ret["unk_c_2"] = read_struct("<BBBB", fh)
        ret["unk_f_l"] = read_struct("<ffffffff", fh)
        if read_struct("<I", fh)[0]:
            ret["ini_2"] = self.parse_block(fh)
        ret["num_mat"] = read_struct("<I", fh)[0]
        ret["mat"] = []
        for _ in range(ret["num_mat"]):
            ret["mat"].append(self.parse_block(fh))
        #     ret["children"] = []
        #     for _ in range(read_struct("<I", fh)[0]):
        #         ret["children"].append(self.parse_block(fh))
        #     ret["unk_2"] = []
        #     for _ in range(4):
        #         ret["unk_2"].append(read_struct("<fff", fh))
        #     ret["materials"] = []
        #     for _ in range(read_struct("<I", fh)[0]):
        #         ret["materials"].append(self.parse_block(fh))
        return ret

    def INI(self, fh):
        num_sections = read_struct("<I", fh)[0]
        sections = []
        for _ in range(num_sections):
            num_lines = read_struct("<I", fh)[0]
            lines = []
            for _ in range(num_lines):
                lines.append(str(read_str(fh).rstrip(b"\0"), "latin1"))
            sections.append("\n".join(lines))
            lines.clear()
        assert fh.read() == b"", "Leftover Data"
        return sections

    def MAT(self, fh):
        #     ret = {}
        #     ret["unk_1"] = read_struct("<I", fh)[0]
        #     ret["name"] = read_str(fh)
        #     ret["colors?"] = ["{:08X}".format(v) for v in read_struct(">7I", fh)]
        # ret["maps"]=[]
        # for _ in range(ret["num_maps"]):
        #     ret["maps"].append(self.parse_block(fh))
        return {"maps": fh.read().count(b"MAP\0")}

    def MAP(self, fh):
        ret = {}
        ret["unk_1"] = read_struct("<I", fh)[0]
        ret["name"] = read_str(fh)
        ret["unk_2"] = read_struct("<IIII", fh)
        ret["unk_3"] = read_struct("<fff", fh)
        ret["unk_4"] = read_struct("<II", fh)
        ret["rest"] = fh.read()
        return ret

    # def CM3(self, fh):
    #     return len(fh.read())

    def DUM(self, fh):
        ret = {}
        ret["unk_1"] = read_struct("<I", fh)
        ret["num_dummies"] = read_struct("<I", fh)[0]
        ret["unk_2"] = read_struct("<I", fh)
        ret["dummies"] = []
        for _ in range(ret["num_dummies"]):
            dum = {}
            dum["name"] = read_str(fh)
            dum["pos"] = read_struct("<fff", fh)
            dum["rot"] = read_struct("<fff", fh)
            dum["has_ini"] = read_struct("<I", fh)[0]
            if dum["has_ini"]:
                dum['ini']=self.parse_block(fh)
            dum["has_next"] = read_struct("<I", fh)[0]
            ret["dummies"].append(dum)
        assert fh.read() == b"", "Leftover Data"
        return ret

    # def AMC(self, fh):
    #     return len(fh.read())

    # def EMI(self, fh):
    #     return len(fh.read())


# ================================

basedir = r"D:/Games/Deep Silver/Scrapland/extracted/Data.packed"

files = [
    r"Models/Chars/Dtritus/Dtritus.sm3",
    r"Models/Elements/AnilloEstructuraA/AnilloEstructuraA.SM3",
    r"models/elements/antenaa/antenaa.lod1.sm3",
    # r"models/elements/abshield/anm/loop.cm3",
    # r"levels/fake/map/map3d.amc",
    # r"levels/shipedit/map/map3d.dum",
    # r"levels/menu/map/map3d.emi",
    r"Models/Skies/Menu/Sky.SM3",
    r"Levels/Menu/Map/Map3D.SM3",
    r"Models/Elements/AnilloEstructuraD/AnilloEstructuraD.LOD1.SM3",
    # r"levels/menu/map/map3d.amc",
    # r"levels/menu/map/map3d.dum",
    # r"levels/menu/map/scenecamera/anm/loop.cm3",
    r"models/chars/boss/boss.sm3",
    # r"models/chars/boss/anm/boss_walk.cm3",
]

filt = [s.lower() for s in sys.argv[1:]]

for root, folders, files in os.walk(basedir):
    for file in files:
        path = os.path.join(root, file).replace("\\","/")
        if not path.lower().endswith(".dum".lower()):
            continue
        print("Parsing", path)
        p = Parser(debug=True)
        with open(path, "rb") as fh:
            while True:
                parsed = p.parse_block(fh)
                if not parsed:
                    break
                pprint(parsed, compact=False, indent=4)
        print("#" * 50)

