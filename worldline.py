import numpy as np


class grid:
    beta = 12  # beta for time
    x_size = 10  # spacial dimension for x axis
    y_size = 10  # spacial dimension for y axis
    z_size = 10  # spacial dimension for z axis
    N = 2  # number of world lines
    forward = True
    cx, cy, cz, ct = 0, 0, 0, 0
    ix, iy, iz, it = 0, 0, 0, 0
    stop = False

    # Use a 100 \times 100 matrix to store all worldlines, 1 for there is a particle and 0 for no particle
    # The 0 axis for time, 1 for x axis, 2 for y axis and 3 for z axis
    location = np.zeros((beta, x_size, y_size, z_size))

    def __init__(self):
        self.mu = None
        self.epsilon = None

    def initial_worldline(self, beta, x, y, z, N, mu, epsilon):
        self.beta = beta
        self.epsilon = epsilon
        self.mu = mu
        t = beta//epsilon
        self.location = np.zeros((t, x, y, z))
        self.x_size = x
        self.y_size = y
        self.z_size = z
        self.N = N
        self.forward = True
        if N >= (x * y * z - 1):
            raise Exception("TOO MANY PARTICLES. Either reduce number of particles or increase the spatial size")
        for i in range(self.N):
            self.location[:, i // 100, (i // 10) % 10, i % 10] = True

    def random_start(self):
        ct = np.random.randint(0, self.beta)
        cn = np.random.randint(0, self.N)
        return ct, cn

    def hop_right(self):
        if not self.location[self.ct + 1, self.cx + 1, self.cy, self.cz]:
            self.location[self.ct + 1, self.cx + 1, self.cy, self.cz] = True
        else:
            self.location[self.ct + 1, self.cx + 1, self.cy, self.cz] = False
            self.forward = False
        self.ct += 1
        self.cx += 1

    def hop_left(self):
        if not self.location[self.ct + 1, self.cx - 1, self.cy, self.cz]:
            self.location[self.ct + 1, self.cx - 1, self.cy, self.cz] = True
        else:
            self.location[self.ct + 1, self.cx - 1, self.cy, self.cz] = False
            self.forward = False
        self.ct += 1
        self.cx -= 1

    def hop_front(self):
        if not self.location[self.ct + 1, self.cx, self.cy + 1, self.cz]:
            self.location[self.ct + 1, self.cx, self.cy + 1, self.cz] = True
        else:
            self.location[self.ct + 1, self.cx, self.cy + 1, self.cz] = False
            self.forward = False
        self.ct += 1
        self.cy += 1

    def hop_back(self):
        if not self.location[self.ct + 1, self.cx, self.cy - 1, self.cz]:
            self.location[self.ct + 1, self.cx, self.cy - 1, self.cz] = True
        else:
            self.location[self.ct + 1, self.cx, self.cy - 1, self.cz] = False
            self.forward = False
        self.ct += 1
        self.cy -= 1

    def hop_up(self):
        if not self.location[self.ct + 1, self.cx, self.cy, self.cz + 1]:
            self.location[self.ct + 1, self.cx, self.cy, self.cz + 1] = True
        else:
            self.location[self.ct + 1, self.cx, self.cy, self.cz + 1] = False
            self.forward = False
        self.ct += 1
        self.cz += 1

    def hop_down(self):
        if not self.location[self.ct + 1, self.cx, self.cy, self.cz - 1]:
            self.location[self.ct + 1, self.cx, self.cy, self.cz - 1] = True
        else:
            self.location[self.ct + 1, self.cx, self.cy, self.cz - 1] = False
            self.forward = False
        self.ct += 1
        self.cz -= 1

    def no_hop(self):
        if not self.location[self.ct + 1, self.cx, self.cy, self.cz]:
            self.location[self.ct + 1, self.cx, self.cy, self.cz] = True
        else:
            self.location[self.ct + 1, self.cx, self.cy, self.cz] = False
            self.forward = False
        self.ct +=1

    def reject(self):
        self.forward = True

    def reverse(self, cx, cy, cz, ct):
        if self.location[ct - 1, cx, cy, cz]:
            self.location[ct - 1, cx, cy, cz] = False
            self.ct -= 1
        elif self.location[ct - 1, cx + 1, cy, cz]:
            self.location[ct - 1, cx + 1, cy, cz] = False
            self.ct -= 1
            self.cx += 1
        elif self.location[ct - 1, cx - 1, cy, cz]:
            self.location[ct - 1, cx - 1, cy, cz] = False
            self.ct -= 1
            self.cx -= 1
        elif self.location[ct - 1, cx, cy + 1, cz]:
            self.location[ct - 1, cx, cy + 1, cz] = False
            self.ct -= 1
            self.cy += 1
        elif self.location[ct - 1, cx, cy - 1, cz]:
            self.location[ct - 1, cx, cy - 1, cz] = False
            self.ct -= 1
            self.cy -= 1
        elif self.location[ct - 1, cx, cy, cz + 1]:
            self.location[ct - 1, cx, cy, cz + 1] = False
            self.ct -= 1
            self.cz += 1
        elif self.location[ct - 1, cx, cy, cz - 1]:
            self.location[ct - 1, cx, cy, cz - 1] = False
            self.ct -= 1
            self.cz -= 1

    def approve_prob(self):
        rand = np.random.uniform(0, 1)
        if rand < self.epsilon:
            self.hop_up()
        elif rand < 2 * self.epsilon:
            self.hop_down()
        elif rand < 3 * self.epsilon:
            self.hop_front()
        elif rand < 4 * self.epsilon:
            self.hop_back()
        elif rand < 5 * self.epsilon:
            self.hop_right()
        elif rand < 6 * self.epsilon:
            self.hop_left()
        else:
            self.no_hop()

    def reject_prob(self):
        rand = np.random.uniform(0, 1)
        if rand < np.exp(- self.mu * self.epsilon):
            self.reverse(self.cx, self.cy, self.cz, self.ct)
        else:
            self.reject()
            self.approve_prob()
            if self.ix == self.cx and self.iy == self.cy and self.iz == self.cz and self.it == self.ct:
                self.stop = True

    def move(self):
        if self.forward:
            self.approve_prob()
            if self.ix == self.cx and self.iy == self.cy and self.iz == self.cz and self.it == self.ct:
                self.stop = True
        else:
            self.reject_prob()

    def print_grid(self):
        print(self.location)

# TODO
# Randomly pick initial annihilation operator at the beginning of each iteration.
# 1 possible way is labeling world line and pick world line at a random time spot.
# Seeking for a better implementation.


grid = grid()
grid.initial_worldline(beta=12, x=10, y=10, z=10, N=2, mu = 5, epsilon=1)
nstep = 10000
nsamplestep = 50
monte = []
randarr = np.random.uniform(0, 1, nstep)

# TODO
# Finish the Monte Carlo iteration, and collect all information.
for i in range(nstep):
    while not grid.stop:
        grid.move()
    if i % nsamplestep == 0:
        monte.append(grid)







