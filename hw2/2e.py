import numpy as np
import matplotlib.pyplot as plt
import time

N = 10**6

def pdf(x):
    return np.where(x >= 0, x * np.exp(-x), 0)

#part b 
start_b = time.time()
us_b = np.random.uniform(0, 1, N)
y = 1 - us_b
low = np.zeros(N)
high = np.full(N, 50.0)
for _ in range(40):
    mid = (low + high) / 2
    ex = np.exp(-mid)
    g = ex * (mid + 1) - y
    low = np.where(g > 0, mid, low)
    high = np.where(g > 0, high, mid)
samples_b = (low + high) / 2
time_b = time.time() - start_b
print(f"Time for numerical inverse (b): {time_b} seconds")

#part c
c = 4 / np.e
theoretical_acc_rate = np.e / 4
num_proposals = int(N / theoretical_acc_rate * 1.1)
start_c = time.time()
us_x = np.random.uniform(0, 1, num_proposals)
xs = -2 * np.log(us_x)
gs = 0.5 * np.exp(-xs / 2)
fs = xs * np.exp(-xs)
ratios = fs / (c * gs)
us_acc = np.random.uniform(0, 1, num_proposals)
accepts = us_acc <= ratios
samples_c = xs[accepts][:N]
time_c = time.time() - start_c
print(f"Time for acceptance-rejection (c): {time_c} seconds")

#part d
start_d = time.time()
us1 = np.random.uniform(0, 1, N)
us2 = np.random.uniform(0, 1, N)
samples_d = -np.log(us1) - np.log(us2)
time_d = time.time() - start_d
print(f"Time for sum of exponentials (d): {time_d} seconds")

#histogram
bins = 50
x_range = [0, 15]
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(samples_d, bins=bins, range=x_range, density=True, alpha=0.6, color='blue', label='Histogram (sum of exp)')
x_vals = np.linspace(x_range[0], x_range[1], 1000)
ax.plot(x_vals, pdf(x_vals), 'r-', label='Theoretical PDF')
ax.set_title('Histogram of Samples from Sum of Exponentials')
ax.set_xlabel('x')
ax.set_ylabel('Density')
ax.set_xlim(x_range)
ax.legend()
plt.tight_layout()
plt.show()