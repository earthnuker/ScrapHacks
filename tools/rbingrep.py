import binascii
import os
import sys

exe_file = os.path.abspath(sys.argv[1])

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


markers = [ "AMC", "ANI", "CAM", "CM3", "CMSH", "DUM", "EMI", "EVA", "INI", "LFVF", "LUZ", "MAP", "MAT", "MD3D", "NAE", "NAM", "PORT", "QUAD", "SCN", "SM3", "SUEL", "TRI", ]

blocksize = 1024 * 4
for marker in markers:
    pattern = bytes(marker, "utf8").ljust(4, b"\0")
    res = search(pattern, exe_file)
    print("?e "+marker)
    for addr in res:
        print("/r `?P {}`".format(hex(addr)))
