import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 300)
y = x**2

plt.plot(x, y, color="r")
plt.show()