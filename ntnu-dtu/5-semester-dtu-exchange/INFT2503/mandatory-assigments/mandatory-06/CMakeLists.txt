cmake_minimum_required(VERSION 3.5)

project(mandatory-06)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++1y -pthread -Wall -Wextra")

add_executable(chess chess.cpp)



find_package(Boost 1.54.0 COMPONENTS system REQUIRED)
include_directories(${Boost_INCLUDE_DIR})

add_executable(echo_server echo_server.cpp)
target_link_libraries(echo_server ${Boost_LIBRARIES} ws2_32 mswsock)

