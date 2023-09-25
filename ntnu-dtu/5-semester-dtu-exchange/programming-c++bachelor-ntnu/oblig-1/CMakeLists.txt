cmake_minimum_required(VERSION 3.5)

project(oblig-1)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++1y -Wall -Wextra")
set(SRC_FILES
read-from-file.cpp
read-from-user.cpp
)

add_executable(oblig-1 ${SRC_FILES})