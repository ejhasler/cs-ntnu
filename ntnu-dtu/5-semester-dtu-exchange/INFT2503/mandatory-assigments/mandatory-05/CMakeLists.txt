cmake_minimum_required(VERSION 3.5)

project(mandatory-05)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++1y -Wall -Wextra")

add_executable(mandatory-05 chess.cpp)
