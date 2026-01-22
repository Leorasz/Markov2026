import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def f(u):
    return u**4 / (1 + u**6)

true_i, _ = integrate.quad(f, 0, 1)
print(f"The true integral value is {true_i}")

xs = np.arange(1, 5.1, 0.1)
Ns = np.floor(10**xs).astype(int)

estimates = []

for N in Ns:
    u = np.random.uniform(0, 1, N)
    y = np.random.uniform(0, 1, N)

    estimates.append(np.sum(y < f(u)) / N)

plt.semilogx(Ns, estimates, label='Monte Carlo')
plt.axhline(true_i, color = 'r', label = 'True Integral')
plt.xlabel('log(N)')
plt.ylabel('E(N)')
plt.title('Monte Carlo Integration vs. Actual')
plt.legend()
plt.show()