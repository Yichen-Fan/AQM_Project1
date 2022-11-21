//
// Created by Ethan  Fan  on 11/21/22.
//

#ifndef MONTECARLO_CVERSION_MAP_H
#define MONTECARLO_CVERSION_MAP_H

#endif //MONTECARLO_CVERSION_MAP_H

/*
 * Preparing the mapping between initial location direction and final localtion. The location convertion would be
 * position = z * n_size^2 + y * n_size + z.
 * N_size: input. The dimension in spacial
 * table: ouput. would be a N^3 * 7 matrix. Element index: position * 7 + direction;
 */
void prep_map(int N_size, int *table);