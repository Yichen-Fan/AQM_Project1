//
// Created by Ethan  Fan  on 11/17/22.
//

#ifndef MONTECARLO_CVERSION_UTIL_H
#define MONTECARLO_CVERSION_UTIL_H

#endif //MONTECARLO_CVERSION_UTIL_H

#include <stdlib.h>

double RANDF();
int RANDI(int floor);
int count_non_zero(int N_size, int *wldline);
double cal_energy(int N_size, double beta, int num, int *forward);
void print_arr(int size, double* pArr, char* pstr);

