//
// Created by Ethan  Fan  on 11/17/22.
//
#include "util.h"
#include <stdio.h>

double RANDF(){
    return (double) (rand() % 100000000) / 100000000;
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

double cal_energy(int totsize, double beta, int *forward){
    int hop = 0;
    int noHop = 0;
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
            case 4:
                noHop++;
                break;
            default:
                break;
        }
    }
    double energy = -hop / beta + 6 * noHop;
    return energy;
}

void print_arr(int size, double* pArr, char* pstr){
    printf("%s:\n", pstr);
    for (int i = 0; i < size; i++){
        printf("%f\n", pArr[i]);
    }
    printf("End of array.\n");
}