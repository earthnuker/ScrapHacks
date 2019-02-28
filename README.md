# Scrapland Reverse Engineering noted and tools

## Scripts:
* `parse_save.py`: Dumps information extracted from Save file
* `scrapper.py`: Extractor and Repacker for *.packed files, needs the `construct` and `tqdm` python modules and python 3.x
 - Run `scrapper.py -h` for help
* `lib/dbg.py`: general Script for poking around inside the game's scripting system
 - Run `import dbg` inside the Game's Console,
  this will load all builtin modules and enable godmode
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

- [Python 3](https://python.org/) + [Construct](https://construct.readthedocs.io/en/latest/)
- [IDA](https://www.hex-rays.com/products/ida/index.shtml) and [x32dbg](https://x64dbg.com/#start)
- [Reclass.NET](https://github.com/ReClassNET/ReClass.NET)
- [HxD](https://mh-nexus.de/en/hxd/)
