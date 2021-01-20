import lief
import sys

exit("WIP, not really useful yet")

Scrap = lief.PE.parse(sys.argv[1])

data = []

section_data = lief.PE.Section(".hdata")
section_data.content = data
section_data.virtual_address = 0x8000
section_data.characteristics = (
    lief.PE.SECTION_CHARACTERISTICS.CNT_INITIALIZED_DATA
    | lief.PE.SECTION_CHARACTERISTICS.MEM_READ
)
sh = Scrap.add_library("_ScrapHack.pyd")
sh.add_entry("Init")

builder = lief.PE.Builder(Scrap)

builder.build_imports(True).patch_imports(True).build()

builder.write("Scrap_mod_sh.exe")
