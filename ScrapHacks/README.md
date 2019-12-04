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

this will generate `ScrapHack.pyd` files in `./build`

## Usage

- create a `lib` folder next to `Scrapland.exe`
- copy `ScrapHack.pyd` into said folder
- open the ingame console (Ctrl+^)
- type `import ScrapHack`
- type `$help`
- Done!

## Notes

(this has only been tested with a (cracked/de-obfuscated) `Scrap.exe` v1.0 with a SHA1 checksum of `d2dde960e8eca69d60c2e39a439088b75f0c89fa`, other version might crash if the memory offsets don't match)

