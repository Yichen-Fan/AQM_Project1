#include <stdio.h>
#include "worldline.h"

int main() {
    time_t ltime = time(NULL);
    printf("Starting for quantum Monte Carlo simulation at %s\n",asctime(localtime(&ltime)));
    srand(time(NULL)); // Generate random seed with time.
    // Define
    int N_size = 2;
    double beta = 12;
    double epsilon = 0.001;
    double mu = 1.4;
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

    int nWait = 10000;
    double num = 0;
    double num3 = 0;

    // int nGroup = 10000;
    // int nElem = 1000;

    for (int j = 0; j < nWait; j++) {
        index = random_start(totsize);
        if (forward[index]){
            arrow = 0;
        }
        else {
            arrow = 1;
        }
        collision = 0;
        int i = 0;
        int temp = index;
        while (1) {
            i++;
            temp = index;
            if (arrow) {
                direction = move(epsilon);
                forward[index] = direction;
                update(direction, N_size, Ntime, &index);
                if (backward[index]) {
                    collision = backward[index];
                    arrow = 0;
                }
                backward[index] = -direction;
                if (!collision && forward[index]) {
                    break;
                }
            }
            else {
                if (backward[index] == 0) {
                    break;
                }
                if (collision) {
                    direction = collision;
                    collision = 0;
                } else {
                    direction = backward[index];
                    backward[index] = 0;
                }
                reverse(direction, N_size, Ntime, &index);
                if (forward[index] != 0)
                {
                    // printf("ERROR\n");
                }
                forward[index] = 0;

                // Reject prob
                if (RANDF() < 1.0 - exp(-mu * epsilon)) {
                    arrow = 1;
                }
            }
        }
        int num1 = count_non_zero(N_size, backward);
        num += num1;
    }
    num = num/ nWait;
    num3 = num3 / nWait;
    printf("avg 1:%f\n",num);
    ltime = time(NULL);
    printf("Finish %d iterations at %s\n", nWait, asctime(localtime(&ltime)));

    free(backward);
    free(forward);
    return 0;
}
