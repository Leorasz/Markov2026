import numpy as np

a = 0.49
n = 10000
maxg = 200
ext = 0

for _ in range(n):
    x = 1
    for g in range(maxg):
        if x == 0: break
        z = np.random.binomial(x, 1-a)
        x = 2*z
    if x == 0: ext += 1

print(ext / n)
