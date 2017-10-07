from construct import *
from pprint import pprint
ScrapSaveStr = Struct(
    'length'/Int32ul,
    'data'/String(this.length,encoding='utf-8'),
    )
ScrapSaveVar = Struct(
    'v_name_size'/Int32ul,
    'v_name'/String(lambda ctx: ctx.v_name_size,encoding='utf-8'),
    'v_data_size'/Int32ul,
    'v_data'/String(lambda ctx: ctx.v_data_size,encoding='utf-8'),
)
ScrapSave = 'ScarpSaveGame'/Struct(
                   'title'/ScrapSaveStr,
                   'id'/ScrapSaveStr,
                   'num_vars'/Int32ul,
                   'data'/ScrapSaveVar[this.num_vars],
                   Terminated
                   )
with open("Save0.sav", 'rb') as sav_file:
    save = ScrapSave.parse_stream(sav_file)
    pprint(save)
    #for block in save.data:
    #    print("{}: {}".format(block.v_name, block.v_data))
