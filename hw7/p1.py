import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from scipy.special import i0

la = 2 / 90.0
lb = 1.5 / 90.0
T = 90.0
pwin = 0.0
for k in range(40):
    pwin = pwin + poisson.pmf(k,1.5) * (1 - poisson.cdf(k,2))
print(pwin)
print(la * 3)

t = np.linspace(0, T, 300)
tau = T - t
pb = np.exp(-(la + lb) * tau) * i0(2 * np.sqrt(la * lb) * tau)
plt.plot(t, pb)
plt.show()

pc = np.zeros(300)
for i in range(300):
    if t[i] <= 60:
        pc[i] = np.exp(-(la + lb) * tau[i]) * i0(2 * np.sqrt(la * lb) * tau[i])
    else:
        tau_i = T - t[i]
        p = 0.0
        mua = la * tau_i
        mub = lb * tau_i
        for m in range(40):
            p = p + poisson.pmf(m, mua) * poisson.pmf(m + 1, mub)
        pc[i] = p

plt.plot(t, pc)
plt.show()
