# Scrapland Reverse Engineering notes and tools


## Note!

All memory addresses are only valid for an unprotected `Scrap.exe` v1.0 with a SHA1 checksum of `d2dde960e8eca69d60c2e39a439088b75f0c89fa` , other version will crash if the memory offsets don't match and you try to inject ScrapHacks

[Computer Bild Spiele Issue 2006/08](https://archive.org/download/cbs-2006-08-coverdisc/) Contains a full version of the game which was used as the basis for this project

## Scripts

* `tools/rbingrep.py`: Search for pattern in all files and generate radare2 script to find all references (currently configured to search for chunked file section headers)
* `frida/`: Scripts for use with Frida
* `parse_chunked.py`: WIP Parser for the game's chunked data format (Models, Animations, Maps)
* `save_to_json.py`: Convert game save to JSON
* `scrapper.py`: Extractor and Repacker for *.packed files, needs the `construct` and `tqdm` python modules and python 3.x
 - Run `scrapper.py -h` for help
* `r2_analyze.py`: uses radare2 to parse and label a lot of interesting stuff in the `Scrap.exe` binary
* `lib/dbg.py`: general Script for poking around inside the game's scripting system
 - Run `import dbg;dbg.init()` inside the Game's Console,
  this will load all builtin modules, ScrapHacks and enable godmode
 - The dbg module also enables writing to the ingame console using `print <var>`
  and defines two global functions s_write() and e_write() for writing to the Ingame Console's Stdout and Stderr Stream
 - `dbg.menu()` Displays the Game's built in Debug Menu (doesn't work properly)
 - `dbg.enable_all_conv()` allows you to "overwrite" any character, even if they are protected/invulnerable
 - `dbg.become(name)` allows you to transform into any character
 - `dbg.helplib()` generates a file `helplib.txt` in the Game's folder containing all available Documentation for all available classes and functions
 - `dbg.settrace()` Logs all Python function calls together with their arguments into a  `dbg.txt` file inside the Game's folder

## [ScrapHacks](ScrapHacks/README.md)

WIP Memory hacking library

## [Notes](NOTES.md)

# Tools used:

- Binary parsing:
  - [HxD](https://mh-nexus.de/en/hxd/) for initial file analysis
  - [Python 3](https://python.org/) + [Construct](https://construct.readthedocs.io/en/latest/) for binary parsing
  - [Kaitai Struct](http://kaitai.io/) for binary parsing
- Static analysis:
  - [IDA](https://www.hex-rays.com/products/ida/index.shtml) initialy used, later replaced by radare2 and Cutter
  - [radare2](https://www.radare.org/)
  - [Cutter](https://cutter.re/)
- Dynamic analysis:
  - [x64dbg](https://x64dbg.com/) for dynamic analysis
  - [Reclass.NET](https://github.com/ReClassNET/ReClass.NET) to analyze structures and classes in memory
  - [Frida](https://frida.re/) for tracing and instrumenting functions