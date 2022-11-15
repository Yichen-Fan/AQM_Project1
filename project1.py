import numpy as np
import matplotlib.pyplot as plt


class worldline:
    def __init__(self):
        Ntime = 1
        Nsize = 2
        mu = 1.4
        epsilon = 1
        forward = np.zeros((Ntime, Nsize, Nsize, Nsize))
        reverse = np.zeros((Ntime, Nsize, Nsize, Nsize))
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
        spatial_hops =  np.count_nonzero(abs(self.forward) == 1) \
                        + np.count_nonzero(abs(self.forward) == 2)\
                        + np.count_nonzero(abs(self.forward) == 3)
        return -spatial_hops / beta + 2 * 3 * worldline.count_number()
