## Features

- read and write memory
- disassemble memory (using zydis)
- change DirectX state
- Draw DirectX overlay (still need to make a useful overlay)
- Dump various data structures to the console
- Assemble and execute code on the fly (using asmtk)
- Can be controlled via keyboard shortcuts (TODO: allow defining own shortcuts for commands)

## Prerequisites

- Visual Studio  2017/2019 (others might work)
- CMake
- Python 3.6 or newer

## Building

Open VS 32-bit command prompt (`vcvars32.bat`) and run the following two commands

```batch
cmake -G"NMake Makefiles" -B build
cmake --build build --target install
```

This will find the Games's installation folder, verify that the version you have is compatible with ScrapHacks and drop the compiled `.pyd` file into the correct folder to be imported

## Getting started

- open the ingame console (Ctrl+^)
- type `import ScrapHack`
- type `$help`

## Config file keys

- patches.asm: map of address->list of assembly instructions
- patches.hex: map of address->hex bytes

Example:

```json
{
    "patches": {
        "hex": {
            "0xDEADBEEF": "BADFOODDEADFEED"
        },
        "asm": {
            "0xBADF00D": [
                "pushad",
                "call 0xf00dbabe",
                "popad",
                "mov eax, 0x42",
                "ret"
            ]
        },
    }
}
```

## Third-Party components used

- Zydis disassembler
- asmJIT/asmTK assembler
- nlohmann/json JSON-parser