import numpy as np

def softplus(x):
    return max(x, 0) + np.log(1 + np.exp(-abs(x)))