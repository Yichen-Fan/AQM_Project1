import numpy as np
#import matplotlib.pyplot as plt


class grid:
    beta = 12  # beta for time
    n_size = 2  # spacial dimension for x y z axis
    x_size = n_size
    y_size = n_size
    z_size = n_size
    N = 0  # number of initial particle number
    forward = True
    cx, cy, cz, ct = 0, 0, 0, 0
    ix, iy, iz, it = 0, 0, 0, 0
    stop = False
    nt = beta
    epsilon = 1

    # Use a 100 \times 100 matrix to store all worldlines, 1 for there is a particle and 0 for no particle
    # The 0 axis for time, 1 for x axis, 2 for y axis and 3 for z axis
    location = np.zeros((beta, x_size, y_size, z_size))

    def __init__(self):
        self.mu = None
        self.N = 0
        self.n_size = 0
        self.direction = None
        #self.epsilon = None

    def initial_worldline(self, beta, n_size, mu, epsilon):
        self.beta = beta
        self.epsilon = epsilon
        self.mu = mu
        self.nt = int(beta / epsilon)
        self.location = np.zeros((self.nt, n_size, n_size, n_size))
        self.n_size = n_size
        self.N = np.random.randint(0, self.n_size**3-1)
        self.forward = True
        if self.N > (n_size**3 - 1):
            raise Exception("TOO MANY PARTICLES. Either reduce number of particles or increase the spatial size")
        for j in range(self.N):
            self.location[:, j // (n_size**2), (j // n_size) % n_size, j % n_size] = True

    def random_start(self):
        ct = np.random.randint(0, self.beta)
        cn = np.random.randint(0, self.N)
        return ct, cn

    def hop_right(self):
        nt = self.nt
        nx = self.x_size
        self.ct = (self.ct + 1) % nt
        self.cx = (self.cx + 1) % nx
        if not self.location[self.ct, self.cx, self.cy, self.cz]:
            self.location[self.ct, self.cx, self.cy, self.cz] = True
        else:
            #self.location[self.ct, self.cx, self.cy, self.cz] = False
            self.direction = 1
            self.forward = False

    def hop_left(self):
        nt = self.nt
        nx = self.x_size
        self.ct = (self.ct + 1) % nt
        self.cx = (self.cx - 1) % nx
        if not self.location[self.ct, self.cx, self.cy, self.cz]:
            self.location[self.ct, self.cx, self.cy, self.cz] = True
        else:
            #self.location[self.ct, self.cx, self.cy, self.cz] = False
            self.forward = False
            self.direction = 2

    def hop_front(self):
        nt = self.nt
        ny = self.y_size
        self.ct = (self.ct + 1) % nt
        self.cy = (self.cy + 1) % ny
        if not self.location[self.ct, self.cx, self.cy, self.cz]:
            self.location[self.ct, self.cx, self.cy, self.cz] = True
        else:
            #self.location[self.ct, self.cx, self.cy, self.cz] = False
            self.forward = False
            self.direction = 3

    def hop_back(self):
        nt = self.nt
        ny = self.y_size
        self.ct = (self.ct + 1) % nt
        self.cy = (self.cy - 1) % ny
        if not self.location[self.ct, self.cx, self.cy, self.cz]:
            self.location[self.ct, self.cx, self.cy, self.cz] = True
        else:
            #self.location[self.ct, self.cx, self.cy, self.cz] = False
            self.forward = False
            self.direction = 4

    def hop_up(self):
        nt = self.nt
        nz = self.z_size
        self.ct = (self.ct + 1) % nt
        self.cz = (self.cz + 1) % nz
        if not self.location[self.ct, self.cx, self.cy, self.cz]:
            self.location[self.ct, self.cx, self.cy, self.cz] = True
        else:
            #self.location[self.ct, self.cx, self.cy, self.cz] = False
            self.forward = False
            self.direction = 5

    def hop_down(self):
        nt = self.nt
        nz = self.z_size
        self.ct = (self.ct + 1) % nt
        self.cz = (self.cz - 1) % nz
        if not self.location[self.ct, self.cx, self.cy, self.cz]:
            self.location[self.ct, self.cx, self.cy, self.cz] = True
        else:
            #self.location[self.ct, self.cx, self.cy, self.cz] = False
            self.forward = False
            self.direction = 6

    def no_hop(self):
        nt = self.nt
        self.ct = (self.ct + 1) % nt
        if not self.location[self.ct, self.cx, self.cy, self.cz]:
            self.location[self.ct, self.cx, self.cy, self.cz] = True
        else:
            #self.location[self.ct, self.cx, self.cy, self.cz] = False
            self.forward = False
            self.direction = 0

    def reject(self):
        self.forward = True

    # TODO: Improve the algorithm. Avoid to annihilate particle in the original direction
    def reverse(self, cx, cy, cz, ct):
        nt = self.nt
        nx = self.x_size
        ny = self.y_size
        nz = self.z_size
        self.ct = (ct - 1) % nt
        ct = self.ct
        if self.location[ct, cx, cy, cz] and self.direction != 0:
            self.location[ct, cx, cy, cz] = False
        elif self.location[ct, (cx + 1) % nx, cy, cz] and self.direction != 2:
            self.location[ct, (cx + 1) % nx, cy, cz] = False
            self.cx = (cx + 1) % nx
        elif self.location[ct, (cx - 1) % nx, cy, cz] and self.direction != 1:
            self.location[ct, (cx - 1) % nx, cy, cz] = False
            self.cx = (cx - 1) % nx
        elif self.location[ct, cx, (cy + 1) % ny, cz] and self.direction != 4:
            self.location[ct, cx, (cy + 1) % ny, cz] = False
            self.cy = (cy + 1) % ny
        elif self.location[ct, cx, (cy - 1) % ny, cz] and self.direction != 3:
            self.location[ct, cx, (cy - 1) % ny, cz] = False
            self.cy = (cy - 1) % ny
        elif self.location[ct, cx, cy, (cz + 1) % nz] and self.direction != 6:
            self.location[ct, cx, cy, (cz + 1) % nz] = False
            self.cz = (cz + 1) % nz
        elif self.location[ct, cx, cy, (cz - 1) % nz] and self.direction != 5:
            self.location[ct, cx, cy, (cz - 1) % nz] = False
            self.cz = (cz - 1) % nz
        self.direction = 7

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

    def new_iter(self):
        self.ix, self.iy, self.iz = np.random.randint(0, self.x_size, 3, int)
        self.it = np.random.randint(0, self.nt, 1, int)
        self.stop = False
        if self.location[self.it, self.ix, self.iy, self.iz]:
            self.forward = False
        else:
            self.location[self.it, self.ix, self.iy, self.iz] = True
            self.forward = True


# TODO
# Randomly pick initial annihilation operator at the beginning of each iteration.
# 1 possible way is labeling world line and pick world line at a random time spot.
# Seeking for a better implementation.


grid = grid()
nstep = 5000
nsamplestep = 10
nMonte = nstep // nsamplestep
monte = []
position = np.zeros_like(grid.location)
npart = []
energy = []
#epsilon = [0.03, 0.02, 0.01, 0.008, 0.005, 0.002, 0.001]
epsilon = [0.03,0.02, 0.01]
for e in epsilon:
    grid.initial_worldline(beta=12, n_size=2, mu=1.4, epsilon=e)
    particle = 0
    for i in range(nstep):
        while not grid.stop:
            grid.move()
        if i % nsamplestep == 0:
            position = grid.location[0, :, :, :]
            particle += np.count_nonzero(position)
        grid.new_iter()
    particle = particle / (nstep // nsamplestep)
    npart.append(particle)
#npart = np.sum(monte) / (nstep // nsamplestep)
print(npart)

#plt.scatter(range(50), monte)
#plt.show()
