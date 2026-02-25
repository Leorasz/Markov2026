import numpy as np

mat = np.array([[1/2, 1/2, 0,0,0,0],[0,1/2,1/2,0,0,0],[1/3,0,1/3,1/3,0,0],[0,0,0,1/2,1/2,0],[0,0,0,0,0,1],[0,0,0,0,1,0]])

def self_matmul(x, power):
    if power == 1:
        return x
    return x @ self_matmul(x, power-1)

print((np.array([1,0,0,0,0,0]) @ self_matmul(mat, 5))[4-1])

N = 1_0000
count = 0

for _ in range(N):
    state = 0
    for step in range(5):
        state = np.random.choice(6, p=mat[state])
    if state == 3:
        count += 1
fraction = count / N
print(fraction)
