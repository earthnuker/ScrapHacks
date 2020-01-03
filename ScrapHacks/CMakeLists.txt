cmake_minimum_required(VERSION 3.1)
cmake_policy(VERSION ${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION})

project(ScrapHacks
        VERSION 1.0
        DESCRIPTION "Scrapland memory hacking library"
        LANGUAGES CXX)

message(STATUS "Fetching Scrapland installation folder")
get_filename_component(SCRAPLAND_DIR "[HKEY_LOCAL_MACHINE\\SOFTWARE\\WOW6432Node\\MercurySteam Entertainment\\Scrapland;DIRECTORY]" ABSOLUTE CACHE)

if(NOT IS_ABSOLUTE "${SCRAPLAND_DIR}" OR NOT EXISTS "${SCRAPLAND_DIR}")
  message(FATAL_ERROR "Scrapland installation folder not found!")
endif()

message(STATUS "Checking Scrap.exe hash")
file(SHA1 "${SCRAPLAND_DIR}/Bin/Scrap.exe" SCRAP_EXE_HASH)

if(NOT ${SCRAP_EXE_HASH} STREQUAL "d2dde960e8eca69d60c2e39a439088b75f0c89fa")
  message(FATAL_ERROR "Scrap.exe hash miss match!")
endif()

set(FETCHCONTENT_QUIET 0)
set(CMAKE_BUILD_TYPE "RelMinSize")
set(CMAKE_INSTALL_PREFIX "${CMAKE_BINARY_DIR}")
set(ASMJIT_EMBED true)
set(ASMTK_EMBED true)
set(ZYDIS_BUILD_TOOLS false)
set(ZYDIS_BUILD_EXAMPLES false)


if(WIN32)
  if(MSVC)
    # ensure we use minimal "windows.h" lib without the crazy min max macros
    # set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /D \"WIN32_LEAN_AND_MEAN\"")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /D \"NOMINMAX\"")
    # disable SAFESEH - to avoid "LNK2026: module unsafe"
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /D \"SAFESEH:NO\"")
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} /SAFESEH:NO /ignore:4217")
    set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} /SAFESEH:NO /ignore:4217")
    set(CMAKE_MODULE_LINKER_FLAGS "${CMAKE_MODULE_LINKER_FLAGS} /SAFESEH:NO /ignore:4217")
  endif(MSVC)
endif(WIN32)

include(FetchContent)

FetchContent_Declare(
  DirectX
  PREFIX ${CMAKE_CURRENT_BINARY_DIR}
  URL
    https://archive.org/download/DirectX.8.0a.SDK_includes_libs_only/DirectX.8.0a.SDK.zip
  URL_HASH SHA1=39f168336d0df92ff14d62d5e3aef1b9e3191312)

FetchContent_MakeAvailable(DirectX)

FetchContent_Declare(
    ASM_JIT
    PREFIX ${CMAKE_CURRENT_BINARY_DIR}
    GIT_REPOSITORY git@github.com:asmjit/asmjit.git
    GIT_SHALLOW true
    GIT_PROGRESS true
)

FetchContent_MakeAvailable(ASM_JIT)

FetchContent_Declare(
    ASM_TK
    PREFIX ${CMAKE_CURRENT_BINARY_DIR}
    GIT_REPOSITORY git@github.com:asmjit/asmtk.git
    GIT_SHALLOW true
    GIT_PROGRESS true
)

FetchContent_MakeAvailable(ASM_TK)

set(ASMJIT_DIR ${asm_jit_SOURCE_DIR})

include(${asm_tk_SOURCE_DIR}/CMakeLists.txt)


FetchContent_Declare(
    Zydis
    PREFIX ${CMAKE_CURRENT_BINARY_DIR}
    GIT_REPOSITORY git@github.com:zyantific/zydis.git
    GIT_SHALLOW true
    GIT_PROGRESS true
)

# FetchContent_MakeAvailable(Zydis)

include_directories(AFTER ${directx_SOURCE_DIR}/8.0/include/ ${ASMTK_INCLUDE_DIRS} ${ASMJIT_INCLUDE_DIRS})
link_directories(AFTER ${directx_SOURCE_DIR}/8.0/lib/)

find_package(Python3 3.6 REQUIRED COMPONENTS Interpreter)

add_custom_command(
  OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/src/D3D8_VMT.hpp
  COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/utils/make_D3D8_VMT.py ${CMAKE_CURRENT_SOURCE_DIR}/src/D3D8_VMT.hpp ${directx_SOURCE_DIR}/8.0/include/d3d8.h
  COMMENT "Generating D3D8_VMT.hpp from d3d8.h"
  VERBATIM
)
add_custom_target(D3D8_VMT ALL
    DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/src/D3D8_VMT.hpp")

add_compile_definitions(_CRT_SECURE_NO_WARNINGS)
add_compile_definitions(POINTER_64=__ptr64)
add_library(ScrapHack SHARED
  ${CMAKE_CURRENT_SOURCE_DIR}/src/dllmain.cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/src/ScrapHack.cpp
  ${ASMTK_SRC}
  ${ASMJIT_SRC}
)

set_target_properties(ScrapHack PROPERTIES SUFFIX ".pyd")
add_dependencies(ScrapHack D3D8_VMT)
# add_dependencies(ScrapHack Python152)
# add_dependencies(ScrapHack Python152_Bin)
target_link_libraries(ScrapHack
                      d3d8
                      d3dx8
                      dxerr8
                      gdiplus
                      # PYTHON15
                      # Zydis
                      legacy_stdio_definitions)

install(TARGETS ScrapHack RUNTIME DESTINATION ${SCRAPLAND_DIR}/lib)
target_compile_features(ScrapHack PUBLIC cxx_std_11)
