add_executable(Injector Injector.cpp)
target_compile_features(Injector PUBLIC cxx_std_11)
install(TARGETS Injector DESTINATION bin)
