#include <stdio.h>
#include "worldline.h"
#include "read_inp.h"
#include "map.h"

int main(int argc, char *argv[]) {
    time_t ltime = time(NULL);
    printf("Starting for quantum Monte Carlo simulation at %s\n",asctime(localtime(&ltime)));
    srand(time(NULL)); // Generate random seed with time.

    // Define
    int N_size;
    double beta;
    double epsilon;
    double mu;
    int nWait;                   // Discard the first few iteration to wait until equilibrium state.
    int nSweep;                 // Total number of groups in the Monte Carlo simulation
    int BlockSize;               // Size of each block. Mean value within block would be calculated
    read_inp(argv[1], &N_size, &beta, &epsilon, &mu, &nWait, &nSweep, &BlockSize);
    printf("Given N_size = %d\nGiven beta = %4f\nGiven epsilon = %4f\nGiven mu = %4f\nGiven Wait time = %d\nGiven Sweep time = %d\nGiven Block size = %d\n", N_size, beta, epsilon, mu, nWait, nSweep, BlockSize);
    int *table;
    table = calloc(N_size * N_size * N_size * 7, sizeof(int));
    prep_map(N_size, table);
    for (int row = 0; row < 8; row++) {
         for (int col = 0; col < 7; col++) {
              printf("%d  ", table[row * 7 + col]);
         }
         printf("\n");
    }
    int *backward = NULL;
    int Ntime = (int) (beta / epsilon);
    int totsize = (int) (beta / epsilon) * N_size * N_size * N_size;
    int arrow = 1;      // Direction of time arrow
    int index = 0;      // Index of the flatten index
    int collision = 0;  // collision at the last move

    // generate_worldline(N_size, beta, epsilon, wldline);
    backward = calloc(totsize, sizeof(int));

    int *forward = NULL;
    forward = calloc(totsize, sizeof(int));
    int direction = 0;



    // Define and calloc space for array
    double* numArrMean;
    double* eneArrMean;
    double energy_sum = 0;
    numArrMean = calloc(nSweep, sizeof(double));
    eneArrMean = calloc(nSweep, sizeof(double));

    for (int j = 0; j < nWait; j++) {
        monte(N_size, Ntime, epsilon, mu, table, forward, backward);
    }
    for (int b = 0; b < nSweep; b++) {
        printf("Start new group. Now the group number is %d\n", b);
        fflush(stdout);
        double num = 0;
        double energy = 0;
        for (int g = 0; g < BlockSize; g++) {
            double ene;
            int number;
            monte(N_size, Ntime, epsilon, mu, table, forward, backward);
            number = count_non_zero(N_size, forward);
            ene = cal_energy(totsize, beta, epsilon, forward);
            num += number;
            energy += ene;
        }
        numArrMean[b] = num / BlockSize;
        eneArrMean[b] = energy / BlockSize;
        energy_sum += energy / BlockSize;
    }
    printf("Current epsilon value: %5f\n", epsilon);
    printf("Current lattice size: %d\n", N_size);
    printf("Current chemical potential: %3f\n", mu);
    print_arr(nSweep, numArrMean, "Particle number");
    fflush(stdout);
    print_arr(nSweep, eneArrMean, "Energy");
    fflush(stdout);
    printf("Energy\n");
    printf("%f\n", energy_sum / nSweep);

    ltime = time(NULL);
    printf("Finish %d iterations at %s\n", nWait + nSweep * BlockSize, asctime(localtime(&ltime)));

    free(backward);
    free(numArrMean);
    free(eneArrMean);
    free(forward);
    free(table);
    return 0;
}
