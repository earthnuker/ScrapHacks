cmake_minimum_required (VERSION 2.6)
project(ScrapHacks)
SET(CMAKE_BUILD_TYPE "Release")
SET(CMAKE_INSTALL_PREFIX "${CMAKE_BINARY_DIR}")
if(WIN32)
  if(MSVC)
    # ensure we use minimal "windows.h" lib without the crazy min max macros    
    SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /D \"WIN32_LEAN_AND_MEAN\"")
    SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /D \"NOMINMAX\"")
    # disable SAFESEH - to avoid "LNK2026: module unsafe"
    SET(CMAKE_CXX_FLAGS           "${CMAKE_CXX_FLAGS} /D \"SAFESEH:NO\"")
    SET(CMAKE_EXE_LINKER_FLAGS    "${CMAKE_EXE_LINKER_FLAGS} /SAFESEH:NO")
    SET(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} /SAFESEH:NO")
    SET(CMAKE_MODULE_LINKER_FLAGS "${CMAKE_MODULE_LINKER_FLAGS} /SAFESEH:NO")
  endif(MSVC)
endif(WIN32)

add_subdirectory(Injector)
add_subdirectory(ScrapHack)