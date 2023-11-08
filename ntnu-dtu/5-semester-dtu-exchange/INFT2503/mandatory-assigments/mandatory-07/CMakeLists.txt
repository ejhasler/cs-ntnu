cmake_minimum_required(VERSION 3.5)

project(mandatory-07)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++1y -Wall -Wextra")

add_executable(fraction fraction/main.cpp fraction/fraction.cpp)

add_executable(set set/set.cpp set/main_set.cpp)
