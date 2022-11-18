#include <stdio.h>
#include "worldline.h"

int main() {
    srand(time(NULL)); // Generate random seed with time.
    // Define
    int N_size = 2;
    double beta = 12;
    double epsilon = 0.03;
    double mu = 1.4;
    int *wldline = NULL;
    int totsize = (int) (beta / epsilon) * N_size * N_size * N_size;
    int arrow = 1;      // Direction of time arrow
    int index = 0;      // Index of the flatten index
    int collision = 0;  // collision at the last move

    generate_worldline(N_size, beta, epsilon, wldline);
    index = random_start(totsize, wldline);
    arrow = index / totsize;
    index = index % totsize;

    int *forward = NULL;
    forward = calloc(totsize, sizeof(int));
    int direction = 0;

    while (1){
        if (arrow) {
            direction = move(epsilon);
            forward[index] = direction;
            update(direction,&index);
            if (wldline[index]) {
                collision = wldline[index];
                arrow = 0;
            }
            if (forward[index] == 4){
                wldline[index] = 4;
            }
            else{
                wldline[index] = -forward[index];
            }
            if (collision && !direction) {
                break;
            }
        }
        else{
            if (wldline[index]){
                break;
            }
            if (collision) {
                direction = collision;
                collision = 0;
            }
            else {
                direction = wldline[index];
                wldline[index] = 0;
            }
            reverse(direction, &index);
            forward[index] = 0;

            // Reject prob
            if (RANDF() > exp(-mu * epsilon)){
                arrow = 1;
            }
        }
    }




    free(wldline);
    return 0;
}
