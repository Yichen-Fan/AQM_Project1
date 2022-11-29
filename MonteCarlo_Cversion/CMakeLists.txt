cmake_minimum_required(VERSION 3.18)
project(MonteCarlo_Cversion C)

#set(CMAKE_C_STANDARD 11)

add_executable(MonteCarlo_Cversion source/susceptibility.h source/susceptibility.c source/read_inp.c source/read_inp.h source/main.c source/worldline.h source/worldline.c source/util.h source/util.c source/move.c source/map.c source/map.h)
target_link_libraries(MonteCarlo_Cversion m)
