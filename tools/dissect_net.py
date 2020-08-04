from construct import *
from binascii import unhexlify
from collections import defaultdict, Counter
import string


class CustomError(SymmetricAdapter):
    def __init__(self, msg):
        super(SymmetricAdapter, self).__init__(Pass)
        self._message = msg

    def _decode(self, obj, context, path):
        # print("Error",path)
        # print(str(context))
        msg = self._message.format(ctx=context, obj=obj)
        raise ValidationError(message=msg, path=this.path)


paket_type = Enum(
    Int8ub,
    GetGameInfo=0x7F01, # 0x7f3d ?
    Connect=0x7F47,
    GameInfo=0xBACE,
    LevelInfo=0x8017,
    Announce=0x4842,
    Disconnect=0x0F02,
    UpdatePlayerInfo=0xC49,  # ???
    # UpdatePlayerInfo=0x8a4c,
    ChatIn=0x921E,
    ChatOut=0x0A1E,
    # Movement=0x802
)

paket_subtype = Enum(
    Int8ub
)


packet_types = {
    "Movement": Struct("data" / GreedyBytes),
    "ChatIn": Struct(
        "unk" / Int16ub,
        "unk_2" / Int8ub,
        "msg" / PascalString(Int8ub, "utf-8"),
        "rest" / GreedyBytes,
    ),
    "ChatOut": Struct(
        "unk" / Int16ub,
        "unk_2" / Int8ub,
        "msg" / PascalString(Int8ub, "utf-8"),
        "rest" / GreedyBytes,
    ),
    "UpdatePlayerInfo": Struct(
        "data" / GreedyBytes
        # "name"/PascalString(Int32ub,"utf-8"),
        # "ship"/PascalString(Int8ub,"utf-8"),
        # "max_life"/Int8ub,
        # "player_char"/PascalString(Int16ub,"utf-8"),
        # "engines"/PascalString(Int8ub,"utf-8")[4],
        # "weapons"/PascalString(Int8ub,"utf-8"),
        # "team_id"/Int32ul
    ),
    "Announce": "info" / CString("utf-8"),
    "GetGameInfo": Const(b"\x00\x00\x07"),
    "Disconnect": Const(b"\x00\x0c\x02"),
    "GameInfo": Struct(
        "version_minor" / Int8ul,
        "version_major" / Int8ul,
        "port" / Int16ul,
        "max_players" / Int16ul,
        "curr_players" / Int16ul,
        "name" / FixedSized(0x20, CString("utf-8")),
        "mode" / FixedSized(0x10, CString("utf-8")),
        "map" / Bytes(2),
        "rest" / GreedyBytes,
    ),
    "Connect": Struct(
        "name" / PascalString(Int32ub, "utf-8"),
        "ship" / PascalString(Int8ub, "utf-8"),
        "max_life" / Int8ub,
        "player_char" / PascalString(Int16ub, "utf-8"),
        "engines" / PascalString(Int8ub, "utf-8")[4],
        "weapons" / PascalString(Int8ub, "utf-8"),
        "team_id" / Int32ul,
    ),
    "LevelInfo": Struct(
        "path" / PascalString(Int32ub, "utf-8"),
        "mode" / PascalString(Int8ub, "utf-8"),
        "rest" / GreedyBytes,
    ),
}

default = "Unknown ID" / Struct("data" / GreedyBytes)
# CustomError("Invalid ID: 0x{ctx.type:02x}")
packet = Struct(
    "type" / Int8ub,
    "subtype"/ Int8ub
    # "data" / Switch(this.type, packet_types, default=default)
)


printable_chars = set(bytes(string.printable, "ascii")) - set(b"\n\r\t\x0b\x0c")


def is_printable(s):
    return all(c in printable_chars for c in s.rstrip(b"\0"))


def hexdump(data, cols=16, offset=0):
    lines = []
    while data:
        hexdata = " ".join("{:02X}".format(v) for v in data[:cols]).ljust(
            3 * cols - 1, " "
        )
        print_data = "".join(
            [chr(v) if v in printable_chars else "." for v in data[:cols]]
        )
        lines.append("{:04X}   {}   {}".format(offset, hexdata, print_data))
        offset += len(data[:cols])
        data = data[cols:]
    return "\n".join(lines).strip()


def main():
    data_type = Counter()
    with open("netlog.txt", "r") as netlog:
        for line in netlog:
            direction, addr, buffer_addr, data = line.strip().split()
            data = unhexlify(data)
            print(direction, addr, buffer_addr)
            print(hexdump(data))
            print()
            try:
                parsed_data = packet.parse(data)
                data_type["{0} {1:08b}:{2:08b} ({1:02X}:{2:02X})".format(direction, parsed_data.type,parsed_data.subtype)] += len(data)
            except Exception:
                pass
    bar_width = 50
    label = "Data type (main:sub)"
    print("=" * 10, label, "=" * 10)
    max_v = max(data_type.values())
    total = sum(data_type.values())
    for k, v in sorted(data_type.items(), key=lambda v: v[1], reverse=True):
        bar = ("#" * round((v / max_v) * bar_width)).ljust(bar_width, " ")
        print(k, bar, "({}, {:.02%})".format(v, v / total))


if __name__ == "__main__":
    main()
