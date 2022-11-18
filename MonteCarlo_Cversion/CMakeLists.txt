cmake_minimum_required(VERSION 3.22)
project(MonteCarlo_Cversion C)

set(CMAKE_C_STANDARD 17)

add_executable(MonteCarlo_Cversion main.c worldline.h worldline.c util.h util.c)
