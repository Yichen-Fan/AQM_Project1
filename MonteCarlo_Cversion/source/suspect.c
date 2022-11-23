//
// Created by Ethan  Fan  on 11/21/22.
//

#include "suspect.h"

void generate_index(int direction, int N_size, int *slice) {
    switch (direction){
        case 1:
            for (int y = 0; y < N_size; y++) {
                for (int z = 0; z < N_size; z++) {
                    slice[z * N_size + y] = z * N_size * N_size + y * N_size;
                }
            }
            break;
        case 2:
            for (int x = 0; x < N_size; x++) {
                for (int z = 0; z < N_size; z++) {
                    slice[z * N_size + x] = z * N_size * N_size + x;
                }
            }
            break;
        case 3:
            for (int y = 0; y < N_size; y++) {
                for (int x = 0; x < N_size; x++) {
                    slice[y * N_size + x] = y * N_size + x;
                }
            }
            break;
        default:
            break;
    }
}

int susceptibility(int direction, int tsteps, int N_size, int *slice, int *forward) {
    int index = 0;
    int ndirection = direction * -1;
    int winding = 0;
    int N_size2 = N_size * N_size;
    int N_size3 = N_size * N_size2;
    for (int t = 0; t < tsteps; t++) {
        for (int i = 0; i < N_size2; i++){
            index = t * N_size3;
            index += slice[i + direction * N_size2];
            if (forward[index] == direction + 1) {
                winding++;
            } else if(forward[index] == ndirection - 1) {
                winding--;
            }
        }
    }
    return winding;
}
