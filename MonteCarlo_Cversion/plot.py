import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
number24 = pd.read_csv("N24/avg.csv", header = None, delimiter = '\\s').to_numpy()
numberstd24 = pd.read_csv("N24/std.csv", header = None, delimiter = '\\s').to_numpy()
number20 = pd.read_csv("N20/avg.csv", header = None, delimiter = '\\s').to_numpy()
numberstd20 = pd.read_csv("N20/std.csv", header = None, delimiter = '\\s').to_numpy()
number16 = pd.read_csv("N16/avg.csv", header = None, delimiter = '\\s').to_numpy()
numberstd16 = pd.read_csv("N16/std.csv", header = None, delimiter = '\\s').to_numpy()

fig, ax = plt.subplots()
plt.plot(number24[:, 0], number24[:,1] * 24, color = 'r')
plt.errorbar(number24[:,0], number24[:,1] * 24, yerr = numberstd24[:,1]/(5000**0.5) * 24, fmt = 'r.', label = "N=24")
plt.plot(number20[:, 0], number20[:,1] * 20, color = 'b')
plt.errorbar(number20[:,0], number20[:,1] * 20, yerr = numberstd20[:,1]/(5000**0.5) * 20, fmt = 'b.', label = "N=20")
plt.plot(number16[:, 0], number16[:,1] * 16, color = 'y')
plt.errorbar(number16[:,0], number16[:,1] * 16, yerr = numberstd16[:,1]/(5000**0.5) * 16, fmt = 'y.', label = "N=16")
ax.set_xlabel("Beta (inverse temperature)")
ax.set_ylabel("Average susceptibility")
ax.set_xlim(0.88, 0.95)
ax.set_ylim(0, 1.5)
ax.set_title("Average susceptibility versus inverse temperature on different lattice size")
plt.grid()
plt.legend()
plt.show()
