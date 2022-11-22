//
// Created by Ethan  Fan  on 11/17/22.
//

#ifndef MONTECARLO_CVERSION_UTIL_H
#define MONTECARLO_CVERSION_UTIL_H

#endif //MONTECARLO_CVERSION_UTIL_H

#include <stdlib.h>

/*
 * RANDF: random floating number generator;
 * double output: a floating number from 0 to 1;
 */
double RANDF();
/*
 * RANDI: random integer number smaller than floor;
 * int output: an inter from 0 to floor;
 */
int RANDI(int floor);
/*
 * count_non_zero: count the number of nonzero entries in given matrix input.
 * N_size: input. Size of lattice;
 * wldline: input. Configuration. only the integer multiple of N_size^3 should be given.
 * int return: number of non zero elements in the first N_size^3 entries.
 */
int count_non_zero(int N_size, int *wldline);
/*
 * cal_energy: calculate energy of each configuration;
 * N_size: input, size of lattice;
 * beta: input. Imaginary time. determine the total memory of configuration;
 * num: input: number of particle. May be obtained from count_non_zero;
 * forward: input. Configuration;
 * double return: energy of given configuration;
 */
double cal_energy(int N_size, double beta, double epsilon, int *forward);
/*
 * print_arr: print given array. Note only work for double array.
 */
void print_arr(int size, double* pArr, char* pstr);

