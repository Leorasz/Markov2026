import numpy as np
import matplotlib.pyplot as plt
a = 0.5
P = np.array([[1 - a, a, 0], [a, 0, 1 - a], [0, 1 - a, a]])
num_chains = 100000
max_n = 50
states = np.zeros(num_chains, dtype=int)
f_n = np.zeros(max_n + 1)
f_n[0] = 1.0

for n in range(1, max_n + 1):
    rands = np.random.rand(num_chains)
    cum_P = np.cumsum(P[states], axis=1)
    new_states = np.argmax(rands[:, None] < cum_P, axis=1)
    states = new_states
    f_n[n] = np.mean(states == 0)
s = np.sqrt(3 * a**2 - 3 * a + 1)
coef1 = (s - 1) / (6 * s * (1 - a))
coef2 = (s + 1) / (6 * s * (1 - a))
n_vals = np.arange(max_n + 1)
q_theo = (1/3) + coef1 * ((-s)**n_vals) * (1 - 2*a - s) + coef2 * (s**n_vals) * (1 - 2*a + s)

plt.plot(n_vals, f_n, label='Simulation')
plt.plot(n_vals, q_theo, label='Theoretical')
plt.xlabel('n')
plt.ylabel('Fraction in state 1')
plt.legend()
plt.show()
