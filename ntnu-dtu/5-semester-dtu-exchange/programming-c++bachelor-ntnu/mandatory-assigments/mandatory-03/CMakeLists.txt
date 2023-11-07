cmake_minimum_required(VERSION 3.5)

project(mandatory-03)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++1y -Wall -Wextra")
set(SRC_FILES_1 exercise-1.cpp Circle.hpp Circle.cpp)
set(SRC_FILES_2 exercise-2.cpp Circle.hpp Circle.cpp)
set(SRC_FILES_3 exercise-3.cpp Commodity.hpp Commodity.cpp)

add_executable(exercise1 ${SRC_FILES_1})
add_executable(exercise2 ${SRC_FILES_2})
add_executable(exercise3 ${SRC_FILES_3})
add_executable(exercise4 exercise-4.cpp)
