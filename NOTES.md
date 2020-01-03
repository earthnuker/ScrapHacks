# Infos

- Engine: ScrapEngine
- Ingame Scripting Language: Python 1.5.2
- Interesting memory locations and functions are noted in `config.yml`

# Launch options:

- `-console`: open external console window on start
- `-wideWindow`: start game in widescreen mode

# Functions identified:

## Ingame-Console (Ctrl+\^ or right click on titlebar and select "switch console") (Handler@`0x402190`):

* `<Command>`: Try to evaluate Command as Python expression
* `:<Var>`: Get Game Engine Global Variable
* `:<Var> <Val>`: Set Game Engine Global Variable
* `?`: Show all Global Variable
* `?<String>`: Show all Global Variable matching `<String>`
* `/<command>`: Run Command defined in `QuickConsole.py`: `import quickconsole;quickconsole.%s()`
* `/<command> <arg>,<arg>`: Run function in `QuickConsole.py` with argument(s) `import quickconsole;quickconsole.%s(%s)`

## External Console (Scenegraph Debugging?) (Handler @ `0x5f9520`):

* `listar luces`
* `listar`
* `arbol` (Patch Scrap.exe@offset 0x314bc9 replace 0x20 with 0x00 (or just type `arbol ` with a space at the end))
* `mem`
* `ver uniones`
* Easter Eggs:
  * `imbecil`
  * `idiota`
  * `capullo`


## Other interesting Memory Addresses

- `0x852914`: D3D8-Device pointer
- `0x7FCC00`: number of opened `.packed` files
- `0x84cb64`: pointer to console command handler
- `0x7fac84`: pointer to C++ callback list structure
- `0x80b2cc`: pointer to ActionClassList (???)
- `0x807a20`: pointer to SScorer (ingame GUI/Menu/Text system) structure (???)
- `0x80a398`: pointer to SoundSystem (???)
- `0x8b18f0`: pointer to Models Data (can be dumped using scenegraph debugging console)
- `0x8b18f4`: pointer to Scenes Data (can be dumped using scenegraph debugging console)
- `0x8b18f8`: pointer to active Models Data (can be dumped using scenegraph debugging console)

## Hash-function used in Hash-Tables

```c
unsigned long hash(const unsigned char *s)
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


## Other Functions:

Check `r2_analyze.py` for full list

## File Index struct @ `0x7fcbec`

```cpp

struct FileEntry {
  uint32_t offset;
  uint32_t size;
  uint32_t unk; // seems to always be 0xBADFOO1
  unsigned char* path;
  FileEntry* next; // next entry in hashtable chain
}

