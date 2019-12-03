cmake_minimum_required(VERSION 3.1)
cmake_policy(VERSION ${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION})

project(ScrapHacks
        VERSION 1.0
        DESCRIPTION "Scrapland memory hacking library"
        LANGUAGES CXX)
set(CMAKE_BUILD_TYPE "Release")
set(CMAKE_INSTALL_PREFIX "${CMAKE_BINARY_DIR}")
if(WIN32)
  if(MSVC)
    # ensure we use minimal "windows.h" lib without the crazy min max macros
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /D \"WIN32_LEAN_AND_MEAN\"")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /D \"NOMINMAX\"")
    # disable SAFESEH - to avoid "LNK2026: module unsafe"
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /D \"SAFESEH:NO\"")
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} /SAFESEH:NO")
    set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} /SAFESEH:NO")
    set(CMAKE_MODULE_LINKER_FLAGS "${CMAKE_MODULE_LINKER_FLAGS} /SAFESEH:NO")
  endif(MSVC)
endif(WIN32)

include(ExternalProject)

ExternalProject_Add(
  DirectX
  PREFIX ${CMAKE_CURRENT_BINARY_DIR}
  CONFIGURE_COMMAND ""
  BUILD_COMMAND ""
  INSTALL_COMMAND ""
  URL
    https://archive.org/download/DirectX.8.0a.SDK_includes_libs_only/DirectX.8.0a.SDK.zip
  URL_HASH SHA1=39f168336d0df92ff14d62d5e3aef1b9e3191312)
ExternalProject_Get_Property(DirectX SOURCE_DIR)
include_directories(AFTER ${SOURCE_DIR}/8.0/include/)
link_directories(AFTER ${SOURCE_DIR}/8.0/lib/)

find_package (Python3 3.6 REQUIRED COMPONENTS Interpreter)

add_custom_target(
  MAKE_D3D8_VMT ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/src/make_D3D8_VMT.py ${CMAKE_CURRENT_SOURCE_DIR}/src/D3D8_VMT.hpp ${SOURCE_DIR}/8.0/include/d3d8.h
  DEPENDS DirectX
)

# ExternalProject_Add(
#   Python152
#   PREFIX ${CMAKE_CURRENT_BINARY_DIR}
#   CONFIGURE_COMMAND ""
#   BUILD_COMMAND ""
#   INSTALL_COMMAND ""
#   URL
#     https://www.python.org/ftp/python/src/py152.tgz
#   URL_HASH SHA1=2d648d07b1aa1aab32a3a24851c33715141779b9
# )
# ExternalProject_Get_Property(Python152 SOURCE_DIR)
# include_directories(AFTER ${SOURCE_DIR}/Include/)


# ExternalProject_Add(
#   Python152_Bin
#   PREFIX ${CMAKE_CURRENT_BINARY_DIR}
#   CONFIGURE_COMMAND ""
#   BUILD_COMMAND ""
#   INSTALL_COMMAND ""
#   URL
#   https://www.python.org/ftp/python/win32/py152.exe
#   URL_HASH SHA1=dfaf2dcc3704fb1bbc339db4f33ff94bd61c74c6
# )
# ExternalProject_Get_Property(Python152 SOURCE_DIR)
# link_directories(AFTER ${SOURCE_DIR}/)

add_compile_definitions(_CRT_SECURE_NO_WARNINGS)
add_compile_definitions(POINTER_64=__ptr64)
add_library(ScrapHack SHARED
  ${CMAKE_CURRENT_SOURCE_DIR}/src/dllmain.cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/src/ScrapHack.cpp
  )
set_target_properties(ScrapHack PROPERTIES SUFFIX ".pyd")
add_dependencies(ScrapHack DirectX)
add_dependencies(ScrapHack MAKE_D3D8_VMT)
add_dependencies(MAKE_D3D8_VMT DirectX)
# add_dependencies(ScrapHack Python152)
# add_dependencies(ScrapHack Python152_Bin)
target_link_libraries(ScrapHack
                      d3d8
                      d3dx8
                      dxerr8
                      # PYTHON15
                      legacy_stdio_definitions)
target_compile_features(ScrapHack PUBLIC cxx_std_11)
install(TARGETS ScrapHack DESTINATION bin)
