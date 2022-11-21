//
// Created by Ethan  Fan  on 11/17/22.
//
#include "util.h"
#include <stdio.h>

double RANDF(){
    return (double) (rand() % RAND_MAX) / RAND_MAX;
}

int RANDI(int ceil){
    return (int) (rand() % ceil);
}

int count_non_zero(int N_size, int *wldline){
    int num = 0;
    for (int i =0; i < N_size * N_size * N_size; i++){
        if (wldline[i] != 0){
            num++;
        }
    }
    return num;
}

double cal_energy(int totsize, double beta, int num, int *forward){
    int hop = 0;
    int noHop = 0;
    //int totsize; // = N_size * N_size * N_size;
    int i;
    for (i = 0; i < totsize; i++){
        switch (forward[i]) {
            case 1:
                hop++;
                break;
            case 2:
                hop++;
                break;
            case 3:
                hop++;
                break;
            case -1:
                hop++;
                break;
            case -2:
                hop++;
                break;
            case -3:
                hop++;
                break;
            default:
                break;
        }
    }
    double energy = -(double) (hop / beta) + 6 * num;
    return energy;
}

void print_arr(int size, double* pArr, char* pstr){
    printf("%s:\n", pstr);
    for (int i = 0; i < size; i++){
        printf("%7f\n", pArr[i]);
    }
    printf("End of array.\n");
}
