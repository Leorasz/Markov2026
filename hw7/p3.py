import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
T = 120.0
lmax = 0.5 * (1 + (T/30)**2)
num = poisson.rvs(lmax * T)
times = np.sort(np.random.uniform(0, T, num))
lt = 0.5 * (1 + (times / 30)**2)
u = np.random.rand(num)
keep = u < (lt / lmax)
times_keep = times[keep]
plt.hist(times_keep, bins=120)
plt.show()
print(len(times_keep))
