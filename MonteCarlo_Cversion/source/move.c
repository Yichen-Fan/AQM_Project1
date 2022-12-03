//
// Created by Ethan  Fan  on 11/17/22.
//
#include "worldline.h"
#include <math.h>

int move(double epsilon) {
    double frand = RANDF();
    int direction = 4;
    if (frand < epsilon) {
        direction = 1;
    } else if (frand < 2 * epsilon) {
        direction = 2;
    } else if (frand < 3 * epsilon) {
        direction = 3;
    } else if (frand < 4 * epsilon) {
        direction = -1;
    } else if (frand < 5 * epsilon) {
        direction = -2;
    } else if (frand < 6 * epsilon) {
        direction = -3;
    }
    return direction;
}

void update(int direction, int N_size, int Ntime, int *pindex, int *table) {
    int old_index = *pindex;
    int Nsizes = N_size * N_size;
    int Nsizec = N_size * N_size * N_size;
    int ctime = (int) (old_index / Nsizec);
    int new_position;
    int position = (old_index - ctime * Nsizec);
    int ndirection;
    switch (direction) {
        case -3:
            new_position = table[position * 7];
            break;
        case -2:
            new_position = table[position * 7 + 1];
            break;
        case -1:
            new_position = table[position * 7 + 2];
            break;
        case 4:
            new_position = table[position * 7 + 3];
            break;
        case 1:
            new_position = table[position * 7 + 4];
            break;
        case 2:
            new_position = table[position * 7 + 5];;
            break;
        case 3:
            new_position = table[position * 7 + 6];
            break;
        default:
            new_position = table[position * 7 + 3];
            break;
    }
    ctime = (ctime + 1) % Ntime;
    *pindex = ctime * Nsizec + new_position;
}

void reverse(int direction, int N_size, int Ntime, int *pindex, int *table) {
    int old_index = *pindex;
    int Nsizes = N_size * N_size;
    int Nsizec = N_size * N_size * N_size;
    int ctime = (int) (old_index / Nsizec);
    int new_position;
    int position = (old_index - ctime * Nsizec);
    switch (direction) {
        case -3:
            new_position = table[position * 7];
            break;
        case -2:
            new_position = table[position * 7 + 1];
            break;
        case -1:
            new_position = table[position * 7 + 2];
            break;
        case 4:
            new_position = table[position * 7 + 3];
            break;
        case 1:
            new_position = table[position * 7 + 4];
            break;
        case 2:
            new_position = table[position * 7 + 5];;
            break;
        case 3:
            new_position = table[position * 7 + 6];
            break;
        default:
            new_position = table[position * 7 + 3];
            break;
    }
    ctime = (ctime - 1 + Ntime) % Ntime;
    *pindex = ctime * Nsizec + new_position;
}


void monte(int N_size, int Ntime, double epsilon, double mu, int *table, int *forward, int *backward) {
    int totsize = N_size * N_size * N_size * Ntime;
    int index = random_start(totsize);
    int initial = index;
    int arrow;
    if (forward[index]) {
        arrow = 0;
        initial *= -1;
    } else {
        arrow = 1;
    }
    int collision = 0;
    // int i = 0;
    int direction;
    while (1) {
        // i++;
        if (arrow) {
            direction = move(epsilon);
            forward[index] = direction;
            update(direction, N_size, Ntime,&index, table);
            if (backward[index]) {
                collision = backward[index];
                arrow = 0;
            }
            backward[index] = - direction;
            if (!collision && forward[index]) {
                // break;
            }
            if (index == initial) {
                break;
            }
        } else {
            if (backward[index] == 0) {
                break;
            }
            if (collision) {
                direction = collision;
                collision = 0; // If collision happened last time.
            } else {
                direction = backward[index];
                backward[index] = 0;
            }
            reverse(direction, N_size, Ntime,&index, table);
            forward[index] = 0;

            // Reject prob
            if (RANDF() < 1.0 - exp(-mu * epsilon)) {
                arrow = 1;
            }
        }
    }
}
