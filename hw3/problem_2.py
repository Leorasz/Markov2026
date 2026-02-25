import numpy as np

mat = np.array([[9/10,1/10,0],[0,7/8,1/8],[2/5,0,3/5]])

def self_matmul(x, power):
    if power == 1:
        return x
    return x @ self_matmul(x, power-1)

print(self_matmul(mat, 50))

N = 1_0000
count = 0
state = 0

for _ in range(N):
    state = np.random.choice(3, p=mat[state])
    if state == 0:
        count += 1

print(count / N)