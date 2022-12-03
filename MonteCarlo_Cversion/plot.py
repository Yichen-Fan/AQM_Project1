import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
number = pd.read_csv("N20/avg.csv", header = None, delimiter = '\\s').to_numpy()
numberstd = pd.read_csv("N20/std.csv", header = None, delimiter = '\\s').to_numpy()
print(number)
print(numberstd)

fig, ax = plt.subplots()
plt.scatter(number[:, 0], number[:,1])
plt.errorbar(number[:,0], number[:,1], yerr = numberstd[:,1]/(5000**0.5), fmt = '.', label = "Average susceptibility")
ax.set_xlabel("Beta (inverse temperature")
ax.set_ylabel("Average susceptibility")
ax.set_title("Average susceptibility versus inverse temperature")
plt.legend()
plt.show()
