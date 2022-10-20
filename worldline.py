import numpy as np


class grid:
    beta = 12  # beta for time
    x_size = 10  # spacial dimension for x axis
    y_size = 10  # spacial dimension for y axis
    z_size = 10  # spacial dimension for z axis
    N = 2  # number of world lines
    forward = True

    # Use a 100 \times 100 matrix to store all worldlines, 1 for there is a particle and 0 for no particle
    # The 0 axis for time, 1 for x axis, 2 for y axis and 3 for z axis
    location = np.zeros((beta, x_size, y_size, z_size))

    def initial_worldline(self, beta, x, y, z, N):
        self.location = np.zeros((beta, x, y, z))
        self.beta = beta
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

    def hop_right(self, cx, cy, cz, ct):
        if not self.location[ct + 1, cx + 1, cy, cz]:
            self.location[ct + 1, cx + 1, cy, cz] = True
        else:
            self.location[ct + 1, cx + 1, cy, cz] = False
            self.forward = False

    def hop_left(self, cx, cy, cz, ct):
        if not self.location[ct + 1, cx - 1, cy, cz]:
            self.location[ct + 1, cx - 1, cy, cz] = True
        else:
            self.location[ct + 1, cx - 1, cy, cz] = False
            self.forward = False

    def hop_front(self, cx, cy, cz, ct):
        if not self.location[ct + 1, cx, cy + 1, cz]:
            self.location[ct + 1, cx, cy + 1, cz] = True
        else:
            self.location[ct + 1, cx, cy + 1, cz] = False
            self.forward = False

    def hop_back(self, cx, cy, cz, ct):
        if not self.location[ct + 1, cx, cy - 1, cz]:
            self.location[ct + 1, cx, cy - 1, cz] = True
        else:
            self.location[ct + 1, cx, cy - 1, cz] = False
            self.forward = False

    def hop_up(self, cx, cy, cz, ct):
        if not self.location[ct + 1, cx, cy, cz + 1]:
            self.location[ct + 1, cx, cy, cz + 1] = True
        else:
            self.location[ct + 1, cx, cy, cz + 1] = False
            self.forward = False

    def hop_down(self, cx, cy, cz, ct):
        if not self.location[ct + 1, cx, cy, cz - 1]:
            self.location[ct + 1, cx, cy, cz - 1] = True
        else:
            self.location[ct + 1, cx, cy, cz - 1] = False
            self.forward = False

    def no_hop(self, cx, cy, cz, ct):
        if not self.location[ct + 1, cx, cy, cz]:
            self.location[ct + 1, cx, cy, cz] = True
        else:
            self.location[ct + 1, cx, cy, cz] = False
            self.forward = False

    def reject(self):
        self.forward = True

    def reverse(self, cx, cy, cz, ct):
        if self.location[ct - 1, cx, cy, cz]:
            self.location[ct - 1, cx, cy, cz] = False
        elif self.location[ct - 1, cx + 1, cy, cz]:
            self.location[ct - 1, cx + 1, cy, cz] = False
        elif self.location[ct - 1, cx - 1, cy, cz]:
            self.location[ct - 1, cx - 1, cy, cz] = False
        elif self.location[ct - 1, cx, cy + 1, cz]:
            self.location[ct - 1, cx, cy + 1, cz] = False
        elif self.location[ct - 1, cx, cy - 1, cz]:
            self.location[ct - 1, cx, cy - 1, cz] = False
        elif self.location[ct - 1, cx, cy, cz + 1]:
            self.location[ct - 1, cx, cy, cz + 1] = False
        elif self.location[ct - 1, cx, cy, cz - 1]:
            self.location[ct - 1, cx, cy, cz - 1] = False

    def print_grid(self):
        print(self.location)


grid = grid()
grid.initial_worldline(beta=12, x=10, y=10, z=10, N=2)

