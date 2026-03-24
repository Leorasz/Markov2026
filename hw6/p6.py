import random

def avalanche():
    total = 1
    active = 1
    while active:
        active = 2 * sum(random.random() < 0.5 for _ in range(active))
        total += active
    return total

n = 1000
count = sum(1 for _ in range(n) if avalanche() == 3)
print(count / n)
