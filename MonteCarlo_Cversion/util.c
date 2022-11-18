//
// Created by Ethan  Fan  on 11/17/22.
//
#include "util.h"


double RANDF(){
    return (double) (rand() % 100000000) / 100000000;
}
int RANDI(int ceil){
    return (int) (rand() % ceil);
}