cmake_minimum_required(VERSION 3.5)

project(mandatory-08)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++1y -Wall -Wextra")

add_executable(exercise-01 exercise-01/main.cpp exercise-01/equal.cpp)

add_executable(exercise-02 exercise-02/pair.cpp exercise-02/main.cpp)
