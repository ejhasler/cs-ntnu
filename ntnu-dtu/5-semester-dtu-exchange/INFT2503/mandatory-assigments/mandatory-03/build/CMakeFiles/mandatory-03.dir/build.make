# CMAKE generated file: DO NOT EDIT!
# Generated by "MSYS Makefiles" Generator, CMake Version 3.27

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /C/msys64/mingw64/bin/cmake.exe

# The command to remove a file.
RM = /C/msys64/mingw64/bin/cmake.exe -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /H/github/cs-ntnu/ntnu-dtu/5-semester-dtu-exchange/programming-c++bachelor-ntnu/assignments/mandatory-03

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /H/github/cs-ntnu/ntnu-dtu/5-semester-dtu-exchange/programming-c++bachelor-ntnu/assignments/mandatory-03/build

# Include any dependencies generated for this target.
include CMakeFiles/mandatory-03.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/mandatory-03.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/mandatory-03.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/mandatory-03.dir/flags.make

CMakeFiles/mandatory-03.dir/main.cpp.obj: CMakeFiles/mandatory-03.dir/flags.make
CMakeFiles/mandatory-03.dir/main.cpp.obj: H:/github/cs-ntnu/ntnu-dtu/5-semester-dtu-exchange/programming-c++bachelor-ntnu/assignments/mandatory-03/main.cpp
CMakeFiles/mandatory-03.dir/main.cpp.obj: CMakeFiles/mandatory-03.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/H/github/cs-ntnu/ntnu-dtu/5-semester-dtu-exchange/programming-c++bachelor-ntnu/assignments/mandatory-03/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/mandatory-03.dir/main.cpp.obj"
	/C/msys64/mingw64/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/mandatory-03.dir/main.cpp.obj -MF CMakeFiles/mandatory-03.dir/main.cpp.obj.d -o CMakeFiles/mandatory-03.dir/main.cpp.obj -c /H/github/cs-ntnu/ntnu-dtu/5-semester-dtu-exchange/programming-c++bachelor-ntnu/assignments/mandatory-03/main.cpp

CMakeFiles/mandatory-03.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/mandatory-03.dir/main.cpp.i"
	/C/msys64/mingw64/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /H/github/cs-ntnu/ntnu-dtu/5-semester-dtu-exchange/programming-c++bachelor-ntnu/assignments/mandatory-03/main.cpp > CMakeFiles/mandatory-03.dir/main.cpp.i

CMakeFiles/mandatory-03.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/mandatory-03.dir/main.cpp.s"
	/C/msys64/mingw64/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /H/github/cs-ntnu/ntnu-dtu/5-semester-dtu-exchange/programming-c++bachelor-ntnu/assignments/mandatory-03/main.cpp -o CMakeFiles/mandatory-03.dir/main.cpp.s

# Object files for target mandatory-03
mandatory__03_OBJECTS = \
"CMakeFiles/mandatory-03.dir/main.cpp.obj"

# External object files for target mandatory-03
mandatory__03_EXTERNAL_OBJECTS =

mandatory-03.exe: CMakeFiles/mandatory-03.dir/main.cpp.obj
mandatory-03.exe: CMakeFiles/mandatory-03.dir/build.make
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/H/github/cs-ntnu/ntnu-dtu/5-semester-dtu-exchange/programming-c++bachelor-ntnu/assignments/mandatory-03/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable mandatory-03.exe"
	/C/msys64/mingw64/bin/cmake.exe -E rm -f CMakeFiles/mandatory-03.dir/objects.a
	/C/msys64/mingw64/bin/ar.exe qc CMakeFiles/mandatory-03.dir/objects.a $(mandatory__03_OBJECTS) $(mandatory__03_EXTERNAL_OBJECTS)
	/C/msys64/mingw64/bin/c++.exe  -std=c++1y -Wall -Wextra -Wl,--whole-archive CMakeFiles/mandatory-03.dir/objects.a -Wl,--no-whole-archive -o mandatory-03.exe -Wl,--out-implib,libmandatory-03.dll.a -Wl,--major-image-version,0,--minor-image-version,0  -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -ladvapi32 

# Rule to build all files generated by this target.
CMakeFiles/mandatory-03.dir/build: mandatory-03.exe
.PHONY : CMakeFiles/mandatory-03.dir/build

CMakeFiles/mandatory-03.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/mandatory-03.dir/cmake_clean.cmake
.PHONY : CMakeFiles/mandatory-03.dir/clean

CMakeFiles/mandatory-03.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MSYS Makefiles" /H/github/cs-ntnu/ntnu-dtu/5-semester-dtu-exchange/programming-c++bachelor-ntnu/assignments/mandatory-03 /H/github/cs-ntnu/ntnu-dtu/5-semester-dtu-exchange/programming-c++bachelor-ntnu/assignments/mandatory-03 /H/github/cs-ntnu/ntnu-dtu/5-semester-dtu-exchange/programming-c++bachelor-ntnu/assignments/mandatory-03/build /H/github/cs-ntnu/ntnu-dtu/5-semester-dtu-exchange/programming-c++bachelor-ntnu/assignments/mandatory-03/build /H/github/cs-ntnu/ntnu-dtu/5-semester-dtu-exchange/programming-c++bachelor-ntnu/assignments/mandatory-03/build/CMakeFiles/mandatory-03.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/mandatory-03.dir/depend
