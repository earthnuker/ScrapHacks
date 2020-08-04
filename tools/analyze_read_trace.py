import msgpack as mp
import sys
import os
from tqdm import tqdm
import struct
import binascii
import string
import re
from binascii import hexlify

def gen():
    with open(sys.argv[1], "rb") as fh:
        size = os.stat(sys.argv[1]).st_size
        progbar = tqdm(total=size, unit="bytes", unit_scale=True, unit_divisor=1024)
        pos = 0
        for entry in mp.Unpacker(fh, raw=True):
            progbar.update(fh.tell() - pos)
            pos = fh.tell()
            for k in entry.copy():
                k_s = str(k, "utf8")
                if k_s not in ["data", "stack", "timestamp"]:
                    entry[k] = str(entry.pop(k), "utf8")
                entry[k_s] = entry.pop(k)
            entry["stack"] = "|".join(
                ["{:08X}".format(int(str(v, "utf8"), 16)) for v in entry["stack"][::-1]]
            )
            yield entry



def strdump(data):
    printable_chars = set(bytes(string.printable, "ascii")) - set(b"\n\r\t\x0b\x0c")
    return "".join(chr(c) if c in printable_chars else "." for c in data)

def tohex(data):
    return str(hexlify(data), "utf8").upper()


# best=sorted(tqdm(gen(),ascii=True),key=lambda v:len(v['data']),reverse=True)

# def score(entry):
#     return len(entry['data'])

# def analyze(entry):
#     data=entry['data']
#     entry['infos'] = {
#         'len':len(data),
#     }
#     for bo in "><":
#         for t in "hHiIlLqQefd":
#             fmt="{}{}".format(bo,t)
#             if len(data)%struct.calcsize(fmt)==0:
#                 entry['infos'][fmt]=[v[0] for v in struct.iter_unpack(fmt,data)]
#     return entry

filters=[re.compile(s) for s in sys.argv[2:]]

with open("all.log", "w") as of:
    for entry in gen():
        fm=[(f.match(entry['filename']) is not None) for f in filters]
        if filters and not any(fm):
            continue
        entry["data_len"] = len(entry["data"])
        entry["str"] = strdump(entry["data"])
        entry["data"] = tohex(entry["data"])
        print(
            "{timestamp} {block_id} {filename} {data_len:08X} {data} {str}".format(**entry), file=of
        )
