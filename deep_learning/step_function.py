def step_function1(x):
    if x > 0:
        return 1
    else:
        return 0

import numpy as np

def step_function2(x):
    y = x > 0
    return y.astype(np.int)

import matplotlib.pylab as plt

def step_function(x):
   return  np.array(x > 0, dtype=np.int)

def plot_step():
    x = np.arange(-5.0, 5.0, 0.1)
    y = step_function(x)
    plt.plot(x, y)
    plt.ulim(-0.1, 1.1)
    plt.show()