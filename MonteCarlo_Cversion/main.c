#include <stdio.h>
#include "worldline.h"

int main() {
    srand(time(NULL)); // Generate random seed with time.
    // Define
    int N_size = 2;
    double beta = 12;
    double epsilon = 0.03;
    int *wldline = NULL;
    int totsize = (int) (beta / epsilon) * N_size * N_size * N_size;

    generate_worldline(N_size, beta, epsilon, wldline);
    random_start(totsize, wldline);



    free(wldline);
    return 0;
}
