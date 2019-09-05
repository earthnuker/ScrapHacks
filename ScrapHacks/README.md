## Prerequisites

- Visual Studio  2017/2019 (others might work)
- CMake

## Building

Open VS 32-bit command prompt (`vcvars32.bat`)

```batch
mkdir build
cd build
cmake -G "NMake Makefiles" ..
cmake --build . --target install
```

this will drop the compiled files into `./build/bin`

(this has only been tested with a (cracked/deobfuscated) `Scrap.exe` v1.0 with a SHA1 checksum of `d2dde960e8eca69d60c2e39a439088b75f0c89fa`, other version might crash if the memory offsets don't match)