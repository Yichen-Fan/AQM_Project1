//
// Created by Ethan  Fan  on 11/17/22.
//
#include "util.h"
#include <stdio.h>
#include <math.h>

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

double cal_energy(int totsize, double beta, double epsilon, int *forward, int *wind){
    int hop = 0;
    int noHop = 0;
    int wx = 0;
    int wy = 0;
    int wz = 0;
    //int totsize; // = N_size * N_size * N_size;
    int i;
    for (i = 0; i < totsize; i++){
        switch (forward[i]) {
            case 1:
                hop++;
                wx++;
                break;
            case 2:
                hop++;
                wy++;
                break;
            case 3:
                hop++;
                wz++;
                break;
            case -1:
                hop++;
                wx--;
                break;
            case -2:
                hop++;
                wy--;
                break;
            case -3:
                hop++;
                wz--;
                break;
            case 4:
                noHop++;
                break;
            case -4:
                noHop++;
                break;
            default:
                break;
        }
    }
    int tsteps = beta / epsilon;
    wind[0] = wx/20;
    wind[1] = wy/20;
    wind[2] = wz/20;
    double energy = -(double) (hop / beta) + 6 * (noHop/ ((1 - 6 * epsilon) * tsteps)); // Update the algoriothm for energy calcualtion. This equation only true for epsilon -> 0 case.
    return energy; // Also update the calculation of error bar. It should be e = sigma/ root(N)
}

void print_arr(int size, double* pArr, char* pstr){
    printf("%s:\n", pstr);
    for (int i = 0; i < size; i++){
        printf("%15f\n", pArr[i]);
    }
    printf("End of array.\n");
}

double calculatemean(double *Arr, int size){
    double sum = 0;
    for (int i = 0; i < size; i++){
        sum += Arr[i];
    }
    return (double) sum / size;
}

double calculateSD(double *Arr, int size){
    double mean = calculatemean(Arr,size);
    double nvar = 0;
    for (int i = 0; i < size; i++){
        nvar += (Arr[i]-mean)*(Arr[i]-mean);
    }
    return (double) sqrt(nvar / size);
}

