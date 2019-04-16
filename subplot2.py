import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 300)
y = x**2
sin_x = np.sin(x)
cos_x = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x, y, color="r")

plt.show()