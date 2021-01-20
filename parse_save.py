import sys
from construct import *
from pprint import pprint

ScrapSaveVar = Struct(
    "name" / PascalString(Int32ul, encoding="utf-8"),
    "data" / PascalString(Int32ul, encoding="utf-8"),
)
ScrapSave = "ScarpSaveGame" / Struct(
    "title" / PascalString(Int32ul, encoding="utf-8"),
    "id" / PascalString(Int32ul, encoding="utf-8"),
    "data" / PrefixedArray(Int32ul, ScrapSaveVar),
    Terminated,
)
with open(sys.argv[1], "rb") as sav_file:
    save = ScrapSave.parse_stream(sav_file)
    print("ID:", save.id)
    print("Title:", save.title)
    for var in save.data:
        print("   {}: {}".format(var.name, var.data))

