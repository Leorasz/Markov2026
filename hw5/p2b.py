import numpy as np
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
print(pi)
