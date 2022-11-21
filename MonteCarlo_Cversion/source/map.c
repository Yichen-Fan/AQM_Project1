//
// Created by Ethan  Fan  on 11/21/22.
//

#include "map.h"
#include <stdio.h>
#include <stdlib.h>

void prep_map(int N_size, int *table) {
    int N_size2 = N_size * N_size;
    int N_size3 = N_size * N_size2;

    int position, direction, new_position;
    int cx, cy, cz;
    int nx, ny, nz;
    for (position = 0; position < N_size3; position++){
        cx = position % N_size;
        cy = position % N_size2 / N_size;
        cz = position / N_size2;
        for (direction = 0; direction < 7; direction ++) {
            nx = cx;
            ny = cy;
            nz = cz;
            switch (direction) {
                case 0:
                    nz = (cz - 1 + N_size) % N_size;
                    break;
                case 1:
                    ny = (cy - 1 + N_size) % N_size;
                    break;
                case 2:
                    nx = (cx - 1 + N_size) % N_size;
                    break;
                case 3:
                    break;
                case 4:
                    nx = (cx + 1 + N_size) % N_size;
                    break;
                case 5:
                    ny = (cy + 1 + N_size) % N_size;
                    break;
                case 6:
                    nz = (cz + 1 + N_size) % N_size;
                    break;
                default:
                    break;
            }
            new_position = nz * N_size2 + ny * N_size + nx;
            table[position * 7 + direction] = new_position;
        }
    }
}