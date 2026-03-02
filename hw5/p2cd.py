import numpy as np
import matplotlib.pyplot as plt
import random
a = 0.04
b = 0.16
K = 0.1
states = 5
p = np.zeros(states + 1)

for n in range(1, 5):
    p[n] = K * np.exp(a * n)

q = np.zeros(states + 1)
for n in range(2, 6):
    q[n] = K * np.exp(b * (n - 1))

P = np.zeros((states, states))
P[0, 0] = 1 - p[1]
P[0, 1] = p[1]
for i in range(1, 4):
    P[i, i - 1] = q[i + 1]
    P[i, i] = 1 - p[i + 1] - q[i + 1]
    P[i, i + 1] = p[i + 1]

P[4, 3] = q[5]
P[4, 4] = 1 - q[5]
eigvals, eigvecs = np.linalg.eig(P.T)
idx = np.argmin(np.abs(eigvals - 1))
pi = np.real(eigvecs[:, idx])
pi = pi / np.sum(pi)
print("Theoretical pi (eigen):", np.round(pi, 4))
pi_analytic = np.zeros(states)
ab = a - b

for i in range(states):
    ii = i + 1
    c = ab * (ii - 1) * ii / 2
    pi_analytic[i] = np.exp(c)
pi_analytic /= np.sum(pi_analytic)
print("Analytic pi:", np.round(pi_analytic, 4))
N = 10**6
current = 0
counts = np.zeros(states)

for _ in range(N):
    counts[current] += 1
    r = random.random()
    cum = 0
    for next_state in range(states):
        cum += P[current, next_state]
        if r < cum:
            current = next_state
            break
frac = counts / N
states_labels = np.arange(1, 6)
width = 0.25
fig, ax = plt.subplots()
ax.bar(states_labels - width, pi, width, label='Numeric')
ax.bar(states_labels, pi_analytic, width, label='Analytic')
ax.bar(states_labels + width, frac, width, label='Simulated')
ax.set_xlabel('State')
ax.set_ylabel('Fraction')
ax.set_title('Theoretical vs. Simulated Stationary Distribution')
ax.legend()
plt.show()