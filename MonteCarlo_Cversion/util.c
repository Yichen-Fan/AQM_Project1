//
// Created by Ethan  Fan  on 11/17/22.
//
#include "util.h"


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