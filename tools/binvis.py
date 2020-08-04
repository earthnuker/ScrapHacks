import struct
from collections import OrderedDict, ChainMap


class LittleEndian:
    byteorder = "<"


class BigEndian:
    byteorder = ">"


class NativeEndian:
    byteorder = "@"


class Field:
    def __init__(self, struct_type=None, size=None, byteorder=None):
        self.struct = struct_type
        self.size = size
        self.byteorder = byteorder
        self.data = None
        self.parsed = False

    def parse(self, data):
        return


class ParserMeta(type):
    def __new__(cls, name, bases, namespace, **kwargs):
        if object in bases:
            return type.__new__(cls, name, bases, dict(namespace))
        fields = []
        for item_name, item_value in namespace.items():
            if isinstance(item_value, Field):
                fields.append(item_name)
        ret = super().__new__(cls, name, bases, namespace)
        ret._fields = fields
        return ret

    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        return OrderedDict()


class Parser(metaclass=ParserMeta):
    def __init__(self, data):
        for field in self._fields:
            print(field, getattr(self, field))


class ChunkedHeader(Parser, LittleEndian):
    size = Field("I")
    data = Field(size=size)


print(ChunkedHeader(b""))
