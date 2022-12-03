import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
number = pd.read_csv("data.csv").to_numpy().flatten()
numberstd = pd.read_csv("std.csv").to_numpy()
numberstd = numberstd.flatten()

mu = np.arange(0, 0.51, 0.01)
print(number)
print(numberstd)
fig, ax = plt.subplots()
plt.scatter(mu, number)
plt.errorbar(mu, number, yerr = numberstd, fmt = '.', label = "Average particle number")
ax.set_xlabel("Chemical potential")
ax.set_ylabel("Average particle number")
ax.set_title("Average particle number versus chemical potential")
ax.set_ylim(0, 4)
ax.set_xlim(0, 0.5)
plt.legend()
plt.show()
