import numpy as np

def nest(c, x):
    n = len(c) - 1
    result = c[n]
    for i in range(n - 1, -1, -1):
        result = result * (x - c[i])
    return result

