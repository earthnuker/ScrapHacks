Open VS 2017 32-bit command prompt (`vcvars32.bat`)

```batch
mkdir build
cd build
cmake -G "NMake Makefiles" -DCMAKE_BUILD_TYPE="Release" -DCMAKE_INSTALL_PREFIX="" ..
cmake --build .
cmake --install .
```

this will drop the compiled files into `./build/bin`

(this has only been tested with `Scrap.exe` with a SHA1 checksum of `d2dde960e8eca69d60c2e39a439088b75f0c89fa`, other version might crash if the memory offsets don't match)