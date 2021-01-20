# ScrapEngine

- Ingame Scripting Language: Python 1.5.2
- Interesting memory locations and functions are noted in `config.yml`

## Launch options

- `-console`: open external console window on start
- `-wideWindow`: start game in widescreen mode
- `-dedicated`: start in multiplayer dedicated server mode (needs to be used with `-server`)
- `-server`: start in multiplayer server mode
- `-build`: Rebuild `Data.packed` (needs a `filelist.2Bpack`)

## Ingame-Console

(Ctrl+\^ or right click on window title bar and select "switch console") (Handler @ `0x402190`)

* `<Code>`: Evaluate Python code
* `:<Var>`: Get Game Engine Variable
* `:<Var> <Val>`: Set Game Engine Variable
* `?`: Show all Game Engine Variables
* `?<String>`: Show all Game Engine Variables matching `<String>`
* `/<command>`: Run Command defined in `QuickConsole.py`
  * `import quickconsole;quickconsole.%s()`
* `/<command> <arg>,<arg>`: Run function in `QuickConsole.py` with argument(s)
  * `import quickconsole;quickconsole.%s(%s)`

## External Console

(Scene graph debugging?) (Handler @ `0x5f9520`)

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
- `0x8b18f0`: pointer to Models Data (can be dumped using scene graph debugging console)
- `0x8b18f4`: pointer to Scenes Data (can be dumped using scene graph debugging console)
- `0x8b18f8`: pointer to active Models Data (can be dumped using scene graph debugging console)
