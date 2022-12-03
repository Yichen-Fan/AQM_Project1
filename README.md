# AQM_Project1
AQM first project with Monte Carlo to generate worldlines.

This program is written for physics 765 at duke on FA22 semester. There are two different versions, the python version is very slow and
the susceptibility calculations are only implemented in C version. Please use the C version. 

# How to make this project
CMake is required, the testing version of cmake is 3.18;
Please call $cmake .$ before making this project.

go to the MonteCarlo_Cversion folder, do following:
cmake .
make
And the excutable file would be MonteCarlo_Cversion. 
########################################################
# Remember to make the program after any modification. #
# Call cmake again when adding new file to the project.#
########################################################

# Input file templete
The C version requires an input file, and the format of input file is the following:
#########################################################################################################################
N_size (int)          // Spacial dimension of the latice, must be positive integer greater or equal to 2;               #
beta (floating)       // Temperature, a positive floating number, which determine the imaginary time,                   #
                      // Note beta is supposed to be positive integer multiples of epsilon;                             #
epsilon (floating)    // Length of time step, a positive floating number;                                               #
mu (floating)         // Chemical potential, a positive floating numbe. Note the negative chemical potential            #
                      // is unphysical for boson system;                                                                #
nSweep (int)          // nSweep, a positive integer. The number of groups in Monte Carlo simulation;                    #
nWait (int)           // nWait, a positive integer. Those configurations are discarded since they are not equilibrium;  #
BlockSize (int)       // BlockSize, a positive inter. Number of configurations in each group.                           #
#########################################################################################################################

# Output from program
The default output would be printing on screen. If want to save the output, please use > to pip the text to files.

# Credit
Yichen Fan, Tingguang Li and Boyu gao in 2022.

