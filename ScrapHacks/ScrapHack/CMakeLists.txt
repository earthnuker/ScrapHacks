include(ExternalProject)
ExternalProject_Add(DirectX
    PREFIX ${CMAKE_CURRENT_BINARY_DIR}
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND ""
    URL https://archive.org/download/DirectX.8.0a.SDK_includes_libs_only/DirectX.8.0a.SDK.zip
    URL_HASH SHA1=39f168336d0df92ff14d62d5e3aef1b9e3191312
)
ExternalProject_Get_Property(DirectX SOURCE_DIR)
include_directories(AFTER ${SOURCE_DIR}/8.0/include/)
link_directories(AFTER ${SOURCE_DIR}/8.0/lib/)
add_compile_definitions(_CRT_SECURE_NO_WARNINGS)
add_compile_definitions(POINTER_64=__ptr64)
add_library(ScrapHack SHARED ScrapHack.cpp dllmain.cpp)
target_link_libraries(ScrapHack d3d8 d3dx8 legacy_stdio_definitions)
install(TARGETS ScrapHack DESTINATION bin)
