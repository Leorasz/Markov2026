import numpy as np
import matplotlib.pyplot as plt

N = 10**5

samples = np.random.uniform(0, 1, N*3)

maxxed = np.maximum.reduce([samples[0:N], samples[N:2*N], samples[2*N:]])

plt.hist(maxxed, bins = 50, density=True, alpha = 0.6, label='Simulation')

x = np.linspace(0, 1, 1000)
my_pdf = 3 * x**2

plt.plot(x, my_pdf, label='My Theoretical PDF')

plt.xlabel('Time (scaled 0 to 1)')
plt.ylabel('Density')
plt.title('Problem 4)b) Simulation vs. Theoretical PDF')
plt.legend()
plt.grid(True)

plt.show()