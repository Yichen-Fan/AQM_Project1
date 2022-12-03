# AQM_Project1
AQM first project with Monte Carlo to generate worldlines.<br />

This program is written for physics 765 at duke on FA22 semester. There are two different versions, the python version is very slow and
the susceptibility calculations are only implemented in C version. Please use the C version. <br />

# How to make this project
CMake is required, the testing version of cmake is 3.18; <br />
Please call $cmake .$ before making this project. <br />

go to the MonteCarlo_Cversion folder, do following: <br />
cmake . <br />
make <br />
And the excutable file would be MonteCarlo_Cversion. <br />
######################################################## <br />
# Remember to make the program after any modification. # <br />
# Call cmake again when adding new file to the project.# <br />
######################################################## <br />

# Input file templete
The C version requires an input file, and the format of input file is the following: <br />
######################################################################################################################### <br />
N_size (int)          // Spacial dimension of the latice, must be positive integer greater or equal to 2;               # <br />
beta (floating)       // Temperature, a positive floating number, which determine the imaginary time,                   # <br />
                      // Note beta is supposed to be positive integer multiples of epsilon;                             # <br />
epsilon (floating)    // Length of time step, a positive floating number;                                               # <br />
mu (floating)         // Chemical potential, a positive floating numbe. Note the negative chemical potential            # <br />
                      // is unphysical for boson system;                                                                # <br />
nSweep (int)          // nSweep, a positive integer. The number of groups in Monte Carlo simulation;                    # <br />
nWait (int)           // nWait, a positive integer. Those configurations are discarded since they are not equilibrium;  # <br />
BlockSize (int)       // BlockSize, a positive inter. Number of configurations in each group.                           # <br />
######################################################################################################################### <br />

# Output from program
The default output would be printing on screen. If want to save the output, please use > to pip the text to files. <br />

# Credit
Yichen Fan, Tingguang Li and Boyu gao in 2022.

