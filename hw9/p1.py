import numpy as np

def simulate_delivery(L=20, alpha=1.0, beta=1.0, num_sims=10000):
    times = np.zeros(num_sims)
    for sim in range(num_sims):
        i = 0
        t = 0.0
        while i < L:
            if i == 0:
                dt = np.random.exponential(1 / alpha)
                t += dt
                i = 1
            else:
                rate = alpha + beta
                dt = np.random.exponential(1 / rate)
                t += dt
                if np.random.rand() < alpha / rate:
                    i += 1
                else:
                    i -= 1
        times[sim] = t
    return np.mean(times), np.var(times, ddof=1)

mean_est, var_est = simulate_delivery()
print(mean_est, var_est)
