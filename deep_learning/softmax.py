import numpy as np
def softmax_of(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(a)
    y = exp_a / sum_exp_a

    return y
    # この書き方だとオーバーフローの危険あり

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) # オーバーフロー対策
    sum_exp_a = np.sum(exp_a)

    y = exp_a / sum_exp_a
    return y

def softmax_2ax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T 

    x = x - np.max(x) # オーバーフロー対策
    return np.exp(x) / np.sum(np.exp(x))

    