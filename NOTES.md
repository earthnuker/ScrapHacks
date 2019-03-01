# Infos
- Engine: ScrapEngine
- Ingame Scripting Language: Python 1.5.2

# Ingame-Console (Ctrl+\^ or right click on titlebar and select "switch console") (Handler@0x402190):
* `<Command>`: Try to evaluate Command as Python expression
* `:<Var>`: Get Game Engine Global Variable
* `:<Var> <Val>`: Set Game Engine Global Variable
* `?`: Show all Global Variable
* `?<String>`: Show all Global Variable matching <String>
* `/<command>`: Run Command defined in QuickConsole.py(c) 'import quickconsole;quickconsole.%s()'
* `/<command> <arg>,<arg>`: Run function in QuickConsole.py(c) with argument(s) 'import quickconsole;quickconsole.%s(%s)'

# External Console (Scenegraph Debugging?) (Handler@0x5f9520):
* `listar luces`
* `listar`
* `arbol` (Patch Scrap.exe@offset 0x314bc9 replace 0x20 with 0x00 (or just type `arbol ` with the space at the end))
* `mem`
* `ver uniones`
* Easter Eggs:
 - `imbecil`
 - `idiota`
 - `capullo`

# Python Stuff
- Modules List @ 0x79C698 (Module Name as `char*`  followed by Pointer to Init Function)
- InitPyMod @ 0x5A8FB0
- PyExec @ 0x5A8390

## m3d.ini loader @ 0x05f7000

## SM3 Scene Loader @ 0x650f80 (?)

## M3D File Loader @ 0x6665a0 (??)

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
