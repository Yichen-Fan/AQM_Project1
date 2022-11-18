//
// Created by Ethan  Fan  on 11/17/22.
//

#ifndef MONTECARLO_CVERSION_WORLDLINE_H
#define MONTECARLO_CVERSION_WORLDLINE_H

#endif //MONTECARLO_CVERSION_WORLDLINE_H
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <printf.h>
#include "util.h"
/*
 * This function would generate initial world line, need to call before any further operations
 * N_size: Input. Size of spactial dimensions. N_size remains same for x y and z axis.
 * beta: Input. Imaginary time. Must be positive and larger than epsilon.
 * epsilon: Input. The magnitude of time step. Must be positive, and smaller than beta. The total number of time steps
 * is int (beta/ epsilon).
 * totsize: Output. The total size of worldline matrix. totsize = N_size^3 * int(beta/epsilon)
 * wldline: Output. Would be a flatten matrix with dimension of N_size^3 * int(beta/epsilon)
 * Initial value of wldline would be a flatten zero matrix
 *
 * Remember to call this function after updated either N_size, beta or epsilon.
 */
void generate_worldline(int N_size, double beta, double epsilon, int *wldline);
/*
 * random_start: This function pick a random point within wldline array.
 * totsize: Input. total size of mtx
 * wldline: Input. The ptr points to the world line matrix
 * return: true if there is no particle false if there is a particle.
 */
int random_start(int totsize, int *wldline);