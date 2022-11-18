//
// Created by Ethan  Fan  on 11/17/22.
//
#include "worldline.h"


void generate_worldline(int N_size, double beta, double epsilon, int *wldline){
    if (wldline != NULL){
        free(wldline);
    }
    time_t ltime;
    ltime = time(NULL);
    printf("Starting for quantum Monte Carlo simulation at %s\n",asctime(localtime(&ltime)));

    int tstep = (int) (beta / epsilon);
    // Initialize worldline
    printf("New worldline generated.\n Current beta is %3f\n Current epsilon is %4.5f\n "
           "Current N_size is %d\n Current time steps are %d\n", beta, epsilon, N_size, tstep);
}

int random_start(int totsize) {
    int randNum = RANDI(totsize);
    return randNum;
}






