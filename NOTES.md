# Infos

- Engine: ScrapEngine/Mercury Engine
- Ingame Scripting Language: Python 1.5.2
- Interesting memory locations and functions are noted in `config.yml`

# Launch options:

- `-console`: open external console window on start
- `-wideWindow`: start game in widescreen mode
- `-dedicated`: start in mutliplayer dedicated server mode (needs to be used with `-server`)
- `-server`: start in multiplayer server mode

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

* `listar luces` List lights in scene
* `listar` list models in scene
* `arbol <model_name>` show details for model 
* `mem` (doesn't do anything?)
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

Check `config.yml` for full list

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

## Packed Index struct (array of 0x80 entries @ `0x7fc1b0`)
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


## Game engine Variables Hashtable @ `0x7fbe50`

## Game engine Variables @ `0x7fbe4c`

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

| Value | Type            |
|-------|-----------------|
| `0x1` | const char*     |
| `0x2` | int32_t         |
| `0x3` | List of Defines |
| `0x4` | float           |
| `0x5` | function        |
| `0x6` | Script function |

## Game World/State Pointer @ `0x7fe944`

Points to World struct

| Offset | Type                     | Description                            |
|--------|--------------------------|----------------------------------------|
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

## cPyEntity structure

| Offset | Type     | Description          |
|--------|----------|----------------------|
| 0x0000 | `void**` | Virtual Method Table |
| 0x0004 | `char*`  | Name                 |
| 0x0008 | `void*`  | ???                  |


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
|--------|---------------|--------------------------|
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

# Netplay protocol (WIP)

Game Info Packet

```
Server 'B':FZ (0/10) Ver 1.0 at 192.168.99.1:28086
[0-3] header/ID?
[4-5] port (16-bit)
[6-7] max_players (16-bit)
[8-9] curr_player (16-bit)
[10-x] server name (char*)

           0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F  0123456789ABCDEF
0019fdc0  ba ce 00 01 b6 6d 0a 00 00 00 42 00 30 fe 19 00  .....m....B.0...
0019fdd0  ff ff ff ff 27 2b b3 9b c7 3e bb 00 9c af 29 00  ....'+...>....).
0019fde0  db 69 00 00 00 00 00 00 00 00 44 65 61 74 68 4d  .i........DeathM
0019fdf0  61 74 63 68 00 00 00 00 ff ff 46 5a 00 4a 91 f0  atch......FZ.J..
0019fe00  92 8b 57 4e 7f 00 00 00 10 21 fe 38 0d ae 00 00  ..WN.....!.8....
0019fe10  f0 ce f3 36 a0 e8 0b 77 a0 e8                    ...6...w..
```


Player Join Packet

```
[0-3] header/ID?
[6-x] Player name

           0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F  0123456789ABCDEF
09c9dfe8  7f 47 00 00 00 0e 55 6e 6e 61 6d 65 64 20 50 6c  .G....Unnamed Pl
09c9dff8  61 79 65 72 06 53 42 6f 73 73 31 b9 00 07 50 5f  ayer.SBoss1...P_
09c9e008  42 65 74 74 79 06 4d 42 4f 53 53 31 06 4d 42 4f  Betty.MBOSS1.MBO
09c9e018  53 53 31 00 00 10 30 2c 31 35 2c 30 2c 30 2c 31  SS1...0,15,0,0,1
09c9e028  35 2c 31 35 2c 31 02 00 00 00                    5,15,1....
```

| Message                                  | Description                                                       |
|------------------------------------------|-------------------------------------------------------------------|
| `5c68625c32383230395c73637261706c616e64` | "Scrapland Server" announcement broadcast (`\hb\28209\scrapland`) |
| `7f01000007`                             | Retrieve Game info                                                |
| `48423d35323932322c3235363a323830383600` | Connection Information (`HB=52922,256:28086`)                     |

# [Notes](NOTES.md)

## File Formats

- [Chunked](file_formats/chunked.md)
- [Packed](file_formats/packed.md)
- [AI Pathfinding Graph](file_formats/ai_path.md)


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