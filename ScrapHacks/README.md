Open VS 2017 32-bit command prompt (`vcvars32.bat`)

```batch
mkdir build
cd build
cmake -G "NMake Makefiles" -DCMAKE_BUILD_TYPE="Release" -DCMAKE_INSTALL_PREFIX="" ..
cmake --build .
cmake --install .
```

this will drop the compiled files into `./build/bin`