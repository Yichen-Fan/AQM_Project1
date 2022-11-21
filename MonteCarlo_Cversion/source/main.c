#include <stdio.h>
#include "worldline.h"

int main() {
    time_t ltime = time(NULL);
    printf("Starting for quantum Monte Carlo simulation at %s\n",asctime(localtime(&ltime)));
    srand(time(NULL)); // Generate random seed with time.
    // Define
    int N_size = 2;
    double beta = 12.0;
    double epsilon = 0.01;
    double mu = 1.4;
    int *backward = NULL;
    int Ntime = (int) (beta / epsilon);
    int totsize = (int) (beta / epsilon) * N_size * N_size * N_size;
    printf("%d", totsize);
    int arrow = 1;      // Direction of time arrow
    int index = 0;      // Index of the flatten index
    int collision = 0;  // collision at the last move

    // generate_worldline(N_size, beta, epsilon, wldline);
    backward = calloc(totsize, sizeof(int));

    int *forward = NULL;
    forward = calloc(totsize, sizeof(int));
    int direction = 0;

    int nWait = 1000;                   // Discard the first few iteration to wait until equilibrium state.
    int nSweep = 100;                 // Total number of groups in the Monte Carlo simulation
    int BlockSize = 500;               // Size of each block. Mean value within block would be calculated


    // Define and calloc space for array
    double* numArrMean;
    double* eneArrMean;
    double energy_sum = 0;
    numArrMean = calloc(nSweep, sizeof(double));
    eneArrMean = calloc(nSweep, sizeof(double));

    for (int j = 0; j < nWait; j++) {
        monte(N_size, Ntime, epsilon, mu, forward, backward);
    }
    for (int b = 0; b < nSweep; b++) {
        printf("Start new group. Now the group number is %d\n", b);
        fflush(stdout);
        double num = 0;
        double energy = 0;
        for (int g = 0; g < BlockSize; g++) {
            double ene;
            int number;
            monte(N_size, Ntime, epsilon, mu, forward, backward);
            number = count_non_zero(N_size, forward);
            ene = cal_energy(totsize, beta, number, backward);
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
    printf("Finish %d iterations at %s\n", nWait, asctime(localtime(&ltime)));

    free(backward);
    free(numArrMean);
    free(eneArrMean);
    free(forward);
    return 0;
}
