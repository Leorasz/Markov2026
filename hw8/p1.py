import numpy as np
import matplotlib.pyplot as plt

ts = np.linspace(0, 5, 200)
Ns = [100, 1000, 10000, 100000]

for N in Ns:
    initials = np.random.choice([1,2], size=N, p=[1./3, 2./3])
    frac = []
    for t in ts:
        K = np.random.poisson(t, N)
        states = ((initials - 1 + K) % 4) + 1
        frac.append(np.mean(states == 1))
    plt.plot(ts, frac)
    plt.plot(ts, 1/4 - (1/12)*np.exp(-2*ts) + np.exp(-ts)*((1/6)*np.cos(ts) - (1/3)*np.sin(ts)))
    plt.xlim(0,5)
    plt.ylim(0,0.5)
    plt.show()
