import sys
import os
from construct import *
import json

save_data = {}

ScrapSaveVar = Struct(
    "name" / PascalString(Int32ul, encoding="windows-1252"),
    "data" / PascalString(Int32ul, encoding="windows-1252"),
)
ScrapSave = "ScarpSaveGame" / Struct(
    "title" / PascalString(Int32ul, encoding="windows-1252"),
    "id" / PascalString(Int32ul, encoding="windows-1252"),
    "data" / PrefixedArray(Int32ul, ScrapSaveVar),
    Terminated,
)

with open(sys.argv[1], "rb") as sav_file:
    save = ScrapSave.parse_stream(sav_file)
    save_data["id"] = save.id
    save_data["title"] = save.title
    save_data["data"] = {}
    for var in save.data:
        save_data["data"][var.name] = var.data
    with open(os.path.basename(sys.argv[1]) + ".json", "w") as of:
        json.dump(save_data, of, indent=4)
