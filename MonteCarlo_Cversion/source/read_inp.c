//
// Created by Ethan  Fan  on 11/20/22.
//

#include "read_inp.h"

void read_inp(char *file, int *pN_size, double *pbeta, double *pepsilon, double *pmu, int *pnWait, int *pnSweep, int *pBlockSize) {
    FILE *fr = fopen(file, "rt");

    char tmpstr1[100];
    char temp[100];

    char tempbuff[100];
    int N_size;
    double beta, epsilon, mu;
    char *seperate = ":";
    while (!feof(fr)) {
        if (fgets(tempbuff, 100, fr)) {
            sscanf(tempbuff, "%s %s;", tmpstr1, temp);
            if (strcmp(tmpstr1, "N_size") == 0) {
                *pN_size = atoi(temp);
            } else if (strcmp(tmpstr1, "beta") == 0) {
                *pbeta = atof(temp);
            } else if (strcmp(tmpstr1, "epsilon") == 0) {
                *pepsilon = atof(temp);
            } else if (strcmp(tmpstr1, "mu") == 0) {
                *pmu = atof(temp);
            } else if (strcmp(tmpstr1, "nWait") == 0) {
                *pnWait = atoi(temp);
            } else if (strcmp(tmpstr1, "nSweep") == 0) {
                *pnSweep = atoi(temp);
            } else if (strcmp(tmpstr1, "BlockSize") == 0) {
                *pBlockSize = atoi(temp);
            }    
            else {
                // printf("Unrecongized parameter : \"%s\"\n", tmpstr1);
            }
        }
    }


    fclose(fr);

    // printf("\nNx : %d \nNy : %d  \ndx : %f  \ndy : %f \n", Nx, Ny, dx, dy);
    printf("Finish reading\n");

}//end of code executed when input is correct


