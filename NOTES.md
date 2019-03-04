# Infos
- Engine: ScrapEngine
- Ingame Scripting Language: Python 1.5.2

# Functions identified:

## Ingame-Console (Ctrl+\^ or right click on titlebar and select "switch console") (Handler@0x402190):
* `<Command>`: Try to evaluate Command as Python expression
* `:<Var>`: Get Game Engine Global Variable
* `:<Var> <Val>`: Set Game Engine Global Variable
* `?`: Show all Global Variable
* `?<String>`: Show all Global Variable matching <String>
* `/<command>`: Run Command defined in QuickConsole.py(c) 'import quickconsole;quickconsole.%s()'
* `/<command> <arg>,<arg>`: Run function in QuickConsole.py(c) with argument(s) 'import quickconsole;quickconsole.%s(%s)'

## External Console (Scenegraph Debugging?) (Handler@0x5f9520):
* `listar luces`
* `listar`
* `arbol` (Patch Scrap.exe@offset 0x314bc9 replace 0x20 with 0x00 (or just type `arbol ` with the space at the end))
* `mem`
* `ver uniones`
* Easter Eggs:
  * `imbecil`
  * `idiota`
  * `capullo`

## Python Stuff
- Modules List @ 0x79C698 (Module Name as `char*`  followed by Pointer to Init Function)
- InitPyMod @ 0x5A8FB0
- PyExec @ 0x5A8390

# Other Functions:

- FindEntity @ 0x404a50
- HashTable hashfunc @ 0x404bb0
- Register C Callback @ 0x404460
- Load Game @ 0x417470
- File opening functions @ 0x5e3800 and 0x419950
- Scrap_Debug_Init @ 0x403370
- Scrap_Init @ 0x401770
- Scrap_InitPy @ 0x4026d0
- Scrap_OpenPak @ 0x41ab50
- PyExec @ 0x5a8390
- Setup_Game_Var @ 0x414570
- Throw_Assertion @ 0x5fbc50
- m3d.ini loader @ 0x5f7000
- SM3 Scene Loader @ 0x650f80 (?)
- M3D Model Loader @ 0x6665a0 (??)
- World_Init @ 0x479b20 (???)

# Data Structures

## Game World/State Pointer @ 0x7fe944

Points to GameState struct

| Offset | Type     | Description                 |
| ------ | -------- | --------------------------- |
| 0x0    | void**   | Virtual Method Table        |
| 0x4    | uint32_t | Size of Entity Hashtable    |
| 0x8    | void**   | Pointer to Entity Hashtable |
| 0x330  | float[3] | Time (why 3 times?)         |
| 0x1c6c | float    | Alarm level                 |
| 0x1C68 | float    | Alarm Grow Level            |

## Entity Hash Table

Hashfunction used: [PJW](https://en.wikipedia.org/wiki/PJW_hash_function) (Same parameters as the example implementation)

Entry format:

| Offset | Type        | Description                    |
| ------ | ----------- | ------------------------------ |
| 0x0    | void*       | Pointer to data                |
| 0x4    | const char* | key as string                  |
| 0x8    | void*       | Pointer to next entry in chain |

Data format:

| Offset | Type        | Description          |
| ------ | ----------- | -------------------- |
| 0x0    | void**      | Virtual Method Table |
| 0x4    | const char* | name as string       |
| 0x14   | void*       | pointer to self      |
| 0x28   | float[3]    | Position             |

# File Formats

## *.packed File Format:
```
Header:
    "BFPK\0\0\0\0"
    Int32ul: number of files
    for each file:
        Int32ul: path length
        String: path
        Int32ul: size
        Int32ul: offset in file
```

## Loading Custom Content (not really working)
1. Create a folder `mods`
2. Drop a `*.packed` file into it

## Interesting file:
* m3d.ini: Rendering Engine Configuration
* scripts/: Game Engine Scripts


# How to enable External Console:
1. exctract `Data.packed`
2. in m3d.ini uncomment (remove `;`) "ConsolaWnd" (GUI Console) or "ConsolaTxt" (Text Console) and set the value to "SI"
3. repack "Data.packed"

or right click on the title bar (in windowed mode) and click "Switch Console"

or Use a custom Content Pack (**untested!**)

# Misc. Interesting things
- sys.path contains "./lib" so you can load your own Python Modules
