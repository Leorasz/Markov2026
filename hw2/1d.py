import numpy as np
import matplotlib.pyplot as plt

gamma = 4
x0 = 10
Ns = [100, 1000, 10000]
bins = 50
x_range = [0, 60]

C = (gamma - 1) * x0**(gamma - 1)
def pdf(x):
    return np.where(x >= x0, C * x**(-gamma), 0)

fig, axs = plt.subplots(1, 3, figsize=(15, 5))
x_vals = np.linspace(x0, x_range[1], 1000)

for i, N in enumerate(Ns):
    u = np.random.uniform(0, 1, N)
    samples = x0 * (1 - u)**(-1/(gamma - 1))
    
    axs[i].hist(samples, bins=bins, range=x_range, density=True, alpha=0.6, color='blue', label='Histogram')
    
    axs[i].plot(x_vals, pdf(x_vals), 'r-', label='Theoretical PDF')
    
    axs[i].set_title(f'N = {N}')
    axs[i].set_xlabel('x')
    axs[i].set_ylabel('Density')
    axs[i].set_xlim(x_range)
    axs[i].legend()

plt.tight_layout()
plt.show()