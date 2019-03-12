# Infos
- Engine: ScrapEngine
- Ingame Scripting Language: Python 1.5.2

# Functions identified:

## Ingame-Console (Ctrl+\^ or right click on titlebar and select "switch console") (Handler@0x402190):
* `<Command>`: Try to evaluate Command as Python expression
* `:<Var>`: Get Game Engine Global Variable
* `:<Var> <Val>`: Set Game Engine Global Variable
* `?`: Show all Global Variable
* `?<String>`: Show all Global Variable matching `<String>`
* `/<command>`: Run Command defined in `QuickConsole.py`: `import quickconsole;quickconsole.%s()`
* `/<command> <arg>,<arg>`: Run function in `QuickConsole.py` with argument(s) `import quickconsole;quickconsole.%s(%s)`

## External Console (Scenegraph Debugging?) (Handler@0x5f9520):
* `listar luces`
* `listar`
* `arbol` (Patch Scrap.exe@offset 0x314bc9 replace 0x20 with 0x00 (or just type `arbol ` with a space at the end))
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

## Other Functions:

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
- World_DeInit @ 0x402510

# Data Structures

## Game World/State Pointer @ `0x7fe944`

Points to World struct

| Offset | Type       | Description                      |
|--------|------------|----------------------------------|
| 0x0000 | `void**`   | Virtual Method Table             |
| 0x0004 | `uint32_t` | Size of Entity Hashtable         |
| 0x0008 | `void**`   | Pointer to Entity Hashtable      |
| 0x02B8 | `uint32_t` | Number of entity lists           |
| 0x02BC | `void**`   | Pointer to entity list Hashtable |
| 0x0330 | `float[3]` | Time (why 3 times?)              |
| 0x1C6C | `float`    | Alarm level                      |
| 0x1C68 | `float`    | Alarm Grow Level                 |
| 0x2158 | `???`      | Used in `World_Init`             |
| 0x2170 | `???`      | Used in `World_Init`             |
| 0x2180 | `???`      | Used in `World_Init`             |
| 0x2188 | `???`      | Used in `World_Init`             |
| 0x218C | `???`      | Used in `World_Init`             |
| 0x2190 | `???`      | Used in `World_Init`             |
| 0x2198 | `???`      | Used in `World_Init`             |
| 0x219C | `???`      | Used in `World_Init`             |
| 0x21A0 | `???`      | Used in `World_Init`             |
| 0x21B4 | `???`      | Used in `World_Init`             |
| 0x21C8 | `???`      | Used in `World_Init`             |
| 0x2204 | `???`      | Used in `World_Init`             |
| 0x2230 | `???`      | Used in `World_Init`             |
| 0x2238 | `???`      | Used in `World_Init`             |
| 0x2254 | `???`      | Used in `World_Init`             |


## Entity Hash Table

Hash-function used: [PJW](https://en.wikipedia.org/wiki/PJW_hash_function) (Same parameters as the example implementation)

Entry format:

| Offset | Type          | Description                    |
|--------|---------------|--------------------------------|
| 0x0    | `void*`       | Pointer to data                |
| 0x4    | `const char*` | key as `char*`                 |
| 0x8    | `void*`       | Pointer to next entry in chain |

Data format:

| Offset | Type          | Description              |
|--------|---------------|--------------------------|
| 0x0    | `void**`      | Virtual Method Table (?) |
| 0x4    | `const char*` | name as string           |
| 0x14   | `void*`       | pointer to self (why?)   |
| 0x28   | `float[3]`    | Position in Game World   |

## Game Window Object (?) Pointer @ `0x7fa380`

| Offset | Type          | Description          |
|--------|---------------|----------------------|
| 0x0000 | `void**`      | Virtual Method Table |
| 0x0004 | `const char*` | Some Model Name (?)  |
| 0x0008 | `void*`       | Pointer to something |
| 0x000C | `void*`       | Ditto                |

# File Formats

## .packed File Format:
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
3. Change `Scrap.cfg` as follows
   1. Add `ModPathName = mods`
   2. Add `ModFileName = <filename>`

## Interesting file:
* `m3d.ini`: Rendering Engine Configuration
* `scripts/`: Game Engine Scripts


# How to enable External Console:
1. exctract `Data.packed`
2. in m3d.ini uncomment (remove `;`) `ConsolaWnd` (GUI Console) and/or `ConsolaTxt` (Text Console) and set the value to `SI`
3. repack `Data.packed`

or right click on the title bar (in windowed mode) and click "Switch Console"

or Use a custom Content Pack (**untested!**)

# Misc. Interesting things
- sys.path contains "./lib" so you can load your own Python Modules

# Code Snippets

## [Kaitai Struct](http://kaitai.io/) Parser for .packed files
```yaml
meta:
  id: packed
  application: Scrapland
  file-extension: packed
  endian: le
  xref: http://wiki.xentax.com/index.php/Scrapland_PACKED
  license: MIT
  encoding: UTF-8
seq:
  - id: magic
    contents: BFPK
    doc: File Magic
  - id: magic2
    contents: [0,0,0,0]
    doc: Second File Magic
  - id: num_files
    type: u4
    doc: Number of files
  - id: files
    type: file_entry
    repeat: expr
    repeat-expr: num_files
    doc: Directory entry for each file
types:
  file_entry:
    seq:
      - id: path_len
        type: u4
        doc: Length of file path
      - id: path
        type: str
        size: path_len
        doc: File path
      - id: size
        type: u4
        doc: File size
      - id: offset
        type: u4
        doc: Absoulte File offset
    instances:
      data:
        pos: offset
        size: size
```

## Hashfunction used in Entity Hash-Table

```c
unsigned long ElfHash(const unsigned char *s)
{
    unsigned long h = 0, high;
    while ( *s )
    {
        h = ( h << 4 ) + *s++;
        if ( high = h & 0xF0000000 )
            h ^= high >> 24;
        h &= ~high;
    }
    return h;
}
```