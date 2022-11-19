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
 * return: index in the flatten matrix. ct \times cz \times cy \times cx
 */
int random_start(int totsize);
/*
 * move: Determine the direction of moving when the time arrow is positive.
 * epsilon: double. The magnitude of time step
 * return value: int. \pm 1 for movement in x axis; \pm 2 for movement in y axis; \pm 3 for movement in z axis
 */
int move(double epsilon);
/*
 * update: Function used to update the index after each movement.
 * direction: input. Direction of movement;
 * pindex: input, and output. The pointer points to the current index. The index will be updated in this function;
 */
void update(int direction, int Nsize, int Ntime, int *pindex);
/*
 *  reverse: Similar to update function, but time arrow is negative here.
 *  direction: input. direction of movement in space;
 *  pindex: input and output. Pointer points to current location. Will be updatetd in this function;
 */
void reverse(int direction, int Nsize, int Ntime, int *pindex);
/*
 *
 */
void monte(int N_size, int Ntime, double epsilon, double mu, int *forward, int *backward);