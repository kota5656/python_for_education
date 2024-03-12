import math
import numpy as np
import matplotlib.pyplot as plt

def squaren_size_order(n):
    return np.power(n, 2)

def pow2_size_order(n):
    return np.power(2, n)

def nlogn_size_order(n):
    return n * np.log(n) + 7 * n

if __name__ == '__main__':
    n = np.arange(10, 400)
    plt.plot(n, squaren_size_order(n))
    plt.plot(n, nlogn_size_order(n))
    plt.plot(n, n)
    # plt.plot(n, pow2_size_order(n))
    
    plt.show()