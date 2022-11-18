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

void update(int direction, int* pindex) {
    int old_index = *pindex;
    switch (direction) {
        case 1:

            break;
        case 2:

            break;
        case 3:

            break;
        case -1:

            break;
        case -2:

            break;
        case -3:

            break;
        default:
            break;
    }
}
void reverse(int direction, int *pindex){
    int oldindex = *pindex;
    switch (direction) {
        case 1:

            break;
        case 2:

            break;
        case 3:

            break;
        case -1:

            break;
        case -2:

            break;
        case -3:

            break;
        default:

            break;
    }
}
