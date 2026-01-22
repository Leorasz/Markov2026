import numpy as np
import matplotlib.pyplot as plt

ks = np.arange(2, 11)
ns = 2**ks
theor = 1/ np.sqrt(ns)
estim = []
N_samples = 10**6

for n in ns:
    S = np.random.poisson(n, size=N_samples)

    Y = (S - n) / np.sqrt(n)

    y_mean = np.mean(Y)
    y_std = np.std(Y)

    skew_est = np.mean((Y - y_mean**3)) / y_std**3
    estim.append(skew_est)

fig, ax = plt.subplots()
ax.loglog(ns, theor, label="Theoretical", marker='o', linestyle='-')
ax.loglog(ns, estim, label='Estimated', marker='x', linestyle='--')
ax.set_xlabel('n (log scale)')
ax.set_ylabel('S(n) (log scale)')
ax.set_title('Log-Log Plot of Skewness S(n)')
ax.legend()
plt.show()
