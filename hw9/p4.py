import numpy as np
import matplotlib.pyplot as plt

m_values = np.arange(1, 101)
stochastic = np.array([np.sum(1.0 / np.arange(1, m)) for m in m_values])
deterministic = np.log(m_values)

plt.figure(figsize=(8, 5))
plt.plot(m_values, stochastic, label='Stochastic: sum_{k=1}^{m-1} 1/k', linewidth=2)
plt.plot(m_values, deterministic, label='Deterministic: ln(m)', linewidth=2)
plt.xlabel('m (number of particles)')
plt.ylabel(r'$\tau_m$ (time to reach m particles, β=1)')
plt.title('Comparison of Stochastic and Deterministic τ_m for Yule Process')
plt.legend()
plt.grid(True)
plt.show()