struct FileIDX {
  uint32_t size;
  FileEntry** entries;
};
```

## Packed Index struct (array @ `0x7fc1b0`)
```cpp
struct PackedIDX {
  void** VMT;
  unsigned char* filename;
  uint32_t locked; // not sure
  void* data;
  uint32_t seek;
}
```

## C(++)-Callbacks @ `0x7fac84`

Structure:

```cpp
struct CPP_Callback {
  const char* name;
  void* func;
  CPP_Callback* left;
  CPP_Callback* right;
}
```

## Game engine Variables Pointer @ `0x7FBE4C`

Structure:

```cpp
struct GameVar {
  GameVar* next;
  const char* name;
  const char* desc;
  uint8_t subtype;
  uint8_t type;
  uint16_t unk;
  void* value;
  void* def_value;
}
```

Types

| Value  | Type                    |
| ------ | ----------------------- |
| `0x10` | const char*             |
| `0x20` | int32_t                 |
| `0x30` | User Control Definition |
| `0x40` | float                   |
| `0x60` | Callback function       |

## Game World/State Pointer @ `0x7fe944`

Points to World struct

| Offset | Type                     | Description                            |
| ------ | ------------------------ | -------------------------------------- |
| 0x0000 | `void**`                 | Virtual Method Table                   |
| 0x0004 | `uint32_t`               | Size of Entity Hashtable               |
| 0x0008 | `void**`                 | Pointer to Entity Hashtable            |
| 0x0288 | `pyEntity*`              | UsrEntity[0]                           |
| 0x028C | `pyEntity*`              | UsrEntity[1]                           |
| 0x0290 | `pyEntity*`              | UsrEntity[2]                           |
| 0x0294 | `pyEntity*`              | UsrEntity[3]                           |
| 0x02B8 | `uint32_t`               | Number of entity lists                 |
| 0x02BC | `void**`                 | Pointer to entity list Hashtable       |
| 0x0330 | `float[3]`               | Time (why 3 times?)                    |
| 0x1C6C | `float`                  | Alarm level                            |
| 0x1C68 | `float`                  | Alarm Grow Level                       |
| 0x2158 | `float`                  | Used in `World_Init`                   |
| 0x2170 | `???`                    | Used in `World_Init`                   |
| 0x2180 | `float`                  | Used in `World_Init`                   |
| 0x2188 | `void*`                  | Used in `World_Init`                   |
| 0x218C | `void*`                  | Used in `World_Init`                   |
| 0x2190 | `float`                  | Used in `World_Init`                   |
| 0x2198 | `void*`                  | Used in `World_Init`                   |
| 0x219C | `void*`                  | Used in `World_Init`                   |
| 0x21A0 | `void**`                 | Used in `World_Init` (VTable pointer?) |
| 0x21B4 | `void**`                 | Used in `World_Init` (VTable pointer?) |
| 0x21C8 | `???`                    | Used in `World_Init`                   |
| 0x2204 | `uint32_t` or `uint16_t` | Used in `World_Init`                   |
| 0x2230 | `float`                  | Used in `World_Init`                   |
| 0x2238 | `???`                    | Used in `World_Init`                   |
| 0x2254 | `float`                  | Used in `World_Init`                   |

## Entity Hash Table

Hash-function used: [PJW](https://en.wikipedia.org/wiki/PJW_hash_function) (Same parameters as the example implementation)

Entry format:

```cpp
struct HT_Entry {
  void* data;
  const char* key;
  HT_Entry* next;
}
```

Data format:

| Offset | Type          | Description              |
| ------ | ------------- | ------------------------ |
| 0x0    | `void**`      | Virtual Method Table (?) |
| 0x4    | `const char*` | name as string           |
| 0x14   | `void*`       | pointer to self (why?)   |
| 0x28   | `float[3]`    | Position in Game World   |

## EntityList Hash Table

Attributes:
- `Near`
- `First`
- `Num`
- `OnDeath`
- `OnDamage`

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

# Virtual Method Tables:

check `r2_analyze.py` for full list

## Loading Custom Content (not really working)

1. Create a folder `mods`
2. Drop a `*.packed` file into it
3. Change `Scrap.cfg` as follows
   1. Add `ModPathName = mods`
   2. Add `ModFileName = <filename>`

## Interesting file inside `Data.packed`

* `m3d.ini`: Rendering Engine Configuration
* `scripts/`: Game Engine Scripts


# How to enable External Console:

1. Right click on the title bar (in windowed mode) and click "Switch Console"
2. or Use a custom Content Pack (**untested!**)

# How to enable Scenegraph debugging console

1. extract `Data.packed`
2. in m3d.ini uncomment (remove `;`) `ConsolaWnd` (GUI Console) and/or `ConsolaTxt` (Text Console) and set the value to `SI`
3. repack `Data.packed`

# Misc. Interesting things

- `sys.path` contains "./lib" so you can import your own Python Modules
- Games crashes when starting a multiplayer server and feeding it random UDP data

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
  - id: version
    contents: [0,0,0,0]
    doc: File Version
  - id: num_files
    type: u4
    doc: Number of files
  - id: files
    type: file_entry
    repeat: expr
    repeat-expr: num_files
    doc: Entry for each file
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

# TODO:

- Figure out how C++ Callbacks work
- Figure out SM3 (Models), CM3 (Animations) file formats
- Figure out rest of World structure
- Figure out rest of Entity structure