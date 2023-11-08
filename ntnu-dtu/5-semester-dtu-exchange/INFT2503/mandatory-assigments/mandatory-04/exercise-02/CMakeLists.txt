cmake_minimum_required(VERSION 3.5)

project(exercise-02)

# Set the C++ standard and enable warnings
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED True)
add_compile_options(-Wall -Wextra)

# Find the PkgConfig module which will be used to locate GTKmm
find_package(PkgConfig REQUIRED)

# Use pkg-config to get hints for linking in the required gtkmm libraries
pkg_check_modules(GTKMM REQUIRED gtkmm-3.0)

# Executable for the application
add_executable(main main.cpp)

# Link the application to the GTKMM libraries
target_link_libraries(main ${GTKMM_LIBRARIES})
target_include_directories(main PUBLIC ${GTKMM_INCLUDE_DIRS})
target_link_directories(main PUBLIC ${GTKMM_LIBRARY_DIRS})

# If necessary, add compile definitions for the application based on GTKMM flags
if(GTKMM_CFLAGS_OTHER)
  target_compile_options(main PUBLIC ${GTKMM_CFLAGS_OTHER})
endif()
