//
// Created by Ethan  Fan  on 11/17/22.
//
#include "worldline.h"

int move(double epsilon){
    double frand = RANDF();
    int direction = 4;
    if (frand < epsilon){
        direction = 1;
    }
    else if(frand < 2 * epsilon){
        direction = -1;
    }
    else if(frand < 3 * epsilon){
        direction = 2;
    }
    else if(frand < 4 * epsilon){
        direction = -2;
    }
    else if(frand < 5 * epsilon){
        direction = 3;
    }
    else if(frand < 6 * epsilon){
        direction = -3;
    }
    return direction;
}

void update(int direction, int N_size, int Ntime, int* pindex) {
    int old_index = *pindex;
    int Nsizes = N_size * N_size;
    int Nsizec = N_size * N_size * N_size;
    int ctime = (int) (old_index / Nsizec);
    int cx, cy, cz;
    cx = (old_index - ctime * Nsizec) % N_size;
    cy = (int) ((old_index - ctime * Nsizec) % Nsizes) / N_size;
    cz = (int) (old_index - ctime * Nsizec) % (Nsizec) / Nsizes;
    ctime = (ctime + 1) % Ntime;
    switch (direction) {
        case 1:
            cx = (cx + 1) % N_size;
            break;
        case 2:
            cy = (cy + 1) % N_size;
            break;
        case 3:
            cz = (cz + 1) % N_size;
            break;
        case -1:
            cx = (cx - 1 + N_size) % N_size;
            break;
        case -2:
            cy = (cy - 1 + N_size) % N_size;
            break;
        case -3:
            cz = (cz - 1 + N_size) % N_size;
            break;
        default:
            break;
    }
    *pindex = ctime * 8 + cz * 4 + cy * 2 + cx;
}
void reverse(int direction, int N_size, int Ntime, int *pindex){
    int old_index = *pindex;
    int Nsizes = N_size * N_size;
    int Nsizec = N_size * N_size * N_size;
    int ctime = (int) (old_index / Nsizec);
    int cx, cy, cz;
    cx = (old_index - ctime * Nsizec) % N_size;
    cy = (int) ((old_index - ctime * Nsizec) % Nsizes) / N_size;
    cz = (int) (old_index - ctime * Nsizec) % (Nsizec) / Nsizes;
    ctime = (ctime - 1 + Ntime) % Ntime;
    switch (direction) {
        case 1:
            cx = (cx + 1) % N_size;
            break;
        case 2:
            cy = (cy + 1) % N_size;
            break;
        case 3:
            cz = (cz + 1) % N_size;
            break;
        case -1:
            cx = (cx - 1 + N_size) % N_size;
            break;
        case -2:
            cy = (cy - 1 + N_size) % N_size;
            break;
        case -3:
            cz = (cz - 1 + N_size) % N_size;
            break;
        default:
            break;
    }
    *pindex = ctime * 8 + cz * 4 + cy * 2 + cx;
}
