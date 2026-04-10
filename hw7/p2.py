import numpy as np
import matplotlib.pyplot as plt
from scipy.special import i0
from scipy.stats import poisson, binom

l = 3.0
t = 48.0
n_max = 1000
interA = np.random.exponential(1/l, n_max)
timesA = np.cumsum(interA)
timesA = timesA[timesA <= t]
interB = np.random.exponential(1/l, n_max)
timesB = np.cumsum(interB)
timesB = timesB[timesB <= t]
plt.figure(1)
for x in timesA: plt.axvline(x, color='red', linewidth=1)
for x in timesB: plt.axvline(x, color='blue', linewidth=1)
plt.xlim(0,t)
plt.show()

rate_tot = 2*l
inter = np.random.exponential(1/rate_tot, 2000)
times = np.cumsum(inter)
times = times[times <= t]
assign = np.random.rand(len(times)) < 0.5
timesA2 = times[assign]
timesB2 = times[~assign]
plt.figure(2)
for x in timesA2: plt.axvline(x, color='red', linewidth=1)
for x in timesB2: plt.axvline(x, color='blue', linewidth=1)
plt.xlim(0,t)
plt.show()

ng = 100000
N = poisson.rvs(2*l*t, size=ng)
NA = binom.rvs(N, 0.5, size=ng)
D = 2*(NA - (N - NA))
print(np.mean(D), np.var(D), np.mean(D == 0))
print('theo:', 0, 8*l*t, np.exp(-2*l*t)*i0(2*l*t))
