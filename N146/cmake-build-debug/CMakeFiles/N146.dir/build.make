# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/sjt758/Jetbrains/clion-2020.1.1/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /home/sjt758/Jetbrains/clion-2020.1.1/bin/cmake/linux/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/sjt758/Coding/leetcode/N146

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/sjt758/Coding/leetcode/N146/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/N146.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/N146.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/N146.dir/flags.make

CMakeFiles/N146.dir/main.cpp.o: CMakeFiles/N146.dir/flags.make
CMakeFiles/N146.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/sjt758/Coding/leetcode/N146/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/N146.dir/main.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/N146.dir/main.cpp.o -c /home/sjt758/Coding/leetcode/N146/main.cpp

CMakeFiles/N146.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/N146.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/sjt758/Coding/leetcode/N146/main.cpp > CMakeFiles/N146.dir/main.cpp.i

CMakeFiles/N146.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/N146.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/sjt758/Coding/leetcode/N146/main.cpp -o CMakeFiles/N146.dir/main.cpp.s

# Object files for target N146
N146_OBJECTS = \
"CMakeFiles/N146.dir/main.cpp.o"

# External object files for target N146
N146_EXTERNAL_OBJECTS =

N146: CMakeFiles/N146.dir/main.cpp.o
N146: CMakeFiles/N146.dir/build.make
N146: CMakeFiles/N146.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/sjt758/Coding/leetcode/N146/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable N146"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/N146.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/N146.dir/build: N146

.PHONY : CMakeFiles/N146.dir/build

CMakeFiles/N146.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/N146.dir/cmake_clean.cmake
.PHONY : CMakeFiles/N146.dir/clean

CMakeFiles/N146.dir/depend:
	cd /home/sjt758/Coding/leetcode/N146/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/sjt758/Coding/leetcode/N146 /home/sjt758/Coding/leetcode/N146 /home/sjt758/Coding/leetcode/N146/cmake-build-debug /home/sjt758/Coding/leetcode/N146/cmake-build-debug /home/sjt758/Coding/leetcode/N146/cmake-build-debug/CMakeFiles/N146.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/N146.dir/depend

