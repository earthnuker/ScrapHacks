@echo off
setlocal
if "%VSINSTALLDIR%"=="" (
  for /f "usebackq tokens=*" %%i in (`vswhere -latest -find **\vcvarsall.bat`) do (
    call "%%i" x86
  )
)
if not exist build cmake -G"NMake Makefiles" -B build
cmake --build build --target install
endlocal