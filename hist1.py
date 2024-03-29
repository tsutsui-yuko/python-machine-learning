import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
l = []
for _ in range(1000):
    l.append(np.random.randint(1, 7, size=10).sum())

plt.hist(l, np.arange(15, 55, 2), color="gray")
plt.show()