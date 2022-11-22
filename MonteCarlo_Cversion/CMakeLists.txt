cmake_minimum_required(VERSION 3.22)
project(MonteCarlo_Cversion C)

set(CMAKE_C_STANDARD 17)

add_executable(MonteCarlo_Cversion source/main.c source/worldline.h source/worldline.c source/util.h source/util.c source/move.c source/read_inp.c source/read_inp.h source/map.c source/map.h source/suspect.c source/suspect.h)
