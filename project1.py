import numpy as np
import matplotlib.pyplot as plt


class worldline:
    def read(Ntime, Nsize, mu, epsilon):
        self.Ntime = Ntime
        self.Nsize = Nsize
        self.mu = mu
        self.epsilon = epsilon

    def __init__(self):
        self.Ntime = 1
        self.Nsize = 2
        self.mu = 1.4
        self.epsilon = 1
        self.forward = np.zeros((Ntime, Nsize, Nsize, Nsize), dtype=int)
        self.reverse = np.zeros((Ntime, Nsize, Nsize, Nsize), dtype=int)
        self.arrow = 0

    def move(self):
        Ntime = self.Ntime
        Nsize = self.Nsize
        mu = self.mu
        epsilon = self.epsilon
        # 0 index for time, 1 2 3 for x y z axis
        config = np.zeros(4, dtype=int)
        config[0] = np.random.randint(Ntime)
        config[1] = np.random.randint(Nsize)
        config[2] = np.random.randint(Nsize)
        config[3] = np.random.randint(Nsize)
        # Random start, creation if there is no particle otherwise annihilation
        if self.forward[config[0], config[1], config[2], config[3]] == 0:
            # Time is going forward
            self.arrow = 1
        else:
            # Time is going backward
            self.arrow = -1
        collision = 0
        while True:
            # Time forward
            if self.arrow == 1:
                # In three dimension space, epsilon for each direction. There are six direction in total
                rand = np.random.uniform(0, 1)
                if rand < epsilon:
                    direction = 1
                elif rand < 2 * epsilon:
                    direction = -1
                elif rand < 3 * epsilon:
                    direction = 2
                elif rand < 4 * epsilon:
                    direction = -2
                elif rand < 5 * epsilon:
                    direction = 3
                elif rand < 6 * epsilon:
                    direction = -3
                else:
                    direction = 4

                self.forward[config[0], config[1], config[2], config[3]] = direction

                # Update configuration
                if direction != 4:
                    config[int(abs(direction))] = (config[int(abs(direction))] + np.sign(direction)) % Nsize  # Hop
                config[0] = (config[0] + 1) % Ntime  # t = t + 1

                # Hard core potential
                if self.reverse[config[0], config[1], config[2], config[3]] != 0:
                    collision = self.reverse[config[0], config[1], config[2], config[3]]
                    self.arrow = -1
                    # Already a particle there, reverse time direction

                # Record last move
                if direction == 4:
                    self.reverse[config[0], config[1], config[2], config[3]] = 4
                else:
                    self.reverse[config[0], config[1], config[2], config[3]] = -direction

                # Stop the loop if back to collision
                if (collision == 0) and (self.forward[config[0], config[1], config[2], config[3]]) != 0:
                    break

                # Time arrow is backward
            elif self.arrow == -1:

                # Stop the loop if there is no particle can be annihilated
                if self.reverse[config[0], config[1], config[2], config[3]] == 0:
                    break

                # Prevent to cut the world line we just created
                if collision != 0:
                    direction = collision
                    collision = 0
                else:
                    direction = self.reverse[config[0], config[1], config[2], config[3]]
                    self.reverse[config[0], config[1], config[2], config[3]] = 0

                # Annihilate particle according to direction of hop
                if direction != 4:
                    config[int(abs(direction))] = (config[int(abs(direction))] + np.sign(direction)) % Nsize
                config[0] = (config[0] - 1) % Ntime  # t = t - 1

                # Update the direction for next time
                self.forward[config[0], config[1], config[2], config[3]] = 0

                # Reject reverse motion according to chemical potential
                if np.random.random() < (1 - np.exp(-mu * epsilon)):
                    self.arrow = 1

    def count_number(self):
        # Since particle number conserved within configuration, we pick the first time step
        return np.count_nonzero(self.forward[0, :, :, :])

    # return the energy of the system
    def energy(self):
        spatial_hops = np.count_nonzero(abs(self.forward) == 1) \
                       + np.count_nonzero(abs(self.forward) == 2) \
                       + np.count_nonzero(abs(self.forward) == 3)
        return -spatial_hops / self.beta + 2 * 3 * worldline.count_number(self)


# Monte Carlo steps
Nstep = 10  # Steps between each sampling
NMonte = 1000  # Number of total monte carlo size
GroupNum = 50  # Number of groups use to calculate stdev
GroupSize = NMonte // GroupNum  # Number of elements in each group
Nwait = 30  # Number of steps before collecting data

Nsize = 2  # Size of spatial coordinate
beta = 12  # Beta

epsilon = np.asarray([0.03, 0.02, 0.01, 0.008, 0.005, 0.002, 0.001])
particleList = []
energyList = []
stdNumber = []
stdEnergy = []
meanNumber = []
meanEnergy = []
for e in epsilon:
    Ntime = beta // e  # Ntime step is beta // epsilon
    worldline.read(Ntime, Nsize, mu=1.4, epsilon=e)
    worldline.__init__()
    Particlenumber = np.zeros(GroupNum)
    EnergyArr = np.zeros(GroupNum)
    for nstep in range(Nwair):
        worldline.move()
    for g in range(GroupNum):
        for i in range(GroupSize):
            for t in range(Nstep):
                worldline.move()
            Particlenumber[GroupNum] += worldline.count_number()
            EnergyArrp[GroupNum] += worldline.energy()
        Particlenumber[GroupNum] *= 1.0 / GroupSize
        EnergyArr[GroupNum] *= 1.0 / GroupSize
    # particleList.append(Particlenumber)
    # energyList.append(EnergyArr)
    stdEnergy.append(np.std(EnergyArr))
    meanEnergy.append(np.mean(EnergyArr))
    stdNumber.append(np.std(Particlenumber))
    meanNumber.append(np.mean(Particlenumber))

print("Error in particle number:")
print(stdNumber)
print("Mean of particle number:")
print(meanNumber)
print("Error in energy:")
print(stdEnergy)
print("Mean of energy:")
print(meanEnergy)










