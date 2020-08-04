# ScrapHack python interface
import _ScrapHack


class Mem:
    def __init__(self):
        return

    def __getitem__(self, key):
        print("GI:", key)

    def __setitem__(self, key, value):
        print("SI:", key, value)

Mem = Mem()

def asm(code,address=0):
    """
    asm(code, address):
    
    Assemble code at address
    """
    return _ScrapHack.asm(address, code)
