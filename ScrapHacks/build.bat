@echo off
setlocal
set SCRAPLAND_DIR=%1
if "%VSINSTALLDIR%"=="" (
  for /f "usebackq tokens=*" %%i in (`vswhere -latest -find **\vcvarsall.bat`) do (
    call "%%i" x86
  )
)
if "%VSINSTALLDIR%"=="" (
  echo "VSINSTALLDIR" not set something is wrong!
  exit
) else (
  if not exist build cmake -G"NMake Makefiles" -B build
  if "%2"=="--run" (
    cmake --build build --target run
  ) else (
    cmake --build build --target install
  )
)
:END
endlocal